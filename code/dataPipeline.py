# Data Pipeline Example

def start_coroutine(func):
    def inner_function(*args, **kwargs):
        var = func(*args, **kwargs)
        var.__next__()
        return var
    return inner_function

# Read the file line by line
def start_data_pipeline(file, next_stage):
    while True:
        line = file.readline()
        if not line:
            break
        next_stage.send(line)

# Search for the word in each line
@start_coroutine
def filter_word(word, next_stage):
    while True:
        line = yield
        if word in line:
            next_stage.send(line)

# Save the entire line in DB if word is found
@start_coroutine
def save_to_db():
    count = 0
    while True:
        line = yield
        print(f"{line} saved to db")
        count +=1
        print(f"the word count is {count}")

# Open the text file and start the data pipeline
file = open(r".\code\harry_potter_goblet_of_fire.txt")
start_data_pipeline(file, filter_word("Harry", save_to_db()))





