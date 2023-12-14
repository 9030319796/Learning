def arrayStringAreEqual(word1: list[str], word2:list[str]):
    combines_string_word1 = ''.join(word1)
    combined_string_word2 = ''.join(word2)
    if combines_string_word1 == combined_string_word2:
        return True
    else:
        return False



word1 = ["ab","c"]
word2 = ["ab","c"]
result = arrayStringAreEqual(word1,word2)

print(result)