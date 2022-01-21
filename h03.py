# -*- coding: utf-8 -*-

merge_sort_called_with = list()


def merge_sort(lst, ascending):
    if len(lst) > 1:
        polovica = len(lst) // 2
        merge_sort_called_with.append(polovica)
        polovica1 = lst[:polovica]
        polovica2 = lst[polovica:]
        merge_sort(polovica1, ascending)
        merge_sort(polovica2, ascending)
        number1 = number2 = number_lst = 0
        len1 = len(polovica1)
        len2 = len(polovica2)
        while number1 < len1 and number2 < len2:
            if ascending is True:
                if polovica1[number1] > polovica2[number2]:
                    lst[number_lst] = polovica2[number2]
                    number2 += 1
                else:
                    lst[number_lst] = polovica1[number1]
                    number1 += 1
            elif ascending is False:
                if polovica1[number1] < polovica2[number2]:
                    lst[number_lst] = polovica2[number2]
                    number2 += 1
                else:
                    lst[number_lst] = polovica1[number1]
                    number1 += 1

            number_lst += 1
        while number1 < len1:
            lst[number_lst] = polovica1[number1]
            number1 += 1
            number_lst += 1
        while number2 < len2:
            lst[number_lst] = polovica2[number2]
            number2 += 1
            number_lst += 1


if __name__ == '__main__':
    arr = [15, 64, 25, 12, 22, 11]
    # merge_sort(arr, ascending= True)
    # print(merge_sort_called_with)
    # print(arr)
    merge_sort(arr, ascending= False)
    print(merge_sort_called_with)
    print(arr)

# for ascending=True it should print
# [2, 1, 1, 1]
# [11, 12, 22, 25, 64]

# for ascending=False it should print
# [2, 1, 1, 1]
# [64, 25, 22, 12, 11]
