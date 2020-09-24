import sys 
sys.setrecursionlimit(100000)
import random

from decorator import time_cal

def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return li
    return li 


def select_sort(li):
    for i in range(len(li) - 1):
        min_index = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_index]:
                min_index = j
        if min_index != i:
            li[i], li[min_index] = li[min_index], li[i]
        print(li)
    return li 
    ...


def insert_sort(li):
    for i in range(1, len(li)):
        for j in range(i, 0, -1):
            if li[j] < li[j-1]:
                li[j], li[j-1] = li[j-1], li[j]
            else:
                break


def insert_sort_2(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] >= tmp:
            li[j + 1] = li[j]
            j -= 1 
        li[j + 1] = tmp

    return li


@time_cal
def quick_sort(li):
    def partition(li, left, right):
        tmp = li[left]
        while left < right:
            while left < right and li[right] >= tmp:
                right -= 1
            li[left] = li[right]
            left += 1

            while left < right and li[left] <= tmp:
                left += 1
            li[right] = li[left]
            right -= 1
        li[left] = tmp 
        return left 

    def quick_sort_single(li, left, right):
        if left < right:
            mid = partition(li, left, right)
            quick_sort_single(li, left, mid - 1)
            quick_sort_single(li, mid + 1, right)

    quick_sort_single(li, 0, len(li) - 1)
    

@time_cal
def quick_sort_2(li):
    
    def quick_sort_2_single(li):
        if len(li) > 1:
            left_list = []
            right_list = []
            mid = li[0]
            for i, e in enumerate(li):
                if i == 0:
                    continue
                if e >= mid:
                    right_list.append(e)
                else:
                    left_list.append(e)
            sort_left = quick_sort_2_single(left_list)
            sort_right = quick_sort_2_single(right_list)
            return sort_left + [mid] + sort_right
        else:
            return li

    sort_result = quick_sort_2_single(li)

    return sort_result


@time_cal
def heap_sort(li):
    def sift(l, low, high):
        i = low
        j = 2 * i + 1
        tmp = li[low]
        while j <= high:
            if j + 1 <= high and l[j + 1] > l[j]:
                j = j + 1 # 右孩子比较大
            if li[j] > tmp:
                l[i] = l[j]
                i = j 
                j = 2 * i + 1
            else:
                l[i] = tmp
                break
        else:
            li[i] = tmp
    # 构建堆
    n = len(li)
    # 农村包围城市的方式构建堆
    # sift(li, (n - 2) // 2, n - 1)
    for i in range((n - 2) // 2, -1, -1):
        sift(li, i, n - 1)
        print(i, li)
    # 挨个取出来
    for h in range(n - 1 , -1, -1):
        li[0], li[h] = li[h], li[0]
        sift(li, 0, h - 1)


def merge_sort(li):
    def merge(li, low, mid, high):
        i = low
        j = mid + 1
        sort_list = []
        while i <= mid and j <= high:
            if li[i] <= li[j]:
                sort_list.append(li[i])
                i += 1
            else:
                sort_list.append(li[j])
                j += 1

        while i <= mid:
            sort_list.append(li[i])
            i += 1
        while j <= high:
            sort_list.append(li[j])
            j += 1
        # print(sort_list)
        li[low:high + 1] = sort_list

    # if low < high:
    #     mid = (low + high) // 2
    #     merge_sort(li, 0, mid)
    #     merge_sort(li, mid + 1, high)
    #     merge(li, low, mid, high)
    def merge_sort_concrete(li, low, high):
        if low < high:
            mid = (low + high) // 2
            merge_sort_concrete(li, 0, mid)
            merge_sort_concrete(li, mid + 1, high)
            merge(li, low, mid, high)

    merge_sort_concrete(li, 0, len(li) - 1)    


def shell_sort(li):
    def insert_sort_gap(li, gap):
        for i in range(gap, len(li)):
            tmp = li[i]
            j = i - gap
            while j >= 0 and li[j] > tmp:
                li[j + gap] = li[j]
                j -= gap
            li[j + gap] = tmp

        print("insert_part", li)

    gap = len(li) // 2
    # insert_sort_gap(li, gap)
    while gap >= 1:
        insert_sort_gap(li, gap)
        gap //= 2

li = list(range(8))
# li = [2, 3, 5, 8, 7]
random.shuffle(li)
print(li)
# bubble_sort(li)
# select_sort(li)
# insert_sort(li)
# insert_sort_2(li)
# bubble_sort(li)
# quick_sort_2(li)
heap_sort(li)
# merge_sort(li)
# shell_sort(li)
# print(li)