import os
import shutil
import sys

include_tests = '{{ cookiecutter.include_tests }}' 
if include_tests == 'no' and os.path.exists("tests"):
    shutil.rmtree("tests")
    sys.exit(0)
