# class node:
#     def __init__(self,value):
#         self.value=value
#         self.next=None

# e1=node(4)
# e2=node(6)
# e3=node(8)
# e4=node(9)

# e1.next=e2
# e2.next=e3
# e3.next=e4
# print(e1.next.next.next.value)
# print(e2.next.next.value)

class node1:
    def __init__(self,value):
        self.value=value
        self.next=next

e1=node1(4)
e2=node1(6)
e3=node1(8)
e4=node1(9)

e1.next=e2
e2.next=e3
e3.next=e4

p1=e1
while p1.next!=None:
    print(p1.value)
    p1=p1.next



