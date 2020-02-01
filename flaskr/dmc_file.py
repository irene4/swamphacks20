#!/usr/bin/env python3

import csv
import pathlib
from dmc_type import DmcType
from color import Color


def load(filename : str, dmc_refs : DmcType):
    try:
        with open(filename, newline = '') as rfile:
            reader = csv.reader(rfile)
            # skip header
            next(reader, None)

            try:
                for line in reader:
                    try:
                        dmc_refs.add(dmc_code = line[0], name = line[1], color = Color(line[2]))
                    except (ValueError, IndexError):
                        print('Unable to add object from line', str(reader.line_num))
            except csv.Error as e:
                print('CSV Error reading {}, line {}: {}'.format(filename, reader.line_num, e))
    except FileNotFoundError:
        print('File {} not found; no changes made to input DmcType'.format(filename))

def store(dmc_refs : DmcType, filename : str):
    if not pathlib.Path(filename).exists():
        with open(filename, 'w', newline = '') as hfile:
            header = csv.writer(hfile)
            header.writerow(('DMC Code', 'Name', 'Color'))
    inc = 0
    cur_dmc = DmcType()
    load(filename, cur_dmc)
    with open(filename, 'a', newline = '') as afile:
        writer = csv.writer(afile)
        for dmc_code, data in dictDif(dmc_refs.data, cur_dmc.data).items():
            writer.writerow((dmc_code, data[0], data[1].asHex()))
            inc += 1
    print('{} entries added to {}'.format(str(inc), filename))

def dictDif(newdict : dict, refdict : dict) -> dict:
    """Returns a new dictionary of all the key,value pairs in newdict not present in refdict."""
    ret_dict = {}
    for key, value in newdict.items():
        if key not in refdict:
            ret_dict[key] = value
    return ret_dict
