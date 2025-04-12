from itertools import chain

def check_format(file_format, valid_extensions, formats):
    """
        Checks and prints the MIME type a file based on its extension.

        Args:
            file_format (list): [filename, extension]
            valid_extensions (list): Allowed file extensions
            formats (dict): MIME types grouped by category (e.g., "image", "application")
        """
    # Check if the file has a valid extension (e.g., ['file', 'pdf'])
    if len(file_format) == 2 and file_format[1] in valid_extensions:
        # Search for the extension in the formats dictionary
        for keys, values in formats.items():
            if file_format[1] in values:
                # Adjust for known format variations
                if file_format[1] == "jpg":
                    file_format[1] = "jpeg"
                if file_format[1] == "txt":
                    print("text/plain")
                print(f"{keys}/{file_format[1]}",end="")

def main():
    #supported MIME types
    formats = {"application": ["pdf", "zip","octet-stream"],
               "image": ["jpg", "gif", "jpeg","png"],
               }

    user_file_format = input("File name:").lower().strip().rsplit('.', 1)
    # Handle edge cases: .bin files or missing extensions
    if "bin" in user_file_format or "" in user_file_format:
        user_file_format.pop.append("octet-stream")
    print(user_file_format)

    # Flatten all valid extensions for quick lookup
    valid_extensions = list(chain(*formats.values()))
    # Check and print the MIME type
    check_format(user_file_format, valid_extensions, formats)


if __name__ == "__main__":
    main()

