def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
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
        if int(b)%2==0:
            c+=1
        a+=1
    return c
print(main('123456788888'))