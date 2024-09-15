import sys
from PySide6.QtGui import (
    QAction,
)
from PySide6.QtCore import (
    QSize,
    Qt,
    QJsonDocument,
)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QMenu,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show()

        with open('memory.json', 'r') as f:
            data = f.read()

        self.setWindowTitle("JASSROE")
        self.label = QLabel()
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenu)

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.setFixedSize(QSize(300, 200))

    def contextMenu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("Thing 1", self))
        context.addAction(QAction("Thing 2", self))
        context.addAction(QAction("Cat in the Hat", self))
        context.exec(self.mapToGlobal(pos))

    def mousePressEvent(self, event):
        # app.exit()
        print("hohla")



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()