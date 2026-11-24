
dark_mode = """
QMainWindow, QWidget {
    background-color: #191D25;
    color: #E6E6E6;
    font-family: "Segoe UI";
    font-size: 10pt;
}

QLabel {
    color: #E6E6E6;
    font-size: 15px;
}

QLabel#title_label {
    color: green;
    font-size: 50px;
    font-family: gabriola;
    font-weight: bold;
    background: transparent;
}

QLabel#task_name_error {
    color: red;
    font-weight: bold;
}

QPushButton#close_error_button {
    background: transparent;
    border: 1px solid red;
    color: red;
    font-weight:bold;
    font-size: 15px;
    padding: none;
}

QPushButton#close_error_button:hover {
    color: darkred;
}

QPushButton {
    background-color: #292D36;
    color: #FFFFFF;
    border: 1px solid #3A404C;
    border-radius: 7px;
    padding: 8px 16px;
}

QPushButton:hover {
    background-color: #383F4C;
    border-color: #64748B;
}

QPushButton:pressed {
    background-color: #20242C;
}

QLineEdit {
    background-color: #222630;
    color: #FFFFFF;
    border: 1px solid #3A404C;
    border-radius: 7px;
    padding: 8px;
    selection-background-color: #5277D9;
}

QLineEdit:focus {
    border: 1px solid #638BFF;
}

QLineEdit::placeholder {
    color: #858B98;
}

QWidget#centralwidget {
    background-color: #181A1F;
}
"""

###########################################################


light_mode = """
QMainWindow, QWidget {
    background-color: #F3F5F9;
    color: #252A34;
    font-family: "Segoe UI";
    font-size: 10pt;
}

QLabel {
    color: black;
    font-size: 15px;
}

QLabel#title_label {
    color: green;
    font-size: 50px;
    font-family: gabriola;
    font-weight: bold;
    background: transparent;
}

QLabel#task_name_error {
    color: red;
    font-weight: bold;
}

QPushButton#close_error_button {
    background: transparent;
    border: 1px solid red;
    color: red;
    font-weight:bold;
    font-size: 15px;
    padding: none;
}

QPushButton#close_error_button:hover {
    color: darkred;
}

QPushButton {
    background-color: #FFFFFF;
    color: #252A34;
    border: 1px solid #D9DDE5;
    border-radius: 7px;
    padding: 8px 16px;
}

QPushButton:hover {
    background-color: #E9EDF5;
    border-color: #AAB5C8;
}

QPushButton:pressed {
    background-color: #DDE3EF;
}

QLineEdit {
    background-color: #FFFFFF;
    color: #252A34;
    border: 1px solid #D9DDE5;
    border-radius: 7px;
    padding: 8px;
    selection-background-color: #5277D9;
}

QLineEdit:focus {
    border: 1px solid #5277D9;
}

QLineEdit::placeholder {
    color: #A0A5AF;
}

QWidget#centralwidget {
    background-color: #F5F6FA;
}
"""