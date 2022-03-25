'''Task 3.6'''

import datetime

class Note():
    '''
    class Note
    '''
    def __init__(self, memo, tags):
        '''
        init function
        '''
        self.memo = memo
        self.creation_date = datetime.datetime.now()
        self.tags = tags

    def match(self, search_filter, code):
        '''
        Finds a match
        '''
        if code == 't':
            if search_filter in self.tags:
                return True
        elif code == 'm':
            if search_filter in self.memo:
                return True
        return False

class Notebook():
    '''
    class Notebook
    '''
    def __init__(self):
        self.all_notes = []

    def search(self, filter, code):
        '''
        Search function
        '''
        ret_list = []
        for note in self.all_notes:
            if note.match(filter, code):
                ret_list.append(note)
        return ret_list

    def new_note(self, memo, tags):
        '''
        Creates new note
        '''
        self.all_notes.append(Note(memo, list(set(tags))))

    def modify_memo(self, note_obj, memo):
        '''
        Modifies note's text
        '''
        for i in range(len(self.all_notes)):
            if self.all_notes[i] == note_obj:
                self.all_notes[i].memo = memo

    def modify_tags(self, note_obj, tags):
        '''
        Modifies note's tags
        '''
        for i in range(len(self.all_notes)):
            if self.all_notes[i] == note_obj:
                self.all_notes[i].tags = list(set(tags))


class Menu():
    '''
    class Menu
    '''
    notebook = Notebook()
    notebook.new_note("memo_1", ["tag1", "tag2"])
    notebook.new_note("memo_2", ["tag1", "tag2"])
    notebook.new_note("memo_3", ["tag1", "tag2"])

    def __init__(self):
        '''
        Init function
        '''
        self.user_list = []
        self.user_list_names = []

    def create_a_user(self):
        '''
        Creates a new user
        '''
        print('Please, enter the username')
        while True:
            username = input('>>> ')
            if username == '':
                print("Sorry, username can't be empty")
                continue
            if username in self.user_list_names:
                print("The user with this username already exists")
                print("Please, try again:")
                continue
            if username.isdigit():
                print('Sorry, username can\'t be a digit')
                print("Please, try again:")
                continue
            break
        notebook = Notebook()
        self.user_list_names.append(username)
        self.user_list.append((username, notebook))

    def delete_user(self):
        '''
        Deletes a user
        '''
        print("Enter the index of a user:")
        while True:
            index = input('>>> ')
            try:
                if index.isdigit() and int(index) > 0 and int(index) <= len(self.user_list):
                    self.user_list.pop(int(index) - 1)
                    break
                print('Sorry, the index wasn\'t entered correctly')
            except TypeError:
                print('Sorry, the index wasn\'t entered correctly')

    def select_user(self):
        '''
        Selects a user
        '''
        while True:
            try:
                index = int(input('>>> '))
            except ValueError:
                print("The index was entered incorrectly")
                continue
            if len(self.user_list) >= index and index > 0:
                return self.user_list[index - 1][1]
            print("Please, try again")

    def print_users(self):
        '''
        Prints all users
        '''
        print('----------')
        for i in range(len(self.user_list)):
            print(f'[{i + 1}]. User {self.user_list[i][0]}')
        print('----------')

class CommandOption():
    '''
    class CommandOption
    '''
    @staticmethod
    def print_menu_commands_none():
        '''
        Print menu commands while there are no users
        '''
        print('[1]. Create a new user')
        while True:
            choice = input('>>> ')
            if choice == '1':
                break
            print("Sorry, the index was entered incorrectly")

    @staticmethod
    def print_menu_commands():
        '''
        Prints menu commands
        '''
        print('[1]. Select a user')
        print('[2]. Delete a user')
        print('[3]. Create a new user')
        while True:
            choice = input('>>> ')
            if choice in ['1', '2', '3']:
                break
            print("Sorry, the index was entered incorrectly")
        return choice

    @staticmethod
    def print_notes(notes):
        '''
        Prints notes
        '''
        print('----------')
        i = 0
        if notes == []:
            print("No notes yet :(")
        for note in notes:
            tags = f'#{note.tags[0]}' if len(note.tags) > 0 else 'No tags to this note :('
            for j in range(1, len(note.tags)):
                tags += f', #{note.tags[j]}'
            print(f'[{i + 1}] Memo: {note.memo}; And all tags: {tags}')
            i += 1
        print('----------')

    @staticmethod
    def print_notes_commands():
        '''
        Notes commands print
        '''
        print('[1]. Search for a note')
        print('[2]. Create a new note')
        print('[3]. Modify memo of a note')
        print('[4]. Modify tags in a note')
        print('[5]. Select other user')
        while True:
            choice = input('>>> ')
            if choice in ['1', '2', '3', '4', '5']:
                break
            print("Sorry, the index was entered incorrectly")
        return choice

    @staticmethod
    def get_string(name):
        '''
        Input a string function
        '''
        print(f'Enter {name}')
        while True:
            text = input('>>> ')
            if text != '':
                break
            print('The text wasn\'t entered!')
        return text

