# coding: utf-8
#########################################################################
# Date: 2017-12-26
# Auther: XiaoxueWang(JoySnow)
# Detail: Quicksort with basic Partation way in <IntrotoAlg>; O(nlogn)
#########################################################################


def Partation(a, p, q):
    """
    Use a[q] as pivot to partation a[p,q]. q-p >=1
    Return the index of pivot value.
    """
    if p == q:
        return p
    elif p >= q:
        return -1
    pivot = a[q]
    i = p-1
    j = p
    while j<q:
        if a[j]<pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
        j += 1
    a[q], a[i+1] = a[i+1], a[q]
    return i+1


def QuickSort(a, p, q):
    pivot = Partation(a, p, q)
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
