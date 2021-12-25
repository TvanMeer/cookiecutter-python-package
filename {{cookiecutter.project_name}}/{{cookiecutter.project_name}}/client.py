from .module1.entrypoint1 import X
from .module2.entrypoint2 import Y


class Client:
    """Example of an inline documented class.

    This class contains client exposed functions that are part of the API.
    These functions use uncoupled implementation code in the ``module1`` and
    ``module2`` modules.

    Properties created with the ``@property`` decorator should be documented
    in the property's getter method. This docstring is used for both the getter
    and setter.

    Args:
        arg1 (int): Some argument passed to the `__init__` function.

    Attributes:
        attr1 (int): Some attribute
        attr2 (str): Another attribute
    """

    def __init__(self, arg1: int) -> None:
        self.attr1 = arg1
        self.attr2 = "foo"

    def func_1(self, arg1: int, arg2: list[str]) -> bool:
        """Demo function 1

        Types are automatically inferred from type hints when sphinx
        renders this inline documentation. Google style inline docs are used.

        Args:
            arg1 (int): Argument 1
            arg2 (list[str]): Argument 2

        Returns:
            bool: Some return value
        """
        x = X()
        succes = x.do_something()
        return succes

    def func_2(self, arg1: int, arg2: str = "foo") -> bool:
        """Demo function 2

        This is a demo of all possible inline documentation components
        for a function.

        Args:
            arg1 (int): Description of arg1.

        Keyword Args:
            arg2 (str, optional): Description of arg2. Defaults to "foo".

        Returns:
            bool: Some return value

        Raises:
            AttributeError: The ``Raises`` section is a list of all exceptions
                that are relevant to the interface.
            ValueError: If `param2` is equal to `param1`.

        Warns:
            UserWarning: A sample warning. See https://docs.python.org/3/library/warnings.html

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Hint:
            Some hint message.

        Tip:
            Some tip message.

        Important:
            Some important message.

        Caution:
            Some caution message.

        Warning:
            Some warning message.

        Attention:
            Some attention message.

        Danger:
            Some danger message.

        Error:
            Some error message.

        References:
            .. [1] `A link <https://github.com/TvanMeer/cookiecutter-python-package>`_, \
            Some description of an external source that is an API reference.
            

        See Also:
            func_1: The related `func_1`
            

        Examples:
            Examples should be written in doctest format, and should illustrate how
            to use the function.

            >>> print([i for i in example_generator(4)])
            [0, 1, 2, 3]

        """
        y = Y()
        succes = y.do_something()
        return succes