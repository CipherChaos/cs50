def replace_emoji(text):
    text = text.replace(":)", "🙂")

    text = text.replace(":(", "🙁")
    return text


def main():
    sample = input("")

    print(replace_emoji(sample))


if __name__ == "__main__":
    main()
