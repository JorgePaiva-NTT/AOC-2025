import os
import time

def run_solution(source_file, parse_func, part1_func, part2_func, is_test=False):
    input_path = os.path.join(os.path.dirname(source_file), 'input.txt')
    input_test_path = os.path.join(os.path.dirname(source_file), 'input_test.txt')
    
    if is_test and os.path.exists(input_test_path):
        input_path = input_test_path

    if not os.path.exists(input_path):
        print(f"Input file not found at {input_path}")
        return

    print(input_path)

    with open(input_path, 'r') as f:
        raw_data = f.readlines()

    data = parse_func(raw_data)
    
    print(f"--- {os.path.basename(os.path.dirname(source_file))} ---")

    start = time.time()
    ans1 = part1_func(data)
    end = time.time()
    
    print(f"Part 1: {ans1} ({(end - start)*1000:.2f}ms)")
    
    start = time.time()
    ans2 = part2_func(data)
    end = time.time()
    
    print(f"Part 2: {ans2} ({(end - start)*1000:.2f}ms)")
    
