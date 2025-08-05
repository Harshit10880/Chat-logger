def save_message (user, message, file_name = "chat.txt"):
    "save formated message to your file"
    with open(file_name, "a") as file:
        file.write(f"[{user}]: {message}\n")

def display_message(user, message):
    'display message in format style.'
    print(f"[{user}]: {message}")

def chat():
    print("=== Simple chat logger ===")
    print("Type 'stop' to end chatting.\n")

    while True:
        user_1 = input("User_1: ")
        if user_1.lower() == 'stop':
            break
        save_message("User_1", user_1)
        # display_message("User_1", user_1)

        user_2 = input("User_2: ")
        if user_2.lower() == 'stop':
            break
        save_message("User_2", user_2)
        # display_message("User_2", user_1)

    print("\nChat saved to 'chat.txt.")

chat()