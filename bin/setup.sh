python3.9 -m venv venv && \
source venv/bin/activate && \
pip install --upgrade pip && \
pip install -r requirements.txt && \
export FLASK_APP=service:create_app && \
export FLASK_DEBUG=1 && \
export DATABASE_URI=postgresql://postgres:postgres@localhost:5432/postgres

