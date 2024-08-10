BASEYEAR=2023
FOR=today
FILES = *.py *.cfg
PYTHON3 = python3
PYVERSION = 3.8
GIT = git
TWINE = twine

A = errnocode.py
B = exitcode.py
C = hex2words.py

default: build

doc:
	$(PYTHON3) exitcode.py --showref | { : \
	; echo "## exitcode"; echo "" \
	; $(PYTHON3) exitcode.py --help ; echo "" \
	; echo "| num | name | ref | description" \
	; echo "| --: | ---- | --- | -----------" \
	; while read -r num name ref desc; do : \
	; echo "| $$num | $$name | $$ref | $$desc" \
	; done ; } > exitcode.md
	$(PYTHON3) errnocode.py --showref | { : \
	; echo "## errnocode"; echo "" \
	; $(PYTHON3) errnocode.py --help ; echo "" \
	; echo "| num | name | ref | description" \
	; echo "| --: | ---- | --- | -----------" \
	; while read -r num name ref desc; do : \
	; echo "| $$num | $$name | $$ref| $$desc" \
	; done ; } > errnocode.md


############# version

version:
	@ grep -l __version__ $(FILES) | { while read f; do : \
	; THISYEAR=`date +%Y -d "$(FOR)"` ; YEARS=$$(expr $$THISYEAR - $(BASEYEAR)) \
        ; WEEKnDAY=`date +%W%u -d "$(FOR)"` ; sed -i \
	-e "/^version /s/[.]-*[0123456789][0123456789][0123456789]*/.$$YEARS$$WEEKnDAY/" \
	-e "/^ *__version__/s/[.]-*[0123456789][0123456789][0123456789]*\"/.$$YEARS$$WEEKnDAY\"/" \
	-e "/^ *__version__/s/[.]\\([0123456789]\\)\"/.\\1.$$YEARS$$WEEKnDAY\"/" \
	-e "/^ *__copyright__/s/(C) \\([123456789][0123456789]*\\)-[0123456789]*/(C) \\1-$$THISYEAR/" \
	-e "/^ *__copyright__/s/(C) [123456789][0123456789]* /(C) $$THISYEAR /" \
	$$f; done; }
	@ grep ^__version__ $(FILES) | grep -v _tests.py
	@ ver=`grep "version.*=" setup.cfg | sed -e "s/version *= */v/"` \
	; echo ": ${GIT} commit -m $$ver"

commit:
	@ ver=`grep "version.*=" setup.cfg | sed -e "s/version *= */v/"` \
	; echo ": ${GIT} commit -m $$ver"
tag:
	@ ver=`grep "version.*=" setup.cfg | sed -e "s/version *= */v/"` \
	; rev=`git rev-parse --short HEAD` \
	; echo ": ${GIT} tag $$ver $$rev"

############## https://pypi.org/...

README: README.MD Makefile
	cat README.MD | sed -e "/\\/badge/d" -e /^---/q > README
setup.py: Makefile
	{ echo '#!/usr/bin/env python3' \
	; echo 'import setuptools' \
	; echo 'setuptools.setup()' ; } > setup.py
	chmod +x setup.py
setup.py.tmp: Makefile
	echo "import setuptools ; setuptools.setup()" > setup.py

.PHONY: build
build:
	rm -rf build dist *.egg-info
	$(MAKE) $(PARALLEL) README setup.py
	# pip install --root=~/local . -v
	$(PYTHON3) setup.py sdist
	- rm -v setup.py README
	$(TWINE) check dist/*
	: $(TWINE) upload dist/*

ins install:
	$(MAKE) setup.py
	$(PYTHON3) -m pip install --no-compile --user .
	rm -v setup.py
	$(MAKE) show | sed -e "s|[.][.]/[.][.]/[.][.]/bin|$$HOME/.local/bin|"
show:
	test -d tmp || mkdir -v tmp
	cd tmp && $(PYTHON3) -m pip show -f $$(sed -e '/^name *=/!d' -e 's/.*= *//' ../setup.cfg)
uns uninstall: 
	test -d tmp || mkdir -v tmp
	cd tmp && $(PYTHON3) -m pip uninstall -v --yes $$(sed -e '/^name *=/!d' -e 's/.*= *//' ../setup.cfg)

# ...........................................
mypy:
	zypper install -y mypy
	zypper install -y python3-click python3-pathspec

MYPY = mypy
MYPY_STRICT = --strict --show-error-codes --show-error-context --no-warn-unused-ignores --python-version $(PYVERSION) --implicit-reexport
AUTOPEP8=autopep8
AUTOPEP8_INPLACE= --in-place

%.type:
	$(MYPY) $(MYPY_STRICT) $(MYPY_OPTIONS) $(@:.type=)

%.pep8:
	$(AUTOPEP8) $(AUTOPEP8_INPLACE) $(AUTOPEP8_OPTIONS) $(@:.pep8=)
	$(GIT) --no-pager diff $(@:.pep8=)

type: 
	$(MAKE) $A.type $B.type $C.type
pep8 style: 
	$(MAKE) $A.pep8 $B.pep8 $C.pep8
