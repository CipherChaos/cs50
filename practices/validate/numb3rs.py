import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    addresses = ip.split(".")
    if re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        for address in addresses:
            if int(address) < 0 or int(address) > 255:
                return False
        else:
            return True
    else:
        return False






if __name__ == "__main__":
    main()
