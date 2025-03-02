formats = {"application": ["pdf", "text", "zip"],
           "image": ["jpg", "gif", "jpeg"]}

user_filename_list = input("File name:").rsplit('.', 1)

valid_extensions = []

for values in formats.values():
    valid_extensions.extend(values)

if len(user_filename_list) == 2 and user_filename_list[1] in valid_extensions:
    print(user_filename_list[1])
    key = list(formats.keys())[list(formats.values()).index(user_filename_list[1])]
    print(key)