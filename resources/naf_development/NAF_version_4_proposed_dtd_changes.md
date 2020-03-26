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

## coref 

The proposal is to add the following attributes to the **coref** element:
* status

The possible values of **status** are:
* manual: manually added
* system: a language system added the annotation
* deprecated: the coref element is deprecated, i.e., will no longer be used.

Version 3
```dtd 
<!ELEMENT coref (span|externalReferences)+>
<!ATTLIST coref
          id ID #REQUIRED
          type CDATA #IMPLIED>
```

Version 4
```dtd
<!ELEMENT coref (span|externalReferences)+>
<!ATTLIST coref
          id ID #REQUIRED
          status CDATA #REQUIRED
          type CDATA #IMPLIED>
```


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