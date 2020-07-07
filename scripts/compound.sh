#!/usr/bin/env bash

export dtd_path="../res/naf_development/naf_v3.1.dtd"

python validate_against_dtd.py \
 --naf_path="../res/data-to-text annotation tool/NAF/before_v31/compound/compound.naf"\
 --naf_dtd_path=$dtd_path
python validate_against_dtd.py \
 --naf_path="../res/data-to-text annotation tool/NAF/after_v31/compound/compound.naf"\
 --naf_dtd_path=$dtd_path
python validate_against_dtd.py \
 --naf_path="../res/data-to-text annotation tool/NAF/after_v31/compound/remove_compound.naf"\
 --naf_dtd_path=$dtd_path