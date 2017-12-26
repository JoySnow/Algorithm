
# coding: utf-8
#########################################################################
# Date: 2017-12-26
# Auther: XiaoxueWang(JoySnow)
# Detail: Quicksort with HoarePartation way in <IntrotoAlg>; O(nlogn)
#########################################################################

def HoarePartation(a, p, q):
    """
    Use a[p] as pivot to partation a[p,q]. q-p >=1
    Return the index of pivot value.
    """
    if p == q:
        return p
    elif p >= q:
        return -1

    pivot = p
    i = p
    j = q
    while True:
        # find the smaller item from right
        while j>p and a[j] >= a[pivot]:
            j -= 1
        # find the bigger item from left
        # this will skip p, since a[p]==a[pivot]
        while i<q and a[i] <= a[pivot]:
            i += 1
        # swap i and j
        if i<j:
            a[i], a[j] = a[j], a[i]
            j -= 1
            i += 1
        # j is the final pivot
        else:
            a[p], a[j] = a[j], a[p]
            return j


def QuickSort(a, p, q):
    pivot = HoarePartation(a, p, q)
    if not p <= pivot <= q:
        return
    if p < pivot-1:
        QuickSort(a, p, pivot-1)
    if pivot+1 < q:
        QuickSort(a, pivot+1, q)


s1 = [5,9,8,3,7,1,4]
s2 = [11,9,8,3,7,1,4]
s3 = [8, 9, 5, 7,]
s4 = [8, 9, 10, 7,]
s5 = [11,9,8,3,7,1,16]
s6 = [9, 8]
s7 = [8, 9]

ss = [s1,s2,s3,s4,s5,s6,s7]
for s in ss:
    QuickSort(s, 0, len(s)-1)
    print s
