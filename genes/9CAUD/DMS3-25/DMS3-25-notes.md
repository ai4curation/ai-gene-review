# DMS3-25 (A0SMN5) — curation notes

**Deep research was unavailable for this gene.** No deep-research API keys exist
in this container, so `just deep-research` was not run and no
`-deep-research-<provider>.md` file exists. Everything below was assembled by
hand from the cached publications, PubMed/Europe PMC, NCBI, PDB/RCSB, EBI OLS
and QuickGO, plus a local sequence analysis in `DMS3-25-bioinformatics/`.

## What the entry is

- UniProt A0SMN5, 175 aa, `SubName: Full=Uncharacterized protein`,
  `GN ORFNames=DMS3-25`, `PE 4: Predicted`. No function, family, domain or
  keyword annotation of any kind beyond the reference-proteome keyword.
- Taxon: Pseudomonas phage DMS3 (NCBITaxon:2913973), a temperate phage of
  *Pseudomonas aeruginosa*. The UniProt reference-1 paper establishes the
  lysogenic lifestyle: [PMID:18952788 "We observed that lysogenic infection of
  Pseudomonas aeruginosa PA14 with bacteriophage DMS3 inhibits biofilm
  formation and swarming motility, both important bacterial group behaviors."].
  DMS3 is the phage whose interaction with the PA14 type I-F CRISPR-Cas locus
  opened the anti-CRISPR field, and DMS3-30 (A0SMP0) in this repository is its
  anti-CRISPR protein.
- NCBI RefSeq YP_950449.1 calls it `hypothetical protein DMS3-25`; so does the
  genome annotation. There is no community name for it.

## GOA

Two CACAO rows, both `GO:0051607 defense response to virus`, IMP,
PMID:41639445, qualifier `acts_upstream_of_or_within_positive_effect`, dated
2026-03-23. They differ only in ECO subtype, which the review schema does not
represent, so one review entry covers the pair:

- ECO:0001175 = deletion mutation phenotypic evidence used in manual assertion
- ECO:0007089 = loss-of-function mutant phenotype evidence used in manual assertion

Both are mutant-phenotype subtypes of IMP, i.e. the curator read a phenotype of
a strain in which this gene was deleted or inactivated.

## The cited paper

PMID:41639445, Patel et al., *Nature* 2026, "A pore-forming antiphage defence is
activated by oligomeric phage proteins". `full_text_available: false`; the
Nature full text is paywalled, Europe PMC has no open-access record and only
abstract-level text-mined annotations, and there is no bioRxiv preprint. The
abstract is the only readable text.

- [PMID:41639445 "Here we describe a 164-residue prophage-encoded protein that
  defends bacteria by sensing conserved oligomeric components of phage
  assembly."]
- [PMID:41639445 "This protein, called ring interacting pore 1 (Rip1), is
  activated by the portal or small terminase proteins of infecting
  phages-oligomeric ring-shaped complexes that are essential for virion
  maturation."]
- [PMID:41639445 "Rip1 uses these phage protein ring complexes as a template to
  assemble into membrane-disrupting pores that inhibit phage virion assembly and
  cause premature death of the host cell."]
- [PMID:41639445 "Rip1 homologues are widely distributed across bacteria and
  provide robust defence against diverse phages."]
- [PMID:41639445 "This study reveals a strategy by which a small defence protein
  integrates both sensing and effector activity by exploiting a conserved
  feature of viral assembly."]
- [PMID:41639445 "The mechanism mirrors eukaryotic pore-forming immunity but is
  executed by a single protein, offering an evolutionarily streamlined solution
  to viral detection and defence."]

The paper's abstract never names DMS3. It does, however, describe **two**
classes of protein on opposite sides of the same defence: Rip1, which executes
it, and the phage portal / small terminase rings, which trigger it. A GOA
qualifier of `acts_upstream_of_or_within_positive_effect` fits the trigger and
not the effector, so the whole judgment turns on which of the two DMS3-25 is.

## Which side of the defence is DMS3-25 on?

Resolved in `DMS3-25-bioinformatics/` (see `RESULTS.md`), using the two chains
of PDB 9OOX — the paper's own cryo-EM structure of HK446 Rip1 bound to phage T6
small terminase — as the two reference points.

- A0SMN5 vs HK446 Rip1 (9OOX chain L, 164 aa): score 176.0, 48/156 = **30.8%
  identity**, aligned over the full length, with the central helix, the
  following beta strand and the C-terminal cysteine module all co-linear. Both
  proteins carry exactly two CxxC motifs and no others (A0SMN5 CADC/CHPC; Rip1
  CAQC/CHRC).
- A0SMN5 vs T6 small terminase (9OOX chain A): score **-65.0**, 14.4% identity,
  no CxxC motif in the terminase. Worse than not aligning.
- Genome context agrees. In NC_008717.1 DMS3-25 is `complement(12769..13296)`,
  divergent from the forward-strand head-packaging operon next to it (DMS3-26
  terminase large subunit, DMS3-27 portal protein). A small terminase gene would
  be in that operon; an accessory gene inserted in the opposite orientation
  inside a structural module is the signature of a prophage moron, which is what
  a prophage-encoded defence gene is. Note also that this is the **only**
  Rip1-like ORF near the packaging genes, and DMS3's own portal (DMS3-27) and
  terminase large subunit (DMS3-26) are separate entries that carry no CACAO
  annotation.

Conclusion: DMS3-25 is a Rip1-family antiphage defence protein encoded as a
moron by the DMS3 prophage. It is the effector, not the trigger.

## Judgment

- `GO:0051607 defense response to virus` is the right term, and it is the term
  GO uses for bacterial antiphage defence systems. Nothing more specific exists:
  OLS returns no abortive-infection term, and none of GO:0051607's non-regulation
  children fits: GO:0009616 is RNAi-mediated, GO:0140374 antiviral innate immune
  response is the metazoan innate-immunity branch, and GO:0044790 suppression of
  viral release by host names release rather than assembly.
- The qualifier is wrong. Rip1 "integrates both sensing and effector activity";
  the protein performs the defence response, so the relation is `involved_in`.
  Recorded as a `WRONG_QUALIFIER` source defect, with the term, reference and
  evidence code left alone. The action is ACCEPT, following the AcrIIA5
  precedent in this repository, since a qualifier field error is not a reason to
  reject a correct and well-evidenced claim.
- This is the second instance of the wrong-qualifier shape in the CACAO
  project, and the first replication of it. The first was
  `genes/9CAUD/acrIIA5`, `GO:0098672` with the same qualifier from
  PMID:28785032. Both are phage/prophage proteins, both papers come from the
  Maxwell and Davidson groups at Toronto, and in both cases the protein is the
  effector of the annotated process.

## Molecular function

No MF row exists in GOA. The paper's mechanism is a pore: the protein
polymerises on the phage ring and inserts into the membrane. GO's term for that
is `GO:0140911 pore-forming activity`, whose synonyms include "holin activity"
and "pinholin activity" — i.e. the term is used in practice for a protein that
forms a pore in the membrane of the cell expressing it, even though the
definition as written says "the membrane of another cell". (GSDMD, the
eukaryotic counterpart the paper invokes, is instead annotated `GO:0022829 wide
pore channel activity` by IDA.) The definition/usage mismatch is raised as a
`suggested_questions` entry. It is asserted both in `core_functions` and as a
single `NEW` row with evidence `ISS` and `UniProtKB:K7P861` as the source. That
accession is the HK446 Rip1 of PDB 9OOX chain L, found by matching the
`CAQCYESSVKSILQ` motif against all 60 HK446 entries in UniProtKB (164 aa,
still named `Uncharacterized protein`); the PDB construct differs from it only
at residue 2. ISS rather than IDA or IMP because no pore has been demonstrated
for the DMS3 protein itself, which is recorded as a knowledge gap.

## GONUTS

Re-checked 2026-11-01, as the project asks. GONUTS is no longer merely offline:
`https://gowiki.tamu.edu/wiki/index.php/Main_Page` now returns **HTTP 410 Gone**
with the page title "GONUTS has been retired" and the body "The GO wiki that was
at gowiki.tamu.edu is no longer online." The per-paper and per-protein CACAO
pages are therefore permanently unavailable, and the project's plan to re-check
abstract-only rows against GONUTS cannot be carried out.

## Open questions and gaps

- Which DMS3 experiments stand behind the two IMP rows is unknown to this
  review: whether the DMS3 prophage Rip1 was deleted from a lysogen and the
  lysogen then challenged, or the gene was expressed heterologously and
  mutated. The two ECO subtypes say a deletion and a loss-of-function allele
  were both involved.
- Whether DMS3-25 is activated by the portal or by the small terminase of the
  superinfecting phage, and which *P. aeruginosa* phages it defends against, is
  not established here.
- Whether the premature host death is the defence mechanism (abortive infection
  by altruistic suicide) or a side effect of pore formation is not settled by
  the abstract; it matters for whether an abortive-infection term would be the
  better annotation if GO created one.
