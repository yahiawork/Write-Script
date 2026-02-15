import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QLabel, QListWidget, QPushButton,
    QLineEdit, QTextEdit, QHBoxLayout, QVBoxLayout
)
from PyQt5.QtGui import QFont, QIcon



class ScriptNote(QWidget):
        
    def __init__(self):
        super().__init__()
        self.notes_file = "assets\json\save.json"

        try:
            with open(self.notes_file, "r", encoding="utf-8") as file:
                self.notes = json.load(file)
        except:
            self.notes = {
                "Welcome!": {
                    "text": "This is the best script taking app in the world!",
                    "tags": ["good", "instructions"]
                }
            }
            with open(self.notes_file, "w", encoding="utf-8") as file:
                json.dump(self.notes, file, ensure_ascii=False, indent=4)

        self.setWindowTitle("Script Note")
        self.resize(900, 500)
        self.setStyleSheet("""
                        QWidget {
                                background: #000;
                                color: #fff;
                            

                                        }
                        QPushButton {
                                background: #fff;
                                color: #000;
                                padding: 8px;
                                border-radius: 10px;
                                        }
                        QLineEdit {
                                background: #111;
                                color: #fff;
                                padding: 8px;
                                border-radius: 10px;
                                border: 1px solid #fff;
                                        }
                        QLineEdit#result {
                                background: #555;
                                color: #fff;
                                padding: 8px;
                                border-radius: 10px;
                                border: 1px solid #111;
                                        }
                        QTextEdit {
                                background: #111;
                                color: #fff;
                                padding: 8px;
                                border-radius: 10px;
                                border: 1px solid #fff;
                                        }
                        QListWidget {
                                background: #fff;
                                color: #000;
                                font-size: 16px;
                                padding: 8px;
                                border-radius: 10px;
                                border: 1px solid #555;
                                        }
                            
                        QPushButton:hover {
                            background: #666;
                                color: #fff;
                            }
        """)

        self.text_note = QTextEdit()

        self.d = 0

        self.list_notes_label = QLabel("List of Scripts")
        self.list_notes = QListWidget()

        self.btn_create = QPushButton("Create script")
        self.btn_delete = QPushButton("Delete script")
        self.btn_save = QPushButton("Save script")

        self.list_tags_label = QLabel("List of tags")
        self.list_tags = QListWidget()

        self.tag_input = QLineEdit()
        self.tag_input.setPlaceholderText("Enter tag...")

        self.btn_add_tag = QPushButton("Add to script")
        self.btn_del_tag = QPushButton("Untag from script")
        self.btn_search = QPushButton("Search script by tag")

        self.intro = QPushButton("intro")
        self.section = QPushButton("Section")
        self.Outro = QPushButton("Outro")
        self.Ad = QPushButton("Ad")
        self.Clear = QPushButton("Clear All")
        self.result = QLineEdit()
        self.result.setObjectName("result")
        self.result.setReadOnly(True)

        self.translateBTN = QPushButton("arabic")
        
                                
        self.Script_Speacker = QPushButton("Compile Script")

        layout_right = QVBoxLayout()

        layout_right.addWidget(self.list_notes_label)
        layout_right.addWidget(self.list_notes)


        notes_btn_row = QHBoxLayout()
        notes_btn_row.addWidget(self.btn_create)
        notes_btn_row.addWidget(self.btn_delete)
        layout_right.addLayout(notes_btn_row)

        layout_right.addWidget(self.btn_save)

        layout_right.addWidget(self.list_tags_label)
        layout_right.addWidget(self.list_tags)
        layout_right.addWidget(self.tag_input)

        tags_btn_row = QHBoxLayout()
        tags_btn_row.addWidget(self.btn_add_tag)
        tags_btn_row.addWidget(self.btn_del_tag)
        layout_right.addLayout(tags_btn_row)


        layout_right.addWidget(self.btn_search)
        layout_right.addWidget(self.Script_Speacker)


        layout_left = QVBoxLayout()
        buttons1 = QHBoxLayout()
        buttons2 = QHBoxLayout()
        layout_left.addWidget(self.Clear)
        buttons1.addWidget(self.intro)
        buttons1.addWidget(self.Outro)
        buttons2.addWidget(self.section)
        buttons2.addWidget(self.Ad)
        layout_left.addWidget(self.result)
        buttons1.setAlignment(Qt.AlignTop)
        layout_left.addLayout(buttons2)
        layout_left.addLayout(buttons1)
        layout_left.addWidget(self.translateBTN)

        layout_main = QHBoxLayout()
        layout_main.addLayout(layout_left, 1)   
        layout_main.addWidget(self.text_note, 3)   
        layout_main.addLayout(layout_right, 1)


        self.setLayout(layout_main)



        self.list_notes.itemClicked.connect(self.show_results)
        self.btn_create.clicked.connect(self.add_note)
        self.btn_delete.clicked.connect(self.del_note)
        self.btn_save.clicked.connect(self.save_note)

        self.Script_Speacker.clicked.connect(self.extract)

        self.btn_add_tag.clicked.connect(self.add_tag)
        self.btn_del_tag.clicked.connect(self.del_tag)
        self.btn_search.clicked.connect(self.search_note)


        self.btn_del_tag.setFont(QFont('Arial Rounded MT Bold', 11))
        self.btn_search.setFont(QFont('Arial Rounded MT Bold', 11))
        self.btn_add_tag.setFont(QFont('Arial Rounded MT Bold', 11))
        self.btn_save.setFont(QFont('Arial Rounded MT Bold', 11))
        self.btn_create.setFont(QFont('Arial Rounded MT Bold', 11))
        self.intro.setFont(QFont('Arial Rounded MT Bold', 11))
        self.Outro.setFont(QFont('Arial Rounded MT Bold', 11))
        self.Clear.setFont(QFont('Arial Rounded MT Bold', 11))
        self.section.setFont(QFont('Arial Rounded MT Bold', 11))
        self.btn_delete.setFont(QFont('Arial Rounded MT Bold', 11))
        self.list_notes_label.setFont(QFont('Arial Rounded MT Bold', 18))
        self.list_tags_label.setFont(QFont('Arial Rounded MT Bold', 18))
        self.text_note.setFont(QFont('Courier New', 14))
        self.tag_input.setFont(QFont('Arial Rounded MT Bold', 11))
        self.Script_Speacker.setFont(QFont('Arial Rounded MT Bold', 11))
        self.translateBTN.setFont(QFont('Arial Rounded MT Bold', 11))
        self.text_note.setPlaceholderText("-> Write a script...")
        self.Ad.setFont(QFont('Arial Rounded MT Bold', 11))
        self.result.setFont(QFont('Arial Rounded MT Bold', 11))
        self.list_notes.addItems(self.notes.keys())

        if self.translateBTN.text() == "arabic":
            self.intro.clicked.connect(lambda: self.add_intro('intro'))
            self.Outro.clicked.connect(lambda: self.add_outro('outro'))
            self.section.clicked.connect(lambda: self.add_section('section'))
            self.Clear.clicked.connect(self.Clear_section)
            self.Ad.clicked.connect(lambda: self.add_ad('AD'))
        elif self.translateBTN.text() == "english":
            self.intro.clicked.connect(lambda: self.add_intro('مقدمة'))
            self.Outro.clicked.connect(lambda: self.add_outro('النهاية'))
            self.section.clicked.connect(lambda: self.add_section('فقرة'))
            self.Clear.clicked.connect(self.Clear_section)
            self.Ad.clicked.connect(lambda: self.add_ad('إعلان'))
            

    def save_json(self):
        with open(self.notes_file, "w", encoding="utf-8") as file:
            json.dump(self.notes, file, ensure_ascii=False, indent=4)


    def show_results(self):
        if self.list_notes.currentItem():
            name = self.list_notes.currentItem().text()
            self.text_note.setText(self.notes[name]["text"])
            self.list_tags.clear()
            self.list_tags.addItems(self.notes[name]["tags"])



    def add_note(self):
        name = "Video #"
        i = 1
        while f"{name}{i}" in self.notes:
            i += 1
        new_name = f"{name}{i}"

        self.notes[new_name] = {"text": "", "tags": []}
        self.list_notes.addItem(new_name)
        self.list_notes.setCurrentRow(self.list_notes.count() - 1)
        self.save_json()


    def extract(self):
        #text = text_note.toPlainText()
        self.result.setText(f"✅ result in : ")
    
        
    def del_note(self):
        if self.list_notes.currentItem():
            name = self.list_notes.currentItem().text()
            del self.notes[name]
            self.list_notes.clear()
            self.list_notes.addItems(self.notes.keys())
            self.text_note.clear()
            self.list_tags.clear()
            self.save_json()


    def save_note(self):
        if self.list_notes.currentItem():
            name = self.list_notes.currentItem().text()
            self.notes[name]["text"] = self.text_note.toPlainText()
            self.save_json()


    def add_tag(self):
        if self.list_notes.currentItem():
            name = self.list_notes.currentItem().text()
            tag = self.tag_input.text().strip()
            if tag and tag not in self.notes[name]["tags"]:
                self.notes[name]["tags"].append(tag)
                self.list_tags.addItem(tag)
                self.save_json()
                self.tag_input.clear()
        
    def Clear_section(self):
        self.text_note.clear()


    def del_tag(self):
        if self.list_notes.currentItem() and self.list_tags.currentItem():
            name = self.list_notes.currentItem().text()
            tag = self.list_tags.currentItem().text()
            self.notes[name]["tags"].remove(tag)
            self.show_results()
            self.save_json()
    
    def add_section(self, something):
        self.d += 1
        self.text_note.append(f"-> [{something} #{self.d}]")

    def add_intro(self, stringintro):
        self.text_note.append(f"-> [{stringintro}]")

    def add_ad(self, stringAd):
        self.text_note.append(f"-> [{stringAd}]")

    def add_outro(self, stringoutro):
        self.text_note.append(f"-> [{stringoutro}]")

    def FontSize(self, value):
        pass

