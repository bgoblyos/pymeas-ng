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
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QTabWidget,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1661, 1204)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.plot_tab = QWidget()
        self.plot_tab.setObjectName(u"plot_tab")
        self.verticalLayout_4 = QVBoxLayout(self.plot_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.graphWidget = PlotWidget(self.plot_tab)
        self.graphWidget.setObjectName(u"graphWidget")

        self.verticalLayout_2.addWidget(self.graphWidget)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

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
        self.horizontalLayout_4 = QHBoxLayout(self.settingsTab)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1409, 1046))
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.genericLockInFreqPrefix.sizePolicy().hasHeightForWidth())
        self.genericLockInFreqPrefix.setSizePolicy(sizePolicy2)
        self.genericLockInFreqPrefix.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.genericLockInFreqPrefix)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.genericLockInRandomButton = QPushButton(self.scrollAreaWidgetContents)
        self.genericLockInRandomButton.setObjectName(u"genericLockInRandomButton")

        self.verticalLayout_5.addWidget(self.genericLockInRandomButton)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_5)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.genericLockInAmp = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.genericLockInAmp.setObjectName(u"genericLockInAmp")
        self.genericLockInAmp.setDecimals(3)
        self.genericLockInAmp.setMinimum(0.005000000000000)
        self.genericLockInAmp.setMaximum(4.999000000000000)
        self.genericLockInAmp.setSingleStep(0.010000000000000)
        self.genericLockInAmp.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.genericLockInAmp)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_5)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(5, QFormLayout.LabelRole, self.verticalSpacer)

        self.genericLockInPhase = QDoubleSpinBox(self.scrollAreaWidgetContents)
        self.genericLockInPhase.setObjectName(u"genericLockInPhase")
        self.genericLockInPhase.setDecimals(3)
        self.genericLockInPhase.setMinimum(-359.999000000000024)
        self.genericLockInPhase.setMaximum(729.980000000000018)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.genericLockInPhase)

        self.genericLockInTau = QComboBox(self.scrollAreaWidgetContents)
        self.genericLockInTau.setObjectName(u"genericLockInTau")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.genericLockInTau)

        self.genericLockInSens = QComboBox(self.scrollAreaWidgetContents)
        self.genericLockInSens.setObjectName(u"genericLockInSens")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.genericLockInSens)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.genericLockInApplyButton = QPushButton(self.genericLockInPage)
        self.genericLockInApplyButton.setObjectName(u"genericLockInApplyButton")

        self.verticalLayout_3.addWidget(self.genericLockInApplyButton)

        self.settingsStack.addWidget(self.genericLockInPage)
        self.testPage2 = QWidget()
        self.testPage2.setObjectName(u"testPage2")
        self.label_4 = QLabel(self.testPage2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(22, 6, 42, 18))
        self.settingsStack.addWidget(self.testPage2)

        self.horizontalLayout_4.addWidget(self.settingsStack)

        self.tabWidget_2.addTab(self.settingsTab, "")

        self.horizontalLayout_2.addWidget(self.tabWidget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(1)
        self.settingsStack.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.genericLockInFreqPrefix.setItemText(0, QCoreApplication.translate("MainWindow", u"Hz", None))
        self.genericLockInFreqPrefix.setItemText(1, QCoreApplication.translate("MainWindow", u"kHz", None))
        self.genericLockInFreqPrefix.setItemText(2, QCoreApplication.translate("MainWindow", u"MHz", None))
        self.genericLockInFreqPrefix.setItemText(3, QCoreApplication.translate("MainWindow", u"GHz", None))

        self.genericLockInRandomButton.setText(QCoreApplication.translate("MainWindow", u"Random", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Amplitude", None))
        self.genericLockInAmp.setSuffix(QCoreApplication.translate("MainWindow", u" V", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Phase", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tau", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Sensitivity", None))
        self.genericLockInPhase.setSuffix(QCoreApplication.translate("MainWindow", u" \u00b0", None))
        self.genericLockInApplyButton.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.settingsTab), QCoreApplication.translate("MainWindow", u"Instrument Settings", None))
    # retranslateUi

