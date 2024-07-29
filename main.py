import database as db
import utils as util

def track_expense():
    date = util.get_today_date()
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))

    db.insert_expense(date, description, amount)

def check_limits():
    month = util.get_current_month()
    total_expenses = db.get_total_expenses(util.get_today_date())
    monthly_limit = db.get_monthly_limit(month)

    if total_expenses > monthly_limit:
        message = f"Warning! Your total expenses for {month} have exceeded the limit.\nTotal: {total_expenses}\nLimit: {monthly_limit}"
        util.send_email("Expense Limit Exceeded", message, "recipient@example.com")
        print(message)
    else:
        print(f"Total expenses for {month}: {total_expenses}, within limit of {monthly_limit}")

def daily_report():
    date = util.get_today_date()
    expenses = db.get_expenses(date)
    report = f"Daily Expense Report for {date}:\n"
    report += "\n".join([f"{exp[1]}: {exp[2]} (Rs.)" for exp in expenses])
    
    total = db.get_total_expenses(date)
    report += f"\nTotal expenses for today: {total:.2f} (Rs.)"
    
    util.send_email(f"Daily Expense Report - {date}", report, "recipient@example.com")
    print(report)

def main():
    db.create_tables()

    while True:
        print("\nExpense Tracker")
        print("1. Track Expense")
        print("2. Check Limits")
        print("3. Generate Daily Report")
        print("4. Set Monthly Limit")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            track_expense()
        elif choice == '2':
            check_limits()
        elif choice == '3':
            daily_report()
        elif choice == '4':
            month = util.get_current_month()
            limit = float(input(f"Enter new monthly limit for {month}: "))
            db.set_monthly_limit(month, limit)
            print(f"Monthly limit for {month} updated to {limit}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
