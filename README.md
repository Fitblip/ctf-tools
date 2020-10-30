
# CTF Tools 
Just a collection of some dockerfiles to help streamline the scramble of getting stable tools during a CTF! Contributions are always welcome :) 

Each tool is supposed to be a passthrough so after running `python3 build.py` to build and stock your docker registery, you can do things like `./bin/nmap -sV some.host` without having to install/build things in your local environment (which increases the security of your computer measurably as well while participating).

## Building
You should be able to just clone this repo, then run `python3 build.py`, which will build all the docker images found in this repo, then regenerate the scripts in the `bin/` directory.

## Current tools:
- [Dirsearch](dockerfiles/Dockerfile.dirsearch)
- [Wfuzz](dockerfiles/Dockerfile.wfuzz)
- [Peda](dockerfiles/Dockerfile.peda)
- [Radare2](dockerfiles/Dockerfile.radare2)
- [Nmap](dockerfiles/Dockerfile.nmap)
- [Pwndbg](dockerfiles/Dockerfile.pwndbg)
- [Angr](dockerfiles/Dockerfile.angr)
- [Pwntools](dockerfiles/Dockerfile.pwntools)


