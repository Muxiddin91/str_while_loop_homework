def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    
    uzunligi=len(s)
    a=0
    c=0
    while a<uzunligi:
        b=s[a]
        if int(b)%2==1:
            c+=int(b)
        a+=1
    return c
print(main('22992'))