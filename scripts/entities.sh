#!/usr/bin/env bash

# add one entity element
python validate_against_dtd.py \
 --naf_path="../res/data-to-text annotation tool/NAF/before/entity/entity.naf" \
 --naf_v4_dtd_path="../res/naf_development/naf_v4.dtd"
python validate_against_dtd.py \
 --naf_path="../res/data-to-text annotation tool/NAF/after/entity/entity.naf" \
 --naf_v4_dtd_path="../res/naf_development/naf_v4.dtd"
