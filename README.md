# Campy

This app serves as a security camera with pan and tilt functionality.
The app is designed to run on a Raspberry Pi.

## Running

First install the dependencies in your python environment:

    pip install -r requirements.txt
    
Next run the application
    
    python run.py
    
In order to run on the Raspberry Pi (without the mock)
    
    python run.py --camera pi --tripod pi
    
Note that this should be run as the 'pi' user, otherwise the camera is doing strange things.
    
    