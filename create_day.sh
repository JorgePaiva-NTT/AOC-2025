#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <day_number>"
  exit 1
fi

DAY=$1
FOLDER_NAME="D$DAY"

# Create directory
if [ ! -d "$FOLDER_NAME" ]; then
  mkdir "$FOLDER_NAME"
  echo "Created folder: $FOLDER_NAME"
else
  echo "Folder $FOLDER_NAME already exists."
fi

PY_FILE="$FOLDER_NAME/day$DAY.py"
README_FILE="$FOLDER_NAME/README.md"
INPUT_FILE="$FOLDER_NAME/input.txt"
INPUT_TEST_FILE="$FOLDER_NAME/input_test.txt"
TEMPLATE_FILE="template.py"

# Create python file
if [ ! -f "$PY_FILE" ]; then
  if [ -f "$TEMPLATE_FILE" ]; then
    cp "$TEMPLATE_FILE" "$PY_FILE"
    echo "Created file: $PY_FILE (from template)"
  else
    touch "$PY_FILE"
    echo "Created file: $PY_FILE (empty)"
  fi
fi

# Create README
if [ ! -f "$README_FILE" ]; then
  touch "$README_FILE"
  echo "Created file: $README_FILE"
fi

# Create input files
if [ ! -f "$INPUT_FILE" ]; then
  touch "$INPUT_FILE"
  echo "Created file: $INPUT_FILE"
fi

if [ ! -f "$INPUT_TEST_FILE" ]; then
  touch "$INPUT_TEST_FILE"
  echo "Created file: $INPUT_TEST_FILE"
fi

echo "Done setup for Day $DAY"
