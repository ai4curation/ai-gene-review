# Build the AIGR paper. `make` = data + stats + pdf.
PY = uv run python
all: stats pdf
data/annotations.tsv:
	$(PY) scripts/extract_annotations.py
data/goa_meta.tsv:
	$(PY) scripts/extract_goa_meta.py
data/predictions.tsv:
	$(PY) scripts/extract_structured.py
data: data/annotations.tsv data/goa_meta.tsv data/predictions.tsv
stats: data
	$(PY) scripts/compute_stats.py
	$(PY) scripts/figures.py
	$(PY) scripts/figures_structured.py
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
