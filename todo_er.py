import os
from datetime import datetime
def print_taSks():
    os.system("clear && cat /home/Akash/productivity/art.txt")
    print()
    os.system("cat /home/Akash/productivity/tasks.txt")
    print("_" * 100)
print_taSks()
def get_tasks():
    tasks={};i=0
    while True:
        print("[+]",end=' ')
        task = input()
        if task.lower()=='end' or task.lower()=='break':
            break
        if task.lower()=='clear':
            with open("/home/Akash/productivity/tasks.txt",'w') as file:
                file.write('')
            print_taSks()
            continue
        else:
            tasks[i]=task
            i+=1
    return tasks
def write_tasks_to_file(tasks, filename):
    now = datetime.now()
    with open(filename, 'a') as file:
        file.write(f"\n Tasks [{now.strftime('%Y-%m-%d %H:%M:%S')}] :\n")
        for key, value in tasks.items():
            file.write(f"{key+1}) {value}\n")

tasks = get_tasks()
write_tasks_to_file(tasks, '/home/Akash/productivity/tasks.txt')
    

