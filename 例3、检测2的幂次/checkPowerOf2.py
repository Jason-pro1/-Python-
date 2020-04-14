# 例3、检测2的幂次
"""1、问题描述：检测一个整数n是否为2的幂次。
2、问题示例： n=4,返回True；n=5,返回False

"""
# 代码实现：
# 采用UTF-8编码格式
# 参数n是一个整数
# 返回True或者False
class Solution:
    def checkPowerOf2(self, n):
        ans = 1
        for i in range(31):
            if ans == n:
                return True
            ans <<= 1  # 位运算 ans = ans << 1
        return False
if __name__ == "__main__":
    temp = Solution()
    nums1 = 16
    nums2 = 62
    print(("输入：" + str(nums1)))
    print(("s输出：" + str(temp.checkPowerOf2(nums1))))
    print(("输入：" + str(nums2)))
    print(("s输出：" + str(temp.checkPowerOf2(nums2))))
