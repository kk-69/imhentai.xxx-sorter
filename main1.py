import itertools
import os
import string
a=list(string.ascii_lowercase[0:7])
a=list(itertools.permutations(a))
b=list(''.join(i) for i in a)
a=sorted(b)

path=input("path: ")
n=int(input("total files(5040 max): "))
file_type=input("file type(jpg,png,etc): ")
a=a[0:n]
b=list(range(1,n+1))
c=list(zip(b,a))
if os.path.exists(path):
    for i,j in c:
        os.rename(f'{path}\{i}.{file_type}',f'{path}\{j}.{file_type}')
        print(f'{path}\{i}.{file_type}   ---->   {path}\{j}.{file_type} ')
else:
    print("invalid path")
    exit()
