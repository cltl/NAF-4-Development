# NAF version 3.2
NAF version 3.2 extends version 3.1 with a new definition of `tunits`
* **date**: January 19, 2021
* **author**: Sophie Arnoult (s.i.arnoult@vu.nl)

## tunits
The `tunits` element allows to specify text units, like headers, paragraphs, notes, etc.

NAF version 3.1 (and 3.0)
```dtd
<!ELEMENT tunits (#PCDATA)*>
```

NAF version 3.2
```
<!ELEMENT tunits (tunit)+>

<!-- TUNIT ELEMENT -->
<!ELEMENT tunit EMPTY>
<!ATTLIST tunit
          id ID #REQUIRED
          type CDATA #IMPLIED
          xpath CDATA #IMPLIED
          offset CDATA #REQUIRED
          length CDATA #REQUIRED>
```

