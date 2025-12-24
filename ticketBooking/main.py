from booking_service import BookingService

service = BookingService()

def main_menu():
    print("\n1. Login\n2. Register\n3. Exit")
    return input("Choose: ")

def user_menu():
    print("\n1. View Movies\n2. Book Ticket\n3. My Bookings\n4. Cancel Booking\n5. Logout")
    return input("Choose: ")

while True:
    choice = main_menu()

    if choice == "1":
        if service.login(
            input("Email: "),
            input("Password: ")
        ):
            while True:
                user_choice = user_menu()

                if user_choice == "1":
                    service.list_movies()

                elif user_choice == "2":
                    service.book_ticket(
                        int(input("Movie ID: ")),
                        int(input("Seats: "))
                    )

                elif user_choice == "3":
                    service.my_bookings()

                elif user_choice == "4":
                    service.cancel_booking(
                        int(input("Booking ID: "))
                    )

                elif user_choice == "5":
                    service.logout()
                    break

    elif choice == "2":
        service.register(
            input("Email: "),
            input("Name: "),
            input("Password: ")
        )

    else:
        print("Thank you!")
        break
