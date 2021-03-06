# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../qt5_ui/page_task_overall.ui'
#
# Created: Mon Oct 29 12:05:24 2018
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PageTaskOverall(object):
    def setupUi(self, PageTaskOverall):
        PageTaskOverall.setObjectName("PageTaskOverall")
        PageTaskOverall.setEnabled(True)
        PageTaskOverall.resize(822, 571)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PageTaskOverall.sizePolicy().hasHeightForWidth())
        PageTaskOverall.setSizePolicy(sizePolicy)
        PageTaskOverall.setMinimumSize(QtCore.QSize(400, 300))
        self.gridLayout = QtWidgets.QGridLayout(PageTaskOverall)
        self.gridLayout.setObjectName("gridLayout")
        self.label_task_name = QtWidgets.QLabel(PageTaskOverall)
        self.label_task_name.setObjectName("label_task_name")
        self.gridLayout.addWidget(self.label_task_name, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.task_name = QtWidgets.QLineEdit(PageTaskOverall)
        self.task_name.setAcceptDrops(True)
        self.task_name.setToolTipDuration(20)
        self.task_name.setWhatsThis("")
        self.task_name.setAutoFillBackground(True)
        self.task_name.setText("")
        self.task_name.setReadOnly(False)
        self.task_name.setClearButtonEnabled(False)
        self.task_name.setObjectName("task_name")
        self.gridLayout.addWidget(self.task_name, 1, 2, 1, 2)
        self.directory = QtWidgets.QLineEdit(PageTaskOverall)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.directory.sizePolicy().hasHeightForWidth())
        self.directory.setSizePolicy(sizePolicy)
        self.directory.setMinimumSize(QtCore.QSize(250, 0))
        self.directory.setAcceptDrops(True)
        self.directory.setToolTip("")
        self.directory.setToolTipDuration(-1)
        self.directory.setWhatsThis("")
        self.directory.setAutoFillBackground(True)
        self.directory.setText("")
        self.directory.setReadOnly(True)
        self.directory.setClearButtonEnabled(False)
        self.directory.setObjectName("directory")
        self.gridLayout.addWidget(self.directory, 2, 2, 1, 3)
        self.label_directory = QtWidgets.QLabel(PageTaskOverall)
        self.label_directory.setObjectName("label_directory")
        self.gridLayout.addWidget(self.label_directory, 2, 1, 1, 1)
        self.button_directory = QtWidgets.QPushButton(PageTaskOverall)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_directory.sizePolicy().hasHeightForWidth())
        self.button_directory.setSizePolicy(sizePolicy)
        self.button_directory.setMinimumSize(QtCore.QSize(30, 30))
        self.button_directory.setMaximumSize(QtCore.QSize(30, 30))
        self.button_directory.setObjectName("button_directory")
        self.gridLayout.addWidget(self.button_directory, 2, 5, 1, 1)
        self.label_user_entities = QtWidgets.QLabel(PageTaskOverall)
        self.label_user_entities.setObjectName("label_user_entities")
        self.gridLayout.addWidget(self.label_user_entities, 3, 1, 1, 1)
        self.list_user_entities = QtWidgets.QListWidget(PageTaskOverall)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_user_entities.sizePolicy().hasHeightForWidth())
        self.list_user_entities.setSizePolicy(sizePolicy)
        self.list_user_entities.setMinimumSize(QtCore.QSize(250, 0))
        self.list_user_entities.setObjectName("list_user_entities")
        self.gridLayout.addWidget(self.list_user_entities, 3, 2, 2, 3)
        self.button_user_entities_plus = QtWidgets.QPushButton(PageTaskOverall)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_user_entities_plus.sizePolicy().hasHeightForWidth())
        self.button_user_entities_plus.setSizePolicy(sizePolicy)
        self.button_user_entities_plus.setMinimumSize(QtCore.QSize(30, 30))
        self.button_user_entities_plus.setMaximumSize(QtCore.QSize(30, 30))
        self.button_user_entities_plus.setObjectName("button_user_entities_plus")
        self.gridLayout.addWidget(self.button_user_entities_plus, 3, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(133, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.list_extra_files = QtWidgets.QListWidget(PageTaskOverall)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_extra_files.sizePolicy().hasHeightForWidth())
        self.list_extra_files.setSizePolicy(sizePolicy)
        self.list_extra_files.setMinimumSize(QtCore.QSize(250, 0))
        self.list_extra_files.setObjectName("list_extra_files")
        self.gridLayout.addWidget(self.list_extra_files, 5, 2, 2, 3)
        self.button_user_entities_minus = QtWidgets.QPushButton(PageTaskOverall)
        self.button_user_entities_minus.setMinimumSize(QtCore.QSize(30, 30))
        self.button_user_entities_minus.setMaximumSize(QtCore.QSize(30, 30))
        self.button_user_entities_minus.setObjectName("button_user_entities_minus")
        self.gridLayout.addWidget(self.button_user_entities_minus, 4, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(133, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 6, 1, 1)
        self.label_extra_files = QtWidgets.QLabel(PageTaskOverall)
        self.label_extra_files.setObjectName("label_extra_files")
        self.gridLayout.addWidget(self.label_extra_files, 5, 1, 1, 1)
        self.button_extra_files_plus = QtWidgets.QPushButton(PageTaskOverall)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_extra_files_plus.sizePolicy().hasHeightForWidth())
        self.button_extra_files_plus.setSizePolicy(sizePolicy)
        self.button_extra_files_plus.setMinimumSize(QtCore.QSize(30, 30))
        self.button_extra_files_plus.setMaximumSize(QtCore.QSize(30, 30))
        self.button_extra_files_plus.setObjectName("button_extra_files_plus")
        self.gridLayout.addWidget(self.button_extra_files_plus, 5, 5, 1, 1)
        self.label_timeout = QtWidgets.QLabel(PageTaskOverall)
        self.label_timeout.setObjectName("label_timeout")
        self.gridLayout.addWidget(self.label_timeout, 9, 1, 1, 1)
        self.button_extra_files_minus = QtWidgets.QPushButton(PageTaskOverall)
        self.button_extra_files_minus.setMinimumSize(QtCore.QSize(30, 30))
        self.button_extra_files_minus.setMaximumSize(QtCore.QSize(30, 30))
        self.button_extra_files_minus.setObjectName("button_extra_files_minus")
        self.gridLayout.addWidget(self.button_extra_files_minus, 6, 5, 1, 1)
        self.checkbox_attach_wavefile = QtWidgets.QCheckBox(PageTaskOverall)
        self.checkbox_attach_wavefile.setObjectName("checkbox_attach_wavefile")
        self.gridLayout.addWidget(self.checkbox_attach_wavefile, 10, 1, 1, 2)
        self.timeout = QtWidgets.QSpinBox(PageTaskOverall)
        self.timeout.setMaximum(120)
        self.timeout.setProperty("value", 30)
        self.timeout.setObjectName("timeout")
        self.gridLayout.addWidget(self.timeout, 9, 2, 1, 1)
        self.checkbox_constraint_script = QtWidgets.QCheckBox(PageTaskOverall)
        self.checkbox_constraint_script.setObjectName("checkbox_constraint_script")
        self.gridLayout.addWidget(self.checkbox_constraint_script, 11, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 57, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 12, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(PageTaskOverall)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 1, 1, 1)
        self.list_languages = QtWidgets.QListWidget(PageTaskOverall)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_languages.sizePolicy().hasHeightForWidth())
        self.list_languages.setSizePolicy(sizePolicy)
        self.list_languages.setMinimumSize(QtCore.QSize(150, 75))
        self.list_languages.setMaximumSize(QtCore.QSize(150, 75))
        self.list_languages.setAutoFillBackground(False)
        self.list_languages.setObjectName("list_languages")
        self.gridLayout.addWidget(self.list_languages, 7, 2, 1, 1)
        self.button_language_plus = QtWidgets.QPushButton(PageTaskOverall)
        self.button_language_plus.setMinimumSize(QtCore.QSize(30, 30))
        self.button_language_plus.setMaximumSize(QtCore.QSize(30, 30))
        self.button_language_plus.setObjectName("button_language_plus")
        self.gridLayout.addWidget(self.button_language_plus, 8, 3, 1, 1)
        self.combo_language = QtWidgets.QComboBox(PageTaskOverall)
        self.combo_language.setCurrentText("")
        self.combo_language.setObjectName("combo_language")
        self.gridLayout.addWidget(self.combo_language, 8, 2, 1, 1)
        self.button_language_minus = QtWidgets.QPushButton(PageTaskOverall)
        self.button_language_minus.setMinimumSize(QtCore.QSize(30, 30))
        self.button_language_minus.setMaximumSize(QtCore.QSize(30, 30))
        self.button_language_minus.setObjectName("button_language_minus")
        self.gridLayout.addWidget(self.button_language_minus, 7, 3, 1, 1)

        self.retranslateUi(PageTaskOverall)
        self.list_languages.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(PageTaskOverall)

    def retranslateUi(self, PageTaskOverall):
        _translate = QtCore.QCoreApplication.translate
        PageTaskOverall.setWindowTitle(_translate("PageTaskOverall", "WizardPage"))
        self.label_task_name.setText(_translate("PageTaskOverall", "Task name"))
        self.task_name.setToolTip(_translate("PageTaskOverall", "Name for the task."))
        self.label_directory.setText(_translate("PageTaskOverall", "Output directory"))
        self.button_directory.setText(_translate("PageTaskOverall", "..."))
        self.label_user_entities.setText(_translate("PageTaskOverall", "User entities"))
        self.button_user_entities_plus.setText(_translate("PageTaskOverall", "+"))
        self.button_user_entities_minus.setText(_translate("PageTaskOverall", "-"))
        self.label_extra_files.setText(_translate("PageTaskOverall", "Extra files"))
        self.button_extra_files_plus.setText(_translate("PageTaskOverall", "+"))
        self.label_timeout.setText(_translate("PageTaskOverall", "Simulation Timeout (in s)"))
        self.button_extra_files_minus.setText(_translate("PageTaskOverall", "-"))
        self.checkbox_attach_wavefile.setText(_translate("PageTaskOverall", "Attach wavefile"))
        self.checkbox_constraint_script.setText(_translate("PageTaskOverall", "Use task constraint script"))
        self.label_2.setText(_translate("PageTaskOverall", "Description languages"))
        self.button_language_plus.setText(_translate("PageTaskOverall", "+"))
        self.button_language_minus.setText(_translate("PageTaskOverall", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PageTaskOverall = QtWidgets.QWizardPage()
    ui = Ui_PageTaskOverall()
    ui.setupUi(PageTaskOverall)
    PageTaskOverall.show()
    sys.exit(app.exec_())

