# NAF version 4 development

NAF (NLP Annotation Format) is an XML format for annotating text documents. Different layers of annotation 
(tokenization, POS tagging, etc.) are represented as standalone annotations in a same document, while information about
the models or *linguistic processors* used to create these annotations are recorded in the document header, together 
with metadata about the document. See example files in `./examples`.

NAF was originally developed as part of the [Newsreader project](http://www.newsreader-project.eu/). Documentation for 
NAF until version 3.1 is hosted in [newsreader/NAF](https://github.com/newsreader/NAF).

This repository presents current NAF development. 

## Version overview
* The [newsreader/NAF](https://github.com/newsreader/NAF) repository documents NAF version 3 as used for the 
[Newsreader project](http://www.newsreader-project.eu/), 
and up to version 3.1.
* Version 3.1 is the first step in further developing NAF for the [Dutch FrameNet](http://dutchframenet.nl/) project, 
for which we are building a [data-to-text annotation tool](https://github.com/cltl/frame-annotation-tool).
* Version 3.2 adds a text-unit element. This was developed for processing [VOC missives](https://github.com/cltl/voc-missives)
 for Clariah+/Text 
* Version 3.3 extends annotations in linguistic-processor elements.
  * The current version is 3.3.1 (`chunk` elements have one and only one `span` sub-element)

The DTD of each version can be found in `./resources/dtd`, version changes are documented in `./doc` and `Changelog.md`.

The files under `./examples` can be validated with the scripts `./scripts/validate_against_dtd.py` (python 3.6+) and 
`./scripts/tests/`. 
You will need to install `lxml` and `pytest` for that:
```python
pip install -r requirements.txt
```
To validate all examples:
```xml
pytest scripts/tests
```

## License
This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details
