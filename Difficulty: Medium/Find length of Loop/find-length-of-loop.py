'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        slow , fast = head , head
        
        while fast and fast.next:
            slow = slow.next          
            fast = fast.next.next    
        

            if slow == fast: 
                count = 1
                temp = slow.next
                while temp != slow:
                    count += 1
                    temp = temp.next
                return count

        return 0
        