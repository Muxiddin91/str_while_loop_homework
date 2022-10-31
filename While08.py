def main(s):
    """
    A string of numbers is given. Find how many odd numbers there are and return.
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
            c+=1
        a+=1
    return c
print(main('1234567777788888'))