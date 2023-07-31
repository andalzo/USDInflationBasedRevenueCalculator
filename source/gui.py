from PySide2 import QtWidgets, QtGui, QtCore
from source import backend


class MainGUI(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.__set_gui_properties()
        self.__create_gui_widgets()
        self.__create_gui_layouts()
        self.__apply_gui_layouts()

    def __set_gui_properties(self):

        self.setFixedSize(650, 500)
        self.text_font = QtGui.QFont("Tahoma", 20)
        self.text_font.setBold(True)
        self.label_size = QtCore.QSize(300, 50)
        self.label_size_wide = QtCore.QSize(600, 50)

    def __create_gui_widgets(self):

        self.prev_dollar_value_label = QtWidgets.QLabel("Previous Dollar Value: ")
        self.prev_dollar_value_label.setFixedSize(self.label_size)
        self.prev_dollar_value_label.setFont(self.text_font)

        self.prev_dollar_value_in = QtWidgets.QLineEdit()
        self.prev_dollar_value_in.setFixedSize(self.label_size)
        self.prev_dollar_value_in.setFont(self.text_font)

        self.new_dollar_value_label = QtWidgets.QLabel("New Dollar Value: ")
        self.new_dollar_value_label.setFixedSize(self.label_size)
        self.new_dollar_value_label.setFont(self.text_font)

        self.new_dollar_value_in = QtWidgets.QLineEdit()
        self.new_dollar_value_in.setFixedSize(self.label_size)
        self.new_dollar_value_in.setFont(self.text_font)

        self.prev_item_value_label = QtWidgets.QLabel("Prev Item Value: ")
        self.prev_item_value_label.setFixedSize(self.label_size)
        self.prev_item_value_label.setFont(self.text_font)

        self.prev_item_value_in = QtWidgets.QLineEdit()
        self.prev_item_value_in.setFixedSize(self.label_size)
        self.prev_item_value_in.setFont(self.text_font)

        self.new_item_value_label = QtWidgets.QLabel("New Item Value: ")
        self.new_item_value_label.setFixedSize(self.label_size)
        self.new_item_value_label.setFont(self.text_font)

        self.new_item_value_in = QtWidgets.QLineEdit()
        self.new_item_value_in.setFixedSize(self.label_size)
        self.new_item_value_in.setFont(self.text_font)

        self.prev_stock_value_label = QtWidgets.QLabel("Prev Stock Value: ")
        self.prev_stock_value_label.setFixedSize(self.label_size)
        self.prev_stock_value_label.setFont(self.text_font)

        self.prev_stock_value_in = QtWidgets.QLineEdit()
        self.prev_stock_value_in.setFixedSize(self.label_size)
        self.prev_stock_value_in.setFont(self.text_font)

        self.new_stock_value_label = QtWidgets.QLabel("New Stock Value: ")
        self.new_stock_value_label.setFixedSize(self.label_size)
        self.new_stock_value_label.setFont(self.text_font)

        self.new_stock_value_in = QtWidgets.QLineEdit()
        self.new_stock_value_in.setFixedSize(self.label_size)
        self.new_stock_value_in.setFont(self.text_font)

        self.dollar_inflation_rate_label = QtWidgets.QLabel("Inflation Acc. Dollar: ")
        self.dollar_inflation_rate_label.setFixedSize(self.label_size_wide)
        self.dollar_inflation_rate_label.setFont(self.text_font)

        self.dollar_profit_rate_label = QtWidgets.QLabel("Dollar Profit Without Inflation: ")
        self.dollar_profit_rate_label.setFixedSize(self.label_size_wide)
        self.dollar_profit_rate_label.setFont(self.text_font)

        self.reel_profit_label = QtWidgets.QLabel("Reel Profit: ")
        self.reel_profit_label.setFixedSize(self.label_size_wide)
        self.reel_profit_label.setFont(self.text_font)

        self.button = QtWidgets.QPushButton("Calculate")
        self.button.setFixedSize(self.label_size_wide)
        self.button.setFont(self.text_font)
        self.button.clicked.connect(self.__calculate)

    def __create_gui_layouts(self):

        self.formBox = QtWidgets.QFormLayout()
        self.vMainBox = QtWidgets.QVBoxLayout()

    def __apply_gui_layouts(self):

        self.formBox.addRow(self.prev_dollar_value_label, self.prev_dollar_value_in)
        self.formBox.addRow(self.new_dollar_value_label, self.new_dollar_value_in)
        self.formBox.addRow(self.prev_stock_value_label, self.prev_stock_value_in)
        self.formBox.addRow(self.new_stock_value_label, self.new_stock_value_in)
        self.formBox.addRow(self.prev_item_value_label, self.prev_item_value_in)
        self.formBox.addRow(self.new_item_value_label, self.new_item_value_in)

        self.vMainBox.addStretch()
        self.vMainBox.addLayout(self.formBox)
        self.vMainBox.addWidget(self.dollar_inflation_rate_label)
        self.vMainBox.addWidget(self.dollar_profit_rate_label)
        self.vMainBox.addWidget(self.reel_profit_label)
        self.vMainBox.addWidget(self.button)
        self.vMainBox.addStretch()

        self.setLayout(self.vMainBox)

    def __calculate(self):
        backend_obj = backend.Backend(float(self.prev_dollar_value_in.text()), float(self.new_dollar_value_in.text()),
                                      float(self.prev_stock_value_in.text()), float(self.new_stock_value_in.text()),
                                      float(self.prev_item_value_in.text()), float(self.new_item_value_in.text()))

        backend_obj.calculate_inflation_rate_regardings_to_dollar()
        dollar_inflation_rate = backend_obj.inflation_rate_regardings_to_dollar * 100 - 100
        self.dollar_inflation_rate_label.setText(f"Inflation Acc. Dollar: {dollar_inflation_rate}%")

        backend_obj.calculate_profit_regardings_to_dollar()
        dollar_profit = backend_obj.profit_regardings_to_dollar * 100 - 100
        if dollar_profit < 0:
            self.dollar_profit_rate_label.setStyleSheet("QLabel{color: red}")
        else:
            self.dollar_profit_rate_label.setStyleSheet("QLabel{color: green}")
        self.dollar_profit_rate_label.setText(f"Dollar Profit: {dollar_profit}%")

        backend_obj.calculate_reel_profit()
        reel_profit = backend_obj.reel_profit * 100 - 100
        if reel_profit < 0:
            self.reel_profit_label.setStyleSheet("QLabel{color: red}")
        else:
            self.reel_profit_label.setStyleSheet("QLabel{color: green}")
        self.reel_profit_label.setText(f"Reel Profit: {reel_profit}%")
