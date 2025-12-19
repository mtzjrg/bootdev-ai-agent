from functions.run_python_file import run_python_file


test_working_directory = "calculator"
test_files = ["main.py", "main.py", "tests.py", "../main.py", "nonexistent.py", "lorem.txt"]
test_arg = ["3 + 5"]

for idx in range(len(test_files)):
    if idx == 1:
        print(f'Result for "{test_files[idx]}", "{test_arg}":')
        result = run_python_file(test_working_directory, test_files[idx], test_arg)
    else:
        print(f'Result for "{test_files[idx]}":')
        result = run_python_file(test_working_directory, test_files[idx])
    print(f"  {result.replace("\n", "\n  ")}")

