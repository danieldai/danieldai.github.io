Title: Python Modules, Packages and Import
Date: 2016-01-16 22:20
Category: Post

Modules in Python are simply Python files with the .py extension, which implement a set of functions. Modules are imported from other modules using the `import` command.

To import a module, we use the `import` command. Check out the full list of built-in modules in the Python standard library [here](http://docs.python.org/2/library/).

The first time a module is loaded into a running Python script, it is initialized by executing the code in the module once. If another module in your code imports the same module again, it will not be loaded twice but once only - so local variables inside the module act as a **"singleton"** - they are **initialized only once**.

If we want to import the module `urllib`, which enables us to create read data from URLs, we simply `import` the module:

```python
# import the library
import urllib

# use it
urllib.urlopen(...)
```

## Writing modules

Writing Python modules is very simple. To create a module of your own, simply create a new .py file with the module name, and then import it using the Python file name (without the .py extension) using the `import` command.

## Writing packages

Packages are namespaces which contain multiple packages and modules themselves. They are simply directories, but with a twist.

Each package in Python is a directory which **MUST** contain a special file called **`__init__.py`**. This file can be empty, and it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.

The **`__init__.py`** file can also decide which modules the package exports as the API, while keeping other modules internal, by overriding the **`__all__`** variable, like so:

```python
__init__.py:

__all__ = ["bar"]
```

# Absolute Imports

In Python 2.4 and earlier, if you're reading a module located inside a package, it is not clear whether

```python
import foo
```

refers to a top-level module or to another module inside the package. As Python's library expands, more and more existing package internal modules suddenly shadow standard library modules by accident. It's a particularly difficult problem inside packages because there's no way to specify which module is meant. To resolve the ambiguity, it is proposed that foo will always be a module or package reachable from sys.path . This is called an absolute import.

The python-dev community chose absolute imports as the default because they're the more common use case and because absolute imports can provide all the functionality of relative (intra-package) imports -- albeit at the cost of difficulty when renaming package pieces higher up in the hierarchy or when moving one package inside another.

Because this represents a change in semantics, absolute imports will be optional in Python 2.5 and 2.6 through the use of

```python
from __future__ import absolute_import
```

This part of the proposal had BDFL approval from the beginning.

# Relative Imports

Relative imports use leading dots. A single leading dot indicates a relative import, starting with the current package. Two or more leading dots give a relative import to the parent(s) of the current package, one level per dot after the first. Here's a sample package layout:

```
package/
    __init__.py
    subpackage1/
        __init__.py
        moduleX.py
        moduleY.py
    subpackage2/
        __init__.py
        moduleZ.py
    moduleA.py
```

Assuming that the current file is either `moduleX.py` or `subpackage1/__init__.py` , following are correct usages of the new syntax:

```python
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
from ...package import bar
from ...sys import path
```

Note that while that last case is legal, it is certainly discouraged ("insane" was the word Guido used).

Relative imports must always use `from <> import` ; `import <>` is always absolute. Of course, absolute imports can use `from <> import` by omitting the leading dots. The reason `import .foo` is prohibited is because after

```python
import XXX.YYY.ZZZ
```

then

```pytohn
XXX.YYY.ZZZ
```

is usable in an expression. But

```pytohn
.moduleY
```

is not usable in an expression.



#ref

1. http://www.learnpython.org/en/Modules_and_Packages
2. https://www.python.org/dev/peps/pep-0328/
3. https://docs.python.org/2.5/whatsnew/pep-328.html