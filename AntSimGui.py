import sys

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel

from ColonyNodeView2 import ColonyNodeView2
from ColonyView2 import ColonyView2
from DegradationEvent import DegradationEvent
from SimulationEvent import SimulationEventType, SimulationEvent


class AntSimGui(QMainWindow):
    def __init__(self):
        super(AntSimGui, self).__init__()
        self.simulation_event_listeners = []
        self.degradation_event_listeners = []
        self.colony_view = None

    def __iadd__(self, listener):
        """Shortcut for using += to add a listener."""
        self.simulation_event_listeners.append(listener)
        return self

    def register_degradation_event_listener(self, listener):
        self.degradation_event_listeners.append(listener)
        return self

    def init_ui(self):
        # Main window setup
        self.setObjectName("MainWindow")
        self.resize(1920, 1080)
        self.setWindowOpacity(31.0)
        self.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.setAnimated(True)
        self.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)

        # Build main layout
        self.mainVerticalLayout = QtWidgets.QVBoxLayout()
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")

        # Build button layout
        self.horizontalMenuBarLayout = QtWidgets.QHBoxLayout()
        self.horizontalMenuBarLayout.setObjectName("horizontalMenuBarLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalMenuBarLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalMenuBarLayout.addItem(spacerItem2)
        self.normalSetupBtn = QtWidgets.QPushButton(self.centralwidget)
        self.normalSetupBtn.setObjectName("normalSetupBtn")
        self.normalSetupBtn.clicked.connect(self.button_pushed_event)
        self.horizontalMenuBarLayout.addWidget(self.normalSetupBtn)

        self.queenTestBtn = QtWidgets.QPushButton(self.centralwidget)
        self.queenTestBtn.setObjectName("queenTestBtn")
        self.queenTestBtn.clicked.connect(self.button_pushed_event)
        self.horizontalMenuBarLayout.addWidget(self.queenTestBtn)

        self.scoutTestBtn = QtWidgets.QPushButton(self.centralwidget)
        self.scoutTestBtn.setObjectName("scoutTestBtn")
        self.scoutTestBtn.clicked.connect(self.button_pushed_event)
        self.horizontalMenuBarLayout.addWidget(self.scoutTestBtn)

        self.foragerTestBtn = QtWidgets.QPushButton(self.centralwidget)
        self.foragerTestBtn.setObjectName("foragerTestBtn")
        self.foragerTestBtn.clicked.connect(self.button_pushed_event)
        self.horizontalMenuBarLayout.addWidget(self.foragerTestBtn)

        self.soldierTestBtn = QtWidgets.QPushButton(self.centralwidget)
        self.soldierTestBtn.setObjectName("soldierTestBtn")
        self.soldierTestBtn.clicked.connect(self.button_pushed_event)
        self.horizontalMenuBarLayout.addWidget(self.soldierTestBtn)

        self.runBtn = QtWidgets.QPushButton(self.centralwidget)
        self.runBtn.setObjectName("runBtn")
        self.runBtn.clicked.connect(self.button_pushed_event)
        self.horizontalMenuBarLayout.addWidget(self.runBtn)

        self.stepBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stepBtn.setObjectName("stepBtn")
        self.stepBtn.clicked.connect(self.button_pushed_event)
        self.horizontalMenuBarLayout.addWidget(self.stepBtn)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalMenuBarLayout.addItem(spacerItem3)
        self.timeLabel = QtWidgets.QLabel(self.centralwidget)
        self.timeLabel.setObjectName("timeLabel")
        self.horizontalMenuBarLayout.addWidget(self.timeLabel)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalMenuBarLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalMenuBarLayout.addItem(spacerItem5)
        self.mainVerticalLayout.addLayout(self.horizontalMenuBarLayout)
        self.gridLayout.addLayout(self.mainVerticalLayout, 0, 0, 1, 1)

        # Build Scroll Area
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(16777213, 16777215))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1894, 937))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 22))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    # def add_colony_node_view(self, colony_node_view: ColonyNodeView2, x: int, y: int):
    #     self.gridLayout_2.addWidget(colony_node_view, x, y)

    def set_colony_view(self, colony_view: ColonyView2):
        self.colony_view = colony_view

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.normalSetupBtn.setText(_translate("MainWindow", "Normal Setup"))
        self.queenTestBtn.setText(_translate("MainWindow", "Queen Test"))
        self.scoutTestBtn.setText(_translate("MainWindow", "Scout Test"))
        self.foragerTestBtn.setText(_translate("MainWindow", "Forager Test"))
        self.soldierTestBtn.setText(_translate("MainWindow", "Soldier Test"))
        self.runBtn.setText(_translate("MainWindow", "Run"))
        self.stepBtn.setText(_translate("MainWindow", "Step"))
        self.timeLabel.setText(_translate("MainWindow", "Day 0, Turn 0"))

    def button_pushed_event(self):
        if self.sender() == self.normalSetupBtn:
            self.fire_simulation_event(SimulationEventType.NORMAL_SETUP_EVENT)
        elif self.sender() == self.queenTestBtn:
            self.fire_simulation_event(SimulationEventType.QUEEN_TEST_EVENT)
        elif self.sender() == self.scoutTestBtn:
            self.fire_simulation_event(SimulationEventType.SCOUT_TEST_EVENT)
        elif self.sender() == self.foragerTestBtn:
            self.fire_simulation_event(SimulationEventType.FORAGER_TEST_EVENT)
        elif self.sender() == self.soldierTestBtn:
            self.fire_simulation_event(SimulationEventType.SOLDIER_TEST_EVENT)
        elif self.sender() == self.runBtn:
            self.fire_simulation_event(SimulationEventType.RUN_EVENT)
        elif self.sender() == self.stepBtn:
            self.fire_simulation_event(SimulationEventType.STEP_EVENT)

    def fire_simulation_event(self, simulation_event_type: SimulationEventType) -> None:
        simulation_event = SimulationEvent(simulation_event_type)
        simulation_event.listeners = self.simulation_event_listeners
        simulation_event.notify(simulation_event_type)

    def fire_degradation_event(self, current_turn_count: int) -> None:
        degradation_event = DegradationEvent(current_turn_count)
        degradation_event.listeners = self.degradation_event_listeners
        degradation_event.notify(current_turn_count)


# app = QApplication(sys.argv)
# window = QMainWindow()
# ui = AntSimGui()
# ui.init_ui(window)

# for x in range(27):
#     row = []
#     for y in range(27):
#         colony_node_view = ColonyNodeView2(ui.scrollAreaWidgetContents, x, y)
#         ui.gridLayout_2.addWidget(colony_node_view, x, y)
#         if x in range(12, 15) and y in range(12, 15):
#             colony_node_view.show()
#         else:
#             colony_node_view.hide()
# window.show()
# app.exec()