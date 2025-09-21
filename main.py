"""
Text Shuffle Tool
----------------
Программа для перемешивания букв в словах выделенного текста.
"""

import keyboard
import pyperclip
from random import shuffle
import time

# Глобальные настройки
is_program_active = False       # Флаг активности программы

def shuffle_word(word: str) -> str:
    """Перемешивает буквы в слове."""
    inner_letters = list(word)
    shuffle(inner_letters)
    return ''.join(inner_letters)

def shuffle_text() -> None:
    """Обрабатывает выделенный текст, перемешивая буквы в каждом слове."""
    keyboard.send('space')
    
    if not is_program_active:
        return
        
    # Копируем выделенный текст
    keyboard.send('ctrl+a')
    keyboard.send('ctrl+c')
    time.sleep(0.01)
    
    # Обработка текста
    user_input = pyperclip.paste()
    words = user_input.split(' ')
    shuffled_words = [shuffle_word(word) for word in words]
    shuffled_text = ' '.join(shuffled_words)
    
    # Вставляем результат
    pyperclip.copy(shuffled_text.capitalize())
    keyboard.send('ctrl+v')

def toggle_active_state() -> None:
    """Переключает состояние активности программы."""
    global is_program_active
    is_program_active = not is_program_active
    status = "активирована" if is_program_active else "деактивирована"
    print(f"Программа {status}")

def main():
    """Основная функция программы."""
    # Настройка горячих клавиш
    keyboard.add_hotkey('space', shuffle_text)
    keyboard.add_hotkey('\\', toggle_active_state, suppress=True)
    # keyboard.add_hotkey('\\', toggle_active_state, suppress=True)
    
    # Информация о запуске
    print("=" * 50)
    print("Программа перемешивания текста запущена")
    print("-" * 50)
    print("Инструкция:")
    print("1. Нажмите \\ для активации/деактивации")
    print("2. Выделите текст и нажмите пробел для перемешивания")
    print("3. Для выхода нажмите Ctrl+C")
    print("=" * 50)
    
    # Основной цикл программы
    try:
        keyboard.wait()
    except KeyboardInterrupt:
        print("\nПрограмма завершена")

if __name__ == "__main__":
    main()