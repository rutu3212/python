# assignment
# min 100 line any super market or movie ticket same logic are apply

def avengers():
    print("Avengers ticket is Rs. 300 per person")

def interstellar():
    print("Interstellar ticket is Rs. 350 per person")

def inception():
    print("Inception ticket is Rs. 400 per person")

def avatar():
    print("Avatar ticket is Rs. 450 per person")

def titanic():
    print("Titanic ticket is Rs. 250 per person")

def jurassic_park():
    print("Jurassic Park ticket is Rs. 280 per person")

def the_dark_knight():
    print("The Dark Knight ticket is Rs. 320 per person")

def toy_story():
    print("Toy Story ticket is Rs. 200 per person")

def spider_man():
    print("Spider-Man ticket is Rs. 370 per person")

def book_ticket(movie, price):
    tickets = int(input("Enter number of tickets: "))
    total = tickets * price
    
    # Apply discount if more than 3 tickets
    if tickets > 3:
        discount = total * 0.1  # 10% discount
        total -= discount
        print(f"Discount Applied: Rs. {discount}")
    
    print(f"Total amount for {tickets} tickets: Rs. {total}")
    confirm_booking(movie, tickets, total)

def confirm_booking(movie, tickets, total):
    confirm = input(f"Confirm booking for {tickets} ticket(s) for {movie} (Yes/No)? ").lower()
    if confirm == 'yes':
        print(f"Booking confirmed! Enjoy {movie}.")
    else:
        print("Booking canceled.")

def display_movies():
    print("\n*** Welcome to Movie Ticket Booking ***")
    print("1. Avengers")
    print("2. Interstellar")
    print("3. Inception")
    print("4. Avatar")
    print("5. Titanic")
    print("6. Jurassic Park")
    print("7. The Dark Knight")
    print("8. Toy Story")
    print("9. Spider-Man")
    print("0. Exit")

def main():
    while True:
        display_movies()
        choose_number = int(input("Enter your choice (or 0 to exit): "))
        
        if choose_number == 1:
            avengers()
            book_ticket("Avengers", 300)
        elif choose_number == 2:
            interstellar()
            book_ticket("Interstellar", 350)
        elif choose_number == 3:
            inception()
            book_ticket("Inception", 400)
        elif choose_number == 4:
            avatar()
            book_ticket("Avatar", 450)
        elif choose_number == 5:
            titanic()
            book_ticket("Titanic", 250)
        elif choose_number == 6:
            jurassic_park()
            book_ticket("Jurassic Park", 280)
        elif choose_number == 7:
            the_dark_knight()
            book_ticket("The Dark Knight", 320)
        elif choose_number == 8:
            toy_story()
            book_ticket("Toy Story", 200)
        elif choose_number == 9:
            spider_man()
            book_ticket("Spider-Man", 370)
        elif choose_number == 0:
            print("Thank you for using Movie Ticket Booking! Have a great day.")
            break
        else:
            print("Invalid choice! Please select a valid option.")
        
        another = input("Do you want to book another ticket? (Yes/No): ").lower()
        if another != 'yes':
            print("Thank you for using our service!")
            break

if __name__ == "__main__":
    main()
