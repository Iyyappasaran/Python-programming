# Converting smiling and frowning emoticons to emojis
def convert(x):
    x = x.replace(":)","🙂")
    x = x.replace(":(","🙁")
    return x

def main():
    text = input()
    print(convert(text))

main()
