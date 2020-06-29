# NAF version 3.1
This document describe the changes in NAF version 3.1 compared to NAF version 3.
Each header provides information about a change.
* **date**: June 26nd, 2020

## Team
the following researchers contributed to this NAF version:
* Piek Vossen (piek.vossen@vu.nl)
* Antske Fokkens (antske.fokkens@vu.nl)
* Marten Postma (m.c.postma@vu.nl)

## subtoken
We introduce a **subtoken** element which is a child of a wf element.
The goal is to represent a subtoken of a word form element, typically used to represent compounds.
The syntax of the id is TOKEN_ID.SUBTOKEN_ID, e.g., "w1.sub1", "w2.sub2", etc.

```dtd
<!ELEMENT subtoken (#PCDATA)>
<!ATTLIST subtoken
          id ID #REQUIRED
          offset CDATA #REQUIRED
          length CDATA #REQUIRED>
```

## wf
A subtoken is a child of a wf element, which is why the definition of the
wf element has changed:

NAF version 3.0
```dtd
<!ELEMENT wf (#PCDATA)>
```

NAF version 3.1
```dtd
<!ELEMENT wf (#PCDATA|subtoken)*>
```

## entity
In NAF version 3, an `entities/entity` element had a child called `references`.
The `references` element has been removed.
Instead, `span` is now directly a child of `entities/entity`

The `type` attribute of an `entities/entity` element is now optional.

## predicate
The **uri** is removed from a **predicate** element.

## role
Similarly, the role element values are defined in the externalReferences element in version 3.1
and no longer in the semRole attribute of the role element.

3.0 
```
<!ELEMENT role (externalReferences|span)+>
<!ATTLIST role
          id ID #REQUIRED
          uri CDATA #IMPLIED
          confidence CDATA #IMPLIED
          semRole CDATA #REQUIRED>
```

3.1
```
<!ELEMENT role (externalReferences|span)+>
<!ATTLIST role
          id ID #REQUIRED
          confidence CDATA #IMPLIED
		  status CDATA #IMPLIED>
```

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
* `srl/predicate/role`
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

## component
A component element has not been changed, but we highlight the following naming convention:

If the component is part of a multiword, i.e., a multiwords/mw element, the syntax for the identifier is MW_ID.C_ID
e.g., mw1.c1 and mw1.c2 for the two components of the multiwords/mw element with the identifier mw1.
If the component is part of a compound, i.e., a terms/term element, the syntax for the identifier is T_ID.C_ID
e.g., t1.c1 and t1.c2 for the two components of the terms/term element with the identifier t1.

## term
The following attributes have been added to the **term** element:
* component_of 
* compound_type

If the term is part of a multiword, i.e., there is a multiword/mw element
that makes reference to it, then the **component_of** attribute can be used to 
make reference to the specific multiword.

The possible values of **compound_type** are:
* endocentric: endocentric compound
* exocentric: exocentric compoud

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
          component_of IDREF #IMPLIED
          compound_type CDATA #IMPLIED>
```

## multiwords
Multiword expression are represented in the **multiwords** layer.
Multi-word terms only have a **component** child in version 3.0.
This component element can have multiple **target** elements,
each referring to a component of the multi-word expression.

```
<!-- MULTIWORDS ELEMENT -->
<!ELEMENT multiwords (mw)+>

<!-- MW ELEMENT -->
<!--
    attributes of mw elements

    id: unique identifier (REQUIRED AND UNIQUE)

    lemma: lemma of the term (IMPLIED).

    pos: part of speech. (IMPLIED)

    morphofeat: morphosyntactic feature encoded as a single attribute. (IMPLIED)

    case: declension case (IMPLIED)

    type: phrasal, idiom
  -->

<!ELEMENT mw (component|externalReferences)+>
<!ATTLIST mw
          id ID #REQUIRED
          lemma CDATA #IMPLIED
          pos CDATA #IMPLIED
		  morphofeat CDATA #IMPLIED
		  case CDATA #IMPLIED
		  type CDATA #REQUIRED>
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
```

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
```