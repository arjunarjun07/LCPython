from collections import deque


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.link = None
    
    def __repr__(self) -> str:
        return "[{0}]->({1})".format(self.data, self.link)
    
# Definition for a Node.
class NodeX:
    def __init__(self, x: int, next: 'NodeX' = None, random: 'NodeX' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class CLinkedList:
    
    def __init__(self) -> None:
        self.head = None
        
    def __repr__(self) -> str:
        
        res = []
        
        p = self.head
        while p:
            res.append(p.data)
            p = p.link

        return " -> ".join(res)
    
    def insert_begin(self, data):
        
        n = Node(data)
        
        if self.head is None:
            self.head = n
        else:
            n.link = self.head
            self.head = n
            
    def insert_end(self, data):
        
        n = Node(data)
        
        if self.head is None:
            self.head = n
        else:
            
            t = self.head
            
            while t:
                prev = t
                t = t.link
                
            prev.link = n
            
    def insert_after(self, data_to_search, data_to_insert):
        
        t = self.head
        while t:
            if t.data == data_to_search:
                break            
            t = t.link
        
        if t:
            n = Node(data_to_insert)
            n.link = t.link
            t.link = n
            
    def remove(self, data_to_del) -> bool:
        
        if self.head is None:
            return True

        if self.head.data == data_to_del:
            t = self.head
            self.head = self.head.link

            t.link = None
            del t
            return True
    
        t = self.head
        
        #if we try to remove the head node. We have to point head again properly
        prev = self.head
        
        while t and t.data != data_to_del:
            prev = t
            t = t.link
        
        #pointing prev node to t.link 
        prev.link = t.link
        
        #del node
        t.link = None
        del t
        return True
        
            
        
        
cl = CLinkedList()

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head:ListNode) -> ListNode:
        
        if head == None:
            return head
        
        prevN = None
        CurrN = head
        NextN = None
        
        while CurrN:
            
            NextN = CurrN.next
            CurrN.next = prevN
            prevN = CurrN
            
            CurrN = NextN
            
        return prevN
    
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        dummy_node = ListNode()
        temp = dummy_node
        
        while list1 and list2:
            
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next #we can safely move the listnode1 to point nxt
                
            else:
                temp.next = list2
                list2 = list2.next #we can safely move the listnode2 to point nxt
                
            #imp step - we need to move temp pointer 
            temp = temp.next
        
        if list1:
            temp.next = list1
        
        elif list2:
            temp.next = list2
            
        return dummy_node.next
    
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #find middle of list
        #reverse the second half
        #2way merge on two lists
        
        def findMid(head:ListNode)-> ListNode:
            
            p = head
            q = head
            
            #For even list - mid may be like [1,2,3,4] - len(list)//2 = 4/2 - There is no mid for even. If we want start of 2st half - use case 1, else we can get end of the 1st half - use case 2  
                       
            # case 1: (q and q.next) This will retrun the mid+1 of the list - start of 2st half
            # case 2: (q.next and q.next.next) This will return the mid of the list - end of the 1st half
            
            while (q.next and q.next.next): 
                p = p.next
                q = q.next.next
            
            return p
        
        mid_end_of_1sthalf = findMid(head)
        
        second_half_head = mid_end_of_1sthalf.next
        mid_end_of_1sthalf.next = None
        
        second_half_head = self.reverseList(second_half_head)        
        
        #merge two sub-half list
        th1 = head
        th2 = second_half_head
        
        while th1 and th2:
            
            th1Nxt = th1.next
            th2Nxt = th2.next
            
            th1.next = th2            
            th1.next.next = th1Nxt
            
            th1 = th1Nxt
            th2 = th2Nxt
            
            
        return head
    
    def removeNthFromEnd(self, head:ListNode, n: int) -> ListNode:  
        
        lenN = 0
        
        curr = head
        while curr:
            lenN += 1
            curr = curr.next
        
        print(lenN)
        
        xthNode = lenN - n
        
        if xthNode != 0:  
            indx = 1  
            curr = head
            while curr and indx < xthNode:
                curr = curr.next
                indx += 1
                
            node_to_del = curr.next
            curr.next = node_to_del.next
            
            node_to_del.next = None
            del(node_to_del)

        else:
            temp = head
            head = head.next
            del(temp)

        return head
    
    def copyRandomList(self, head: NodeX) -> NodeX:
        
        newH = None
        prev = None
        curr = head
        
        src_addr_pos_map = {}
        dst_pos_addr_map = {}
        
        #creating duplicate with actual next links
        
        indx = 1
        while curr:
            newN = NodeX(curr.val)
            
            if newH == None:
                newH = newN
                prev = newN
            else:
                prev.next = newN
                prev = prev.next
                
            dst_pos_addr_map.update({indx: prev})
            src_addr_pos_map.update({curr: indx})
            
            curr = curr.next
            indx += 1
        
        currsrc = head 
        currdst = newH
        
        while currsrc:
            
            rnd = currsrc.random
            srcpos = src_addr_pos_map.get(rnd)
            dstaddr = dst_pos_addr_map.get(srcpos)
            
            currdst.random = dstaddr
            
            currdst = currdst.next
            currsrc = currsrc.next
            
        print(newH)
        return newH
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        newlistH = None
        currPtrNewList = None


        def getdigit(dat1, dat2) -> int:
            
            nonlocal carry
            
            dig = dat1 + dat2 + carry
            carry = 0
            
            if dig >= 10:
                
                if dig == 10:
                    dig = 0
                    
                    carry = 1
                else:
                    d = dig

                    carry += (d//10)
                    dig = d % 10
                    
            return dig
        
        def InsertNode(data):
            
            nonlocal newlistH
            nonlocal currPtrNewList
            
            if newlistH == None:
                
                newlistH = ListNode(data)
                currPtrNewList = newlistH
            else:
                
                currPtrNewList.next = ListNode(data)
                currPtrNewList = currPtrNewList.next
            
      
        h1 = l1
        h2 = l2
        
        while h1 and h2:
            
            sum_of_dig = getdigit(h1.val, h2.val)
                        
            InsertNode(sum_of_dig)
            
            h1 = h1.next
            h2 = h2.next        
            
        while h1:
            sum_of_dig = getdigit(h1.val, 0)
            InsertNode(sum_of_dig)
            h1 = h1.next
            
        while h2:
            sum_of_dig = getdigit(h2.val, 0)
            InsertNode(sum_of_dig)            
            h2 = h2.next
            
        if carry != 0:
            InsertNode(carry)
            
        print(newlistH)
        return newlistH
    
    def hasCycle(self, head: ListNode) -> bool:
        
        curr = head
        indx = 1
        
        addr_pos = {}
        
        while curr:
            
            if curr not in addr_pos.keys():
                addr_pos.update({curr:indx})          
                curr = curr.next
                indx += 1
            else:
                return True
        
        return False
    
    def findDuplicate(self, nums: list[int]) -> int:

        hmap = {}
        indx = 0
        for each_elem in nums:

            if each_elem not in hmap.keys():
                hmap.update({each_elem:indx})
                indx += 1
            else:
                return each_elem
        return -1
    
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        
        if lists.__len__() == 0:
            return None
        
        if lists.__len__() == 1:
            return lists[0]
        
        while len(lists) > 1:
            
            mergedlist = []
            
            for i in range(0, len(lists), 2):
                
                #we need to merge the k sorted list using 2-way merge
                #on each pass we use 2 lists
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                
                mergedlist.append(self.mergeTwoLists(l1, l2))
            
            lists = mergedlist
            
        return lists[0]
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if head is None:
            return None
        
        dummyN = ListNode(0, head)
        
        i = 1
        currN = head
        nxtN = currN.next
        prevN = dummyN
        
        while currN:
            
            if i == k:
                
                i = 0
                
                _1stnodeoflistBeforeRev = prevN.next
                currN.next = None
                
                temp = self.reverseList(_1stnodeoflistBeforeRev)
                
                _1stnodeoflistBeforeRev.next = nxtN
                prevN.next = temp
                prevN = _1stnodeoflistBeforeRev
            
            i += 1            
            currN = nxtN
            
            if currN:
                nxtN = currN.next
            
        return head         
                    
s = Solution()

class DNode:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def __repr__(self) -> str:
        
        res = []
        
        p = self.head
        while p:
            res.append(p.data)
            p = p.next

        return str(res)
    
    def InsertFront(self, data):
        
        node = DNode(data)
        
        if self.head == None:
            
            self.head = node
            self.tail = node
        
        else:
            
            node.next = self.head
            node.next.prev = node
            self.head = node
            
    def InsertEnd(self, data):
                
        if self.head is None:
            self.InsertFront(data)
            
        else:
            node = DNode(data)    
            
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
    
    def InsertMiddle(self, data_to_insert, insert_after):
        
        curr = self.head
        
        while curr:
            
            if insert_after == curr.data:
                                
                node = DNode(data_to_insert)

                node.next = curr.next
                node.prev = curr
                
                curr.next.prev = node
                curr.next = node
                
                break
            
            curr = curr.next
            
    def DelFront(self):
        
        if self.head is not None:
            
            temp = self.head
            
            if self.head.next:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None
                
            temp.next = None
            del(temp)
            

    def DelBack(self):
        
        if self.head == None:
            return
        
        if self.head == self.tail:
            self.DelFront()       
        else:
            
            temp = self.tail
            
            self.tail.prev.next = None
            self.tail = self.tail.prev
            
            temp.prev = None
            del(temp)
            
    def DelMiddle(self, data_to_del):
        
        curr = self.head
        
        while curr:
            
            if curr.data == data_to_del:
                
                if curr == self.head:
                    self.DelFront()
                elif curr == self.tail:
                    self.DelBack()
                else:
                    
                    temp = curr
                    
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    
                    temp.next = None
                    temp.prev = None
                    del(temp)
                
                break
            
            curr = curr.next    
    
class NodeDLL:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = NodeDLL(0, 0), NodeDLL(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = NodeDLL(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
s = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

val = s.reverseKGroup(n1, 2)
print(val)