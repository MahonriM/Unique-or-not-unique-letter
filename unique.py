#Develop by MahonriM
#Don`t forget to follow me in YouTube as chumixGaming
uniquestring="AbCdEf"
nonuniquestr="Non uug gyyy"
n3="Repetido valor Repetido si jala eso lo veremos"
def uniqueornot(str):
    str=str.replace(" ","").lower()
    list=[]
    for i in str:
        if i in list:
            return False
        elif i not in list:
            list.append(i)
    return True
print(uniqueornot(uniquestring))
print(uniqueornot(nonuniquestr))
print(uniqueornot(n3))
