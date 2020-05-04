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
* [NAF version 4](doc/NAF_version_4.md)
* [DTD NAF version 4](res/naf_development/naf_v4.dtd)
* [DTD validation of NAF file using Python](scripts/validate_against_dtd.py)
* [Discussion points for future development of NAF](doc/NAF_discussion_document.md)

## Contents
* **doc**: contains documentation
* **res** contains data, e.g., DTD, NAF and JSON files.
* **scripts** contains Python modules

## Authors
* **Marten Postma** (m.c.postma@vu.nl)

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details
