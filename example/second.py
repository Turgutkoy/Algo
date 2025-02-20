def stutter(word):
    first=word[:2]
    word=f"{first}... {first}... {word}"
    return word
a=input("Bir kelime giriniz:")
print(stutter(a))
