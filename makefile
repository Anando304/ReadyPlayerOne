PY = python3
PT = pytest
PIP = pip3
PYFLAGS = --cov-report html --cov=src/ 
DOXY = doxygen
DOXYCFG = doxConfig

RMDIR = rm -rf

.PHONY: install run

run:
	cd src && $(PY) main.py
	
install:
	$(PIP) install -r requirements.txt

test:
	$(PT) $(PYFLAGS) src/tests/test.py
