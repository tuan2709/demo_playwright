python3 -m venv venv
venv/bin/pip install playwright pytest
venv/bin/python -m playwright install
venv/bin/pytest demo_playwright.py
