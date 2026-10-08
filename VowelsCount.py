user_str = input("Enter a Sentence: ")
vowel_string = "AEIOUaeiou"

vowel_count = sum(user_str.count(vowel) for vowel in vowel_string)

print("Counts of vowels:", vowel_count)
