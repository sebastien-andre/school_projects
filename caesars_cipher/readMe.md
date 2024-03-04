# Caesar's Cipher Encoder and Decoder

This Python project implements the Caesar's Cipher, an ancient encryption technique, for encoding and decoding messages. It shifts each letter in the plaintext by a random number within the alphabet to produce the ciphertext. The program then employs statistical analysis to crack the encoded message.

## Features

- **Encoding:** Transforms plaintext messages into encoded ciphertext using a randomly chosen shift factor, ensuring that each encoding is unique.
- **Decoding:** Attempts to decode the ciphertext without prior knowledge of the shift factor, utilizing the frequency distribution of letters in the English language.
- **Statistical Analysis:** Employs the chi-square statistic to compare the frequency distribution of letters in the encoded message against expected frequencies in normal English text, identifying the most likely shift factor used for encoding.
- **Accuracy Improvement with Longer Texts:** The decoding accuracy improves with the length of the input text, as longer texts provide a more representative sample of English letter frequencies.

## Implementation Details

The script includes several key functions:

- `encode(n, s)`: Encodes the plaintext `s` with a shift factor `n`. This function iterates through each letter in the input string `s`, checks if it is a lowercase letter, and applies the shift `n`. The shifted letter is then added to the resulting string, which is returned as the encoded message.

- `frequencies(s)`: Calculates the frequency distribution of lowercase letters in the string `s`. This function counts the occurrence of each lowercase letter in the input string and calculates its frequency as a percentage of the total number of lowercase letters. The frequencies are stored in a list, with each element representing the frequency of the corresponding letter in the alphabet.

- `chisqr(os, es)`: Computes the chi-square statistic for the observed frequencies `os` against the expected frequencies `es`. This statistical measure is used to determine how well the observed frequencies of letters in the encoded message match the expected frequencies of letters in standard English text. The closer the chi-square statistic is to zero, the better the match.

- `crack(s)`: Decodes the ciphertext `s` by finding the shift factor that minimizes the chi-square statistic. It calculates the chi-square statistic for each possible shift factor (0 to 25) by comparing the frequency distribution of the shifted text against the expected frequency distribution. The shift factor that results in the lowest chi-square statistic is considered the most likely shift used to encode the message, and the function then decodes the message using this shift factor.
