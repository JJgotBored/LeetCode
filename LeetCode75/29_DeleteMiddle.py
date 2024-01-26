#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        count = 0
        temp = head
        while(temp != None):
            count += 1
            temp = temp.next
        
        middle = int(count/2)

        count = 0
        temp = head
        while(count < middle-1):
            temp = temp.next
            count += 1

        temp2 = temp.next
        if(temp2 != None):
            temp.next = temp2.next
        else:
            head = None

        return head

def setup(vals) -> ListNode:
    head = ListNode(vals[0])
    temp = head
    for i in range(1, len(vals)):
        temp.next = ListNode(vals[i])
        temp = temp.next
    return head


def main():
    vals = [2]
    print(vals)
    head = setup(vals)
    test = Solution

    out = test.deleteMiddle(test, head)

    temp = out
    while(temp != None):
        print(temp.val)
        temp = temp.next

if(__name__ == "__main__"):
    main()
