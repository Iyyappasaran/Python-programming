# Get a str as input from user and convert it into the emojized form
import emoji

text = input("Input: ")
print(emoji.emojize(text, language = "alias"))