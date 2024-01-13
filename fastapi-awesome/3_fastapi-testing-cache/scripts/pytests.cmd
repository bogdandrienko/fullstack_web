cd ..
python -m venv env
call env/scripts/activate
pip install -r requirements.txt
pip install pytest pytest-asyncio anyio pytest-tornasync pytest-trio pytest-twisted twisted


pytest test_messages.py


cmd
