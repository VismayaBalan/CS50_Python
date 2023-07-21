import sys
import csv

if len(sys.argv) == 3 and sys.argv[2].endswith('csv') == True and sys.argv[2].endswith('csv') == True:
    students = []
    try:
        with open(sys.argv[1]) as file1:
            reader = csv.DictReader(file1)
            with open(sys.argv[2], 'w') as file2:
                writer = csv.DictWriter(file2,fieldnames= ["first","last","house"])
                writer.writeheader()
                for row in reader:
                    row["first"] = row.pop("name")
                    last_name, first_name = row["first"].split(",")
                    row["first"] = first_name.strip()
                    row["last"] = last_name
                    writer.writerow(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Not a CSV file")



