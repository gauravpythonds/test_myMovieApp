
VENV="venv"

python3 -m pip install --upgrade pip

if [ ! -d $VENV ]
then
	python3 -m venv venv
fi

source ./venv/bin/activate
pip3 install -r requirements.txt

python3 myMovieApp/run.py
