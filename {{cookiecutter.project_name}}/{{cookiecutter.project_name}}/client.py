from .module1.entrypoint1 import X
from .module2.entrypoint2 import Y


class Client:
    def func_1(self, arg1: int, arg2: list[str]) -> bool:
        """Demo function 1

        Types are automatically inferred from type hints when sphinx
        renders this inline documentation. Google style inline docs are used.

        Args:
            arg1: Argument 1
            arg2: Argument 2

        Returns:
            Some return value
        """
        x = X()
        succes = x.do_something()
        return succes

    def func_2(self, arg1: int = None, arg2: str = "foo") -> bool:
        """Demo function 2

        This is a demo of all possible inline documentation components
        for a function.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            arg1: Description of arg1. Defaults to None.
            arg2: Description of arg2. Defaults to "foo".

        Returns:
            Some return value

        Raises:
            AttributeError: The ``Raises`` section is a list of all exceptions
                that are relevant to the interface.
            ValueError: If `param2` is equal to `param1`.

        Examples:
            Examples should be written in doctest format, and should illustrate how
            to use the function.

            >>> print([i for i in example_generator(4)])
            [0, 1, 2, 3]
        """
        y = Y()
        succes = y.do_something()
        return succes