. .venv/Scripts/activate
echo "Check formatting"
black --check .
echo "Reformat code"
black *.py
black */*.py
black */*/*.py
echo "Check formatting"
black --check .
echo "Check Linting"
flake8
deactivate