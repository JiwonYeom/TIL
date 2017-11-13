## Magic Constants

- Predefined constants, but are created by various extensions so they are present only when extensions are available. (dynamic loading / compiled in)

- Resolved at compile time (regular constants are resolved at runtime)

- `__LINE__` : current line
- `__FILE__` : full path & filename of the file with symlinks *resolved*. 
- `__DIR__` : directory of the file. 
- `__FUNCTION__` : function name
- `__CLASS__` : class name (includes namespace it was declared in)
- `__TRAIT__` : trait name (includes the namespace it was declared in)
- `__METHOD__` : class method name
- `__NAMESPACE__` : current namespace
- `ClassName::class` : fully qualified class name.