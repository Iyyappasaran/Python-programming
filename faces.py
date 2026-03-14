# Converting smiling and frowning emoticons to emojis
def convert(str):
    str = str.replace(":)","🙂")
    str = str.replace(":(","🙁")
    return str

def main():
    text = input("Enter text: ")
    print("Text after conversion:",convert(text))

main()