def freq_to_words(words):
    word_freq_dict = {}
    
    # Count the frequency of each word
    for word in words:
        word_freq_dict[word] = word_freq_dict.get(word, 0) + 1

    # Create a dictionary with the frequency as key and a list of words as value
    freq_to_words_dict = {}
    for word, freq in word_freq_dict.items():
        if freq not in freq_to_words_dict:
            freq_to_words_dict[freq] = []
        freq_to_words_dict[freq].append(word)

    return freq_to_words_dict