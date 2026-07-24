# My Git & GitHub Learning Notes

## Day 1 — July 11, 2026

**What I did:**
- Installed Git, configured user.name and user.email
- Created a local repo using git init
- Created test.py and made my first commit
- Created a GitHub repo named "git-practice"
- Connected local repo to GitHub using git remote add
- Pushed my first commit to GitHub
- Added a README.md directly on GitHub

**Commands learned:**
- git init
- git config --global user.name
- git config --global user.email
- git status
- git add .
- git commit -m "message"
- git remote add origin
- git branch -M main
- git push -u origin main

**Key learning:**
- Git = tool on my laptop that tracks changes
- GitHub = website that hosts my git repos online

## Day 2 — July 12, 2026

What I did:
- Day 1 was only about Git & GitHub basics (no Python yet)
- Since I already know basic Python, today I started practicing 
  small Python problems and committing them using Git
- First practice: Variable swap without using a third variable

Concept practiced:
- Method 1: Tuple unpacking → a, b = b, a
- Method 2: Arithmetic (+ and -) → x = x+y, y = x-y, x = x-y

Goal: Build a daily habit of practicing Python + committing to GitHub

## Day 3 — July 13, 2026

What I did:
- Learned and practiced about Data Types in Python
- Explored how Python automatically detects the type of a variable
- Practiced using type() function to check data types

## Day 4 — July 14, 2026

What I did:
- Fixed my entire repo folder structure (major cleanup)
- Found that "day 1" folder had git repo (.git) inside it instead of the root
  - Moved .git folder from "day 1" to root level using Move-Item
  - Moved day2 and day3 folders out of day1, into root level
  - Moved test.py, README.md, notes.md into a proper "day 1" folder for consistency
  - Verified with git status that everything was tracked as "renamed" (clean history)
  - Committed and pushed the fix successfully

- Practiced if-elif-else conditionals
  - Wrote a program to check if a number is positive, negative, or zero
  - First attempt had a bug: used nested if instead of elif
  - Nested if = each condition checked only if the outer one was true (wrong logic)
  - elif = all conditions checked at the same level, only one runs (correct logic)
  - Fixed the code by aligning if-elif-else at the same indentation
  - Tested with 0, positive, and negative numbers — all worked correctly

Achievement unlocked today:
- Learned to debug and fix a real folder/repo structure issue independently 
- Learned the difference between nested if and elif through a real mistake
- First time fixing a logic bug by understanding indentation in Python

Note: I used an AI chatbot as a guide to help me understand and fix the 
issues I ran into today. I made sure to understand the reasoning behind 
each fix rather than just copying solutions, which helped me learn Git 
internals and Python logic more deeply.

## Day 5 — July 15, 2026

What I did:
- Practiced for loop and while loop basics
- Printed numbers 1 to 10 using for loop with range()
- Printed even numbers between 1-10 using for loop + if condition

## Day 6 — July 16, 2026

What I did:
- Built a simple ATM system using while loop, if-elif-else, and break
- Menu-driven program: Check Balance, Deposit, Withdraw, Exit
- Used while True: with break to keep the menu running until user exits
- Handled insufficient balance case during withdrawal using if condition
- Practiced updating a variable (balance) across multiple loop iterations
- Realized my first version had no PIN check — added PIN verification 
  before allowing access to the menu (with limited attempts, like a 
  real ATM blocking the card after 3 wrong tries)

Concept learned:
- while True: creates an infinite loop that keeps running until explicitly stopped
- break exits the loop immediately when a condition is met
- Combined loops + conditionals + user input to build a real mini-project
- Learned to think about missing real-world logic (like PIN security) 
  and add it after reviewing my own code

## Day 7 — July 17, 2026
What I did:
- Built a terminal-based Washing Machine Control Simulation using a while True loop and conditional if-elif-else logic.
- Implemented a 4-option main menu: Select Mode, Start Wash, Check Time Remaining, and Exit.
- Created a nested menu under "Select Mode" to set specific wash cycles with dynamic configurations:
   Quick Wash: 15 minutes
   Normal Wash: 30 minutes
   Heavy Wash: 45 minutes
- Handled state validation by ensuring the user cannot start the wash or check the remaining time without selecting a wash mode first (current_mode is None).
- Used error-handling else blocks and the continue keyword to reset the loop if the user enters an invalid mode.

Concepts learned:
- State Initialization: Using None as a placeholder for a variable (current_mode) to track whether an action has taken place yet.
- Nested Conditionals: Writing if-elif-else structures inside another if block to handle multi-layered user choices.
- Loop Control Flow: Using continue to instantly skip the rest of the current loop iteration and restart from the top, preventing invalid data from processing.
- Case Sensitivity in Variables: Realized how a single accidental capitalization (like Wash_time vs wash_time) can cause a bug, reinforcing the importance of consistent naming conventions.

## Day 8 — July 18, 2026

