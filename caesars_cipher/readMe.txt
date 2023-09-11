Encodes plain lowercase text into cipher text using the Caesar's Cipher method. It will shift each letter in the alphabet over by a random number. The program then attempts to decode this coded message. It uses the frequency distrubution of the individual letters in normal English text usage. The program determines the frequencies of a-z in the coded text and stores it in a table. Then, the program compares the two frequency distrubution tables and determines the chi-square statistic. It will rotate the table by one shift factor and keep doing this until it has gone through all possible shift factors. The result with the lowest chi-square statistic will then be used as the shift factor to "crack" the message. 

The more words you give it, the more accurate it is. If you only provide a single word like hello, it may guess incorrectly.

Only works with lowercase letters.
