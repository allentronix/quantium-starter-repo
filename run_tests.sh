#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run test suite
python -m pytest

# Store the result
TEST_RESULT=$?

# Return correct exit code
if [ $TEST_RESULT -eq 0 ]; then
    exit 0
else
    exit 1
fi