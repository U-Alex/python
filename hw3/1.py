""" Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
"""

source_list = [1, 2, 3, 3, 4, 4, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10]
dest_list = [source_list[i] for i in range(len(source_list)) if source_list.count(source_list[i]) > 1]
dest_list = list(set(dest_list))

print(source_list)
print(dest_list)
