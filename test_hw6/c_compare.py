from c_list import CustomList


def compare(list1, list2):
    clist1 = CustomList(list1)
    clist2 = CustomList(list2)

    if not clist1.average or not clist2.average:
        mess = "Один из списков пуст"
    elif clist1.average > clist2.average:
        mess = "Первый список имеет большее среднее значение"
    elif clist1.average < clist2.average:
        mess = "Второй список имеет большее среднее значение"
    else:
        mess = "Средние значения равны"

    return mess


if __name__ == '__main__':
    print(compare([3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6]))
    print(compare([1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 7, 8]))
    print(compare([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]))

    print(compare([3, 4, 5, 6, 7, 8], []))
    print(compare([], [3, 4, 5, 6, 7, 8]))
