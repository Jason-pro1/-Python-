# 例1、完美平方
"""问题描述：给定一个正整数n，找到若干个完全平方数（例如：1,4,9，...），使得它们的和等于n，完全平方数的个数最少"""
"""问题示例：给出n = 12，返回3，因为12 = 4 + 4 + 4；给出n=13,返回2，因为 13 = 4 + 9"""
# 代码实现：
# 参数n是一个正整数
# 返回一个整数
class Solution:
    def numSquares(self, n):
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        for i in range(n + 1):
            temp = i * i
            if temp <=  n:
                if int((n - temp) ** 0.5) ** 2 + temp == n:
                    return 1 + (0 if temp == 0 else 1)
            else:
                break
        return 3
    
if __name__ == "__main__":
    n = 12
    print("初始值：", n)
    solution = Solution()
    print("结果：", solution.numSquares(n))
