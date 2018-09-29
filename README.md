# Instructions: 

## Requirement: 
    virtualenv==15.1.0
    MAC OS/Linux

## Instructions to set-up:

### For MAC OS:

    git clone git@github.com:rupamk/RUPKUNSDE003.git
    cd RUPKUNSDE003
    PYVER=2.7
    PYTHON=/opt/local/Library/Frameworks/Python.framework/Versions/$PYVER/bin/python$PYVER
    pip install virtualenv
    virtualenv --python=$PYTHON venv
    source venv/bin/activate
    cp fwpy ./venv/bin/
    chmod +x ./venv/bin/fwpy
    pip install -r requirements.txt

### For Linux OS:

1. UBUNTU 18.04

	virtualenv venv
	source venv/bin/activate
	pip install -r requirements_linux.txt
	pip install -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-18.04 wxPython

2. UBUNTU 16.04

	virtualenv venv
	source venv/bin/activate
	pip install -r requirements_linux.txt
	pip install -f https://wxpython.org/pages/downloads/ wxPython

## Running Sample:GetFbPostGUI

### For MAC OS:

    fwpy GetFbPostGUI/GUI.py 
    
### For Linux OS:

	python GetFbPostGUI/GUI.py 

### GetFbPostGUI UserInterface

![alt text](https://github.com/rupamk/RUPKUNSDE003/blob/master/GetFbPostGUI/GetFbPostGUI.png)
        
## Running Sample:TopQuotesGUI

### For MAC OS:

    fwpy TopQuotesGUI/GUI.py 
    
### For Linux OS:

	python TopQuotesGUI/GUI.py 

### TopQuotesGUI UserInterface

![alt text](https://github.com/rupamk/RUPKUNSDE003/blob/master/TopQuotesGUI/QuotesGUI.png)

## To Exit VirtualEnv:

    deactivate


    

