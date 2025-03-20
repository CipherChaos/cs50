import inflect

def main():
    p = inflect.engine()
    names = []
    try:
        while True:
            name = str(input("")).strip()
            if name:
                names.append(name)
    except EOFError:
        if names:
            result = p.join(names)
            print(f"Adieu, adieu, to {result}")

if __name__ == "__main__":
    main()
