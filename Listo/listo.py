#!/usr/bin/env python3
'''
Mission: A kwargs demonstration.

File: listo.py (aka: ListBlocks3.py)

State: READY (R.S.C)
'''
import os, os.path, sys

version = 0.1


views = {'manifest' : [100,'Include file names'],
         'classy'   : [200,'Class names only']
         }


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

def fix_blocks(zBlocks:list)->list:
    ''' Fix parser results. '''
    results = list()
    for block in zBlocks:
        row = list(block)
        if not row[1]:
            row[1] = '()'
        results.append(row)
    return results

def view_file(fss:int, zBlocks:list):
    ''' View the classic manifest. '''
    prev_class = 1
    for ss, zBlock in enumerate(zBlocks):
        if zBlock[0].startswith('class'):
            prev_class = 0
        if zBlock[0].startswith('def'):
            print('..... ',end='')
        print(f'{fss:02}.{ss + prev_class:02} {zBlock[0]}{zBlock[1]}')


def view_classy(zBlocks:list):
    ''' View the clsses, only. '''
    for zBlock in zBlocks:
        if zBlock[0].startswith('def'):
            continue
        print(f'class {zBlock[0]}{zBlock[1]}')


def reporting(**kwargs):
    '''
Block reporting - a kwargs demonstration.
NEXT: Multiple reporting types / views? Argparse?
    '''
    import re
    ptrn = re.compile(r'^\s*(class|def)\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(', re.MULTILINE)

    view = views['manifest'][0]
    if 'view' in kwargs:
        mode = kwargs['view']
        if mode in views:
            print(f'***** A "{mode.upper()}" VIEW *****')
            view = views[mode][0]
        else:
            print(f"Warning: View '{mode}' is not supported.")
    
    if 'class' in kwargs:
        ptrn = re.compile(
            r'^\s*class\s+([A-Za-z_][A-Za-z0-9_]*)\s*(\([^\)]*\))?\s*:',
            re.MULTILINE
        )
        
    path = '.'
    if 'path' in kwargs:
        path = kwargs['path']
    print(f'***** OF {path} *****')

    file_type = '.py'
    if 'type' in kwargs:
        file_type = kwargs['type']

    fss = 0
    big_block = []
    for zFile in sorted(list_files(path)):
        with open(zFile) as fh:
            data = str(fh.read())
            zBlocks = fix_blocks(ptrn.findall(data))
            aFile = zFile.split(os.path.sep)[-1]
            fss += 1
            match(view):
                case 100:
                    if not zBlocks:
                        print(f"{fss:02}.00 {aFile}\n\tThere are no blocks.\n")
                        continue
                    print(f'{fss:02}.00 {aFile}')
                    view_file(fss, zBlocks)
                    print()
                case 200:
                    big_block.extend(zBlocks)

    for zBlock in sorted(big_block, key=lambda a: a[0].lower()):
        print(f'{zBlock[0]}{zBlock[1]}')



if __name__ == '__main__':
    params = dict()
    params['path'] = r'C:\Users\ranag\Desktop\TotalPythoneering-main\PyTrek0001000\PyTrek'
    params['class'] = None
    for view in views:        
        params['view'] = view
        reporting(**params)
    print(f"\nLISTO {version}. File:", sys.argv[0])
