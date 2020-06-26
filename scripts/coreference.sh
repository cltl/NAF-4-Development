#!/usr/bin/env bash

# coreference of two mentions referring to Incident URI
python validate_against_dtd.py --naf_path="../res/data-to-text annotation tool/NAF/before_v31/coreference/coreference.naf" --naf_dtd_path="../res/naf_development/naf_v3.1.dtd"
python validate_against_dtd.py --naf_path="../res/data-to-text annotation tool/NAF/after_v31/coreference/coreference.naf" --naf_dtd_path="../res/naf_development/naf_v3.1.dtd"
python validate_against_dtd.py --naf_path="../res/data-to-text annotation tool/NAF/after_v31/coreference/update_coreference.naf" --naf_dtd_path="../res/naf_development/naf_v3.1.dtd"
python validate_against_dtd.py --naf_path="../res/data-to-text annotation tool/NAF/after_v31/coreference/deprecate_coreference.naf" --naf_dtd_path="../res/naf_development/naf_v3.1.dtd"