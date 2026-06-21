# ============ Hint for for Windows Users ============

# On Windows the "sh" shell that comes with Git for Windows should be used.
# If it is not on path, provide the path to the executable in the following line.
#set windows-shell := ["C:/Program Files/Git/usr/bin/sh", "-cu"]

# ============ Variables used in recipes ============

# Set shebang line for cross-platform Python recipes (assumes presence of launcher on Windows)
shebang := if os() == 'windows' {
  'py'
} else {
  '/usr/bin/env python3'
}


# ============== Project recipes ==============

# List all commands as default command. The prefix "_" hides the command.
_default: _status
    @just --list

# Initialize a new project (use this for projects not yet under version control)
[group('project management')]
setup: _git-init _ai-instructions install _git-add
  git commit -m "Initialise git with minimal project" -a

  
# Install project dependencies
[group('project management')]
install:
  uv sync --group dev


# Run all tests
[group('model development')]
test: pytest doctest mypy format

test-full: test pytest-integration test-examples

pytest:
  uv run pytest tests

# Run integration tests (replays VCR cassettes)
pytest-integration:
	uv run pytest -m integration --vcr-record=none

# Record VCR cassettes for integration tests (requires network)
record-cassettes:
	uv run pytest -m integration --vcr-record=new_episodes -x -v

# Re-record all VCR cassettes from scratch (requires network)
rerecord-cassettes:
	uv run pytest -m integration --vcr-record=all -x -v

doctest:
  uv run pytest  --doctest-modules src

mypy:
  uv run mypy src tests --exclude "src/ai_gene_review/(datamodel|tools|export)/"

format:
	uv run ruff check .

# Validate SSSOM mapping files: (1) structural validation against the SSSOM schema, and
# (2) ontology term validation (every ARO/GO CURIE resolves and its label matches) via
# linkml-term-validator on the regenerated nested term-tuple file.
validate-mappings:
	uv run linkml-validate -s "$(uv run python -c 'import sssom_schema,os;print(os.path.join(os.path.dirname(sssom_schema.__file__),"schema","sssom_schema.yaml"))')" -C "mapping set" projects/ANTIMICROBIAL_RESISTANCE/*.sssom.yaml
	uv run python projects/ANTIMICROBIAL_RESISTANCE/sssom_to_terms.py projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml -o projects/ANTIMICROBIAL_RESISTANCE/aro2go.terms.yaml
	uv run linkml-term-validator validate-data projects/ANTIMICROBIAL_RESISTANCE/aro2go.terms.yaml -s src/ai_gene_review/schema/aro_go_mapping.yaml -t AROGOMappingSet --labels -c conf/oak_config.yaml

# Validate the curated RHEA->GO gap-fill mapping set (projects/RHEA/rhea2go.sssom.yaml):
# (1) SSSOM structural validation, then (2) GO term/label validation on the regenerated nested file.
validate-rhea-mappings:
	uv run linkml-validate -s "$(uv run python -c 'import sssom_schema,os;print(os.path.join(os.path.dirname(sssom_schema.__file__),"schema","sssom_schema.yaml"))')" -C "mapping set" projects/RHEA/*.sssom.yaml
	uv run python projects/RHEA/sssom_to_terms.py projects/RHEA/rhea2go.sssom.yaml -o projects/RHEA/rhea2go.terms.yaml
	uv run linkml-term-validator validate-data projects/RHEA/rhea2go.terms.yaml -s src/ai_gene_review/schema/rhea_go_mapping.yaml -t RHEAGOMappingSet --labels -c conf/oak_config.yaml

# Validate the CAZy->GO mapping sets (projects/GLYCOBIOLOGY/cazy2go*.sssom.yaml):
# (1) SSSOM structural validation of all three sets, then (2) GO term/label validation on the
# regenerated nested files (seed, safe propagation set, and full generated derivation).
validate-cazy-mappings:
	uv run linkml-validate -s "$(uv run python -c 'import sssom_schema,os;print(os.path.join(os.path.dirname(sssom_schema.__file__),"schema","sssom_schema.yaml"))')" -C "mapping set" projects/GLYCOBIOLOGY/cazy2go.sssom.yaml projects/GLYCOBIOLOGY/cazy2go.safe.sssom.yaml projects/GLYCOBIOLOGY/cazy2go.generated.sssom.yaml
	for base in cazy2go cazy2go.safe cazy2go.generated; do \
	  uv run python projects/GLYCOBIOLOGY/sssom_to_terms.py projects/GLYCOBIOLOGY/$base.sssom.yaml -o projects/GLYCOBIOLOGY/$base.terms.yaml; \
	  uv run linkml-term-validator validate-data projects/GLYCOBIOLOGY/$base.terms.yaml -s src/ai_gene_review/schema/cazy_go_mapping.yaml -t CAZYGOMappingSet --labels -c conf/oak_config.yaml; \
	done

# Validate the hand-curated Pfam entry reviews (interpro/pfam/<PFAM>/<PFAM>-review.yaml):
# (1) structural + premise checks (Pfam membership, member list, GO non-obsolete/aspect, parent
# entry carries no equivalent term, gene_review paths exist, REJECTED backed by a same-family
# counter-example) and index refresh via validate_pfam_reviews.py, then (2) LinkML structural
# validation and (3) GO term/label validation of each review.
validate-pfam-reviews:
	uv run python projects/PFAM/validate_pfam_reviews.py
	for f in interpro/pfam/*/*-review.yaml; do \
	  uv run linkml-validate -s src/ai_gene_review/schema/pfam_entry_review.yaml -C PfamEntryReview "$f"; \
	  uv run linkml-term-validator validate-data "$f" -s src/ai_gene_review/schema/pfam_entry_review.yaml -t PfamEntryReview --labels -c conf/oak_config.yaml; \
	done

