file = input("File name: ").strip().split('.')
extension = file[-1].lower()

if extension in ['jpg','jpeg']:
    print("image/jpeg")
elif extension in ['png','gif']:
    print("image/"+extension)
elif extension in ['pdf','zip']:
    print("application/"+extension)
elif extension == 'txt':
    print("text/plain")
else:
    print("application/octet-stream")
