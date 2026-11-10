# DMS3-30 (A0SMP0) — Pseudomonas phage DMS3 gene 30 / AcrIE3

## Provenance of this file

No deep-research provider keys exist in this container, so `just deep-research` was
not run and **no `-deep-research-<provider>.md` file was created**. The research below
is from the cached publications in `publications/`, PubMed/E-utilities, UniProt REST,
QuickGO and the RCSB PDB.

GONUTS (`gowiki.tamu.edu`), the CACAO curation wiki, was checked again on 2026-11-01.
It is no longer merely "temporarily offline while we perform upgrades" as recorded in
CACAO batches 1–2: it now returns HTTP 410 with the page "GONUTS, the GO wiki, has
been retired — The GO wiki that was at gowiki.tamu.edu is no longer online." The
Internet Archive has no snapshot of either
`gowiki.tamu.edu/wiki/index.php/UniProtKB:A0SMP0` or `.../PMID:24736222`
(`archive.org/wayback/available` returns `"archived_snapshots": {}` for both). The
student-evidence check the CACAO project plan relies on is therefore permanently
unavailable, not deferred.

## Identity

- UniProt A0SMP0 (`A0SMP0_9CAUD`), TrEMBL, unreviewed, 68 aa, `PE 4: Predicted`,
  `DE SubName: Full=Uncharacterized protein {ECO:0000313|EMBL:ABG66684.1}`,
  `GN ORFNames=DMS3-30`. Genome reference is the DMS3 complete sequence
  (EMBL DQ631426, ABG66684.1) from [PMID:18952788 "Interaction between bacteriophage
  DMS3 and host CRISPR region inhibits group behaviors of Pseudomonas aeruginosa."].
- Despite the "Uncharacterized protein" name, the entry already carries the family
  assignment: `DR CDD; cd22551; AcrIE3; 1.`, `DR InterPro; IPR049758; AcrIE3-like.`,
  `DR Pfam; PF28100; AcrIE3-like; 1.` So this protein is **AcrIE3**, the type I-E
  anti-CRISPR of phage DMS3, originally named **ACR3-30** ("3" = DMS3, "30" = gene 30).
- Independent confirmation that AcrIE3 == A0SMP0: both deposited AcrIE3 crystal
  structures have exactly this 68-residue sequence. PDB **8HEL** chain A is
  `MKITNDTTTYEVAELMGSEADELDGRIMMGLLSRECVVDTDDLSEDQWLALIDESQKVRREQFESDEALEHHHHHH`
  (A0SMP0 plus a His tag) and is labelled "AcrIE3 | Pseudomonas phage DMS3
  (2913973)"; PDB **8ZEY** chain A is the untagged 68-mer, identical to A0SMP0.
- Gene-symbol question: the stub emitted `gene_symbol: A0SMP0`, i.e. the accession.
  GOA's SYMBOL for this row is `DMS3-30`, UniProt's `GN ORFNames` is `DMS3-30`, and
  the folder is `DMS3-30`. The review therefore uses `gene_symbol: DMS3-30`. The
  community-standard protein name is AcrIE3 (used by CDD, Pfam and InterPro and by
  every paper since 2024), but it is not a gene symbol from any nomenclature
  authority, and UniProt has not adopted it for this entry — see the source defect
  below.

## What the CACAO-cited paper actually shows for this gene

[PMID:24736222 Pawluk et al. 2014, mBio, full text cached] is the paper that
discovered the type I-E anti-CRISPRs. It assays **four** anti-CRISPR genes, each from
a different phage, and DMS3 gene 30 is one of them.

Two independent experiments in that paper are about this protein:

1. **Gain of function, plasmid expression of the DMS3 gene (Fig. 3C).** The gene was
   cloned out of DMS3 and expressed from pHERD30T in *P. aeruginosa* SMC4386, whose
   native type I-E system they had just shown to be active:
   [PMID:24736222 "As shown in Fig. 3C, expression of putative anti-CRISPR genes from
   phages JBD88a, DMS3, D3112, and JBD5 allowed CRISPR-sensitive phage JBD8 to form
   plaques with 103- to 105-fold-higher efficiency than on cells containing empty
   vector."] and
   [PMID:24736222 "We designate the proteins encoded by these anti-CRISPR genes as
   ACR88a-32, ACR3-30, ACR3112-31, and ACR5-34"]. The DMS3 member of that set is
   ACR3-30 = gene 30 = this protein.
   Specificity controls in the same figure: five type I-F anti-CRISPR genes and
   JBD30-36 had no effect
   [PMID:24736222 "In contrast, plasmids expressing any one of five different type I-F
   anti-CRISPR genes, or gene JBD30-36 (homologs of which are found at the 3′ ends of
   all anti-CRISPR regions) had no effect on JBD8 plaquing."].
2. **Loss of function in the phage's own genome during lytic infection (Fig. 4).**
   [PMID:24736222 "However, phage DMS3m also has an active type I-E anti-CRISPR gene
   (gene 30), encoding ACR3-30 (Fig. 3C), that is expected to protect it from
   inhibition by the CRISPR-Cas system."];
   [PMID:24736222 "In contrast, a mutant phage in which the DMS3m type I-E
   anti-CRISPR gene was replaced with a type I-F anti-CRISPR gene (DMS3m30-35 [9]) was
   not able to form plaques on SMC4386."]; conclusion
   [PMID:24736222 "These results demonstrate that gene 30, the type I-E anti-CRISPR
   gene of phage DMS3m, functions during lytic infection to inhibit the type I-E
   CRISPR-Cas system of SMC4386 and, thus, allow robust phage replication within this
   strain."].
3. **Negative result, host specificity.** The four type I-E Acrs did not inhibit the
   *E. coli* K-12 type I-E system even though all four were expressed
   [PMID:24736222 "These data show that the anti-CRISPR proteins encoded by
   P. aeruginosa phages are not active against the type I-E system in E. coli."]. They
   also do not inhibit the *P. aeruginosa* type I-F system
   [PMID:24736222 "Although the type I-E anti-CRISPR genes did not inhibit the
   P. aeruginosa type I-F system as assayed in our previous study (9), we tested
   whether they might inhibit the distantly related type I-E CRISPR system of
   E. coli"].

Is "DMS3m" a different phage from DMS3? No — it is an isogenic point mutant of DMS3
itself, made so that DMS3 would be CRISPR-targeted. From the cited companion paper
[PMID:23242138 "A constructed mutant DMS3 phage (DMS3m) described previously14 as
DMS3100%, contains five point mutations in gene 42 creating a 100% match to this
crRNA."]. The lysogen panel in Fig. 3A used wild-type DMS3 itself
[PMID:24736222 "the lysogens of phages JBD5, JBD24, DMS3, and JBD26 could be
transformed with ~100% efficiency compared to the empty vector"]. So every experiment
behind this annotation is on phage DMS3 or an isogenic derivative of it.

## Mechanism (post-2024)

Two 2024 structural papers are about this exact protein (both abstract-only in the
cache; the PDB sequences tie them to A0SMP0, see above).

- [PMID:39541974 Koo et al. 2025, Structure; PDB 8HEL] "Our results reveal that
  AcrIE3 selectively binds to the Cas8e subunit of the Cascade complex." and
  "Through extensive mutational analyses, we show that AcrIE3 interacts with the
  protospacer adjacent motif (PAM) recognition site in Cas8e through its negatively
  charged surface residues." So AcrIE3 is a Cas8e-binding, acidic-surface inhibitor
  that occludes the PAM-recognition site of the type I-E surveillance complex —
  a DNA-mimicry-like competitive block of target recognition, upstream of Cas3
  recruitment.
- [PMID:38797150 Kim et al. 2024, BBRC; PDB 8ZEY] "Our structural examination showed
  that AcrIE3 adopts a helical bundle fold comprising four α-helices, with a notably
  extended loop at the N-terminus." and "surface analysis of AcrIE3 revealed the
  presence of three acidic regions, which potentially play a crucial role in the
  inhibitory function of this protein."

Note the two papers do not agree on the helix count/fold description in their
abstracts (Koo: "all-helical fold with a negatively charged surface"; Kim: "helical
bundle fold comprising four α-helices"), but they agree on the acidic surface, which
is the functionally load-bearing claim and is the one supported by mutagenesis in Koo
et al.

A related 2025 paper on the sibling AcrIE5 states the comparison explicitly
[PMID:41161091 — not cached, abstract only via E-utilities: "AcrIE5 may compete with
DNA binding to the PAM recognition site of type I-E Cascade, similar to AcrIE3 and
AcrIE4"]. Not cited in the review (not in `publications/`).

## Ontology gap: no MF term for anti-CRISPR activity

A QuickGO ontology search for "CRISPR" returns only BP terms (GO:0099048, GO:0043571,
GO:0098672, and two obsoletes). There is no molecular-function term for inhibiting a
CRISPR-Cas surveillance complex. `GO:0140721 nuclease inhibitor activity` (the term
the AcrIIA5 review used for a Cas9 inhibitor) is a poor fit here: Cascade is not the
nuclease — Cas3 is — and AcrIE3 blocks target DNA recognition by Cas8e, not catalysis.
In GOA, GO:0140721 and its children are in practice used only for ribonuclease
inhibitors (RraA/RraB-type, InterPro and UniProt electronic rows). The review
therefore leaves `core_functions.molecular_function` unset and files a
`proposed_new_terms` entry, with `proposed_molecular_function` pointing at it.

## The CACAO row, and the two screened-for shapes

GOA row under review (the gene's only annotation of any kind):

```
UniProtKB  A0SMP0  DMS3-30  acts_upstream_of_or_within_positive_effect
GO:0098672  symbiont-mediated suppression of host CRISPR-cas system
biological_process  ECO:0007040  IDA  PMID:24736222  taxon 2913973  CACAO  20250503
```

### Shape (a), screen 3 — wrong qualifier: **PRESENT, and systematic**

`acts_upstream_of_or_within_positive_effect` says the gene product influences the
process from outside it, and positively. AcrIE3 *is* the effector of
GO:0098672: it binds host Cas8e and blocks the host surveillance complex. The right
qualifier is `involved_in`. This replicates the AcrIIA5 finding exactly (same
qualifier, same term, same assigning group).

It is not a one-off. A QuickGO pull of every annotation to GO:0098672 (18 rows,
2026-11-01) shows **9 of 18 carry `acts_upstream_of_or_within_positive_effect`, and
all 9 are CACAO**; every `involved_in` row on the term is either CACAO or UniProt
keyword-derived. Affected accessions: A0A220GHA5 (AcrIIA5, already filed),
A0A247D711 (acrIIA4), A0A2D0TCG3, A0A425B3G2, A0A6B1YCA6, A0SMP0, B3G1L5, L7P7M1
(JBD30_035, also in batch 3), Q6TM71 (orf31).

The sharpest comparator is on the same paper: **Q6TM71 (D3112 orf31 / ACR3112-31)
carries both** the CACAO `acts_upstream_of_or_within_positive_effect` row from
PMID:24736222 **and** a UniProt `involved_in` row (GO_REF:0000043) for the identical
term and claim. The correct qualifier for this exact assertion is therefore already
present in GOA, on the sibling gene from the same figure of the same paper.

### Shape (b), screen 2 — cross-isolate experimental transfer: **ABSENT**

The screen flagged PMID:24736222 because CACAO cites it on gene products from two
closely related Mu-like *Pseudomonas* phages (A0SMP0 from DMS3, Q6TM71 from D3112).
Reading the paper shows this is not the Gag shape. The paper identified **four
distinct anti-CRISPR families** and assayed one representative gene **from each of
four different phages** in the same figure — JBD88a gene 32, DMS3 gene 30, D3112 gene
31, JBD5 gene 34 — so each annotation rests on its own phage's gene. DMS3 gene 30 is
additionally assayed in its own genome in Fig. 4, and "DMS3m" there is an isogenic
point mutant of DMS3, not a sibling isolate. IDA is the correct evidence code on both
accessions; no ISS is warranted. The two-taxon span is a genuine comparative study,
which is the failure mode the screen's own design note anticipated ("taxon count alone
is a bad screen").

## Source defect: UniProt has not characterized this entry

A0SMP0 is still `DE SubName: Full=Uncharacterized protein {ECO:0000313|EMBL:ABG66684.1}`
with `PE 4: Predicted` and no GO annotation of its own, twelve years after
PMID:24736222 established its function and two years after two crystal structures were
solved from it, while its own record already cross-references CDD `AcrIE3`, InterPro
`IPR049758 AcrIE3-like` and Pfam `PF28100`. The directly comparable sibling from the
same figure of the same paper, Q6TM71, is a reviewed Swiss-Prot entry with
`RecName: Full=Anti-CRISPR protein 31`, a FUNCTION line citing PubMed:24736222, and
three keyword-derived `involved_in` GO rows (GO:0039504, GO:0052031, GO:0098672).
A0SMP0 has none of these. Recorded as a `MISSING_STATEMENT` source defect against
UniProt (on the `file:9CAUD/DMS3-30/DMS3-30-uniprot.txt` reference's
`reference_review.source_defects`, which is where defects in cited curated record text
belong), requesting `AcrIE3` / `Anti-CRISPR protein 30` as the protein name,
`PE 1: Evidence at protein level`, and a FUNCTION line from PubMed:24736222 and
PubMed:39541974.

## Terms considered and not proposed

- `GO:0039504` symbiont-mediated suppression of host adaptive immune response and
  `GO:0052031` symbiont-mediated perturbation of host defense response — these are
  what UniProt's keyword gives the sibling Q6TM71. GO:0052031 is an **ancestor** of
  GO:0098672 (checked via QuickGO ancestors), so adding it would be a parent-level
  restatement; GO:0039504 is off the GO:0098672 branch and describes adaptive immunity
  in the vertebrate sense. Neither is proposed as NEW.
- No cellular-component term is proposed. The protein acts inside the infected
  bacterial cell, and `GO:0030430 host cell cytoplasm` would be an inference with no
  localization assay behind it; it is recorded only as the core function's location,
  where the activity necessarily happens (host Cascade is cytoplasmic).

## Outcome

One existing annotation row, action **ACCEPT**. Two source defects filed: the CACAO
qualifier (`WRONG_QUALIFIER`, resource CACAO, on the annotation's `review`) and the
uncharacterized UniProt entry (`MISSING_STATEMENT`, resource UNIPROT, on the
`file:…-uniprot.txt` reference's `reference_review`). One `proposed_new_terms` entry
("CRISPR-Cas surveillance complex inhibitor activity"), referenced from the core
function's `proposed_molecular_function` because no GO MF term fits. Three knowledge
gaps, five suggested questions, five suggested experiments. `just validate 9CAUD
DMS3-30` reports **valid, 0 errors**; the one substantive warning is that the core
function's location `GO:0030430 host cell cytoplasm` has no matching
`existing_annotations` row, which is deliberate — no paper localizes the protein, and
the location is an inference from where host Cascade is, so it is recorded only as the
site of the activity and not asserted as a CC annotation. (The AcrIIA5 review takes
the same position.)
