import string

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

        words = file_contents.split()
        
        print('--- Begin report of books/frankenstein.txt ---')

        print(str(len(words)) + " words found in the document")
        sortAndOutputCharacters(file_contents)
        print('--- End report ---')

def countChars(my_string: str):
    string_lower = my_string.lower()
    output = {}

    for letter in string.ascii_lowercase:
        output[letter] = string_lower.count(letter)
    return output


def sortAndOutputCharacters(my_string:str):
    string_dictionary = countChars(my_string)
    
    string_list = dictToString(string_dictionary)

    string_list.sort(reverse=True, key=sort_on)
    for dictionary in string_list:
        if dictionary['letter'].isalpha():
            print("The '" + dictionary['letter'] + "' character was found " + str(dictionary['count']) + " times")

def dictToString(string_dictionary: dict):
    string_list = []
    for k, v in string_dictionary.items():
        string_list.append({'letter': k, 'count': v})
    return string_list

def sort_on(dict):
    return dict["count"]


main()

