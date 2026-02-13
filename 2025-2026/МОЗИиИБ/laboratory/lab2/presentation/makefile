PDF_FORMAT_OPTIONS = -t beamer --slide-level=2
FILTERS = --citeproc
PDF_ENGINE = --pdf-engine=xelatex
PDF_OPTIONS = --number-sections

FILENAME = presentation



.PHONY: pdf
pdf:
	pandoc $(FILENAME).md \
	$(FILTERS) \
	$(PDF_ENGINE) \
	$(PDF_OPTIONS) \
	$(PDF_FORMAT_OPTIONS) \
	--verbose \
	-o $(FILENAME).pdf

.PHONY: html
html: 
	pandoc $(FILENAME).md \
	-f markdown+pipe_tables \
	--embed-resources \
	--standalone \
	-t revealjs \
	--slide-level=2 \
	-V theme=league \
	-c style.css \
	-o $(FILENAME).html

.PHONY: pdf html all
all: pdf html

clean:
	rm $(FILENAME).pdf
	rm $(FILENAME).html


.PHONY: serve-html
serve-html:
	python3 -m http.server 8000