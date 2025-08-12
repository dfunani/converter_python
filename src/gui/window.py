from PyQt6.QtWidgets import (
    QMainWindow,
    QFrame,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QWidget,
)
from PyQt6.QtCore import Qt
from factory import ConverterFactory, Converters


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Converter App")
        self.setGeometry(100, 100, 800, 600,)
        self.setStyleSheet(
            "margin: 0;font-family: 'Segoe UI', Arial, sans-serif;background: linear-gradient(120deg, #f8fafc 0%, #e0e7ff 100%); width: 100px; height: 100px;"
        )
        # Remove fixed size to allow resizing
        # self.setFixedSize(800, 600)

        # Main widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Create a frame for the navbar
        self.navbar = QFrame()
        self.navbar.setObjectName("navbar")
        self.navbar.setFixedHeight(72)
        self.navbar_layout = QHBoxLayout(self.navbar)
        self.navbar_layout.setContentsMargins(32, 0, 32, 0)
        self.navbar_layout.setSpacing(0)

        # Brand label
        self.title_label = QLabel("Converter App")
        self.title_label.setObjectName("navbarBrand")
        self.navbar_layout.addWidget(self.title_label)

        # Tabs
        self.tabs_frame = QFrame()
        self.tabs_layout = QHBoxLayout(self.tabs_frame)
        self.tabs_layout.setContentsMargins(0, 0, 0, 0)
        self.tabs_layout.setSpacing(0)

        self.tab_converters = QPushButton("Converters")
        self.tab_converters.setObjectName("tabConverters")
        self.tab_converters.setCheckable(True)
        self.tab_converters.setChecked(True)
        self.tab_json = QPushButton("JSON Viewer")
        self.tab_json.setObjectName("tabJson")
        self.tab_json.setCheckable(True)

        self.tabs_layout.addWidget(self.tab_converters)
        self.tabs_layout.addWidget(self.tab_json)
        self.navbar_layout.addWidget(self.tabs_frame, alignment=Qt.AlignmentFlag.AlignRight)

        self.main_layout.addWidget(self.navbar)

        # Centered container for main content
        from PyQt6.QtWidgets import QStackedWidget
        self.center_container = QWidget()
        self.center_layout = QVBoxLayout(self.center_container)
        self.center_layout.setContentsMargins(0, 0, 0, 0)
        self.center_layout.setSpacing(0)
        self.center_layout.addStretch(1)
        self.stacked = QStackedWidget()
        self.stacked.setObjectName("centeredStacked")
        self.center_layout.addWidget(self.stacked, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.center_layout.addStretch(1)
        self.main_layout.addWidget(self.center_container, stretch=1)

        # --- Converters Page ---
        self.page_converters = QWidget()
        self.page_converters.setObjectName("converterSection")
        self.page_converters_layout = QVBoxLayout(self.page_converters)
        self.page_converters_layout.setContentsMargins(60, 60, 60, 60)
        self.page_converters_layout.setSpacing(24)
        self.page_converters_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.converter_title = QLabel("Select Converter")
        self.converter_title.setObjectName("sectionTitle")
        self.page_converters_layout.addWidget(self.converter_title)

        from PyQt6.QtWidgets import QComboBox, QLineEdit
        self.converter_select = QComboBox()
        for converter in Converters:
            self.converter_select.addItem(converter.name.title(), converter)
        self.converter_select.setObjectName("converterSelect")
        self.page_converters_layout.addWidget(self.converter_select)

        # Conversion form
        self.form_frame = QFrame()
        self.form_layout = QVBoxLayout(self.form_frame)
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.form_layout.setSpacing(12)

        self.label_convert_to = QLabel("Convert To:")
        self.label_convert_to.setObjectName("formLabel")
        self.form_layout.addWidget(self.label_convert_to)

        self.convert_to_select = QComboBox()
        self.convert_to_select.setObjectName("convertToSelect")
        self.form_layout.addWidget(self.convert_to_select)

        # Populate convert_to_select based on initial converter
        def update_convert_to_options():
            self.convert_to_select.clear()
            converter = self.converter_select.currentData()
            if converter is not None:
                print(converter)
                for opt in converter.value[1]:
                    self.convert_to_select.addItem(opt.name.title(), opt)

        # Initial population
        update_convert_to_options()
        # Update on converter change
        self.converter_select.currentIndexChanged.connect(update_convert_to_options)

        self.input_value = QLineEdit()
        self.input_value.setPlaceholderText("Enter value...")
        self.input_value.setObjectName("inputValue")
        self.form_layout.addWidget(self.input_value)

        def update_input_value(text: str):
            # update the text in result box
            converter = self.converter_select.currentData()
            if converter is not None:
                conversion_type = self.convert_to_select.currentData()
                if conversion_type is not None:
                    text = ConverterFactory.get_converter(converter.name).to(text, conversion_type.name)
                    self.result_box.setText(str(text))

        self.convert_btn = QPushButton("Convert")
        self.convert_btn.setObjectName("convertBtn")
        self.form_layout.addWidget(self.convert_btn)

        self.page_converters_layout.addWidget(self.form_frame)
        self.convert_btn.clicked.connect(lambda: update_input_value(self.input_value.text()))
        self.result_box = QLabel("Converted value will appear here.")
        self.result_box.setObjectName("resultBox")
        self.result_box.setMinimumHeight(32)
        self.page_converters_layout.addWidget(self.result_box)

        self.stacked.addWidget(self.page_converters)

        # --- JSON Viewer Page ---
        self.page_json = QWidget()
        self.page_json.setObjectName("jsonSection")
        self.page_json_layout = QVBoxLayout(self.page_json)

        self.page_json_layout.setSpacing(24)
        self.page_json_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.page_json_layout.setContentsMargins(60, 60, 60, 60)

        self.json_title = QLabel("JSON Viewer")
        self.json_title.setObjectName("sectionTitle")
        self.page_json_layout.addWidget(self.json_title)

        from PyQt6.QtWidgets import QTextEdit
        self.json_input = QTextEdit()
        self.json_input.setPlaceholderText("Paste your JSON here...")
        self.json_input.setObjectName("jsonInput")
        # self.json_input.setFixedHeight(160)
        self.page_json_layout.addWidget(self.json_input)

        self.json_output = QLabel("Formatted JSON will appear here.")
        self.json_output.setObjectName("resultBox")
        self.json_output.setMinimumHeight(48)
        self.json_output.setWordWrap(True)
        self.page_json_layout.addWidget(self.json_output)

        self.stacked.addWidget(self.page_json)

        # Tab switching logic
        def switch_to_converters():
            self.tab_converters.setChecked(True)
            self.tab_json.setChecked(False)
            self.stacked.setCurrentWidget(self.page_converters)
        def switch_to_json():
            self.tab_converters.setChecked(False)
            self.tab_json.setChecked(True)
            self.stacked.setCurrentWidget(self.page_json)
        self.tab_converters.clicked.connect(switch_to_converters)
        self.tab_json.clicked.connect(switch_to_json)

        # JSON formatting logic
        def update_json_output():
            import json
            text = self.json_input.toPlainText()
            try:
                parsed = json.loads(text)
                formatted = json.dumps(parsed, indent=2)
                self.json_output.setText(f'<pre style="color:#374151;">{formatted}</pre>')
            except Exception:
                if text.strip():
                    self.json_output.setText('<span style="color:#ef4444;">Invalid JSON</span>')
                else:
                    self.json_output.setText('Formatted JSON will appear here.')
        self.json_input.textChanged.connect(update_json_output)

        # --- Styling ---
        self.setStyleSheet('''
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #f8fafc, stop:1 #e0e7ff);
            }
            #navbar {
                background: #6366f1;
                color: #fff;
                box-shadow: 0 2px 8px rgba(99,102,241,0.1);
            }
            #navbarBrand {
                font-size: 24px;
                font-weight: bold;
                letter-spacing: 1px;
            }
            #tabConverters, #tabJson {
                background: transparent;
                color: #fff;
                border: none;
                padding: 8px 32px;
                border-radius: 6px;
                font-size: 16px;
                font-weight: 500;
                margin-left: 8px;
                margin-right: 0;
            }
            #tabConverters:checked, #tabJson:checked {
                background: #818cf8;
                color: #fff;
            }
            #centeredStacked {
                min-width: 500px;
                max-width: 800px;
                max-height: 600px;
                width: 80vw;
            }
            #converterSection, #jsonSection {
                background: #fff;
                border-radius: 32px;
                box-shadow: 0 4px 24px rgba(99,102,241,0.08);
                max-height: 600px;
                width: 100%;
                margin: auto;
                
            }
            #sectionTitle {
                color: #6366f1;
                font-size: 20px;
                font-weight: 600;
            }
            #converterSelect, #convertToSelect, #inputValue, #jsonInput {
                padding: 8px;
                border-radius: 6px;
                border: 1px solid #c7d2fe;
                font-size: 16px;
                outline: none;
            }
            #converterSelect:focus, #convertToSelect:focus, #inputValue:focus, #jsonInput:focus {
                border: 1.5px solid #6366f1;
            }
            #formLabel {
                font-weight: 500;
                color: #374151;
            }
            #convertBtn {
                background: #6366f1;
                color: #fff;
                border: none;
                border-radius: 6px;
                padding: 12px 0;
                font-size: 18px;
                font-weight: 500;
                cursor: pointer;
                margin-top: 8px;
                margin-left: 3px;
                margin-right: 3px;
            }
            #convertBtn:hover {
                background: #818cf8;
            }
            #resultBox {
                background: #f1f5f9;
                border-radius: 8px;
                padding: 16px;
                color: #374151;
                font-size: 16px;
                box-shadow: 0 2px 8px rgba(99,102,241,0.05);
                margin-left: 3px;
                margin-right: 3px;
            }
        ''')

    