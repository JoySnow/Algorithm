###############################################
# refer to http://lobert.iteye.com/blog/2315802
# Name: Floyd alg
# Q: 'shorted distance of two node'
###############################################


"""
2 ways for path tracking:(dont understand!)

http://blog.csdn.net/immiao/article/details/22199939
1. path[i][j]=k;

 void output(int i,int j){
     if(i==j) return;
     if(path[i][j]==0) cout<<j<<' ';
     else{
         output(i,path[i][j]);
         output(path[i][j],j);
     }
 }


https://www.cnblogs.com/dolphin0520/archive/2011/08/27/2155542.html
2. path[i][j]=path[k][j]; //path[i][j]记录从i到j的最短路径上j的前一个顶点

void showPath(int path[N][M],int s,int t)    //打印出最短路径
{
    stack<int> st;
    int v=t;
    while(t!=s)
    {
        st.push(t);
        t=path[s][t];
    }
    st.push(t);
    while(!st.empty())
    {
        cout<<st.top()<<"";
        st.pop();
    }
}


"""

INF = 999

def floyed(matrix):

    N = len(matrix)
    path = [[-1]*N]*N
    print path
    for k in xrange(0, N):
        for i in xrange(0, N):
            for j in xrange(0, N):
                # none of (i, j, k) are same
                if (len(set([i, j, k])) == 3 and
                        matrix[i][k] != INF and matrix[k][j] != INF):
                    #matrix[i][j] = min(matrix[i][k] + matrix[k][j], matrix[i][j])
                    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
                        path[i][j] = k
        print "matrix after a k loop: k = ", k
        for l in matrix:
            print l
        print "here is path: "
        for l in path:
            print l

    return path

def print_path(path, i, j):
    if i == j:
        return
    if path[i][j] == -1:
        return
    print_path(path, i, path[i][j])
    print_path(path, path[i][j], j)


if __name__ == '__main__':
    matrix1 = [
           [0, 2, 6, 4],
           [INF, 0, 3, INF],
           [7, INF, 0, 1],
           [5, INF, 12, 0]]
    output_matrix = [
           [0, 2, 5, 4],
           [9, 0, 3, 4],
           [6, 8, 0, 1],
           [5, 7, 10, 0]]

    floyed(matrix1)
    print matrix1
    assert matrix1 == output_matrix
