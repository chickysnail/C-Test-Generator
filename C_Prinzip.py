# %%
import re, string
import nltk
nltk.download('punkt')  # Download the necessary tokenizer data (if not already downloaded)
from nltk.tokenize import sent_tokenize

# %%
def divide_into_sentences(german_text):
    sentences = sent_tokenize(german_text, language='german')
    return sentences

# Example usage
german_text = "Das ist ein Beispieltext! Er zeigt, wie man Sätze in Python teilen kann."
sentences = divide_into_sentences(german_text)
print(sentences)


# %%
def extract_words(sentence):
    words = sentence.split()
    return words

# Example usage
input_sentence = "Hello, this is an example sentence with some punctuation!"
word_array = extract_words(input_sentence)
print(word_array)


# %%
def delete_second_half(word):
    punctuation = ''
    if word[-1] in '.,;!?':
        punctuation = word[-1]
        word = word[:-1]

    length = len(word)
    half_length = length // 2
    first_half = word[:half_length]
    return first_half + "_" + punctuation

# Example usage
input_word = "example?"
result = delete_second_half(input_word)
print(result)


# %%
def apply_function_to_second_long_words(word_array, some_function):
    new_word_array = []

    for i, word in enumerate(word_array):
        if i % 2 == 1 and len(word) > 1:
            new_word_array.append(some_function(word))
        else:
            new_word_array.append(word)

    return new_word_array


# Example usage
input_words = ['Hello', 'this', 'is', 'an', 'example', 'sentence', 'with', 'some', 'punctuation']
new_words = apply_function_to_second_long_words(input_words, delete_second_half)
print(new_words)

# %%
def apply_c_principle(german_text):
    sentences = divide_into_sentences(german_text)
    result = []

    for i, sentence in enumerate(sentences):
        if i == 0 or i == len(sentences) - 1:
            result.append(sentence)
        else:
            words = extract_words(sentence)
            new_words = apply_function_to_second_long_words(words, delete_second_half)
            new_sentence = ' '.join(new_words)
            result.append(new_sentence)

    return ' '.join(result)

text = "Die Biodiversität, also die Vielfalt des Lebens auf der Erde, ist von entscheidender Bedeutung für die Umwelt. Sie sichert Ökosysteme, reguliert Klima und Nährstoffkreisläufe, sowie die Bestäubung von Pflanzen. Doch bedrohliche Umweltfaktoren wie Klimawandel und Habitatverlust gefährden diese Vielfalt. Der Schutz der Biodiversität ist daher essenziell, um Ökosysteme widerstandsfähig zu halten. Durch nachhaltige Landnutzung, Schutzgebiete und internationale Zusammenarbeit können wir dem Rückgang der Artenvielfalt entgegenwirken. Indem wir unsere Konsumgewohnheiten überdenken und natürliche Ressourcen schonen, tragen wir zur Bewahrung der Umwelt und der Biodiversität bei, um zukünftigen Generationen eine intakte Erde zu übergeben."
result_text = apply_c_principle(text)
print(result_text)



