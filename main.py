from faker import Faker
from random import shuffle, seed
from faker.providers.person.en import Provider
import random

fake = Faker()
letters = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i',
    'o', 'p', 'a', 's', 'd', 'f', 'g', 'h',
    'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b',
    'n', 'm'
]
numbers = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
]

def create_word(number):
    word = ""
    for _ in range(int(number)):
        word += random.choice(letters)
    
    return word

def create_words(number):
    words = []
    for _ in range(int(number)):
        words.append(create_word(random.randint(5, 15)))

    return words

def create_sentence(number):
    sentence = ""
    for _ in range(int(number)):
        sentence += create_word(random.randint(5, 15))
        sentence += ' '

    return sentence

def create_sentences(number):
    sentences = []
    for _ in range(int(number)):
        sentences.append(create_sentence(random.randint(5, 10)))

    return sentences

# You can create up to 6824 names
def create_first_names(number):
    first_names = list(set(Provider.first_names))
    seed(4321)
    shuffle(first_names)
    return first_names[0:int(number)]

def create_full_names(number):
    full_names = []
    for _ in range(int(number)):
        full_names.append(fake.name())

    return full_names

def create_countries(number):
    countries = []
    for i in range(int(number)):
        countries.append(fake.country())

    return countries

def create_texts(number):
    texts = []
    for _ in range(int(number)):
        texts.append(fake.text())

    print(texts)
    return texts

def create_emails(number):
    emails = []
    for _ in range(int(number)):
        emails.append(fake.email())

    return emails

def create_urls(number):
    urls = []
    for _ in range(int(number)):
        urls.append(fake.url())

    return urls

def main():
    number = input("How many sentences: ")
    create_sentences(number)


if __name__ == "__main__":
    main()