import sys
import json
import datetime as dt
file_name="task.json"


# checking the JSON file  and loading any previous data if there are any else returning empty list to be appended
def check_file():
    try:
        with open (file_name,"r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
### saves the new list that is appended in the programs by adding dictionary with unique ID
def save_file(changed_list):
    with open(file_name,"w+") as f:
        json.dump(changed_list,f,indent=4)


## necessary global 
previous_task=check_file()


### Our first task that allows user to add their task 

def add_task(description):
    
    id= 1 if previous_task==[] else previous_task[-1]["Id"]+1
    time=dt.datetime.now().isoformat()
    value= { "Id":id,
            "Description":description,
            "Status":"to-do",
            "Current_time":time,
            "Updated_time":time
            }
    previous_task.append(value)
    print("Task added sucessfully!!!")
    save_file(previous_task)

# Updating tasks
def update_task(id,description):
    found=False
    update_time=dt.datetime.now().isoformat()
    for all_task in previous_task:
        if all_task["Id"]==id:
            all_task["Description"]=description
            all_task["Updated_time"]=update_time
            found=True
            break
    if found==False:
        raise ValueError(f"NO value associated with ID {id} ")
    save_file(previous_task)
    print("Updated sucessfully")

#deleting tasks     
def delete(id):
    found=False
    for i,v in enumerate(previous_task):
        if v["Id"]==id:
            previous_task.pop(i)
            found=True
            break
    if found==False:
        raise ValueError(f"NO value associated with ID {id} ")
    save_file(previous_task)
    print("Deleted sucessfully")



#listing tasks
def listing(*args):
    type_of_listing =''.join(args)
    if type_of_listing:
        match type_of_listing.upper():
            case "TO-DO":
                for task in previous_task:
                    if task["Status"]=="to-do":
                        print(task)
            case "DONE":
                for task in previous_task:
                    if task["Status"]=="done":
                        print(task)
            case "IN-PROGRESS":
                for task in previous_task:
                    if task["Status"]=="in-progress":
                        print(task)
            case _:
                raise ValueError(f"NO such status found {type_of_listing} ")
    else:
            for task in previous_task:
                    print(task)




def mark_in_progress(id):
    found=False
    update_time=dt.datetime.now().isoformat()
    for all_task in previous_task:
        if all_task["Id"]==id:
            all_task["Status"]="in-progress"
            all_task["Updated_time"]=update_time
            found=True
            break
    if found==False:
        raise ValueError(f"NO value associated with ID {id} ")
    save_file(previous_task)
    print("Marked-in-progess sucessfully")


def mark_done(id):
    found=False
    update_time=dt.datetime.now().isoformat()
    for all_task in previous_task:
        if all_task["Id"]==id:
            all_task["Status"]="done"
            all_task["Updated_time"]=update_time
            found=True
            break
    if found==False:
        raise ValueError(f"NO value associated with ID {id} ")
    save_file(previous_task)
    print("Marked-done sucessfully")
    pass

def main():
    command_Line=sys.argv[1:]   ### as the sys.arg[0] is the file name "base.py"
    if not command_Line:
        print("Usage: base.py command 'argument'")
        sys.exit(1)
    command=command_Line[0].upper()    # index for the command 
    length=len(command_Line)
    if command=="ADD":
        if length<2:
            print("Usage: base.py add 'Description'")
        else:
            #Calling a add task function that creates new id and adds other info
            add_task(''.join(command_Line[1:]))  ## first index= second value  and all other remaining description here

    elif command=="UPDATE":
        if length<3:
            print("Usage: base.py update ID 'Description'" )
        else:
            update_task(int(command_Line[1]),"".join(command_Line[2:]))
    elif command=="DELETE":
        if length<2:
            print("Usuage: base.py delete ID")
        else:
            delete(int(command_Line[1]))
    elif command=="LIST":
        if not (length==1 or length==2):
                print("Usage: base.py list [(optional) to-do/ in-progress/ done] ")
        elif length==1:
            listing()
        elif length==2:
            listing(command_Line[1])
    elif command=="MARK-IN-PROGRESS":
        if length!=2:
            print("Usage: base.py mark-in-progress ID" )
        else:
            mark_in_progress(int(command_Line[1]))
    elif command=="MARK-DONE":
        if length!=2:
            print("Usage: base.py mark-done ID" )
        else:
            mark_done(int(command_Line[1]))

        pass
main()