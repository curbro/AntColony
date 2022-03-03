import string

from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QFrame, QWidget, QSizePolicy, QStyle

from ColorConstants import QUEEN_NODE_COLOR, OPEN_NODE_COLOR, PHEROMONE_1000, PHEROMONE_800, PHEROMONE_600, \
    PHEROMONE_400, PHEROMONE_200, PHEROMONE_0


class ColonyNodeView2(QFrame):
    def __init__(self, parent: QWidget):
        super(ColonyNodeView2, self).__init__()
        self.hover_text = None
        self.setParent(parent)
        self.palette = self.palette()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        self.setStyleSheet("QLabel { color: black; }")
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setRetainSizeWhenHidden(True)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(96, 96))
        self.setMaximumSize(QtCore.QSize(96, 96))
        self.setFixedSize(96, 96)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 166, 44))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 166, 44))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 166, 44))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 166, 44))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.setFont(font)
        self.setAcceptDrops(False)
        self.setToolTipDuration(-2)
        self.setAutoFillBackground(True)
        self.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.setLineWidth(1)
        self.setMidLineWidth(0)
        self.setObjectName("colonyNodeView")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName("mainLayout")
        self.labelWidget = QWidget(self)
        self.labelLayout = QtWidgets.QVBoxLayout()
        self.labelLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.labelLayout.setObjectName("labelLayout")
        self.labelLayout.setSpacing(0)
        self.idLabel = QtWidgets.QLabel(self)
        self.idLabel.setObjectName("idLabel")
        self.labelLayout.addWidget(self.idLabel)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.labelLayout.addItem(spacerItem6)
        self.foragerLabel = QtWidgets.QLabel(self)
        self.foragerLabel.setObjectName("foragerLabel")
        self.labelLayout.addWidget(self.foragerLabel)
        self.scoutLabel = QtWidgets.QLabel(self)
        self.scoutLabel.setObjectName("scoutLabel")
        self.labelLayout.addWidget(self.scoutLabel)
        self.soldierLabel = QtWidgets.QLabel(self)
        self.soldierLabel.setObjectName("soldierLabel")
        self.labelLayout.addWidget(self.soldierLabel)
        self.balaLabel = QtWidgets.QLabel(self)
        self.balaLabel.setEnabled(True)
        self.balaLabel.setLineWidth(1)
        self.balaLabel.setScaledContents(False)
        self.balaLabel.setObjectName("balaLabel")
        self.labelLayout.addWidget(self.balaLabel)
        self.foodLabel = QtWidgets.QLabel(self)
        self.foodLabel.setObjectName("foodLabel")
        # self.foodLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.labelLayout.addWidget(self.foodLabel)
        self.pheromoneLabel = QtWidgets.QLabel(self)
        self.pheromoneLabel.setObjectName("pheromoneLabel")
        self.labelLayout.addWidget(self.pheromoneLabel)
        self.mainLayout.addLayout(self.labelLayout)
        self.horizontalLayout_3.addLayout(self.mainLayout)

        self.iconLayout = QtWidgets.QVBoxLayout()
        self.iconLayout.setObjectName("iconLayout")
        self.iconLayout.setSpacing(0)
        self.queenIcon = QtWidgets.QLabel(self)
        self.queenIcon.setText("")
        self.queenIcon.setPixmap(
            QtGui.QPixmap("/Users/curtisbrown/Desktop/../PycharmProjects/AntConlonySimulatorGUI/resources/queen.gif"))
        self.queenIcon.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.queenIcon.setWordWrap(False)
        self.queenIcon.setObjectName("queenIcon")
        self.iconLayout.addWidget(self.queenIcon)
        self.foragerIcon = QtWidgets.QLabel(self)
        self.foragerIcon.setText("")
        self.foragerIcon.setPixmap(
            QtGui.QPixmap("/Users/curtisbrown/Desktop/../PycharmProjects/AntConlonySimulatorGUI/resources/forager.gif"))
        self.foragerIcon.setObjectName("foragerIcon")
        self.iconLayout.addWidget(self.foragerIcon)
        self.scoutIcon = QtWidgets.QLabel(self)
        self.scoutIcon.setText("")
        self.scoutIcon.setPixmap(
            QtGui.QPixmap("/Users/curtisbrown/Desktop/../PycharmProjects/AntConlonySimulatorGUI/resources/scout.gif"))
        self.scoutIcon.setObjectName("scoutIcon")
        self.iconLayout.addWidget(self.scoutIcon)
        self.soldierIcon = QtWidgets.QLabel(self)
        self.soldierIcon.setText("")
        self.soldierIcon.setPixmap(
            QtGui.QPixmap("/Users/curtisbrown/Desktop/../PycharmProjects/AntConlonySimulatorGUI/resources/soldier.gif"))
        self.soldierIcon.setObjectName("soldierIcon")
        self.iconLayout.addWidget(self.soldierIcon)
        self.balaIcon = QtWidgets.QLabel(self)
        self.balaIcon.setText("")
        self.balaIcon.setPixmap(
            QtGui.QPixmap("/Users/curtisbrown/Desktop/../PycharmProjects/AntConlonySimulatorGUI/resources/bala.gif"))
        self.balaIcon.setObjectName("balaIcon")
        self.iconLayout.addWidget(self.balaIcon)
        self.mainLayout.addLayout(self.iconLayout)

        self.set_queen(False)
        self.foragerLabel.setText("F")
        self.set_forager_count(0)
        self.scoutLabel.setText("Sc")
        self.set_scout_count(0)
        self.soldierLabel.setText("S")
        self.set_soldier_count(0)
        self.balaLabel.setText("B")
        self.set_bala_count(0)
        self.foodLabel.setText("Food:")
        self.set_food_count(0)
        self.pheromoneLabel.setText("Ph:")
        self.set_pheromone_count(0)
        self.setVisible(False)

    def show_node(self):
        self.setVisible(True)

    def hide_node(self):
        self.setVisible(False)

    def set_id(self, id: string) -> None:
        self.idLabel.setText(id)

    def set_queen(self, is_queen_present: bool) -> None:
        self.is_queen_present = is_queen_present
        if is_queen_present:
            self.palette.setColor(QPalette.Window, QUEEN_NODE_COLOR)
            self.show_queen()
        else:
            self.palette.setColor(QPalette.Window, OPEN_NODE_COLOR)
            self.hide_queen()
        self.setPalette(self.palette)

    def show_queen(self):
        self.queenIcon.show()

    def hide_queen(self):
        self.queenIcon.hide()

    def set_forager_count(self, forager_count: int) -> None:
        self.foragerLabel.setText("F: " + str(forager_count))
        if forager_count > 0:
            self.show_forager()
        else:
            self.hide_forager()

    def show_forager(self):
        self.foragerIcon.show()

    def hide_forager(self):
        self.foragerIcon.hide()

    def set_scout_count(self, scout_count: int) -> None:
        self.scoutLabel.setText("Sc: " + str(scout_count))
        if scout_count > 0:
            self.show_scout()
        else:
            self.hide_scout()

    def show_scout(self):
        self.scoutIcon.show()

    def hide_scout(self):
        self.scoutIcon.hide()

    def set_soldier_count(self, soldier_count: int) -> None:
        self.soldierLabel.setText("S: " + str(soldier_count))
        if soldier_count > 0:
            self.show_soldier()
        else:
            self.hide_soldier()

    def show_soldier(self):
        self.soldierIcon.show()

    def hide_soldier(self):
        self.soldierIcon.hide()

    def set_bala_count(self, bala_count: int) -> None:
        self.balaLabel.setText("B: " + str(bala_count))
        if bala_count > 0:
            self.show_bala()
        else:
            self.hide_bala()

    def show_bala(self):
        self.balaIcon.show()

    def hide_bala(self):
        self.balaIcon.hide()

    def set_food_count(self, food_count: int) -> None:
        self.foodLabel.setText("Food: " + str(food_count))

    def set_pheromone_count(self, pheromone_count: int) -> None:
        self.pheromoneLabel.setText("Ph: " + str(pheromone_count))

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