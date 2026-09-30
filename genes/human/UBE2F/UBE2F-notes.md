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
