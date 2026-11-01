class BookReservationSystem:

    def __init__(self,books,students):
        self.books=books
        self.students=students
        self.reservations=set()


    def reserve_book(self,student_id,book_id):
        reservation=(student_id,book_id)

        if student_id not in self.students:
            return False

        if book_id not in self.books:
            return False

        if self.books[book_id]<=0:
            return False
        if reservation in self.reservations:
            return False
        
        self.books[book_id]-=1
        self.reservations.add(reservation)

        return True

    def available_copies(self,book_id):
        if book_id not in self.books:
            return False
        
        return self.books[book_id]

    def cancel_reservation(self,student_id,book_id):
        reservation=(student_id,book_id)

        if reservation not in self.reservations:
            return False

        self.reservations.remove(reservation)

        self.books[book_id]+=1
        return True