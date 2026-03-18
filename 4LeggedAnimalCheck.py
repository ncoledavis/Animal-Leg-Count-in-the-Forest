animals = ['lion', 'tiger', 'bear', 'dog']

def four_legged_animals(user_list):
    matches = [a for a in user_list if  a in animals]
    count = len(matches)

    if count == 0:
        explanation = "There are no 4 legged animals."
    elif count == 1:
        explanation = f"'{matches[0]}' has four legs."
    elif count == 2: 
        explanation = f"'{matches[0]}' and '{matches[1]}' have four legs."
    else:
        explanation = (
            ", ".join(f"'{m}'" for m in matches[:-1]) 
            + f", and '{matches[-1]}' have four legs."
        )

    return f"Count: {count}. Explanation: From the selected inputs {explanation}"
def parse_input(raw):
    return [t.strip().lower() for t in raw.replace(",", " ").split() if t.strip()]

user_input = input("Enter animals seperated by commas: ")
user_animals = parse_input(user_input)
result = four_legged_animals(user_animals)
print(result)