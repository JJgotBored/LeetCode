# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        newHead = None
        temp = None
        iter = head

        while(iter != None):
            temp = iter
            iter = iter.next
            temp.next = newHead
            newHead = temp
        return newHead

def setup(vals) -> ListNode:
    if(vals == []):
        return None
    head = ListNode(vals[0])
    temp = head
    for i in range(1, len(vals)):
        temp.next = ListNode(vals[i])
        temp = temp.next
    return head

def main():
    vals = [1]
    print(vals)
    head = setup(vals)
    test = Solution

    out = test.reverseList(test, head)

    temp = out
    while(temp != None):
        print(temp.val)
        temp = temp.next

if(__name__ == "__main__"):
    main()