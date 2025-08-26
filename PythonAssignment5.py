def process_file():
    # Ask the user for the input filename
    input_filename = input("📂 Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify the content (example: reverse each line)
        modified_lines = [line[::-1] for line in content.splitlines()]
        modified_content = "\n".join(modified_lines)

        # Define the output filename
        output_filename = "modified_" + input_filename

        # Write the modified content to the new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ Success! Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"🚫 Error: Permission denied when trying to read '{input_filename}'.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

# Run the function
process_file()