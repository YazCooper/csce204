#author yaz c

FILE_NAME = "assignments/ass-22/jobs.txt"


def read_assignments():
    assignments = {}
    with open (FILE_NAME) as file:
        for line in file:
            line = line.replace("\n","") .strip()
            h = line.split(",")
            j = h[0]
            s= h[1]
            assignments[j] = s
            
            
            
           

            
    return assignments


def write_assignments(assignments):
    with open (FILE_NAME, "w") as file:
        for assignment in assignments:
            file.write(assignment +  "\n")
            




def list_assignments(assignments):
    for assignment in assignments:
        print(f"{assignment} : {assignments[assignment]}")

def add_assignment(assignments):
    assignment = input("Job: ").strip()
    student = input("Student: ").strip()


    if assignment in assignments:
        for assignment in assignments:
            assignments[assignment] = student
            write_assignments(assignments)
            print(f"{student} was added.")
            return assignments
    else:
        print("Sorry No")

    
    
    # print(f"{assignment} was added.")

    

assignments = read_assignments() 

while True:
    command = input("(V)iew,(A)dd, or (Q)uit?: ").strip().lower()

    if command=="q":
        break
    elif command == "v":
        list_assignments(assignments)
    elif command == "a":
        adds = add_assignment(assignments)
    else:
        print("Invalid Command")

write_assignments(assignments)
