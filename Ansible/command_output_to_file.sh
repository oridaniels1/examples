#!/bin/bash

# Function to execute the command and send output to a file
execute_command() {
    command=$1
    output_file=$2

# Execute the command and redirect the output to the file
    $command > "$output_file"

    echo "Command output saved to $output_file"
}

# Main script
# Check if the command option is provided
if [[ $1 == "-c" ]]; then
# Check if both the command and output file options are provided
    if [[ -n $2 && -n $3 ]]; then
        command_to_execute=$2
        output_file_path=$3

# Call the function to execute the command and send output to the file
        execute_command "$command_to_execute" "$output_file_path"
    else
        echo "Error: Both command and output file options are required."
        echo "Usage: bash script.sh -c 'command' output_file.txt"
    fi
else
    echo "Error: Invalid option. Please use the -c option to specify the command."
    echo "Usage: bash script.sh -c 'command' output_file.txt"
fi
