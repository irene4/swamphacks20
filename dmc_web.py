#!/usr/bin/env python3

import requests
import lxml.html
from dmc_type import DmcType
from color import Color

path = ['body', 'table', 'tbody', 'tr', 'td']

def __get(element) -> str:
    if len(element.findall('font')) == 0:
        return ' '.join(element.find('p').findtext('font').split())
    else:
        return ' '.join(element.findtext('font').split())

def parse(url : str, dmc : DmcType, alt : bool = False):
    html = requests.get(url)
    doc = lxml.html.fromstring(html.content)
    ele = doc
    if alt:
        ele = ele.find(path[0])
        ele = ele.findall(path[1])[1]
        for p in path[2:]:
            ele = ele.find(p)
    else:
        for p in path:
            ele = ele.find(p)

    realt = None
    for table in ele.findall('table'):
        for item in table.items():
            if(item[0] == 'cellspacing'):
                if(item[1] == '1'):
                    realt = table.find('tbody')
                break
    for tr in realt:
        try:
            if len(tr.find('td').find('font').findall('b')) != 0:
                continue
        except AttributeError:
            pass
        tds = tr.findall('td')
        if len(tds) >= 3:
            code0 = __get(tds[0])
            name0 = __get(tds[1])
            col0 = Color(tds[2].items()[0][1])
            dmc.add(dmc_code = code0, name = name0, color = col0)
            if len(tds) >= 6:
                code1 = __get(tds[3])
                name1 = __get(tds[4])
                col1 = Color(tds[5].items()[0][1])
                dmc.add(dmc_code = code1, name = name1, color = col1)
