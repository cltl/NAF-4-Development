#!/usr/bin/env bash

#!/usr/bin/env bash

# add one lp element
python validate_against_dtd.py \
 --naf_path="../resources/data-to-text annotation tool/NAF/before/lp/lp.naf" \
 --naf_v4_dtd_path="../resources/naf_development/naf_v4.dtd"
python validate_against_dtd.py \
 --naf_path="../resources/data-to-text annotation tool/NAF/after/lp/lp.naf" \
 --naf_v4_dtd_path="../resources/naf_development/naf_v4.dtd"
