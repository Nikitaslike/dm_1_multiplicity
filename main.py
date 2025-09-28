from operations import (
    union, intersection, difference, symmetric_diff, complement,
    boolean_table_set, cartesian_product,
    relation_matrix, print_matrix,
    union_rel, intersection_rel, complement_rel, composition_rel, composition_matrix, boolean_power, domain, range_rel, inverse_rel
)

def read_elements(prompt, as_relation=False, to_set=False):
    """
    Універсальна функція зчитування:
    - as_relation=True → читає відношення [(a,b),...]
    - to_set=True → повертає множину замість списку
    """
    raw = input(prompt).strip()
    if not raw:
        return set() if to_set else []

    def smart_cast(x: str):
        try:
            return int(x)
        except ValueError:
            return x

    if as_relation:
        rel = []
        for el in raw.split():
            el = el.strip("()[]")
            a, b = el.split(",")
            rel.append((smart_cast(a), smart_cast(b)))
        return set(rel) if to_set else rel
    else:
        elems = [smart_cast(el) for el in raw.split()]
        return set(elems) if to_set else elems

if __name__ == "__main__":
    U = read_elements("Введіть універсальну множину U (елементи через пробіл): ", to_set=True)
    A = read_elements("Введіть множину A: ", to_set=True)
    B = read_elements("Введіть множину B: ", to_set=True)
    C = read_elements("Введіть множину C: ", to_set=True)

    R = read_elements("Введіть відношення R (елементи у вигляді [a,b]): ", as_relation=True, to_set=True)
    S = read_elements("Введіть відношення S (елементи у вигляді [b,c]): ", as_relation=True, to_set=True)
    
    print("\n№1")

    print("\n--- Операції над множинами ---")
    print("A ∪ B =", union(A, B))
    print("A ∩ B =", intersection(A, B))
    print("A \\ B =", difference(A, B))
    print("B \\ A =", difference(B, A))
    print("A ⊕ B =", symmetric_diff(A, B))
    print("¬A =", complement(A, U))
    print("¬B =", complement(B, U))
    
    print("\n№2")

    print("\n--- Булеан множини ---")
    print("Булеан множини A:")
    boolean_table_set(list(A))

    print("Булеан множини B:")
    boolean_table_set(list(B))

    print("Потужність множини P(A) =", boolean_power(A))
    print("Потужність множини P(B) =", boolean_power(B))

    print("\n---Декартовий добуток ---")
    print("A × B = ", cartesian_product(A, B))
    print("B × A = ", cartesian_product(B, A))
    print("A² = ", cartesian_product(A, A))
    print("B² = ", cartesian_product(B, B))
    
    print("\n№3")
    
    print("\nОбласть визначення R:", domain(R))
    print("Область значень R:", range_rel(R))
    print("Обернене відношення R^{-1}:", inverse_rel(R))

    print("\n--- Бінарне відношення R ⊆ A×B (матриця) ---")
    R_mat = relation_matrix(A, B, lambda a, b: (a, b) in R)
    print_matrix(R_mat, list(A), list(B))

    print("\n--- Бінарне відношення S ⊆ B×C (матриця) ---")
    S_mat = relation_matrix(B, C, lambda b, c: (b, c) in S)
    print_matrix(S_mat, list(B), list(C))

    print("\n--- Композиція матриць R та S ---")
    S_mat = relation_matrix(B, C, lambda b, c: (b, c) in S)
    SR_mat = composition_matrix(R_mat, S_mat)
    print_matrix(SR_mat, list(A), list(C))