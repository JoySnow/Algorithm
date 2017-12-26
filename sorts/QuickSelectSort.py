# coding: utf-8

# In[16]:

#a = [5,2,8,3,7,1,4]


# In[5]:


def partation(a, p, q):
    """
    Use a[p] as pivot for partation.
    Return the index of pivot value.
    """
    print "=== Start in partation ==="

    if p == q:
        return p
    elif p > q:
        return -1

    #a = copy(s)
    pivot = p
    i = p
    #j = len(a)-1
    j = q-p-1
    while i<j:
        print "i = ", i
        if a[i] > a[pivot]:
            a[i], a[j] = a[j], a[i]
            j -= 1
        i += 1
    print "a = ", a
    a[pivot], a[i-1] = a[i-1], a[pivot]
    print "aa = ", a
    print "=== end of partation ==="
    return i-1

s1 = [5,9,8,3,7,1,4]
print partation(s1, 0, 7)

s2 = [11,9,8,3,7,1,4]
print partation(s2, 0, 7)



def quick_select_sort(s, k):
    if not 0 <= k < len(s):
        return "Invalid k"
    kk = k
    pivot = 0
    while 0 <= pivot < len(s):
        pivot = partation(s, 0, len(s))
        if kk == pivot+1:
            print "kk == pivot+1"
            print "pivot: ", pivot
            print s[pivot]
            break
        elif kk > pivot+1:
            print "kk > pivot+1"
            p = pivot + 1
            q = len(s)
            kk -= pivot+1
        else:
            print "kk < pivot"
            p = 0
            q = pivot -1

    if 0 <= pivot < len(s):
        return s[pivot]
    else:
        return None

print quick_select_sort(s, 4)

