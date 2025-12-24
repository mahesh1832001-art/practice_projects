class Movie:
    def __init__(self, movie_id, name, total_seats, price):
        self.movie_id = movie_id
        self.name = name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.price = price

    def has_seats(self, count):
        return self.available_seats >= count

    def book_seats(self, count):
        self.available_seats -= count

    def __str__(self):
        return (
            f"{self.movie_id}. {self.name} | "
            f"Seats: {self.available_seats}/{self.total_seats} | "
            f"Price: ₹{self.price}"
        )
