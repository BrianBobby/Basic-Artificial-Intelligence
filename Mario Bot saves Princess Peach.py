#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    mid=n//2
    temp=mid
    mario=grid[mid][mid]
    for i in range(n):
        for j in range(n):
            if grid[i][j]=="p":
                index1=i
                index2=j
    for i in range(n):
        if temp>index1:
            print("UP")
            temp-=1
        elif temp<index1:
            print("DOWN")
            temp+=1
        else:
            break
    temp=mid
    for i in range(n):
        if temp>index2:
            print("LEFT")
            temp-=1
        elif temp<index2:
            print("RIGHT")
            temp+=1
        else:
            break
    
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)