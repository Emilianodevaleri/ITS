def caesar_cypher_encrypt(s: str, key: int) -> str:
    a = "abcdefghilmnopqrstuvwxyz"
    encrypted = []
    for char in s:
        if char in a:
            original_index = a.index(char)
            new_index = (original_index + key) % len(a)
            encrypted.append(a[new_index])
        else:
            encrypted.append(char)  # mantieni caratteri non presenti nell'alfabeto
    return ''.join(encrypted)

print(caesar_cypher_encrypt("csello", 3))