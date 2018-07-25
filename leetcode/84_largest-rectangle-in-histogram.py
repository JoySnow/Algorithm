
### **条形图中可圈出的最大长方形面积**

[Leetcode: 84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)


##### Solution-1: Plain & Simple Way O(n^2)
One by one consider all bars as starting points and calculate area of allrectangles starting with every bar. Finally return maximum of all possible areas. Time complexity of this solution would be O(n^2).  
Refer to:
https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/

##### Solution-2: Divide and Conquer O(nLogn)
The idea is to find the `minimum value` in the given array. Once we have index of the minimum value, the max area is maximum of following three values:
 - a) Maximum area in left side of minimum value (Not including the min value)
 - b) Maximum area in right side of minimum value (Not including the min value)
 - c) Number of bars multiplied by minimum value.


###### Way-1 of Get the minimum value: linear search
The worst case time complexity of this algorithm becomes O(n^2).
Each search for min value: O(n);  
Worst case of divide_and_conquer is always (n-1) and 0 divide, so, will be O(n) times instead of O(logn);  
T(n) = O(n) * O(n) = O(n^2).

###### Way-2 of Get the minimum value: Range Minimum Query using Segment Tree
Segment tree can handle the search-in-range more efficient.  
(TODO: how segment tree works?)   
And the time to build is O(n), the query is O(logn).

Overall Time = Time to build Segment Tree + Time to recursively find maximum area  
T(n) = O(n) + (O(Logn) * T(n-1))   # still worst case, O(n-1)  
So overall time is O(nLogn).

Refer to:
https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/

```python
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        Divide and Conquer O(nlogn)

        Max area is maximum of following three values:
         - a) Maximum area in left side of minimum value (Not including the min value)
         - b) Maximum area in right side of minimum value (Not including the min value)
         - c) Number of bars multiplied by minimum value.

        1. Divide: find the min as Pivort;
        2. Conquer: choose the maxmum solution.

        Results:
          With Way-1: Time Limit Exceeded
          With Way-2: TODO
        """        
        # Way-1: linear search
        def get_min_index(heights, p, q):
            m = p
            for i in xrange(p+1, q+1):
                if heights[m] > heights[i]:
                    m = i
            return m

        # TODO:
        # Way-2: Range Minimum Query using Segment Tree
        #def get_min_index(heights, p, q):       
        #

        def handle(heights, p, q):
            print "Handle: ", p, q
            if p > q:
                print "< R 0"
                return 0
            if p == q:
                print "< R == ", heights[p]
                return heights[p]
            mini = get_min_index(heights, p, q)
            minx = heights[mini]
            print "min: ", mini, minx
            a = handle(heights, p, mini-1)
            b = handle(heights, mini+1, q)
            c = (q-p+1) * minx
            print "abc: ", a, b, c
            print "< R mx ", max(a, b, c)
            return max(a, b, c)

        N = len(heights)
        return handle(heights, 0, N-1)
```

#### Solution-3: Stack O(n)

For every bar `x`, we calculate the area with `x` as the smallest bar in the rectangle.  
If we calculate such area for every bar `x` and find the maximum of all areas, our task is done.  
###### How to calculate area with ‘x’ as smallest bar?  
Since `x` is as the smallest, then the areas = height * length.  
Height is `x`, length is the between of [left index, right index].  
left index: index of the first smaller (smaller than ‘x’) bar on left of ‘x’;  
right index: index of first smaller bar on right of ‘x’.  

So, How to use Stack to achieve these?  
(HINT: Before, we use stack to get item's next bigger value in a given list.)  
Here, maintain a stack in increasing order of values.  

We traverse all bars from left to right, maintain a stack of bars. Every bar is pushed to stack once. Stack is maintained in increasing order.  
A bar is popped from stack when a bar of smaller height is seen.  
When a bar is popped, we calculate the area with the popped bar as smallest bar.  
How do we get left and right indexes of this popped bar?
 - The current index tells us the ‘right index’;
 - The index of previous item in stack is the ‘left index’.

HINT: we calculate the area of items for pushed ones at it's pop time.

Following is the complete algorithm.

1) Create an empty stack.

2) Start from first bar, and do following for every bar ‘hist[i]’ where ‘i’ varies from 0 to n-1.
  - a) If stack is empty or hist[i] is higher than the bar at top of stack, then push ‘i’ to stack.
  - b) If this bar is smaller than the top of stack, then keep removing the top of stack while top of the stack is greater. Let the removed bar be hist[tp]. Calculate area of rectangle with hist[tp] as smallest bar. For hist[tp], the ‘left index’ is previous (previous to tp) item in stack and ‘right index’ is ‘i’ (current index).

3)  Step 2) must ended with the push of the last value.  
If the stack is not empty, then one by one remove all bars from stack and do step 2.b for every removed bar.  
Here, right index will be (N-1), since no smaller item exist in tp's left.

Refer to: https://www.geeksforgeeks.org/largest-rectangle-under-histogram/

```python
class Solution-3(object):
    def largestRectangleArea(self, heights):
        """
        Stack solution:
        Refer to https://www.geeksforgeeks.org/largest-rectangle-under-histogram/
        :type heights: List[int]
        :rtype: int
        """
        N = len(heights)
        st = []
        max_area = 0
        i = 0
        while i < N:
            x = heights[i]

            # 1
            if not st or x >= heights[st[-1]]:
                st.append(i)
                i += 1
            # 2
            else:
                tp = st.pop()
                # not include i and st[-1], but include tp of course.
                # if st is empty, then no smaller item in the left of tp.
                cross = i if not st else (i - st[-1] - 1)
                current_top_area = heights[tp] * cross
                max_area = max(max_area, current_top_area)
                # not i++, still use current i, to compare next st.top.

        # the while must ended with the last one pushed
        assert i == N

        while st:
            # heights[tp] is as the minimum,
            # right index can be the last item: N-1
            # left index is 0 if empty, else left of tp.
            tp = st.pop()
            cross = N if not st else (N-1 - st[-1])
            max_area = max(max_area, heights[tp] * cross)

        return max_area
```
