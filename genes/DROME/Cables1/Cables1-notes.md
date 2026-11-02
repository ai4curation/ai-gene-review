# Cables1 (A0A0B4KF19): evidence and ProtNLM claim review

Cables1 is a cyclin-fold protein required for the organization of sensory and motile cilia in Drosophila. It is recruited to maturing sperm basal bodies, and its loss disrupts neuronal ciliary architecture and the central pair of sperm axonemal microtubules. Its molecular activity at the basal body remains unresolved.

Exact input: [A0A0B4KF19](https://www.uniprot.org/uniprotkb/A0A0B4KF19/entry), 746 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [Cables1-predictions-source.json](Cables1-predictions-source.json). Source features: [Cables1-uniprot.txt](Cables1-uniprot.txt), with an exact extraction in [Cables1-sequence-evidence.json](Cables1-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR012388; CABLES1/2.
DR   InterPro; IPR036915; Cyclin-like_sf.
DR   InterPro; IPR006671; Cyclin_N.
FT   DOMAIN          621..699
FT                   /note="Cyclin N-terminal"
FT                   /evidence="ECO:0000259|Pfam:PF00134"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Cyclin N-terminal domain-containing protein | CNN | The cyclin N-terminal domain is independently supported by Pfam PF00134 at residues 621-699 in the source record. The domain name is accurate; it does not assert kinase activity or establish cell-cycle regulation. |
| Location | Nucleus (SL-0191) | UNC | Direct fly imaging supports basal-body recruitment in spermatogenesis (PMID:37317646). This does not demonstrate nuclear residence or exclude a nuclear pool in other tissues; the nuclear claim needs localization evidence for this exact product. |

## Literature evidence

- [PMID:37317646](https://pubmed.ncbi.nlm.nih.gov/37317646/): “TEX9, CCDC6, and CABLES1 are recruited to maturing basal bodies during Drosophila spermatogenesis.”
- [PMID:37317646](https://pubmed.ncbi.nlm.nih.gov/37317646/): “RNAi‐mediated depletion/deletion of CABLES1, CCDC6, CEP104, and TEX9 in Drosophila chordotonal neurons”

## Annotation decisions

- GO:0036064 ciliary basal body (IDA): **ACCEPT**. GFP-tagged Cables1 is recruited to maturing basal bodies during spermatogenesis in the full-text analysis of PMID:37317646; the relatively faint signal does not negate the localization.
- GO:0044458 motile cilium assembly (IMP): **ACCEPT**. Depletion and deletion produce sperm axonemal defects including loss of the central pair in PMID:37317646; this is a direct ciliogenesis phenotype.
- GO:0051726 regulation of cell cycle (IEA): **UNDECIDED**. IPR012388 establishes CABLES-family architecture. The direct fly evidence in PMID:37317646 concerns basal bodies and ciliary architecture; it does not establish regulation of cell-cycle progression by this protein.
- GO:1905515 non-motile cilium assembly (IMP): **ACCEPT**. Neuronal cilia show disorganization and shortened axonemes after Cables1 loss in PMID:37317646; the developmental assembly role is supported.

## Research assessment

The Falcon report misses PMID:37317646 and incorrectly presents fly Cables1 as lacking a localization or phenotype study. The full-text 2023 ciliogenesis paper explicitly examines Cables1/CG6191, including depletion/deletion and basal-body recruitment. Those primary experiments determine the biological assessment; mammalian CDK/cancer discussion is contextual and is not substituted for fly evidence.

Provider output: [Cables1-deep-research-falcon.md](Cables1-deep-research-falcon.md). Primary papers and source records, rather than provider verdicts, support the assessment.

The annotation and prediction assessments are complete. UNC/UNDECIDED record delimited scientific or evidence uncertainty. Empty core-function lists indicate that no sufficiently resolved molecular activity can be asserted, rather than an unfinished review.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was consulted for this section.

### Identity of the benchmark accession

FlyBase FBgn0027581 (Cables1/CG6191) maps to four unreviewed UniProt entries (UniProt REST query `xref:flybase-FBgn0027581`, 2026-10-20): A0A0B4KF19 (746 aa), A0A0B4KEN8 (728 aa), A1Z9G1 (717 aa) and Q9Y138 (696 aa, cDNA BcDNA:GH06193). None is Swiss-Prot reviewed, so there is no separate canonical entry. A pairwise comparison of the FASTA sequences shows that A1Z9G1 is identical to residues 1-717 of A0A0B4KF19 (A0A0B4KF19 has a 29-residue C-terminal extension), that A0A0B4KEN8 shares residues 1-501 and then diverges, and that Q9Y138 matches the first 694 residues. All four carry the Pfam PF00134 cyclin N-terminal domain (621-699 in A0A0B4KF19, 632-710 in A0A0B4KEN8) and are classified as PTHR22896:SF0. A0A0B4KF19 is the longest product and the only one with FlyBase experimental GO annotations, so it is the gene's annotation representative and not a fragment. It is an alternative-isoform product of a multi-isoform gene with no missing domains.

### Evolutionary placement

PANTHER PTHR22896 (CDK5 AND ABL1 ENZYME SUBSTRATE 1) splits into SF1 (vertebrate CABLES1: human Q8TDN4, mouse Q9ESJ1, zebrafish cables1), SF3/SF4 (vertebrate CABLES2, zebrafish cables2a/cables2b) and SF0, which contains fly Cables1 and the uncharacterized C. elegans Y71F9B.6 (A0A078BPF2 and isoforms, IEA-only in GOA). The fly gene is therefore a single-copy invertebrate relative of both vertebrate paralogs, in a subfamily separate from the characterized CABLES1. Human CABLES1 carries IBA terms (GO:0007399 nervous system development, GO:0005829 cytosol); fly Cables1 receives no IBA at all. I treat that as a deliberate PAINT decision and transfer none of the mammalian CDK5/ABL1/cell-proliferation biology to the fly protein.

The family review at interpro/panther/PTHR22896/PTHR22896-review.yaml places A0A0B4KF19 in SF0, which agrees with UniProt. I found no disagreement about subfamily placement. The grep hits for "cables" in modules/linc_complex.yaml are "actin cables" text and unrelated, so no module covers this gene.

### Re-examination of the annotations against PMID:37317646 (full text)

- Basal body (IDA): the paper says "CABLES1, also localized to spermatocyte basal bodies, albeit much more weakly, precluding detailed analysis." The localization is real but faint. ACCEPT retained.
- Motile and non-motile cilium assembly (IMP; RNAi plus deletion mutants): for CABLES1, CCDC6 and TEX9 together, the paper reports "a general disorganization and shortening of ciliary axonemes, with missing and displaced doublet microtubules toward the ciliary tip" in chordotonal neurons, and in sperm "the central pair of microtubules was frequently missing". These are ultrastructural defects in the axoneme itself, so they are a direct ciliogenesis readout and not a downstream organismal phenotype. The protein is at the basal body, so participation is plausible. Both ACCEPTs retained.
- Regulation of cell cycle (IEA, InterPro2GO from IPR012388): still UNDECIDED. I expanded the reason to give the SF0/SF1 separation and the absence of IBA. The term is neither supported nor contradicted in fly.

The falcon deep-research report still misses PMID:37317646, so it is not used as support. The description and core function (basal-body localization, motile and sensory cilium assembly, molecular activity unresolved) hold and are unchanged.

### Relative to review next

The closest experimentally characterized relative chosen by phylogeny is human CABLES1 (Q8TDN4, PTHR22896:SF1), the better-studied of the two vertebrate paralogs of the SF0 fly gene. The SF0 worm relative is uncharacterized. The repo has no review of CABLES1 or CABLES2 in any species (genes/*/CABLES* has no matches; mouse Cables1 is absent too).
