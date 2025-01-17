# -*- coding: utf-8 -*-
"""Binary_Search.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NyvnE2eFOi5bPBFw5fVnVG9RZ2GmwFpK

# **Binary_Search**
"""

# Iterative Method
def bin_search(arr,target):
  arr.sort()
  n=len(arr)
  low=0
  high=n-1
  while(low<=high):
    mid=(low+high)//2
    if arr[mid]==target:
      return mid
    # When target is not in left half of array
    elif target>arr[mid]:
      low=mid+1
    else:
      high=mid-1
  return -1
arr=[3,1,2,10,9,5,6]
bin_search(arr,6)

# Recursive Method
def bina_search(arr,low,high,target):
  arr.sort()
  if low>high:
    return -1
  mid=(low+high)//2
  if arr[mid]==target:
    return mid
  elif target > arr[mid]:
    return bina_search(arr,mid+1,high,target)
  else:
    return bina_search(arr,low,mid-1,target)
arr=[3,1,2,10,9,5,6]
low=0
high=len(arr)-1
target=6
bina_search(arr,low,high,target)

"""# **Implement Lower Bound**
*   Smallest index such that: **arr[index]>=n**
*   n=Number for which find the lower bound


"""

def lower_bound(arr,n):
  arr.sort()
  low=0
  high=len(arr)-1
  ans=len(arr)
  while(low<=high):
    mid=(low+high)//2
    # May be mid is answer
    if arr[mid]>=n:
      ans=mid
      # Look for smaller index on left
      high=mid-1
    else:
      # Look for right
      low=mid+1
  return "Index Number at which given number > or = to given number : ",ans
arr=[1,2,3,4,5]
n=4
lower_bound(arr,n)

"""# **Implement Upper Bound**
*   Smallest index such that: **arr[index]>n**
*   n=Number for which find the Upper bound
"""

def upper_bound(arr,n):
  arr.sort()
  low=0
  high=len(arr)-1
  ans=len(arr)
  while(low<=high):
    mid=(low+high)//2
    # May be mid is answer
    if arr[mid]>n:
      ans=mid
      # Look for smaller index on left
      high=mid-1
    else:
      # Look for right
      low=mid+1
  return "Its index number :",ans
arr=[1,2,3,4,5]
n=4
upper_bound(arr,n)

"""# **Search Insert Position**
* Find the index at which Insert an number in its correct position in sorted array
"""

# that is equal to find the lower bound
def lower_bound(arr,n):
  arr.sort()
  low=0
  high=len(arr)-1
  ans=len(arr)
  while(low<=high):
    mid=(low+high)//2
    # May be mid is answer
    if arr[mid]>=n:
      ans=mid
      # Look for smaller index on left
      high=mid-1
    else:
      # Look for right
      low=mid+1
  return ans
arr=[1,2,3,4,5]
n=4
lower_bound(arr,n)

"""# **Floor and Ceil**
* Floor : Largest number in array <= n

* Ceil : Smallest number in array >=n
"""

def ceil(arr,n):
  arr.sort()
  low=0
  high=len(arr)-1
  ans=-1
  while(low<=high):
    mid=(low+high)//2
    # May be mid is answer
    if arr[mid]>=n:
      ans=arr[mid]
      # Look for smaller index on left
      high=mid-1
    else:
      # Look for right
      low=mid+1
  return ans
arr=[10,20,30,25,40]
ceil(arr,21)

def floor(arr,n):
  arr.sort()
  low=0
  high=len(arr)-1
  ans=-1
  while(low<=high):
    mid=(low+high)//2
    # May be mid is answer
    if arr[mid]<=n:
      ans=arr[mid]
      # Look for smaller index on right
      low=mid+1
    else:
      # Look for left
      high=mid-1
  return ans

arr=[10,20,30,25,40]
floor(arr,21)

"""# **First and Last Occurrences in Array**"""

# Method 1
# TC:O(n)
# SC:O(1)
n=int(input("Enter the number to find the occurance : "))
arr=[2,4,6,8,8,8,9,11,13]
arr.sort()
first=-1
last=-1
for i in range(len(arr)):
  if arr[i]==n:
    #check for first occurance
    if first==-1:
      first=i
      last=i
    else:
      last=i
print(first,last)

