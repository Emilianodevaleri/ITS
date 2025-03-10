#per esercizio 8-15

def show_messages():

    print("inserire i messaggi")

    messages:list=[input(""), input(""),input("")]

    for i in messages:
        print (i)
    
#8-16

def make_shirt(size:int,message:str):
    print(f"this shirt is a size {size} and it display this message: {message}")