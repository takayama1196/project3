from typing import List

def selectionSort(arr: List[int]):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
print("Selection Sort:", selectionSort([80, 93, 2, 41, 50]))


def bubbleSort(arr: List[int]):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print("Bubble Sort:", bubbleSort([80, 93, 2, 41, 50]))


def insertSort(arr: List[int]):
    n = len(arr)
    for i in range(n):
        current = arr[i]
        j = i - 1
        while current < arr[j] and j >0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr
print("Insert Sort:", insertSort([80, 93, 2, 41, 50]))


def countingSort(arr: List[int], r: int):
    count = [0] * (r + 1)
    for x in arr:
        count[x] += 1
    index = 0
    for v in range(r + 1):
        while count[v] > 0:
            arr[index] = v
            index += 1
            count[v] -= 1
    return arr
print("Counting Sort:", countingSort([80, 93, 2, 41, 50], 93))


def quickSort(arr: list[int]):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)
print("Quick Sort:", quickSort([80, 93, 2, 41, 50]))


# 鏈表節點定義
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 解法類別
class Solution:
    # 合併排序主函式
    def mergesort(self, head: ListNode):
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        return self.merge(self.mergesort(head), self.mergesort(head2))

    # 合併兩個已排序鏈表
    def merge(self, head1: ListNode, head2: ListNode):
        zero = ListNode(-1)
        current = zero
        while head1 and head2:
            if head1.val <= head2.val:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next
        current.next = head1 if head1 else head2
        return zero.next

# 生成鏈表
head = ListNode(80, ListNode(93, ListNode(2, ListNode(41, ListNode(50)))))

# 建立 Solution 實例，排序鏈表
sol = Solution()
sorted_head = sol.mergesort(head)

# 輸出排序後的鏈表結果
current = sorted_head
while current:
    print(current.val, end=" ")
    current = current.next



