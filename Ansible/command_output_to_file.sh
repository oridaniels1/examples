#!/bin/bash

# Function to display the usage of the script
display_usage() {
    echo "Usage: $0 [-c <command>] [-n <notes>] [-o <output_file>]"
    echo "Options:"
    echo "  -c <command>        Specify the command to execute"
    echo "  -n <notes>          Add notes before the output"
    echo "  -o <output_file>    Specify the output file (default: output.txt)"
}

# Default values
output_file="output.txt"
command=""
notes=""

# Parse command-line arguments
while getopts ":c:n:o:" option; do
    case "${option}" in
        c)
            command=${OPTARG}
            ;;
        n)
            notes=${OPTARG}
            ;;
        o)
            output_file=${OPTARG}
            ;;
        *)
            display_usage
            exit 1
            ;;
    esac
done

# Check if the mandatory command is provided
if [[ -z $command ]]; then
    echo "Error: Command is required."
    display_usage
    exit 1
fi

# Add notes to the output file
if [[ -n $notes ]]; then
    echo "$notes" >> "$output_file"
fi

# Execute the command and append output to the file
eval "$command" >> "$output_file"

echo "Output written to $output_file"
