# 例2、判断平方数
"""1、问题描述：给定一个正整数num，判断是否为完全平方数，要求当num为完全平方数是返回True否则返回False
2、问题示例：输入num=16,输出True, sqrt(16)=4；输入num=15,输出False,sqrt(15)=3.87
3、代码实现：
"""


class Solution:
    def isPerfectSquare(self, num):
        a = 0
        r = num
        while (r - a > 1):
            mid = (a + r) / 2
            if (mid * mid <= num):
                a = mid
            else:
                r = mid
        ans = a
        if (a * a < num):
            ans = r
        return ans * ans == num
    
# 主函数
if __name__ == '__main__':
    num = 16
    print("初始值：", num)
    solution = Solution()
    print("结果：", solution.isPerfectSquare(num))
                
