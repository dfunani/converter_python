from enum import Enum
from typing import Any


class HexadecimalConversions(Enum):
    DECIMAL = "decimal"
    BINARY = "binary"
    OCTAL = "octal"


class HexadecimalConverter:
    def to(self, value: Any, convert_to: str) -> Any:
        match convert_to:
            case HexadecimalConversions.DECIMAL.name:
                return self._to_decimal(value)
            case HexadecimalConversions.BINARY.name:
                return self._to_binary(value)
            case HexadecimalConversions.OCTAL.name:
                return self._to_octal(value)
            case _:
                raise ValueError("Unsupported conversion type")

    def _to_decimal(self, value: Any) -> Any:
        return int(value, 16)

    def _to_binary(self, value: Any) -> Any:
        return bin(self._to_decimal(value)).replace("0b", "").upper()

    def _to_octal(self, value: Any) -> Any:
        return oct(self._to_decimal(value)).upper()
