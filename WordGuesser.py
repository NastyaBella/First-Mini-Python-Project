#❤️ Happy Pythoning! 🐍




from random import choice

def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]

def play(word):
    word = word.lower()
    guessed_letters = []
    word_display = ['_'] * len(word)
    tries = 6
    
    print(display_hangman(tries))
    print(' '.join(word_display))

    while tries > 0:
        letter = input("Введите букву: ").lower()
        
        if len(letter) != 1 or not letter.isalpha():
            print("Пожалуйста, введите ровно одну букву!")
            continue
            
        if letter in guessed_letters:
            print("Вы уже вводили эту букву!")
            continue
        
        guessed_letters.append(letter)
        
        if letter in word:
            for i, char in enumerate(word):
                if char == letter:
                    word_display[i] = letter
            print("Молодец! Загаданное слово содержит эту букву.")
        else:
            tries -= 1
            print("Ой. Загаданное слово не содержит эту букву :(")
        
        # Проверка победы
        if '_' not in word_display:
            print("Поздравляем! Вы угадали слово!")
            break
        
        print(' '.join(word_display))
        print(display_hangman(tries))

    if tries == 0:
        print(f"Вы проиграли! Загаданное слово было: {word}")

def get_word():
    words = [
        "apple", "book", "cat", "dog", "egg",
        "fish", "glass", "house", "island", "jungle",
        "kite", "lemon", "moon", "notebook", "ocean", 
        "pencil", "queen", "river", "sun", "tree"
    ]
    return choice(words)

while True:
    play(get_word())
    s = input("Вы бы хотели играть ещё раз? (yes): ").lower()
    if s != "yes":
        print("До скорых встреч!")
        break
