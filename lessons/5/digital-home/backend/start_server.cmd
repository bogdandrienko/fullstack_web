python -m venv env
call env/scripts/activate
pip install fastapi



uvicorn main:app --host=0.0.0.0 --port=8000 --reload --log-level info



cmd