# Method 2
# TC:2*(log2^n)
# SC:O(1)
def lower_bound(arr,n):
  arr.sort()
  low=0
  high=len(arr)-1
  ans=len(arr)
  while(low<=high):
    mid=(low+high)//2
    # May be mid is answer
    if arr[mid]>=n:
      ans=mid
      # Look for smaller index on left
      high=mid-1
    else:
      # Look for right
      low=mid+1
  return ans

def upper_bound(arr,n):
  arr.sort()
  low=0
  high=len(arr)-1
  ans=len(arr)
  while(low<=high):
    mid=(low+high)//2
    # May be mid is answer
    if arr[mid]>n:
      ans=mid
      # Look for smaller index on left
      high=mid-1
    else:
      # Look for right
      low=mid+1
  return ans

n=int(input("Enter the number to find the occurance : "))
arr=[2,4,6,8,8,8,9,11,13]
lb=lower_bound(arr,n)
ub=upper_bound(arr,n)
if lb==n or arr[lb]!=n:
  print(-1,-1)
else:
  print(lb,ub-1)

# Method 3
# TC:2*(log2^n)
# SC:O(1)
def first_occure(arr,x):
  first=-1
  arr.sort()
  low=0
  high=len(arr)-1
  while low<=high:
    mid=(low+high)//2
    if arr[mid]==x:
      first=mid
      high=mid-1
    elif arr[mid]<x:
      low=mid+1
    else:
      high=mid-1
  return first

def last_occurance(arr,x):
  arr.sort()
  last=-1
  low=0
  high=len(arr)-1
  while(low<=high):
    mid=(low+high)//2
    if arr[mid]==x:
      last=mid
      low=mid+1
    elif arr[mid]<x:
      low=mid+1
    else:
      high=mid-1
  return last

n=int(input("Enter the number to find the occurance : "))
arr=[2,4,6,8,8,8,9,11,13]
first=first_occure(arr,n)
last=last_occurance(arr,n)
if first==-1:
  print(-1,-1)
else:
  print(first,last)

"""#**Count occurrences in Array**"""

# Method 1
# TC:2*(log2^n)
# SC:O(1)
def first_occure(arr,x):
  first=-1
  arr.sort()
  low=0
  high=len(arr)-1
  while low<=high:
    mid=(low+high)//2
    if arr[mid]==x:
      first=mid
      high=mid-1
    elif arr[mid]<x:
      low=mid+1
    else:
      high=mid-1
  return first

def last_occurance(arr,x):
  arr.sort()
  last=-1
  low=0
  high=len(arr)-1
  while(low<=high):
    mid=(low+high)//2
    if arr[mid]==x:
      last=mid
      low=mid+1
    elif arr[mid]<x:
      low=mid+1
    else:
      high=mid-1
  return last

n=int(input("Enter the number to find the occurance : "))
arr=[2,4,6,8,8,8,9,11,13]
first=first_occure(arr,n)
last=last_occurance(arr,n)
if first==-1:
  print(0)
else:
  print(last-first+1)

"""# **Search Element in Rotated Sorted Array - I**
* Find the index number where the array is rotated
* Array must have unique elements
"""

# Method 1
# TC: O(n)
# SC: O(1)
n=int(input('Enter the target : '))
arr=[7,8,9,1,2,3,4,5,6]
for i in range(len(arr)):
  if arr[i]==n:
    print(i)

# Method 2
# TC: O(log2^n)
# SC: O(1)
n=int(input('Enter the target : '))
arr=[7,8,9,1,2,3,4,5,6]
def rotated_arr(arr,n):
  low=0
  high=len(arr)-1
  while(low<=high):
    mid=(low+high)//2
    if arr[mid]==n:
      return mid
    # left half of array are sorted
    if arr[low]<=arr[mid]:
      # Check if element in left half
      if arr[low]<=n and n<=arr[mid]:
        high=mid-1
      else:
        low=mid+1
    # Right half of array are sorted
    else:
      # Check if element in right half
      if arr[mid]<=n and n<=arr[high]:
        low=mid+1
      else:
        high=mid-1
  return mid
rotated_arr(arr,n)

"""# **Search Element in Rotated Sorted Array - 2**
* Find the element in the array is present or not
* Array may or may not have unique elements
"""

