def prefixarray(a):
  ar=[0 for _ in range(len(a))]
  s=0
  for i in range(len(a)):
    s+=a[i]
    ar[i]=s
  return ar
def range_sum(a,st,end):
  return a[end]-a[st-1]
a=[3,1,4,1,5,9,2,6]
prefix=prefixarray(a)
print(prefix)
print(range_sum(prefix, 2, 5))

def summary(a,k,target):
  s=0
  if k<=0 or k>=len(a):
    return 'invalid key elemnts'
  for i in range(k):
    s=s+a[i]
  if s==target:
    return [a[i] for i in range(k)]
  for i in range(k,len(a)):
    s=s+a[i]-a[i-k]
    if s==target:
      return [a[i] for i in range(i-k+1,i+1)]
  return -1
print(summary(a,3,10))