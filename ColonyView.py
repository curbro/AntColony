from PySide6 import QtWidgets
from PySide6.QtGui import QColor, QPalette, Qt
from PySide6.QtWidgets import QFrame, QGridLayout, QSizePolicy, QScrollArea, QLabel, QWidget

import ColonyNodeView


class ColonyView(QScrollArea):
    NODE_SIZE = 12
    BACKGROUND_COLOR = QColor(200, 178, 55)

    def __init__(self, height_in_nodes, width_in_nodes, parent: QWidget):
        super(ColonyView, self).__init__()
        self.setParent(parent)
        self.layout = QGridLayout()
        for x in range(height_in_nodes):
            self.layout.setRowStretch(x, 1)
        self.setLayout(self.layout)
        self.setMinimumSize(height_in_nodes * ColonyView.NODE_SIZE, width_in_nodes * ColonyView.NODE_SIZE)
        self.setAutoFillBackground(True)
        self.palette = self.palette()
        self.palette.setColor(QPalette.Window, ColonyView.BACKGROUND_COLOR)
        self.setPalette(self.palette)

        # Scroll Area Properties
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        size_policy.setHorizontalStretch(1)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setWidgetResizable(True)
        self.setFixedHeight(1000)

    def add_node_to_view(self, node: ColonyNodeView, x_coordinate: int, y_coordinate: int) -> None:
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        self.addScrollBarWidget(node, Qt.AlignTop)
        # self.setMinimumSize(1200, 1200)
        self.layout.addWidget(node, x_coordinate, y_coordinate)
        # node.hide_node()
