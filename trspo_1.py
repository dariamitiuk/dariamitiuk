import threading


def sum(a, b):
    print("Sum: {}".format(a + b))


def product(a, b):
    print("Product: {}".format(a * b))


if __name__ == "__main__":
    t1 = threading.Thread(target=sum, args=(10, 15))
    t2 = threading.Thread(target=product, args=(10, 15))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Threads are completed!")