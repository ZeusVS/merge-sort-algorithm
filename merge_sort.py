def merge_sort(list):
    if len(list) <= 1:
        return list
    
    middle = len(list) // 2
    left_list = list[:middle]
    right_list = list[middle:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)


    list = []
    left_pointer = 0
    left_max = len(left_list) - 1
    right_pointer = 0
    right_max = len(right_list) - 1

    while True:
        if left_list[left_pointer] <= right_list[right_pointer]:
            list.append(left_list[left_pointer])
            left_pointer += 1
        else:
            list.append(right_list[right_pointer])
            right_pointer += 1
        if left_pointer > left_max:
            list.extend(right_list[right_pointer:])
            break
        if right_pointer > right_max:
            list.extend(left_list[left_pointer:])
            break
    return list
        


list = [45, 7, 85, 24, 60, 25, 38, 63, 1, 2]
list = merge_sort(list)
print(list)