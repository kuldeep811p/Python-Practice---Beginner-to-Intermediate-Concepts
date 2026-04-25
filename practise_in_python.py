""" ==========================================================
         PYTHON REVISION SHEET - BY KULDEEP PARMAR
 ============================================================
 > This file covers all basic Python topics with:
   - Definition of each topic (in comments)
   - Then the actual code that demonstrates the topic
   - It's designed for comprehensive revision sheet for beginners.
 ============================================================"""



""" ===========================================================
 TOPIC 1: PRINT & VARIABLES
 ------------------------------------------------------------
 DEFINITION:
   - print() is a built-in function used to display output on screen.
   - Variables are containers used to store data values.
 ============================================================"""

#personal information
print("Hii Kuldeep Parmar")
age = 20
study = "vit bhopal"
print("Kuldeep's age is:" , age , "and He study in" , study)


""" ============================================================
 TOPIC 2: INPUT FROM USER
 ------------------------------------------------------------
 DEFINITION:
   input() is a built-in function that takes input from the user
   as a string. Whatever the user types is stored in a variable.
 ============================================================"""

#input from user
enter = input("what is your purpose? ")
print(enter)

name = input("what is your name? ")
print("very nice to meet you", name)


""" ============================================================
 TOPIC 3: SUM OF TWO NUMBERS (Type Casting)
 ------------------------------------------------------------
 DEFINITION:
   input() always returns a string, so to do math we must
   convert it to a number using int() or float().
   This conversion is called TYPE CASTING.
 ============================================================"""

#sum of two numbers
firstnum = input("enter first number:")
secondnum = input("enter second number:")
sum = int(firstnum) + int(secondnum)
print("the sum of two number is:", sum)


""" ============================================================
 TOPIC 4: STRING METHODS
 ------------------------------------------------------------
 DEFINITION:
   Strings are sequences of characters enclosed in quotes.
   Python provides built-in methods to manipulate strings:
     .upper()        → converts all letters to UPPERCASE
     .lower()        → converts all letters to lowercase
     .title()        → capitalizes First Letter Of Each Word
     .replace(a, b)  → replaces part 'a' of string with 'b'
 ============================================================"""

#string concatenation
name = "kuldeep parmar"
print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("kuldeep", "kuldip"))


""" ==========================================================
 TOPIC 5: STRING FINDING
 ------------------------------------------------------------
 DEFINITION:
   .find(substring) searches for a substring inside a string
   and returns the INDEX (position) where it is first found.
   Index starts from 0. Returns -1 if not found.
 ============================================================"""

#string finding
name = "kuldeep parmar"
print(name.find("parmar"))
print(name.find('u'))


""" ============================================================
 TOPIC 6: MEMBERSHIP OPERATORS (in / not in)
 ------------------------------------------------------------
 DEFINITION:
   'in' checks if a value EXISTS inside a string, list, etc.
   It returns True or False (Boolean values).
     True  → value is found
     False → value is not found
 ============================================================"""

#true or false
name = "kuldeep parmar"
print("a" in name)
print("z" in name)
print("kuldeep" in name)
print("aakrti" in name)


""" ============================================================
 TOPIC 7: ARITHMETIC OPERATORS
 ------------------------------------------------------------
 DEFINITION:
   Arithmetic operators are used to perform math operations.
     +   → Addition
     -   → Subtraction
     *   → Multiplication
     /   → Division (gives float result)
     %   → Modulus (gives remainder)
     **  → Exponentiation (power)
     //  → Floor Division (removes decimal, rounds down)

   Comparison operators compare two values and return True/False:
     >   → Greater than
     <   → Less than
     ==  → Equal to
     !=  → Not equal to
     >=  → Greater than or equal to
     <=  → Less than or equal to
 ============================================================"""

