# pypi-to-module
Creates an environment module from a package on pypi

## Algorithm
User runs pypi_to_module.py passing specfile directory, pypi package name, module name, and an install script
- if there is NOT a specfile with the same version as pypi
  - the install script is called with these args `$NAME $VERSION $RELEASE`



## Installation
```
wget https://raw.githubusercontent.com/Duke-GCB/pypi-to-module/master/pypi_to_module.py
chmod 755 pypi_to_module.py
```

Create an installation script that performs the specific environment module installation process.
See [example_install_script.sh](https://github.com/Duke-GCB/pypi-to-module/blob/master/example_install_script.sh) for an example of a install script. 




## Usage
```
usage: ./pypi_to_module.py <SPECFILE_DIRECTORY> <PYPI_NAME> <MODULE_NAME> <INSTALL_SCRIPT>
```
So to try installing the python package `DukeDSClient` with the module name `ddsclient` using the `/data/specfiles` directory and using a installation script at `/usr/bin/install_module.sh`. You would run this command:
```
./pypi_to_module.py /data/specfiles DukeDSClient ddsclient /usr/bin/install_module.sh
```

