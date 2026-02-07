print("hello world")

def chai(n):
    print(n)

chai("lemon chai")
chai("green tea")
chai = "lemon tea"
print(chai)
lemon tea

first_char = chai[0] 
print(first_char)  
slice_chai = chai[0:6]
print(slice_chai)






 chai 

lemon tea
>>> print(chai.upper()) 
LEMON TEA
>>> chai =   " lemon tea"
>>> chai
' lemon tea'
>>> print(chai.strip())
lemon tea
>>> chai = "masala tea"
>>> chai
'masala tea'
>>> print(chai.replace("lemon", "ginger"))
masala tea
>>> print(chai.replace("masala", "ginger"))     
ginger tea
>>> chai = "lemon, ginger, green"
>>> print(chai.split())
['lemon,', 'ginger,', 'green']
>>> print(chai.split(", "))
['lemon', 'ginger', 'green']
>>> chai = "lemon tea"
>>> print(chai.find("chai"))  
-1
>>>
>>> chai = "lemon chai"
>>> print(chai.find("chai"))
6
>>> chai_type = "lemon"
>>> quantity = 2
>>> order = "i ordered {} cup of {} chai"
>>> order
'i ordered {} cup of {} chai'
>>> print(order.format(quantity, chai_type)
... print(order.format(quantity, chai_type))
 
>>> print(order.format(quantity, chai_type))
i ordered 2 cup of lemon chai
>>> chai_variety = ["lemon", "ginger", "green"]
>>> chai_variety
['lemon', 'ginger', 'green']
>>> print(" ".join(chai_variety)) 
lemon ginger green
>>> chai_variety   