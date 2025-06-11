
def caesar_cypher_encrypt(s: str, key: int) -> str:
    a = "abcdefghilmnopqrstuvwxyz"
    encrypted = []
    for char in s:
        if char in a:
            original_index = a.index(char)
            new_index = (original_index + key) % len(a)
            encrypted.append(a[new_index])
        else:
            encrypted.append(char) 
    return ''.join(encrypted)    


print(caesar_cypher_encrypt("gaming",3))

def caesar_cypher_decrypt(s: str, key: int) -> str:
    a = "abcdefghilmnopqrstuvwxyz"
    decrypted = []
    for char in s:
        if char in a:
            original_index = a.index(char)
            new_index = (original_index - key) % len(a)
            decrypted.append(a[new_index])
        else:
            decrypted.append(char) 
    return ''.join(decrypted)

print(caesar_cypher_decrypt("ldpnql",3))