#!/usr/bin/env python3

from color import Color

class DmcType:
    """Container class for DMC data."""

    def __init__(self):
        self.data = {}

    def add(self, *, dmc_code : str, name : str, color : Color):
        self.data[dmc_code] = (name, color)

    def clear(self):
        self.data.clear()

    def getClosest(self, color : Color, limit : int = 10) -> list:
        distsqr = {}
        for key,value in self.data.items():
            distsqr[key] = sum((x-y)**2 for x,y in zip(color.asTuple(),value[1].asTuple()))
        distsort = sorted(distsqr, key=distsqr.get)
        limit = min(len(distsort), limit)
        outlist = []

        for i in range(limit):
            outlist.append((distsort[i], distsqr[distsort[i]]))
        return outlist

    def get(self, key : str) -> tuple:
        return self.data.get(key)
