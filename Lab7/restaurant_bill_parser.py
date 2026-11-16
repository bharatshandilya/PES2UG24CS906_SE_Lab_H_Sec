def clean_dish_name(name):
    """Remove menu-special markers and title-case a dish name.

    Invalid non-string inputs return an empty string instead of raising
    an exception. Normal string inputs retain the original behaviour.
    """
    if not isinstance(name, str):
        return ""

    name = name.strip()

    for marker in ("*", "#", "~"):
        name = name.replace(marker, "")

    return name.title()

def parse_item_prices(text):
    """Parse comma-separated, non-negative whole-number prices.

    Returns an empty list for non-string, empty, or malformed input.
    The complete input is rejected if any token is invalid.
    """
    if not isinstance(text, str):
        return []

    text = text.strip()

    if not text:
        return []

    prices = []

    for token in text.split(","):
        token = token.strip()

        if not token or not token.isdecimal():
            return []

        try:
            price = int(token)
        except (TypeError, ValueError):
            return []

        if price < 0:
            return []

        prices.append(price)

    return prices

def split_amount(text):
    """Return the whole-number share for a TOTAL/PEOPLE bill split.

    Invalid input, negative totals, or a non-positive people count
    return 0. Integer floor division is retained from the original code.
    """
    if not isinstance(text, str):
        return 0

    parts = text.split("/")

    if len(parts) != 2:
        return 0

    total_text, people_text = (part.strip() for part in parts)

    if not total_text.isdecimal() or not people_text.isdecimal():
        return 0

    try:
        total = int(total_text)
        people = int(people_text)
    except (TypeError, ValueError):
        return 0

    if total < 0 or people <= 0:
        return 0

    return total // people

def main():
    print("==== Running clean_dish_name ====")
    value = input("Enter a dish name from the menu (e.g. *paneer tikka*): ")
    print("Dish name:", clean_dish_name(value))

    print("\n==== Running parse_item_prices ====")
    value = input("Enter item prices separated by commas (e.g. 250,180,320): ")
    print("Item prices:", parse_item_prices(value))

    print("\n==== Running split_amount ====")
    value = input("Enter the bill and number of people as TOTAL/PEOPLE (e.g. 1200/4): ")
    print("Each person pays:", split_amount(value))

if __name__ == "__main__":
    main()