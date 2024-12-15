from Pizza import PizzaFactory
from Topping import CheeseDecorator, OlivesDecorator, MushroomsDecorator
from Manager import Manager
from pay import PaymentContext, PayPalPayment, CreditCardPayment


def main():
    inventory_manager = Manager()
    pizza_factory = PizzaFactory()

    print("Welcome to the Pizza Restaurant!")
    while True:
        print("Choose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => to exit")
        pizza_choice = input("Enter the number of your choice: ")
        if pizza_choice == '0':
            break

        pizza = None
        if pizza_choice == '1':
            pizza = pizza_factory.create_pizza("Margherita")
        elif pizza_choice == '2':
            pizza = pizza_factory.create_pizza("Pepperoni")

        if pizza is None:
            print("Invalid choice. Try again.")
            continue

    
        while True:
            print("\nAvailable toppings:")
            print("1. Cheese ($1.0)")
            print("2. Olives ($0.5)")
            print("3. Mushrooms ($0.7)")
            print("4. Finish order")
            topping_choice = input("Enter the number of your choice: ")

            if topping_choice == "1" and inventory_manager.check_and_decrement("Cheese"):
                pizza = CheeseDecorator(pizza)
            elif topping_choice == "2" and inventory_manager.check_and_decrement("Olives"):
                pizza = OlivesDecorator(pizza)
            elif topping_choice == "3" and inventory_manager.check_and_decrement("Mushrooms"):
                pizza = MushroomsDecorator(pizza)
            elif topping_choice == "4":
                break
            else:
                print("Topping unavailable or out of stock!")

        print("\nYour order:")
        print(f"Description: {pizza.Description()}")
        print(f"Total cost: ${pizza.Cost():.2f}")

        print("\nChoose payment method:")
        print("1. PayPal")
        print("2. Credit Card")
        payment_choice = input("Enter the number of your choice: ")

        if payment_choice == '1':
            payment_context = PaymentContext(PayPalPayment())
        elif payment_choice == '2':
            payment_context = PaymentContext(CreditCardPayment())
        else:
            print("Invalid payment method!")
            continue

        payment_context.execute_payment(pizza.Cost())

        print("\nRemaining Inventory:")
        print(inventory_manager.get_inventory())

if __name__ == "__main__":
    main()
