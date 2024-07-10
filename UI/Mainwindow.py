# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QProgressBar,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QStatusBar,
    QTabWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1060, 814)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setTabPosition(QTabWidget.TabPosition.North)
        self.plot_tab = QWidget()
        self.plot_tab.setObjectName(u"plot_tab")
        self.horizontalLayout_9 = QHBoxLayout(self.plot_tab)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.graphWidget = PlotWidget(self.plot_tab)
        self.graphWidget.setObjectName(u"graphWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphWidget.sizePolicy().hasHeightForWidth())
        self.graphWidget.setSizePolicy(sizePolicy)

        self.verticalLayout_11.addWidget(self.graphWidget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.plotClearButton = QPushButton(self.plot_tab)
        self.plotClearButton.setObjectName(u"plotClearButton")

        self.horizontalLayout_2.addWidget(self.plotClearButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.quickSaveButton = QPushButton(self.plot_tab)
        self.quickSaveButton.setObjectName(u"quickSaveButton")

        self.horizontalLayout_2.addWidget(self.quickSaveButton)

        self.saveAsButton = QPushButton(self.plot_tab)
        self.saveAsButton.setObjectName(u"saveAsButton")

        self.horizontalLayout_2.addWidget(self.saveAsButton)


        self.verticalLayout_11.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_9.addLayout(self.verticalLayout_11)

        self.tabWidget_2.addTab(self.plot_tab, "")
        self.devices_tab = QWidget()
        self.devices_tab.setObjectName(u"devices_tab")
        self.horizontalLayout = QHBoxLayout(self.devices_tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.deviceTree = QTreeWidget(self.devices_tab)
        self.deviceTree.setObjectName(u"deviceTree")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.deviceTree.sizePolicy().hasHeightForWidth())
        self.deviceTree.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.deviceTree)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.tabWidget_2.addTab(self.devices_tab, "")
        self.settingsTab = QWidget()
        self.settingsTab.setObjectName(u"settingsTab")
        self.verticalLayout_10 = QVBoxLayout(self.settingsTab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.deviceSelectionTree = QTreeWidget(self.settingsTab)
        self.deviceSelectionTree.setObjectName(u"deviceSelectionTree")
        self.deviceSelectionTree.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout_4.addWidget(self.deviceSelectionTree)

        self.settingsStack = QStackedWidget(self.settingsTab)
        self.settingsStack.setObjectName(u"settingsStack")
        self.placeholderPage = QWidget()
        self.placeholderPage.setObjectName(u"placeholderPage")
        self.verticalLayout_6 = QVBoxLayout(self.placeholderPage)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.placeholderPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_7)

        self.settingsStack.addWidget(self.placeholderPage)
        self.genericLockInPage = QWidget()
        self.genericLockInPage.setObjectName(u"genericLockInPage")
        self.verticalLayout_3 = QVBoxLayout(self.genericLockInPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.genericLockInPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 806, 528))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy2)
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.genericLockInFreqBox = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.genericLockInFreqBox.setObjectName(u"genericLockInFreqBox")
        self.genericLockInFreqBox.setDecimals(3)
        self.genericLockInFreqBox.setMaximum(10000.000000000000000)
        self.genericLockInFreqBox.setSingleStep(1.000000000000000)
        self.genericLockInFreqBox.setValue(1.000000000000000)

        self.horizontalLayout_3.addWidget(self.genericLockInFreqBox)

        self.genericLockInFreqPrefix = QComboBox(self.scrollAreaWidgetContents)
        self.genericLockInFreqPrefix.addItem("")
        self.genericLockInFreqPrefix.addItem("")
        self.genericLockInFreqPrefix.addItem("")
        self.genericLockInFreqPrefix.addItem("")
        self.genericLockInFreqPrefix.setObjectName(u"genericLockInFreqPrefix")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.genericLockInFreqPrefix.sizePolicy().hasHeightForWidth())
        self.genericLockInFreqPrefix.setSizePolicy(sizePolicy4)
        self.genericLockInFreqPrefix.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.genericLockInFreqPrefix)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.genericLockInRandomButton = QPushButton(self.scrollAreaWidgetContents)
        self.genericLockInRandomButton.setObjectName(u"genericLockInRandomButton")

        self.verticalLayout_5.addWidget(self.genericLockInRandomButton)


        self.formLayout.setLayout(1, QFormLayout.FieldRole, self.verticalLayout_5)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.genericLockInAmp = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.genericLockInAmp.setObjectName(u"genericLockInAmp")
        self.genericLockInAmp.setDecimals(3)
        self.genericLockInAmp.setMinimum(0.005000000000000)
        self.genericLockInAmp.setMaximum(4.999000000000000)
        self.genericLockInAmp.setSingleStep(0.010000000000000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.genericLockInAmp)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.genericLockInPhase = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.genericLockInPhase.setObjectName(u"genericLockInPhase")
        self.genericLockInPhase.setDecimals(3)
        self.genericLockInPhase.setMinimum(-359.999000000000024)
        self.genericLockInPhase.setMaximum(729.980000000000018)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.genericLockInPhase)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.genericLockInTau = QComboBox(self.scrollAreaWidgetContents)
        self.genericLockInTau.setObjectName(u"genericLockInTau")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.genericLockInTau)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_6)

        self.genericLockInSens = QComboBox(self.scrollAreaWidgetContents)
        self.genericLockInSens.setObjectName(u"genericLockInSens")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.genericLockInSens)

        self.label_10 = QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_10)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.genericLockInDisp1 = QComboBox(self.scrollAreaWidgetContents)
        self.genericLockInDisp1.setObjectName(u"genericLockInDisp1")

        self.horizontalLayout_6.addWidget(self.genericLockInDisp1)

        self.genericLockInDisp2 = QComboBox(self.scrollAreaWidgetContents)
        self.genericLockInDisp2.setObjectName(u"genericLockInDisp2")

        self.horizontalLayout_6.addWidget(self.genericLockInDisp2)


        self.formLayout.setLayout(9, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.label_11 = QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_11)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.genericLockInAqOne = QRadioButton(self.scrollAreaWidgetContents)
        self.genericLockInAqOne.setObjectName(u"genericLockInAqOne")

        self.horizontalLayout_7.addWidget(self.genericLockInAqOne)

        self.genericLockInAqCont = QRadioButton(self.scrollAreaWidgetContents)
        self.genericLockInAqCont.setObjectName(u"genericLockInAqCont")

        self.horizontalLayout_7.addWidget(self.genericLockInAqCont)


        self.formLayout.setLayout(10, QFormLayout.FieldRole, self.horizontalLayout_7)

        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_12)

        self.genericLockInMeasurementFreq = QComboBox(self.scrollAreaWidgetContents)
        self.genericLockInMeasurementFreq.setObjectName(u"genericLockInMeasurementFreq")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.genericLockInMeasurementFreq)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(12, QFormLayout.LabelRole, self.verticalSpacer)

        self.label_14 = QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_14)

        self.label_13 = QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.label_13)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.genericLockInApplyButton = QPushButton(self.genericLockInPage)
        self.genericLockInApplyButton.setObjectName(u"genericLockInApplyButton")

        self.verticalLayout_9.addWidget(self.genericLockInApplyButton)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.genericLockInTriggerButton = QPushButton(self.genericLockInPage)
        self.genericLockInTriggerButton.setObjectName(u"genericLockInTriggerButton")

        self.horizontalLayout_8.addWidget(self.genericLockInTriggerButton)

        self.genericLockInBufferReadButton = QPushButton(self.genericLockInPage)
        self.genericLockInBufferReadButton.setObjectName(u"genericLockInBufferReadButton")

        self.horizontalLayout_8.addWidget(self.genericLockInBufferReadButton)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)


        self.verticalLayout_3.addLayout(self.verticalLayout_9)

        self.settingsStack.addWidget(self.genericLockInPage)
        self.sweeperPage = QWidget()
        self.sweeperPage.setObjectName(u"sweeperPage")
        self.verticalLayout_7 = QVBoxLayout(self.sweeperPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.scrollArea_2 = QScrollArea(self.sweeperPage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 270, 124))
        self.formLayout_2 = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.radioButton = QRadioButton(self.scrollAreaWidgetContents_2)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_8.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.scrollAreaWidgetContents_2)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_8.addWidget(self.radioButton_2)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_8)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea_2)

        self.pushButton = QPushButton(self.sweeperPage)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_7.addWidget(self.pushButton)

        self.settingsStack.addWidget(self.sweeperPage)

        self.horizontalLayout_4.addWidget(self.settingsStack)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.tabWidget_2.addTab(self.settingsTab, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_5 = QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.expList = QListWidget(self.tab)
        QListWidgetItem(self.expList)
        QListWidgetItem(self.expList)
        QListWidgetItem(self.expList)
        self.expList.setObjectName(u"expList")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.expList.sizePolicy().hasHeightForWidth())
        self.expList.setSizePolicy(sizePolicy5)
        self.expList.setMinimumSize(QSize(150, 0))
        self.expList.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_5.addWidget(self.expList)

        self.expStack = QStackedWidget(self.tab)
        self.expStack.setObjectName(u"expStack")
        self.expPlaceholder = QWidget()
        self.expPlaceholder.setObjectName(u"expPlaceholder")
        self.horizontalLayout_10 = QHBoxLayout(self.expPlaceholder)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_15 = QLabel(self.expPlaceholder)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_15)

        self.expStack.addWidget(self.expPlaceholder)
        self.expSweepAndLockIn = QWidget()
        self.expSweepAndLockIn.setObjectName(u"expSweepAndLockIn")
        self.verticalLayout_4 = QVBoxLayout(self.expSweepAndLockIn)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea_3 = QScrollArea(self.expSweepAndLockIn)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 858, 503))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sweepAndLockPower = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.sweepAndLockPower.setObjectName(u"sweepAndLockPower")
        self.sweepAndLockPower.setMinimum(-80.000000000000000)
        self.sweepAndLockPower.setMaximum(20.000000000000000)

        self.gridLayout.addWidget(self.sweepAndLockPower, 8, 1, 1, 1)

        self.label_28 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout.addWidget(self.label_28, 13, 0, 1, 1)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 6, 0, 1, 1)

        self.sweepAndLockFreq = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.sweepAndLockFreq.setObjectName(u"sweepAndLockFreq")
        self.sweepAndLockFreq.setDecimals(1)
        self.sweepAndLockFreq.setMaximum(100000.000000000000000)

        self.gridLayout.addWidget(self.sweepAndLockFreq, 3, 1, 1, 1)

        self.label_24 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 13, 2, 1, 1)

        self.line_12 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_12, 11, 0, 1, 1)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 1, 0, 1, 1)

        self.sweepAndLockDataPointsLabel = QLabel(self.scrollAreaWidgetContents_3)
        self.sweepAndLockDataPointsLabel.setObjectName(u"sweepAndLockDataPointsLabel")

        self.gridLayout.addWidget(self.sweepAndLockDataPointsLabel, 13, 3, 1, 1)

        self.sweepAndLockTau = QComboBox(self.scrollAreaWidgetContents_3)
        self.sweepAndLockTau.setObjectName(u"sweepAndLockTau")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.sweepAndLockTau.sizePolicy().hasHeightForWidth())
        self.sweepAndLockTau.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.sweepAndLockTau, 2, 3, 1, 1)

        self.sweepAndLockSampleFreq = QComboBox(self.scrollAreaWidgetContents_3)
        self.sweepAndLockSampleFreq.setObjectName(u"sweepAndLockSampleFreq")

        self.gridLayout.addWidget(self.sweepAndLockSampleFreq, 3, 3, 1, 1)

        self.sweepAndLockSelectLockIn = QComboBox(self.scrollAreaWidgetContents_3)
        self.sweepAndLockSelectLockIn.setObjectName(u"sweepAndLockSelectLockIn")
        sizePolicy6.setHeightForWidth(self.sweepAndLockSelectLockIn.sizePolicy().hasHeightForWidth())
        self.sweepAndLockSelectLockIn.setSizePolicy(sizePolicy6)

        self.gridLayout.addWidget(self.sweepAndLockSelectLockIn, 1, 1, 1, 1)

        self.line_4 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_4, 5, 2, 1, 1)

        self.line_2 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 5, 3, 1, 1)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 2, 0, 1, 1)

        self.line = QFrame(self.scrollAreaWidgetContents_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 5, 1, 1, 1)

        self.sweepAndLockSweepTime = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.sweepAndLockSweepTime.setObjectName(u"sweepAndLockSweepTime")
        self.sweepAndLockSweepTime.setDecimals(3)

        self.gridLayout.addWidget(self.sweepAndLockSweepTime, 8, 3, 1, 1)

        self.label_26 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout.addWidget(self.label_26, 2, 2, 1, 1)

        self.line_9 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_9, 11, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 14, 0, 1, 1)

        self.sweepAndLockNumRuns = QSpinBox(self.scrollAreaWidgetContents_3)
        self.sweepAndLockNumRuns.setObjectName(u"sweepAndLockNumRuns")
        self.sweepAndLockNumRuns.setMinimum(1)
        self.sweepAndLockNumRuns.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.sweepAndLockNumRuns, 13, 1, 1, 1)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 7, 2, 1, 1)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 8, 2, 1, 1)

        self.line_10 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_10, 11, 3, 1, 1)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout.addWidget(self.label_25, 3, 0, 1, 1)

        self.label_19 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 7, 0, 1, 1)

        self.sweepAndLockEndFreq = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.sweepAndLockEndFreq.setObjectName(u"sweepAndLockEndFreq")
        self.sweepAndLockEndFreq.setDecimals(6)
        self.sweepAndLockEndFreq.setMinimum(2.000000000000000)
        self.sweepAndLockEndFreq.setMaximum(20.000000000000000)

        self.gridLayout.addWidget(self.sweepAndLockEndFreq, 7, 3, 1, 1)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout.addWidget(self.label_27, 8, 0, 1, 1)

        self.sweepAndLockSelectSweeper = QComboBox(self.scrollAreaWidgetContents_3)
        self.sweepAndLockSelectSweeper.setObjectName(u"sweepAndLockSelectSweeper")
        sizePolicy6.setHeightForWidth(self.sweepAndLockSelectSweeper.sizePolicy().hasHeightForWidth())
        self.sweepAndLockSelectSweeper.setSizePolicy(sizePolicy6)
        self.sweepAndLockSelectSweeper.setEditable(False)

        self.gridLayout.addWidget(self.sweepAndLockSelectSweeper, 6, 1, 1, 1)

        self.line_11 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_11, 11, 2, 1, 1)

        self.label_21 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 3, 2, 1, 1)

        self.line_3 = QFrame(self.scrollAreaWidgetContents_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 5, 0, 1, 1)

        self.sweepAndLockStartFreq = QDoubleSpinBox(self.scrollAreaWidgetContents_3)
        self.sweepAndLockStartFreq.setObjectName(u"sweepAndLockStartFreq")
        self.sweepAndLockStartFreq.setDecimals(6)
        self.sweepAndLockStartFreq.setMinimum(2.000000000000000)
        self.sweepAndLockStartFreq.setMaximum(20.000000000000000)
        self.sweepAndLockStartFreq.setValue(2.000000000000000)

        self.gridLayout.addWidget(self.sweepAndLockStartFreq, 7, 1, 1, 1)

        self.sweepAndLockSens = QComboBox(self.scrollAreaWidgetContents_3)
        self.sweepAndLockSens.setObjectName(u"sweepAndLockSens")

        self.gridLayout.addWidget(self.sweepAndLockSens, 2, 1, 1, 1)

        self.label_22 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 4, 0, 1, 1)

        self.label_29 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout.addWidget(self.label_29, 4, 2, 1, 1)

        self.sweepAndLockDIsp1 = QComboBox(self.scrollAreaWidgetContents_3)
        self.sweepAndLockDIsp1.setObjectName(u"sweepAndLockDIsp1")

        self.gridLayout.addWidget(self.sweepAndLockDIsp1, 4, 1, 1, 1)

        self.SweepAndLockDisp2 = QComboBox(self.scrollAreaWidgetContents_3)
        self.SweepAndLockDisp2.setObjectName(u"SweepAndLockDisp2")

        self.gridLayout.addWidget(self.SweepAndLockDisp2, 4, 3, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_4.addWidget(self.scrollArea_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.sweepAndLockStart = QPushButton(self.expSweepAndLockIn)
        self.sweepAndLockStart.setObjectName(u"sweepAndLockStart")
        sizePolicy6.setHeightForWidth(self.sweepAndLockStart.sizePolicy().hasHeightForWidth())
        self.sweepAndLockStart.setSizePolicy(sizePolicy6)

        self.horizontalLayout_11.addWidget(self.sweepAndLockStart)

        self.sweepAndLockCancel = QPushButton(self.expSweepAndLockIn)
        self.sweepAndLockCancel.setObjectName(u"sweepAndLockCancel")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.sweepAndLockCancel.sizePolicy().hasHeightForWidth())
        self.sweepAndLockCancel.setSizePolicy(sizePolicy7)

        self.horizontalLayout_11.addWidget(self.sweepAndLockCancel)

        self.sweepAndLockExport = QPushButton(self.expSweepAndLockIn)
        self.sweepAndLockExport.setObjectName(u"sweepAndLockExport")
        sizePolicy7.setHeightForWidth(self.sweepAndLockExport.sizePolicy().hasHeightForWidth())
        self.sweepAndLockExport.setSizePolicy(sizePolicy7)

        self.horizontalLayout_11.addWidget(self.sweepAndLockExport)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.sweepAndLockProgress = QProgressBar(self.expSweepAndLockIn)
        self.sweepAndLockProgress.setObjectName(u"sweepAndLockProgress")
        self.sweepAndLockProgress.setMaximum(100)
        self.sweepAndLockProgress.setValue(3)
        self.sweepAndLockProgress.setTextVisible(False)
        self.sweepAndLockProgress.setInvertedAppearance(False)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.sweepAndLockProgress)

        self.sweepAndLockTotalProgress = QProgressBar(self.expSweepAndLockIn)
        self.sweepAndLockTotalProgress.setObjectName(u"sweepAndLockTotalProgress")
        self.sweepAndLockTotalProgress.setValue(24)
        self.sweepAndLockTotalProgress.setTextVisible(False)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.sweepAndLockTotalProgress)

        self.label_49 = QLabel(self.expSweepAndLockIn)
        self.label_49.setObjectName(u"label_49")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_49)

        self.label_50 = QLabel(self.expSweepAndLockIn)
        self.label_50.setObjectName(u"label_50")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_50)


        self.verticalLayout_4.addLayout(self.formLayout_4)

        self.expStack.addWidget(self.expSweepAndLockIn)
        self.expODMRWaterfall = QWidget()
        self.expODMRWaterfall.setObjectName(u"expODMRWaterfall")
        self.verticalLayout_12 = QVBoxLayout(self.expODMRWaterfall)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.scrollArea_4 = QScrollArea(self.expODMRWaterfall)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 837, 585))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ODMRWaterfallDisplay2Radio = QRadioButton(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallDisplay2Radio.setObjectName(u"ODMRWaterfallDisplay2Radio")

        self.gridLayout_2.addWidget(self.ODMRWaterfallDisplay2Radio, 3, 2, 1, 1)

        self.ODMRWaterfallWorstTimeLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallWorstTimeLabel.setObjectName(u"ODMRWaterfallWorstTimeLabel")

        self.gridLayout_2.addWidget(self.ODMRWaterfallWorstTimeLabel, 16, 3, 1, 1)

        self.ODMRWaterfallDisplay2 = QComboBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallDisplay2.setObjectName(u"ODMRWaterfallDisplay2")

        self.gridLayout_2.addWidget(self.ODMRWaterfallDisplay2, 3, 3, 1, 1)

        self.label_45 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_2.addWidget(self.label_45, 15, 0, 1, 1)

        self.line_21 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.Shape.HLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_21, 8, 0, 1, 1)

        self.label_37 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_2.addWidget(self.label_37, 7, 0, 1, 1)

        self.ODMRWaterfallPSUSelection = QComboBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallPSUSelection.setObjectName(u"ODMRWaterfallPSUSelection")

        self.gridLayout_2.addWidget(self.ODMRWaterfallPSUSelection, 9, 1, 1, 1)

        self.label_39 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_2.addWidget(self.label_39, 6, 2, 1, 1)

        self.ODMRWaterfallSweepEnd = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallSweepEnd.setObjectName(u"ODMRWaterfallSweepEnd")
        self.ODMRWaterfallSweepEnd.setDecimals(6)

        self.gridLayout_2.addWidget(self.ODMRWaterfallSweepEnd, 6, 3, 1, 1)

        self.ODMRWaterfallSweepPower = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallSweepPower.setObjectName(u"ODMRWaterfallSweepPower")
        self.ODMRWaterfallSweepPower.setDecimals(1)

        self.gridLayout_2.addWidget(self.ODMRWaterfallSweepPower, 7, 1, 1, 1)

        self.label_40 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_2.addWidget(self.label_40, 9, 0, 1, 1)

        self.line_23 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.Shape.HLine)
        self.line_23.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_23, 8, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 17, 0, 1, 1)

        self.line_26 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.Shape.HLine)
        self.line_26.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_26, 14, 1, 1, 1)

        self.ODMRWaterfallVoltage = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallVoltage.setObjectName(u"ODMRWaterfallVoltage")

        self.gridLayout_2.addWidget(self.ODMRWaterfallVoltage, 11, 3, 1, 1)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_2.addWidget(self.label_30, 1, 0, 1, 1)

        self.ODMRWaterfallLockInSampleRate = QComboBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallLockInSampleRate.setObjectName(u"ODMRWaterfallLockInSampleRate")

        self.gridLayout_2.addWidget(self.ODMRWaterfallLockInSampleRate, 2, 3, 1, 1)

        self.line_17 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_17, 4, 0, 1, 1)

        self.label_42 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_2.addWidget(self.label_42, 11, 0, 1, 1)

        self.ODMRWaterfallExpectedTimeLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallExpectedTimeLabel.setObjectName(u"ODMRWaterfallExpectedTimeLabel")

        self.gridLayout_2.addWidget(self.ODMRWaterfallExpectedTimeLabel, 16, 1, 1, 1)

        self.line_18 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.HLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_18, 4, 1, 1, 1)

        self.ODMRWaterfallLockInSens = QComboBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallLockInSens.setObjectName(u"ODMRWaterfallLockInSens")

        self.gridLayout_2.addWidget(self.ODMRWaterfallLockInSens, 1, 1, 1, 1)

        self.label_53 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_2.addWidget(self.label_53, 12, 0, 1, 1)

        self.line_20 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.Shape.HLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_20, 4, 3, 1, 1)

        self.ODMRWaterfallDisplay1Radio = QRadioButton(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallDisplay1Radio.setObjectName(u"ODMRWaterfallDisplay1Radio")
        self.ODMRWaterfallDisplay1Radio.setChecked(True)

        self.gridLayout_2.addWidget(self.ODMRWaterfallDisplay1Radio, 3, 0, 1, 1)

        self.ODMRWaterfallEndCurrent = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallEndCurrent.setObjectName(u"ODMRWaterfallEndCurrent")
        self.ODMRWaterfallEndCurrent.setDecimals(3)

        self.gridLayout_2.addWidget(self.ODMRWaterfallEndCurrent, 10, 3, 1, 1)

        self.label_31 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_2.addWidget(self.label_31, 0, 0, 1, 1)

        self.line_24 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.Shape.HLine)
        self.line_24.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_24, 8, 3, 1, 1)

        self.label_41 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_2.addWidget(self.label_41, 10, 0, 1, 1)

        self.line_25 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.Shape.HLine)
        self.line_25.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_25, 14, 0, 1, 1)

        self.ODMRWaterfallSweepStart = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallSweepStart.setObjectName(u"ODMRWaterfallSweepStart")
        self.ODMRWaterfallSweepStart.setDecimals(6)

        self.gridLayout_2.addWidget(self.ODMRWaterfallSweepStart, 6, 1, 1, 1)

        self.label_46 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_2.addWidget(self.label_46, 15, 2, 1, 1)

        self.line_19 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.HLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_19, 4, 2, 1, 1)

        self.line_22 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.Shape.HLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_22, 8, 1, 1, 1)

        self.label_38 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_2.addWidget(self.label_38, 7, 2, 1, 1)

        self.ODMRWaterfallTotalResolutionLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallTotalResolutionLabel.setObjectName(u"ODMRWaterfallTotalResolutionLabel")

        self.gridLayout_2.addWidget(self.ODMRWaterfallTotalResolutionLabel, 15, 3, 1, 1)

        self.label_51 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_2.addWidget(self.label_51, 16, 0, 1, 1)

        self.line_28 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.Shape.HLine)
        self.line_28.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_28, 14, 3, 1, 1)

        self.ODMRWaterfallLockInFreq = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallLockInFreq.setObjectName(u"ODMRWaterfallLockInFreq")
        self.ODMRWaterfallLockInFreq.setDecimals(1)
        self.ODMRWaterfallLockInFreq.setMaximum(10000.000000000000000)
        self.ODMRWaterfallLockInFreq.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.gridLayout_2.addWidget(self.ODMRWaterfallLockInFreq, 2, 1, 1, 1)

        self.label_33 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_2.addWidget(self.label_33, 2, 0, 1, 1)

        self.label_44 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_2.addWidget(self.label_44, 11, 2, 1, 1)

        self.line_27 = QFrame(self.scrollAreaWidgetContents_4)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.Shape.HLine)
        self.line_27.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_27, 14, 2, 1, 1)

        self.label_32 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_2.addWidget(self.label_32, 5, 0, 1, 1)

        self.ODMRWaterfallSweepResolutionLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallSweepResolutionLabel.setObjectName(u"ODMRWaterfallSweepResolutionLabel")

        self.gridLayout_2.addWidget(self.ODMRWaterfallSweepResolutionLabel, 15, 1, 1, 1)

        self.label_35 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_2.addWidget(self.label_35, 2, 2, 1, 1)

        self.ODMRWaterfallLockInTau = QComboBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallLockInTau.setObjectName(u"ODMRWaterfallLockInTau")
        sizePolicy6.setHeightForWidth(self.ODMRWaterfallLockInTau.sizePolicy().hasHeightForWidth())
        self.ODMRWaterfallLockInTau.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.ODMRWaterfallLockInTau, 1, 3, 1, 1)

        self.label_54 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_2.addWidget(self.label_54, 12, 2, 1, 1)

        self.ODMRWaterfallPowerSteps = QSpinBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallPowerSteps.setObjectName(u"ODMRWaterfallPowerSteps")
        self.ODMRWaterfallPowerSteps.setMinimum(1)
        self.ODMRWaterfallPowerSteps.setMaximum(10000)
        self.ODMRWaterfallPowerSteps.setValue(2)

        self.gridLayout_2.addWidget(self.ODMRWaterfallPowerSteps, 11, 1, 1, 1)

        self.ODMRWaterfallLockInSelection = QComboBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallLockInSelection.setObjectName(u"ODMRWaterfallLockInSelection")
        sizePolicy6.setHeightForWidth(self.ODMRWaterfallLockInSelection.sizePolicy().hasHeightForWidth())
        self.ODMRWaterfallLockInSelection.setSizePolicy(sizePolicy6)

        self.gridLayout_2.addWidget(self.ODMRWaterfallLockInSelection, 0, 1, 1, 1)

        self.ODMRWaterfallStartCurrent = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallStartCurrent.setObjectName(u"ODMRWaterfallStartCurrent")
        self.ODMRWaterfallStartCurrent.setDecimals(3)

        self.gridLayout_2.addWidget(self.ODMRWaterfallStartCurrent, 10, 1, 1, 1)

        self.label_52 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_2.addWidget(self.label_52, 16, 2, 1, 1)

        self.ODMRWaterfallSweeperSelection = QComboBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallSweeperSelection.setObjectName(u"ODMRWaterfallSweeperSelection")

        self.gridLayout_2.addWidget(self.ODMRWaterfallSweeperSelection, 5, 1, 1, 1)

        self.label_36 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_2.addWidget(self.label_36, 6, 0, 1, 1)

        self.ODMRWaterfallSweepTime = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallSweepTime.setObjectName(u"ODMRWaterfallSweepTime")

        self.gridLayout_2.addWidget(self.ODMRWaterfallSweepTime, 7, 3, 1, 1)

        self.label_43 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_2.addWidget(self.label_43, 10, 2, 1, 1)

        self.ODMRWaterfallDisplay1 = QComboBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallDisplay1.setObjectName(u"ODMRWaterfallDisplay1")

        self.gridLayout_2.addWidget(self.ODMRWaterfallDisplay1, 3, 1, 1, 1)

        self.label_34 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_2.addWidget(self.label_34, 1, 2, 1, 1)

        self.label_55 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_2.addWidget(self.label_55, 13, 0, 1, 1)

        self.label_56 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_2.addWidget(self.label_56, 13, 2, 1, 1)

        self.ODMRWaterfallShutdownInterval = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallShutdownInterval.setObjectName(u"ODMRWaterfallShutdownInterval")
        self.ODMRWaterfallShutdownInterval.setDecimals(3)
        self.ODMRWaterfallShutdownInterval.setMinimum(0.100000000000000)
        self.ODMRWaterfallShutdownInterval.setMaximum(10.000000000000000)
        self.ODMRWaterfallShutdownInterval.setValue(0.200000000000000)

        self.gridLayout_2.addWidget(self.ODMRWaterfallShutdownInterval, 12, 3, 1, 1)

        self.ODMRWaterfallInitialSettleTime = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallInitialSettleTime.setObjectName(u"ODMRWaterfallInitialSettleTime")
        self.ODMRWaterfallInitialSettleTime.setDecimals(3)
        self.ODMRWaterfallInitialSettleTime.setMinimum(0.100000000000000)
        self.ODMRWaterfallInitialSettleTime.setMaximum(100.000000000000000)
        self.ODMRWaterfallInitialSettleTime.setValue(10.000000000000000)

        self.gridLayout_2.addWidget(self.ODMRWaterfallInitialSettleTime, 13, 3, 1, 1)

        self.ODMRWaterfallSettleTime = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallSettleTime.setObjectName(u"ODMRWaterfallSettleTime")
        self.ODMRWaterfallSettleTime.setDecimals(3)
        self.ODMRWaterfallSettleTime.setMinimum(0.100000000000000)
        self.ODMRWaterfallSettleTime.setMaximum(100.000000000000000)
        self.ODMRWaterfallSettleTime.setValue(3.000000000000000)

        self.gridLayout_2.addWidget(self.ODMRWaterfallSettleTime, 13, 1, 1, 1)

        self.ODMRWaterfallShutdownStepSize = QDoubleSpinBox(self.scrollAreaWidgetContents_4)
        self.ODMRWaterfallShutdownStepSize.setObjectName(u"ODMRWaterfallShutdownStepSize")
        self.ODMRWaterfallShutdownStepSize.setDecimals(3)
        self.ODMRWaterfallShutdownStepSize.setMaximum(10.000000000000000)
        self.ODMRWaterfallShutdownStepSize.setValue(0.050000000000000)

        self.gridLayout_2.addWidget(self.ODMRWaterfallShutdownStepSize, 12, 1, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_12.addWidget(self.scrollArea_4)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.ODMRWaterfallStart = QPushButton(self.expODMRWaterfall)
        self.ODMRWaterfallStart.setObjectName(u"ODMRWaterfallStart")
        sizePolicy6.setHeightForWidth(self.ODMRWaterfallStart.sizePolicy().hasHeightForWidth())
        self.ODMRWaterfallStart.setSizePolicy(sizePolicy6)

        self.horizontalLayout_12.addWidget(self.ODMRWaterfallStart)

        self.ODMRWaterfallCancel = QPushButton(self.expODMRWaterfall)
        self.ODMRWaterfallCancel.setObjectName(u"ODMRWaterfallCancel")

        self.horizontalLayout_12.addWidget(self.ODMRWaterfallCancel)

        self.ODMRWaterfallExport = QPushButton(self.expODMRWaterfall)
        self.ODMRWaterfallExport.setObjectName(u"ODMRWaterfallExport")

        self.horizontalLayout_12.addWidget(self.ODMRWaterfallExport)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_47 = QLabel(self.expODMRWaterfall)
        self.label_47.setObjectName(u"label_47")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_47)

        self.ODMRWaterfallSweepProgress = QProgressBar(self.expODMRWaterfall)
        self.ODMRWaterfallSweepProgress.setObjectName(u"ODMRWaterfallSweepProgress")
        self.ODMRWaterfallSweepProgress.setValue(24)
        self.ODMRWaterfallSweepProgress.setTextVisible(False)
        self.ODMRWaterfallSweepProgress.setInvertedAppearance(False)
        self.ODMRWaterfallSweepProgress.setTextDirection(QProgressBar.Direction.TopToBottom)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.ODMRWaterfallSweepProgress)

        self.label_48 = QLabel(self.expODMRWaterfall)
        self.label_48.setObjectName(u"label_48")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_48)

        self.ODMRWaterfallTotalProgress = QProgressBar(self.expODMRWaterfall)
        self.ODMRWaterfallTotalProgress.setObjectName(u"ODMRWaterfallTotalProgress")
        self.ODMRWaterfallTotalProgress.setValue(24)
        self.ODMRWaterfallTotalProgress.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.ODMRWaterfallTotalProgress.setTextVisible(False)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.ODMRWaterfallTotalProgress)


        self.verticalLayout_12.addLayout(self.formLayout_3)

        self.expStack.addWidget(self.expODMRWaterfall)
        self.expStitchedSweep = QWidget()
        self.expStitchedSweep.setObjectName(u"expStitchedSweep")
        self.verticalLayout_13 = QVBoxLayout(self.expStitchedSweep)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scrollArea_5 = QScrollArea(self.expStitchedSweep)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 858, 505))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_64 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_3.addWidget(self.label_64, 7, 0, 1, 1)

        self.label_61 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_3.addWidget(self.label_61, 1, 2, 1, 1)

        self.line_13 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_13, 8, 0, 1, 1)

        self.StitchedSweepDisp1Check = QCheckBox(self.scrollAreaWidgetContents_5)
        self.StitchedSweepDisp1Check.setObjectName(u"StitchedSweepDisp1Check")
        self.StitchedSweepDisp1Check.setChecked(True)

        self.gridLayout_3.addWidget(self.StitchedSweepDisp1Check, 3, 0, 1, 1)

        self.StitchedSweepTau = QComboBox(self.scrollAreaWidgetContents_5)
        self.StitchedSweepTau.setObjectName(u"StitchedSweepTau")
        sizePolicy6.setHeightForWidth(self.StitchedSweepTau.sizePolicy().hasHeightForWidth())
        self.StitchedSweepTau.setSizePolicy(sizePolicy6)

        self.gridLayout_3.addWidget(self.StitchedSweepTau, 1, 3, 1, 1)

        self.line_8 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_8, 4, 3, 1, 1)

        self.label_58 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_3.addWidget(self.label_58, 1, 0, 1, 1)

        self.label_67 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_3.addWidget(self.label_67, 9, 0, 1, 1)

        self.label_65 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_3.addWidget(self.label_65, 6, 2, 1, 1)

        self.comboBox_4 = QComboBox(self.scrollAreaWidgetContents_5)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_3.addWidget(self.comboBox_4, 3, 3, 1, 1)

        self.label_57 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_3.addWidget(self.label_57, 0, 0, 1, 1)

        self.StitchedSweepEndFreq = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.StitchedSweepEndFreq.setObjectName(u"StitchedSweepEndFreq")
        self.StitchedSweepEndFreq.setDecimals(6)

        self.gridLayout_3.addWidget(self.StitchedSweepEndFreq, 6, 3, 1, 1)

        self.line_7 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_7, 4, 2, 1, 1)

        self.comboBox_3 = QComboBox(self.scrollAreaWidgetContents_5)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_3.addWidget(self.comboBox_3, 3, 1, 1, 1)

        self.StitchedSweepNumSweeps = QSpinBox(self.scrollAreaWidgetContents_5)
        self.StitchedSweepNumSweeps.setObjectName(u"StitchedSweepNumSweeps")
        self.StitchedSweepNumSweeps.setMinimum(1)
        self.StitchedSweepNumSweeps.setMaximum(1000)
        self.StitchedSweepNumSweeps.setValue(2)

        self.gridLayout_3.addWidget(self.StitchedSweepNumSweeps, 9, 1, 1, 1)

        self.label_66 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_3.addWidget(self.label_66, 7, 2, 1, 1)

        self.label_60 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_3.addWidget(self.label_60, 5, 0, 1, 1)

        self.StitchedSweepSampleRate = QComboBox(self.scrollAreaWidgetContents_5)
        self.StitchedSweepSampleRate.setObjectName(u"StitchedSweepSampleRate")

        self.gridLayout_3.addWidget(self.StitchedSweepSampleRate, 2, 3, 1, 1)

        self.StitchedSweepSens = QComboBox(self.scrollAreaWidgetContents_5)
        self.StitchedSweepSens.setObjectName(u"StitchedSweepSens")
        sizePolicy6.setHeightForWidth(self.StitchedSweepSens.sizePolicy().hasHeightForWidth())
        self.StitchedSweepSens.setSizePolicy(sizePolicy6)

        self.gridLayout_3.addWidget(self.StitchedSweepSens, 1, 1, 1, 1)

        self.StitchedSweepStartFreq = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.StitchedSweepStartFreq.setObjectName(u"StitchedSweepStartFreq")
        self.StitchedSweepStartFreq.setDecimals(6)

        self.gridLayout_3.addWidget(self.StitchedSweepStartFreq, 6, 1, 1, 1)

        self.label_62 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_3.addWidget(self.label_62, 2, 2, 1, 1)

        self.StitchedSweepDisp2Check = QCheckBox(self.scrollAreaWidgetContents_5)
        self.StitchedSweepDisp2Check.setObjectName(u"StitchedSweepDisp2Check")

        self.gridLayout_3.addWidget(self.StitchedSweepDisp2Check, 3, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 11, 0, 1, 1)

        self.StitchedSweepSweepTime = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.StitchedSweepSweepTime.setObjectName(u"StitchedSweepSweepTime")

        self.gridLayout_3.addWidget(self.StitchedSweepSweepTime, 7, 3, 1, 1)

        self.StitchedSweepSweeperSelection = QComboBox(self.scrollAreaWidgetContents_5)
        self.StitchedSweepSweeperSelection.setObjectName(u"StitchedSweepSweeperSelection")

        self.gridLayout_3.addWidget(self.StitchedSweepSweeperSelection, 5, 1, 1, 1)

        self.label_59 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_3.addWidget(self.label_59, 2, 0, 1, 1)

        self.StitchedSweepTotalTimeLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.StitchedSweepTotalTimeLabel.setObjectName(u"StitchedSweepTotalTimeLabel")

        self.gridLayout_3.addWidget(self.StitchedSweepTotalTimeLabel, 9, 3, 1, 1)

        self.StitchedSweepLockInFreq = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.StitchedSweepLockInFreq.setObjectName(u"StitchedSweepLockInFreq")
        self.StitchedSweepLockInFreq.setDecimals(1)
        self.StitchedSweepLockInFreq.setMaximum(100000.000000000000000)

        self.gridLayout_3.addWidget(self.StitchedSweepLockInFreq, 2, 1, 1, 1)

        self.StitchedSweepPower = QDoubleSpinBox(self.scrollAreaWidgetContents_5)
        self.StitchedSweepPower.setObjectName(u"StitchedSweepPower")

        self.gridLayout_3.addWidget(self.StitchedSweepPower, 7, 1, 1, 1)

        self.line_5 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 4, 0, 1, 1)

        self.line_15 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.Shape.HLine)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_15, 8, 2, 1, 1)

        self.label_68 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_3.addWidget(self.label_68, 9, 2, 1, 1)

        self.StitchedSweepLockInSelection = QComboBox(self.scrollAreaWidgetContents_5)
        self.StitchedSweepLockInSelection.setObjectName(u"StitchedSweepLockInSelection")

        self.gridLayout_3.addWidget(self.StitchedSweepLockInSelection, 0, 1, 1, 1)

        self.line_16 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_16, 8, 3, 1, 1)

        self.line_14 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_14, 8, 1, 1, 1)

        self.label_63 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_3.addWidget(self.label_63, 6, 0, 1, 1)

        self.line_6 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_6, 4, 1, 1, 1)

        self.label_69 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_3.addWidget(self.label_69, 10, 0, 1, 1)

        self.label_70 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_3.addWidget(self.label_70, 10, 1, 1, 1)

        self.label_71 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_3.addWidget(self.label_71, 10, 2, 1, 1)

        self.StitchedSweepTotalPointsLabel = QLabel(self.scrollAreaWidgetContents_5)
        self.StitchedSweepTotalPointsLabel.setObjectName(u"StitchedSweepTotalPointsLabel")

        self.gridLayout_3.addWidget(self.StitchedSweepTotalPointsLabel, 10, 3, 1, 1)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_13.addWidget(self.scrollArea_5)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.StitchedSweepStartButton = QPushButton(self.expStitchedSweep)
        self.StitchedSweepStartButton.setObjectName(u"StitchedSweepStartButton")
        sizePolicy6.setHeightForWidth(self.StitchedSweepStartButton.sizePolicy().hasHeightForWidth())
        self.StitchedSweepStartButton.setSizePolicy(sizePolicy6)

        self.horizontalLayout_13.addWidget(self.StitchedSweepStartButton)

        self.StitchedSweepCancelButton = QPushButton(self.expStitchedSweep)
        self.StitchedSweepCancelButton.setObjectName(u"StitchedSweepCancelButton")

        self.horizontalLayout_13.addWidget(self.StitchedSweepCancelButton)

        self.StitchedSweepExportButton = QPushButton(self.expStitchedSweep)
        self.StitchedSweepExportButton.setObjectName(u"StitchedSweepExportButton")

        self.horizontalLayout_13.addWidget(self.StitchedSweepExportButton)


        self.verticalLayout_13.addLayout(self.horizontalLayout_13)

        self.StitchedSweepSweepProgress = QProgressBar(self.expStitchedSweep)
        self.StitchedSweepSweepProgress.setObjectName(u"StitchedSweepSweepProgress")
        self.StitchedSweepSweepProgress.setValue(24)
        self.StitchedSweepSweepProgress.setTextVisible(False)

        self.verticalLayout_13.addWidget(self.StitchedSweepSweepProgress)

        self.StitchedSweepTotalProgress = QProgressBar(self.expStitchedSweep)
        self.StitchedSweepTotalProgress.setObjectName(u"StitchedSweepTotalProgress")
        self.StitchedSweepTotalProgress.setValue(24)
        self.StitchedSweepTotalProgress.setTextVisible(False)

        self.verticalLayout_13.addWidget(self.StitchedSweepTotalProgress)

        self.expStack.addWidget(self.expStitchedSweep)

        self.horizontalLayout_5.addWidget(self.expStack)

        self.tabWidget_2.addTab(self.tab, "")

        self.verticalLayout_2.addWidget(self.tabWidget_2)

        self.logBox = QPlainTextEdit(self.centralwidget)
        self.logBox.setObjectName(u"logBox")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(1)
        sizePolicy8.setHeightForWidth(self.logBox.sizePolicy().hasHeightForWidth())
        self.logBox.setSizePolicy(sizePolicy8)
        self.logBox.setMinimumSize(QSize(0, 0))
        self.logBox.setMaximumSize(QSize(16777215, 120))
        self.logBox.setBaseSize(QSize(0, 0))
        self.logBox.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.logBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(3)
        self.settingsStack.setCurrentIndex(1)
        self.expStack.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.plotClearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
