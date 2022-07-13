import src.game_elements as game

def find_best_word(usable_words, unused_letters):
    # The list here is reversed because you want the more rare words to be used and the more common words to be ignored
    percentile = {
	'E' : 0.1666443494095728,
	'S' : 0.16910785672082543,
	'I' : 0.28433642450522245,
	'A' : 0.4813375414276502,
	'R' : 0.7642435423327905,
	'N' : 0.9207954585640057,
	'O' : 0.9323183153424455,
	'T' : 1.191026317012862,
	'L' : 1.623570520082154,
	'C' : 1.8587957343178887,
	'D' : 2.4972414678212305,
	'U' : 2.806212965438979,
	'P' : 2.900342785122164,
	'M' : 3.003929294161448,
	'G' : 3.313576269590347,
	'H' : 3.356806849503941,
	'B' : 4.0163115971196035,
	'Y' : 5.233522612811748,
	'F' : 6.510930621674017,
	'K' : 6.63923167180361,
	'V' : 6.69895185710704,
	'W' : 6.97065287314487,
	'Z' : 7.7383930065000825,
	'X' : 9.026568926351858,
	'Q' : 9.631638109186618,
	'J' : 11.263513032947026
    }

    # can someone thats reviewing this verify that this way to find the best word actually works?
    pre_ranking = {}
    for word in usable_words:
        used_letters = []
        word_percentile_rank = 100
        pre_ranking[word] = {}

        for letter in unused_letters:
            if letter in word and letter not in used_letters:
                used_letters.append(letter)
                word_percentile_rank -= percentile[letter]

        pre_ranking[word]["used_letters"] = used_letters
        pre_ranking[word]["word_percentile_rank"] = word_percentile_rank

    lowest_percentile = 100
    best_word = ''
    for word, word_items in pre_ranking.items():
        if word_items["word_percentile_rank"] < lowest_percentile:
            lowest_percentile = int(word_percentile_rank)
            best_word = word

    print(f"{best_word} was the best word with being at the bottom {lowest_percentile}%")

    return best_word

def find_usable_words(driver, wordlist):
    usable_words = []
    syllable = game.get_syllable(driver)
    for i in wordlist:
        if syllable in i:
            usable_words.append(i)

    return usable_words