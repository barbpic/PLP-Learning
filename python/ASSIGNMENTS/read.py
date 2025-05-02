def read_and_modify_file():
    try:
        # Ask user for input filename
        input_file = input("Enter the name of the file to read: ")

        with open("python/ASSIGNMENTS/my_list.py", 'r') as file:
            content = file.read()

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        # Define output filename
        output_file = "modified_" + input_file

        with open("python/ASSIGNMENTS/my_list.py", 'w') as file:
            file.write(modified_content)

        print(f"Modified content written to '{output_file}' successfully!")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Could not read/write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()
