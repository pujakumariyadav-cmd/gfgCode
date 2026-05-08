'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self, head1, head2):
        dummy = Node(0)
        cur = dummy
        while head1 and head2:               
            if head1.data < head2.data:
                cur.next = head1
                head1, cur = head1.next, head1
            else:
                cur.next = head2
                head2, cur = head2.next, head2
                
        if head1 or head2:
            cur.next = head1 if head1 else head2
            
        return dummy.next

        