class Solution:
    def numTrees(self, n: int) -> int:
        #计算以1...n为节点组成的二叉树有多少种
        #动态规划
        #假设n个节点存在二叉排序树的个数是G(n)，令f(i)
        #为以i为根的二叉搜索树的个数
        #即有: G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)
        #n为根节点，当i为根节点时，其左子树节点个数为[1, 2, 3, ..., i - 1]
        #右子树节点个数为[i + 1, i + 2, ...n]
        #所以当i为根节点时，其左子树节点个数为i - 1个，右子树节点为n - i
        #即f(i) = G(i - 1) * G(n - i),
        #上面两式可得: G(n) = G(0) * G(n - 1) + G(1) * (n - 2) + ... + G(n - 1) * G(0)

        if n < 1:
            return 1
        num = [0] * (n+1)
        num[0] = num[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                num[i] += num[j] *num[i-j-1]
        return num[-1]
