#!/usr/bin/env python3
import hashlib

def part1():
    words = open('input.txt').read().strip().splitlines()
    NOT_ALLOWED = ('ab', 'cd', 'pq', 'xy')
    VOWELS = ('a', 'e', 'i', 'o', 'u')

    good_words = []

    invalid = False

    for word in words:
        vowel_count = 0
        twice_in_a_row = False

        invalid = False
        good_word = True

        for i, c in enumerate(word):
            if i != (len(word) - 1):
                current_pair = word[i:i + 2]

                if current_pair in NOT_ALLOWED:
                    invalid = True
                    break

                if current_pair == current_pair[::-1]:
                    twice_in_a_row = True

            if c in VOWELS:
                vowel_count += 1

        if invalid:
            continue

        good_word = twice_in_a_row and vowel_count >= 3

        if good_word:
            good_words.append(word)

    print('Part 1:', len(good_words))

def part2():
    print('Part 2:')

if __name__ == '__main__':
    part1()
    part2()
