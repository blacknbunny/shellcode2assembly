# ShellcodeToAssembly

## Replace in shellcodetoasm.py with your shellcode. { Endian type is little endian. }
```c
shellcode = ''
```
---------

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)]()

## Installation
`git clone https://github.com/blacknbunny/ShellcodeToAssembly.git && cd ShellcodeToAssembly/ && pip2 install -r requirements.txt && python2 shellcodetoasm.py`


## Modules manual installation
#### `pip install -r requirements.txt` it can be `pip2 install -r requirements.txt`

## Usage
`python2 shellcodetoasm.py [returnbit] [architecture] [assembly-flavor]`

## For example
`python2 shellcodetoasm.py 32 x86 att`

`python2 shellcodetoasm.py 64 x86`

`Second one is auto intel`

## Architectures
### `ARM`
### `ARM64`
### `MIPS`
### `ppc`
### `X86`

## Return Bit
### `64`
### `32`

## Assembly Flavor
### `AT&T`
### `INTEL`

------

[![demo](https://asciinema.org/a/xjWrXfftZS7BvSzVRd44LuzkP.png)](https://asciinema.org/a/xjWrXfftZS7BvSzVRd44LuzkP?autoplay=1)
