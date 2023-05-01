import random as r
from uzwords import words
from pywebio.output import put_text, popup
from pywebio.input import input

def get_word():
    word = r.choice(words)
    while '-' in word or ' ' in word:
        word = r.choice(words)
    return word.upper()

def display(user_letters, word):
    display_letters = ""
    for letter in word:
        if letter in user_letters:
            display_letters += letter
        else:
            display_letters += '-'
    return display_letters

def play():
    #pywebio.output.clear(scope=- 1)
    word = get_word()
    word_letters = set(word)
    user_letters = ""
    put_text(f"Men {len(word)} ta harfli so'z o'yladim. Topa olasizmi???\n"
    f"Eslatma: Krill alifbosidagi harflardan foydalaning!!!")
    while len(word_letters) > 0:
        pywebio.output.clear(scope=- 1)
        put_text(display(user_letters, word))
        if len(user_letters) > 0:
            put_text(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters} . ")
        letter = input("Harf kiriting>>>").upper()
        if letter in user_letters:
            put_text("Bu harfni avval kiritgansiz!!!")
            continue
        elif letter in word:
            word_letters.remove(letter)
            put_text(f"{letter} harf to'g'ri.")
        else:
            put_text("Bunday harf mavjud emas!!!")
        user_letters += letter
    popup(f"Tabriklayman! {word} so'zini {len(user_letters)} ta urinishda topdingiz.")