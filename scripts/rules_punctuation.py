#!/usr/bin/env python3
"""Remove commas immediately following dice icons in formatted gameplay rules."""
from html.parser import HTMLParser
from pathlib import Path
import argparse
import re

from rules_metadata import refresh, split_metadata


def is_dice_icon(name):
    return (name.endswith('_die.svg') or bool(re.fullmatch(r'die_\d+\.svg', name))
            or name in {'smallstraight.svg', 'largestraight.svg'} or name.startswith('defense_'))


class DiceCommas(HTMLParser):
    def __init__(self, text):
        super().__init__();self.offsets=[0];self.positions=[];self.stack=[];self.skip=0;self.pending_dice=False;self.after_dice=False
        for match in re.finditer('\n',text):self.offsets.append(match.end())
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if self.skip:self.skip+=1;return
        active=self.stack[-1][1] if self.stack else False
        if 'data-source-line' in a:active=a['data-source-line']=='rules';self.after_dice=False
        if a.get('data-icon') and active:
            self.pending_dice=is_dice_icon(a['data-icon']);self.skip=1;return
        if tag not in {'img','br','hr','meta','link'}:self.stack.append((tag,active))
        if tag=='br':self.after_dice=False
    def handle_startendtag(self,tag,attrs):
        if tag=='br':self.after_dice=False
    def handle_endtag(self,tag):
        if self.skip:
            self.skip-=1
            if not self.skip:self.after_dice=self.pending_dice
            return
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i][0]==tag:del self.stack[i:];break
    def handle_data(self,data):
        if self.skip or not self.stack or not self.stack[-1][1]:return
        if self.after_dice:
            match=re.match(r'\s*,',data)
            if match:
                line,column=self.getpos();self.positions.append(self.offsets[line-1]+column+match.end()-1)
                data=data[:match.end()-1]+data[match.end():]
        if data.strip():self.after_dice=False


def remove_dice_commas(body):
    parser=DiceCommas(body);parser.feed(body)
    for index in reversed(parser.positions):
        assert body[index]==','
        body=body[:index]+body[index+1:]
    return body,len(parser.positions)


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('paths',nargs='+',type=Path);args=parser.parse_args()
    for path in args.paths:
        body,_=split_metadata(path.read_text());body,count=remove_dice_commas(body)
        if count:
            path.write_text(body);refresh(path)
        else:refresh(path,check=True)
        print(f'{path}: removed {count} commas immediately after dice icons')


if __name__=='__main__':main()
