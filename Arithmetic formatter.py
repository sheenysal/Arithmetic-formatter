def arithmetic_arranger(problems=None, display_answers=False):
    """
    Arrange arithmetic problems vertically and optionally display the answers.

    Parameters:
    problems (list): A list of strings containing arithmetic problems.
    display_answers (bool): Whether to display the answers to the problems.

    Returns:
    str: The arranged problems or an error message if input is invalid.
    """
    # Allow user to input problems if not provided
    if problems is None:
        problems = input("Enter arithmetic problems separated by commas: ").split(',')
        problems = [problem.strip() for problem in problems]

    # Error checks
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_operands = []
    second_operands = []
    operators = []
    answers = []

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return 'Error: Invalid problem format.'

        num1, operator, num2 = parts

        if operator not in ('+', '-', '*'):
            return "Error: Operator must be '+' or '-' or '*'."

        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'

        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        # Add operands and operator to their respective lists
        first_operands.append(num1)
        second_operands.append(num2)
        operators.append(operator)

        # Calculate answer if display_answers is True
        if display_answers:
            if operator == '+':
                answers.append(str(int(num1) + int(num2)))
            elif operator == '-':
                answers.append(str(int(num1) - int(num2)))
            elif operator == '*':
                answers.append(str(int(num1) * int(num2)))

    # Prepare arranged problems
    top_row = []
    bottom_row = []
    dashes = []
    results = []

    for i in range(len(first_operands)):
        num1 = first_operands[i]
        num2 = second_operands[i]
        operator = operators[i]

        width = max(len(num1), len(num2)) + 2

        top_row.append(num1.rjust(width))
        bottom_row.append(operator + ' ' + num2.rjust(width - 2))
        dashes.append('-' * width)

        if display_answers:
            results.append(answers[i].rjust(width))

    # Combine rows
    arranged_problems = '    '.join(top_row) + '\n'
    arranged_problems += '    '.join(bottom_row) + '\n'
    arranged_problems += '    '.join(dashes)

    if display_answers:
        arranged_problems += '\n' + '    '.join(results)

    return arranged_problems


if __name__ == "__main__":
    print("Welcome to the Arithmetic Arranger!")
    print("You can enter up to 5 arithmetic problems using '+' or '-' or '*' operators.")
    print("Example input: 32 + 8, 1 - 3801, 523 - 49, 45 * 3")

    problems_input = input("Enter your problems separated by commas: ").split(',')
    problems_input = [problem.strip() for problem in problems_input]

    show_answers = input("Do you want to display the answers? (yes/no): ").strip().lower() == 'yes'

    result = arithmetic_arranger(problems_input, show_answers)
    print(result)
