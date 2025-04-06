import re

def main():
    print(parse(input("HTML: ")))


def parse(s):

    pattern = r'iframe.+"http(s)?:\/\/(?:www.)?youtube\.com\/embed\/(.+?)"'
    match = re.search(pattern, s)

    if match:
        return "https://youtu.be/" + match.group(2)
    else:
        return None


if __name__ == "__main__":
    main()
