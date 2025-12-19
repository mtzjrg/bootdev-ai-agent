from functions.get_file_content import get_file_content


test_working_directory = "calculator"
test_files = ["lorem.txt", "main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]

for file in test_files:
    trunc_msg = f'[...File "{file}" truncated at 10000 characters]'
    result = get_file_content(test_working_directory, file)
    print(f'Result for "{file}":')
    match result:
        case result if result.startswith("Error:"):
            print(f"  {result}")
        case _:
            print(f"  File length: {len(result)} characters\n  Truncated: {trunc_msg in result}")
            print(f"  {result.replace("\n", "\n  ")}")

