# NAF version 4
This document describe the changes in NAF version 4 compared to NAF version 3.
Each header provides information about a change.
* **date**: May 4th, 2020

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

## span

The proposal is to add the following attributes to the **span** element:
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

Version 4
```dtd
<!-- SPAN ELEMENT -->
<!ELEMENT span (target)+>
<!ATTLIST span
          primary CDATA #IMPLIED
		  status CDATA #IMPLIED>
```

## term

The proposal is to add the following attributes to the **term** element:
* phrase_type 

The possible values of **phrase_type** are:
* singleton
* component: part of a multi-word expression
* multi_word: the term is a multi-word.
* idiom: part of an idiom
* compound

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

Version 4

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
          phrase_type CDATA #IMPLIED>
```

## multi-word

The proposal is to remove the following elements:
* span 

The proposal is to add the following elements:
* target 

The proposal is to remove the following attributes:
* id 
* type
* lemma
* pos 
* morphofeat
* netype
* case 
* head 

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

Version 4

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