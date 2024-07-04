answer = input("What the answer to the Great Question of Life, the Universe and Everything ")

answer_lower_stripped = answer.lower().strip()

match answer_lower_stripped:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")
