import sys
from PyQt5.QtWidgets import QApplication, QWidget,QDesktopWidget,QPushButton, QBoxLayout,QTreeWidget,QTreeWidgetItem

__auther__='d0rk'

class my_app(QWidget):
    def __init__(self):
        super().__init__()

        self.add_btn=QPushButton('추가')
        self.del_btn=QPushButton('삭제')
        self.wishlist=QTreeWidget(self)
        self.lecture_list=QTreeWidget(self)

        self.initUI()



    def initUI(self):
        self.setWindowTitle('QTree example')
        self.init_lectures()

        self.resize(800, 480)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def init_lectures(self):
        headers = ['과목','시간','캠퍼스','강의실','교수명']

        self.lecture_list.setColumnCount(len(headers))
        self.lecture_list.setHeaderLabels(headers)

        self.wishlist.setColumnCount(len(headers))
        self.wishlist.setHeaderLabels(headers)


        list_layout = QBoxLayout(QBoxLayout.LeftToRight)
        list_layout.addWidget(self.lecture_list)
        list_layout.addWidget(self.wishlist)

        lecture_root = QTreeWidget.invisibleRootItem(self.lecture_list)
        # append data for exam
        datas = ['하','이','루','방','가']
        item = QTreeWidgetItem()
        for idx, data in enumerate(datas):
            item.setText(idx, data)

        lecture_root.addChild(item)

        datas = ['바','이','루','방','가']
        item = QTreeWidgetItem()
        for idx, data in enumerate(datas):
            item.setText(idx, data)

        lecture_root.addChild(item)

        datas = ['D', '0', 'R', 'K', '_']
        item = QTreeWidgetItem()
        for idx, data in enumerate(datas):
            item.setText(idx, data)

        lecture_root.addChild(item)

        # add button by layout
        btn_layout = QBoxLayout(QBoxLayout.RightToLeft)
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.del_btn)

        main_layout = QBoxLayout(QBoxLayout.TopToBottom)
        main_layout.addLayout(list_layout)
        main_layout.addLayout(btn_layout)

        # connect event when button clicked
        self.add_btn.clicked.connect(self.move_item)
        self.del_btn.clicked.connect(self.move_item)

        self.setLayout(main_layout)
        return main_layout


    def move_item(self):
        # This function called when btn clicked

        # sender is button caller
        sender = self.sender()

        # if sender is add_btn
        if self.add_btn == sender:
            source = self.lecture_list
            target = self.wishlist
        else:
            source = self.wishlist
            target = self.lecture_list

        # get item from source and delete item from source
        item = QTreeWidget.invisibleRootItem(source).takeChild(source.currentIndex().row())
        # add to target item from source
        QTreeWidget.invisibleRootItem(target).addChild(item)


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = my_app()
    sys.exit(app.exec_())

