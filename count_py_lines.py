import os

def count_lines_in_py_files(directory):
    total_lines = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        lines = content.splitlines()
                        line_count = len(lines)
                        if content.endswith('\n'):
                            line_count += 1
                        
                        print(f"\n{file_path}: {line_count} lines")
                        print("File content:")
                        for i, line in enumerate(lines, 1):
                            print(f"{i}: {line}")
                        if content.endswith('\n'):
                            print(f"{line_count}: <empty line>")
                        
                        total_lines += line_count
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return total_lines

current_directory = os.getcwd()
total_lines = count_lines_in_py_files(current_directory)
print(f"\nTotal lines in all Python files: {total_lines}")

