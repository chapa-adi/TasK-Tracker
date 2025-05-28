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

### Our first task that allows user to add their task 

def add_task(description):
    previous_task=check_file()
    id= 1 if previous_task==[] else previous_task[-1]["Id"]+1
    time=dt.datetime.now().isoformat()
    value= { "Id":id,
            "Description":description,
            "Current_time":time,
            "Updated_time":time
            }
    previous_task.append(value)
    print("Task added sucessfully!!!")
    save_file(previous_task)




def main():
    command_Line=sys.argv[1:]   ### as the sys.arg[0] is the file name "base.py"
    if not command_Line:
        print("Usage: base.py command 'argument'")
        sys.exit(1)
    command=command_Line[0].upper()    # index for the command 

    if command=="ADD":
        if len(command_Line)<3:
            print("Usage: base.py commad 'Description'")
        else:
            #Calling a add task function that creates new id and adds other info
            add_task(''.join(command_Line[1:]))  ## first index= second value  and all other remaining description here


        

main()