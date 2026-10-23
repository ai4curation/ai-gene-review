# Vmn2r73 (A0A3B2WCZ5): evidence and exact-input prediction review

The domain-containing name is supported, but the glutamate GPCR function paragraph assigns autonomous membrane signaling to a product lacking the required seven-transmembrane module.

## Input identity and functional boundary

A0A3B2WCZ5 is 496 residues, compared with the 851-residue Vmn2r73 reference D3Z7M3 linked to the same MGI gene. The first 429 residues are identical. A later 43-residue segment retains 41 identities, but the complete reference seven-transmembrane region is absent. Sparse matches in a global alignment of the alternative tail do not constitute a transmembrane module. The signal peptide and ligand-binding domain are retained.

## Biological evidence

- [PMID:30675062 — Structural insights into the activation of metabotropic glutamate receptors.](https://pubmed.ncbi.nlm.nih.gov/30675062/): Class C receptor signaling requires a seven-transmembrane module distinct from the extracellular ligand-binding region; the experimental study concerns mGlu5 rather than Vmn2r73.

> the GPCR-defining 7TM domain

- [PMID:9288755 — A novel family of putative pheromone receptors in mammals with a topographically organized and sexually dimorphic distribution.](https://pubmed.ncbi.nlm.nih.gov/9288755/): The founding rat V2R study identifies a receptor family related to, but distinct from, metabotropic glutamate receptors.

> genes encoding seven transmembrane receptors with sequence similarity with
> Ca2+-sensing and metabotropic glutamate receptors

## Exact non-GO claims

The complete emitted record is preserved in [Vmn2r73-protnlm-source.json](Vmn2r73-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Receptor ligand binding region domain-containing protein

CNN (CS 2). The wording identifies the retained receptor ligand-binding region without claiming that an intact GPCR or a particular ligand specificity is present. The exact sequence retains this annotated domain in the same-gene reference.

### Function

> G-protein coupled receptor for glutamate. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of down-stream effectors. Signaling inhibits adenylate cyclase activity

NPI (CS 0). The compound claim requires an autonomous G-protein-coupled receptor, whereas the exact input lacks the seven-transmembrane signaling module. The extracellular class C fold also does not establish glutamate specificity or inhibition of adenylate cyclase. The emitted donor accession is Q14833; it does not substitute for domain completeness in the target. [Sequence analysis](Vmn2r73-bioinformatics/RESULTS.md); [class C signaling study](https://pubmed.ncbi.nlm.nih.gov/30675062/).

No GO or EC term was emitted in this record; the name, function and location assessments above constitute its prediction review.

## Family integration

V2R family membership and retention of its ligand-binding region are separable from an intact class C receptor architecture. A partial gene product can preserve family identity while losing the domain needed for the ancestral activity. Neither the V2R designation nor similarity to glutamate receptors establishes the ligand of this particular product.

## Evidence limits

No assay or localization study of the exact 496-residue product was found. The genuine Falcon report describes conventional seven-transmembrane receptor biology but does not account for this input sequence boundary; its full-length signaling conclusions cannot be transferred. The 1997 V2R publication is abstract-only in the cache. Stable expression and any accessory role of the shortened product remain unresolved.

Exact sequence mapping: [Vmn2r73-bioinformatics/RESULTS.md](Vmn2r73-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 file or prediction-evidence folder was opened for this section. New analysis:
`Vmn2r73-bioinformatics/compare_sequences_rereview.py` → `RESULTS-rereview.md` (sequences fetched
from UniProt REST).

### Identity (alternative gene model)

- A0A3B2WCZ5 (496 aa) = Ensembl ENSMUST00000232965 (Vmn2r73-203), a non-canonical transcript of
  ENSMUSG00000070458. Ensembl canonical is ENSMUST00000077478 (Vmn2r73-201) → UniProt D3Z7M3, 851 aa.
  There are 8 TrEMBL Vmn2r73 gene models (475–851 aa); none is Swiss-Prot reviewed.
- Target 1–429 = canonical 1–429 (signal peptide + Venus-flytrap ligand-binding domain); canonical
  430–505 skipped; target 430–470 = canonical 506–546 (nine-cysteine domain, Pfam NCD3G 432–474 on
  target); then a ~26-aa divergent tail.
- No transmembrane segment: UniProt has no TRANSMEM on the target (7 on D3Z7M3), and the only
  KD window ≥1.6 is the signal peptide (positive control: 69 windows in canonical 561–851).
- So the product, if made, is a soluble/luminal extracellular-domain-only V2R fragment.

### Evolutionary placement

- PANTHER PTHR24061 (CALCIUM-SENSING RECEPTOR-RELATED) : SF413 (VOMERONASAL 2, RECEPTOR 66-RELATED),
  for the target and all Vmn2r73 models. The family review `interpro/panther/PTHR24061/PTHR24061-review.yaml`
  places it in the same subfamily; no disagreement.
- No experimentally characterised member of SF413 is known to me; the deorphanised V2Rs
  (Vmn2r116/ESP1 receptor, SF398; Vmn2r1, family C, SF546) are in other subfamilies, so no
  ligand specificity can be transferred. mGlu/CaSR structural work is used only for class C
  domain architecture (VFT binds ligand, 7TM couples G protein; PMID:30675062).
- No IBA rows exist for this accession; no GO-CAM or module includes Vmn2r73.

### Decisions

| Term | Prior | Now | Why |
|---|---|---|---|
| GO:0004930 GPCR activity (IEA InterPro) | REMOVE | REMOVE | product lacks 7TM; domain-architecture mismatch |
| GO:0007186 GPCR signaling pathway (IEA InterPro) | UNDECIDED | REMOVE | same basis as MF; no evidence for any decoy/partner role |
| GO:0005886 plasma membrane (IEA SubCell, ARBA) | UNDECIDED | MARK_AS_OVER_ANNOTATED | multi-pass topology false; partner-mediated surface retention untested |
| GO:0016020 membrane (IEA InterPro) | UNDECIDED | MARK_AS_OVER_ANNOTATED | no anchor; signal-peptide product |

Description rewritten as a gene-level summary that states the gene-model identity. core_functions
left empty: no function is established for this product. Literature: the Falcon report found no
Vmn2r73-specific study; Vmn2r73 is an orphan V2R.

### Relative to review next

Canonical same-gene product D3Z7M3 (Vmn2r73-201, 851 aa, full 7TM) has no review in the repo →
`genes/mouse/Vmn2r73__D3Z7M3` (relation same_gene_canonical).
