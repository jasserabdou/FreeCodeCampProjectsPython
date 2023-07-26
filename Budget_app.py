class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{'*' * 15}{self.name}{'*' * 15}\n"
        items = "".join(
            [f"{item['description'][:23]:<23}{item['amount']:>7.2f}\n" for item in self.ledger]
        )
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    total_withdrawals = sum(category.get_balance() for category in categories)
    percentages = [(category.get_balance() / total_withdrawals)
                   * 100 for category in categories]

    chart = "Percentage spent by category\n"

    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"

    return chart


if __name__ == "__main__":
    food = Category("Food")
    clothing = Category("Clothing")
    entertainment = Category("Entertainment")

    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food")
    clothing.deposit(500, "initial deposit")
    clothing.withdraw(50, "new clothes")
    entertainment.deposit(200, "initial deposit")
    entertainment.withdraw(15, "movie")

    print(food)
    print(clothing)
    print(entertainment)

    print(create_spend_chart([food, clothing, entertainment]))
