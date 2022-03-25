# Notebook program

The goal was to create a Notebook program, that would alow user to create notes and interact with the notebook. I created a program with a bit bigger functionality, I added the ability to create multiple users and notebooks.

# The program has three main classes and a ```main()``` function

## Class Note

The class note has three variables in it: memo(a text of a note), tags(a list of tags of a note) and the date of creation a note. To calculate the time when the note was created:
```python
import datetime
self.creation_date = datetime.datetime.now()
```

The class also has ```python match()``` function, that finds a match if there is one. I used flags to determane whether search by tags of memo

```python
def match(self, search_filter, code):
    if code == 't':
        if search_filter in self.tags:
            return True
    elif code == 'm':
        if search_filter in self.memo:
            return True
    return False
```

## Class Notebook()

The class that has as it's main variable a list of Note class objects. Also has a few funcitions. 

Two fuctions that modify memo of a note or a tag of a note, search function, that returns a list of match notes, and a function that makes a new note
```python
def new_note(self, memo, tags):
    self.all_notes.append(Note(memo, list(set(tags))))
```
I used a tricky thing to avoid repetition of one tag in a list of tags: made is a set and then list again.


## Class Menu()

As my program has an ability to have multiple users, class menu also has as its variable a list of users, that contains tuples of username, that can't repeat, and that user's notebook. 

Functions are: ```create_a_user(self)```,```delete_user(self)```, ```select_user(self)``` and ```print_users(self)```

## Class ComandOption

The class that doesn't have an __init__ fucntion, and is created to just store some functions:

```print_menu_commands_none()```, ```print_menu_commands()```, ```print_notes(notes)```,  ```print_notes_commands()```, ```get_string(name)```

```get_string(name)``` function is used to get strings from a user

# Conclusion and the main function

The whole program runs using a ```while True loop```, a lot of inputs and strings. 

In the end, I created a program that can be used as a Notebook
