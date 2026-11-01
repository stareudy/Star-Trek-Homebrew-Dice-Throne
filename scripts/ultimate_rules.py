#!/usr/bin/env python3
"""Preserve original Ultimate typography while rebuilding effects from rules.md.

Ultimates are independent layouts. Never wrap, center, or shrink their effects
using regular ability-panel defaults. The original disclaimer remains intact.
"""
from __future__ import annotations

import copy
from html.parser import HTMLParser
import math
from pathlib import Path
import re
import xml.etree.ElementTree as ET

SVG = 'http://www.w3.org/2000/svg'
XML = 'http://www.w3.org/XML/1998/namespace'
IDENTITY = (1., 0., 0., 1., 0., 0.)


def multiply(a, b):
    return (a[0]*b[0]+a[2]*b[1], a[1]*b[0]+a[3]*b[1],
            a[0]*b[2]+a[2]*b[3], a[1]*b[2]+a[3]*b[3],
            a[0]*b[4]+a[2]*b[5]+a[4], a[1]*b[4]+a[3]*b[5]+a[5])


def transform(value):
    result = IDENTITY
    for name, arguments in re.findall(r'(\w+)\(([^)]*)\)', value or ''):
        n = [float(v) for v in re.findall(r'[-+]?(?:\d*\.)?\d+(?:[eE][-+]?\d+)?', arguments)]
        if name == 'translate':
            matrix = (1, 0, 0, 1, n[0], n[1] if len(n)>1 else 0)
        elif name == 'scale':
            matrix = (n[0], 0, 0, n[1] if len(n)>1 else n[0], 0, 0)
        elif name == 'matrix' and len(n) == 6:
            matrix = tuple(n)
        elif name == 'rotate':
            c, s = math.cos(math.radians(n[0])), math.sin(math.radians(n[0]))
            matrix = (c, s, -s, c, 0, 0)
            if len(n) == 3:
                matrix = multiply(multiply((1,0,0,1,n[1],n[2]),matrix),(1,0,0,1,-n[1],-n[2]))
        else:
            raise ValueError(f'Unsupported Ultimate layout transform: {name}')
        result = multiply(result, matrix)
    return result


def matrices(root):
    result = {}
    def walk(node, parent):
        result[node] = multiply(parent, transform(node.get('transform')))
        for child in node:
            walk(child, result[node])
    walk(root, IDENTITY)
    return result


def font_size(node):
    return float(re.search(r'[\d.]+', node.get('font-size', '0')).group())


def source_layout(root, title):
    parents = {c:p for p in root.iter() for c in p}
    stem = re.sub(r'\s*\(ULTIMATE\)$', '', title).lower().replace('!', '').replace(' ', '-')
    panel = next(e for e in root.iter() if e.get('id') == 'panel-'+stem)
    ctm = matrices(root)
    texts = [e for e in panel.iter() if e.tag == f'{{{SVG}}}text' and 'Avenir' in e.get('font-family','')]
    sizes = {e:font_size(e)*math.hypot(ctm[e][0],ctm[e][1]) for e in texts}
    largest = max(sizes.values())
    effects = [e for e in texts if abs(sizes[e]-largest)<.001]
    ancestor_paths = []
    for text in effects:
        chain = []; node = text
        while node is not panel:
            chain.insert(0,node);node=parents[node]
        ancestor_paths.append(chain)
    common = panel
    for nodes in zip(*ancestor_paths):
        if all(e is nodes[0] for e in nodes):common=nodes[0]
        else:break
    if common.tag != f'{{{SVG}}}g':
        common = parents[common]
    if any(parents[t] is not common for t in effects):
        raise ValueError('Ultimate effects text uses unsupported mixed nested transforms; do not guess')
    first = effects[0]
    baselines = {round(float(e.get('y')),5) for e in effects}
    if len(baselines) != 1:
        raise ValueError('Original Ultimate effects are not a single line')
    disclaimers = [e for e in texts if e not in effects]
    return {'panel':panel,'body':common,'texts':effects,'first':first,
            'effective_size':largest,'local_size':font_size(first),
            'disclaimers':disclaimers,'disclaimer_sizes':[sizes[e] for e in disclaimers]}


def _style(text):
    return dict(pair.strip().split(':',1) for pair in (text or '').split(';') if ':' in pair)


