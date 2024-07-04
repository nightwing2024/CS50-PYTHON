string = input("Input: ")

print("Output: " , end="")

for vowels in string:
    if not vowels.lower() in ["a","e","i","o","u"]:
        print (vowels, end="")


print()
