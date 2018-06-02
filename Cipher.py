class AtbashCipher(object):

    start =65
    end = start+25
    midpoint = (end-start)//2+65
    def __init__(self):
        self.cipher = {chr(x):chr(self.end-(x-self.start))for x in range(self.start,self.midpoint+1)}

    def change(self, sentence):
        newSentence = [];
        sentence = sentence.upper()
        for word in sentence:
            for i in word:
                if(i in self.cipher.keys()):
                    newSentence.append(list(self.cipher.values())[list(self.cipher.keys()).index(i)])
                elif (i in self.cipher.values()):
                    newSentence.append(list(self.cipher.keys())[list(self.cipher.values()).index(i)])
                else: newSentence.append(' ')
        return "".join(newSentence)
    def getStart(self):
        return self.start

class LinkedList(object):

    class Node(object):
        data = None
        next=None
        def __init__(self,data=None):
            self.data = data
        def setNext(self,nextNode):
            self.next=nextNode
        def __str__(self):
            return super().__str__()+", Data:"+str(self.data)

    head = Node(None)
    def __init__(self,item):
        self.head = self.Node(item)
    def append(self,dataAppended):
        head = self.head
        if(head is None):
            head = self.Node(dataAppended);
        while(head.next is not None):
            head = head.next
        head.setNext(self.Node(dataAppended))

    def size(self):
        head = self.head
        count = 1
        while (head.next is not None):
            count+=1
            head = head.next
        return count

    length = size

    def appendBeginning(self, data):
        if(self.head==None):
            self.head=self.Node(data)
            return
        self.head, tempHead = self.Node(data), self.head
        self.head.setNext(tempHead)

    def __str__(self):
        s = ""
        node = self.head
        while(node is not None):
            s+=str(node.data)
            node = node.next
            if(node is not None):s+="->"

        return s

    def insert(self,index,data):
        if(index<=0):
            self.appendBeginning(data)
            return
        elif(index>self.size()):
            self.append(data)
            return
        nodeToAdd = self.Node(data)
        nodePrev=None
        nodeTraversed = self.head
        i = 0
        while(i<index):
            nodeTraversed,nodePrev = nodeTraversed.next,nodeTraversed
            i+=1
        nodePrev.setNext(nodeToAdd)
        nodeToAdd.setNext(nodeTraversed)

    def reverse(self):
        if(self.size()==0 or self.size()==1): return
        prevNode, node = self.head, self.head.next
        prevNode.next = None
        while(node is not None):
            tempNext = node.next
            node.next = prevNode
            prevNode = node
            node = tempNext
        self.head = prevNode

    def reverseRecur(self,node):
        if(node.next is None):
            self.head.next=None
            self.head = node
        else:
            newHead = self.reverseRecur(node.next)
            newHead.next = node
        return node



    def get(self,index):
        if(index>=self.size()):
            return -1
        node,i = self.head,0
        while(i<index):
            node=node.next
            i+=1
        return node.data

    def remove_position(self,index):
        if(index==0):
            head = self.head
            self.head = self.head.next
            return head.data
        elif(index>=self.size() or index<0):
            return -1
        i=0
        prevNode=None
        nodeToTraverse = self.head
        while(i<index):
            prevNode = nodeToTraverse
            nodeToTraverse = nodeToTraverse.next
            i+=1
        prevNode.next = nodeToTraverse.next
        return nodeToTraverse.data

    def remove_object(self,value):
        prevNode = None
        nodeToTraverse = self.head
        while (nodeToTraverse.next is not None):
            if (nodeToTraverse.data == value):
                break
            prevNode = nodeToTraverse
            nodeToTraverse = nodeToTraverse.next
        else:
            return None
        prevNode.next = nodeToTraverse.next
        return nodeToTraverse.data

    def swap_positions(self, pos1, pos2):
        first,second = self.get(pos1), self.get(pos2)
        self.replace(pos1,second)
        self.replace(pos2,first)

    def replace_index(self,index,data):
        self.remove_position(index)
        self.insert(index,data)

    def removeFirst(self):
        return self.remove_position(0)
    def removeLast(self):
        return self.remove_position(self.size()-1)


test = LinkedList(0)
test.append(1)
test.append(2)
print(test)
test.reverseRecur(test.head)
#test.reverse()
print(test)

#x = 5 if l.size()>8 else 0

"""
c = AtbashCipher()
print (c.change(input("Input:\n")))
print(c.primeNumberGen(6))

"""
