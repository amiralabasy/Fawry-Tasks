#!/bin/bash

# Show help function
show_help() {
  echo "Usage: $0 [options] search_string filename"
  echo "Options:"
  echo "  -n   Show line numbers for matching lines"
  echo "  -v   Invert match (show non-matching lines)"
  echo "  --help   Show this help message"
}

# Check for --help
if [[ "$1" == "--help" ]]; then
  show_help
  exit 0
fi

# Parse options
show_line_numbers=false
invert_match=false

while [[ "$1" =~ ^- ]]; do
  case "$1" in
    *n*) show_line_numbers=true ;;
    *v*) invert_match=true ;;
    *) echo "Error: Unknown option $1"; show_help; exit 1 ;;
  esac
  shift
done

# Validate arguments
if [[ $# -lt 2 ]]; then
  echo "Error: Missing search string or filename."
  show_help
  exit 1
fi

search_string="$1"
filename="$2"

# Validate file
if [[ ! -f "$filename" ]]; then
  echo "Error: File $filename not found."
  exit 1
fi

# Main logic
if $invert_match; then
  if $show_line_numbers; then
    grep -inv "$search_string" "$filename"
  else
    grep -iv "$search_string" "$filename"
  fi
else
  if $show_line_numbers; then
    grep -in "$search_string" "$filename"
  else
    grep -i "$search_string" "$filename"
  fi
fi