def linearsearch(arr,find):
    count=0
    for i in arr:
        if i == find:
            count+=1
    return count

arr=list(map(int,input().split()))
find = int(input())
print(linearsearch(arr,find))