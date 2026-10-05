def linearsearch(a,el):
    ar=[]
    for i in range(len(a)):
        if a[i]==el:
           # print(f'{el} is found at {i} index')
            ar.append(i)
    return ar
a=[12,2,44,23,14,65,]
print(linearsearch(a,14))
