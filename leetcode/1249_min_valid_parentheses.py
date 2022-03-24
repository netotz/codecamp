'''
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

iterate input string s, O(n)
use a stack to store indexes of open parentheses.
if current char is opening parenthesis,
push current index to stack.
or if current character is closing parenthesis,
then check if stack is empty:
    if it is, next char.
    otherwise pop stack
finally add current char to output string builder.
return output as string, skipping indexes in stack.
'''


def minRemoveToMakeValid(s: str) -> str:
    '''
    Time O(n)
    Space O(n)
    '''
    OPENING_PARENTHESIS = '('
    CLOSING_PARENTHESIS = ')'
    
    output = []
    indexes = []
    
    i = 0
    # O(n)
    for char in s:
        if char == OPENING_PARENTHESIS:
            indexes.append(i)
        elif char == CLOSING_PARENTHESIS:
            if len(indexes) == 0:
                continue
            
            indexes.pop()

        output.append(char)
        i += 1
    
    indexes = set(indexes)
    # O(n)
    return ''.join(output[i] for i in range(len(output)) if i not in indexes)
 