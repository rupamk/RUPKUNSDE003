# Instructions

## Requirement: 
    virtualenv==15.1.0
    MAC OS

## Instructions to set-up:
    git clone git@github.com:rupamk/RUPKUNSDE003.git
    cd RUPKUNSDE003
    pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    cp fwpy ./venv/bin/
    chmod +x ./venv/bin/fwpy
    pip install -r requirements.txt

## Running Sample:GetFbPostGUI

    fwpy GetFbPostGUI/GUI.py 
        
## Running Sample:TopQuotesGUI

    fwpy TopQuotesGUI/GUI.py 

## To Exit VirtualEnv:

    deactivate


    
