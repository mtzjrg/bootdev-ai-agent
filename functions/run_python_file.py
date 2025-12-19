import os
from subprocess import run


def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        cmd = ["python", f"{target_file}"]
        if args:
            cmd.extend(args)
        result = run(cmd, capture_output=True, cwd=working_dir_abs, timeout=30, text=True)

        pretty_result = f"STDOUT: \n{result.stdout}" if result.stdout != "" else "STDOUT: No output produced"
        pretty_result += f"\nSTDERR: \n{result.stderr}" if result.stderr != "" else "\nSTDERR: No output produced"
        if result.returncode != 0:
            pretty_result += f"\nProcess exited with code {result.returncode}"
    except Exception as e:
        return f"Error: executing Python file: {e}"
    return f"{pretty_result}"
