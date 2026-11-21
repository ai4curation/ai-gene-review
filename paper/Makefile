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
goa: release/goa_counts.yaml
release/goa_counts.yaml:
	$(PY) scripts/fetch_goa_counts.py
stats: data release/goa_counts.yaml
	$(PY) scripts/compute_stats.py
	$(PY) scripts/figures.py
	$(PY) scripts/figures_structured.py
	$(PY) scripts/audit_residue_claims.py
	$(PY) scripts/alignment_manifest.py
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
