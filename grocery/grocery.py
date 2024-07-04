#

def main():
    grocery_list = {}

    #
    print("")
    try:
        while True:
            item = input().strip().upper()
            if not item:
                break
            grocery_list[item] = grocery_list.get(item, 0) + 1
    except EOFError:
        pass

    #
    sorted_items = sorted(grocery_list.items(), key=lambda x: x[0])

    # 
    for item, count in sorted_items:
        print(f"{count} {item}")

if __name__ == "__main__":
    main()
