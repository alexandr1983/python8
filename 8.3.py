class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


my_list = []
while True:
    user_input = input("Enter number or Enter stop: ")

    if user_input == "stop":
        break

    try:
        if not user_input.isdigit():
            raise NotNumberError("not format")

        my_list.append(int(user_input))
    except NotNumberError as e:
        print(e)

print(my_list)
