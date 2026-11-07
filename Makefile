install:
	cd backend && python -m venv .venv && .venv/bin/pip install -r requirements.txt
	cd frontend && npm install

back:
	cd backend && .venv/bin/uvicorn main:app --reload --port 8000

front:
	cd frontend && npm run dev

build:
	cd frontend && npm run builds
