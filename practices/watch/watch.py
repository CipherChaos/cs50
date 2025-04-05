import re

def main():
    print(parse(input("HTML: ")))


def parse(s):

    pattern = r'.+"http(s)?:\/\/(?:www.)?youtube\.com\/embed\/(.+?)"'
    match = re.search(pattern, s)
    if "iframe" in s:
        if match:
            return "https://youtu.be/" + match.group(2)
        else:
            return None
    else:
        return None


if __name__ == "__main__":
    main()
