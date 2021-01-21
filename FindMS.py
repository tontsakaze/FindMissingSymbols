import sys

def main(arg):
    try:
        f = open(arg)
    except IOError:
        print( "Cannot find {}".format(arg) )
    else:
        lines = f.readlines()
        f.close()

        #for i in range(len(lines)):
        #    lines[i] = lines[i].replace("\t", "").replace("\n", "")
            
        stack = []

        # CHECK FOR BRACES
        line_nro = 0
        last_open_brace = 0
        last_char = ""
        wrong = False

        for line in lines:
            line_nro += 1
            for ch in line:
                if ch=='{' or ch=='(' or ch=='[' or ch=='<':
                    stack.append(ch)
                    last_open_brace = line_nro
                    
                if ch=='}':
                    last_open_brace = line_nro
                    wrong = True
                    if len(stack)>0:
                        last_char = stack.pop(-1)
                        if last_char=='{':
                            wrong = False
                elif ch==')':
                    last_open_brace = line_nro
                    wrong = True
                    if len(stack)>0:
                        last_char = stack.pop(-1)
                        if last_char=='(':
                            wrong = False
                elif ch==']':
                    last_open_brace = line_nro
                    wrong = True
                    if len(stack)>0:
                        last_char = stack.pop(-1)
                        if last_char=='[':
                            wrong = False
                elif ch=='>':
                    last_open_brace = line_nro
                    wrong = True
                    if len(stack)>0:
                        last_char = stack.pop(-1)
                        if last_char=='<':
                            wrong = False
                        
                if wrong:
                    break

            if wrong:
                break

        if wrong:
            print( "{} ERROR! IN LINE {}".format(last_char, line_nro) )
        elif len(stack)>0:
            print( "Too many open paranthesis/braces/brackets")
            print("Stack: " + str(stack))
        else:
            print( "NO {}{}{}{}{}{}{}{} ERRORS!".format('{','}','(',')','[','}','<','>') )




        # CHECK FOR " ERRORS
        braces = 0
        line_nro = 0
        last_open_brace = 0

        for line in lines:
            line_nro += 1
            braces=0
            for ch in line:
                if "\"" in ch:
                    last_open_brace = line_nro
                    braces += 1

            if braces%2!=0:
                break


        if braces%2!=0:
            print( "ERROR WITH \"!" )
            print( "   IN LINE {}".format(line_nro) )
        else:
            print( "NO \"\" ERRORS!" )




        # CHECK FOR ' ERRORS
        braces = 0
        line_nro = 0
        last_open_brace = 0

        for line in lines:
            line_nro += 1
            braces=0
            for ch in line:
                if "'" in ch:
                    last_open_brace = line_nro
                    braces += 1

            if braces%2!=0:
                break


        if braces%2!=0:
            print( "ERROR WITH '!" )
            print( "   IN LINE {}".format(line_nro) )
        else:
            print( "NO '' ERRORS!" )


if __name__ == "__main__":
    try:
        arg = sys.argv[1]
    except IndexError:
        print("ERROR! Filename needed!")
        print("Open from command line. Example:")
        print("python FindMS.py filename.txt")
        input("...")
    else:
        main(arg)