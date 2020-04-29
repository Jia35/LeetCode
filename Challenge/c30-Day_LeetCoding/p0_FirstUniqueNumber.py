# First Unique Number
# You have a queue of integers, you need to retrieve the first unique integer in the queue.
from collections import Counter


class FirstUnique(object):

    def __init__(self, nums):
        self.ct = Counter(nums)
        self.cur = 0
        self.nums = nums

    def showFirstUnique(self):
        while self.cur < len(self.nums):
            if self.ct[self.nums[self.cur]] == 1:
                return self.nums[self.cur]
            self.cur += 1
        return -1

    def add(self, value):
        self.nums.append(value)
        if value not in self.ct:
            self.ct[value] = 1
        else:
            self.ct[value] += 1

# class FirstUnique(object):

#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.exist = set(nums)
#         self.unique_nums = []
#         for num in nums:
#             if nums.count(num) == 1:
#                 self.unique_nums.append(num)

#     def showFirstUnique(self):
#         """
#         :rtype: int
#         """
#         if not self.unique_nums:
#             return -1
#         else:
#             return self.unique_nums[0]

#     def add(self, value):
#         """
#         :type value: int
#         :rtype: None
#         """
#         if value not in self.exist:
#             self.unique_nums.append(value)
#             self.exist.add(value)
#         elif value in self.unique_nums:
#             self.unique_nums.remove(value)

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)


if __name__ == "__main__":
    firstUnique = FirstUnique([2,3,5])
    print(firstUnique.showFirstUnique())   # return 2
    firstUnique.add(5)
    print(firstUnique.showFirstUnique())   # return 2
    firstUnique.add(2)
    print(firstUnique.showFirstUnique())   # return 3
    firstUnique.add(3)
    print(firstUnique.showFirstUnique())   # return -1
