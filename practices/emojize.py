def main():
    import emoji

    sample = str(input())

    print(emoji.emojize(sample, language="alias"), end="")

if __name__ == "__main__":
    main()
