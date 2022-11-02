def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    s=0
    i=0
    while i<len(list1):
       if list1[0]==list1[i]:
           s=True
       else:
           return False
       i+=1
    return s
print(main([0,1,1,0,0]))