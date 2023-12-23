def fun():
    print("start")
    # here due to yield this function behaves as generator which when called does not execute loc near yield keyword
    yield 10
    print("end")
fun()
