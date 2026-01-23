# To do list:
# What will it do:
#   > let's user add or remove task
#   > let's user view that task
#   > let's them mark it as done
#   > stores task in a file
#   > let's them prioritize task
#   > let's them give deadlines
#   > Recommends user tasks randomly and let's them add it
#   > let's them see previously done task (deleted task)
# Needs:
#   > Function
#   > Loops
#   > File handling
#   > Lists & Strings


add_task = []
completed_task = []

while True:
    task = input("What task do you want to add? (q to quit): ")
    if task.lower() == "q":
        break
    else:
        add_task.append(task)
print("-----------------------------------------------------")
print(f"Task: {add_task}")
print("-----------------------------------------------------")

while True:
    is_rem = input("do you want to remove task? (yes/no) : ").lower()
    if is_rem == "yes":
        remove = input("which task do want to remove? : ")
        add_task.remove(remove)
        print(f"Task: {add_task}")

    elif is_rem == "no":
        print(f"Task: {add_task}")
        break
    else:
        print("Invalid Option")

while True:
    is_done = input("do you want to mark any task as done? (yes/no) : ").lower()
    if is_done == "yes":
        mark = input("which task do you want to mark as done? : ")
        completed_task.append(mark)
        add_task.remove(mark)
        print(f"Task: {add_task}")


    elif is_done == "no":
        print(f"Task remening: {add_task}")
        break
    else:
        print("Invalid Option")
