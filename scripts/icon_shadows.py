"""Remove activation-only halos without changing icon surfaces or text styling."""
import re


def remove_shadow_filters(element):
    shadow_ids={node.get('id') for node in element.iter()
                if node.tag.rsplit('}',1)[-1]=='filter' and
                (re.search(r'shadow|halo',node.get('id',''),re.I) or
                 any(child.tag.rsplit('}',1)[-1]=='feDropShadow' for child in node.iter()))}
    for node in element.iter():
        value=node.get('filter','')
        if any(name in shadow_ids or re.search(r'shadow|halo',name,re.I)
               for name in re.findall(r'url\(#([^)]+)\)',value)):
            node.attrib.pop('filter',None)
        style=node.get('style')
        if style:
            parts=[part for part in style.split(';') if not re.match(r'\s*(?:filter|box-shadow|text-shadow)\s*:',part)]
            node.set('style',';'.join(parts))


def strip_ultimate_activation_shadows(root,title):
    from ultimate_rules import source_layout
    layout=source_layout(root,title);panel=layout['panel'];body=layout['body']
    parents={c:p for p in panel.iter() for c in p}
    body_nodes=set(body.iter());body_ancestors=set();node=body
    while node is not None:
        body_ancestors.add(node);node=parents.get(node)
    for icon in list(panel.iter()):
        if icon in body_nodes or icon.tag.rsplit('}',1)[-1]!='svg':continue
        source=icon.get('data-source') or icon.get('data-vector-source') or icon.get('data-vector-icon') or ''
        if not re.search(r'(?:_die(?:\.svg)?$|(?:small|large)straight\.svg$|defense_)',source):continue
        remove_shadow_filters(icon)
        node=parents.get(icon)
        while node is not None and node not in body_ancestors:
            value=node.get('filter','')
            if re.search(r'shadow|halo',value,re.I):node.attrib.pop('filter',None)
            node=parents.get(node)
