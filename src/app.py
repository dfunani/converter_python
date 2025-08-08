import sys
import tkinter
from typing import cast
from inquirer import List, prompt, Text
from factory import ConverterFactory, Converters
from gui.window import AppWindow
from PyQt6.QtWidgets import QApplication, QWidget, QLabel


def main():
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    # window = Window()
    main()
    # print("Starting the application...")
    # converter = [
    #     List(
    #         "converter",
    #         message="Choose a converter",
    #         choices=[item.name for item in Converters],
    #         default=Converters.BINARY.name,
    #         carousel=True,
    #     )
    # ]
    # answers = cast(dict[str, str], prompt(converter))
    # print(f"Converter Selected: {answers['converter']}")

    # value = [
    #     Text(
    #         "value",
    #         message="Enter the value to convert",
    #         validate=lambda _, val: Converters[answers["converter"]].value[0].match(val)
    #         is not None,
    #     )
    # ]
    # value_answer = cast(dict[str, str], prompt(value))
    # print(f"Value Entered: {value_answer['value']}")
    # converter_instance = ConverterFactory.get_converter(answers["converter"])

    # convert_to = [
    #     List(
    #         "convert_to",
    #         message="Convert to",
    #         choices=[item.name for item in Converters[answers["converter"]].value[1]],
    #         carousel=True,
    #     )
    # ]
    # convert_to_answer = cast(dict[str, str], prompt(convert_to))
    # print(f"Conversion Type Selected: {convert_to_answer['convert_to']}")
    # result = converter_instance.to(value_answer["value"], convert_to_answer["convert_to"])
    # print(f"Conversion Result: {result}")
