#!/usr/bin/env python3
'''
Mission: A kwargs demonstration.

File: listo.py (aka: ListBlocks3.py)

State: Lightly Tested
'''
import os, os.path, sys
import argparse


version = 0.2


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
        print(f'{fss:02}.{ss + prev_class:02} {zBlock[0]} {zBlock[1]}')


def view_classy(zBlocks:list):
    ''' View the classes, only. '''
    for zBlock in zBlocks:
        if zBlock[0].startswith('def'):
            continue
        print(f'class {zBlock[0]} {zBlock[1]}')


def reporting(**kwargs)->bool:
    '''
Block reporting - a kwargs demonstration.
NEXT: Multiple reporting types / views? Argparse?
    '''
    import re
    ptrn = re.compile(r'^\s*(class|def)\s+([A-Za-z_][A-Za-z0-9_]*)\s*(\([^\)]*\))?\s*:', re.MULTILINE)

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

    file_type = '.py'
    if 'type' in kwargs:
        file_type = kwargs['type']

    print(f'***** {view} VIEW OF {path} *****')

    fss = 0
    big_block = []
    for zFile in sorted(list_files(path)):
        with open(zFile) as fh:
            data = str(fh.read())
            zBlocks = fix_blocks(ptrn.findall(data))
            aFile = zFile.split(os.path.sep)[-1]
            fss += 1
            match(view):
                case 100: # manifest view
                    if not zBlocks:
                        print(f"{fss:02}.00 {aFile}\n\tThere are no blocks.\n")
                        continue
                    print(f'{fss:02}.00 {aFile}')
                    view_file(fss, zBlocks)
                    print()
                case 200: # classy view
                    big_block.extend(zBlocks)

    # classy
    if zBlocks:
        view_classy(sorted(big_block, key=lambda a: a[0].lower()))
    return True


def valid_directory(path:str)->bool:
    ''' See if the past is on the file system. '''
    if path is None:
        return None
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(f"'{path}' is not a valid directory.")
    return os.path.abspath(path)


def main():
    parser = argparse.ArgumentParser(description="Use path to code. Default is `pwd.`")
    parser.add_argument(
        '--path', 
        type=valid_directory, 
        default='.', 
        help='Path to a directory to verify (optional).'
    )
    parser.add_argument(
        '--class',
        dest='class',
        default=None,
        action=argparse.BooleanOptionalAction,
        help='Class only (default: True). Use "--no-class" for full detail.'
    )
    parser.add_argument(
        '--view',
        dest='view',
        default='manifest',
        help='View type (default: "manifest"). Use "classy" for fewer details.'
    )

    args = vars(parser.parse_args())

    if 'class' in args:
        if not args['class']:
            del args['class']

    reporting(**args)
    print(f"Effect: {str(args)}")

class foo: # edge
    pass

class bar():
    pass

if __name__ == '__main__':
    main()
    print(f"\nLISTO {version}. File:", sys.argv[0])
