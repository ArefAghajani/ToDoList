#user make a to do list and app save that list in a json file in the same dirctory. the method of the writing this program will be the oop.
import json

class Todo:
    def __init__(self, name, time, tag, done):
        self.name = name
        self.time = time
        self.tag = tag
        self.done = done
    def get_info(self):
        return { 'time' :self.time, 'tag': self.tag, 'done': self.done }
class User:
    names = set()
    def __init__(self, name):
        self.name = name
        self.todolist = {}
        self.load()
    def set_todo(self, name, time, tag='', done = False):
        todo = Todo(name, time, tag, done)
        self.todolist[todo.name] = todo.get_info()
        self.save()
    def remove_todo(self , todo_name):
            if self.todolist.pop(todo_name,False):
                self.save()
                return 'successful'
            else:
                return 'there is not matching item'
    def get_todo(self):
        return self.todolist
    def save(self):
        with open(f'{self.name}.json', 'w') as file:
            json.dump(self.todolist,file)
    def load(self):
        try:
            with open(f'{self.name}.json', 'r') as file:
                self.todolist=json.load(file)
        except FileNotFoundError:
            self.save()
    def done(self,todo_name):
        if todo_name in self.todolist: 
            self.todolist[todo_name] = True
            return 'successful'
        else:
            return 'there is not any matching item'
print('ToDoList -- written by aref aghajani')
while True:
    txt = input("print name or type exit >>>")
    if txt == 'exit':
        break
    p = User(txt)
    while True:
        print(f'logged in as {p.name}')
        txt = input('get, set, remove, done, back >>>')
        if txt == 'back':
            break
        elif txt == 'get':
            print(p.get_todo())
        elif txt == 'set':
            txt = input('name time tag done>>>>').split()
            p.set_todo(txt[0],txt[1],txt[2] if len(txt)>2 else '', txt[3] if len(txt)>3 else False )
        elif txt == 'remove':
            txt = input('todo_name >>>')
            print(p.remove_todo(txt))
        elif txt =='done':
            print(p.done(input('todo_name >>>')))