# Method 1
# TC: O(log2^n)
# SC: O(1)
n=int(input('Enter the target : '))
arr=[3,3,9,3,3,3,3]
def rotated_arr(arr,n):
  low=0
  high=len(arr)-1
  while(low<=high):
    mid=(low+high)//2
    if arr[mid]==n:
      return True
    if arr[low]==arr[mid] and arr[mid]==arr[high]:
      low=low+1
      high=high-1
      continue
    # left half of array are sorted
    if arr[low]<=arr[mid]:
      # Check if element in left half
      if arr[low]<=n and n<=arr[mid]:
        high=mid-1
      else:
        low=mid+1
    # Right half of array are sorted
    else:
      # Check if element in right half
      if arr[mid]<=n and n<=arr[high]:
        low=mid+1
      else:
        high=mid-1
  return False
rotated_arr(arr,n)

"""# **Minimum in Rotated Sorted Array**"""

import math
def find_min(arr):
  low=0
  high=len(arr)-1
  ans=math.inf
  while low<=high:
    mid=(low+high)//2
    if arr[low]<=arr[mid]:
      ans=min(ans,arr[low])
      low=mid+1
    else:
      high=mid-1
      ans=min(ans,arr[mid])
  return ans
arr=[5,6,7,1,2,3]
find_min(arr)

"""# **Find out how many times array has been rotated**"""

import math
def find_min(arr):
  low=0
  high=len(arr)-1
  ans=math.inf
  index=-1
  while low<=high:
    mid=(low+high)//2
    if arr[low]<=arr[mid]:
      if arr[low]<ans:
        ans=arr[low]
        index=low
      low=mid+1
    else:
      high=mid-1
      ans=min(ans,arr[mid])
      index=mid
  return index
arr=[4,5,6,7,1,2,3]
find_min(arr)

"""# **Single Element in Sorted Array**"""

# Method 1
# TC : O(n)
arr=[1,1,2,2,3,3,4,4,5,5,6,6,7]
n=len(arr)
if n==1:
  print(arr[0])
for i in range(n):
  if i==0:
    if arr[i]!=arr[i+1]:
      print(arr[i])
      break
  elif i==n-1:
    if arr[i]!=arr[i-1]:
      print(arr[i])
      break
  else:
    if arr[i]!=arr[i+1] and arr[i]!=arr[i-1]:
      print(arr[i])
      break

# Method 1
# TC : O(log2^n)
arr=[1,1,2,2,3,3,4,5,5,6,6]
n=len(arr)
if n==1:
  print(arr[0])
if arr[0]!=arr[1]:
  print(arr[0])
if arr[n-1]!=arr[n-2]:
  print(arr[n-1])
low=1
high=n-2
while(arr[low]<=arr[high]):
  mid=(low+high)//2
  if arr[mid]!=arr[mid-1] and arr[mid]!=arr[mid+1]:
    print(arr[mid])
  if (mid%2==1 and arr[mid]==arr[mid-1]) or (mid%2==0 and arr[mid]==arr[mid+1]):
    low=mid+1
  else:
    high=mid-1

"""# **Find Peak Element**"""

arr=[1,2,3,4,5,7,6]
n=len(arr)
for i in range(n):
  if (i==0 or arr[i-1]<arr[i]) and (i==n-1 or arr[i]>arr[i+1]):
    print(arr[i])
    break

"""## **Finding Apporximate Sqrt of a number using Binary Search**"""

#Method 1
# TC: O(n)
# SC: O(1)
n=int(input("Enter a number to find squar root : "))
ans=1
for i in range(n):
  if i*i <=n:
    ans=i
  else:
    break
print(ans)

#Method 1
# TC: O(log2^n)
# SC: O(1)
n=int(input("Enter a number to find squar root : "))
ans=1
low=1
high=n
while low<=high:
  mid=(low+high)//2
  val=mid*mid
  if val<=n:
    ans=mid
    low=mid+1
  else:
    high=mid-1
print(high)

"""# **Find the Nth root of an Integer**


1.   m=27 and n=3 then find 3root(27)=3
2.   List item m=64 and n=3 find 3root(64)=4


"""

# Method 1
# TC:O(n*log2^n)
n=int(input("Enter Number to find the root : "))
n_root=int(input("Enter a which root you find : "))
x=(lambda i,n_root:i**n_root)
for i in range(1,n+1):
  # Responsible for log2^n
  if x(i,n_root)==n:
    print(i)
    break
  elif x(i,n_root)>n:
    print(-1)
    break

