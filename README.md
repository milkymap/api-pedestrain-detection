# api-pedestrain-detection
this is an implementation of pedestrian detection by background subtraction in Python

# installation
you need python 3.7+

clone the project : git clone https://github.com/Milkymap/api-pedestrain-detection.git 

enter in the project : cd api-pedestrian-detection

create the virtualenv : python -m venv env

activate the virtualenv : source env/bin/activate 

update pip : pip install --upgrade pip 

install dependencies : pip install -r requirements.txt

# make prediction and detection
python -m processing.process --source source_data/video/public_walk.mp4
