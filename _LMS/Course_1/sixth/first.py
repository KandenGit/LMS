string = 'Боб'.lower()

def isPalindrome(string: str):
    reverse_str = string[::-1].lower()
    if string == reverse_str:
        return True
    else:
        return False
    

func = isPalindrome(string)
print(func)