What I did:
- Learned Python's built-in data structures: List, Tuple, Dictionary, Set
- Practiced creating and modifying a List (append, remove)
- Practiced Tuple (immutable, cannot be changed after creation)
- Practiced Dictionary (key-value pairs, added/updated keys)
- Practiced Set (unordered, automatically removes duplicates)
- Faced a VS Code warning "python-envs.runAs not found" — fixed by updating VS Code

Concept learned:
- List: ordered, changeable, allows duplicates
- Tuple: ordered, unchangeable, allows duplicates
- Dictionary: key-value pairs, keys must be unique
- Set: unordered, no duplicates allowed — useful for removing duplicate values
- Choosing the right data structure depends on whether data needs to change, 
  stay ordered, or avoid duplicates

## Day 9 — July 19, 2026

What I did:
- Practiced List methods: append, insert, remove, pop, sort, reverse, 
  index, clear, len
- Practiced List slicing and looping through a list
- Practiced Tuple operations: indexing, slicing, count, index, len
- Learned that tuples are immutable — to modify one, I need to convert 
  it to a list first, make changes, then convert it back to a tuple

Concept learned:
- List methods can directly change (mutate) the list
- Tuple has only read-only methods (count, index) — no way to modify it directly
- Slicing works the same way for both lists and tuples: [start:end]
- numbers[::-1] is a quick way to reverse any list or tuple

## Day 10 — July 20, 2026

What I did:
- Practiced Dictionary methods: get(), update(), keys(), values(), items(), pop()
- Learned the difference between direct access (student["key"]) and 
  .get() method — direct access throws an error if key doesn't exist, 
  but .get() safely returns None or a default value
- Looped through a dictionary using .items() to print key-value pairs
- Added, updated, and removed keys from a dictionary

Concept learned:
- .get() is safer than direct indexing when a key might not exist
- .update() can add a new key or update an existing one
- .items() is the standard way to loop through both keys and values together
- Dictionaries are very useful for storing structured data (like a student 
  record, config settings, or API response data)

  ## Day 11 — July 21, 2026

What I did:
- Practiced Set operations: union (|), intersection (&), difference (-), and symmetric difference (^)
- Learned both operator style (|, &, -, ^) and method style (.union(), .intersection(), .difference(), .symmetric_difference())
- Explored Set methods: add(), update(), remove(), discard(), and pop()
- Understood the difference between remove() and discard() — remove() throws a KeyError if the element is missing, but discard() does not
- Learned that pop() removes a random element since sets are unordered
- Practiced subset, superset, and disjoint checks using issubset(), issuperset(), and isdisjoint()
- Built a real-world example using sets to find common friends, all friends, and unique friends between two people

Key takeaways:
- Sets store only unique elements — duplicates are automatically removed
- Sets are unordered, so indexing is not possible
- Set operations are very useful for comparing data (finding common items, unique items, etc.)
- Use | for union, & for intersection, - for difference, ^ for symmetric difference
- Use discard() instead of remove() when you're not sure if the element exists

## Day 12 — July 22, 2026

What I did:
- Practiced writing basic Python functions
- Created functions with parameters and return values
- Learned the difference between print() and return inside a function
- Practiced default parameter values (like name="Guest")
- Wrote and tested functions: add_numbers(), square(), welcome()

Concept learned:
- def keyword is used to define a function
- Functions help avoid repeating the same code again and again
- print() only displays output, return actually sends a value back that 
  can be stored and reused
- Default parameters let a function work even if no argument is passed

## Day 13 — July 23, 2026

What I did:
- Practiced common String methods: strip(), lower(), upper(), replace(), split()
- Practiced string checks: startswith(), endswith(), isdigit(), isalpha()
- Practiced string slicing and indexing (first character, last character, substring)
- Learned split() and join() as a pair — split() converts a string into 
  a list, join() converts a list back into a string
- Solved a practice problem: cleaned a sentence with extra spaces, changed 
  case, replaced a word, counted words, and checked if it starts with a 
  specific word

Concept learned:
- strip() only removes spaces from the start and end, not in the middle
- Always strip() before using startswith()/endswith() if the string might 
  have extra leading/trailing spaces — otherwise the check can wrongly 
  return False
- split() automatically handles multiple/extra spaces between words
- String methods don't change the original string — they return a new one 
  (strings are immutable in Python)

  ## Day 14 — July 24, 2026

What I did:
- Practiced Lambda functions — short, one-line functions without def
- Used lambda together with sorted(), filter(), and map()
- Practiced *args — allows a function to accept any number of arguments, 
  treated as a tuple inside the function
- Learned **kwargs — allows any number of named arguments, treated as 
  a dictionary inside the function

Concept learned:
- lambda is used for small, throwaway functions, usually passed as an 
  argument to another function (like sorted, filter, map)
- *args is useful when you don't know in advance how many values will 
  be passed to a function
- **kwargs is useful when you want to pass named data (like key=value 
  pairs) without fixing the parameter names in advance
- filter() keeps only the elements where the lambda condition is True
- map() applies the lambda to every element and returns the transformed results