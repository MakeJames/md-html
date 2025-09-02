"""Content utility to parse html elements."""

from dataclasses import dataclass
from typing import Any, Generic, Protocol, TypeVar

from md_html.elements.base_element import HTMLBaseClass

HTMLElement = TypeVar("HTMLElement", bound=HTMLBaseClass, covariant=True)


class HTMLFactory(Protocol[HTMLElement]):
    """Factory class for content blocks."""

    def __call__(self, *args: Any, **kwargs: Any) -> HTMLElement:
        """Return the html element class."""
        ...


@dataclass
class Content(Generic[HTMLElement]):
    """Content dataclass."""

    kind: HTMLFactory[HTMLElement]
    content: str

    def build(self, *args: tuple[Any, ...], **kwargs: dict[str, Any] ) -> HTMLElement:
        """Build the content."""
        return self.kind(self.content, *args, **kwargs)
