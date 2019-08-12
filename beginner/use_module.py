# Import Complete module
from beginner.module import module1

module1.hello("Jorge Cas")

# Import Component
from beginner.module.module1 import bye

bye("Jorge Cas")

# Import Component and rename
from beginner.module.module1 import bye as adios

adios("Jorge Cas")

# pip package manager and python modules
# pip --version
# pip list
# pip install <module name>
# pip uninstall <module name>
