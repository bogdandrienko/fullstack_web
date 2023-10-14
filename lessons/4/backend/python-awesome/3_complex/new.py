class Solution:
    @staticmethod
    def twoSum(nums: list[int], target: int) -> list[int]:
        # constant memory
        # <= log(N) [O(1), log(N), Nlog(N) - сортировка, O(N^2)]
        # два указателя
        #  1 2
        # [2,7,11,15]
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


print(Solution.twoSum([3, 3], 6))
print(Solution.twoSum([2, 7, 11, 15], 9))


def check_balanse1(text: str) -> bool:
    counter = 0
    for i in text:
        if i == ")":
            counter -= 1
            if counter < 0:
                return False
        elif i == "(":
            counter += 1
    return counter == 0


str6 = '())(()'  # False
str7 = '()'  # True
str8 = '()()'  # True
str9 = ')('  # False

print(check_balanse1(str6))
print(check_balanse1(str7))
print(check_balanse1(str8))
print(check_balanse1(str9))



def check_balanse2(text: str) -> bool:
    dict1 = {
        "(": 0,
        "{": 0,
        "[": 0,
    }
    counter = 0
    for i in text:
        # (
        if i == ")":
            dict1["("] -= 1
            if dict1["("] < 0:
                return False
        elif i == "(":
            dict1["("] += 1
        # {
        elif i == "}":
            dict1["{"] -= 1
            if dict1["{"] < 0:
                return False
        elif i == "{":
            dict1["{"] += 1
        # [
        elif i == "]":
            dict1["["] -= 1
            if dict1["["] < 0:
                return False
        elif i == "[":
            dict1["["] += 1
    for v in dict1.values():
        if v != 0:
            return False
    return True

str6 = '[{()}]'  # True
str7 = '[]'  # True
str8 = '[(}]'  # False
str9 = '(({}))'  # True
str10 = '(({}))('  # False
print(check_balanse2(str6))
print(check_balanse2(str7))
print(check_balanse2(str8))
print(check_balanse2(str9))
print(check_balanse2(str10))


def areBracketsBalanced(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()  # (
            if current_char == '(' and char != ")":
                return False
            if current_char == '{' and char != "}":
                return False
            if current_char == '[' and char != "]":
                return False
    if stack:
        return False
    return True

print("\n\n\n\n\n\n\n\n")
print(areBracketsBalanced(str6))
print(areBracketsBalanced(str7))
print(areBracketsBalanced(str8))
print(areBracketsBalanced(str9))
print(areBracketsBalanced(str10))
print(areBracketsBalanced("{()}[]"))
print(areBracketsBalanced("{()[]"))

# https://habr.com/ru/companies/kts/articles/727528/
# https://proglib.io/p/slozhnost-algoritmov-i-operaciy-na-primere-python-2020-11-03


list1 = ["admin@gmail.com", "bogdan@gmail.com", "admin@gmail.com", "bogdan@gmail.com", "bogdan@gmail.com"]

print(len(set(list1)))
list2 = []
for i in list1:  # > O(N)
    if i not in list2:
        list2.append(i)
print(list2)
