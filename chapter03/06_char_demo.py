def process_characters():
    ch = input("Please insert a char: ")

    while ch != "#":
        print(ch, ":", ord(ch))
        ch = input("Please insert a char: ")

    print("Goodbye")

def process_characters2():
    ch = input("Please insert a char: ")

    while True:
        ch = input("Please insert a char: ")
        if ch == "#":
            break
        print(ch, ":", ord(ch))

    print("Goodbye")

def main():
    process_characters()
    process_characters2()

if __name__ == "__main__":
    main()