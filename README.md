# Mini CSV Cleaner

A small Python command-line utility for applying simple, repeatable cleanup rules to CSV files.

**Independent demonstration project** · Python 3.10+ · Standard library only · MIT license

## What it does

- Trims leading and trailing whitespace from each cell.
- Skips fully blank rows.
- Optionally removes duplicate rows with `--dedupe` after whitespace is trimmed.
- Reads UTF-8 files with an optional UTF-8 BOM (`utf-8-sig`) and writes UTF-8 output.
- Keeps the source intact: input and output paths must differ.
- Refuses to overwrite an existing output file.

## Requirements

- Python 3.10 or later
- No third-party package installation required

## Quick start

Show command options:

```bash
python main.py --help
```

Clean a file without deduplication:

```bash
python main.py input.csv cleaned.csv
```

Trim fields, skip blank rows, and remove duplicate rows:

```bash
python main.py input.csv cleaned.csv --dedupe
```

Choose a new output filename each time. The tool intentionally stops if the output file already exists.

## Example

Input:

```csv
name, value
 Alice , 10

Alice,10
```

Command:

```bash
python main.py input.csv cleaned.csv --dedupe
```

Output:

```csv
name,value
Alice,10
```

## Tests

Run the unit tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

The current tests cover trimming/blank-row handling with deduplication, rejecting an existing output file, and rejecting identical input/output paths.

## Scope and limitations

This is a deliberately small CSV utility. It does not infer data types, standardize date formats, repair malformed rows, or decide whether two different-looking values represent the same entity. Deduplication compares the complete row after whitespace trimming. Review output before using it in a business workflow.

## Related Quantix projects

- [Quantix 100 Mini Python Projects](https://github.com/000MAK/quantix-100-new-mini-projects)
- [Mini JSON–CSV Converter](https://github.com/000MAK/mini-json-csv-converter)
- [All public repositories](https://github.com/000MAK?tab=repositories)

## Safety

Use synthetic examples for public demonstrations. Do not commit credentials, private data, or customer files. The output is a convenience tool and should be validated against your actual requirements before production use.

## License

MIT. See [LICENSE](LICENSE).
