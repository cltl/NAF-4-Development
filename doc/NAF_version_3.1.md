# NAF version 3.1 
This document describe the changes in NAF version 3.1 compared to NAF version 3.
Each header provides information about a change.
* **date**: May 25th, 2020

## Team
the following researchers contributed to this NAF version:
* Piek Vossen (piek.vossen@vu.nl)
* Antske Fokkens (antske.fokkens@vu.nl)
* Marten Postma (m.c.postma@vu.nl)

## entity
In NAF version 3, an `entities/entity` element had a child called `references`.
The `references` element has been removed.
Instead, `span` is now directly a child of `entities/entity`

The `type` attribute of an `entities/entity` element is now optional.


## predicate

The **uri** is removed from a **predicate** element.

## span

The following attribute is added to the **span** element:
* status 

The possible values of **status** are:
* manual: manually added
* system: a language system added the annotation
* deprecated: the element is deprecated

We added this attribute to the following elements:
* `entities/entity`
* `srl/predicate`
* `coref`
* `coref/span`

Version 3
```dtd
<!-- SPAN ELEMENT -->
<!ELEMENT span (target)+>
<!ATTLIST span
          primary CDATA #IMPLIED>
```

Version 3.1
```dtd
<!-- SPAN ELEMENT -->
<!ELEMENT span (target)+>
<!ATTLIST span
          primary CDATA #IMPLIED
		  status CDATA #IMPLIED>
```

## term

The following attributes have been added to the **term** element:
* phrase_type 
* ud_rel

The possible values of **phrase_type** are:
* component: the term is part of a multi-word expression
* singleton: term consisting of a one single token
* multi_word: part of a multi-word expression

The possible values of **ud_rel** are:
* compound:prt: the term is a phrasal verb.
* compound: the term is a compound

Version 3
```dtd
<!ATTLIST term
          id ID #REQUIRED
          type CDATA #IMPLIED
          lemma CDATA #IMPLIED
          pos CDATA #IMPLIED
          morphofeat CDATA #IMPLIED
          netype CDATA #IMPLIED
          case CDATA #IMPLIED
          head CDATA #IMPLIED
```

Version 3.1

```dtd
<!ATTLIST term
          id ID #REQUIRED
          type CDATA #IMPLIED
          lemma CDATA #IMPLIED
          pos CDATA #IMPLIED
          morphofeat CDATA #IMPLIED
          netype CDATA #IMPLIED
          case CDATA #IMPLIED
          head CDATA #IMPLIED
          phrase_type CDATA #IMPLIED
          ud_rel CDATA #IMPLIED>
```

## multi-word
Multi-word terms only have a **component** child in version 3.1.
This component element can have multiple **target** elements,
each referring to a component of the multi-word expression.

Version 3
```dtd 

<!ELEMENT component (sentiment?|span|externalReferences)+>
<!ATTLIST component
          id ID #REQUIRED
          type CDATA #IMPLIED
          lemma CDATA #IMPLIED
          pos CDATA #IMPLIED
          morphofeat CDATA #IMPLIED
          netype CDATA #IMPLIED
          case CDATA #IMPLIED
          head CDATA #IMPLIED>
```

Version 3.1

```dtd 

<!ELEMENT component (target|sentiment?|externalReferences)+>
<!ATTLIST component>
```

## externalRef

We added the following attributes to the `externalReferences/externalRef` element:
* timestamp: timestamp of adding externalRef

Version 3
```dtd
<!ELEMENT externalRef (sentiment|externalRef)*>
<!ATTLIST externalRef
          resource CDATA #IMPLIED
          reference CDATA #REQUIRED
          reftype CDATA #IMPLIED
          status CDATA #IMPLIED
          source CDATA #IMPLIED
          confidence CDATA #IMPLIED>```

Version 3.1
```dtd
<!ELEMENT externalRef (sentiment|externalRef)*>
<!ATTLIST externalRef
          resource CDATA #IMPLIED
          reference CDATA #REQUIRED
          reftype CDATA #IMPLIED
          status CDATA #IMPLIED
          source CDATA #IMPLIED
          confidence CDATA #IMPLIED
		  timestamp CDATA #IMPLIED>