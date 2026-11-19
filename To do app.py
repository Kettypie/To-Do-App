import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QScrollArea, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence


class Home(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Do It!")

        self.tasks = []
        self.tasks_remaining = []

        #############################################################

        self.wids_lays()

        self.funcs()

        self.stylings()

    def wids_lays(self):
        self.main_wid = QWidget()
        self.main_lay = QVBoxLayout()

        self.main_wid.setLayout(self.main_lay)

        self.setCentralWidget(self.main_wid)

        #############################################################

        self.wid1 = QWidget()
        self.lay1 = QVBoxLayout()

        self.wid1.setLayout(self.lay1)

        self.main_lay.addWidget(self.wid1)

        #############################################################

        self.title_label = QLabel("Do It!")

        self.title_label.setObjectName("title_label")

        self.lay1.addWidget(self.title_label)

        #############################################################

        self.wid2 = QWidget()
        self.lay2 = QHBoxLayout()

        self.wid2.setLayout(self.lay2)

        self.main_lay.addWidget(self.wid2)

        #############################################################

        # tasks = self.tasks.count()

        # print(tasks)

        self.task_count = QLabel(f"Number of tasks to do: {len(self.tasks_remaining)}")
        self.input_field = QLineEdit()
        self.add_button = QPushButton("ADD")

        self.task_count.setObjectName("task_count")
        self.add_button.setObjectName("add_button")

        self.lay2.addWidget(self.task_count)
        self.lay2.addWidget(self.input_field)
        self.lay2.addWidget(self.add_button)

        #############################################################

        self.wid3 = QWidget()
        self.lay3 = QVBoxLayout()

        self.wid3.setLayout(self.lay3)

        self.main_lay.addWidget(self.wid3)

        #############################################################

        self.task_name_error = QLabel()

        self.task_name_error.setObjectName("task_name_error")

        self.lay3.addWidget(self.task_name_error)

        #############################################################

        self.wid4 = QWidget()
        self.lay4 = QVBoxLayout()

        self.wid4.setLayout(self.lay4)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.lay4.addStretch()
        self.scroll_area.setWidget(self.wid4)

        self.main_lay.addWidget(self.scroll_area)

        self.scroll_area.setObjectName("scroll_area")

        self.scroll_area.setStyleSheet("background-color: gray;" \
                "border-color: darkgray;" \
                "border-radius: 5px;" \
                "color: white;" \
                "font-family: calibri;" \
                "font-size: 20px;")

    def task_count_update(self):
        self.task_count.setText(f"Number of tasks to do: {len(self.tasks_remaining)}")

    def tasks_remaining_update(self, name,bool):
        if bool:
            self.tasks_remaining.remove(name)

        elif bool == False:
            self.tasks_remaining.append(name)

        self.task_count_update()

        print(self.tasks_remaining)
        
    def funcs(self):
        self.add_button.clicked.connect(self.add)
        self.input_field.setPlaceholderText("Enter a task name")

        self.enter = QShortcut(QKeySequence("Return"), self)
        self.enter.activated.connect(self.add)

    def add(self):
        task_name = self.input_field.text().lstrip().rstrip()

        if task_name == "":
            self.task_name_error.setText("Enter a name!")

        elif task_name in self.tasks:
            reply = QMessageBox.warning(
                None,
                "Confirmation",
                "This task already exists!\n"
                "Do you still want to create it?",
                QMessageBox.No,
                QMessageBox.Yes
            )

            if reply == QMessageBox.Yes:
                task = Tasks(name=task_name, mainwinodow=self)
                
                self.lay4.insertWidget(0, task)
                
                self.tasks.append(task_name)
                self.tasks_remaining.append(task_name)

                self.input_field.clear()
                self.task_name_error.clear()
                
                self.task_count_update()
                
                print(self.tasks)
                print(len(self.tasks))

            else:
                pass

        else:
            task = Tasks(name=task_name, mainwinodow=self)

            self.lay4.insertWidget(0, task)

            self.tasks.append(task_name)
            self.tasks_remaining.append(task_name)

            self.input_field.clear()
            self.task_name_error.clear()

            self.task_count_update()

            print(self.tasks)
            print(len(self.tasks))

    def remove_task(self, name):
        print("Before: ", self.tasks)
        self.tasks.remove(name)

        if name in self.tasks_remaining:
            self.tasks_remaining.remove(name)

        print("After: ", self.tasks)
        self.task_count_update()

    def stylings(self):
        self.setStyleSheet("""
        QPushButton{
            background-color: hsl(0, 0, 130);
            color: white;
            font-family: arial black;
        }

        QMainWindow{
            background-color: hsl(0, 0, 110);
        }

        QLabel#title_label{
            color: cyan;
            font-family: calibri;
            font-size: 50px;
            font-weight: bold;
        }

        QLabel#task_count{
            color: white;
            font-family: calibri;
            font-size: 15px;
            font-weight: bold;
        }

        QLabel#task_name_error{
            color: red;
            font-family: Arial;
            font-size: 15px;
            font-weight: bold;
        }

        QScrollArea#scroll_area{
            background-color: gray;
        }
    """)

class Tasks(QWidget):
    def __init__(self, name, mainwinodow):
        super().__init__()

        self.name = name
        self.mainwindow = mainwinodow

        self.main_lay = QVBoxLayout()
        self.setLayout(self.main_lay)

        self.task_wid = QWidget()
        self.main_lay.addWidget(self.task_wid)

        self.task_wid.setStyleSheet("background-color: dimgray;")
        self.task_wid.setFixedHeight(50)

        self.task_lay = QHBoxLayout()

        self.task_wid.setLayout(self.task_lay)

        #############################################################

        self.label = QLabel(self.name)
        self.done = QPushButton("Done")
        self.undone = QPushButton("Undone")
        self.delete_button = QPushButton("🗑️")

        self.task_lay.addWidget(self.label)
        self.task_lay.addWidget(self.done)
        self.task_lay.addWidget(self.undone)
        self.task_lay.addWidget(self.delete_button)

        self.label.setFixedHeight(30)
        self.label.setStyleSheet("color: white;" \
        "font-family: calibri;" \
        "font-weight: bold;" \
        "font-size: 20px;")

        self.done.setFixedWidth(80)
        self.done.setStyleSheet("background: darkgray;" \
        "font-family: calibri;" \
        "font-weight: bold;" \
        "font-size: 20px;" \
        "height: 30;")

        self.undone.setFixedWidth(80)
        self.undone.setStyleSheet("background: darkgray;" \
        "font-family: calibri;" \
        "font-weight: bold;" \
        "font-size: 20px;" \
        "height: 30;")

        self.delete_button.setFixedWidth(80)
        self.delete_button.setStyleSheet("background: darkgray;" \
        "font-size: 20px;" \
        "height: 30;")


        self.undone.setHidden(True)

        #############################################################

        self.delete_button.clicked.connect(self.delete_click)
        self.done.clicked.connect(self.done_click)
        self.undone.clicked.connect(self.undone_click)

    def delete_click(self):
        reply = QMessageBox.warning(
            None,
            "Comfirmation",
            f"""Are you sure you want to delete the task "{self.name}"?""",
            QMessageBox.Yes,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.deleteLater()
            self.mainwindow.remove_task(self.name)
            
        else:
            pass

    def done_click(self):
        self.label.setText(''.join([c + '\u0336' for c in self.name]))

        self.done.setHidden(True)
        self.undone.setHidden(False)

        self.mainwindow.tasks_remaining_update(self.name, True)

    def undone_click(self):
        self.label.setText(self.name)

        self.undone.setHidden(True)
        self.done.setHidden(False)

        self.mainwindow.tasks_remaining_update(self.name, False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home = Home()
    home.show()
    sys.exit(app.exec_())