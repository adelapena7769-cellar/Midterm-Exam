FILE_NAME = "sales_log.txt"

def display_menu():
    print('========================================')
    print('    SALES RECORD MANAGEMENT SYSTEM')
    print('========================================')
    print('1. Add Sale Record')
    print('2. View All Records & Summary Statistics')
    print('3. Clear All Sales Data')
    print('4. Exit System')
    print('========================================')

def main():
    while True:
        display_menu()

        option = input("Select an option (1-4): ")

        if option == "1":
            add_sales_record()

        elif option == "2":
            view_records()

        elif option == "3":
            clear_sales_data()

        elif option == "4":
            print(
                "Thank you for using the Sales Record Management System."
            )
            break

        else:
            print("Invalid option. Please select 1, 2, 3, or 4.")

        print()


if __name__ == "__main__":
    main()

def add_sales_record():
    try:
        item_name = input('Item Name: ')
        quantity_sold = int(input('Quantity Sold: '))
        price_per_unit = float(input('Price Per Unit: '))

        total_amount = quantity_sold * price_per_unit

        print(f'Item Name: {item_name}'
              f'\nQuantity Sold: {quantity_sold}'
              f'\nPrice Per Unit: {price_per_unit}'
              f'\nTotal Amount: {total_amount}')

        with open(FILE_NAME, "a") as file:
            file.write(
                f"{item_name},{quantity_sold},"
                f"{price_per_unit:.2f},{total_amount:.2f}\n"
            )
        print("Sale record saved successfully.")

    except ValueError:
        print("Invalid input. Quantity must be an integer and " "price must be a number.")

def clear_sales_data():
    try:
        with open(FILE_NAME, "w") as file:
            file.write("")

        print("All records cleared. No records remaining.")

    except:
        print("Error: Unable to clear the sales data.")
