""" Check Palindrome or not ,Basically palindrome is a sequence of characters (numbers , letters, phrases etc.) which when read in reverse order sounds and readble like from forward"""
def is_palindrome(s):

    originalstring = s
    reversestring = reverse(s)

    if originalstring == reversestring:
        return True

    else:
        return False

def reverse(data):

    n = list(data)

    start_index = 0
    end_index = len(n)- 1

    while start_index  < end_index:
        n[start_index] , n[end_index] = n[end_index], n[start_index]
        start_index += 1
        end_index -= 1
    
    return ''.join(n)


def palindrome_python(s):

    if s == s[::-1]:
        return True

    else:
        return False

if __name__=='__main__':
    print(palindrome_python("madam"))
    print(is_palindrome("radar"))