# Method 2
# TC:O(log2^n*log2^n)
n=int(input("Enter Number to find the root : "))
n_root=int(input("Enter a which root you find : "))
x=(lambda a,b:a**b)
low=1
high=n
while low<=high:
  mid=(low+high)//2
  if x(mid,n_root)==n:
    print(mid)
    break
  elif x(mid,n_root)>n:
    high=mid-1
  else:
    low=mid+1
else:
  print(-1)

"""## **Koko Eating Bananas**


*   Given an list of banana and hours
*   You need to find the min eat banana per hour withen given hours


"""

# Method 1
# TC: O(max(arr)*len(arr))
# SC: O(1)
import math
arr=[3,6,7,11]
h=8
def eat_hr(arr,h):
  m=max(arr)
  m_hr=0
  i=1
  while i<m:
    for j in arr:
      m_hr+=math.ceil(j/i)
    if m_hr==h:
      print(i)
      break
    i+=1
    m_hr=0
eat_hr(arr,h)

# Method 2
# TC: O(log2^(max(arr))*len(arr))
# SC: O(1)
import math
def eat_banana(arr,epr):
  total_hour=0
  for i in arr:
    total_hour+=math.ceil(i/epr)
  return total_hour

def bs_eat_banana(arr,h):
  low=0
  high=max(arr)
  ans=0
  while low<=high:
    mid=(low+high)//2
    total_hour=eat_banana(arr,mid)
    if total_hour<=h:
      ans=mid
      high=mid-1
    else:
      low=mid+1
  return ans
arr=[3,6,7,11]
h=8
bs_eat_banana(arr,h)

"""## **Minimum days to make M bouquets**"""

# Method 1
# TC O(mini-maxi+1)*N
def possible(arr,day,m,k):
  n=len(arr)
  count=0
  no_of_bk=0
  for i in range(n):
    if arr[i]<=day:
      count+=1
    else:
      no_of_bk+=count/k
      count=0
  no_of_bk+=count/k
  if no_of_bk>=m:
    return True
  else:
    return False

arr=[7,7,7,7,13,11,12,7]
m=2
k=3
mini=min(arr)
maxi=max(arr)
for i in range(mini,maxi+1):
  if possible(arr,i,m,k)==True:
    print(i)
    break
else:
  print(-1)

# Method 2
# TC O(log2^(maxi-min+1))*N
def possible(arr,day,m,k):
  n=len(arr)
  count=0
  no_of_bk=0
  for i in range(n):
    if arr[i]<=day:
      count+=1
    else:
      no_of_bk+=count/k
      count=0
  no_of_bk+=count/k
  if no_of_bk>=m:
    return True
  else:
    return False


def bn_possible(arr,m,k):
  low=min(arr)
  high=max(arr)
  ans=0
  while low<=high:
    mid=(low+high)//2
    if possible(arr,mid,m,k)==True:
      ans=mid
      high=mid-1
    else:
      low=mid+1
  return ans

arr=[7,7,7,7,13,11,12,7]
m=2
k=3
bn_possible(arr,m,k)

"""## **Find the Smallest Divisor Given a Threshold**"""

# Method 1
# TC: O(maxi)*(len(arr))
# SC: O(1)
import math
def fnd_diviser(arr,thresold):
  mini=min(arr)
  maxi=max(arr)
  temp=0
  while mini<=maxi:
    for i in arr:
      temp+=math.ceil(i/mini)
    if temp<=thresold:
      return mini
    temp=0
    mini+=1
  return -1
arr=[1,2,5,9]
thresold=6
fnd_diviser(arr,thresold)

# Method 1
# TC: O(log2^(max))*O(n)
# SC: O(1)
import math
def bn_fnd_diviser(arr,thresold):
  low=min(arr)
  high=max(arr)
  sum=0
  ans=0
  while low<=high:
    mid=(low+high)//2
    for i in arr:
      sum+=math.ceil(i/mid)
    if sum<=thresold:
      ans=mid
      high=mid-1
    else:
      low=mid+1
    sum=0
  return ans
arr=[1,2,5,9]
thresold=4
bn_fnd_diviser(arr,thresold)

"""## **Capacity to Ship Packages within D Days**"""

# Method 1
# TC: O(s-maxi+1)*(n)
# SC: O(1)
def load_ship(wt,cap):
  days=1
  load=0
  maxi=max(wt)
  s=sum(wt)
  for i in range(len(wt)):
    if load+wt[i]>cap:
      days+=1
      load=wt[i]
    else:
      load+=wt[i]
  return days

wt=[1,2,3,4,5,6,7,8,9,10]
days=5
maxi=max(wt)
s=sum(wt)

