def main():
    print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"

   Prosperity comes in threes!
========================================

ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
Flying Carpet...............$119.99
Phoenix Feather...............14.99
Time Turner................$84.99
Enchanted Sword............$65.99
Potion of Luck.............$11.99
Crystal Ball..................$39.99
""")

    # Shopkeeper's rule: All purchases must be at least 3 items for good luck!
    # (Don't worry - the shopkeeper checks every order himself)
    name = input()
    item = float(input())
    quantity = int(input())

    # TODO: Calculate subtotal, tax, and total
    subtotal = item * quantity
    # Tax rate: 9.5%
    tax = 9.5 * 0.10
    total = subtotal + tax

    # TODO: Round total to 2 decimal places using round()

    total = round(subtotal + tax, 2)

    # TODO: Print receipt
    print("--------------------------")

    print(f"{name} x{quantity} @ ${item} each")

    print("--------------------------")
    # Print subtotal, tax, and total here
   print(f"Subtotal: ${subtotal}")
   print(f"Tax: ${tax}")
   print(f"Total: ${total}")


    print("\nThank you for shopping at\nthe Peculiar Emporium!")

    # The Peculiar Emporium


if __name__ == "__main__":
    main()
