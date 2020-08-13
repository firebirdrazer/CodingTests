def check_bracket(Str):
    stack = []                                              #make a empty check stack
    while Str != "":                                        #as long as the input is not empty
        tChar = Str[0]                                      #extract the first character as the test character
        Str = Str[1:]                                       #the rest characters would be the input in the next while loop
        if tChar == "(" or tChar == "{":                    #as the test character is a left-bracket "(" or "{"
            stack.append(tChar)                             #the character would be added into the stack
        elif tChar == ")" or tChar == "}":                  #if the test character is a right-bracket ")" or "}"
            if len(stack) == 0:                             #then we have to check the stack to see if there's a corresponding one
                return False                                #if no or empty, the string would be invalid
            else:                                           #if yes, we can pop the corresponding character from the stack
                if tChar == ")" and stack[-1] == "(":
                    stack.pop(-1)
                elif tChar == "}" and stack[-1] == "{":
                    stack.pop(-1)
                else:
                    return False
    if stack == []:                                         #which means if the string is valid, the stack would be empty
        return True                                         #after the process
    else:                                                   #if there's anything left after the process
        return False                                        #the function would return False

#main program
Test=input()                                                #input string
print(check_bracket(Test))                                  #return True if the input has valid brackets