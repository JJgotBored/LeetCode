# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head:ListNode) -> int:
        count = 0
        arr = []
        temp = head
        max = 0

        while(temp != None):
            arr.append(temp.val)
            count += 1
            temp = temp.next

        for i in range(0, int(count/2)):
            if(arr[i] + arr[count -1 - i] > max):
                max = arr[i] + arr[count -1 -i]
        return max

def setup(vals: list) -> ListNode:
    if(vals == []):
        return None
    
    head = ListNode(vals[0])
    temp = head
    for i in range(1,len(vals)):
        temp.next = ListNode(vals[i])
        temp = temp.next
    return head

def main():
    vals =[4,2,2,3]
    print(vals)
    head = setup(vals)
    test = Solution
    print(test.pairSum(test, head))
    """
    temp = head
    while(temp != None):
        print(temp.val)
        temp = temp.next
    """

if(__name__ == "__main__"):
    main()