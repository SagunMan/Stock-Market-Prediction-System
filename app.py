import sys
from PyQt5 import QtWidgets
import os

from input import get_alias

class Window(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 100, 700, 630)
        self.setWindowTitle("Stock Market Prediction")

        self.home()
        
    def home(self):        
        values = get_alias()
        alias = values[0]
        
        self.companyChoice = QtWidgets.QLabel(self)
        self.companyChoice.setGeometry(50, 90, 500, 120)
        
        self.companyChoicename = QtWidgets.QLabel(self)
        self.companyChoicename.setGeometry(50, 120, 1000, 120)
        
        self.btn = QtWidgets.QPushButton("Make Prediction",self)
        self.btn.move(50,220)
        self.btn.clicked.connect(self.displayPrediction)

        self.reloadbtn = QtWidgets.QPushButton("Make another Prediction",self)
        self.reloadbtn.hide()
        self.reloadbtn.setGeometry(50,550,150,40)
        self.reloadbtn.clicked.connect(self.restart_program)
        
        self.choicelbl = QtWidgets.QLabel("Select a company", self)

        comboBox = QtWidgets.QComboBox(self)
        for i in range(0,len(alias)):
            comboBox.addItem(alias[i])
        comboBox.move(150, 20)
        
        self.choicelbl.move(50,20)
        comboBox.activated[str].connect(self.company_choice)
        
        self.searchlbl = QtWidgets.QLabel(self)
        self.searchlbl.setText("Search company by alias")
        self.searchlbl.setGeometry(200, 80, 250, 20)
        self.searchlbl.move(320,25)
        
        self.searchtxt = QtWidgets.QTextEdit(self)
        self.searchtxt.move(450,20)
        
        self.searchbtn = QtWidgets.QPushButton("Search",self)
        self.searchbtn.move(560,20)
        self.searchbtn.clicked.connect(self.search)
        
        self.hdnval = QtWidgets.QLabel(self)
        self.hdnval.hide()

        

        self.l1 = QtWidgets.QLabel(self)
        self.l2 = QtWidgets.QLabel(self)
        self.l3 = QtWidgets.QLabel(self)
        self.l4 = QtWidgets.QLabel(self)
        self.l5 = QtWidgets.QLabel(self)
        self.l6 = QtWidgets.QLabel(self)
        self.l7 = QtWidgets.QLabel(self)
        self.l8 = QtWidgets.QLabel(self)
        self.l9 = QtWidgets.QLabel(self)
        self.l10 = QtWidgets.QLabel(self)
        self.l11 = QtWidgets.QLabel(self)
        self.l12 = QtWidgets.QLabel(self)
        
        self.l1.setGeometry(50, 340, 250, 20)
        self.l2.setGeometry(50, 360, 1000, 20)
        self.l3.setGeometry(50, 380, 250, 20)
        self.l4.setGeometry(50, 400, 250, 20)
        self.l5.setGeometry(50, 420, 250, 20)
        self.l6.setGeometry(50, 440, 250, 20)
        self.l7.setGeometry(50, 460, 250, 20)
        self.l8.setGeometry(50, 480, 250, 20)
        self.l9.setGeometry(250, 380, 250, 20)
        self.l10.setGeometry(250, 400, 250, 20)
        self.l11.setGeometry(250, 420, 250, 20)
        self.l12.setGeometry(50, 510, 250, 20)
        
        self.choiceheading = QtWidgets.QLabel(self)
        self.choiceheading.setGeometry(50, 50, 1000, 120)
        self.choiceheading.setText("<font size = 20>Selected company</font>")

        self.resultheading = QtWidgets.QLabel(self)
        self.resultheading.setGeometry(50, 250, 1000, 120)
        self.resultheading.setText("<font size = 20>Prediction result</font>")
        
        self.show()

    def company_choice(self, text):
        values = get_alias()
        alias = values[0]
        name = values[1]
        
        for i in range(0,len(alias)):
            if(alias[i].lower()==text.lower()):
                self.companyChoicename.setText("<font color='green' size='50'>" + name[i] + "</font>")
        self.companyChoice.setText("<font color='green' size='50'>Company alias: " + text + "</font>")
        self.hdnval.setText(text)
        
        from program import main
        main(self.hdnval.text())

    def search(self):
        values = get_alias()
        alias = values[0]
        name = values[1]
        counter = 1
        for j in range(0,len(alias)):
            if(alias[j].lower()==self.searchtxt.toPlainText().lower()):    
                for i in range(0,len(alias)):
                    if(alias[i].lower()==self.searchtxt.toPlainText().lower()):
                        self.companyChoicename.setText("<font color='green' size='50'>" + name[i] + "</font>")
                self.companyChoice.setText("<font color='green' size='50'>Company alias: " + alias[j] + "</font>")
                self.hdnval.setText(alias[j])
                
                counter = counter-1
                from program import main
                main(self.hdnval.text())
        if(counter>0):
            self.companyChoice.setText("<font color='red' size='50'>Company not found</font>")
            self.companyChoicename.setText("")
    
    
    def displayPrediction(self):        
        from program import main
        main(self.hdnval.text())
        from program import get_prediction
        from program import get_outcome
        values = get_prediction(self.hdnval.text())
        out = get_outcome(self.hdnval.text())
        
        self.l1.setText(values[0])
        self.l2.setText(values[1])
        self.l3.setText(values[2])
        self.l4.setText(values[3])
        self.l5.setText(values[4])
        self.l6.setText(values[5])
        self.l7.setText(values[6])
        self.l8.setText(values[7])
        
        pos = 0 
        neg = 0
        if(out[0]>0):
            self.l9.setText("<font color='green' size='5'>Closing price difference: "+str(round(out[0],2))+"</font>")
            pos = pos + 1
        if(out[0]<0):
            self.l9.setText("<font color='red' size='5'>Closing price difference: "+str(round(out[0],2))+"</font>")
            neg = neg + 1
        if(out[0]==0):
            self.l9.setText("<font color='black' size='5'>Closing price difference: "+str(round(out[0],2))+"</font>")    
        if(out[1]>0):
            self.l10.setText("<font color='green' size='5'>Max price difference: "+str(round(out[1],2))+"</font>")
            pos = pos + 1
        if(out[1]<0):
            self.l10.setText("<font color='red' size='5'>Max price difference: "+str(round(out[1],2))+"</font>")
            neg = neg + 1
        if(out[1]==0):
            self.l10.setText("<font color='black' size='5'>Max price difference: "+str(round(out[1],2))+"</font>")
        if(out[2]>0):
            self.l11.setText("<font color='green' size='5'>Min price difference: "+str(round(out[2],2))+"</font>")
            pos = pos + 1
        if(out[2]<0):
            self.l11.setText("<font color='red' size='5'>Min price difference: "+str(round(out[2],2))+"</font>")
            neg = neg + 1
        if(out[2]==0):
            self.l11.setText("<font color='black' size='5'>Min price difference: "+str(round(out[2],2))+"</font>")
        
        if(pos>neg):
            self.l12.setText("<font color='green' size='5'>Stock predicted to rise</font>")
        if(pos<neg):
            self.l12.setText("<font color='red' size='5'>Stock predicted to fall</font>")
        if(pos==neg):
            self.l12.setText("<font color='black' size='5'>Stock predicted to be neutral</font>")
        
        self.reloadbtn.show()

    def restart_program(self):
    	python = sys.executable
    	os.execl(python, python, * sys.argv)

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()    