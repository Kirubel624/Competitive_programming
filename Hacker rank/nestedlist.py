if __name__ == '__main__':
    n = int(input())
    students = []

    for _ in range(n):
        name = input()
        grade = float(input())
        students.append([name, grade])

    students.sort(key=lambda x: (x[1], x[0]))

    second_lowest_grade = sorted(set(grade for name, grade in students))[1]

    for name, grade in students:
        if grade == second_lowest_grade:
            print(name)
