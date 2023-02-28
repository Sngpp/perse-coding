ranklist=['1st','2nd','3rd','4th','5th']
mylist=[]
for i in range(5):
    value = input()
    mylist.append(value)
rk=mylist.index('Ellie')
print(ranklist[rk])
