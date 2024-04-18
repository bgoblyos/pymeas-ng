# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDoubleSpinBox,
    QFormLayout, QHBoxLayout, QHeaderView, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPlainTextEdit,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTabWidget,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1091, 842)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.plot_tab = QWidget()
        self.plot_tab.setObjectName(u"plot_tab")
        self.horizontalLayout_9 = QHBoxLayout(self.plot_tab)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.graphWidget = PlotWidget(self.plot_tab)
        self.graphWidget.setObjectName(u"graphWidget")

        self.horizontalLayout_2.addWidget(self.graphWidget)

        self.listWidget = QListWidget(self.plot_tab)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout_2.addWidget(self.listWidget)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_2)

        self.tabWidget_2.addTab(self.plot_tab, "")
        self.devices_tab = QWidget()
        self.devices_tab.setObjectName(u"devices_tab")
        self.horizontalLayout = QHBoxLayout(self.devices_tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.deviceTree = QTreeWidget(self.devices_tab)
        self.deviceTree.setObjectName(u"deviceTree")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.deviceTree.sizePolicy().hasHeightForWidth())
        self.deviceTree.setSizePolicy(sizePolicy)

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
        self.label_7.setAlignment(Qt.AlignCenter)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 816, 566))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

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
        self.genericLockInFreqBox.setStepType(QAbstractSpinBox.DefaultStepType)
        self.genericLockInFreqBox.setValue(1.000000000000000)

        self.horizontalLayout_3.addWidget(self.genericLockInFreqBox)

        self.genericLockInFreqPrefix = QComboBox(self.scrollAreaWidgetContents)
        self.genericLockInFreqPrefix.addItem("")
        self.genericLockInFreqPrefix.addItem("")
        self.genericLockInFreqPrefix.addItem("")
        self.genericLockInFreqPrefix.addItem("")
        self.genericLockInFreqPrefix.setObjectName(u"genericLockInFreqPrefix")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.genericLockInFreqPrefix.sizePolicy().hasHeightForWidth())
        self.genericLockInFreqPrefix.setSizePolicy(sizePolicy3)
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
        self.genericLockInAmp.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 733, 381))
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

        self.settingsLogBox = QPlainTextEdit(self.settingsTab)
        self.settingsLogBox.setObjectName(u"settingsLogBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.settingsLogBox.sizePolicy().hasHeightForWidth())
        self.settingsLogBox.setSizePolicy(sizePolicy4)

        self.verticalLayout_10.addWidget(self.settingsLogBox)

        self.tabWidget_2.addTab(self.settingsTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(0)
        self.settingsStack.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Placeholder", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"For", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Plot", None));
        ___qlistwidgetitem3 = self.listWidget.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qlistwidgetitem4 = self.listWidget.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Selection", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

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
        self.genericLockInAqOne.setText(QCoreApplication.translate("MainWindow", u"One-shot", None))
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
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.settingsTab), QCoreApplication.translate("MainWindow", u"Instrument Settings", None))
    # retranslateUi

