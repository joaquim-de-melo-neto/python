def line_count(file_name:str):
    count = 0
    for line in open(file_name):
        count += 1
    return count

print(line_count('C:\\Users\\Londres31\\Desktop\\texto.txt'))