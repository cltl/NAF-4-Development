# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## v3.3
* Date: June 7, 2022
* Authors: Sophie Arnoult (s.i.arnoult@vu.nl)
### Added

* `lpDependency` element 
* `id` attribute to `lp` element

### Changed

* `lp` element accepts `lpDependency` children and `id` attribute
* restrict element declaration of: `causalRelations`, `component`, `coref`, `entity`, `externalRef`, `mark`, `mw`, `opinion`,
`opinion_expression`, `opinion_holder`, `opinion_target`, `predicate`, `role`, `statement`, `term`, `wf`


### Removed

* `factualityLayer` element

## v3.2
* Date: January 19, 2021
* Author: Sophie Arnoult (s.i.arnoult@vu.nl)

#### Added

* `tunits` layer and `tunit` element


## v3.1 
* Date: June 26nd, 2020
* Authors: Piek Vossen (piek.vossen@vu.nl), Antske Fokkens (antske.fokkens@vu.nl) and Marten Postma (m.c.postma@vu.nl)

#### Added

* `subtoken` element
* `multiwords` layer and `mw` elements

#### Changed

* `wf` element accepts `subtoken` children
* `entity` element directly accepts `span` child; attribute `type` becomes optional
* `predicate` element loses `uri` attribute
* `role` element loses `uri` attribute
* `span` element accepts `status` attribute
* `term` element accepts `component_of` and `compound_type` attributes
* `externalRef` element accepts `timestamp` attribute

