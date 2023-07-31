from source import gui
from PySide2 import QtWidgets
import sys

style_sheet = """
    QLabel 
    {
    color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
    stop:0 rgb(60, 186, 186) , stop: 0.5 rgb(41, 158, 158), stop:1 rgb(23, 122, 122));
    }
    
    QLineEdit{
    border-width: 0px;
    padding: 1px;
    border-style: solid;
    border-radius: 7px;
    color: white;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
    stop:0 rgb(60, 186, 186) , stop: 0.5 rgb(41, 158, 158), stop:1 rgb(23, 122, 122));
    }
    
    QPushButton {
    border-width: 0px;
    padding: 1px;
    border-style: solid;
    border-radius: 7px;
    color: white;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
    stop:0 rgb(60, 186, 186) , stop: 0.5 rgb(41, 158, 158), stop:1 rgb(23, 122, 122));
    }
    
    QPushButton:hover 
    {
    border-width: 0px;
    padding: 1px;
    border-style: solid;
    border-radius: 7px;
    color: white;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
    stop:0 rgb(132, 227, 227) , stop: 0.5 rgb(83, 173, 173), stop:1 rgb(48, 128, 128));
    }
    
    QPushButton:pressed 
    {
    border-width: 2px;
    padding: 1px;
    border-style: solid;
    border-radius: 7px;
    border-color: rgb(42, 115, 115);
    color: white;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
    stop:0 rgb(66, 153, 153) , stop: 0.5 rgb(42, 115, 115), stop:1 rgb(29, 87, 87));
    }
    
    
    
    """

def main():
    app0 = QtWidgets.QApplication(sys.argv)
    window = gui.MainGUI()
    window.setStyleSheet(style_sheet)
    window.show()
    sys.exit(app0.exec_())


if __name__ == "__main__":
    main()