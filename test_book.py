from book_reservation import BookReservationSystem

def test_reserve_book():
    system=BookReservationSystem(
        books={"B1":2},
        students={"S1"}
    )
    assert system.reserve_book("S1","B1")==True

def test_check_availability():
    system=BookReservationSystem(
        books={"B1":2},
        students={"S1"}
    )
    system.reserve_book("S1","B1")
    assert system.available_copies("B1")==1

def test_duplicate_reservation():
    system=BookReservationSystem(
        books={"B1":2},
        students={"S1"}
    )
    system.reserve_book("S1","B1")
    assert system.reserve_book("S1","B1")==False

def test_cancel_reservation():
    system=BookReservationSystem(
        books={"B1":2},
        students={"S1"}
    )
    system.reserve_book("S1","B1")
    system.cancel_reservation("S1","B1")
    assert system.available_copies("B1")==2