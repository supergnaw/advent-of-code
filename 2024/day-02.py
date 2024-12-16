import os
import re

sample_input = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def get_puzzle_input() -> str:
    script_name = os.path.basename(__file__)
    day_number = script_name.split('-')[1].split('.')[0]
    return open(f"inputs/day-{day_number}.txt", "r").read()


def number_of_safe_reports(raw_input: str) -> int:
    reports: list[list] = []

    for report in raw_input.strip().split("\n"):
        reports.append([int(i) for i in re.split("\s+", report.strip())])

    safe_report_count = 0

    for report in reports:
        failed_safety_checks = False
        is_increasing: bool = None

        for level in range(len(report)):

            # first level we don't care about
            if 0 == level:
                continue

            # set or check direction of increments
            if 1 == level:
                if report[0] < report[1]:
                    is_increasing = True
                else:
                    is_increasing = False
            elif is_increasing:
                # increment changed direction
                if report[level] < report[level - 1]:
                    failed_safety_checks = True
            else:
                # increment changed direction
                if report[level] > report[level - 1]:
                    failed_safety_checks = True

            # check increment distance
            increment = max(report[level], report[level - 1]) - min(report[level], report[level - 1])
            if increment < 1 or 3 < increment:
                failed_safety_checks = True

        if not failed_safety_checks:
            safe_report_count += 1

    return safe_report_count


def number_of_safe_reports_with_dampener(raw_input: str, ignore_level: int = None) -> int:
    reports: list[list] = []

    for report in raw_input.strip().split("\n"):
        reports.append([int(i) for i in re.split("\s+", report.strip())])

    safe_report_count = 0

    for report in reports:
        if report_is_safe(report):
            print(f"safe:   {report}")
            safe_report_count += 1
            continue

        print(f"initially unsafe, attempting dampener")
        for i in range(len(report)):
            dampened_report = [level for index, level in enumerate(report) if index != i]
            if report_is_safe(dampened_report):
                print(f"safe:   {dampened_report}")
                safe_report_count += 1
                break

        print(f"unsafe: {report}")

    return safe_report_count


def report_is_safe(report: list) -> bool:
    increasing = [level for level in report]
    increasing.sort()
    decreasing = [level for level in report]
    decreasing.sort(reverse=True)

    if increasing != report and decreasing != report:
        # print(f"unsafe: {report}\n - increment changes direction")
        return False

    for l in range(len(report)):
        if 0 == l:
            continue

        increment = max(report[l], report[l - 1]) - min(report[l], report[l - 1])
        if 1 > increment:
            # print(f"unsafe: {report} - no level change between {report[l - 1]} and {report[l]}")
            return False
        if 3 < increment:
            # print(f"unsafe: {report}\n - level change greater than 3 from {report[l - 1]} to {report[l]}")
            return False
    return True


print("\n# Part I: part_one_function\n")
print(f"sample input: {number_of_safe_reports(sample_input)}")
print(f"puzzle input: {number_of_safe_reports(get_puzzle_input())}")

print("\n# Part II: part_two_function\n")
print(f"sample input: {number_of_safe_reports_with_dampener(sample_input)}")
print(f"puzzle input: {number_of_safe_reports_with_dampener(get_puzzle_input())}")
