.PHONY: setup install run dev clean

# ── Bootstrap (works even without pip installed) ──────────────────────
setup:
	chmod +x setup.sh && ./setup.sh

# ── Install as pip package (requires pip) ─────────────────────────────
install:
	pip install -e .

install-lite:
	pip install -r requirements.txt

# ── Run ───────────────────────────────────────────────────────────────
run:
	.venv/bin/noxhw

dev:
	.venv/bin/uvicorn app.main:app --reload --port 3000

# ── Clean ─────────────────────────────────────────────────────────────
clean:
	rm -rf *.egg-info __pycache__ .venv build dist
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
