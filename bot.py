from enum import Enum

WORD_LENGTH = 5

class Mask(Enum):
    CORRECT = "C"
    MISPLACED = "M"
    INCORRECT = "I"

    def create_mask_list(letters):
        return [elem.name for elem in [Mask.CORRECT if obj == "C" else (Mask.MISPLACED if obj == "M" else Mask.INCORRECT) for obj in list(letters)]]

def create_word_mask(guess_word, correct_word):
    word_mask = [Mask.INCORRECT] * 5

    correct_letters = []
    for idx in reversed(range(WORD_LENGTH)):
        if guess_word[idx] == correct_word[idx]:
            correct_letters.append(guess_word[idx])
            word_mask[idx] = Mask.CORRECT
            guess_word.pop(idx)
            correct_word.pop(idx)

    for idx in range(len(guess_word)):
        if word_mask[idx] == Mask.INCORRECT and guess_word[idx] in correct_word and guess_word[idx] in correct_letters:
            word_mask[idx] = Mask.MISPLACED

    return [elem.name for elem in word_mask]

if __name__ == '__main__':
    print(create_word_mask(list("abcde"), list("azzaz")))