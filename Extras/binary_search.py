# Binary search

# Método de procura utilizado em uma lista ordenada para encontrar um valor sem precisar iterar pela lista inteira
def bin_search(a, target, min=None, max=None):
    if min == None:
        min = 0

    if max == None:
        max = len(a) - 1

    if max < min:
        return -1
    
    mid = (min + max) // 2

    if a[mid] == target:
        return mid
    elif target < a[mid]:
        return bin_search(a, target, min, mid-1)
    else:
        return bin_search(a, target, mid+1, max)


if __name__=='__main__':
    my_list = [29, 33, 26, 35, 24, 59, 70, 21, 93, 51]
    my_list = sorted(list(my_list))

    print(bin_search(my_list, 33))
    