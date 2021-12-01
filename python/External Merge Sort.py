sample_list = [45, 345, 2, 4, 6, 645, 56, 65, 78, 34, 34, 34, 345, 90, 55, 23, 12, 40, 11]

def external_merge_sort(list):
    split_1 = []
    split_2 = []
    while len(split_1) == 0 or len(split_2) == 0:
        for i in range(len(list)):
            if i == 0:
                split_1.append(list[i])
                split_list = True
            else:
                if list[i] < list[i - 1]:
                    if split_list:
                        split_list = False
                    else:
                        split_list = True
                
                if split_list:
                    split_1.append(list[i])
                else:
                    split_2.append(list[i])

        list = []
        split_1_index = 0
        split_2_index = 0
        if len(split_2) == 0:
            return split_1

        for i in range(len(split_1) + len(split_2)):
            if i == 0:
                if split_1[i] < split_2[i]:
                    list.append(split_1[split_1_index])
                    split_1_index += 1
                else:
                    list.append(split_2[split_2_index])
                    split_2_index += 1
            else:
                if split_1_index == len(split_1):
                    list.append(split_2[split_2_index])
                    split_2_index += 1
                elif split_2_index == len(split_2):
                    list.append(split_1[split_1_index])
                    split_1_index += 1
                else:
                    if split_1[split_1_index] < split_2[split_2_index]:
                        list.append(split_1[split_1_index])
                        split_1_index += 1
                    else:
                        list.append(split_2[split_2_index])
                        split_2_index += 1        
        split_1 = []
        split_2 = []

print("Unsorted List:", sample_list)
print("Sorted List:", external_merge_sort(sample_list))