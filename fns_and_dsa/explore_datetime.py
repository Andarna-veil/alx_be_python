from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays and returns the current date and time.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date  # Return the current date object

def calculate_future_date(current_date):
    """
    Prompts the user for number of days to add and prints the future date.
    """
    # Prompt for user input
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)

