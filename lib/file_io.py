def write_file(file_name, file_content):
    full_file_name = str(file_name) + ".txt"
    with open(full_file_name, mode='w') as file:
        file.write(file_content)
        

def append_file(file_name, append_content):
    full_file_name = str(file_name) + ".txt"
    with open(full_file_name, mode='a') as file:
        file.write(append_content)

def read_file(file_name):
    full_file_name = str(file_name) + '.txt'
    with open(full_file_name) as file:
        for line in file:
            return line
