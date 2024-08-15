print(f"{"Задача"} {'"Матрица воплоти"'}")

def get_matrix(n, m, value):
    matrix = []
    if n <= 0:
        print("Матрица пуста, задано неверное количество строк:", n)
    elif m <= 0:
        print("Матрица пуста, задано неверное количество столбцов:", m)
    else:
        for i in range(n):
            matrix.append([])
            for j in range(m):
                matrix[i].append(value)
        return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
