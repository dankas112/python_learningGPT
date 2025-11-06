# Задача 3 — Объединение и сортировка

# Пусть есть два списка чисел:

# list1 = [3, 1, 4, 5]
# list2 = [8, 2, 4, 3]


# Нужно объединить их, удалить дубликаты, отсортировать и вывести результат.

list1 = [3, 1, 4, 5]
list2 = [8, 2, 4, 3]

for x in list2:
    if x in list1:
        continue
    else:
        list1.append(x)

list1.sort()
print(list1)


# ✅ Логика верная, но в Python есть элегантнее:

# result = sorted(set(list1 + list2))
# print(result)


# (Используется set() для удаления дублей и sorted() для сортировки.)