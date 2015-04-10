#!/usr/bin/env python3

import sys, getopt, re, os

#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))
#print(sys.argv)

def explore(filepattern, pattern):
    regObj = re.compile(filepattern)
    for root, dirs, fnames in os.walk('.'):
        for fname in fnames:
            print('filename ', root, '/', fname, sep='')
            if regObj.match(fname):
                print('file', fname, 'matches')

def usage():
    print('Usage: cgrep [-mp] [-f <file regexp>] <regexp>')
    print('  -h: this help')
    print('  -m: search in make files')
    print('  -p: search in perl files')
    print('  -f: use an alternate file regular expression')
    print('  (see \'man perlre\' for perl regular expressions)')

def main(argv):
    pattern     = ''
    filepattern = '\.(h|c|cc|cpp)$'; # default to source files
    try:
        opts, args = getopt.getopt(argv,"cmpf:o:")
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-c"):
            filepattern = '^Cons(cript|struct)$'
        elif opt in ("-m"):
            filepattern = '([Mm]ake[^~]*|\.mk)$'
        elif opt in ("-p"):
            filepattern = '\.p[lm]$'
        elif opt in ("-f"):
            filepattern = arg

    print('File pattern is "', filepattern)
    print('arg1 is ', str(sys.argv[len(sys.argv) - 1]))
    print('arg is "', arg)
    pattern = str(sys.argv[len(sys.argv) - 1]) # pattern is the last argument
    print('pattern = ', pattern)
    explore(filepattern, pattern)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == "__main__":
    main(sys.argv[1:])