def main():
    '''
    Main function
    '''
    menu = Menu()
    commandOption = CommandOption()
    user_notebook = None

    print("Welcome!")

    while True:

        if user_notebook == None:
            if len(menu.user_list) == 0:
                print("Select an action:")
                commandOption.print_menu_commands_none()
                menu.create_a_user()
            else:
                menu.print_users()
                print("Select an action:")
                choice = commandOption.print_menu_commands()
                if choice == '1':
                    print("Type in the index of a user")
                    user_notebook = menu.select_user()
                elif choice == '2':
                    menu.delete_user()
                elif choice == '3':
                    menu.create_a_user()
            continue

        commandOption.print_notes(user_notebook.all_notes)
        print("Select an action:")
        choice = commandOption.print_notes_commands()

        if choice == '1':
            print("Enter a search preference: memo/tags")
            while True:
                search_pref = input('>>> ')
                if search_pref == 'tags':
                    tag = commandOption.get_string('a tag:')
                    mass = user_notebook.search(tag, 't')
                    break
                elif search_pref == 'memo':
                    memo = commandOption.get_string('a part of text:')
                    mass = user_notebook.search(memo, 'm')
                    break
                print("The preference wasn't memo or tags")
            if mass == []:
                print("No matches were found")
                continue
            i = 0
            print("The result of a search is:")
            for mas in mass:
                tags = f'#{mas.tags[0]}' if len(mas.tags) > 0 else 'No tags to this note :('
                for j in range(1, len(mas.tags)):
                    tags += f', #{mas.tags[j]}'
                print(f'[{i + 1}] Memo: {mas.memo}; And all tags: {tags}')
                i += 1

        elif choice == '2':
            memo = commandOption.get_string('the memo of a new note:')
            tags = []

            print('Enter the tags of a note')
            print('Enter one tag and press enter')
            print('When you have entered all tags, enter "end": ')
            while True:
                tag = commandOption.get_string('a tag:')
                if tag == 'end':
                    break
                tags.append(tag)

            user_notebook.new_note(memo, tags)

        elif choice == '3':
            print(f'You are ready to select an index of a note you want \
to edit or do you want to make a search?')
            print('[1]. Select with an index right now')
            print('[2]. Do a search first')
            while True:
                index = input('>>> ')
                if index in ['1', '2']:
                    if index == "2":
                        print("Enter a search preference: memo/tags")
                        while True:
                            search_pref = input('>>> ')
                            if search_pref == 'tag':
                                tag = commandOption.get_string('a tag:')
                                mass = user_notebook.search(tag, 't')
                                break
                            elif search_pref == 'memo':
                                memo = commandOption.get_string('a part of text:')
                                mass = user_notebook.search(memo, 'm')
                                break
                            print("The preference was entered incorectly. Please try memo or tags")
                        if mass == []:
                            print("No matches were found")
                            print('You are ready to select an index of a note you want to edit or do you want to make a search?')
                            continue
                        i = 0
                        print("The result of a search is:")
                        for mas in mass:
                            tags = f'#{mas.tags[0]}' if len(mas.tags) > 0 else 'No tags to this note :('
                            for j in range(1, len(mas.tags)):
                                tags += f', #{mas.tags[j]}'
                            print(f'[{i + 1}] Memo: {mas.memo}; And all tags: {tags}')
                            i += 1
                    else:
                        mass = user_notebook.all_notes

                    print('Select the index:')
                    while True:
                        try:
                            index = int(input('>>> '))
                        except ValueError:
                            print("Incorrect type!")
                            continue
                        if index > 0 and index <= len(mass):
                            text = commandOption.get_string('new text:')
                            note_to_find = mass[index - 1]
                            user_notebook.modify_memo(note_to_find, text)
                            break
                        print('The choice was entered incorrectly')
                    break
                print('The choice was entered incorrectly')
        elif choice == '4':
            print(f'You are ready to select an index of a note you want \
to edit tags in or do you want to make a search?')
            print('[1]. Select with an index right now')
            print('[2]. Do a search first')
            while True:
                index = input('>>> ')
                if index in ['1', '2']:
                    if index == '2':
                        print("Enter a search preference: memo/tags")
                        while True:
                            search_pref = input('>>> ')
                            if search_pref == 'tags':
                                tag = commandOption.get_string('a tag:')
                                mass = user_notebook.search(tag, 't')
                                break
                            elif search_pref == 'memo':
                                memo = commandOption.get_string('a part of text:')
                                mass = user_notebook.search(memo, 'm')
                                break
                            print("The preference was entered incorectly. Please try memo or tags")
                        if mass == []:
                            print('You are ready to select an index of a note you want to edit or do you want to make a search?')
                            print("No matches were found")
                            continue
                        i = 0
                        print("The result of a search is:")
                        for mas in mass:
                            tags = f'#{mas.tags[0]}' if len(mas.tags) > 0 else 'No tags to this note :('
                            for j in range(1, len(mas.tags)):
                                tags += f', #{mas.tags[j]}'
                            print(f'[{i + 1}] Memo: {mas.memo}; And all tags: {tags}')
                            i += 1
                    else:
                        mass = user_notebook.all_notes

                    print('Select the index:')
                    while True:
                        try:
                            index = int(input('>>> '))
                        except ValueError:
                            print("Incorrect type!")
                            continue
                        if index > 0 and index <= len(mass):
                            tags = []
                            print('Enter the tags of a note')
                            print('Enter one tag and press enter')
                            print('When you have entered all tags, enter "end": ')
                            while True:
                                tag = commandOption.get_string('a tag:')
                                if tag == 'end':
                                    break
                                tags.append(tag)
                            note_to_find = mass[index - 1]
                            user_notebook.modify_tags(note_to_find, tags)
                            break
                        print('The choice was entered incorrectly')
                    break
                print('The choice was entered incorrectly')
        else:
            user_notebook = None

if __name__ == '__main__':
    main()