import sys

if len(sys.argv) == 2  and sys.argv[1].endswith('py') == True:
    try:
        with open(sys.argv[1]) as file:
            nlines = 0
            for line in file:
                if not line.lstrip().startswith('#') and line.lstrip() != '':
                    nlines += 1
        print(nlines)
    except FileNotFoundError:
        sys.exit('File does not exist')
elif len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) == 2 and sys.argv[1].endswith('py') == False:
    sys.exit('Not a Python file')








