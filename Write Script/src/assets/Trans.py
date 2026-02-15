from assets.AppSystem import ScriptNote

class translate(ScriptNote):
    def __init__(self):
        super().__init__()
        self.translateBTN.clicked.connect(self.trans)

    def trans(self):
        if self.translateBTN.text() == "arabic":
            self.btn_del_tag.setText("حذف التاغ")
            self.btn_search.setText("إبحث")
            self.btn_add_tag.setText("أَضف")
            self.btn_save.setText("حفظ")
            self.btn_create.setText("إنشاء")
            self.intro.setText("مقدمة")
            self.Outro.setText("النهاية")
            self.Clear.setText("إخلاء")
            self.section.setText("فقرة")
            self.btn_delete.setText("حذف")
            self.list_notes_label.setText("قائمة السكريبتات")
            self.list_tags_label.setText("قائمة التاغز")
            self.Script_Speacker.setText("تحويل السكريبت")
            self.text_note.setPlaceholderText("-> إكتب شيئا")
            self.Ad.setText("إعلان")
            self.tag_input.setPlaceholderText("إبحث بإستخدام التاغ")
            self.translateBTN.setText("english")
        else:
            self.btn_del_tag.setText("Delete Script")
            self.btn_search.setText("Search Script by tag")
            self.btn_add_tag.setText("Add to script")
            self.btn_save.setText("Save script")
            self.btn_create.setText("Create Script")
            self.intro.setText("intro")
            self.Outro.setText("Outro")
            self.Clear.setText("Clear All")
            self.section.setText("section")
            self.btn_delete.setText("Delete script")
            self.list_notes_label.setText("List of Scripts")
            self.list_tags_label.setText("List of tags")
            self.Script_Speacker.setText("Compile Script")
            self.text_note.setPlaceholderText("-> Write a script...")
            self.Ad.setText("Ad")
            self.tag_input.setPlaceholderText("Enter tag")
            self.translateBTN.setText("arabic")

    def search_note(self):
        tag = self.tag_input.text().strip()

        if self.translateBTN.text() == "arabic":
            if self.btn_search.text() == "Search script by tag":
                filtered = {}

                for note_name, data in self.notes.items():
                    if tag in data["tags"]:
                        filtered[note_name] = data

                self.list_notes.clear()
                self.list_notes.addItems(filtered.keys())
                self.btn_search.setText("Reset Search")

            else:
                self.tag_input.clear()
                self.list_notes.clear()
                self.list_notes.addItems(self.notes.keys())
                self.btn_search.setText("Search script by tag")
            

        else:

            if self.btn_search.text() == "إبحث":
                filtered = {}

                for note_name, data in self.notes.items():
                    if tag in data["tags"]:
                        filtered[note_name] = data

                self.list_notes.clear()
                self.list_notes.addItems(filtered.keys())
                self.btn_search.setText("أعد البحث")

            else:
                self.tag_input.clear()
                self.list_notes.clear()
                self.list_notes.addItems(self.notes.keys())
                self.btn_search.setText("إبحث")