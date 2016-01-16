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

#ref

1. http://www.learnpython.org/en/Modules_and_Packages