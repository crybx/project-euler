# Problem 17 - Number letter counts
#
# If the numbers 1 to 5 are written out in words: one, two, three,
# four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written
# out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example,
# 342 (three hundred and forty-two) contains 23 letters and
# 115 (one hundred and fifteen) contains 20 letters. The use of
# "and" when writing out numbers is in compliance with British usage.


def num_to_word(num):
    num_words = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
                 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
                 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
                 17: "seventeen", 18: "eighteen", 19: "nineteen"}

    num_words_tens = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty",
                      7: "seventy", 8: "eighty", 9: "ninety"}

    word = ""

    while num > 0:
        if num < 20:
            word += num_words[num]
            num = 0

        if 20 <= num < 100:
            tens = int(str(num)[0])
            word += num_words_tens[tens]
            num = int(str(num)[1])

        if 100 <= num < 1000:
            hundreds = int(str(num)[0])
            word += num_words[hundreds] + "hundred"
            if num % 100 != 0:
                word += "and"
            num = int(str(num)[1:])

        if 1000 <= num < 10000:
            thousands = int(str(num)[0])
            word += num_words[thousands] + "thousand"
            num = int(str(num)[1:])

    return word


start = 1
end = 1000
letter_count = 0

for n in range(start, end + 1):
    letter_count += len(num_to_word(n))

print("Problem 17: " + str(letter_count) + " letters")

# Using "and" in number words feels so wrong. Like incorrectly writing a check.
