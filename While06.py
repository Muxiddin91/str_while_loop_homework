def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    uzunligi=len(s)
    x=0
    c=0
    while x<uzunligi:
        b=s[x]
        if b="a" or b="e" b="i" or b="o" or b="u" or b.isdigit():
            c+=0
        else:
            c+=1
        x+=1
    return c
print(main('eded36'))