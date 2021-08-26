# Compare files
[![Actions Status](https://github.com/Krutov777/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/Krutov777/python-project-lvl2/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/cb8218bd9867d2c8302b/test_coverage)](https://codeclimate.com/github/Krutov777/python-project-lvl2/test_coverage)
[![Actions Status](https://github.com/Krutov777/python-project-lvl2/workflows/linter/badge.svg)](https://github.com/Krutov777/python-project-lvl2/actions)
[![Actions Status](https://github.com/Krutov777/python-project-lvl2/workflows/tests/badge.svg)](https://github.com/Krutov777/python-project-lvl2/actions)

**Files comparison** is a CLI-utility that compares two configuration files.
## Installation
To install the utility use:
```
pip install -i https://test.pypi.org/simple/ krutov_gendiff
```
## Usage
To run the utility after installing:
`gendiff first_file second_file`.(You must be in the directory with the files you want to compare or specify an absolute path)

Files formats can be either *.json* or *.yml / .yaml*.

The result of comparison can also be displayed in different formats. To choose format add an optional argument `--format`:
- **_json_** for json format
- **_plain_** for plain format
- **_default_** for json-like txt format. This format is used as a default.

E.g. `gendiff first_file second_file --format plain`

You can always call `gendiff -h` for some __help__ information.

**Diff between two files (json or yaml) with text format output:**
```
gendiff before.json after.yaml
```
```
gendiff before.json after.yaml --format text
```
**Diff between two files (json or yaml) with plain format output:**
```
gendiff before.json after.yaml --format plain
```
**Diff between two files (json or yaml) with json format output:**
```
gendiff before.json after.yaml --format json
```
[![asciicast](https://asciinema.org/a/QKEMKLmaDOiR99iTEyu1GuSWL.svg)](https://asciinema.org/a/QKEMKLmaDOiR99iTEyu1GuSWL)
