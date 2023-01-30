def file_line_count(filename):
    with open(filename) as file:
        lines =file.readlines()
        total_lines = len(lines)
        return total_lines
count= file_line_count('file.txt')
print(count)