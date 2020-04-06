# Proposed dtd changes NAF version 4

## span

The proposal is to add the following attributes to the **span** element:
* status 

The possible values of **status** are:
* manual: manually added
* system: a language system added the annotation
* deprecated: the coref element is deprecated, i.e., will no longer be used.

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
* idiom
* [TO DISCUSS] compound

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

## Multi-word

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

DISCUSSION: represent head as term attribute, e.g., "head IDREF #IMPLIED"?
 
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

## the status attribute

The proposal is to add the following attributes to the **coref** element:
* status

The possible values of **status** are:
* manual: manually added
* system: a language system added the annotation
* deprecated: the coref element is deprecated, i.e., will no longer be used.

We add this attribute to at least the following elements:
* entities/entity
* srl/predicate
* coref
* coref/span

TODO: to how many elements do we want to add this?

## externalRef

The proposal is to add the following attributes to the **externalRef** element:
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