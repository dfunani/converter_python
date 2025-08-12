from enum import Enum
from typing import Any


class DecimalConversions(Enum):
    BINARY = "binary"
    HEXADECIMAL = "hexadecimal"
    OCTAL = "octal"


class DecimalConverter:
    def to(self, value: Any, convert_to: str) -> Any:
        match convert_to:
            case DecimalConversions.BINARY.name:
                return self._to_binary(value)
            case DecimalConversions.HEXADECIMAL.name:
                return self._to_hexadecimal(value)
            case DecimalConversions.OCTAL.name:
                return self._to_octal(value)
            case _:
                raise ValueError("Unsupported conversion type")

    def _to_binary(self, value: Any) -> Any:
        return bin(int(value)).replace("0b", "").upper()

    def _to_hexadecimal(self, value: Any) -> Any:
        return hex(int(value)).upper()

    def _to_octal(self, value: Any) -> Any:
        return oct(int(value)).upper()
