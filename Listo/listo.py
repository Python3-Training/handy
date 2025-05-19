#!/usr/bin/env python3
'''
Mission: A kwargs demonstration.

File: listo.py (aka: ListBlocks3.py)

State: READY (R.S.C)
'''
import os, os.path, sys


def list_files(zDir, file_type='.py'):
    ''' Return an unsorted list of typed file names in zDir. '''
    if not zDir.endswith(os.path.sep):
        zDir += os.path.sep
    results = list()
    for file in os.listdir(zDir):
        if file.lower().endswith(file_type):
            zFile = zDir + file
            results.append(zFile)
    return results


def reporting(**kwargs):
    '''
Block reporting - a kwargs demonstration.
NEXT: Multiple reporting types / views? Argparse?
    '''
    import re
    ptrn = re.compile(r'^\s*(class|def)\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(', re.MULTILINE)
    
    if 'class' in kwargs:
        ptrn = re.compile(
            r'^\s*class\s+([A-Za-z_][A-Za-z0-9_]*)\s*(\([^\)]*\))?\s*:',
            re.MULTILINE
        )
        
    path = '.'
    if 'path' in kwargs:
        path = kwargs['path']

    file_type = '.py'
    if 'type' in kwargs:
        file_type = kwargs['type']

    for fss, zFile in enumerate(sorted(list_files(path)), 1):           
        with open(zFile) as fh:
            prev_class = 1                  # EDGE: Fix ZeroBased def problem.
            data = str(fh.read())
            zBlocks = ptrn.findall(data)
            print(zFile.split(os.path.sep)[-1])
        if not zBlocks:
            print("\tThere are no blocks.") # EDGE: Confirm there are no blocks.
            continue
        for ss, zBlock in enumerate(zBlocks,0):
            if zBlock[0].startswith('class'):
                prev_class = 0
            if zBlock[0].startswith('def'):
                print('..... ',end='')
            print(f'{fss:02}.{ss + prev_class:02} {zBlock[0]} {zBlock[1]}')
            
    m = sys.argv[0].split(os.path.sep)
    print("\nFile:",m[-1])


if __name__ == '__main__':
    reporting(path=r'C:\Users\ranag\Desktop\TotalPythoneering-main\PyTrek0001000\PyTrek')
