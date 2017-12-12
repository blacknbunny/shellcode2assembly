from capstone import *
import time, sys, platform, os

# Change here
shellcode = ''

def loading():
    print "Loading..."
    for i in range(0, 100):
        time.sleep(0.1)
        width = (i + 1) / 4
        bar = "[" + "#" * width + " " * (25 - width) + "]"
        sys.stdout.write(u"\u001b[1000D" +  bar)
        sys.stdout.flush()
    print
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def holefunc(architecture, mode):
    options = Cs(architecture, mode)
    if sys.argv[3] == 'att':
        options.syntax = CS_OPT_SYNTAX_ATT
    else:
        options.syntax = CS_OPT_SYNTAX_INTEL
    listofinstructions = options.disasm(shellcode, 0x2000)
    for shtoasm in listofinstructions:
        print("%x\t%s\t%s" %(shtoasm.address, shtoasm.mnemonic, shtoasm.op_str))
def error(error):
    cls()
    print("Select the bit %s" % (error))
    sys.exit(1)

if len(sys.argv) < 3:
    cls()
    print("Author : https://www.github.com/blacknbunny")
    print("Usage:\t./shellcodetoasm.py [returnbit] [architecture] [assembly-flavor]")
    sys.exit(1)
else:
    cls()
    loading()
    returnbit = sys.argv[1]
    arch = sys.argv[2]
    if returnbit == '64':
        if arch == 'arm':
            holefunc(CS_ARCH_ARM, CS_MODE_ARM)
        elif arch == 'arm64':
            holefunc(CS_ARCH_ARM64, CS_MODE_ARM)
        elif arch == 'mips':
            holefunc(CS_ARCH_MIPS, CS_MODE_MIPS64)
        elif arch == 'ppc':
            holefunc(CS_ARCH_PPC, CS_MODE_64)
        elif arch == 'x86':
            holefunc(CS_ARCH_X86, CS_MODE_64)
    	else:
       	    error("architecture")
    elif returnbit == '32':
        if arch == 'arm':
            holefunc(CS_ARCH_ARM, CS_MODE_ARM)
        elif arch == 'arm64':
            holefunc(CS_ARCH_ARM64, CS_MODE_ARM)
        elif arch == 'mips':
            holefunc(CS_ARCH_MIPS, CS_MODE_MIPS32)
        elif arch == 'ppc':
            holefunc(CS_ARCH_PPC, CS_MODE_32)
        elif arch == 'x86':
            holefunc(CS_ARCH_X86, CS_MODE_32)
        else:
            error("architecture")
    else:
        error("size")
