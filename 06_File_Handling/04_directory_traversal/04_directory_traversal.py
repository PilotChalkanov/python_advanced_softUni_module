import os
import io

def dir_traversal(dir_path, result):
    for element in os.listdir(dir_path):
        file_with_path = os.path.join(dir_path, element)
        if os.path.isfile(file_with_path):
            ext = element.split('.')[-1]
            if ext not in result:
                result[ext] = []
                result[ext].append(file_with_path)

        elif os.path.isdir(file_with_path):
            dir_traversal(file_with_path,result)
result ={}
dir_traversal(os.getcwd(),result)
with open('report.txt', 'w') as report_file:
    for ext,files in sorted(result.items()):
        report_file.write(f'.{ext}')
        report_file.write('\n')
        for file in sorted(files):
            report_file.write(f'--- {file}')
            report_file.write('\n')