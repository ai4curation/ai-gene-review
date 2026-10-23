# UBE2F (F8WDQ9): evidence and exact-input prediction review

F8WDQ9 is a 101-residue UBE2F product, not an intact ubiquitin-conjugating enzyme. The selected sequence lacks the canonical NEDD8 E2 catalytic cysteine. The ubiquitin-transferase prediction is contradicted; participation of this short product in protein ubiquitination remains uncertain.

## Input identity and functional boundary

The selected accession F8WDQ9 and reviewed Q969M7 share HGNC:12480. Their first 94 residues are identical, followed by an alternative seven-residue selected tail. The reference UBC core spans residues 32–185; catalytic Cys116 lies outside the retained segment. The short sequence is the reviewed target throughout. No inference that it is an expressed dominant-negative protein is made.

## Biological evidence

- [PMID:19250909 — E2-RING expansion of the NEDD8 cascade confers specificity to cullin modification.](https://pubmed.ncbi.nlm.nih.gov/19250909/): Biochemical and cellular experiments identify full-length UBE2F as a NEDD8-conjugating E2, not a ubiquitin E2.

> the previously uncharacterized E2 UBE2F is a NEDD8-conjugating enzyme in vitro
> and in vivo.

- [PMID:23300442 — Inhibition of a NEDD8 Cascade Restores Restriction of HIV by APOBEC3G.](https://pubmed.ncbi.nlm.nih.gov/23300442/): Full-length UBE2F indirectly enables a ubiquitin-ligase pathway through cullin neddylation; this is distinct from intrinsic ubiquitin transfer.

> conjugation of NEDD8 to Cullin-5 by the NEDD8-conjugating
> enzyme UBE2F is required for HIV Vif-mediated degradation

## Exact non-GO claims

The complete emitted record is preserved in [UBE2F-protnlm-source.json](UBE2F-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> UBC core domain-containing protein

CNN (CS 2) as a partial domain description: the N-terminal UBC-family segment is directly visible in the sequence and the current domain annotation. The name must not imply a complete functional E2 domain. [Sequence mapping](UBE2F-bioinformatics/RESULTS.md).

### Location

> Nucleus

UNC (CS 1). Nuclear localization was transferred from the structurally related SUMO E2 P63280. Neither this donor nor the localization of full-length UBE2F establishes localization of F8WDQ9. No targeting or imaging evidence for this exact short product was found.

## Emitted GO claims

All 2 emitted GO claims are individually assessed in [UBE2F-protnlm-predictions-review.yaml](UBE2F-protnlm-predictions-review.yaml).

## Family integration

The exact product has no current PANTHER assignment. The verified same-gene reference Q969M7 places the gene in PTHR24067, but this is gene-level context, not evidence that F8WDQ9 retains the family catalytic core. The sequence deletion is decisive regardless of the broader E2-family functional diversity.

## Evidence limits

The zero-row GOA snapshot contains no existing annotation to accept or remove. No core molecular function is asserted for this severely truncated product. The 2009 paper is abstract-only in the publication cache; the 2012 paper has full text. Neither characterizes F8WDQ9.

Exact sequence mapping: [UBE2F-bioinformatics/RESULTS.md](UBE2F-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## Research integration

The genuine Falcon report is retained. Its gene-level synthesis is interpreted through the exact product sequence and the primary sources above; the truncation boundary and paralog distinctions are assessed independently.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined the description, core functions and references from the literature, the
UniProt records (F8WDQ9 and the reviewed Q969M7 in UBE2F-same-gene-reference.json) and the
PANTHER/PAINT evidence. No ProtNLM2 file or prediction-evidence folder was opened.

### Identity of F8WDQ9
- F8WDQ9 (101 aa, TrEMBL) is the Ensembl model ENST00000455999 / ENSP00000389685 of UBE2F
  (ENSG00000184182, HGNC:12480). It is not among the seven isoforms described on Q969M7
  (Q969M7-1..7), so it is an alternative gene model, not a curated UniProt isoform.
- Residues 1-94 are identical to Q969M7 1-94. Canonical residues 95-178 are absent, and a 7-residue
  tail (FIERTFN) follows, with only 2/7 identity to canonical 179-185
  (UBE2F-bioinformatics/RESULTS.md, alignment.txt).
- Retained: the N-terminal UBA3-docking extension (canonical "Interaction with UBA3" region 1-29),
  the N-acetyl-Met1/Leu2/Leu4 surface that binds the DCNL PONY domain [PMID:23201271
  "LC-MS/MS analysis revealed UBE2F as retaining its N-terminal methionine and being
  N-terminally acetylated"], and the first ~60 residues of the UBC fold (helix 1 and beta 1-4).
- Lost: the HPN motif (His106-Pro107-Asn108) and catalytic Cys116 (C116 mutagenesis abolishes
  NEDD8 conjugation on Q969M7), plus the C-terminal helices of the UBC core. UniProt's PROSITE
  rule PRU00388 carries the matching CAUTION ("Lacks conserved residue(s) required for the
  propagation of feature annotation"). F8WDQ9 therefore cannot be a NEDD8- or ubiquitin-
  conjugating enzyme.

### Evolutionary grounding
- Canonical Q969M7 is in PANTHER PTHR24067 (UBIQUITIN-CONJUGATING ENZYME E2). The PAINT node
  PTN000630367 carries IBD NEDD8 transferase activity (GO:0019788) and protein neddylation
  (GO:0045116), with donors UBE2M P61081, Q969M7, fly, mouse and yeast Ubc12.
- F8WDQ9 has no PANTHER assignment and no IBA rows. It is a same-gene product, so the
  relationship needs no orthology inference, but the inherited catalytic function needs the
  active site that it lacks. I therefore transfer no function from the PAINT node.
- PTHR24067 family review (interpro/panther/PTHR24067/PTHR24067-review.yaml): it says that NEDD8
  specificity needs separate evidence. This matches my reading, and I found no disagreement about
  subfamily placement. A NEDD8-E2 subfamily (SF261 "NEDD8-CONJUGATING ENZYME UBC-12") exists, but
  UniProt lists only the family-level PTHR24067 for Q969M7, and F8WDQ9 has no assignment, so no
  subfamily claim is made.

### Annotation decisions
- GOA has no rows for F8WDQ9 (empty GOA file), so there are no existing annotations to act on.
- core_functions is left empty on purpose: no activity has been shown for, or can be inferred
  for, a product without the catalytic Cys. I did not propose any NEW term, because necessity of
  the gene (canonical product) for CUL5 neddylation does not show that this product takes part.
- Description rewritten: it describes the gene and the canonical product, then states precisely
  what F8WDQ9 keeps and lacks.
- Added PMID:23201271 (N-terminal acetylation and DCNL binding, residues 1-25 kept in F8WDQ9) and
  the UniProt flat file (family membership and CAUTION). The protnlm-source.json reference is
  kept but marked relevance NONE, not used.

### Relative
- Relative for the next review: canonical same-gene product Q969M7 (UBE2F), relation
  same_gene_canonical. Its complete review is in open PR #5303
  (genes/human/UBE2F__Q969M7/UBE2F__Q969M7-ai-review.yaml), so no new review is needed.
- Modules: modules/ubiquitin_transfer_relay.yaml (generic E1-E2-E3 relay, which mentions NEDD8 reuse).
  modules/dmel_cop9_signalosome.yaml covers deneddylation (fly) and is related only indirectly.
