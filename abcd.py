# class Customer:
#     def __init__(self,customer_id, quantity, price):
#         self.customer_id = customer_id
#         self.quantity = quantity
#         self.price = price
#         self.discount = 0
    
#     def generate_bill(self):
#         price = self.quantity * self.price
#         self.discount_amount = price * self.discount
#         return price - self.discount_amount
    
# class SilverCustomer(Customer):
#     def __init__(self,id, quantity, price):
#         Customer.__init__(self,id,quantity,price)
#         self.discount = 10/100 

# class GoldCustomer(Customer):
#     def __init__(self,id,quantity,price):
#         Customer.__init__(self,id, quantity, price)
#         self.discount = 20/100


# customer_zero = Customer(2,10,100)
# print("Your bill amount is : ",customer_zero.generate_bill())

# customer_one = SilverCustomer(2,10,100)
# print("Your bill amount is : ",customer_one.generate_bill())

# customer_two = GoldCustomer(2,10,100)
# print("Your bill amount is : ",customer_two.generate_bill())





# class Customer:
#     def __init__(self, customer_id, quantity, price):
#         self.customer_id = customer_id
#         self.quantity = quantity
#         self.price = price
#         self.discount = 0

#     def generate_bill(self):
#         price = self.quantity * self.price
#         self.discount_amount = price * self.discount
#         return price - self.discount_amount


# class SilverCustomer(Customer):
#     def __init__(self, customer_id, quantity, price):
#         super().__init__(customer_id, quantity, price)
#         self.discount = 10 / 100


# class GoldCustomer(Customer):
#     def __init__(self, customer_id, quantity, price):
#         super().__init__(customer_id, quantity, price)
#         self.discount = 20 / 100



# while True:
#     print("Welcome to the Billing System")
#     customer_id = int(input("Enter your customer ID: "))
#     quantity = int(input("Enter the quantity of items: "))
#     price = float(input("Enter the price per item: "))

#     customer_type = input("Are you a Gold or Silver customer? (Enter 'gold' or 'silver'): ").lower()

#     if customer_type == 'gold':
#         customer = GoldCustomer(customer_id, quantity, price)
#     elif customer_type == 'silver':
#         customer = SilverCustomer(customer_id, quantity, price)
#     else:
#         print("Invalid customer type. Please try again.")
#         continue

#     bill_amount = customer.generate_bill()
#     print("Your bill amount is:", bill_amount)
    
#     choice = input("Do you want to continue? (yes/no): ").lower()
#     if choice != 'yes':
#         print("Thank you for using the Billing System. Goodbye!")
#         break





class Customer:
    def __init__(self, customer_id, quantity, price):
        self.customer_id = customer_id
        self.quantity = quantity
        self.price = price
        self.discount = 0

    def generate_bill(self):
        price = self.quantity * self.price
        self.discount_amount = price * self.discount
        return price - self.discount_amount


class SilverCustomer(Customer):
    def __init__(self, customer_id, quantity, price):
        super().__init__(customer_id, quantity, price)
        self.discount = 10 / 100


class GoldCustomer(Customer):
    def __init__(self, customer_id, quantity, price):
        super().__init__(customer_id, quantity, price)
        self.discount = 20 / 100


def get_customer_type():
    while True:
        print("Choose your customer type:")
        print("1. Gold")
        print("2. Silver")
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            return 'gold'
        elif choice == '2':
            return 'silver'
        else:
            print("Invalid choice. Please enter 1 or 2.")



while True:
    print("Welcome to the Billing System")
    customer_id = int(input("Enter your customer ID: "))
    quantity = int(input("Enter the quantity of items: "))
    price = float(input("Enter the price per item: "))

    customer_type = get_customer_type()

    if customer_type == 'gold':
        customer = GoldCustomer(customer_id, quantity, price)
    elif customer_type == 'silver':
        customer = SilverCustomer(customer_id, quantity, price)

    bill_amount = customer.generate_bill()
    print("Your bill amount is:", bill_amount)
    
    while True:
        print("Do you want to continue?")
        print("1. Yes")
        print("2. No")
        choice = int(input("Enter your choice (1 or 2) : "))
        if choice == 1:
            break
        elif choice == 2:
            print("Thank you for using the Billing System. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

