file_location = 'P1_data.txt'

def count_word_occurences_from_txt(location: str) -> dict:
    hash_ = {}
    with open(location,'r') as file:
        content = file.read().lower().replace('\n',' ')
        words_list = content.split(' ')
    for i in words_list:
        if i not in hash_.keys():
            hash_[i] = 1
        else:
            hash_[i] += 1
    return hash_

count_word_occurences_from_txt(file_location)