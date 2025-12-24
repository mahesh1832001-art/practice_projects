from user import User
from movie import Movie
from booking import Booking

class BookingService:
    def __init__(self):
        self.users = []
        self.movies = []
        self.bookings = []
        self.current_user = None
        self.booking_counter = 1

        self.movies.append(Movie(1, "Avengers", 50, 200))
        self.movies.append(Movie(2, "Interstellar", 30, 250))
        self.movies.append(Movie(3, "Inception", 40, 220))

    # ---------- USER ----------
    def register(self, email, name, password):
        for user in self.users:
            if user.email == email:
                print("Email already exists")
                return
        self.users.append(User(email, name, password))
        print("Registration successful")

    def login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                self.current_user = user
                print(f"Welcome {user.name}")
                return True
        print("Invalid credentials")
        return False

    def logout(self):
        self.current_user = None
        print("Logged out successfully")

    def list_movies(self):
        print("\nAvailable Movies:")
        for movie in self.movies:
            print(movie)

    def book_ticket(self, movie_id, seats):
        if not self.current_user:
            print("Login required")
            return

        for movie in self.movies:
            if movie.movie_id == movie_id:
                if not movie.has_seats(seats):
                    print("Not enough seats available")
                    return

                movie.book_seats(seats)
                booking = Booking(
                    self.booking_counter,
                    self.current_user,
                    movie,
                    seats
                )
                self.booking_counter += 1
                self.bookings.append(booking)
                print("Booking successful")
                print(booking)
                return

        print("Invalid movie ID")

    def my_bookings(self):
        print("\nMy Bookings:")
        found = False
        for booking in self.bookings:
            if booking.user == self.current_user:
                print(booking)
                found = True
        if not found:
            print("No bookings found")

    def cancel_booking(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id and booking.user == self.current_user:
                if booking.status == "CANCELLED":
                    print("Booking already cancelled")
                    return
                booking.cancel()
                print("Booking cancelled successfully")
                return
        print("Invalid booking ID")
