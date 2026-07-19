def decimal_to_roman(number):
    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]

    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]

    roman = ""

    for i in range(len(values)):
        while number >= values[i]:
            roman += symbols[i]
            number -= values[i]

    return roman


def main():
    try:
        number = int(input("Enter a number (1-3999): "))

        if 1 <= number <= 3999:
            print("Roman Numeral:", decimal_to_roman(number))
        else:
            print("Please enter a number between 1 and 3999.")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == "__main__":
    main()
