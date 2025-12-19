from functions.write_file import write_file


test_working_directory = "calculator"
test_files = {
    "lorem.txt": "wait, this isn't lorem ipsum",
    "pkg/morelorem.txt": "lorem ipsum dolor sit amet",
    "/tmp/temp.txt": "this should not be allowed",
}

for file, content in test_files.items():
    result = write_file(test_working_directory, file, content)
    print(f'Result for "{file}":\n  {result}')
