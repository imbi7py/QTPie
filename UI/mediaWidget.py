#pylint: disable=C0103, C0301, R0902
"""
Sets up and maintains the Widget part of the UI for QTPie
"""
__author__ = "Noupin"

#Third Party Imports
import os
import sys
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui

#First Party Imports
from UI.widget import QTPieWidget


class QTPieMediaWidget(QTPieWidget):
    """
    A super function extending the QTPieWidget class from QTPie. Specialized for media attributes.

    Args:\n
        QtWidgets (PyQt5.QtWidgets.QWidget): Inherits from QWidget
    """

    def __init__(self, parent=None, doesSignal=False):
        """
        Initializes the super class

        Args:\n
            parent (PyQt5.QtWidgets.*): The object to put the widget on. Defaults to None.
            isVideo (bool, optional): Determines whether the video attributes will be used. Defaults to False.
        """

        super().__init__(parent, doesSignal)

        #Grid varibles for the widget
        self.grid = None
        self.gridCount = 0

        #Media variables for the widget
        self.media = None
        self.video = None
        self.filename = ""