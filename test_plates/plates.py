def main():
    s = input("Plate: ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if plate[0:2].isalpha() and 2 <= len(plate) <= 6:
         if plate[2:7].isalpha():
             return True
         else:
            for i in range(len(plate)):
               if plate[i] not in ['.',' ','!','?']:
                  if plate[i].isdigit():
                     if plate[i+1:].isdigit():
                        if plate[i] != '0':
                           return True
                        else:
                           break
               else:
                  break
    return False

if __name__ == "__main__":
    main()
