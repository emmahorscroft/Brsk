import random
import re

def main():
    # create hashmap of txt file words and corresponding length
    txt_hash = {}
    with open('corncob_lowercase.txt', 'r') as file:
        for line in file:
            word = line.strip()
            first_word = word[0]
            word_length = len(word)

            if first_word in txt_hash:
                txt_hash[first_word].append((word, word_length))
            else:
                txt_hash[first_word] = [(word, word_length)]

    #loop until user chooses to exit
    while True:
        # user inputs a sentence
        sentence = input("Please enter your sentence for alternative words: ").lower()
        user_input = re.split('\s+',sentence.strip())

        # create hashmap for the user input of the letter and corresponding length
        sentence_map = {}
        for word in user_input:
            first_word = word[0]
            word_length = len(word)

            if first_word in sentence_map:
                sentence_map[first_word].append((word, word_length))
            else:
                sentence_map[first_word] = [(word, word_length)]

        # find alternative words
        def find_alt(word, sentence_map):
            first_word = word[0]
            word_length = len(word)
            if first_word in sentence_map:
                alt = [alt_word for alt_word, alt_length in sentence_map[first_word] if word_length == alt_length and alt_word != word]
                if alt:
                    return random.choice(alt)
            return word

        output_words = [find_alt(word, txt_hash) for word in user_input]
        output_sentence = ' '.join(output_words)

        # output 
        print('The new updated sentence is: ', output_sentence)
        print()

        # additional logic to loop in order to try again with a new sentence
        try_again = input("Do you want to try again?: Y/yes or anything else to exit! ").lower().strip()
        if try_again not in ('yes' ,'y'):
            print("Good luck scrabbling - goodbye!")
            break

if __name__ == "__main__":
    main()
