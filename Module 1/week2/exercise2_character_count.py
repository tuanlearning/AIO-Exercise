def count_character_occurences(s: str) -> dict:
    hash_ = {}
    for i in s:
        if i not in hash_.keys():
            hash_[i] = 1
        else:
            hash_[i] += 1
    return hash_

count_character_occurences('happiness')