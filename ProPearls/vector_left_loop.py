##############################################################
# Auther: Xiaoxue Wang / Joy
# Date: Mon Jul 31 18:14:41 CST 2017
##############################################################
#
# Question:
#   Left-loop l items in a vector( length of vector is n ),
#   Time is O(n), Space <= 100 bytes.
#   Sample:
#       Input:  abcdefgh, l=3, n=8
#       Output: defghabc
#
# Solution_1:
#   Start a once_loop:
#       t = x[0]
#       x[l] -> x[0]
#       x[2*l] -> x[l]
#       ...
#       loop until the index of x is 0 again
#   Until now, if there are still any items is not moved,
#   start this loop again with x[1]
#   ...
#   everybody is moved. :D
#
# Solution_2:
#   Let's suppose len(a) < len(b) !
#   len(a) = l, len(br) = l, len(bl) = len(b) - len(br) = n-2l
#   ab = a bl br --step1--> br bl a --step2--> bl br a = ba
#   --step1--> : easy.
#   --step2--> : like use Solution_1 to make brbl --> blbr
#
# Solution_3:
#   reverse(0, l-1)  # cba defgh
#   reverse(l, n-1)  # cba hgfed
#   reverse(0, n-1)  # defgh abc
#
##############################################################


x, l, n = list("abcdefg"), 3, 7
#x, l, n = list("abcdefgh"), 3, 8
#x, l, n = list("abcdefgh"), 4, 8


def loop_once(j):
    t = x[j]
    empty = j
    for i in xrange(1, n+1):
        index = (i*l+j)%n
        if index == j:
            x[empty] = t
            print "End here: x: ", x
            break
        x[empty] = x[index]
        empty = index
        print "x: ", x
    print "End of one loop: ", x


def vector_left_loop(x, l):
    """Solution_1: """
    n = len(x)
    print "Before: x: ", x
    if n%l:
        loop_once(0)
    else:
        for j in xrange(0, l):
            loop_once(j)
    print "After: x: ", x

if __name__ == "__main__":
    print "Start vector_left_loop process:"
    vector_left_loop(x, l)
