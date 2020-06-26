"""
Validate xml file against dtd file

Usage:
    validate_against_dtd.py --naf_path=<naf_path> --naf_dtd_path=<naf_dtd_path>

Options:
    --naf_path=<naf_path> path to NAF file
    --naf_dtd_path=<naf_dtd_path> path to dtd file

Example:
    python validate_against_dtd.py --naf_path="../resources/data-to-text annotation tool/NAF/before/coreference/coreference.naf"\
    --naf_dtd_path="../resources/naf_development/naf_v3.1.dtd"
"""
from docopt import docopt
import sys
import requests
import io

from lxml import etree

# load arguments
arguments = docopt(__doc__)
print()
print('PROVIDED ARGUMENTS')
print(arguments)
print()

def load_dtd_as_file_object(dtd_url=None,
                            dtd_path=None,
                            verbose=0):
    dtd = None


    if dtd_url is not None:
        r = requests.get(dtd_url)

        if r.status_code == 200:
            dtd_file_object = io.StringIO(r.text)
            dtd = etree.DTD(dtd_file_object)

        if verbose >= 1:
            print()
            if dtd is None:
                print(f'failed to load dtd from {dtd_url}')
            else:
                print(f'succesfully loaded dtd from {dtd_url}')

    elif dtd_path is not None:
        with open(dtd_path) as infile:
            dtd = etree.DTD(infile)

        if verbose >= 1:
            print()
            if dtd is None:
                print(f'failed to load dtd from {dtd_path}')
            else:
                print(f'succesfully loaded dtd from {dtd_path}')

    return dtd

def validate_naf_file(dtd, root):
    succes = dtd.validate(root)

    if not succes:
        print()
        print(sys.stderr.write("DTD error log:"))
        for error in dtd.error_log.filter_from_errors():
            sys.stderr.write(str(error))
        raise Exception(f'dtd validation failed. Please inspect stderr.')

    return succes

naf_path = arguments['--naf_path']
dtd_path = arguments['--naf_dtd_path']

dtd = load_dtd_as_file_object(dtd_path=dtd_path, verbose=1)

doc = etree.parse(naf_path)
root = doc.getroot()

validate_naf_file(dtd, root)

print('the DTD validation was a succes!')
