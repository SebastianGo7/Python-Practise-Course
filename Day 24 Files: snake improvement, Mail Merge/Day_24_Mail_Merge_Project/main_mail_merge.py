
with open("/Users/Sebastian/PycharmProjects/Day_24_Mail_Merge_Project/Input/Names/invited_names.txt", "r") as giv_list:
    names_read_list = giv_list.readlines()


adapted_names_list = []
txt_name_list = []

for i in names_read_list:
    name_only = i.replace("\n", "")
    adapted_names_list.append(name_only)

    actual_txt_name = "letter_for_" + name_only + ".txt"
    txt_name_list.append(actual_txt_name)


for i in range(0, len(adapted_names_list)):
    with open("Input/Letters/starting_letter.txt", "r") as file:
        content = file.read()

    content = content.replace("[name]", adapted_names_list[i])

    with open(f"Output/ReadyToSend/{txt_name_list[i]}", "w") as file:
        file.write(content)
