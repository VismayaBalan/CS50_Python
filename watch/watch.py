import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"https?://(?:www\.)?youtube.com/embed/([0-9A-Za-z]*)\"></iframe>",s):
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None



if __name__ == "__main__":
    main()