#if QT_CONFIG(tooltip)
        self.quickSaveButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Save data to current directory.</p><p>The filename is the current timestamp.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.quickSaveButton.setText(QCoreApplication.translate("MainWindow", u"Quick Save", None))
#if QT_CONFIG(tooltip)
        self.saveAsButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Open save dialog</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.saveAsButton.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.plot_tab), QCoreApplication.translate("MainWindow", u"Plot viewer", None))
        ___qtreewidgetitem = self.deviceTree.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Model", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Instrument type", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Status", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.devices_tab), QCoreApplication.translate("MainWindow", u"Device viewer", None))
        ___qtreewidgetitem1 = self.deviceSelectionTree.headerItem()
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Devices", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Please select a device.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.genericLockInFreqPrefix.setItemText(0, QCoreApplication.translate("MainWindow", u"Hz", None))
        self.genericLockInFreqPrefix.setItemText(1, QCoreApplication.translate("MainWindow", u"kHz", None))
        self.genericLockInFreqPrefix.setItemText(2, QCoreApplication.translate("MainWindow", u"MHz", None))
        self.genericLockInFreqPrefix.setItemText(3, QCoreApplication.translate("MainWindow", u"GHz", None))

        self.genericLockInRandomButton.setText(QCoreApplication.translate("MainWindow", u"Random", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.genericLockInAmp.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Phase", None))
        self.genericLockInPhase.setSuffix(QCoreApplication.translate("MainWindow", u" \u00b0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tau", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sensitivity", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Display", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Type</p></body></html>", None))
        self.genericLockInAqOne.setText(QCoreApplication.translate("MainWindow", u"O&ne-shot", None))
        self.genericLockInAqCont.setText(QCoreApplication.translate("MainWindow", u"Contino&us", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Frequency</p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Common parameters</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p><p><span style=\" font-weight:700;\">Data acquisition and storage</span></p></body></html>", None))
        self.genericLockInApplyButton.setText(QCoreApplication.translate("MainWindow", u"Apply settings", None))
        self.genericLockInTriggerButton.setText(QCoreApplication.translate("MainWindow", u"Manual trigger", None))
        self.genericLockInBufferReadButton.setText(QCoreApplication.translate("MainWindow", u"Read buffers", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Operation mode", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"&RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioB&utton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.settingsTab), QCoreApplication.translate("MainWindow", u"Instrument settings", None))

        __sortingEnabled = self.expList.isSortingEnabled()
        self.expList.setSortingEnabled(False)
        ___qlistwidgetitem = self.expList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Sweep and Lock-in", None));
        ___qlistwidgetitem1 = self.expList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Stitched Sweep", None));
        ___qlistwidgetitem2 = self.expList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"ODMR Waterfall", None));
        self.expList.setSortingEnabled(__sortingEnabled)

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Please select an experiment.", None))
        self.sweepAndLockPower.setSuffix(QCoreApplication.translate("MainWindow", u" dBm", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Measurements", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Sweeper", None))
        self.sweepAndLockFreq.setSuffix(QCoreApplication.translate("MainWindow", u" Hz", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Data points", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Lock-in", None))
        self.sweepAndLockDataPointsLabel.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Sensitivity", None))
        self.sweepAndLockSweepTime.setPrefix("")
        self.sweepAndLockSweepTime.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Time const.", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"End freq.", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Sweep time", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Lock-in freq.", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Start freq.", None))
        self.sweepAndLockEndFreq.setSuffix(QCoreApplication.translate("MainWindow", u" GHz", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.sweepAndLockSelectSweeper.setCurrentText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Sample freq.", None))
        self.sweepAndLockStartFreq.setSuffix(QCoreApplication.translate("MainWindow", u" GHz", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Display 1", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Display 2", None))
        self.sweepAndLockStart.setText(QCoreApplication.translate("MainWindow", u"Start measurement", None))
        self.sweepAndLockCancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.sweepAndLockExport.setText(QCoreApplication.translate("MainWindow", u"Export results", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Sweep progress", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Total progress", None))
        self.ODMRWaterfallDisplay2Radio.setText(QCoreApplication.translate("MainWindow", u"Display &2", None))
        self.ODMRWaterfallWorstTimeLabel.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
#if QT_CONFIG(tooltip)
        self.label_45.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>The number of data points captured by the lock-in amplifier during a sweep. The maximum that the device can handle is displayed in brackets. If the memory fills up, the measurement will be padded with zeros. The memory is wiped between sweeps.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Points/sweep", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"End frequency", None))
        self.ODMRWaterfallSweepEnd.setSuffix(QCoreApplication.translate("MainWindow", u" GHz", None))
        self.ODMRWaterfallSweepPower.setSuffix(QCoreApplication.translate("MainWindow", u" dBm", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Power Supply", None))
        self.ODMRWaterfallVoltage.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Sensitivity", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Steps", None))
        self.ODMRWaterfallExpectedTimeLabel.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Shutdown step size", None))
        self.ODMRWaterfallDisplay1Radio.setText(QCoreApplication.translate("MainWindow", u"Display &1", None))
        self.ODMRWaterfallEndCurrent.setSuffix(QCoreApplication.translate("MainWindow", u" A", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Lock-In Amplifier", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Start current", None))
        self.ODMRWaterfallSweepStart.setSuffix(QCoreApplication.translate("MainWindow", u" GHz", None))
#if QT_CONFIG(tooltip)
        self.label_46.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Total resolution of the resulting heatmap</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Sweep time", None))
        self.ODMRWaterfallTotalResolutionLabel.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
#if QT_CONFIG(tooltip)
        self.label_51.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Total measurement time including sweep time, PSU settle time and a 2 second wait before reading the lock-in. Does not include other blockers, such as the time it takes to read out the data from the instruments or the process of shutting down the power supply.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Expected time", None))
        self.ODMRWaterfallLockInFreq.setSuffix(QCoreApplication.translate("MainWindow", u" Hz", None))
#if QT_CONFIG(tooltip)
        self.label_33.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Frequency of the lock-in amplifier's internal oscillator. Set this to a random value that's not a multiple of any expected noise frequencies.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Lock-in frequency", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Maximum voltage", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Sweeper", None))
        self.ODMRWaterfallSweepResolutionLabel.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
#if QT_CONFIG(tooltip)
        self.label_35.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Number of measurements made per second</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Sample rate", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Shutdown interval", None))
        self.ODMRWaterfallStartCurrent.setSuffix(QCoreApplication.translate("MainWindow", u" A", None))
