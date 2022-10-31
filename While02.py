def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
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
        if b.isalpha():
            c+=1
        a+=1
    return c
print(main('1q2whh3e'))