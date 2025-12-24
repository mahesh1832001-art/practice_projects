class Booking:
    def __init__(self, booking_id, user, movie, seats):
        self.booking_id = booking_id
        self.user = user
        self.movie = movie
        self.seats = seats
        self.total_amount = seats * movie.price
        self.status = "CONFIRMED"

    def cancel(self):
        self.status = "CANCELLED"
        self.movie.available_seats += self.seats

    def __str__(self):
        return (
            f"Booking ID: {self.booking_id} | "
            f"Movie: {self.movie.name} | "
            f"Seats: {self.seats} | "
            f"Amount: ₹{self.total_amount} | "
            f"Status: {self.status}"
        )
