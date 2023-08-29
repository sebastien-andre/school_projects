import random
from string import ascii_lowercase


def table_from_corpus():
    return [8.1, 1.5, 2.8, 4.2, 12.7, 2.2, 2.0, 6.1, 7.0,
            0.2, 0.8, 4.0, 2.4, 6.7, 7.5, 1.9, 0.1, 6.0,
            6.3, 9.0, 2.8, 1.0, 2.4, 0.2, 2.0, 0.1]


def encode(n, s):
    # this function takes as input n, the shift factor and
    # plain text s and returns the encoded string.
    list = ''
    for letter in s:
        if letter not in ascii_lowercase:
            list += letter
        else:
            list += chr(((ord(letter) - ord('a') + n) % 26) + ord('a'))
    return (list)


def count(c, s): # part of frequencies function
    ## This functions takes as input a character c and a string s and returns the
    ## the number of times c appears in s
    counter = 0
    for letter in s:
        if letter == c:
            counter += 1
    return counter



def num_lower_case(s): # part of frequencies function
    ## This function takes as input a string s and returns the
    ## number of lower-case letters in s
    counter = 0
    for letter in s:
        if letter in ascii_lowercase:
            counter += 1
    return counter



def frequencies(s):
    ## This function takes as input a string s and returns the
    ## frequency list for s, containing 26 percentages, one for
    ## each lower-case letter. The percentage should be taken
    ## over the number of lower-case letters in s.
    xs = []
    total_letters = num_lower_case(s)
    for letter in ascii_lowercase:
        count1 = count(letter, s)
        percentage = 100* count1/total_letters
        xs.append (percentage)
    return xs


def chisqr(os, es):
    ## returns the chi-square statistic for os and es
    chi_statistic = 0
    counter = 0
    for items in os:
        estimated_list_position = es[counter]
        chi_statistic += ((items - estimated_list_position) ** 2)/estimated_list_position
        counter += 1
    return chi_statistic



def rotate(n, xs):
    ## rotates list xs by n positions
    # might have to create a new list variable xs
    xs = xs[-n:] + xs[:-n]
    return xs



def chisquare_statistic(xs, es):
    ## This computes 26 ch-square statistics in a list, one for each
    ## list obtained by rotating os by n = 0 to 25.
    frequency_list = []
    for x in range(0,26):
        frequency_list.append(chisqr(rotate(x,xs),es))
    return frequency_list


def crack(s):
    # This function takes as input a coded text and returns the plain text
    # for the coded text
    frequency_list = chisquare_statistic(frequencies(s),table_from_corpus())
    match = min(frequency_list)
    shift_factor = frequency_list.index(match)

    return encode(shift_factor, s)



def main():
    while True:
        plain = input("\nEnter plain text: ")
        if plain == "exit":
            break
        shift = random.randint(2, 25)
        cipher = encode(shift, plain)
        print("Coded text: ", cipher)
        recovered = crack(cipher)
        print("Cracked text: ", recovered)


main()