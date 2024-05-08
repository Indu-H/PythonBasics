if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    q = sorted(scores)#sort the scores in ascending order
    second_min = q[1]#take the second min value
    students = []#to store students who got the second_min grade
    for i in range(len(names)):
        if scores[i] == second_min:
            students.append(names[i])
    students.sort()#sorts the array in alphabetical order
    for i in students:
        print(i)


#Input 
#5
#Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39
# Output
#Berry
#Harry
