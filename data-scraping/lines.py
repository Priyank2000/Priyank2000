file_name = input("Enter file name:")
file = open(file_name, "r")

number_of_lines = 0
number_of_words = 0
number_of_characters = 0
for line in file:
    line = line.strip("\n")
    words = line.split()
    number_of_lines += 1
    number_of_words = len(words)
    number_of_characters += len(line)
    print("line no",number_of_lines, "words:", number_of_words)
    if len(words)>= 9 and len(words)<= 45:
        print(line)
        file_object = open('hindi_line.txt', 'a')
        file_object.write("\n")
        file_object.write(line)
        file_object.close()
file.close()