#if QT_CONFIG(tooltip)
        self.label_52.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Worst-case scenario where each sweep is held up for 10 more seconds.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Worst time", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Start frequency", None))
        self.ODMRWaterfallSweepTime.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"End current", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Time constant", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Settle time", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Initial settle time", None))
        self.ODMRWaterfallShutdownInterval.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.ODMRWaterfallInitialSettleTime.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.ODMRWaterfallSettleTime.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.ODMRWaterfallShutdownStepSize.setSuffix(QCoreApplication.translate("MainWindow", u" A", None))
        self.ODMRWaterfallStart.setText(QCoreApplication.translate("MainWindow", u"Start measurement", None))
        self.ODMRWaterfallCancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.ODMRWaterfallExport.setText(QCoreApplication.translate("MainWindow", u"Export results", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Sweep progress", None))
        self.ODMRWaterfallSweepProgress.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Total progress", None))
        self.ODMRWaterfallTotalProgress.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Time constant", None))
        self.StitchedSweepDisp1Check.setText(QCoreApplication.translate("MainWindow", u"Display 1", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Sensitivity", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Sweeps", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"End frequency", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Lock-in Amplifier", None))
        self.StitchedSweepEndFreq.setSuffix(QCoreApplication.translate("MainWindow", u" GHz", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Sweep time", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Sweeper", None))
        self.StitchedSweepStartFreq.setSuffix(QCoreApplication.translate("MainWindow", u" GHz", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Sample rate", None))
        self.StitchedSweepDisp2Check.setText(QCoreApplication.translate("MainWindow", u"Display 2", None))
        self.StitchedSweepSweepTime.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.StitchedSweepTotalTimeLabel.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.StitchedSweepLockInFreq.setSuffix(QCoreApplication.translate("MainWindow", u" Hz", None))
        self.StitchedSweepPower.setSuffix(QCoreApplication.translate("MainWindow", u" dBm", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Total time", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Start frequency", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Data points / sweep", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Total data points", None))
        self.StitchedSweepTotalPointsLabel.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.StitchedSweepStartButton.setText(QCoreApplication.translate("MainWindow", u"Start measurement", None))
        self.StitchedSweepCancelButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.StitchedSweepExportButton.setText(QCoreApplication.translate("MainWindow", u"Export data", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Experiments", None))
    # retranslateUi

