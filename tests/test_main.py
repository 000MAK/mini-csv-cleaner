import tempfile, unittest
from pathlib import Path
from main import clean_csv
class CsvCleanerTests(unittest.TestCase):
    def test_trim_blank_and_dedupe(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/"in.csv"; dst=Path(d)/"out.csv"
            src.write_text(" name , value \n Alice , 1 \n\nAlice,1\n",encoding="utf-8")
            self.assertEqual(clean_csv(src,dst,dedupe=True),2)
            self.assertEqual(dst.read_text(),"name,value\nAlice,1\n")
    def test_existing_output_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/"in.csv"; dst=Path(d)/"out.csv"
            src.write_text("a\n"); dst.write_text("keep")
            with self.assertRaises(FileExistsError): clean_csv(src,dst)
            self.assertEqual(dst.read_text(),"keep")
    def test_same_path_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/"x.csv"; src.write_text("a\n")
            with self.assertRaises(ValueError): clean_csv(src,src)
if __name__ == "__main__": unittest.main()
