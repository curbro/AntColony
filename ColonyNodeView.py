import string

from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QPalette, QFont, QColor, QMovie, QPixmap
from PySide6.QtWidgets import QFrame, QPushButton, QLabel, QGridLayout, QWidget, QHBoxLayout, QVBoxLayout
from ColorConstants import *


class ColonyNodeView(QFrame):
    def __init__(self, ):

        super(ColonyNodeView, self).__init__()
        main_layout = QHBoxLayout()
        label_layout = QVBoxLayout()
        icon_layout = QVBoxLayout()
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setAutoFillBackground(True)
        self.palette = self.palette()
        self.palette.setColor(QPalette.Window, QColor(200, 178, 55))
        self.setPalette(self.palette)
        self.setLayout(main_layout)
        self.is_queen_present = False

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setMinimumSize(QtCore.QSize(96, 96))
        self.setMaximumSize(QtCore.QSize(96, 96))

        # Id
        self.id_label = QLabel(self)
        self.id_label.setText("1,2")
        self.id_label.setFont(NODE_FONT)
        self.set_label_font_color(self.id_label)
        label_layout.addWidget(self.id_label)

        # Queen
        self.queen_label = QLabel(self)
        self.queen_label.setText("")
        self.set_label_font_color(self.queen_label)
        label_layout.addWidget(self.queen_label)
        self.queen_icon = QLabel(self)
        self.queen_icon.setPixmap(QPixmap('resources/queen.gif'))
        self.queen_icon.setAlignment(QtCore.Qt.AlignRight)
        icon_layout.addWidget(self.queen_icon)

        # Forager
        self.forager_label = QLabel(self)
        self.forager_label.setText("F")
        self.set_label_font_color(self.forager_label)
        label_layout.addWidget(self.forager_label)
        self.forager_icon = QLabel(self)
        self.forager_icon.setPixmap(QPixmap('resources/forager.gif'))
        self.forager_icon.setAlignment(QtCore.Qt.AlignRight)
        icon_layout.addWidget(self.forager_icon)

        # Scout
        self.scout_label = QLabel(self)
        self.scout_label.setText("Sc")
        self.set_label_font_color(self.scout_label)
        label_layout.addWidget(self.scout_label)
        self.scout_icon = QLabel(self)
        self.scout_icon.setPixmap(QPixmap('resources/scout.gif'))
        self.scout_icon.setAlignment(QtCore.Qt.AlignRight)
        icon_layout.addWidget(self.scout_icon)

        # Soldier
        self.soldier_label = QLabel(self)
        self.soldier_label.setText("S")
        self.set_label_font_color(self.soldier_label)
        label_layout.addWidget(self.soldier_label)
        self.soldier_icon = QLabel(self)
        self.soldier_icon.setPixmap(QPixmap('resources/soldier.gif'))
        self.soldier_icon.setAlignment(QtCore.Qt.AlignRight)
        icon_layout.addWidget(self.soldier_icon)

        # Bala
        self.bala_label = QLabel(self)
        self.bala_label.setText("B")
        self.set_label_font_color(self.bala_label)
        label_layout.addWidget(self.bala_label)
        self.bala_icon = QLabel(self)
        self.bala_icon.setPixmap(QPixmap('resources/bala.gif'))
        self.bala_icon.setAlignment(QtCore.Qt.AlignRight)
        icon_layout.addWidget(self.bala_icon)

        # Food
        self.food_label = QLabel(self)
        self.food_label.setText("Food:")
        self.set_label_font_color(self.food_label)
        label_layout.addWidget(self.food_label)

        # Pheromone
        self.pheromone_label = QLabel(self)
        self.pheromone_label.setText("Ph:")
        self.set_label_font_color(self.pheromone_label)
        label_layout.addWidget(self.pheromone_label)

        main_layout.addLayout(label_layout)
        main_layout.addLayout(icon_layout)
        # self.setMinimumSize(96, 96)

    def set_label_font_color(self, label: QLabel) -> None:
        label.setStyleSheet("color: black")

    def show_node(self):
        self.setVisible(True)
        self.update()

    def hide_node(self):
        self.setVisible(False)

    def set_id(self, id: string) -> None:
        self.id_label.setText(id)

    def set_queen(self, is_queen_present: bool) -> None:
        self.is_queen_present = is_queen_present
        if is_queen_present:
            self.palette.setColor(QPalette.Window, QUEEN_NODE_COLOR)
        else:
            self.palette.setColor(QPalette.Window, OPEN_NODE_COLOR)
        self.setPalette(self.palette)

    def show_queen(self):
        self.queen_icon.show()

    def hide_queen(self):
        self.queen_icon.hide()

    def set_forager_count(self, forager_count: int) -> None:
        self.forager_label.setText("F: " + str(forager_count))

    def show_forager(self):
        self.forager_icon.show()

    def hide_forager(self):
        self.forager_label.hide()

    def set_scout_count(self, scout_count: int) -> None:
        self.scout_label.setText("Sc: " + str(scout_count))

    def show_scout(self):
        self.scout_icon.show()

    def hide_scout(self):
        self.scout_label.hide()

    def set_soldier_count(self, soldier_count: int) -> None:
        self.soldier_label.setText("S: " + str(soldier_count))

    def show_soldier(self):
        self.soldier_icon.show()

    def hide_soldier(self):
        self.soldier_icon.hide()

    def set_bala_count(self, bala_count: int) -> None:
        self.bala_label.setText("B: " + str(bala_count))

    def show_bala(self):
        self.bala_icon.show()

    def hide_bala(self):
        self.bala_icon.hide()

    def set_food_count(self, food_count: int) -> None:
        self.food_label.setText("Food: " + str(food_count))

    def set_pheromone_level(self, pheromone_count: int) -> None:
        self.pheromone_label.setText("Ph: " + str(pheromone_count))

        if pheromone_count == 1000:
            self.palette.setColor(QPalette.Window, PHEROMONE_1000)
        elif pheromone_count >= 800:
            self.palette.setColor(QPalette.Window, PHEROMONE_800)
        elif pheromone_count >= 600:
            self.palette.setColor(QPalette.Window, PHEROMONE_600)
        elif pheromone_count >= 400:
            self.palette.setColor(QPalette.Window, PHEROMONE_400)
        elif pheromone_count >= 200:
            self.palette.setColor(QPalette.Window, PHEROMONE_200)
        elif pheromone_count > 0:
            self.palette.setColor(QPalette.Window, PHEROMONE_0)
        elif self.is_queen_present:
            self.palette.setColor(QPalette.Window, QUEEN_NODE_COLOR)
        else:
            self.palette.setColor(QPalette.Window, OPEN_NODE_COLOR)
        self.setPalette(self.palette)

