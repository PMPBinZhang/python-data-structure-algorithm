import random 
import numpy as np 


def count_sort(li):
    li_max = max(li)
    print(li_max)
    count_lst = [0 for _ in range(li_max + 1)]

    for e in li:
        count_lst[e] += 1

    li.clear()
    for ind, val in enumerate(count_lst):
        for _ in range(val):
            li.append(ind)


def buck_sort(li):
    n = 10
    li_max = max(li)
    bucks = [[] for _ in range(n)]

    print(len(bucks))
    for ele in li:
        # 要写入第几号通
        i = min(ele // ((li_max) // n), n - 1)
        bucks[i].append(ele)
        for j in range(len(bucks[i]) - 1, 1, -1):
            if bucks[i][j] < bucks[i][j - 1]:
                bucks[i][j], bucks[i][j - 1] = bucks[i][j - 1], bucks[i][j]

    li.clear()
    for buck in bucks:
        li.extend(buck)


def radix_sort(li):
    li_max = max(li)

    for i in range(int(np.log10(li_max)) + 1):
        bucks = [[] for i in range(10)]
        for val in li:
            # 放入到第几号桶
            # print(int(np.log10(li_max)))
            buck_index = int(str(val).zfill(int(np.log10(li_max) + 1))[-1 - i])
            bucks[buck_index].append(val)

        print(bucks)
        li.clear()
        for buck in bucks:
            # print(buck)
            li.extend(buck)

        i += 1

random.seed(1)
li = [random.randint(2, 100) for _ in range(10000)]
# li = [2, 10, 20]
# print(li)
# count_sort(li)
# buck_sort(li)
radix_sort(li)
print(li)