.PHONY: clean cleaner

all:
	python3 support/tutorial_tools/notebook/process_notebook.py index multifoxs foxs

clean:
	rm -f index.md foxs.md multifoxs.md Doxyfile
	rm -rf html

cleaner:
	rm -f index.ipynb foxs.ipynb multifoxs.ipynb foxs.sh multifoxs.sh foxs.md multifoxs.md index.md Doxyfile
	rm -rf html

