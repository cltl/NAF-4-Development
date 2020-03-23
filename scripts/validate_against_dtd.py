"""
Validate xml file against dtd file

Usage:
    validate_against_dtd.py --naf_path=<naf_path> --naf_v4_dtd_path=<naf_v4_dtd_path>

Options:
    --naf_path=<naf_path> path to NAF file (<!DOCTYPE NAF SYSTEM "naf_v4.dtd"> should be on second line of NAF file)
    --naf_v4_dtd_path=<naf_v4_dtd_path> path to dtd file

Example:
    python validate_against_dtd.py --naf_path="../resources/data-to-text annotation tool/NAF/before/coreference/coreference.naf"\
    --naf_v4_dtd_path="../resources/naf development/naf_v4.dtd"
"""
from docopt import docopt
import os
import shutil

from lxml import etree

# load arguments
arguments = docopt(__doc__)
print()
print('PROVIDED ARGUMENTS')
print(arguments)
print()

module_dir = os.path.dirname(os.path.realpath(__file__))


naf_path = arguments['--naf_path']
dtd_path = arguments['--naf_v4_dtd_path']

shutil.copy(dtd_path, module_dir)

parser = etree.XMLParser(dtd_validation=True)
tree = etree.parse(naf_path, parser)

print('the DTD validation was a succes!')