for i in range(maxi,s+1):
  if load_ship(wt,i)<=days:
    print(i)
    break
else:
  print(-1)

# Method 1
# TC: O(log2^(s-maxi+1))*(n)
# SC: O(1)
def load_ship(wt,cap):
  days=1
  load=0
  maxi=max(wt)
  s=sum(wt)
  for i in range(len(wt)):
    if load+wt[i]>cap:
      days+=1
      load=wt[i]
    else:
      load+=wt[i]
  return days

def bn_load(wt,days):
  low=max(wt)
  high=sum(wt)
  ans=0
  while low<=high:
    mid=(low+high)//2
    if load_ship(wt,mid)<=days:
      ans=mid
      high=mid-1
    else:
      low=mid+1
  return ans

wt=[1,2,3,4,5,6,7,8,9,10]
days=5
bn_load(wt,days)

"""## **Kth Missing Positive Number**"""

# Method 1
# TC: O(n)
# SC: O(1)
arr=[2,3,4,7,11]
k=5
for i in arr:
  if i<=k:
    k+=1
  else:
    print(k)
    break

# Method 2
# TC: O(log2^n)
# SC: O(1)
def bn_missing(arr,k):
  low=0
  high=len(arr)-1
  while low<=high:
    mid=(low+high)//2
    missing=arr[mid]-(mid+1)
    if missing<k:
      low=mid+1
    else:
      high=mid-1
  return low+k
arr=[2,3,4,7,11]
k=5
bn_missing(arr,k)

"""## **Aggressive Cows**


*   Min distance between two cows are maximum


"""

# Method 1
# TC: O(max-min)(n)
# SC: O(1)
def can_we_place(arr,dist,cows):
  cnt_cows=1
  last_cow=arr[0]
  for i in range(1,len(arr)):
    if arr[i]-last_cow>=dist:
      cnt_cows+=1
      last_cow=arr[i]
  if cnt_cows>=cows:
    return True
  else:
    False

arr=[0,3,4,7,9,10]
cows=4
arr.sort()
maxi=max(arr)
mini=min(arr)
for i in range(1,((maxi-mini)+1)):
  if can_we_place(arr,i,cows)==True:
    continue
  else:
    print(i-1)
    break

# Method 2
# TC: O(log2^(max-min))(n)
# SC: O(1)
def can_we_place(arr,dist,cows):
  cnt_cows=1
  last_cow=arr[0]
  for i in range(1,len(arr)):
    if arr[i]-last_cow>=dist:
      cnt_cows+=1
      last_cow=arr[i]
  if cnt_cows>=cows:
    return True
  else:
    False


def bn_fnd_min_of_max(arr,cows):
  low=0
  high=max(arr)-min(arr)
  ans=0
  while low<=high:
    mid=(low+high)//2
    if can_we_place(arr,mid,cows)==True:
      ans=mid
      low=mid+1
    else:
      high=mid-1
  return ans
arr=[0,3,4,7,9,10]
cows=4
bn_fnd_min_of_max(arr,cows)

"""## **Allocate Books or Book Allocation**"""

# Method 1
# TC: O(sum(arr)-max(arr)+1)*(n)
# SC: O(1)

def max_page_allow(arr,pages):
  student=1
  no_of_page=0
  for i in arr:
    if no_of_page+i<=pages:
      no_of_page+=i
    else:
      student+=1
      no_of_page=i
  return student

arr=[25,46,28,49,24]
student=4
mini=max(arr)
maxi=sum(arr)
for pages in range(mini,maxi+1):
  cnt_student=max_page_allow(arr,pages)
  if cnt_student==student:
    print(pages)
    break

# Method 2
# TC: O(log2^(sum(arr)-max(arr)+1))*(n)
# SC: O(1)

def max_page_allow(arr,pages):
  student=1
  no_of_page=0
  for i in arr:
    if no_of_page+i<=pages:
      no_of_page+=i
    else:
      student+=1
      no_of_page=i
  return student

arr=[25,46,28,49,24]
student=4
def bn_fnd_pages(arr):
  low=max(arr)
  high=sum(arr)
  while low<=high:
    mid=(low+high)//2
    no_of_page=max_page_allow(arr,mid)
    if no_of_page>student:
      low=mid+1
    else:
      high=mid-1
  return low
arr=[25,46,28,49,24]
student=4
bn_fnd_pages(arr)

