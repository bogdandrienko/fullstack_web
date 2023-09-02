cd ..
python3 -m venv venv
source env/bin/activate
uvicorn main:app --reload