from typing import Counter


class Node(): # node -> data with a starting and ending point
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class linkedList(): # linked list -> a bunch of nodes linked together
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data): # adding a node at the very end
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode
    
    def prepend(self, data): # adding a node at the beginning
        newNode = Node(data)
        
        newNode.next = self.head
        self.head = newNode
    
    def insertAfterNode(self, prevNode, data): # adding a node after a specific node
        if not prevNode:
            print('node does not exist')
            return
        
        newNode = Node(data)

        newNode.next = prevNode.next
        prevNode.next = newNode

    def delNodeKey(self, key): # delete node given key
        currentNode = self.head

        if currentNode and currentNode.data == key:
            self.head = currentNode.next
            currentNode = None
            return
        
        previousNode = None
        while currentNode and currentNode.data != key:
            previousNode = currentNode
            currentNode = currentNode.next

        if currentNode is None:
            return

        previousNode.next = currentNode.next
        currentNode = None 

    def delNodePos(self, pos): # delete node give position (index)
        if self.head:
            currentNode = self.head
            if pos == 0:
                self.head = currentNode.next
                currentNode = None
                return
            
            previousNode = None
            index = 0

            while currentNode and index != pos:
                previousNode = currentNode
                currentNode = currentNode.next
                index += 1

            if currentNode is None:
                return
            
            previousNode.next = currentNode.next
            currentNode = None

    def len_iterative(self): # finds the length by iterating through every node
        length = 0
        currentNode = self.head
        while currentNode:
            length += 1
            currentNode = currentNode.next

        return length

    def len_recursive(self, node): # finds the length through recursion
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swapNodes(self, key1, key2): # swaps two nodes given key
        
        if key1 == key2:
            return

        prev1 = None
        currentNode1 = self.head
        while currentNode1 and currentNode1.data != key1:
            prev1 = currentNode1
            currentNode1 = currentNode1.next
        
        prev2 = None
        currentNode2 = self.head
        while currentNode2 and currentNode2.data != key2:
            prev2 = currentNode2
            currentNode2 = currentNode2.next

        if not currentNode1 or currentNode2:
            return

        if prev1:
            prev1.next = currentNode2
        else:
            self.head = currentNode2

        if prev2:
            prev2.next = currentNode1
        else:
            self.head = currentNode1 

        currentNode1.next, currentNode2.next = currentNode2.next, currentNode1.next

    def reverse_iterative(self): # reverses the linked list iteratively
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def reverse_recursive(self): # reverses the linked list recursively
        def reverseRecursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return reverseRecursive(cur, prev)
        
        self.head = reverseRecursive(cur = self.head, prev = None)

    def print_list(self): # printing the linked list
        currentNode = self.head
        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next
    
    def mergeSorted(self, llist):
        
        p = self.head
        q = llist.head
        s = None
        
        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next 
                
            newHead = s
        
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p  
                p = s.next
            
            else:
                s.next = q
                s = q
                q = s.next
        
        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = newHead
        
        return self.head

    def removeDuplicates(self):
        cur = self.head
        prev = None
        dupes = []
        
        while cur:
            if cur.data in dupes:
                prev.next = cur.next
                cur = None
            else:
                dupes.append(cur.data)
                prev = cur
            cur = prev.next
   
    def nFromLast1(self, n):
        length = self.len_iterative()
        
        cur = self.head
        while cur:
            if length == n:
                return cur.data
            length -= 1
            cur = cur.next
        
        if cur is None:
            print(str(n), "is greater than the number of nodes in this list")
            return 
        
    def nFromlast2(self, n):
        p = self.head
        q = self.head
        
        if n > 0:
            count = 0
            while q:
                count += 1
                
                if count >= n:
                    break
                q = q.next
                
            if not q:
                print(str(n), "is greater than the number of nodes in this list")
                return

            while p and q.next:
                p = p.next
                q = q.next
            return p.data
        else:
            return None

    def countIterative(self, data):
        count = 0
        current = self.head
        
        while current:
            if current.data == data:
                count += 1
            
            current = current.next
        
        return count
        
    def countRecursive(self, node, data):
        if not node:
            return 0
        
        if node.data == data:
            return 1 + self.countRecursive(node.next, data)
        else:
            return 0 + self.countRecursive(node.next, data)
    
    def rotate(self, piv):
        p = self.head
        q = self.head
        prev = None
        count = 0
        
        while p and count < piv:
            prev = p
            p = p.next
            q = q.next
            count += 1
        
        p = prev
        
        while q:
            prev = q
            q = q.next
            
        q = prev
        
        q.next = self.head
        self.head = p.next
        p.next = None
        
    def isPalindrome1(self):
        string = ""
        p = self.head
        while p:
            string += p.data
            p = p.next
        
        return string == string[::-1]

    def isPalindrome2(self):
        p = self.head
        s = []
        
        while p:
            s.append(p.data)
            p = p.next

        p = self.head
        
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True
    
    def isPalindrome3(self):
        if self.head:
            p = self.head
            q = self.head
            prev = []
            
            i = 0
            
            while q:
                prev.append(q)
                q = q.next
                i += 1
            
            q = prev[i - 1]
            
            count = 1
            
            while count <= i // 2 + 1:
                if prev[-count].data != p.data:
                    return False

                p = p.next
                count += 1
            return True
        else:
            return True
    
    def moveTailToHead(self):
        if self.head and self.head.next:
            last = self.head
            secondtolast = None
            
            while last.next:
                secondtolast = last
                last = last.next
            
            last.next = self.head
            secondtolast.next = None
            self.head = last
    

    def sum_two_lists(self, llist):
        p = self.head  
        q = llist.head

        sum_llist = linkedList()

        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0 
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        return sum_llist.print_list()
    
llist1 = linkedList()
llist1.append(5)
llist1.append(6)
llist1.append(3)

llist2 = linkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)

print(365 + 248)
llist1.sum_two_lists(llist2)