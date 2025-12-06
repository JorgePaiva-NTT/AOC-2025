import os
import time

def run_solution(source_file, parse_func, part1_func):
    input_path = os.path.join(os.path.dirname(source_file), 'input.txt')
    
    if not os.path.exists(input_path):
        print(f"Input file not found at {input_path}")
        return

    with open(input_path, 'r') as f:
        raw_data = f.read().strip()

    data = parse_func(raw_data)
    
    print(f"--- {os.path.basename(os.path.dirname(source_file))} ---")

    start = time.time()
    ans1 = part1_func(data)
    end = time.time()
    print(f"Part 1: {ans1} ({(end - start)*1000:.2f}ms)")
