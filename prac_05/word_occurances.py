string = input("Please enter a string: ")

word_dict = {}
string_ls = string.split(" ")
max_word = 0
for word in string_ls:
    if word in word_dict.keys():
        word_dict[word] += 1
    else:
        word_dict[word] = 1

    if len(word) > max_word:
        max_word = len(word)


for word in word_dict:
    print(f"{word:{max_word}} : {word_dict[word]}")
