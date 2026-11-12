# Build the AIGR paper. `make` = data + stats + pdf.
PY = uv run python
all: stats pdf
data/annotations.tsv:
	$(PY) scripts/extract_annotations.py
data/goa_meta.tsv:
	$(PY) scripts/extract_goa_meta.py
data: data/annotations.tsv data/goa_meta.tsv
stats: data
	$(PY) scripts/compute_stats.py
	$(PY) scripts/figures.py
pdf:
	latexmk -pdf -interaction=nonstopmode main.tex
refresh:
	rm -rf data && $(MAKE) all
clean:
	latexmk -C
.PHONY: all data stats pdf refresh clean
explainer: stats
	$(PY) scripts/build_explainer.py
.PHONY: explainer
