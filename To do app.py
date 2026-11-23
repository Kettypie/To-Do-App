import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QScrollArea, QMessageBox, QShortcut
from PyQt5.QtGui import QKeySequence

import themes

class Home(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Do It!")

        self.tasks = []
        self.tasks_remaining = []
        self.tasks_widgets = []

        self.theme_toggle_condition = True

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
        self.lay1 = QHBoxLayout()

        self.wid1.setLayout(self.lay1)

        self.main_lay.addWidget(self.wid1)

        #############################################################

        self.title_label = QLabel("Do It!")
        self.theme_toggle = QPushButton("🌕")

        self.title_label.setObjectName("title_label")

        self.lay1.addWidget(self.title_label)
        self.lay1.addStretch()
        self.lay1.addWidget(self.theme_toggle)

        #############################################################

        self.wid2 = QWidget()
        self.lay2 = QHBoxLayout()

        self.wid2.setLayout(self.lay2)

        self.main_lay.addWidget(self.wid2)

        #############################################################

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
        self.theme_toggle.clicked.connect(self.theme_changer)

        self.input_field.setPlaceholderText("Enter a task name")

        self.enter = QShortcut(QKeySequence("Return"), self)
        self.enter.activated.connect(self.add)

    def add(self):
        task_name = self.input_field.text().lstrip().rstrip()

        if task_name == "":
            self.task_name_error.setText("Enter a name!")

        elif len(task_name) > 50:
            self.task_name_error.setText("Too long!")

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
                self.tasks_widgets.append(task)

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
            self.tasks_widgets.append(task)

            self.input_field.clear()
            self.task_name_error.clear()

            self.task_count_update()

            print(self.tasks)
            print(len(self.tasks))

    def remove_task(self, name, widget):
        print("Before: ", self.tasks)
        print("Before: ", self.tasks_widgets)
        self.tasks.remove(name)
        self.tasks_widgets.remove(widget)

        if name in self.tasks_remaining:
            self.tasks_remaining.remove(name)

        print("After: ", self.tasks)
        print("After: ", self.tasks_widgets)
        self.task_count_update()

    def stylings(self):
        self.setStyleSheet(themes.light_mode)

    def theme_changer(self):
        if self.theme_toggle_condition:
            self.setStyleSheet(themes.dark_mode)
            self.theme_toggle_condition = False

            if self.tasks_widgets:
                for task in self.tasks_widgets:
                    task.theme_changer(self.theme_toggle_condition)
            
            else:
                pass

        else:
            self.setStyleSheet(themes.light_mode)
            self.theme_toggle_condition = True

            if self.tasks_widgets:
                for task in self.tasks_widgets:
                    task.theme_changer(self.theme_toggle_condition)
            
            else:
                pass

    def change_task_name(self, old_name, new_name, task):
        print("Before: ", self.tasks)

        index = self.tasks.index(old_name)
        self.tasks.remove(old_name)
        self.tasks.insert(index, new_name)

        print("After: ", self.tasks)

        #############################################################

        print("Before: ", self.tasks_remaining)
        
        index = self.tasks_remaining.index(old_name)
        self.tasks_remaining.remove(old_name)
        self.tasks_remaining.insert(index, new_name)

        print("After: ", self.tasks_remaining)

class Tasks(QWidget):
    def __init__(self, name, mainwinodow):
        super().__init__()

        self.name = name
        self.mainwindow = mainwinodow

        self.main_lay = QVBoxLayout()
        self.setLayout(self.main_lay)

        self.task_wid = QWidget()
        self.main_lay.addWidget(self.task_wid)

        self.task_wid.setFixedHeight(50)

        self.task_lay = QHBoxLayout()

        self.task_wid.setLayout(self.task_lay)

        #############################################################

        self.label = QLabel(self.name)
        self.done = QPushButton("Done")
        self.undone = QPushButton("Undone")
        self.delete_button = QPushButton("Delete")

        ##############################################################
        
        self.edit_name = QLineEdit()
        self.edit_button = QPushButton("Edit")
        self.save_button = QPushButton("Save")

        self.task_lay.addWidget(self.label)
        self.task_lay.addWidget(self.edit_name)
        self.task_lay.addWidget(self.edit_button)
        self.task_lay.addWidget(self.save_button)
        self.task_lay.addWidget(self.done)
        self.task_lay.addWidget(self.undone)
        self.task_lay.addWidget(self.delete_button)

        #############################################################

        self.label.setFixedHeight(30)
        self.edit_button.setFixedWidth(100)
        self.done.setFixedWidth(100)
        self.undone.setFixedWidth(100)
        self.delete_button.setFixedWidth(100)

        #############################################################

        self.edit_name.setHidden(True)
        self.save_button.setHidden(True)
        self.undone.setHidden(True)

        #############################################################

        self.edit_button.clicked.connect(self.edit_click)
        self.save_button.clicked.connect(self.save_click)
        self.delete_button.clicked.connect(self.delete_click)
        self.done.clicked.connect(self.done_click)
        self.undone.clicked.connect(self.undone_click)

        #############################################################
        
        self.theme_changer(bool=self.mainwindow.theme_toggle_condition)

    def delete_click(self):
        reply = QMessageBox.warning(
            None,
            "Comfirmation",
            f"""Are you sure that you want to delete the task "{self.name}"?""",
            QMessageBox.Yes,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.deleteLater()
            self.mainwindow.remove_task(self.name, self)
            
        else:
            pass

    def done_click(self):
        self.label.setText(''.join([c + '\u0336' for c in self.name]))

        self.edit_button.setHidden(True)
        self.done.setHidden(True)
        self.undone.setHidden(False)

        self.mainwindow.tasks_remaining_update(self.name, True)

    def undone_click(self):
        self.label.setText(self.name)

        self.edit_button.setHidden(False)
        self.undone.setHidden(True)
        self.done.setHidden(False)

        self.mainwindow.tasks_remaining_update(self.name, False)

    def edit_click(self):
        self.label.setHidden(True)

        self.edit_name.setHidden(False)
        self.done.setHidden(True)
        self.edit_name.setText(self.name)

        self.edit_button.setHidden(True)
        self.save_button.setHidden(False)

    def save_click(self): #working here
        self.old_name = self.name
        self.name = self.edit_name.text().lstrip().rstrip()

        self.label.setText(self.name)
        self.label.setHidden(False)
        
        self.edit_name.setHidden(True)
        self.done.setHidden(False)

        self.edit_button.setHidden(False)
        self.save_button.setHidden(True)

        self.mainwindow.change_task_name(old_name=self.old_name, new_name=self.name, task=self)

    def theme_changer(self, bool):
        if bool:
            self.task_wid.setStyleSheet("""
                background-color: #FFFFFF;
                border: 1px solid #E1E5EC;
                border-radius: 8px;
            """)

            self.label.setStyleSheet("""
                color: #252B36;
                font-family: Calibri;
                font-weight: bold;
                font-size: 20px;
                border: none;
            """)

            self.edit_name.setStyleSheet("""
                color: #252B36;
                font-family: Calibri;
                font-weight: bold;
                font-size: 15px;
            """)

            self.edit_button.setStyleSheet("""
                QPushButton {
                    background-color: #E0F0FF;
                    color: #1D639B;
                    border: 1px solid #B8DAF8;
                    border-radius: 8px;
                    font-family: Calibri;
                    font-weight: bold;
                    font-size: 16px;
                    padding: 5px 12px;
                }
                QPushButton:hover {
                    background-color: #C9E3FC;
                }
            """)

            self.save_button.setStyleSheet("""
                QPushButton {
                    background-color: #E6E8FF;
                    color: #39429B;
                    border: 1px solid #C2C7F7;
                    border-radius: 8px;
                    font-family: Calibri;
                    font-weight: bold;
                    font-size: 16px;
                    padding: 5px 12px;
                }
                QPushButton:hover {
                    background-color: #D2D6FC;
                }
            """)

            self.done.setStyleSheet("""
                QPushButton {
                    background-color: #DDF5E4;
                    color: #247542;
                    border: 1px solid #B8E5C5;
                    border-radius: 8px;
                    font-family: Calibri;
                    font-weight: bold;
                    font-size: 16px;
                    padding: 5px 12px;
                }
                QPushButton:hover {
                    background-color: #C5EBD0;
                }
            """)

            self.undone.setStyleSheet("""
                QPushButton {
                    background-color: #FFF0D2;
                    color: #94600E;
                    border: 1px solid #F1DCA9;
                    border-radius: 8px;
                    font-family: Calibri;
                    font-weight: bold;
                    font-size: 16px;
                    padding: 5px 12px;
                }
                QPushButton:hover {
                    background-color: #F9E3B5;
                }
            """)

            self.delete_button.setStyleSheet("""
                QPushButton {
                    background-color: #FFE2E2;
                    color: #B52D37;
                    border: 1px solid #F5C0C0;
                    border-radius: 8px;
                    font-family: Calibri;
                    font-weight: bold;
                    font-size: 16px;
                    padding: 5px 12px;
                }
                QPushButton:hover {
                    background-color: #FFCACA;
                }
            """)
        else:
            self.task_wid.setStyleSheet("""
                background-color: #242832;
                border: 1px solid #383E4B;
                border-radius: 8px;
            """)

            self.label.setStyleSheet("""
                color: #EAEAEA;
                font-family: Calibri;
                font-weight: bold;
                font-size: 20px;
                border: none;
            """)

            self.edit_name.setStyleSheet("""
                color: #EAEAEA;
                font-family: Calibri;
                font-weight: bold;
                font-size: 15px;
            """)

            self.edit_button.setStyleSheet("""
                QPushButton {
                    background-color: #25384B;
                    color: #8CC8FF;
                    border: 1px solid #35526E;
                    border-radius: 8px;
                    font-family: Calibri;
                    font-weight: bold;
                    font-size: 16px;
                    padding: 5px 12px;
                }
                QPushButton:hover {
                    background-color: #314C66;
                }
            """)

            self.save_button.setStyleSheet("""
                QPushButton {
                    background-color: #2D304E;
                    color: #A5AEFF;
                    border: 1px solid #424773;
                    border-radius: 8px;
                    font-family: Calibri;
                    font-weight: bold;
                    font-size: 16px;
                    padding: 5px 12px;
                }
                QPushButton:hover {
                    background-color: #3C4069;
                }
            """)

            self.done.setStyleSheet("""
                QPushButton {
                    background-color: #263D32;
                    color: #8BE0A5;
                    border: 1px solid #365C45;
                    border-radius: 8px;
                    font-family: Calibri;
                    font-weight: bold;
                    font-size: 16px;
                    padding: 5px 12px;
                }
                QPushButton:hover {
                    background-color: #345943;
                }
            """)

            self.undone.setStyleSheet("""
                QPushButton {
                    background-color: #493C24;
                    color: #FFD580;
                    border: 1px solid #66532D;
                    border-radius: 8px;
                    font-family: Calibri;
                    font-weight: bold;
                    font-size: 16px;
                    padding: 5px 12px;
                }
                QPushButton:hover {
                    background-color: #63502D;
                }
            """)

            self.delete_button.setStyleSheet("""
                QPushButton {
                    background-color: #482B30;
                    color: #FF929B;
                    border: 1px solid #663940;
                    border-radius: 8px;
                    font-family: Calibri;
                    font-weight: bold;
                    font-size: 16px;
                    padding: 5px 12px;
                }
                QPushButton:hover {
                    background-color: #653840;
                }
            """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    home = Home()
    home.show()
    sys.exit(app.exec_())