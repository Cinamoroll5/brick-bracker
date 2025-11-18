#list.py

from enum import member


snacks=["marshmelows", "oreo","chocolate" ,"lolipop"]
scores=[100,200,300,400,500,600,700,800,900,1000.]


#getting a item
#remember we strt counting from 0
print(snacks)
print(scores)
print(scores[4])

#getting length of a list
print(len(snacks))

#change an item

snacks[0]="biscutes"
print(snacks)


#removing any item
snacks.remove("biscutes")
print(snacks)
 #removing last item
snacks.pop()
print(snacks)