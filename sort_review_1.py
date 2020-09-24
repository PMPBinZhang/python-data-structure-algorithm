import random


def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        exchange = False
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                exchange = True

        if not exchange:
            break 


def select_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        min_value = lst[i] 
        for j in range(i + 1, n):
            if lst[j] < min_value:
                min_index = j 
                min_value = lst[j]
        if min_index != i:
            lst[min_index], lst[i] = lst[i], lst[min_index]


def insert_sort(lst):
    n = len(lst)
    for i in range(1, n):
        # print("i is ", i )
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
            else:
                break

def insert_sort_1(lst):
    n = len(lst)
    for i in range(1, n):
        tmp = lst[i]
        j = i - 1
        while j >= 0 and lst[j] >= tmp:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = tmp



# li = [1, 3, 5, 7, 8, 2, 6, 4]
li = list(range(0, 200))
random.shuffle(li)
print(li)
# bubble_sort(li)
# select_sort(li)
insert_sort_1(li)
print('after sort')
print(li)
