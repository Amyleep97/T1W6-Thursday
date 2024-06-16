## Control Flow
Order in which lines of code are excecuted in a program.

# Sequential control flow
Execution of code statements one after another, in the order they apear in the program.

# Conditional control flow / Control flow
Execution of code statements based on some input

if tomorrow is Saturday
   set alarm for 7
if tomorrow is Tuesday
    set alarm for 6

# Boolean Data Type Re-visit
Data type that has two values: True and False. Boolean values are used to control the flow of the program.

# Comparison Operators / Relational Operators
Decide the relationship between the operands. Result of comparison is boolean value (True/False)

if tomorrow == Saturday
   set alarm for 7
if tomorrow == Tuesday
    set alarm for 6

# if, elif, else
Simplest form of AI (you could say that)
'if' checks the condition, if true, the inteded blocks get executed, if false, it skips the intended blocks.

today = "Tuesday"

if today == "Monday":
    print("Set an alarm for 5 AM!")
elif today == "Tuesday":
    print("Set an alarm for 6AM!")
elif today == "Saturday":
    print("Set an alarm for 7AM!")

temperature = 40

if temperature > 35:
    print("It's hot outside.")
if temperature < 15:
    print("It's cold outside.")
else:
    print("The weather is mild.")

# pass
Does nothing, just...pases..for now.

# Boolean Operators
AND, OR, NOT. Operands needs to be boolean as well

age = 20
has_permission = False

if age >= 18:
    if has_permission:
        print("Acess granted.")
    else:
        print("Acess denied")
else: 
    print("Acess denied.")

if age >=18 and has_permission:
    print("Acess granted.")
else: 
    print("Acess denied")

# Termary Operator
Condense series of code to one line, where applicable

print("Access granted.") if age >=18 and has_permission else print("Access denied.")

temperature = 30
if temperature > 30:
    message = "It's hot outside"
 else:
     message = "It's not hot outside"

print(message)

message = "it's hot outside" if temperature > 30 else "It's not hot outside"

# Match-case
Control flow, similar to switch statement in other programming lanaguages day_number = 3

day_number = 3

match day_number:
    case 1:
        day_name = "Monday"
    case 2:
        day_name = "Tuesday"  
    case 3:
        day_name = "Wednesday"
    case 4:
        day_name = "Thursday"

print(day_name)

# Activity
write a python script that asks the user to input a numerical score and categorizes it into grades (A, B ,C ,D ,F) based on the following criteria:

     90-100: A
     80-89: B
     70-79: C
     60-69: D
     0-59: F

