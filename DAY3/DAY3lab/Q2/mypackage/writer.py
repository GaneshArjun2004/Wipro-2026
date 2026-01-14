def write_numbers_to_file(filename):
    try:
        with open(filename, "w") as f:
            for i in range(1, 101):
                f.write(str(i) + "\n")
        print(f"Numbers written successfully to {filename}")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
