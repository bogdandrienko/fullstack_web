cd ..
python -m venv venv
call env/scripts/activate
uvicorn main:app --reload