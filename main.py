import random
import os


def get_user_input():
    """Отримує базу слів, транскрипцій та перекладів від користувача"""
    words_base = []  # Зберігаємо всі слова у списку
    print('Введіть базу слів (слово:транскрипція:переклад), порожній рядок для завершення:')

    while True:
        user_input = input().strip()
        if not user_input:  # Порожній рядок завершує введення
            break

        if ':' in user_input:
            parts = user_input.split(':', 2)
            if len(parts) == 3:
                word, transcription, translation = parts
                words_base.append({
                    'word': word.strip(),
                    'translation': translation.strip(),
                    'transcription': transcription.strip()
                })
            else:
                print('Неправильний формат! Використовуйте формат "слово:транскрипція:переклад".')
        else:
            print('Неправильний формат! Використовуйте формат "слово:транскрипція:переклад".')

    os.system('cls' if os.name == 'nt' else 'clear')
    return words_base

def print_separator():
    """Виводить візуальну перегородку"""
    print('\n' + '=' * 50 + '\n')

def train_word_to_translation(words_base, count_training):
    """Тренування: слово -> переклад"""
    all_words = words_base.copy()  # Створюємо копію списку слів

    while all_words:
        random_word = random.choice(all_words)  # Вибираємо випадкове слово
        word = random_word['word']
        translation = random_word['translation']
        transcription = random_word['transcription']

        answer = input(f'СЛОВО: "{word}" [{transcription}]: ').strip()

        if answer in [i.strip() for i in translation.split(',')]:
            print('ВІРНО!')
            all_words.remove(random_word)  # Видаляємо пару після правильної відповіді
            print_separator()  # Додаємо візуальну перегородку між словами
        else:
            print(f'НЕВІРНО! "{word}" -> "{translation}"')
            print_separator()  # Додаємо візуальну перегородку між словами

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Вітаємо! Ви успішно завершили тренування. Лічильник: {count_training}')

def train_translation_to_word(words_base, count_training):
    """Тренування: переклад -> слово"""
    all_words = words_base.copy()  # Створюємо копію списку слів

    while all_words:
        random_word = random.choice(all_words)  # Вибираємо випадкове слово
        word = random_word['word']
        translation = random_word['translation']

        answer = input(f'ПЕРЕКЛАД: "{translation}": ').strip()

        if answer == word:
            print('ВІРНО!')
            all_words.remove(random_word)  # Видаляємо пару після правильної відповіді
            print_separator()  # Додаємо візуальну перегородку між словами
        else:
            print(f'НЕВІРНО! "{translation}" -> "{word}"')
            print_separator()  # Додаємо візуальну перегородку між словами

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Вітаємо! Ви успішно завершили тренування. Лічильник: {count_training}')


def start_training():
    """Запускає тренування та вибір режиму"""
    words_base = get_user_input()  # Отримуємо базу слів від користувача
    count_training = 0
    if not words_base:
        print('Словник порожній! Завершення програми.')
        return
    preview_choice = ''
    while True:
        print('\nМеню:')
        print('1. Тренування слово -> переклад')
        print('2. Тренування переклад -> слово')
        print('3. Вихід')

        choice = input('Оберіть режим (1, 2 або 3): ').strip()
        print_separator()
        if choice == '1':
            if preview_choice != '1':
                count_training = 1
                preview_choice = '1'
            else:
                count_training += 1
            train_word_to_translation(words_base, count_training)
        elif choice == '2':
            if preview_choice != '2':
                count_training = 1
                preview_choice = '2'
            else:
                count_training += 1
            train_translation_to_word(words_base, count_training)
        elif choice == '3':
            print('Вихід з програми.')
            break
        else:
            print('Невірний вибір, спробуйте ще раз.')

if __name__ == '__main__':
    # Стартуємо програму
    print('Вітаємо у тренуванні слів!')
    start_training()
