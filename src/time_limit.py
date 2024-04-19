import signal
from contextlib import contextmanager


class TimeoutException(Exception):
    pass


@contextmanager
def enforce_time_limit(seconds):
    def signal_handler(_signum, _frame):
        raise TimeoutException("Timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
