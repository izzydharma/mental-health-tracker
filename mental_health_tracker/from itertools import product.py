from itertools import product

# Language definitions
L5 = {'b', 'ba', 'bcaa', 'cba'} 
L2 = {"acc", "b", "bb", "bcaa"}
L6 = {'aca', 'bb', 'c', 'caba'}
L7 = {'ca', 'b'}

# Cartesian product helper
def cartesian_power(L, n):
    return {"".join(p) for p in product(L, repeat=n)}

# Star operation helper (Kleene star)
def star(L, max_len=5):
    result = {""}
    for i in range(1, max_len + 1):  # Limiting the star to avoid infinite loops
        result |= cartesian_power(L, i)
    return result

# Concatenation of two languages
def concatenate(L1, L2):
    return {w1 + w2 for w1 in L1 for w2 in L2}

# Union of two languages
def union(L1, L2):
    return L1 | L2

# Set difference helper
def difference(L1, L2):
    return L1 - L2

# Main computation for L9^* - (L1 U L3)^*
def compute_L9_minus_union_star():
    L_union = union(L5, L6)  # L1 U L3
    L_union_star = star(L_union)  # (L1 U L3)*
    L9_star = star(L7)  # L9*
    result = difference(L9_star, L_union_star)  # L9^* - (L1 U L3)*
    return result

# Enumerate the first 10 strings of length > 5, ordered by length and lexicographically
def enumerate_proper_order(L):
    filtered = [w for w in L if len(w) > 5]
    sorted_filtered = sorted(filtered, key=lambda x: (len(x), x))  # Sort by length and then lexicographically
    return sorted_filtered[:10]

# Execute the operation
result = compute_L9_minus_union_star()
output = enumerate_proper_order(result)

# Output the results
for i, string in enumerate(output, 1):
    print(f"{string}")