class UltimateMarkdown(HTMLParser):
    def __init__(self):
        super().__init__();self.stack=[];self.rules={};self.skip=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if self.skip:self.skip+=1;return
        frame=dict(self.stack[-1]) if self.stack else {'rule':None,'role':None,'style':{}}
        frame['tag']=tag
        frame['style']={**frame['style'],**_style(a.get('style'))}
        if a.get('data-rule'):
            frame['rule']=a['data-rule'] if a['data-rule'].endswith('(ULTIMATE)') else None
            if frame['rule']:self.rules[frame['rule']]={'activation':[],'effects':[],'disclaimer':[]}
        if a.get('data-ultimate-role'):frame['role']=a['data-ultimate-role']
        if a.get('data-icon') and frame['rule'] and frame['role']:
            self.rules[frame['rule']][frame['role']].append({'kind':'icon','name':a['data-icon'],'value':a.get('data-value')})
            self.skip=1;return
        if tag not in ['br','img']:self.stack.append(frame)
        elif tag=='br' and frame['role']=='effects':raise ValueError('Ultimate effects must remain on one line')
    def handle_startendtag(self,tag,attrs):
        if tag=='br':
            frame=self.stack[-1] if self.stack else {}
            if frame.get('role')=='effects':raise ValueError('Ultimate effects must remain on one line')
    def handle_endtag(self,tag):
        if self.skip:self.skip-=1;return
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i]['tag']==tag:del self.stack[i:];break
    def handle_data(self,text):
        if not self.skip and self.stack:
            f=self.stack[-1]
            if f['rule'] and f['role']:
                self.rules[f['rule']][f['role']].append({'kind':'text','text':text,'style':f['style']})


def parse_ultimates(markdown):
    parser=UltimateMarkdown();parser.feed(markdown);return parser.rules


def _icon_name(node):
    reference=node.get('data-source') or node.get('data-vector-source') or node.get('data-vector-icon') or ''
    name=Path(reference).name
    return name if name.endswith('.svg') else name+'.svg' if name else None


def rebuild_ultimate(root, markdown, title, widths):
    layout=source_layout(root,title);rule=parse_ultimates(markdown)[title]
    body=layout['body'];first=layout['first'];baseline=float(first.get('y'));x=float(first.get('x'))
    original_icons={_icon_name(e):e for e in body.iter() if e.tag==f'{{{SVG}}}svg' and _icon_name(e)}
    templates=copy.deepcopy(original_icons)
    y_offsets={};source_ends=[]
    # Current approved Ultimate icons use translation-only wrappers inside their
    # effects line. Preserve each icon's own size and baseline offset exactly.
    parents={c:p for p in body.iter() for c in p}
    for name,icon in original_icons.items():
        node=parents[icon];relative=IDENTITY
        while node is not body:
            local=transform(node.get('transform'))
            if abs(local[0]-1)>.00001 or abs(local[3]-1)>.00001 or abs(local[1])+abs(local[2])>.00001:
                raise ValueError('Unsupported scaled icon wrapper in Ultimate; do not guess')
            relative=multiply(local,relative);node=parents[node]
        y_offsets[name]=float(icon.get('y','0'))+relative[5]-baseline
        source_ends.append(float(icon.get('x','0'))+relative[4]+float(icon.get('width')))
    def measure(value, size):
        total=0.;table=widths['normal']
        for word in re.findall(r'\s+|\S+', value):
            if word.isspace():total+=size*table[' ']
            elif word in table:total+=size*table[word]
            else:raise ValueError(f'Missing exact Chrome text measurement for {word!r}')
        return total
    source_ends.extend(float(e.get('x'))+measure(''.join(e.itertext()),font_size(e)) for e in layout['texts'])
    original_end=max(source_ends)
    items=rule['effects']
    if not items:raise ValueError('Missing Ultimate effects in rules.md')
    for child in list(body):body.remove(child)
    body.text=None
    body.set('data-md-ultimate','effects');body.set('data-layout','single-line-rules')
    body.set('data-source-effective-font-size',str(layout['effective_size']))
    size=layout['local_size'];index=0
    for item in items:
        if item['kind']=='text':
            value=re.sub(r'\s+',' ',item['text'])
            if not value:continue
            attributes={k:v for k,v in first.attrib.items() if k not in ['id','x','y']}
            attributes.update(x=str(x),y=str(baseline),**{'text-anchor':'start','data-md-ultimate-text':'true','font-size':str(size)})
            if item.get('style',{}).get('color'):attributes['fill']=item['style']['color']
            ET.SubElement(body,f'{{{SVG}}}text',attributes).text=value
            x+=measure(value,size)
        else:
            name=item['name']
            if name not in templates:raise ValueError(f'New Ultimate icon needs an explicit layout template: {name}')
            icon=copy.deepcopy(templates[name]);index+=1
            ids={e.get('id'):f'md-ultimate-{index}-'+e.get('id') for e in icon.iter() if e.get('id')}
            for e in icon.iter():
                for key,value in list(e.attrib.items()):
                    if key=='id':e.set(key,ids[value]);continue
                    for old,new in ids.items():value=value.replace('url(#'+old+')','url(#'+new+')')
                    if key in ['aria-labelledby','aria-describedby']:value=' '.join(ids.get(v,v) for v in value.split())
                    e.set(key,value)
                if e.get('data-editable')=='number' and item['value'] is not None:e.text=item['value']
            icon.set('x',str(x));icon.set('y',str(baseline+y_offsets[name]));icon.set('data-md-icon',name)
            if item['value'] is not None:icon.set('data-md-value',item['value'])
            body.append(icon);x+=float(icon.get('width'))
    if x>original_end+.001:
        raise ValueError('Ultimate wording exceeds the original single-line width; explicit layout review is required, not automatic wrapping or shrinking')
    from icon_shadows import strip_ultimate_activation_shadows
    strip_ultimate_activation_shadows(root,title)
    # Disclaimer elements, their wrapping, source transforms, and activation
    # dice geometry is retained from the original panel; activation shadows are omitted.
    return {'title':title,'effects_effective_font_size':layout['effective_size'],
            'disclaimer_effective_font_sizes':layout['disclaimer_sizes'],
            'local_start':float(first.get('x')),'local_end':x,'baseline':baseline}


