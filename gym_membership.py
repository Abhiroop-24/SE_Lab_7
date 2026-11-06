def parse_plan(code):
    """
    Parses a gym membership plan code in format '<PLAN>-<MONTHS>' (e.g., 'GOLD-12').
    Returns a tuple (plan.upper(), months) on valid input, or (None, None) / None on invalid input.
    """
    try:
        if not isinstance(code, str):
            return None
        parts = code.split('-')
        if len(parts) != 2:
            return None
        plan = parts[0].strip()
        months_str = parts[1].strip()
        if not plan or not months_str:
            return None
        months = int(months_str)
        if months <= 0:
            return None
        return plan.upper(), months
    except Exception:
        return None


def calculate_bmi(data):
    """
    Calculates BMI given weight in kg and height in meters (e.g., '70,1.75').
    Returns round(weight / (height ** 2), 1) on valid input, or None on invalid input.
    """
    try:
        if not isinstance(data, str):
            return None
        parts = data.split(',')
        if len(parts) != 2:
            return None
        weight = float(parts[0].strip())
        height = float(parts[1].strip())
        if height <= 0 or weight <= 0:
            return None
        bmi = weight / (height ** 2)
        return round(bmi, 1)
    except Exception:
        return None


def average_workout(minutes):
    """
    Calculates average workout duration from space-separated integer minutes (e.g., '45 60 30').
    Returns average integer minutes on valid input, or None on invalid input.
    """
    try:
        if not isinstance(minutes, str):
            return None
        parts = minutes.split()
        if not parts:
            return None
        values = [int(m) for m in parts]
        if any(v < 0 for v in values):
            return None
        return sum(values) // len(values)
    except Exception:
        return None


def main():
    print("==== Running parse_plan ====")
    user_input = input("Enter a plan code (e.g. GOLD-12): ")
    result = parse_plan(user_input)
    print("Plan and Months:", result)

    print("\n==== Running calculate_bmi ====")
    user_input = input("Enter weight and height (e.g. 70,1.75): ")
    result = calculate_bmi(user_input)
    print("BMI:", result)

    print("\n==== Running average_workout ====")
    user_input = input("Enter workout minutes separated by spaces (e.g. 45 60 30): ")
    result = average_workout(user_input)
    print("Average Minutes:", result)


if __name__ == "__main__":
    main()
