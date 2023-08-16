def count_vowels(word):
    vowels = "АЕУЫИОЁЯЮЭаеуыиоёяюэ"
    return sum(1 for letter in word if letter in vowels)

def check_rhythm(pooh_poem):
    phrases = pooh_poem.split()
    phrase_vowel_counts = list(map(count_vowels, phrases))
    
    if all(count == phrase_vowel_counts[0] for count in phrase_vowel_counts):
        return "Парам пам-пам"
    else:
        return "Пам парам"

poem = input("Введите стихотворение Винни-Пуха: ")

result = check_rhythm(poem)
print(result)
