import random


def topk(li, k):
    def sift(l, low, high):
        i = low
        j = 2 * i + 1
        tmp = l[low]
        while j <= high:
            if j + 1 <= high and l[j + 1] < l[j]:
                j = j + 1 # 右孩子比较大
            if l[j] < tmp:
                l[i] = l[j]
                i = j 
                j = 2 * i + 1
            else:
                l[i] = tmp
                break
        else:
            l[i] = tmp

    # 取前k个元素构建堆
    li_k = li[:k]
    for i in range((k - 2) // 2, -1, -1):
        sift(li_k, i, k - 1)
    # 将列表中大于堆顶的值替换
    for i in range(k, len(li) - 1):
        if li[i] > li_k[0]:
            li_k[0], li[i] = li[i], li_k[0]
            sift(li_k, 0, k - 1)
    # 挨个取出来
    for h in range(k - 1, -1, -1):
        li_k[0], li_k[h] = li_k[h], li_k[0]
        sift(li_k, 0, h - 1)

    return li_k 

li = list(range(100))
random.seed(1)
random.shuffle(li)
print(li[:5])
li_topk = topk(li, 5)
print(li_topk)