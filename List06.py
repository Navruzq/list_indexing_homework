def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    s=0
    i=0
    while i<5:
       if list1[i]==1:
           s='1' in list1
           list1[s]=True
       i+=1
    return list1
print(main([1,0,0,0,0]))