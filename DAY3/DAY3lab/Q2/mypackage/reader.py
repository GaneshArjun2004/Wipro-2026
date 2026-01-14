from mypackage.writer import write_numbers_to_file

def read_numbers_from_file(filename):
    try:
        with open(filename, "r") as f:
            content = f.readlines()
        print("File content read successfully:")
        for line in content[:10]:   # show first 10 lines for brevity
            print(line.strip())
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")


if __name__ == "__main__":
    filename = "numbers.txt"
    write_numbers_to_file(filename)
    read_numbers_from_file(filename)
