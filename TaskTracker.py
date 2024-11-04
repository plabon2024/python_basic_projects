import json
import os

file_name="ToDo.json"

def content():
    if os.path.exists(file_name):
        with open(file_name, 'r+') as file:
            try:
                return json.load(file)
            except Exception:
                return []
    else:
        return []


def save_content(content):
    with open(file_name,'w')as file:
        json.dump(content,file,indent=4)


def add():
    tasks=content()
    add_todo=input("Enter Your Task :").strip().title()
    if not add_todo:
        print("Task Can't Be Empty ")
        return

    if tasks==[]:
        task_id=0
    else:
        task_id = int(max(task['id'] for task in tasks))

    new_todo={
        'id':task_id+1,
        'ToDo':add_todo,
        'status':False
    }
    tasks.append(new_todo)
    save_content(tasks)
    print(" Task added !")


def delete():
    tasks = content()
    task_id = int(input("Enter Task Number You Want To Delete: "))
    found = False
    for task in tasks:
        if task_id == task['id']:
            tasks.remove(task)
            new_id = 1
            for task in tasks:
                task['id'] = new_id
                new_id += 1
            save_content(tasks)
            print('Task deleted !')
            found = True
            break
    if not found:
        print("Task not found!")

def mark_done():
    tasks=content()
    task_done=int(input('Enter Done Task Number :'))
    found=False
    for task in tasks:
        if task_done==task['id']:
            task['status']=True
            save_content(tasks)
            found=True
            print("Congratulation !")
    if not found:
            print("Task not found !")

def list_all():
    dict_list = content()
    if dict_list:
        print("All ToDo : ")
        for task in dict_list:
            if task['status']==True:
                status="Done"
            else:
                status="To Do!"
            print(f'{task['id']} {task['ToDo']} - {status}')
    else:
        print("No task found ! ")


def list_all_done():
    tasks=content()
    status=False
    for task in tasks:
        if task['status']==True:
            print(f'{task['id']} {task['ToDo']}')
            status=True
    if not status:
        print('No Task Done !')

def list_all_notdone():
    tasks = content()
    status=False
    for task in tasks:
        if task['status']==False:
            print(f'{task['id']} {task['ToDo']}')
            status=True
    if not status:
        print('All Task Done !')

def reset():
    restore=[]
    save_content(restore)

while True:
    print("""/n-> SELECT OPTION <-
              1.Add Task.
              2.Delete Task.  
              3.List All Task.
              4.List All Task Done.
              5.List All Task Not Done. 
              6.Mark As Dome.
              0.Clear All Task.""")
    try:
        option = int(input("Enter Your Option : "))
        if option == 1:
            add()
        elif option == 2:
            delete()
        elif option == 3:
            list_all()
        elif option == 4:
            list_all_done()
        elif option==5:
            list_all_notdone()
        elif option == 6:
            mark_done()
        elif option==0:
            reset()

        else:
            print("SELECT 1/2/3/4/5/6/0 !")
    except Exception as e:
        print("Unexpected ! TRY AGAIN !!")