def main():
    import argparse
    import hashlib
    import json
    from rules_metadata import load_icon_inventory
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--hero',choices=['Janeway','Tuvok','all'],default='all')
    parser.add_argument('--measurements',type=Path,required=True,help='Fresh Chrome canvas measurements JSON')
    parser.add_argument('--write-mdtest',action='store_true',help='Write only hero_board_mdtest.svg copies')
    args=parser.parse_args()
    root_dir=Path(__file__).resolve().parents[1]
    widths=json.loads(args.measurements.read_text())['widths']
    ET.register_namespace('',SVG)
    heroes=['Janeway','Tuvok'] if args.hero=='all' else [args.hero]
    pending=[]
    for hero in heroes:
        hero_dir=root_dir/'Heroes'/hero;md=hero_dir/'rules.md';load_icon_inventory(md)
        original_path=hero_dir/'hero_board.svg';original_bytes=original_path.read_bytes()
        original=ET.fromstring(original_bytes)
        title=next(iter(parse_ultimates(md.read_text())))
        source=source_layout(original,title)
        destination=hero_dir/'hero_board_mdtest.svg'
        current_bytes=destination.read_bytes() if destination.exists() else original_bytes
        working=ET.fromstring(current_bytes)
        parents={c:p for p in working.iter() for c in p}
        previous=next(e for e in working.iter() if e.get('id')==source['panel'].get('id'))
        parent=parents[previous];index=list(parent).index(previous)
        parent.remove(previous);parent.insert(index,copy.deepcopy(source['panel']))
        report=rebuild_ultimate(working,md.read_text(),title,widths)
        rebuilt=source_layout(working,title)
        assert abs(rebuilt['effective_size']-source['effective_size'])<.00001
        assert [ET.tostring(e) for e in rebuilt['disclaimers']]==[ET.tostring(e) for e in source['disclaimers']]
        assert working.attrib==original.attrib
        # Everything outside the Ultimate is retained from the current test copy.
        before=ET.fromstring(current_bytes);after=copy.deepcopy(working)
        for tree in [before,after]:
            panel=next(e for e in tree.iter() if e.get('id')==source['panel'].get('id'));panel.clear()
        assert ET.tostring(before)==ET.tostring(after)
        assert hashlib.sha256(original_path.read_bytes()).digest()==hashlib.sha256(original_bytes).digest()
        pending.append((destination,ET.tostring(working,encoding='utf-8',xml_declaration=True)))
        print(hero,json.dumps(report))
    if args.write_mdtest:
        for destination,data in pending:
            destination.write_bytes(data);ET.parse(destination)
            print('Saved',destination)


if __name__=='__main__':
    main()
