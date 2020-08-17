import os

TRIANING_FILES = 27367
VALIDATION_FILES = 3000

total_states = 0
training_states = 0
validation_states = 0
total_files = 0
for filename in os.listdir("../data/ida-solutions"):
    file = open("../data/ida-solutions/" + filename, "r")
    states_in_file = len(file.readlines())
    total_states += states_in_file
    if total_files < TRIANING_FILES:
        training_states += states_in_file
    else:
        validation_states += states_in_file
    total_files += 1

print("TOTAL FILES: ", total_files)
print("TOTAL STATES: ", total_states)
print()
print("training states: ", training_states)
print("validation states: ", validation_states)
