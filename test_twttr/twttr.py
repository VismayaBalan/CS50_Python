def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    output = ""
    for j in word:
        if j.lower() not in ['a', 'e', 'i', 'o', 'u']:
            output += j
    return output



if __name__ == "__main__":
    main()