# Validate the curated NCBIFAM->GO seed mapping set (projects/NCBIFam/ncbifam2go.sssom.yaml):
# (1) SSSOM structural validation, then (2) GO term/label validation on the regenerated nested file.
validate-ncbifam-mappings:
	uv run linkml-validate -s "$(uv run python -c 'import sssom_schema,os;print(os.path.join(os.path.dirname(sssom_schema.__file__),"schema","sssom_schema.yaml"))')" -C "mapping set" projects/NCBIFam/*.sssom.yaml
	uv run python projects/NCBIFam/sssom_to_terms.py projects/NCBIFam/ncbifam2go.sssom.yaml -o projects/NCBIFam/ncbifam2go.terms.yaml
	uv run linkml-term-validator validate-data projects/NCBIFam/ncbifam2go.terms.yaml -s src/ai_gene_review/schema/ncbifam_go_mapping.yaml -t NCBIFAMGOMappingSet --labels -c conf/oak_config.yaml
# Validate the curated InterPro2GO mapping review (projects/INTERPRO/interpro2go.sssom.yaml):
# (1) SSSOM structural validation, then (2) GO term/label validation on the regenerated nested file.
validate-interpro-mappings:
	uv run linkml-validate -s "$(uv run python -c 'import sssom_schema,os;print(os.path.join(os.path.dirname(sssom_schema.__file__),"schema","sssom_schema.yaml"))')" -C "mapping set" projects/INTERPRO/*.sssom.yaml
	uv run python projects/INTERPRO/sssom_to_terms.py projects/INTERPRO/interpro2go.sssom.yaml -o projects/INTERPRO/interpro2go.terms.yaml
	uv run linkml-term-validator validate-data projects/INTERPRO/interpro2go.terms.yaml -s src/ai_gene_review/schema/interpro_go_mapping.yaml -t InterProGOMappingSet --labels -c conf/oak_config.yaml

# Apply the ARO->GO mapping: chain UniProt -> ARO (via DR CARD lines) -> GO across all genes.
aro2go-pipeline: validate-mappings
	uv run python projects/ANTIMICROBIAL_RESISTANCE/uniprot2aro2go.py --sssom projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml 'genes/**/*-uniprot.txt'

# Render the ARO->GO mapping set to a curator-facing HTML page.
render-mappings:
	uv run python projects/ANTIMICROBIAL_RESISTANCE/render_sssom_html.py --sssom projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml --gain-tsv projects/ANTIMICROBIAL_RESISTANCE/data/candidate_new_annotations.tsv -o projects/ANTIMICROBIAL_RESISTANCE/aro2go.html

# Report the candidate GO annotations UniProt would gain from the mappings (uses the cached snapshot).
annotation-gain:
	uv run python projects/ANTIMICROBIAL_RESISTANCE/annotation_gain_report.py --sssom projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml --uniprot projects/ANTIMICROBIAL_RESISTANCE/data/uniprot_card_xrefs.tsv --out-md projects/ANTIMICROBIAL_RESISTANCE/ANNOTATION_GAIN.md --out-tsv projects/ANTIMICROBIAL_RESISTANCE/data/candidate_new_annotations.tsv

# Publish the AR project's sub-products (markdown -> HTML via the project template + the SSSOM HTML)
# under pages/projects/ANTIMICROBIAL_RESISTANCE/ (next to the rendered project page).
render-ar-pages:
	uv run python -c "from pathlib import Path; from ai_gene_review.render_projects import render_project; [render_project(Path('projects/ANTIMICROBIAL_RESISTANCE')/f, output_dir=Path('pages/projects/ANTIMICROBIAL_RESISTANCE')) for f in ['README.md','ANNOTATION_GAIN.md','SPOT_REVIEW.md']]"
	cp projects/ANTIMICROBIAL_RESISTANCE/aro2go.html pages/projects/ANTIMICROBIAL_RESISTANCE/aro2go.html

# ============== Hidden internal recipes ==============

_status:
  @echo "OK"

# Update project template
_update-template:
  copier update --trust --skip-answered


# Run documentation server
_serve:
  uv run mkdocs serve

# Initialize git repository
_git-init:
  git init

# Add files to git
_git-add:
  git add .

# Commit files to git
_git-commit:
  git commit -m 'chore: just setup was run' -a

# Show git status
_git-status:
  git status

goosehints:
  [ -f .goosehints ] || ln -s CLAUDE.md .goosehints

copilot-instructions:
  [ -f .github/copilot-instructions.md ] || cd .github && ln -s ../CLAUDE.md copilot-instructions.md

_ai-instructions: goosehints copilot-instructions

gh-add-topics:
  gh repo edit --add-topic "ai-gene-review,monarchinitiative,linkml"

gh-add-secrets:
  gh secret set PAT_FOR_PR --body "$PAT_FOR_PR"
  gh secret set ANTHROPIC_API_KEY --body "$ANTHROPIC_API_KEY"
  gh secret set OPENAI_API_KEY --body "$OPENAI_API_KEY"
  gh secret set CBORG_API_KEY --body "$CBORG_API_KEY"
  gh secret set CLAUDE_CODE_OATH_TOKEN --body "$CLAUDE_CODE_OATH_TOKEN"

gh-invite-the-dragon:
  gh api repos/monarch-initiative/ai-gene-review/collaborators/dragon-ai-agent -X PUT -f permission=push

# ============== Include project-specific recipes ==============

import "project.justfile"