"""## **Painter's Partition and Split Array - Largest Sum**


*   Split the array into k subarray such that max of sum subarray is minimum



"""

def max_page_allow(arr,pages):
  student=1
  no_of_page=0
  for i in arr:
    if no_of_page+i<=pages:
      no_of_page+=i
    else:
      student+=1
      no_of_page=i
  return student

arr=[25,46,28,49,24]
student=4
def bn_fnd_pages(arr):
  low=max(arr)
  high=sum(arr)
  while low<=high:
    mid=(low+high)//2
    no_of_page=max_page_allow(arr,mid)
    if no_of_page>student:
      low=mid+1
    else:
      high=mid-1
  return low
arr=[10,20,30,40]
student=2
bn_fnd_pages(arr)

"""## **Median of two Sorted Arrays of Different Sizes**"""

# Method 1
# TC: O(n1+n2)
# SC: O(n)

arr1=[1,3,5,7,9]
arr2=[2,4,6,8,10]
n1=len(arr1)
n2=len(arr2)
ans=[]
i=0
j=0
while(i<n1 and j<n2):
  if arr1[i]<arr2[j]:
    ans.append(arr1[i])
    i+=1
  else:
    ans.append(arr2[j])
    j+=1
while i<n1:
  ans.append(arr1[i])
  i+=1
while j<n2:
  ans.append(arr2[j])
  j+=1
print(ans)

