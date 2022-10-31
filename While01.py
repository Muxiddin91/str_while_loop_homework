from re import A
def main(str):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    uzunligi=len(str)
    a=0
    c=0
    while a<uzunligi:
        b=str[a]
        # b=int(b)
        if b.isdigit():
            c+=1
        a+=1
    return c
print(main('1gg7h64'))
