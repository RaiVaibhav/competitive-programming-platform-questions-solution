X = int(input().strip())
Y = int(input().strip())
mat = [[0]*Y for _ in range(X)]
for i in range(X):
    mat[i] = [int(j) for j in input().strip().split(" ")]
tran_mat = [[mat[j][i] for j in range(X)] for i in range(Y)]
print(tran_mat)