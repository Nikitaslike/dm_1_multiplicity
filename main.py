from operations import (
    union, intersection, difference, symmetric_diff, complement,
    cartesian_product, relation_matrix, print_matrix,
    composition_matrix
)
# def ordered(result_set, universe_list):
#     """Повертає список елементів result_set у порядку, як у universe_list"""
#     return [el for el in universe_list if el in result_set]

def smart_cast(x: str):
    """Перетворює елемент на int, якщо це число, інакше лишає як рядок"""
    try:
        return int(x)
    except ValueError:
        return x

def read_list(prompt):
    """Зчитування множини як списку (зберігає порядок)"""
    raw = input(prompt).strip()
    if not raw:
        return []
    return [smart_cast(el) for el in raw.split()]

def to_set(lst):
    """Перетворює список у множину (для операцій)"""
    return set(lst)

if __name__ == "__main__":
    print("🧮 МАТЕМАТИЧНІ ОПЕРАЦІЇ НАД МНОЖИНАМИ 🧮\n")

    U_list = read_list("Введіть універсальну множину U (елементи через пробіл): ")
    A_list = read_list("Введіть множину A: ")
    B_list = read_list("Введіть множину B: ")
    C_list = read_list("Введіть множину C: ")

    U, A, B, C = to_set(U_list), to_set(A_list), to_set(B_list), to_set(C_list)

    print("\nВихідні множини")
    print("U =", "{" + ", ".join(map(str, U_list)) + "}")
    print("A =", "{" + ", ".join(map(str, A_list)) + "}")
    print("B =", "{" + ", ".join(map(str, B_list)) + "}")
    print("C =", "{" + ", ".join(map(str, C_list)) + "}")

    print("\n--- Операції над множинами ---")
    print("A ∪ B =", sorted(union(A, B)))
    print("A ∩ B =", sorted(intersection(A, B)))
    print("A \\ B =", sorted(difference(A, B)))
    print("B \\ A =", sorted(difference(B, A)))
    print("A ⊕ B =", sorted(symmetric_diff(A, B)))
    print("¬A =", sorted(complement(A, U)))
    print("¬B =", sorted(complement(B, U)))

    print("\n--- Декартові добутки ---")
    print("A × B =", cartesian_product(A_list, B_list))
    print("\n")
    print("A² =", cartesian_product(A_list, A_list))
    print("\n")
    print("B² =", cartesian_product(B_list, B_list))
    print("\n")
    print("A² × B² =", cartesian_product(cartesian_product(A_list, A_list),
                                        cartesian_product(B_list, B_list)))

    print("\n--- Бінарне відношення R ⊆ A×B (A == B) ---")

    R = relation_matrix(A_list, B_list, lambda a, b: a == b)
    print_matrix(R, A_list, B_list)

    print("\n--- Бінарне відношення S ⊆ B×C (B == C) ---")
        
    S = relation_matrix(B_list, C_list, lambda b, c: str(b)[0] == str(c)[0])
    print_matrix(S, B_list, C_list)

    print("\n--- Композиція S∘R ---")
    SR = composition_matrix(R, S)
    print_matrix(SR, A_list, C_list)