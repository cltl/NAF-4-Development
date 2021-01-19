#!/usr/bin/env bash

export dtd_path="../res/naf_development/naf_v3.2.dtd"

python validate_against_dtd.py \
 --naf_path="../res/data-to-text annotation tool/NAF/after_v32/tunits/tunits.naf" \
 --naf_dtd_path=$dtd_path
