def find_anagrams(word, candidates):
    candidates_to_test = candidates.copy() #to prevent mutation in the original words
    for i, w in enumerate(candidates_to_test): #standardize the candidates in lowercase
        w = w.lower()
        candidates_to_test[i] = w

    word = word.lower() #standardize the word in lowercase

    anagrams = [] #where the eligible anagrams will be stored as deliverable results

    for i, candidate in enumerate(candidates_to_test):
        if len(candidate) == len(word): #only check words that are equal in length to the anagram
            candidate_letters = list(set(candidate)) #obtain list of unrepeated letters in the candidate
            counter = 0 #to keep track of how many letter-counts match between anagram and the word given
            for letter in candidate_letters:
                if candidate.count(letter) != word.count(letter):
                    continue
                else:
                    counter += 1
            if counter == len(candidate_letters) and candidate != word: #test if all letters match and the word is different
                anagrams.append(candidates[i])
    
    return anagrams
