def integer_Reverse(n):
    reverse_int = 0
    remainder =0
    while n > 0:
        remainder = n%10
        n = n//10
        reverse_int = reverse_int*10 + remainder
    return reverse_int
    

if __name__== "__main__":

    num  = int(input("enter your entries here --> "))
    print(num)
    print(integer_Reverse(num))
    
