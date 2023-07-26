def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = [[], [], [], []]

    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == "+":
            result = int(num1) + int(num2)
        else:
            result = int(num1) - int(num2)

        width = max(len(num1), len(num2)) + 2

        arranged_problems[0].append(num1.rjust(width))
        arranged_problems[1].append(operator + " " + num2.rjust(width - 2))
        arranged_problems[2].append("-" * width)
        arranged_problems[3].append(str(result).rjust(width))

    if show_answers:
        return "\n".join("    ".join(row) for row in arranged_problems)
    else:
        return "\n".join("    ".join(row[:3]) for row in arranged_problems)


if __name__ == "__main__":
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(
        ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
