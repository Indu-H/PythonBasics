if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks[query_name]
    avg_marks = sum(marks)/3
    print("{:.2f}".format(avg_marks))

#Input 
#3
#Krishna 67 68 69
#Arjun 70 98 63
#Malika 52 56 60
#Malika
# Output
#56.00
