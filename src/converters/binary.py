from enum import Enum
from typing import Any


class BinaryConversions(Enum):
    DECIMAL = "decimal"
    HEXADECIMAL = "hexadecimal"
    OCTAL = "octal"


class BinaryConverter:
    def to(self, value: Any, convert_to: str) -> Any:
        match convert_to:
            case BinaryConversions.DECIMAL.name:
                return self._to_decimal(value)
            case BinaryConversions.HEXADECIMAL.name:
                return self._to_hexadecimal(value)
            case BinaryConversions.OCTAL.name:
                return self._to_octal(value)
            case _:
                raise ValueError("Unsupported conversion type")

    def _to_decimal(self, value: Any) -> Any:
        result: int = 0
        for index, char in enumerate(reversed(str(value))):
            result += int(char) * (2**index)

        return result

    def _to_hexadecimal(self, value: Any) -> Any:
        decimal_value = self._to_decimal(value)
        return hex(decimal_value).upper()

    def _to_octal(self, value: Any) -> Any:
        decimal_value = self._to_decimal(value)
        return oct(decimal_value).upper()
