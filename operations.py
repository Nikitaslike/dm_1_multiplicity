from itertools import combinations, product, chain

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

def domain(R):
    """Область визначення (множина a для яких існує (a,b))"""
    return set(a for a, _ in R)

def range_rel(R):
    """Область значень (множина b для яких існує (a,b))"""
    return set(b for _, b in R)

def inverse_rel(R):
    """Обернене відношення R^{-1}"""
    return set((b, a) for a, b in R)

# ------------------ БУЛЕАН ------------------

def boolean_table_set(elements):
    """
    Друкує булеву таблицю.
    """
    n = len(elements)
    table = [list(bits) for bits in product([0, 1], repeat=n)]
    
    print(" ".join(str(e) for e in elements))
    for row in table:
        print(" ".join(str(b) for b in row))
    
    return table

def boolean_power(elements):
    """
    Повертає булеан множини (усі підмножини).
    """
    elems = list(elements)
    power_set = list(chain.from_iterable(
        combinations(elems, r) for r in range(len(elems)+1)
    ))
    return [set(s) for s in power_set]

# ------------------ ДЕКАРТОВИЙ ДОБУТОК ------------------

def cartesian_product(A, B):
    """Повертає декартів добуток у вигляді списку (з порядком)"""
    return [(a, b) for a in A for b in B]

# ------------------ БІНАРНІ ВІДНОШЕННЯ ------------------

def relation_matrix(A, B, relation):
    """Створює матрицю для відношення R ⊆ A×B за функцією relation(a,b)"""
    return [[1 if relation(a, b) else 0 for b in B] for a in A]

def print_matrix(matrix, A, B):
    """Друк матриці відношення з підписами рядків і стовпців"""
    header = "    " + " ".join(str(b).rjust(3) for b in B)
    print(header)
    for i, a in enumerate(A):
        row = " ".join(str(matrix[i][j]).rjust(3) for j in range(len(B)))
        print(str(a).rjust(3), row)

def union_rel(R1, R2):
    return R1 | R2

def intersection_rel(R1, R2):
    return R1 & R2

def complement_rel(R, A, B):
    """Доповнення відношення: (A×B) \\ R"""
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