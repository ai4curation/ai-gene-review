# AlphaFold Database Integration for Gene Annotation Review

## Overview

The AlphaFold Database (AFDB) now includes proteome-scale quaternary structure predictions (protein complexes), not just monomers. This creates opportunities to use predicted structural information as evidence when reviewing GO annotations and ARBA rules.

Reference: Han, Tsenkov, Venanzi et al. "AlphaFold Database expands to proteome-scale quaternary structures" (NVIDIA Digital Biology / EBI)

## Use Cases

### 1. Structural Validation of GO Annotations

When reviewing GO annotations (especially Molecular Function and Cellular Component), AFDB structures can validate or challenge claims:

- **Binding site annotations**: Does the predicted structure actually have the binding pocket for the claimed substrate? AFDB + predicted ligand binding sites can confirm GO MF annotations (e.g., "ATP binding" should have a recognizable nucleotide-binding fold).
- **Complex membership**: AFDB quaternary structures show which proteins form complexes. This directly validates GO CC annotations (e.g., "proteasome complex") and can flag ARBA rules that assign complex membership to proteins absent from predicted complexes.
- **Enzyme active sites**: For ARBA rules assigning catalytic activity GO terms, the predicted structure can show whether active site residues are present and correctly positioned.

### 2. Cross-Species Annotation Transfer Confidence

ARBA rules often transfer annotations across species based on sequence similarity (InterPro signatures). AFDB adds a structural dimension:

- If the predicted structure of a target protein is structurally similar to the source (not just sequence-similar), the annotation transfer is higher confidence.
- Conversely, if structures diverge despite sequence similarity (e.g., different fold topology), the rule should be flagged for manual review.
- This is especially relevant for distant homologs where sequence identity is low but structural conservation may still hold.

### 3. Protein-Protein Interaction Evidence

The new quaternary structure predictions can:

- Validate or challenge "protein binding" (GO:0005515) annotations — does the predicted complex interface actually exist?
- Provide structural evidence for signaling pathway annotations — do the predicted interaction surfaces make biological sense?
- Identify which interaction partners are biologically plausible vs. artifacts of sequence-based transfer rules.

### 4. Disorder / Intrinsically Disordered Region Context

AFDB per-residue confidence scores (pLDDT) mark disordered regions:

- Annotations about structured protein domains should not map to low-confidence (disordered) regions.
- Membrane protein annotations should correlate with predicted transmembrane helices.
- "DNA binding" or "RNA binding" annotations can be cross-checked against predicted nucleic acid binding surfaces.

### 5. Flagging Structurally Implausible ARBA Rules

Some ARBA rules assign GO terms that are structurally implausible for the target proteins:

- Rule assigns "transmembrane transport" but AFDB shows no transmembrane helices.
- Rule assigns "kinase activity" but predicted structure lacks a kinase fold.
- Rule assigns membership in a specific complex but quaternary predictions don't include the target protein.

These structural mismatches can serve as independent evidence for recommending rule deprecation or modification.

## Practical Integration

### API Access

AFDB entries can be fetched per UniProt accession:

```bash
# Monomer structure
curl https://alphafold.ebi.ac.uk/api/prediction/{uniprot_id}

# Download PDB/mmCIF
curl https://alphafold.ebi.ac.uk/files/AF-{uniprot_id}-F1-model_v4.pdb

# Per-residue confidence (pLDDT) is in the B-factor column of the PDB file
```

### Integration with Review Workflow

For each gene in an ARBA rule review:

1. **Fetch AFDB entry** via UniProt accession (already available from the UniProt record in the gene folder)
2. **Extract structural features**: fold classification, predicted binding sites, transmembrane regions, disordered regions (pLDDT < 70)
3. **Compare against GO terms** being assigned by the rule
4. **Flag mismatches** in the review output

### Evidence Type

AFDB-derived evidence would be classified as:
- `evidence_source: COMPUTATIONAL` (predicted structure, not experimental)
- Could reference the AFDB accession as a dataset
- pLDDT confidence scores provide a built-in quality metric

## Relationship to Other Projects

- **dismech**: AFDB structures could enrich disease mechanism entries — e.g., showing how a mutation disrupts a predicted protein interface (relevant to the STRUCTURAL_BIOLOGY project)
- **NAM (New Approach Methodologies)**: AFDB is a computational NAM — predicted structures as alternatives to experimental structure determination
- **linkml-term-validator**: Could potentially validate that GO MF terms are structurally plausible for the annotated protein

## Action Items

- [ ] Add AFDB lookup to the gene review bioinformatics pipeline (fetch structure per UniProt ID)
- [ ] Create a skill or script that extracts structural features relevant to GO term validation
- [ ] Pilot on 5-10 ARBA rule reviews: does structural evidence change the review outcome?
- [ ] Explore using AFDB quaternary structures for complex membership validation
- [ ] Evaluate whether pLDDT-based disorder prediction adds value for flagging incorrect domain annotations
- [ ] Consider adding structural evidence as a field in the gene review YAML schema
