#
main = input("File name: ").strip()

#
main_lower = main.lower()

if main_lower.endswith(".gif"):
    print("image/gif")
elif main_lower.endswith(".jpg"):
    print("image/jpeg")
elif main_lower.endswith(".jpeg"):
    print("image/jpeg")
elif main_lower.endswith(".png"):
    print("image/png")
elif main_lower.endswith(".pdf"):
    print("application/pdf")
elif main_lower.endswith(".txt"):
    print("text/plain")
elif main_lower.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
