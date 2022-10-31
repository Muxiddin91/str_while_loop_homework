def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
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
        if b.islower():
            c+=1
        a+=1
    return c
print(main('fgrhgtyAAF246'))