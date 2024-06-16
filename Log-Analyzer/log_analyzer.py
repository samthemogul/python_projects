import os
import sys
import pathlib

def most_used_test_type(log_lines):
    # Finds the most used type of test

    test_types = ["System","Performance","Functional"]
    system_type_count = 0
    perform_type_count = 0
    functional_type_count = 0
    for tests in log_lines:
        if test_types[0] in tests:
            system_type_count += 1
        elif test_types[1] in tests:
            perform_type_count += 1
        elif test_types[2] in tests:
            functional_type_count += 1
    test_types_count = {
            "System": system_type_count,
            "Performance": perform_type_count,
            "Functional": functional_type_count,
    }
    max_text_type = max(test_types_count["System"], test_types_count["Performance"], test_types_count["Functional"])
    for keys in test_types_count:
        if test_types_count[keys] == max_text_type:
            return keys
    pass 

def failure_map(log_lines):
    # Count the failures per test type. A test failure has the word "FAIL" in 
    # the test output.

    system_fail_count = 0
    perform_fail_count = 0
    function_fail_count = 0
    for tests in log_lines:
        if "System" in tests and "FAIL" in tests:
            system_fail_count += 1
        elif "Performance" in tests and "FAIL" in tests:
            perform_fail_count += 1
        elif "Functional" in tests and "FAIL" in tests:
            function_fail_count += 1
    failures = {
            
            "Performance": perform_fail_count,
            "Functional": function_fail_count,
            "System": system_fail_count
            }
    return failures

def count_tests(log_lines):
    return len(log_lines)

def format_failures(results):
    # Format the failure counts table
    table = [f"Type\t\tCount"]
    for test_type, count in results.items():
        table.append(f"{test_type}  \t{count}")
    return "\n".join(table)


def count_phrase(log_lines, phrase):
    # Count the occurrences of a phrase in the log lines
    
    count = 0
    for test_line in log_lines:
        if phrase in test_line:
            count += 1
    return count


def analyze_logs(log):
    # Analyze the lines of the log file

    log_lines = log.splitlines()
    phrase = "component"
    test_count = count_tests(log_lines)
    most_used_type = most_used_test_type(log_lines)
    failure_table = failure_map(log_lines)
    phrase_count = count_phrase(log_lines, phrase)

    return f"""Number of tests: {test_count}
Most used type of test: {most_used_type}
Tests related to \"{phrase}\": {phrase_count}

Failures:
{format_failures(failure_table)}
"""

def write_stats(report, destination):
    """
    Write the report to a destination file
    """
    with open(file=destination, mode='w') as dest:
        dest.write(report)


if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python log_analyzer.py [input_file] [output_file]")
        exit()

    input_filename = sys.argv[1]
    with open(input_filename) as f:
        report = analyze_logs(f.read())
    if len(sys.argv) == 2:
        print(report)
    elif len(sys.argv) == 3:
        output_file = sys.argv[2] 
        write_stats(report, output_file)
