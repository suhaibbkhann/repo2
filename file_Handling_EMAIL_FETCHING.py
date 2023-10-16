f_read = open("assignment_1.txt", "r")

data = f_read.readlines()

f_emails = open("emails.txt", "a")
f_numbers = open("numbers.txt", "a")


for email in data:
    row = email.split(" ")
    for word in row:
        if "@" in word:
            f_emails.write(word + "\n")
        else:
            if len(word) == 10 and word.isnumeric():
                f_numbers.write(word + "\n")
f_read.close()
print(f_read.closed)