#arithmetic operators
a = 10
b = 5
print(a + b) #addition
print(a - b) #subtraction
print(a * b) #multiplication
print(a / b) #division
print(a % b) #modulus
print(a ** b) #exponentiation
print(a // b) #floor division
print(a > b) #greater than
print(a < b) #less than
print(a == b) #equal to
print(a != b) #not equal to
print(a >= b) #greater than or equal to
print(a <= b) #less than or equal to


"""============================================================
 TOPIC 8: OPERATOR PRECEDENCE (BODMAS in Python)
 ------------------------------------------------------------
 DEFINITION:
   When multiple operators are in one expression, Python follows
   a specific ORDER to evaluate them (just like BODMAS in math):
     1. ()  → Parentheses (highest priority)
     2. **  → Exponentiation
     3. * / // %  → Multiplication, Division
     4. + -  → Addition, Subtraction (lowest priority)
 ============================================================"""

#operators precedence
result1 = 10 + 5 * 2
print(result1) #output will be 20 because multiplication has higher precedence than addition
result2 = (10 + 5) * 2
print(result2) #output will be 30 because parentheses have higher precedence than multiplication
result3 = 10 + 5 * 2 - 3
print(result3) #output will be 17 because multiplication has higher precedence than addition and subtraction
result4 = 10 + 5 * (2 - 3) ** 2
print(result4) #output will be 15 because parentheses are evaluated first, then exponentiation, then multiplication, and finally addition



"""" ============================================================
 TOPIC 9: LOGICAL OPERATORS
 ------------------------------------------------------------
 DEFINITION:
   Logical operators are used to combine multiple conditions:
     and → True only if BOTH conditions are True
     or  → True if AT LEAST ONE condition is True
     not → REVERSES the result (True→False, False→True)
 ============================================================"""

#logical operators
x = 10
y = 5
print(x > 5 and y < 10) #True because both conditions are true
print(x > 5 or y > 10) #True because at least one condition is
print(not(x > 5)) #False because x is greater than 5
print(not(y < 10)) #False because y is less than 10


""" ============================================================
 TOPIC 10: IF-ELSE STATEMENT
 ------------------------------------------------------------
 DEFINITION:
   if-else is used for DECISION MAKING in Python.
   If the condition is True → runs the 'if' block
   If the condition is False → runs the 'else' block
 ============================================================"""

#if else statement
age = 20
if age >= 18:
    print("you are an adult")
else:
    print("you are a minor")


"""============================================================
 TOPIC 11: IF-ELIF-ELSE STATEMENT
 ------------------------------------------------------------
 DEFINITION:
   When there are MORE THAN TWO conditions to check, we use
   elif (short for "else if") between if and else.
   Python checks each condition top to bottom and runs the
   FIRST block where the condition is True. 
   'else' runs if NO condition is True.
 ============================================================"""

#if elif else statement
age = int(input("enter your age:"))
if age >= 18 and age < 60:
    print("you are an adult")
elif age <= 13:
    print("you are a child")
else:
    print("you are a senior citizen")


""" ============================================================
 TOPIC 12: SIMPLE CALCULATOR (Applying if-elif-else)
 ------------------------------------------------------------
 DEFINITION:
   This is a practical use of if-elif-else where we check
   which operator the user entered and perform that operation.
   It combines input(), type casting, and conditionals together.
 ============================================================"""

#a simple calculator using if elif else statement
first = input("enter first number:")
operator = input("enter operator (+, -, *, /):")
second = input("enter second number:")

if operator == "+":
    result = int(first) + int(second)
    print("the result is:", result)
elif operator == "-":
    result = int(first) - int(second)
    print("the result is:", result)
elif operator == "*":
    result = int(first) * int(second)
    print("the result is:", result)
elif operator == "/":
    result = int(first) / int(second)
    print("the result is:", result)
else:
    print("invalid operator")


""" ============================================================
 TOPIC 13: WHILE LOOP
 ------------------------------------------------------------
 DEFINITION:
   A while loop REPEATS a block of code as long as a condition
   is True. It keeps checking the condition before each run.
   ⚠️ Always update the variable inside the loop, or it will
   run forever (infinite loop)!
 ============================================================"""

#while loop
i = 1
while i <= 5:
    print(i)
    i += 1


""" ===========================================================
 TOPIC 14: PATTERN PRINTING (using while loop)
 ------------------------------------------------------------
 DEFINITION:
   By multiplying a string like "*" with a number, we can
   print repeated characters. This is a common technique
   used to print patterns using loops.
 ============================================================"""

#pattern printing using while loop
i = 1
while i <= 5:
    print(i * "*")
    i += 1


""" ==========================================================
 TOPIC 15: FOR LOOP
 ------------------------------------------------------------
 DEFINITION:
   A for loop is used to ITERATE (go through) a sequence.
   range(n) generates numbers from 0 to n-1.
   range(start, stop) generates from start to stop-1.
   It is preferred when we KNOW how many times to repeat.
 ============================================================"""

#for loop
for i in range(6):
    print(i)

#pattern printing using for loop
for i in range(1, 6):
    print(i * "*")


""" ============================================================
 TOPIC 16: LIST
 ------------------------------------------------------------
 DEFINITION:
   A list is an ORDERED, CHANGEABLE collection that can hold
   multiple items in a single variable. Lists use [] brackets.
   Each item has an INDEX starting from 0.
     .append(x)      → adds x to the END of the list
     .insert(i, x)   → adds x at INDEX i
     .remove(x)      → removes first occurrence of x
     len(list)       → returns number of items in list
   Slicing: list[start:end] → gives items from start to end-1
 ============================================================"""

#list
fruits = ["apple", "banana", "orange"]
print(fruits)
print(fruits[0]) #accessing first element
print(fruits[1]) #accessing second element  
print(fruits[2]) #accessing third element
print(fruits[-1]) #accessing last element
print(fruits[0:2]) #accessing first two elements
print(fruits.append("grape")) #adding an element to the end of the list
print(fruits)
print(fruits.insert(1, "kiwi")) #adding an element at a specific index
print(fruits)
print(fruits.remove("banana")) #removing an element from the list
print(fruits)
print(len(fruits)) #finding the length of the list


""" ============================================================
 TOPIC 17: BREAK AND CONTINUE STATEMENTS
 ------------------------------------------------------------
 DEFINITION:
   These are loop control statements used to change loop behavior:
     break    → EXITS the loop completely when condition is met.
                Remaining items are NOT processed.
     continue → SKIPS the current iteration and moves to next.
                Remaining items ARE still processed.
 ============================================================"""

#break and continue statement
students = ["kuldeep", "rahul", "sneha","sidu", "anita"]
for student in students:
    if student == "sidu":
        break #this will exit the loop when it encounters "sidu"
    print(student)

students = ["kuldeep", "rahul", "sneha","sidu", "anita"]
for student in students:
    if student == "sidu":
        continue #this will skip the current iteration when it encounters "sidu"
    print(student)


""" ===========================================================
 TOPIC 18: TUPLES
 ------------------------------------------------------------
 DEFINITION:
   A tuple is an ORDERED, UNCHANGEABLE (immutable) collection.
   Tuples use () parentheses. Once created, you CANNOT add,
   remove, or change items. Use when data should stay fixed.
   Indexing and slicing works exactly like lists.
 ============================================================"""

#tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[0]) #accessing first element
print(my_tuple[3]) #accessing fourth element
print(my_tuple[-1]) #accessing last element
print(my_tuple[1:4]) #accessing elements from index 1 to 3


""" ============================================================
 TOPIC 19: SET
 ------------------------------------------------------------
 DEFINITION:
   A set is an UNORDERED collection of UNIQUE items.
   Sets use {} curly brackets. Duplicate values are removed
   automatically. Sets do NOT support indexing.
     .add(x)     → adds x to the set
     .remove(x)  → removes x from the set
     len(set)    → returns number of items in set
 ============================================================"""

#set
my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set.add(6) #adding an element to the set
print(my_set)
my_set.remove(3) #removing an element from the set
print(my_set)
print(len(my_set)) #finding the length of the set


""" ============================================================
 TOPIC 20: DICTIONARY
 ------------------------------------------------------------
 DEFINITION:
   A dictionary stores data as KEY-VALUE pairs using {} brackets.
   Each key is unique and is used to access its value.
   It is like a real dictionary — you look up a word (key)
   to get its meaning (value).
     dict[key]         → access value
     dict[key] = val   → update existing value
     dict[new_key] = val → add new key-value pair
 ============================================================"""

#dictionary
my_dict = {"name": "kuldeep", "age": 20, "city": "bhopal"}
print(my_dict)  
print(my_dict["name"]) #accessing value using key
print(my_dict["age"]) #accessing value using key
print(my_dict["city"]) #accessing value using key
my_dict["age"] = 21 #updating value using key
print(my_dict)
my_dict["country"] = "india" #adding a new key-value pair to the dictionary
print(my_dict)


""" ============================================================
 TOPIC 21: FUNCTIONS
 ------------------------------------------------------------
 DEFINITION:
   A function is a REUSABLE block of code that runs only when
   it is CALLED. Functions help avoid repeating the same code.
     def keyword    → used to DEFINE a function
     parameters     → inputs given to the function inside ()
     calling        → writing the function name with () to run it
 ============================================================"""

#functions
def greet(name):
    print("Hello, " + name + "!")
greet("kuldeep") #calling the function with an argument


def print_sum(a, b):
    sum = a + b
    print("the sum is:", sum)
print_sum(10, 5) #calling the function with arguments
print_sum(20, 30) #calling the function with different arguments
print_sum(-5, 15) #calling the function with negative and positive arguments


# ============================================================
#              END OF REVISION SHEET
# ============================================================

