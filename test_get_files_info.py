from functions.get_files_info import get_files_info


test_working_directory = "calculator"
test_directory = [".", "pkg", "/bin", "../"]

for dir in test_directory:
    result = get_files_info(test_working_directory, dir).replace("\n", "\n  ")
    match dir:
        case ".":
            print(f"Result for current directory:\n  {result}")
        case _:
            print(f"Result for '{dir}' directory:\n  {result}")
