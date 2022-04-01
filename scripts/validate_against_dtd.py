"""
Validate naf file against dtd
"""
import sys

from lxml import etree


def load_dtd_from_path(path):
    with open(path) as infile:
        return etree.DTD(infile)


def print_error_message(dtd):
    print(dtd.error_log.filter_from_errors()[0])


def validate(naf_path: str, dtd_path: str):
    dtd = load_dtd_from_path(dtd_path)
    doc = etree.parse(naf_path)
    naf = doc.getroot()
    print(f'validating {naf_path} against {dtd_path}...')
    is_valid = dtd.validate(naf)
    if not is_valid:
        print_error_message(dtd)
    else:
        print(' file is valid')
    return is_valid


if __name__ == '__main__':
    validate(sys.argv[1], sys.argv[2])
