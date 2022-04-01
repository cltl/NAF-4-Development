# Spec changes
This document lists changes in element specifications from NAF 3.2 to 3.3
* **date**: June 7, 2022
* **author**: Sophie Arnoult (s.i.arnoult@vu.nl)

## Remove FactualityLayer

v3.3
```html
<!ELEMENT NAF (nafHeader|raw|topics|text|terms|multiwords|deps|chunks|entities|coreferences|constituency|srl|opinions|timeExpressions|tunits|locations|dates|temporalRelations|causalRelations|markables|attribution|factualities)*>
```

v3.2
```html
<!ELEMENT NAF (nafHeader|raw|topics|text|terms|multiwords|deps|chunks|entities|coreferences|constituency|srl|opinions|timeExpressions|factualitylayer|tunits|locations|dates|temporalRelations|causalRelations|markables|attribution|factualities)*>

<!ELEMENT factualitylayer (factvalue)+>
<!ELEMENT factvalue EMPTY>
<!ATTLIST factvalue
          id IDREF #REQUIRED
          prediction CDATA #REQUIRED
          confidence CDATA #IMPLIED>
```

## Add lpDependency elements to lp elements
v3.3
```html
<!ELEMENT lp (lpDependency)+>
<!-- LPDEPENDENCY ELEMENT -->
<!-- <lpDependency> elements describe tool/data/model dependencies of linguistic processors.
	Attributes:
		- name: name of the dependency
		- version: version of the dependency
		- type: type of the dependency, e.g., 'tool', 'data', 'model'
	-->
<!ELEMENT lpDependency (EMPTY)>
<!ATTLIST lpDependency
		name CDATA #REQUIRED
		version CDATA #IMPLIED
		type CDATA #IMPLIED>
```

v3.2
```html
<!ELEMENT lp EMPTY>
```

## Add 'id' attribute to lp elements
v3.3
```html
<!ATTLIST lp
          name CDATA #REQUIRED
          version CDATA #REQUIRED
          timestamp CDATA #IMPLIED
          beginTimestamp CDATA #IMPLIED
          endTimestamp CDATA #IMPLIED
          hostname CDATA #IMPLIED
		  id CDATA #IMPLIED>
```

v3.2
```html
<!ATTLIST lp
          name CDATA #REQUIRED
          version CDATA #REQUIRED
          timestamp CDATA #IMPLIED
          beginTimestamp CDATA #IMPLIED
          endTimestamp CDATA #IMPLIED
          hostname CDATA #IMPLIED>
```
 
## Restricted element specifications
### wf elements
v3.3
```html
<!ELEMENT wf (#PCDATA,subtoken*)>
```

v3.2
```html
<!ELEMENT wf (#PCDATA|subtoken)*>
```

### terms
v3.3
```html
<!ELEMENT term (span,component*,externalReferences?,sentiment?)>
```
v3.2
```html
<!ELEMENT term (sentiment?|span|externalReferences|component)+>
```

### mw elements (multiwords)
v3.3
```html
<!ELEMENT mw (component+,externalReferences?)>
```
v3.2
```html
<!ELEMENT mw (component|externalReferences)+>
```
### externalRef elements
v3.3
```html
<!ELEMENT externalRef (sentiment?,externalRef*)>
```
v3.2
```html
<!ELEMENT externalRef (sentiment|externalRef)*>
```
### Components
v3.3
```html
<!ELEMENT component ((span,sentiment?,externalReferences?)
                    |(span,externalReferences?,sentiment?))>
```
v3.2
```html
<!ELEMENT component (sentiment?|span|externalReferences)+>
```
### Mark elements
v3.3
```html
<!ELEMENT mark ((span,sentiment?,externalReferences?)
	       |(span,externalReferences?,sentiment?))>
```
v3.2
```html
<!ELEMENT mark (sentiment?|span|externalReferences)+>
```
### Entities
v3.3
```html
<!ELEMENT entity (span,externalReferences?)>
```
v3.2
```html
<!ELEMENT entity (span|externalReferences)+>
```
### Coref elements
v3.3
```html
<!ELEMENT coref (span+,externalReferences?)>
```
v3.2
```html
<!ELEMENT coref (span|externalReferences)+>
```
### Predicates
v3.3
```html
<!ELEMENT predicate ((span,externalReferences?,role*)
       		    |(span,role*,externalReferences?))>
```
v3.2
```html
<!ELEMENT predicate (externalReferences|span|role)+>
```
### Roles
v3.3
```html
<!ELEMENT role (span,externalReferences?)>
```
v3.2
```html
<!ELEMENT role (externalReferences|span)+>
```
### Opinions
v3.3
```html
<!ELEMENT opinion ( (opinion_holder?,opinion_expression,opinion_target?)
		| (opinion_expression,opinion_holder?,opinion_target?)
		| (opinion_expression,opinion_target?,opinion_holder?)
		| (opinion_holder?,opinion_target?,opinion_expression)
		| (opinion_target?,opinion_holder?,opinion_expression)
		| (opinion_target?,opinion_expression,opinion_holder?))>
```
v3.2
```html
<!ELEMENT opinion (opinion_holder | opinion_target | opinion_expression)+>
```
### Causal relations
v3.3
```html
<!ELEMENT causalRelations (clink)+>
```
v3.2
```html
<!ELEMENT causalRelations (clink)*>
```
### Statements
v3.3
```html
<!ELEMENT statement (statement_target, statement_source?, statement_cue?)>
```
v3.2
```html
<!ELEMENT statement (statement_target| statement_source | statement_cue)+>
```

## Opinion elements have only one span
v3.3
```html
<!ELEMENT opinion_holder (span)>
<!ELEMENT opinion_target (span)>
<!ELEMENT opinion_expression (span)>
```
v3.2
```html
<!ELEMENT opinion_holder (span)+>
<!ELEMENT opinion_target (span)+>
<!ELEMENT opinion_expression (span)+>
```

## Timex3 elements have a single span
v3.3
```html
<!ELEMENT timex3 (span)>
```
v3.2
```html
<!ELEMENT timex3 (span)+>
```
