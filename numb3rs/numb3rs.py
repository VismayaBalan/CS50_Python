import re

def main():
    ip = input("IPv4 Address: ").strip()
    print(validate(ip))


def validate(ip):
    matches = re.search(r"^(?:[01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])(?:\.[01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]){3}$", ip)
    if matches:
        return True
    else:
        return False



if __name__ == "__main__":
    main()