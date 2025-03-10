#8-4

def make_shirt(size:int,message:str):
    print(f"this shirt is a size {size} and it display this message: {message}")

size_L:str = "L"
text_default:str = "in need of some boobies"

make_shirt(size_L, text_default)

size_M:str = "M"

make_shirt(size_M, text_default)

size:str = input("insert your size ")
message:str = input("insert the message you want ")

make_shirt(size, message)