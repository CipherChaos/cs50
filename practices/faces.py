def replace_emoji(text):

    text = text.replace(":)", "🙂")

    text = text.replace(":(", "🙁")
    return text


sample = input("")

print(replace_emoji(sample))
