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

llist_1 = linkedList()
llist_2 = linkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.mergeSorted(llist_2)
llist_1.print_list()
