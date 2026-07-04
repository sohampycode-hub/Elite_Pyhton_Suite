import sqlite3
from datetime import datetime

DATABASE_FILE = "expenses.db"

def initialize_database():
    """Establishes connection and provisions relational schema tables if missing."""
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    category TEXT NOT NULL,
                    amount REAL NOT NULL,
                    description TEXT
                )
            """)
            conn.commit()
    except sqlite3.Error as e:
        print(f"[!] Database engine initialization failure: {e}")

def log_expense(category, amount, description):
    """Inserts records using parameters to protect against injection exploits."""
    if amount <= 0:
        print("\n[!] Validation Error: Financial amount must evaluate greater than zero.")
        return
        
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            # Parameters (?) separate execution code from volatile user-input values safely
            cursor.execute("""
                INSERT INTO expenses (date, category, amount, description)
                VALUES (?, ?, ?, ?)
            """, (current_date, category.strip().title(), amount, description.strip()))
            conn.commit()
        print(f"\n[+] Success: Recorded expense of INR {amount:.2f} under '{category}'.")
    except sqlite3.Error as e:
        print(f"\n[!] Database transaction abort: {e}")

def view_all_expenses():
    """Fetches full transaction logs out of the targeted storage node."""
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, date, category, amount, description FROM expenses ORDER BY id DESC")
            records = cursor.fetchall()
            
        if not records:
            print("\n--- Zero transaction history discovered in the ledger records. ---")
            return
            
        print("\n" + "=" * 65)
        print(f"{'ID':<4} {'Timestamp':<17} {'Category':<12} {'Amount':<10} {'Description':<20}")
        print("=" * 65)
        for row in records:
            print(f"{row[0]:<4} {row[1]:<17} {row[2]:<12} INR {row[3]:<6.2f} {row[4]:<20}")
        print("=" * 65)
    except sqlite3.Error as e:
        print(f"\n[!] Read operations halted: {e}")

def display_category_insights():
    """Leverages database engine aggregation functions to deliver budget distribution totals."""
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            # Database engine processes the calculations instantly
            cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
            insights = cursor.fetchall()
            
        if not insights:
            print("\n[INFO] Accumulate entries first to populate analysis indicators.")
            return
            
        print("\n" + "=" * 35)
        print("     EXPENDITURE RISK INSIGHTS     ")
        print("=" * 35)
        print(f"{'Category Allocation':<20} {'Total Allocated':<15}")
        print("-" * 35)
        for category, structural_sum in insights:
            print(f"{category:<20} INR {structural_sum:.2f}")
        print("=" * 35)
    except sqlite3.Error as e:
        print(f"\n[!] Analytical calculations failed: {e}")

def main():
    """Core menu dispatch sequence layer loop."""
    initialize_database()
    
    while True:
        print("\n::: RELATIONAL TRANSACTION LEDGER PROTOCOL :::")
        print("1. View Full Expense Ledger")
        print("2. Insert New Expense Entry")
        print("3. View Category Summary Insights")
        print("4. Terminate Tracking Systems")
        
        choice = input("\nSelect processing instruction (1-4): ").strip()
        
        if choice == "1":
            view_all_expenses()
        elif choice == "2":
            try:
                category = input("Enter asset budget category (e.g., Food, Travel, Books): ")
                amount = float(input("Enter actual monetary value: "))
                description = input("Enter contextual memo details: ")
                log_expense(category, amount, description)
            except ValueError:
                print("\n[!] Input Error: Numerical entries require explicit decimal or integer formatting.")
        elif choice == "3":
            display_category_insights()
        elif choice == "4":
            print("\nDatabase file handles detached. Disconnecting data core. Offline.")
            break
        else:
            print("\n[!] Invalid Selection index instruction configuration parameter.")

if __name__ == "__main__":
    main()
