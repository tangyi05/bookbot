def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    characters = {}
    for c in text:
        char = c.lower()
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def char_count_sorted(text):
    ch = char_count(text)
    sorted_characters = sorted(ch.items(), key=lambda item: item[1], reverse=True)
    return sorted_characters