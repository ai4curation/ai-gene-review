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

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This entry was written during a re-review that deliberately ignored the ProtNLM2 predictions; the earlier sections above, including the ProtNLM2 claim assessments, are retained unchanged.

### 2026-10-20 full re-review (independent of any ML predictions)

#### Identity of the benchmark accession

F8WDQ9 is an unreviewed 101-residue UniProt entry derived from Ensembl ENSP00000389685
(transcript ENST00000455999), gene UBE2F (HGNC:12480). It is NOT the canonical product.
The reviewed canonical product is Q969M7 (185 aa).

Sequence mapping ([RESULTS.md](UBE2F-bioinformatics/RESULTS.md); script now reads the
F8WDQ9 sequence from `UBE2F-uniprot.txt` rather than any prediction file):

- F8WDQ9 1-94 = Q969M7 1-94 (100% identity), then a 7-residue alternative tail `FIERTFN`.
- The tail matches the C-terminal end of the described isoform 5 alternative sequence
  (VSP_037271, `...MSEFIERTFN`), but the splice junction differs (isoform 5 diverges at
  residue 72, F8WDQ9 at 95), so F8WDQ9 is not identical to any Swiss-Prot-described isoform.
- Retained: N-terminal E1-docking extension and acetylated N terminus (the DCNL-binding
  segment; [PMID:23201271 "recognizes acetylated N termini"]), and about 70 of the 154 UBC-core residues.
- Lost: catalytic Cys116 (glycyl thioester site) and the rest of the UBC core. UniProt itself
  cautions: "Lacks conserved residue(s) required for the propagation of feature annotation".
- Conclusion: a truncated alternative gene-model product; cannot be a NEDD8-conjugating
  enzyme. No proteomic evidence of expression was found.

#### Existing annotations

GOA has zero rows for F8WDQ9. Nothing to accept/remove. I did not propose NEW terms:
transferring NEDD8 conjugating enzyme activity (GO:0061654) or protein neddylation
(GO:0045116) from Q969M7 would be wrong given the missing catalytic cysteine, and binding
terms for the retained N-terminus have no direct evidence for this product.

#### Evolutionary context

- Canonical Q969M7 is classified in PANTHER PTHR24067 by UniProt; panther.obo also has a
  subfamily PTHR24068:SF129 "NEDD8-CONJUGATING ENZYME UBE2F" — release skew between
  PTHR24067 and PTHR24068, already documented in `interpro/panther/PTHR24068/PTHR24068-review.yaml`.
- PAINT node PTN000630367 (NEDD8-conjugating clade, seeds include human UBE2M P61081,
  UBE2F Q969M7, mouse MGI:1915171, yeast UBC12) carries IBD GO:0019788 and GO:0045116.
  F8WDQ9 itself has no PANTHER assignment and no IBA, consistent with the truncation.
- Closest characterised relative: the canonical product Q969M7 of the same gene; nearest
  ortholog with experimental seeding is mouse Ube2f (Q9CY34, MGI:1915171), in the same
  UBE2F subfamily. No review exists in the repo for either. Paralog UBE2M (P61081) is the
  other branch of the same PAINT clade.
- GO-CAM 6606056e00002524 (HIV-1 Vif / CUL5) includes Q969M7 as NEDD8 conjugating enzyme.

#### Literature on the canonical protein (gene-level baseline only)

- [PMID:19250909 "the previously uncharacterized E2 UBE2F is a NEDD8-conjugating enzyme in vitro"]
- [PMID:23300442 "conjugation of NEDD8 to Cullin-5 by the NEDD8-conjugating enzyme UBE2F is required for HIV Vif-mediated degradation"]

#### Modules

`modules/ubiquitin_transfer_relay.yaml` (generic E1-E2-E3 relay, also reused by NEDD8) is
the only relevant module; no dedicated neddylation module exists (curation gap, noted here).
