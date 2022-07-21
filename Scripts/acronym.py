Input = input(">")
words = Input.split()
acronym = ""
for word in words:
    acronym += word[0]


print(acronym)