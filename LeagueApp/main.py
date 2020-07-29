import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, QButtonGroup
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QCheckBox, QRadioButton
from PyQt5 import QtCore

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'League Statistics Tracker'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()
    
class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(MyTableWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Scrape Data")
        self.tabs.addTab(self.tab2,"About")
        
        # Create first tab
        self.tab1.layout = QVBoxLayout() # used to be QVBoxLayout(self)
        self.pushButton1 = QPushButton("Scrape Matches")
        self.tab1.layout.addWidget(self.pushButton1)
        self.pushButton1.clicked.connect(self.checkWhatToScrape)
        self.tab1.setLayout(self.tab1.layout)

        # Add option to select all leagues
        self.manualSelect = QRadioButton("Manually Select Leagues")
        self.manualSelect.setChecked(True)
        self.manualSelect.clicked.connect(self.selectLeagues)

        self.autoSelect = QRadioButton("Select All Leagues")
        self.autoSelect.clicked.connect(self.selectLeagues)

        self.tab1.layout.addWidget(self.manualSelect)
        self.tab1.layout.addWidget(self.autoSelect)

        # Add checkboxes for each scrapable league
        self.leagueLCS = QCheckBox("LCS")
        self.leagueLEC = QCheckBox("LEC")
        self.leagueLCK = QCheckBox("LCK")
        self.leagueOPL = QCheckBox("OPL")
        self.leagueLPL = QCheckBox("LPL")
        self.leagueLLA = QCheckBox("LLA")
        self.leagueLFL = QCheckBox("LFL")
        self.leagueLVP = QCheckBox("LVP")
        self.leagueUltraliga = QCheckBox("Ultraliga")
        self.leagueNAA = QCheckBox("NA Academy")
        self.leagueTCL = QCheckBox("TCL")
        self.leagueCBLOL = QCheckBox("CBLOL")
        self.leagueLJL = QCheckBox("LJL")
        self.leagueVCS = QCheckBox("VCS")
        self.leaguePCS = QCheckBox("PCS")

        self.checkboxes = [self.leagueLCS, self.leagueLEC, self.leagueLCK, self.leagueOPL, self.leagueLPL, self.leagueLLA, self.leagueLFL, self.leagueLVP, self.leagueUltraliga, self.leagueNAA ,self.leagueTCL, self.leagueCBLOL, self.leagueLJL, self.leagueVCS, self.leaguePCS]

        for box in self.checkboxes:
            self.tab1.layout.addWidget(box)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
    # Toggle league selection using radio buttons
    def selectLeagues(self):
        if self.manualSelect.isChecked() == True:
            for box in self.checkboxes:
                box.setChecked(False)
                box.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, False)

        if self.autoSelect.isChecked() == True:
            for box in self.checkboxes:
                box.setChecked(True)
                box.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)

    def checkWhatToScrape(self): 
        for box in self.checkboxes:
            print(box.isChecked())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())