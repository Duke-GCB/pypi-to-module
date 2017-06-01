# pypi-to-module
Creates an environment module from a package on pypi

## Algorithm
User runs pypi_to_module.py passing specfile directory, pypi package name, module name, and a __scriptname__
- if there is a specfile with the same version as pypi
  - __scriptname__ is called like so: `scriptname $NAME $VERSION $RELEASE`

See `example_install_script.sh` for an example of a install script. 

## Installation
Python program
```
wget https://raw.githubusercontent.com/Duke-GCB/pypi-to-module/master/pypi_to_module.py
chmod 755 pypi_to_module.py
```




## Usage
```
usage: ./pypi_to_module.py <SPECFILE_DIRECTORY> <PYPI_NAME> <MODULE_NAME> <INSTALL_SCRIPT>
```

