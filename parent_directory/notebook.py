import datetime

# Хранит следующий доступный идентификатор для всех новых заметок.
last_id = 0

class Note:
    '''Представляет заметку в зааписной книжке. Совпадает с 
    строкой при поиске и хранит метки для каждой заметки.'''
    def __init__(self, memo, tags=''):
        '''Иницианализирует заметку с помощью memo и опциональных разделенных пробелами меток. 
        Автоматически устанавливает дату создания заметки и уникальный идентификатор.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
        
    def match(self, filter):
        '''Определяет, соответствует ли эта заметка фильтру. Возврацает True, если совпадает,
        иначе False. Поиск чувствителен к регистру и соответствует как тексту, так и меткам.'''
        return filter in self.memo or filter in self.tags
    
    
class Notebook:
    '''Представляет колекцию заметок, которые могут быть помечены, изменены и найдены через поиск.'''
    def __init__(self):
        '''Иницианализируем записную книжку пустым списком.'''
        self.notes = []
        
    def new_note(self, memo, tags=''):
        '''Создает новую заметку и добавляет ее в список.'''
        self.notes.append(Note(memo, tags))
     
    def _find_note(self, note_id):
        '''Найти заметку с данным идентификатором.''' 
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
       
    def modify_memo(self, note_id, memo):
        '''Находит заметку с указанным идентификатором и меняет ее содержимое (memo) на указанное значение.'''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False
            
    def modify_tags(self, note_id, tags):
        '''Находит заметку с указанным идентификатором и меняет ее метки на указанное значение.'''
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break
            
    def search(self, filter):
        '''Находит все заметки, соответствующие указанному фильтру.'''
        return [note for note in self.notes if note.match(filter)]