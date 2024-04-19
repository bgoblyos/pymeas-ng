from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QPlainTextEdit

import logging


# Taken from https://stackoverflow.com/a/75149586
# Class licensed under CC BY-SA 4.0
# Copyright 2023 https://stackoverflow.com/users/3435468/partybuddha

# This class is responsible for GUI logging
# Initialze by passing a QPlainTextEdit widget
# Add as logging handler to use
class QTextEditLogger(logging.Handler):
    class Emitter(QObject):
        log = Signal(str)

    def __init__(self, widget):
        super().__init__()

        # create text edit widget
        self.widget = widget
        self.widget.setReadOnly(True)

        # Create a QObject which will emit a signal for each log. This implicitly queues each 
        # appendPlainText() call which makes it thread-safe
        self.emitter = QTextEditLogger.Emitter()
        self.emitter.log.connect(self.widget.appendPlainText)

    # override Handler's emit method (this happens to share a name with Qt's emit method.
    # Don't get confused)
    def emit(self, record):
        msg = self.format(record)
        self.emitter.log.emit(msg)
        print(msg)
