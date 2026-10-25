import argparse, csv
from pathlib import Path

def clean_csv(source, destination, dedupe=False):
    src, dst = Path(source).resolve(), Path(destination).resolve()
    if src == dst: raise ValueError("Input and output paths must be different")
    if not src.is_file(): raise FileNotFoundError(src)
    if dst.exists(): raise FileExistsError(dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    seen=set(); rows_written=0
    with src.open("r", encoding="utf-8-sig", newline="") as inp, dst.open("w", encoding="utf-8", newline="") as out:
        reader=csv.reader(inp); writer=csv.writer(out)
        for row in reader:
            row=[cell.strip() for cell in row]
            if not row or not any(row): continue
            key=tuple(row)
            if dedupe and key in seen: continue
            seen.add(key); writer.writerow(row); rows_written += 1
    return rows_written

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("input"); ap.add_argument("output"); ap.add_argument("--dedupe", action="store_true")
    a=ap.parse_args(); print(f"Wrote {clean_csv(a.input,a.output,a.dedupe)} rows to {a.output}")
if __name__ == "__main__": main()
