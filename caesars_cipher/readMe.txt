# Caesar's Cipher Encoder and Decoder

This Python project implements the Caesar's Cipher, an ancient encryption technique, for encoding and decoding messages. It shifts each letter in the plaintext by a random number within the alphabet to produce the ciphertext. The program then employs statistical analysis to crack the encoded message.

## Features

- **Encoding:** Transforms plaintext messages into encoded ciphertext using a randomly chosen shift factor, ensuring that each encoding is unique.
- **Decoding:** Attempts to decode the ciphertext without prior knowledge of the shift factor, utilizing the frequency distribution of letters in the English language.
- **Statistical Analysis:** Employs the chi-square statistic to compare the frequency distribution of letters in the encoded message against expected frequencies in normal English text, identifying the most likely shift factor used for encoding.
- **Accuracy Improvement with Longer Texts:** The decoding accuracy improves with the length of the input text, as longer texts provide a more representative sample of English letter frequencies.

## Usage

