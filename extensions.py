# Implement a program that prompts the user for the name of a file and then outputs the file's media type
text = input("File name: " ).strip().lower()
if text.endswith(".gif"):
    print("image/gif")
elif text.endswith((".jpg", ".jpeg")):
    print("image/jpeg")
elif text.endswith(".png"):
    print("image/png")
elif text.endswith(".pdf"):
    print("application/pdf")
elif text.endswith(".txt"):
    print("text/plain")
elif text.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")