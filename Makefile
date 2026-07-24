.PHONY: install run dev clean

# Install noHXW as a pip package (editable for development)
install:
	pip install -e .

# Or install from requirements.txt (lighter weight)
install-lite:
	pip install -r requirements.txt

# Run production server
run:
	noxhw

# Run with hot-reload for development
dev:
	uvicorn app.main:app --reload --port 3000

# Clean up
clean:
	rm -rf *.egg-info __pycache__ .venv build dist
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
