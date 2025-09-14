# ------------------ ОПЕРАЦІЇ НАД МНОЖИНАМИ ------------------

def union(A, B):
    return set(A) | set(B)  # A ∪ B

def intersection(A, B):
    return set(A) & set(B)  # A ∩ B

def difference(A, B):
    return set(A) - set(B)  # A \ B

def symmetric_diff(A, B):
    return set(A) ^ set(B)  # A ⊕ B

def complement(A, U):
    return set(U) - set(A)  # U \ A

# ------------------ ДЕКАРТОВИЙ ДОБУТОК ------------------

def cartesian_product(A, B):
    """Повертає декартів добуток у вигляді списку (з порядком)"""
    return [(a, b) for a in A for b in B]

# ------------------ БІНАРНІ ВІДНОШЕННЯ ------------------

def relation_matrix(A, B, relation):
    """Створює матрицю для відношення R ⊆ A×B за функцією relation(a,b)"""
    return [[1 if relation(a, b) else 0 for b in B] for a in A]

def print_matrix(matrix, A, B):
    header = "   " + " ".join(str(b) for b in B)
    print(header)
    for i, a in enumerate(A):
        row = " ".join(str(val) for val in matrix[i])
        print(str(a).rjust(2), row)

def union_rel(R1, R2):
    return R1 | R2

def intersection_rel(R1, R2):
    return R1 & R2

def complement_rel(R, A, B):
    """Доповнення відношення: (A×B) \ R"""
    return set((a, b) for a in A for b in B) - R

def composition_rel(R, S, A, B, C):
    """
    Композиція S∘R, де
    R ⊆ A×B
    S ⊆ B×C
    Повертає множину пар (a, c).
    """
    result = set()
    for a in A:
        for c in C:
            if any(((a, b) in R) and ((b, c) in S) for b in B):
                result.add((a, c))
    return result

# ------------------ МАТРИЧНА КОМПОЗИЦІЯ ------------------

def composition_matrix(R_mat, S_mat):
    """
    Композиція відношень у вигляді матриць.
    R_mat: |A| × |B|
    S_mat: |B| × |C|
    SR = булевий добуток: (a,c)=1, якщо ∃b: R[a][b]=1 і S[b][c]=1
    """
    A_size, B_size = len(R_mat), len(R_mat[0])
    C_size = len(S_mat[0])
    SR = [[0] * C_size for _ in range(A_size)]

    for i in range(A_size):
        for k in range(C_size):
            for j in range(B_size):
                if R_mat[i][j] and S_mat[j][k]:
                    SR[i][k] = 1
                    break  
    return SR