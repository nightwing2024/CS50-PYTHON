def convert(emoji):
    emoji = emoji.replace(":)", "🙂")
    emoji = emoji.replace(":(", "🙁")
    return emoji

def main ():
    text = input ("Write your message! ")
    result = convert(text)
    print (result)

main()
