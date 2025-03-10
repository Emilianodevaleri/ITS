#8-10

messages:list = ["ciao", "come stai?", "sei un cesso", "lazio merda"]
sent_messages:list = []

def send_messages():
    for i in messages:
        print(i)
        sent_messages.append(i)
    messages.clear()

send_messages()

print(messages)
print(sent_messages)


