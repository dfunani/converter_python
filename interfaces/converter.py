from abc import ABC, abstractmethod
from typing import Any


class IConverter(ABC):
    @abstractmethod
    def to(self, value: Any, convert_to: str) -> Any:
        pass