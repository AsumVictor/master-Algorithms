def split_to_equal_sum(arr):
    total_sum = sum(arr)
    r_arr = arr.copy()
    r_arr.reverse()

    if total_sum % 2 != 0:
        return "Not Possible"

    l = sum_to_num(arr, total_sum / 2)
    r = sum_to_num(r_arr, total_sum / 2)
    
    if r == None or l == None:
        return "Not Possible"
    
    return [arr[:l+1], arr[len(arr) - 1 -r:]]


def sum_to_num(arr, n):
    sum = 0
    for i in range(len(arr) - 1):
        sum += arr[i]
        if sum > n:
            return None
        if sum == n:
            return i

    return None