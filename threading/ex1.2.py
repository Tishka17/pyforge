from threading import Thread
from time import sleep


def foo(name, delay):
    print("begin from", name)
    sleep(delay)
    print("end from", name)
    return f"{name} result"


# start with params

# Thread(
#     target=foo, args=("threaded_foo", 0.1),
# ).start()

# Thread(
#     target=foo, args=("threaded_foo", ), kwargs={"delay": 0.1}
# ).start()

# Thread(
#     target=foo, args=("threaded_foo", ), kwargs={"delay": 1}
# ).start()

# daemon thread - is not waited when app finishes
Thread(
    target=foo, args=("daemon_foo", 1),
    daemon=True,
).start()
