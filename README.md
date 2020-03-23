# NAF version 4 development

The purpose of this repository is to facilitate the development of moving from [NAF](https://github.com/newsreader/NAF) version 3 to NAF version 4.
After completing the development, we will update the [converter from spaCy to NAF](https://github.com/cltl/SpaCy-to-NAF).

## Prerequisites

Python 3.6 was used to create this project. It might work with older versions of Python.
One of the main reasons to move to NAF version 4 is the creation of an annotation tool within the [Dutch FrameNet](http://dutchframenet.nl/) project.
Within this project, we are building a [data-to-text annotation tool](https://github.com/cltl/frame-annotation-tool).

## Python modules
A number of external modules need to be installed, which are listed in **requirements.txt**.
Depending on how you installed Python, you can probably install the requirements using one of following commands:
```bash
pip install -r requirements.txt
```

## Important content
* [Discussion points for NAF version 4](documentation/V4.md)
* [Proposed DTD changes for NAF version 4](resources/naf_development/NAF_version_4_proposed_dtd_changes.md)
* [Current state of DTD NAF version 4](resources/naf_development/naf_v4.dtd)
* [DTD validation of NAF file using Python](scripts/validate_against_dtd.py)

## Contents
* **documentation**: contains documentation, e.g., ideas.
* **resources** contains data, e.g., NAF and JSON files.
* **scripts** contains Python modules

## TODO
* how to access DTD using URI?

## Authors
* **Marten Postma** (m.c.postma@vu.nl)

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details
