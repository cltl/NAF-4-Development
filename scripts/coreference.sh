#!/usr/bin/env bash

# coreference of two mentions referring to Incident URI
python validate_against_dtd.py --naf_path="../resources/data-to-text annotation tool/NAF/before/coreference/coreference.naf" --naf_v4_dtd_path="../resources/naf development/naf_v4.dtd"
python validate_against_dtd.py --naf_path="../resources/data-to-text annotation tool/NAF/after/coreference/coreference.naf" --naf_v4_dtd_path="../resources/naf development/naf_v4.dtd"