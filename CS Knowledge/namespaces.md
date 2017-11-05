## Namespaces (general)

For some reason I'm having trouble grabbing and utilizing the concept of `namespace`.
So here goes a more detailed sum up

> ref: https://en.wikipedia.org/wiki/Namespace

* Definition: set of symbols that are used to organize **objects of various kinds**, in order to refer them **by name**.
    * **file systems** are itself namespaces for files.
    * some langauges organize their variables and subroutines in namespaces. (Java, PHP, C#.. etc)
    * `subroutine`? :  sequence of program instructions that perform specific task, packaged as unit. => procedure, function, routine, method, subprogram...
    * computer networks & distributed systems assigning names to resources (printers, websites, remote files..)

* Namespaces are usually structured as hierarchies. This means a name can be reused in different contexts.

##### Name Conflicts
- Ex) One XML contains **`HTML` table** and another one a XML table. These two will conflict when combined together.

* Solution : Use prefix (add `h:` or `f:` in front of each tag)

##### Naming System
* Name in namespace consists of namespace identifier and local name. Namespace name is usually applied as a prefix to the local name. 

* Augmented Backus-Naur form:
> name = <namespace identifier> separator <local name>

* Examples:
    * path: `/home/user/readme.txt` ==> identifier: /home/user, local name: readme.txt
    * Domain name: `www.example.com` ==> identifier: example.com(domain), local name: www (host name)
    * XML: `xmlns:xhtml="http://www.w3.org/1999/xhtml"<xhtml:body>` ==> identifier: http://www.w3.org/1999/xhtml, local name: body
    * Java: `java.util.Date` ==> identifier: java.util, local name: Date
    * Mac Address: `01-23-45-67-89-ab` ==> identifier: 01-23-45 (organizationally unique), local name: 67-89-ab(NIC specific)

(continued)