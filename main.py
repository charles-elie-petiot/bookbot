def main(book):
    with open(f"books/{book}") as f:
        file_content = f.read()
    print(f"--- Begin report of books/{book} ---")
    print(f"{get_num_words(file_content)} words found in the document\n")
    dic = get_num_character(file_content)
    liste = []
    for key in dic:
        liste.append({'character' : key, 'number' : dic[key]})
    
    liste.sort(reverse=True, key=sort_on)

    for dico in liste:
        if dico['character'].isalpha():
            print(f"The '{dico['character']}' character was found {dico['number']} times")

    print("--- End report ---")

def get_num_words(text):
    return len(text.split())

def get_num_character(text):
    dic = {}
    for letter in text.lower():
        if letter in dic.keys():
            dic[letter] += 1
        else :
            dic[letter] = 1
    return dic

def sort_on(dic):
    return dic['number']

main('frankenstein.txt')