class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def printlist(self):
        temp=self.head
        mylist=[]
        while temp:
            answers=temp.data
            temp=temp.next
            mylist.append(answers)
        x=len([i for i in mylist if i=="ha" or i=="no"])
        if x !=len(mylist):
            print("Only 'ha' or 'no' allowed")

        ha=len([i for i in mylist if i=="ha"])
        no=len([i for i in mylist if i=="no"])
        s=ha+no
        ha_s=100*ha/s
        no_s=100*no/s
        if ha_s>no_s:
            print("Your life is good!Percentage {}%, please don't stop".format(ha_s))
        elif ha_s==no_s:
            print("Your life is not bad:-|Percentage 50%!Please, hard work")
        elif no_s>ha_s:
            print("Your life is bad:( Percentage {}%".format(no_s))
        print("Thank you for your attention:)")




"""This is for time"""
l=[]
for i in range(7,24,2):
   l.append(i)
l.pop()
a=l[::2]
b=l[1::2]
c=dict(zip(a,b))
print(c) #->{7: 9, 11: 13, 15: 17, 19: 21}

list=LinkedList()
"""Questions"""
list.head = Node(input(f"{a[0]}:00-{b[0]}:00 gacha dsaturchilik bilan shug'ullanmoqchisiz(ha/no)? "))
tushlik=Node(input(f"{a[1]}:00-{b[1]}:00 oraliqda tushlikka chiqasizmi(ha/no)? "))
sport=Node(input(f"{a[2]:02d}-{b[2]:02d}:00 vaqt oralig'ida sport bilan shug'ullanasizmi(ha/no)? "))
dam=Node(input(f"{a[3]}:00-{b[3]}:00 vaqt oralig'ida dam olasizmi(ha/no)?: "))
game=Node(input(f"Ertaga {a[1]}:00 dan {a[2]}:45 gacha kompyuter o'yinlarini o'ynaysizmi(ha/no)? "))


"""Don't forget to tie this knots"""
list.head.next=tushlik
tushlik.next=sport
sport.next=dam
dam.next=game
"""Don't forget to tie this knots"""

list.printlist() #->Main function()
