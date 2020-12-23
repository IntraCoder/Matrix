def mat_input(rows):  # Inputting rows in matrix
    mat = []
    for i in range(rows):
        row = eval(input(f"Enter row-{i + 1} in form of list:"))
        mat.append(row)
    return mat


def add_sub(mat_list, operation):
    for i in range(len(mat_list[0])):
        for j in range(len(mat_list[0][i])):
            for k in range(1, len(mat_list)):
                if operation == "add":
                    mat_list[0][i][j] += mat_list[k][i][j]
                elif operation == "sub":
                    mat_list[0][i][j] -= mat_list[k][i][j]
    return mat_list[0]


def multiply(mat_list):
    mat1, mat2 = mat_list[0], mat_list[1]
    result = []

    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            elem = 0
            for k in range(len(mat1[0])):
                elem += mat1[i][k] * mat2[k][j]
            row.append(elem)
        result.append(row)

    return result


def transpose(mat):
    t_mat = []
    for i in range(len(mat[0])):
        row = []
        for j in range(len(mat)):
            row.append(mat[j][i])
        t_mat.append(row)
    return t_mat


def determent(mat):
    if len(mat) == 3:
        a11 = mat[0][0] * (mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1])
        a12 = -mat[0][1] * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0])
        a13 = mat[0][2] * (mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0])
        det = a11 + a12 + a13

    elif len(mat) == 2:
        det = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    else:
        det = []
    return det


def adjoint(mat):
    if len(mat) == 3:
        adj_mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        adj_mat[0][0] = mat[1][1] * mat[2][2] - mat[1][2] * mat[2][1]
        adj_mat[0][1] = -1 * (mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0])
        adj_mat[0][2] = mat[1][0] * mat[2][1] - mat[1][1] * mat[2][0]
        adj_mat[1][0] = -1 * (mat[0][1] * mat[2][2] - mat[0][2] * mat[2][1])
        adj_mat[1][1] = mat[0][0] * mat[2][2] - mat[0][2] * mat[2][0]
        adj_mat[1][2] = -1 * (mat[0][0] * mat[2][1] - mat[0][1] * mat[2][0])
        adj_mat[2][0] = mat[0][1] * mat[1][2] - mat[0][2] * mat[1][1]
        adj_mat[2][1] = -1 * (mat[0][0] * mat[1][2] - mat[0][2] * mat[1][0])
        adj_mat[2][2] = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

        adj_mat = transpose(adj_mat)

    elif len(mat) == 2:
        adj_mat = mat
        adj_mat[0][0], adj_mat[1][1] = adj_mat[1][1], adj_mat[0][0]
        adj_mat[0][1], adj_mat[1][0] = -adj_mat[0][1], -adj_mat[1][0]

    else:
        adj_mat = []

    return adj_mat


def inverse(mat):
    if determent(mat) == 0:
        print("Inverse doesn't exist")
    else:
        return (adjoint(mat), determent(mat))


while True:
    print("***********************************  Matrix Operator ***********************************\n\n")
    print("Addition/Subtraction/Multiplication/Determenent/Transpose/Adjoint/Inverse/Quit")
    ask = input("Enter the operation:")

    if ask.lower() in ("addition", "subtraction"):
        try:
            matrices = []
            num = int(input("Enter number of Matrices:"))
            rows = int(input("Enter number of rows in each Matrix:"))
            for i in range(num):
                print(f"Matrix-{i + 1}")
                matrix = mat_input(rows)
                matrices.append(matrix)

            result = add_sub(matrices, ask[0:3].lower())
            print("Result:")
            for i in result:
                print(i)
        except:
            print("Please enter valid matrices of same order")

    elif ask.lower() == "multiplication":
        matrices = []
        for i in range(2):
            print(f"Matrix-{i + 1}")
            rows = int(input("Enter number of rows in Matrix:"))
            matrix = mat_input(rows)
            matrices.append(matrix)
        if len(matrices[0][0]) == len(matrices[1]):
            print("Product:")
            for i in multiply(matrices):
                print(i)
        else:
            print("Number of columns of matrix-1 should be equal to number of rows of matrix-2.")

    elif ask.lower() == "determenent":
        rows = int(input("Enter number of rows in Matrix:"))
        matrix = mat_input(rows)
        print("Determent:", determent(matrix))

    elif ask.lower() == "adjoint":
        row = int(input("Enter number of rows:"))
        matrix = mat_input(row)
        print("Adjoint:")
        for i in adjoint(matrix):
            print(i)

    elif ask.lower() == 'transpose':
        row = int(input("Enter number of rows:"))
        matrix = mat_input(row)
        print('Transpose:')
        for i in transpose(matrix):
            print(i)

    elif ask.lower() == "inverse":
        row = int(input("Enter number of rows in matrix:"))
        matrix = mat_input(row)
        if row != len(matrix[0]):
            print("Please enter Square Matrix!")
        else:
            for i in adjoint(matrix):
                print(i)
            print("Divide above matrix by", determent(matrix), "to get inverse.")
    elif ask.lower() == "quit":
        print("[+] Thankyou for visiting!")
        exit()
