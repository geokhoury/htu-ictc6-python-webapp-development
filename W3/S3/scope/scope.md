# Scope

A scope defines the visibility of a name within a block. If a local variable is defined in a block, its scope includes that block. If the definition occurs in a function block, the scope extends to any blocks contained within the defining one, unless a contained block introduces a different binding for the name.

**What does this mean?**

This means not all variables are accessible from all other parts of your program.
The part of the program where the variable is accessible is called its "scope" and is determined by where the variable is declared.
When a name is not found at all, a NameError exception is raised.

* You can read more about scopes in python [here](https://docs.python.org/3/reference/executionmodel.html#resolution-of-names).

## Types of Scope

Python has three different variable scopes:

* Local scope
* Global scope
* Enclosing scope


### Local Scope

A variable declared within a function has a **local scope**. It is accessible from the point at which it is declared until the end of the function, and exists for as long as the function is executing. Local variables are removed from memory when the function call exits. Therefore, trying to get the value of the local variable outside the function causes an error.

* Look at [local_scope.py](./local_scope.py)

### Global Scope

A variable declared outside all functions has a **global scope**. It is accessible throughout the file, and also inside any file which imports that file.
Global variables are often used for flags (boolean variables that indicate whether a condition is true).

Although you can access global variables inside or outside of a function, you cannot modify it inside a function.

To access the global variable rather than the local one, you need to explicitly declare x global, using the **global** keyword. [Read more](https://docs.python.org/3/reference/simple_stmts.html#global)

* Look at [global_scope.py](./global_scope.py)
* Look at [`globals()`](https://docs.python.org/3/library/functions.html?highlight=globals#globals)

### Enclosing Scope

If a variable is declared in an enclosing function, it is nonlocal to nested functions. It allows you to assign to variables in an outer, but no-global, scope.
The usage of nonlocal is very similar to that of global, except that the former is primarily used in nested methods. [Read more](https://docs.python.org/3/reference/simple_stmts.html#nonlocal)

* Look at [enclosing_scope.py](./enclosing_scope.py)


## Scoping Rule – LEGB Rule


When a variable is referenced, Python follows **LEGB rule** and searches up to four scopes in this order:

* Local scope
* Enclosing scope
* Global scope
* Built-in scope