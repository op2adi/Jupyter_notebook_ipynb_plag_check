import os
import nbformat
from nbconvert import PythonExporter
import subprocess

def find_files(directory, extensions=[".ipynb", ".py"]):
    """Recursively find all files with the given extensions in the directory."""
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                files.append(os.path.join(root, filename))
    return files

def convert_ipynb_to_py(ipynb_file, output_dir):
    """Convert an .ipynb file to a .py file."""
    with open(ipynb_file, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)
    exporter = PythonExporter()
    python_code, _ = exporter.from_notebook_node(notebook)
    
    py_file = os.path.join(output_dir, os.path.basename(ipynb_file).replace('.ipynb', '.py'))
    with open(py_file, 'w', encoding='utf-8') as f:
        f.write(python_code)
    return py_file

def submit_to_moss(py_files, base_files):
    """
    Submit converted .py files to MOSS, excluding boilerplate in base files.
    
    Args:
        py_files (list): List of paths to the .py files to be submitted.
        base_files (list): List of paths to base .py files to be excluded as boilerplate.
    """
    moss_command = [
        "perl", "./moss.pl", "-l", "python", 
    ]
    
    # Add base files
    for base_file in base_files:
        moss_command.extend(["-b", base_file])
    
    # Adding  submission files
    moss_command.extend(py_files)
    print(" ".join(moss_command))

    #Using for running 
    subprocess.run(moss_command)
    print("MOSS submission complete with base files excluded as boilerplate.")

def main():
    source_dir = "source"
    base_dir = "base"

    # Create output directory for converted .py files
    output_dir = "converted_files"
    base_output_dir = "base_converted_files"
    os.makedirs(output_dir, exist_ok=True)

    # Find all .ipynb and .py files in source and base directories
    source_files = find_files(source_dir)
    base_files = find_files(base_dir)

    # Separate .ipynb files and .py files
    source_ipynb_files = [f for f in source_files if f.endswith('.ipynb')]
    source_py_files = [f for f in source_files if f.endswith('.py')]
    
    base_ipynb_files = [f for f in base_files if f.endswith('.ipynb')]
    base_py_files = [f for f in base_files if f.endswith('.py')]

    # Convert base .ipynb files to .py
    base_py_files_converted = [convert_ipynb_to_py(f, base_output_dir) for f in base_ipynb_files]

    # Convert source .ipynb files to .py
    source_py_files_converted = [convert_ipynb_to_py(f, output_dir) for f in source_ipynb_files]

    # Combine original and converted .py files for submission
    all_py_files = source_py_files + source_py_files_converted
    
    # Submit .py files to MOSS with base files as boilerplate
    submit_to_moss(all_py_files, base_py_files + base_py_files_converted)

    print("MOSS submission complete with base files excluded as boilerplate.")

if __name__ == "__main__":
    main()
