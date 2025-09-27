from datetime import datetime, timedelta
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date  # Return it for later use
def calculate_future_date(current_date):
    # Ask the user for the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date
    future_date = current_date + timedelta(days=days_to_add)
    # Format and print the future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))
def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()
