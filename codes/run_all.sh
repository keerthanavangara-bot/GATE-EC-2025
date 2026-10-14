#!/bin/bash

echo "========== RUNNING PYTHON FILES =========="

for file in *.py; do
    [ -f "$file" ] || continue

    echo ""
    echo ">>> Running $file"
    python3 "$file"

    echo ">>> Finished $file"
done

echo ""
echo "========== COMPILING AND RUNNING C FILES =========="

for file in *.c; do
    [ -f "$file" ] || continue

    output="${file%.c}"

    echo ""
    echo ">>> Compiling $file"

    if gcc "$file" -o "$output"; then
        echo ">>> Running $file"
        "./$output"
    else
        echo ">>> Compilation failed: $file"
    fi
done

echo ""
echo "========== ALL FILES PROCESSED =========="
