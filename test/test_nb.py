import subprocess
import tempfile
import os
from glob import glob

def _exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test():
	notebooks = [y for x in os.walk('../') for y in glob(os.path.join(x[0], '*.ipynb'))]
	for notebook in notebooks:
		_exec_notebook(notebook)