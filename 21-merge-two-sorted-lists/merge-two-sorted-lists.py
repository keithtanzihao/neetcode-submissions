# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        node1 = list1
        node2 = list2
        if list2.val <= list1.val:
            node1 = list2
            node2 = list1
        # Let node1 be always list with starting lower val
        head_merge = node1
        curr_node = node1

        node1 = node1.next
        
        while True:
            # If both run out i.e. None return ref to head            
            if not node1 and not node2:
                return head_merge

            elif node1 and not node2:
                curr_node.next = node1
                node1 = node1.next
                
            elif node2 and not node1:    
                curr_node.next = node2
                node2 = node2.next            
                
            elif node2.val <= node1.val:
                curr_node.next = node2
                node2 = node2.next
                
            else: # node1.val < node2.val
                curr_node.next = node1
                node1 = node1.next
                
            curr_node = curr_node.next
            
            