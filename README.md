# cli-tui-eg-py

Example of using `argparse` and `PyInquirer` to make a nice mixed CLI/TUI. As a bonus, we use Poetry to create this:

```sh
# Update Poetry first to solve issue https://github.com/python-poetry/poetry/issues/7572

poetry self update
# Initiate new project using Poetry
poetry new cli-tui-eg-py
cd cli-tui-eg-py

# Add dependencies
poetry add argparse
poetry add InquirerPy

# Create a requirements.txt for pip users
poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt

# Run the code!
poetry run python cli_tui_eg_py/main.py -c Hello -k 6 -p "they/them" 
```

This does not provide a framework which unifies `argparse` and `PyInquirer`! This just shows an example of using them both together.  