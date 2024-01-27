# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if(head == None):
            return None

        oddHead = None
        oddTemp = oddHead

        evenHead = None
        evenTemp = evenHead

        temp1 = head
        count = 0

        while(temp1 != None):
            if(count % 2 == 1):

                if(oddHead == None):
                    oddHead = ListNode(temp1.val)
                    oddTemp = oddHead
                else:    
                    oddTemp.next = ListNode(temp1.val)
                    oddTemp = oddTemp.next
            else:
                if(evenHead == None):
                    evenHead = ListNode(temp1.val)
                    evenTemp = evenHead
                else:
                    evenTemp.next = ListNode(temp1.val)
                    evenTemp = evenTemp.next
                
            temp1 = temp1.next
            count += 1
        
        evenTemp.next = oddHead
        return evenHead

                

def setup(vals) -> ListNode:
    head = ListNode(vals[0])
    temp = head
    for i in range(1, len(vals)):
        temp.next = ListNode(vals[i])
        temp = temp.next
    return head

def main():
    vals = [2,1,3,5,6,4,7]
    print(vals)
    head = setup(vals)
    test = Solution

    #out = head
    out = test.oddEvenList(test, head)

    temp = out
    while(temp != None):
        print(temp.val)
        temp = temp.next

if(__name__ == "__main__"):
    main()
        