# coding: utf-8
#########################################################################
# Date: 2017-12-26
# Auther: XiaoxueWang(JoySnow)
# Detail: QuickSelectSort, work with both basic and Hoare Partation way.
#         is it O(NlogN) or O(N)?
#         This can be used for finding the Kth min/max num in a list.
#########################################################################


def BasicPartation(a, p, q):
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


def quick_select_sort(s, p, q, k):
    """
    Use HoarePartation or BasicPartation.
    """
    if not 0 < k <= q-p+1:
        print "check fail?"
        return "Invalid k"
    #pivot = BasicPartation(s, p, q)
    pivot = HoarePartation(s, p, q)
    len_pivot_left = pivot+1-p #contain pivot
    if len_pivot_left == k:
        return s[pivot]
    elif len_pivot_left < k:
        return quick_select_sort(s, p+len_pivot_left, q, k-len_pivot_left)
    else:
        return quick_select_sort(s, p, pivot-1, k)


if __name__ == '__main__':
    #s = [5,9,8,3,7,1,4]
    #print quick_select_sort(s, 0, len(s)-1, 4) # should be 5

    # Test all
    vl = [1,3,4,5,7,8,9]
    for i in xrange(1, 8):
        s = [5,9,8,3,7,1,4]
        out = quick_select_sort(s, 0, len(s)-1, i)
        assert out == vl[i-1]
