import timeit


class Timer:
    """
    Simple class written by warevil
    """
    code: str
    name: str
    setup: str
    times: int

    def __init__(
        self,
        code: str = "pass",
        name: str = "Johan",
        setup: str = "pass",
        times: int = 1000,
    ):
        self.code = code
        self.name = name
        self.setup = setup
        self.times = times

    def log(
        self,
        code: str | None = None,
        name: str | None = None,
        setup: str | None = None,
        times: int | None = None,
    ):
        if code:
            self.code = code
        if name:
            self.name = name
        if setup:
            self.setup = setup
        if times:
            self.times = times

        print(self.name)
        print(
            timeit.timeit(
                setup=self.setup,
                stmt=self.code,
                number=self.times,
            ),
        )
