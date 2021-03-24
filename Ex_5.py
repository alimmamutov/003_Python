import random


def get_jokes(n, allowRepeat = False):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(n):
        if i == 5 and allowRepeat:
            return None
        random.shuffle(nouns)
        random.shuffle(adverbs)
        random.shuffle(adjectives)
        jokeList = list(zip(nouns, adverbs, adjectives))
        print(jokeList[len(jokeList)-1])

        if allowRepeat:
            nouns.pop()
            adverbs.pop()
            adjectives.pop()

#1 вариант
get_jokes(10, False)
print('____________________________________________')
#2 Вариант
get_jokes(10, True)