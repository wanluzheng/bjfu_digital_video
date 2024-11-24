# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoPlayeroPhUIO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VideoPlayer(object):
    def setupUi(self, VideoPlayer):
        if not VideoPlayer.objectName():
            VideoPlayer.setObjectName(u"VideoPlayer")
        VideoPlayer.setWindowModality(Qt.NonModal)
        VideoPlayer.resize(1500, 747)
        VideoPlayer.setCursor(QCursor(Qt.ArrowCursor))
        VideoPlayer.setAcceptDrops(False)
        VideoPlayer.setStyleSheet(u"")
        self.video = QWidget(VideoPlayer)
        self.video.setObjectName(u"video")
        self.video.setGeometry(QRect(30, 40, 611, 671))
        self.video.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.keyframe = QWidget(VideoPlayer)
        self.keyframe.setObjectName(u"keyframe")
        self.keyframe.setGeometry(QRect(660, 40, 531, 431))
        self.keyframe.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.plateNum = QWidget(VideoPlayer)
        self.plateNum.setObjectName(u"plateNum")
        self.plateNum.setGeometry(QRect(660, 490, 531, 221))
        self.plateNum.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.Messge = QListWidget(VideoPlayer)
        self.Messge.setObjectName(u"Messge")
        self.Messge.setGeometry(QRect(1210, 40, 261, 611))
        self.Messge.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.Save = QPushButton(VideoPlayer)
        self.Save.setObjectName(u"Save")
        self.Save.setGeometry(QRect(1210, 670, 101, 41))
        self.Save.setStyleSheet(u"background-color:rgb(255, 255, 255)")
        self.Confirm = QPushButton(VideoPlayer)
        self.Confirm.setObjectName(u"Confirm")
        self.Confirm.setGeometry(QRect(1370, 670, 101, 41))
        self.Confirm.setStyleSheet(u"background-color:rgb(255, 255, 255)")

        self.retranslateUi(VideoPlayer)

        QMetaObject.connectSlotsByName(VideoPlayer)
    # setupUi

    def retranslateUi(self, VideoPlayer):
        VideoPlayer.setWindowTitle(QCoreApplication.translate("VideoPlayer", u"Form", None))
        self.Save.setText(QCoreApplication.translate("VideoPlayer", u"\u4fdd \u5b58", None))
        self.Confirm.setText(QCoreApplication.translate("VideoPlayer", u"\u786e \u8ba4", None))
    # retranslateUi

