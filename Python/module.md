# Module in Python
A module can contain executable statements as well as function definitions.   

#### They are executed only the first time the module name is encountered in an import statement.仅在第一次import时运行

#### Each module has its own private symbol table
Thus, the author of a module can use global variables in the module without worrying about accidental clashes with a user’s global variables.
#### you can touch a module’s global variables with the same notation used to refer to its functions, modname.itemname.