n=len(ans)
if n%2==1:
  print("Median is : ",ans[n//2])
else:
  print("Median is : ",(ans[n//2]+ans[n//2-1])/2)

# Method 2
# TC: O(n1+n2)
# SC: O(n)
arr1=[1,3,5,7,9]
arr2=[2,4,6,8,10]
n1=len(arr1)
n2=len(arr2)
n=n1+n2
ind2=n//2
ind1=ind2-1
cnt=0
ind_ele1,ind_ele2=-1,-1
i=0
j=0
while i<n1 and j<n2:
  if arr1[i]<arr2[j]:
    if cnt==ind1:
      ind_ele1=arr1[i]
    if cnt==ind2:
      ind_ele2=arr1[i]
    cnt+=1
    i+=1
  else:
    if cnt==ind1:
      ind_ele1=arr2[j]
    if cnt==ind2:
      ind_ele2=arr2[j]
    cnt+=1
    j+=1
while i<n1:
  if cnt==ind1:
    ind_ele1=arr1[i]
  if cnt==ind2:
    ind_ele2=arr1[i]
  cnt+=1
  i+=1
while j<n2:
  if cnt==ind1:
    ind_ele1=arr2[j]
  if cnt==ind2:
    ind_ele2=arr2[j]
  cnt+=1
  j+=1

if n%2==1:
  print(ind_ele2)
else:
  print((ind_ele2+ind_ele1)/2)

"""## **Row with maximum number of 1s**"""

# Method 1
# TC: O(row*col)
arr=[[0,0,0,0],
     [0,1,1,1],
     [0,1,1,1],
     [1,1,1,1]]
row=len(arr)
col=len(arr[0])
max_cnt=1
ind=-1
for i in range(row):
  cnt=0
  for j in range(col):
    if arr[i][j]==1:
      cnt+=arr[i][j]
  if cnt>max_cnt:
    max_cnt=cnt
    ind=i
print(ind)

# Method 2
# TC: O(nlog2^m)
def lower_bound(arr,m):
  low=arr[0]
  high=arr[len(arr)-1]
  ans=len(arr)
  while low<=high:
    mid=(low+high)//2
    if arr[mid]>=m:
      high=mid-1
      ans=mid
    else:
      low=mid+1
  return mid

arr=[[0,0,0,0],
     [0,1,1,1],
     [0,1,1,1],
     [1,1,1,1]]
def fnd_max_ones(arr):
  cnt_max=0
  ind=-1
  for i in range(len(arr)):
    no_element=len(arr[i])
    cnt_one=no_element-lower_bound(arr[i],1)
    if cnt_one>cnt_max:
      cnt_one=cnt_max
      ind=i
  return ind

fnd_max_ones(arr)

"""## **Search in a 2D Matrix - I**"""

# Method 1
# TC : O(len(row)*len(col))
# SC: O(1)
arr=[[3,4,7,9],
     [12,14,17,19],
     [20,23,27,29]]
n=23
def fnd_element(arr):
  for row in arr:
    for ele in row:
      if ele==n:
        return True
  return False
fnd_element(arr)

# Method 1 Without function
# TC : O(len(row)*len(col))
# SC: O(1)
arr=[[3,4,7,9],
     [12,14,17,19],
     [20,23,27,29]]
n=21
flag=False
for i in arr:
  for j in i:
    if j==n:
      flag=True
      break
print(flag)

# Method 2 Using Binary search
# TC : O(n)+log2^m
# SC: O(1)
def bn_search_matrix(arr,target):
  low=0
  high=len(arr)-1
  while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
      return True
    elif arr[mid]>target:
      high=mid-1
    else:
      low=mid+1
  return False

arr=[[3,4,7,9],
     [12,14,17,19],
     [20,23,27,29]]
target=23
n=len(arr)
m=len(arr[0])
flag=False
for i in range(n):
  if arr[i][0]<=target and target<=arr[i][m-1]:
    flag=bn_search_matrix(arr[i],target)
print(flag)

# Method 1 Without function
# TC : O(log2^(m*n))
# SC: O(1)

def bin_search_in_matrix(mat,target):
  n=len(mat)
  m=len(mat[0])
  low=0
  high=(n*m)-1
  while low<=high:
    mid=(low+high)//2
    row=mid//m
    col=mid%m
    if mat[row][col]==target:
      return True
    elif mat[row][col]<target:
      low=mid+1
    else:
      high=mid-1
  return False

mat=[[3,4,7,9],
     [12,14,17,19],
     [20,23,27,29]]
target=2
bin_search_in_matrix(mat,target)

"""## **Search in a 2D Matrix - II**


*   Entire Matrix are not sorted
*   Every row and column are sorted itself


"""

# Method 1
# TC : O((m*n))
# SC: O(1)


mat=[[1,4,7,11,15],
     [2,5,8,12,19],
     [3,6,9,16,22],
     [10,13,14,17,24],
     [18,21,23,26,30]]
target=14
n=len(mat)
m=len(mat[0])
ans=[]
for i in range(n):
  for j in range(m):
    if mat[i][j]==target:
      print(i,j)

# Method 2
# TC : O(nlog2^(m))
# SC: O(1)

def bn_search_matrix(arr,target):
  low=0
  high=len(arr)-1
  while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
      return mid
    elif arr[mid]>target:
      high=mid-1
    else:
      low=mid+1
  return -1

mat=[[1,4,7,11,15],
     [2,5,8,12,19],
     [3,6,9,16,22],
     [10,13,14,17,24],
     [18,21,23,26,30]]
target=30
n=len(mat)
for i in range(n):
  ind=bn_search_matrix(mat[i],target)
  if ind!=-1:
    print(i,ind)

# Method 1 Without function
# TC : O((m+ n))
# SC: O(1)

mat=[[1,4,7,11,15],
     [2,5,8,12,19],
     [3,6,9,16,22],
     [10,13,14,17,24],
     [18,21,23,26,30]]
target=30
def search_in_matrix(mat,target):
  col=len(mat[0])-1
  row=0
  n=len(mat)
  while row<n and col>0:
    if mat[row][col]==target:
      return row,col
    elif mat[row][col]<target:
      row+=1
    else:
      col-=1
  return -1,-1

search_in_matrix(mat,target)

"""## **Find Peak Element-II | Binary Search**
* all Adjustent value must be less than the elemnet then it call pick element
"""

def fnd_max_index(mat,n,m,col):
  maxval=-1
  ind=-1
  for i in range(n):
    if mat[i][col]>maxval:
      maxval=mat[i][col]
      ind=i
  return ind

def pick_element(mat,n,m):
  low=0
  high=m-1
  while low<=high:
    mid=(low+high)//2
    max_row_ind=fnd_max_index(mat,n,m,mid)
    if mid-1>=0:
      left= mat[max_row_ind][mid-1]
    else:
      left= -1
    if mid+1<m:
      right=mat[max_row_ind][mid-1]
    else:
      right=-1

    if mat[max_row_ind][mid]>left and mat[max_row_ind][mid]>right:
      return (max_row_ind,mid)
    elif mat[max_row_ind][mid-1]<left:
      high=mid-1
    else:
      low=mid+1
  return (-1,-1)

mat=[[9, 2, 3], [4, 5, 6], [7, 8, 10]]
n=len(mat)
m=len(mat[0])
pick_element(mat,n,m)































