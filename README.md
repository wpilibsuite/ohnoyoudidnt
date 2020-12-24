# ohnoyoudidnt

ohnoyoudidnt is a doc8 sphinx linter intended for use by [frc-docs](https://github.com/wpilibsuite/frc-docs). Its an expansion to the normal doc8 linter with custom checks intended to follow the frc-docs [styleguide](https://docs.wpilib.org/en/stable/docs/contributing/style-guide.html)

Project created by [TheTripleV](https://github.com/thetriplev)

## Usage

### Manual

1. Ensure [doc8](https://pypi.org/project/doc8/) is installed.
2. Install ohnoyoudidnt
```python
python -m pip install ohnoyoudidnt
```
3. Run the linter using
```
doc8
```

### VS Code

1. Follow instructions 1 and 2 from above
2. Install the `reStructuredText` VS Code extension
3. Add
```json
    "restructuredtext.linter.name": "doc8",
    "restructuredtext.linter.extraArgs": [
        "--ignore D001",
        "--ignore D004",
        "--ignore D002",
        "--ignore WUMBO002"
    ],
```
to your `settings.json` file.

## Contribution Guidelines
### Checks
- Checks can never yield a line number < 1
- Checks must compile regex patterns once per import, not once per file
