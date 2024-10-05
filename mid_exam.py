class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)

    @classmethod
    def get_hall_list(cls):
        return cls.__hall_list


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().entry_hall(self)
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = {}
        self.__show_list = []

    def entry_show(self, show_id, movie_name, time):
        show_info = (show_id, movie_name, time)
        self.__show_list.append(show_info)
        seat_matrix = [["Free" for _ in range(
            self.__cols)] for _ in range(self.__rows)]
        self.__seats[show_id] = seat_matrix

    def book_seats(self, show_id, seat_list):
        if show_id not in self.__seats:
            print("Error: Invalid Show ID!")
            return

        show_seats = self.__seats[show_id]
        for row, col in seat_list:
            if row < 1 or row > self.__rows or col < 1 or col > self.__cols:
                print(f"Error: Invalid seat position ({row}, {col})!")
                continue

            if show_seats[row - 1][col - 1] == "Booked":
                print(f"Error: Seat ({row}, {col}) is already booked!")
            else:
                show_seats[row - 1][col - 1] = "Booked"
                print(f"Seat ({row}, {col}) successfully booked.")

    def view_show_list(self):
        if not self.__show_list:
            print("No shows available!")
        else:
            for show in self.__show_list:
                print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("Error: Invalid Show ID!")
            return

        show_seats = self.__seats[show_id]
        print(f"Available seats for Show ID {show_id}:")
        for row in show_seats:
            print(" ".join(row))


hall11 = Hall(5, 5, 'H1')

while True:
    print("\nOptions:")
    print("1. Add a show")
    print("2. View available shows")
    print("3. Book seats")
    print("4. View available seats for a show")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        show_id = input("Enter the show ID: ")
        movie_name = input("Enter the movie name: ")
        time = input("Enter the show time: ")
        hall11.entry_show(show_id, movie_name, time)
        print(f"Show '{movie_name}' added successfully.")

    elif choice == 2:
        hall11.view_show_list()

    elif choice == 3:
        show_id = input("Enter the show ID: ")
        num_seats = int(input("How many seats would you like to book? "))
        seat_list = []
        for _ in range(num_seats):
            row = int(input("Enter row number: "))
            col = int(input("Enter column number: "))
            seat_list.append((row, col))
        hall11.book_seats(show_id, seat_list)

    elif choice == 4:
        show_id = input("Enter the show ID: ")
        hall11.view_available_seats(show_id)

    elif choice == 5:
        print("Exiting the system.")
        break

    else:
        print("Invalid choice! Please try again.")
