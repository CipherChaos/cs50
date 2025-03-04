from email.policy import default
from itertools import chain

def check_format(file_format, valid_extensions, formats):
    if len(file_format) == 2 and file_format[1] in valid_extensions:
        for keys, values in formats.items():
            if file_format[1] in values:
                if file_format[1] == "jpg":
                    file_format[1] = "jpeg"
                if file_format[1] == "txt":
                    print("text/plain")
                print(f"{keys}/{file_format[1]}",end="")

def main():
    formats = {"application": ["pdf", "zip","octet-stream"],
               "image": ["jpg", "gif", "jpeg","png"],
               }

    user_file_format = input("File name:").lower().strip().rsplit('.', 1)
    if "bin" in user_file_format or "" in user_file_format:
        user_file_format.pop.append("octet-stream")
    print(user_file_format)
    valid_extensions = list(chain(*formats.values()))
    check_format(user_file_format, valid_extensions, formats)


if __name__ == "__main__":
    main()

