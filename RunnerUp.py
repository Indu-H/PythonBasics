if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    q = list(set(arr))#reamove the duplicates
    q.sort()#sorted it in ascending order
    print(q[len(q)-2])#print(q[-2])

#Input 
#5
#2 3 6 6 5
# Output
#5
