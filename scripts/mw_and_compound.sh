#!/usr/bin/env bash
export dtd_path="../res/naf_development/naf_v4.dtd"

python validate_against_dtd.py \
 --naf_path="../res/data-to-text annotation tool/NAF/before/mw_and_compounds/phrasal_verb.naf"\
 --naf_v4_dtd_path=$dtd_path
python validate_against_dtd.py \
 --naf_path="../res/data-to-text annotation tool/NAF/after/mw_and_compounds/phrasal_verb.naf"\
 --naf_v4_dtd_path=$dtd_path

