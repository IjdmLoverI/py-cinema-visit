from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_objects = [Customer(customer["name"], customer["food"])
                        for customer in customers]
    cinema_hall = CinemaHall(hall_number)
    cleaner_stuff = Cleaner(cleaner)
    for customer in customer_objects:
        CinemaBar.sell_product(customer.food, customer)
    cinema_hall.movie_session(movie, customer_objects, cleaner_stuff)
