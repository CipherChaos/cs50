from itertools import chain

def check_format(file_format, valid_extensions, formats):
    if len(file_format) == 2 and file_format[1] in valid_extensions:
        for keys, values in formats.items():
            if file_format[1] in values:
                print(f"{keys}/{file_format[1]}")

def main():
    formats = {"application": ["pdf", "text", "zip"],
               "image": ["jpg", "gif", "jpeg"]}

    user_file_format = input("File name:").rsplit('.', 1)

    valid_extensions = list(chain(*formats.values()))
    check_format(user_file_format, valid_extensions, formats)

if __name__ == "__main__":
    main()

