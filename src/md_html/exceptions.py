"""Custom exceptions for the package."""


class HTMLParseError(Exception):
    """Exception raised during the parsing of markdown text.

    Attributes:
        message -- explanation of the error

    """

    def __init__(self, message: str) -> None:
        """Instantiate the HTMLParseError exception."""
        self.message = message
        super().__init__(self.message)


class MDParseError(Exception):
    """Exception raised during the parsing of markdown text.

    Attributes:
        message -- explanation of the error

    """

    def __init__(self, message: str) -> None:
        """Instantiate MDParseError exception."""
        self.message = message
        super().__init__(self.message)
