'''
https://www.pramp.com/challenge/8noLWxLP6JUZJ2bA2rnx
'''


def decrypt(word: str) -> str:
    # input string can be empty
    if len(word) == 0:
        return ""
    
    # avoid magic numbers and magic strings
    ORD_A = ord('a')
    LOWERCASE_LENGTH = 26

    # previous subtraction step,
    # for the first character decrement its code 
    previous = 1
    # output string builder
    output = []
    
    # O(n)
    for char in word:
        charcode = ord(char)
        decrypted_code = charcode - previous
        
        # because of the subtraction,
        # normalize code to be in the range of lowercase letter codes
        # by adding the length of the range
        if decrypted_code < ORD_A:
            decrypted_code += LOWERCASE_LENGTH
        
        output.append(chr(decrypted_code))
        # use remainder of division between previous and length
        # so next iterations only need to add the length once
        previous = (previous + decrypted_code) % LOWERCASE_LENGTH
    
    return "".join(output)
