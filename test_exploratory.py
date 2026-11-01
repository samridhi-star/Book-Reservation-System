from book_reservation import BookReservationSystem


# 1. Reserve the last available copy
def test_last_available_copy():
    system = BookReservationSystem(
        books={"B1": 1},
        students={"S1", "S2"}
    )

    assert system.reserve_book("S1", "B1") == True
    assert system.available_copies("B1") == 0
    assert system.reserve_book("S2", "B1") == False


# 2. Reserve an unavailable book
def test_unavailable_book():
    system = BookReservationSystem(
        books={"B1": 0},
        students={"S1"}
    )

    assert system.reserve_book("S1", "B1") == False


# 3. Duplicate reservation
def test_duplicate_reservation():
    system = BookReservationSystem(
        books={"B1": 2},
        students={"S1"}
    )

    system.reserve_book("S1", "B1")

    assert system.reserve_book("S1", "B1") == False


# 4. Cancel reservation twice
def test_cancel_twice():
    system = BookReservationSystem(
        books={"B1": 2},
        students={"S1"}
    )

    system.reserve_book("S1", "B1")
    assert system.cancel_reservation("S1", "B1") == True
    assert system.cancel_reservation("S1", "B1") == False


# 5. Invalid student ID
def test_invalid_student():
    system = BookReservationSystem(
        books={"B1": 2},
        students={"S1"}
    )

    assert system.reserve_book("S2", "B1") == False