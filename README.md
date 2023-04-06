# cli-tui-eg-py

Example of using `argparse` and `PyInquirer` to make a nice mixed CLI/TUI. As a bonus, we use Poetry to create this:

```sh
# Initiate new project using Poetry
poetry new cli-tui-eg-py
cd cli-tui-eg-py

# Add dependencies
poetry add argparse
poetry add PyInquirer

# Create a requirements.txt for pip users
poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt

# Run the code!
poetry run python cli_tui_eg_py/main.py -s Hello -n 100 -b -l 1 10 2
```

