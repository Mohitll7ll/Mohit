def insertion_sort(a):
     n=len(a)
     for i in range(1,n):
         x=a[i]
         j=i-1
         while j>=0 and x<a[j]:
             a[j+1]=a[j]
             j=j-1
         a[j+1]=x    
             
         

a=[5,2,4,1,3]
print("before")
print(a)
insertion_sort(a)
print("after")
print(a)
