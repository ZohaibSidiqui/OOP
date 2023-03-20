
class Product:
    def __init__(self):
        self.code = self.get_product_code()
        self.name = self.get_product_name()
        self.sale_price = self.get_product_sale_price()
        self.manufacture_cost = self.get_product_manufacture_cost()
        self.stock_level = self.get_stock_level()
        self.monthly_units_manufactured = self.get_estimated_monthly_units_manufactured()
        self.monthly_checkup_list = [] #The "[]" after monthly_checkup_list in the __init__ method creates an empty list to store the monthly checkup data. This is necessary because the simulateMonthlyProductionAndSale method appends a tuple containing the month number, the number of units manufactured, the number of units sold, and the stock level to this list for each simulated month. If the list is not initialized as empty, the append method would raise an attribute error. By initializing the list as empty, we can add the simulated data to the list as we go.

    def get_product_code(self):
        while 1==1:
            try: # try just tells the code to accept this code and try it
                code = int(input("Enter the product code (an integer from 100 to 1000): "))
                if code < 100 or code > 1000:
                    raise ValueError #ValueError basically just tells the code to put an error
                return code
            except ValueError: # this is saying if the user input a wrong answer print this
                print("Invalid input. Please enter an integer between 100 and 1000.")

    def get_product_name(self):
        return input("Enter the product name: ")

    def get_product_sale_price(self):
        while 1==1:
            try:
                sale_price = float(input("Enter the product sale price (a real number greater than zero): "))
                if sale_price <= 0:
                    raise ValueError
                return sale_price
            except ValueError:
                print("Invalid input. Please enter a real number greater than zero.")

    def get_product_manufacture_cost(self):
        while 1==1:
            try:
                manufacture_cost = float(input("Enter the product manufacture cost (a real number greater than zero): "))
                if manufacture_cost <= 0:
                    raise ValueError
                return manufacture_cost
            except ValueError:
                print("Invalid input. Please enter a real number greater than zero.")

    def get_stock_level(self):
        while 1==1:
            try:
                stock_level = int(input("Enter the stock level (an integer number greater than 0): "))
                if stock_level <= 0:
                    raise ValueError
                return stock_level
            except ValueError:
                print("Invalid input. Please enter an integer greater than 0.")

    def get_estimated_monthly_units_manufactured(self):
        while 1==1:
            try:
                monthly_units_manufactured = int(input("Enter the estimated monthly units manufactured (an integer greater than or equal to 0): "))
                if monthly_units_manufactured < 0:
                    raise ValueError
                return monthly_units_manufactured
            except ValueError:
                print("Invalid input. Please enter an integer greater than or equal to 0.")

    def simulateMonthlyProductionAndSale(self, month):
        import random

        units_sold = random.randint(self.monthly_units_manufactured +10, self.monthly_units_manufactured + 10)
        self.stock_level -= units_sold
        units_manufactured = self.monthly_units_manufactured
        self.stock_level += units_manufactured
        self.monthly_checkup_list.append((month, units_manufactured, units_sold, self.stock_level))

    def printMonthlyCheckupList(self):
        print("Monthly Check-up List:")
        for month, units_manufactured, units_sold, stock_level in self.monthly_checkup_list:
            print(f"Month {month}: Manufactured {units_manufactured} units, Sold {units_sold} units, Stock Level: {stock_level} units")

    def runSimulation(self):
        for month in range(1, 13):
            self.simulateMonthlyProductionAndSale(month)
        self.printMonthlyCheckupList()


product = Product()
product.runSimulation()

