import sys
from notebook import Note, Notebook


class Menu:
    '''Отображает меню и реагирует на выбор пользователя при запуске.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            '1' : self.show_notes,
            '2' : self.search_notes,
            '3' : self.add_note,
            '4' : self.modify_note,
            '5' : self.quit
        }
        
    def display_menu(self):
        print("""Меню записной книжки 1. Показать все заметки 2. Найти заметки 
              3. Добавить заменку 4. Изменить заметку 5. Выход""")
        
    def run(self):
        '''Отображает меню и реагирует на выбор пользователя.'''
        while True:
            self.display_menu()
            choice = input('Выберите вариант: ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f'{choice} - неверный выбор')
    
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f'{note.id}: {note.tags}\n{note.memo}')
            
    def search_notes(self):
        filter = input('Поиск: ')
        notes = self.notebook.search(filter)
        self.show_notes(notes)
        
    def add_note(self):
        memo = input('Введите заметку: ')
        self.notebook.new_note(memo)
        print('Заметка была успешно добавлена')
        
    def modify_note(self):
        id = input('Введите идентификатор заметки: ')
        memo = input('Ведите заметку: ')
        tags = input('Введите метки: ')
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)
            
    def quit(self):
        print('Спасибо за использование вашей записной книжки сегодня.')
        sys.exit(0)
        
if __name__ == '__main__':
    Menu().run()