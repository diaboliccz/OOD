value = input("Enter Input : ")

def checkBracket(value):
    stack = []
    
    for char in value:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == "(":
                if char != ")":
                    return False
            if current_char == "{":
                if char != "}":
                    return False
            if current_char == "[":
                if char != "]":
                    return False
    if stack:
        return False
    return True

if checkBracket(value):
    print("Parentheses : Matched ! ! !")
else:
    print("Parentheses : Unmatched ! ! !")
