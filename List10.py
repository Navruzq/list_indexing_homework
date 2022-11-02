def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    a=list_num[0]
    b=list_num[-1]
    if a<b:

       return b
    else:
        return a
print(main([5,32,1,4,3]))