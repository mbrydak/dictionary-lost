
# Dictionary generator using initial words and substitution characters. Creates a dictionary of all possible words and all possible combination of words, preserving initial order of words.
# Most useful with passwords created following xkcd password-creation tips: https://xkcd.com/936/
# by: @wbrydak
# date: 2022-01-11
# version: 1.0
# license: MIT

import itertools

init_data = input("Please enter initial data: ")
complete_wordlist = []

# create dictionary with multiple values per key
substitutions_dict = {
    "o": ["o", "0"],
    "b": ["b"],
    "c": ["c"],
    "d": ["d"],
    "e": ["e", "3"],
    " ": ["-", "_", ""],
    "i": ["i", "1"],
    "l": ["l", "1"],
    "a": ["a", "4", "@"],
}

# characters to be tried to be appended to the end of init_data #TODO: implement this
append_list = ["!"]
# characters to be tried to be prepended to the end of init_data #TODO: implement this
prepend_list = ["#", "!", "#!"]

# separate the init_data into a list of words
init_data_word_list = init_data.split()

list_of_lists = []

# for each word in the init_data_word_list create new single-element list
for word in init_data_word_list:
    list_of_lists.append([word])

# for each word in the init_data_word_list create new list of words with first letter capitalized
for i in range(0, len(init_data_word_list)):
    list_of_lists[i].append(list_of_lists[i][0].capitalize())

for i in range(0, len(init_data_word_list)):
    # perfonrm all viable character substitutions from the substitutions_dict on each word in the init_data_word_list[i]
    # append only unique values to the list_of_lists[i]
    for char in substitutions_dict:
        for sub in substitutions_dict[char]:
            if list_of_lists[i][0].replace(char, sub) not in list_of_lists[i]:
                list_of_lists[i].append(list_of_lists[i][0].replace(char, sub))


# cartesian product all sublists in the list_of_lists
cartesian_product = list(itertools.product(*list_of_lists))

# turn each tuple in cartesian_product into a string and append to complete_wordlist
for tuple in cartesian_product:
    complete_wordlist.append(" ".join(tuple))

# replace all spaces in complete_wordlist with a hyphen and append to complete_wordlist_no_spaces
complete_wordlist_no_spaces_hyphen = []
for word in complete_wordlist:
    complete_wordlist_no_spaces_hyphen.append(word.replace(" ", "-"))

# replace all spaces in complete_wordlist with an underscore and append to complete_wordlist_no_spaces
complete_wordlist_no_spaces_underscore = []
for word in complete_wordlist:
    complete_wordlist_no_spaces_underscore.append(word.replace(" ", "_"))

# delete all spaces from complete_wordlist and append to complete_wordlist_no_spaces
complete_wordlist_no_spaces = []
for word in complete_wordlist:
    complete_wordlist_no_spaces.append(word.replace(" ", ""))

# combine complete_wordlist_no_spaces_hyphen and complete_wordlist_no_spaces and append to complete_wordlist_final
complete_wordlist_final = []
for word in complete_wordlist_no_spaces_hyphen:
    complete_wordlist_final.append(word)
for word in complete_wordlist_no_spaces_underscore:
    complete_wordlist_final.append(word)
for word in complete_wordlist_no_spaces:
    complete_wordlist_final.append(word)

# update wordlist.txt with complete_wordlist_final and print to console each word in complete_wordlist_final
with open("wordlist.txt", "w") as f:
    for word in complete_wordlist_final:
        f.write(word + "\n")
        print(word)
