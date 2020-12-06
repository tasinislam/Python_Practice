def statement_splitter(statement):
    letter_list = [char for char in statement]
    current_string = ""
    n = 0
    for letter in letter_list:
        if n < (len(statement) - 1) and letter_list[n] != " " and letter_list[n+1] != " ":
            add_string = letter + "-"
        elif letter_list[n] != " ":
            add_string = letter
        elif letter_list[n] == " ":
            add_string = " "
        n += 1
        current_string += add_string
    print(current_string)


statement_splitter("Hello World")
