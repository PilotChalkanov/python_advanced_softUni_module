import os


class File_Manipulator():
    ERROR_MASSAGE = "An error occured"

    def __init__(self, file_name):
        self.file_name = file_name

    def add_file(self, file_name, content):
        with open(f"{file_name}", 'a') as file:
            file.writelines(content + '\n')

    def create_file(self, file_name):
        with open(f"{file_name}", 'w') as file:
            file.writelines("")

    def replace_file(self, file_name, content1, content2):
        try:
            with open(f"{file_name}", "r+") as file:
                lines = file.read().replace(content1, content2)
                file.seek(0)
                file.truncate()
                file.writelines(lines)

        except FileNotFoundError:
            print(self.ERROR_MASSAGE)

    def delete_file(self, file_name):
        try:
            os.remove(f"{file_name}")
        except FileNotFoundError:
            print(self.ERROR_MASSAGE)


command = input()
while command != "End":
    line = command.split("-")
    action = line[0]
    file_name = line[1]
    file_executor = File_Manipulator(file_name)
    if action == 'Create':
        file_executor.create_file(file_name)
    elif action == 'Add':
        content = line[2]
        file_executor.add_file(file_name, content)
    elif action == 'Replace':
        content1 = line[2]
        content2 = line[3]
        file_executor.replace_file(file_name, content1, content2)
    elif action == 'Delete':
        file_executor.delete_file(file_name)
    command = input()
