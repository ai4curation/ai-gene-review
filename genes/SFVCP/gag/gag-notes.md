# SFVcpz Gag polyprotein (Pr71Gag, UniProt Q87039) — curation notes

## Provenance of this file

Deep research was **unavailable** for this review: no deep-research API keys are
configured in the container, so `just deep-research` could not be run and no
`-deep-research-<provider>.md` file exists for this gene. The literature below was
assembled by hand from the cached publications in `publications/`, PubMed (MCP), and
the UniProt record `gag-uniprot.txt`. The GONUTS wiki (`gowiki.tamu.edu`), which keeps
a page per CACAO paper and would normally record what the student curator saw, was
checked on 2026-10-29 and still serves only "This site is temporarily offline while we
perform upgrades" — the same state the CACAO project page records. All CACAO rows here
were therefore judged from the papers themselves (all three are full-text in the cache).

## What the entry is

Q87039 is the Gag polyprotein (Pr71Gag) of **simian foamy virus, chimpanzee isolate
SFVcpz** (NCBI:txid298339), 653 aa, with host *Pan troglodytes*. UniProt lists two
cleavage products of the same accession: `PRO_0000378592` Gag protein / p68Gag
(1–626) and `PRO_0000378593` p3 / p3Gag (627–653), produced by the partial cleavage at
site 626/627 by the viral protease. Per CLAUDE.md these are **PRO_ chains of one
accession, not separate genes**, so they are modelled as `functional_isoforms` of type
`CLEAVAGE_PRODUCT` in the review rather than as their own folders. Cleavage is partial
and both p71 and p68 are present in particles, so there is no evidence that the two
chains carry distinct GO-annotatable functions; the only chain-specific statement in
UniProt is that p3 is in the virion.

Foamy viruses are spumaretroviruses and differ from orthoretroviruses in most of the
relevant biology: Gag is **not** cleaved into MA/CA/NC, mature particles instead contain
two large Gag species, the protease stays fused to Pol, Gag has no myristoylation or
other membrane-targeting signal, and budding needs Env
[file:genes/SFVCP/gag/gag-uniprot.txt "Mature particles do not include the usual processed retroviral structural protein (MA, CA and NC), but instead contain two large Gag proteins"].

## Relationship to prototype foamy virus (PFV/HFV) — matters for every CACAO row

**Every experimental paper that bears on this entry was done on PFV, not on SFVcpz.**
PFV (historically "human foamy virus", HFV) is UniProt **P14349** (GAG_FOAMV,
`Human spumaretrovirus (SFVcpz(hu))`, 648 aa, NCBI:txid11963) — a *different* entry
and a *different* taxon from Q87039. The two are sister isolates of chimpanzee foamy
virus [PMID:8184531 "DNA and deduced protein sequences of SFVcpz show high homologies to human foamy virus (HFV)"],
with 86–95% amino-acid identity gene by gene
[PMID:8184531 "Amino acid homologies between corresponding genes of SFVcpz and HFV range between 86% for the taf gene and 95% for the pol gene"].

Pairwise comparison of the two Gag sequences (UniProt FASTA, fetched 2026-10-29) shows:

- aa 95–112, the CRM1-dependent NES characterised in PMID:21255441, is `LAFQDLDLPEGPLRFGPL`
  in **both** P14349 and Q87039 — identical, including Gly110, the residue whose G110V
  substitution produces the dominant-negative nuclear phenotype.
- the N-terminal 150 residues are 92% identical position-for-position.
- the C-terminal GR-box region is offset by ~9 residues by a short indel, but the GRII
  core (`RTYQPQRYGGGRGRR`) is present in both.

So the *claims* the CACAO rows make about Q87039 are almost certainly true. What is
wrong is the **evidence code**: an IDA/IMP on Q87039 asserts that *this* protein was
assayed, which it was not. The correct code for transferring a PFV result onto Q87039 is
ISS. This is recorded as a `source_defects` entry (`WRONG_EVIDENCE_CODE`) on each CACAO
row rather than as a `REMOVE`, in line with the curator-deference rule.

## Established functions

### Capsid structure and Gag–Env-dependent budding

Gag is the capsid scaffold. In mature PFV particles the capsid shell plus "a less ordered
shell of density between the capsid and the membrane" is "likely formed by the Gag
N-terminal domain and the cytoplasmic part of the Env leader peptide gp18LP"
[PMID:27399201 "Mature PFV particles have a distinct morphology with a capsid of constant dimension as well as a less ordered shell of density between the capsid and the membrane likely formed by the Gag N-terminal domain and the cytoplasmic part of the Env leader peptide gp18LP"].

Unlike orthoretroviral Gag, FV Gag cannot bud on its own: "FV release requires
co-expression and a highly specific interaction between capsid (Gag) and glycoprotein
(Env), which cannot be complemented by heterologous Env proteins"
[PMID:23618494 "FV release requires co-expression and a highly specific interaction between capsid (Gag) and glycoprotein (Env), which cannot be complemented by heterologous Env proteins"].
The Env-interaction determinant is an N-terminal helical motif: "a minimal PFV Gag
protein comprising the N-terminal 129 aa was released into the supernatant, whereas
proteins lacking this domain failed to do so"
[PMID:23618494 "a minimal PFV Gag protein comprising the N-terminal 129 aa was released into the supernatant, whereas proteins lacking this domain failed to do so"].

### ESCRT recruitment (PSAP L domain → TSG101)

PFV Gag carries a PSAP late domain (UniProt MOTIF 289–292 PTAP/PSAP in Q87039) that
behaves as a conventional class E VPS L domain: "Mutation of the PSAP and PPPI motifs
individually reduced PFV egress, and their combined mutation had an additive effect"
and "yeast two-hybrid analysis showed a PSAP motif-dependent interaction between PFV Gag
and Tsg101"
[PMID:15858022 "yeast two-hybrid analysis showed a PSAP motif-dependent interaction between PFV Gag and Tsg101"].
A second motif, PPPI, promotes egress Vps4-independently, so FV budding is not purely
ESCRT-routed.

### Genome binding: the GR boxes are the NC-domain equivalent

Gag has no Cys-His box; instead three glycine–arginine-rich boxes occupy the C-terminus
(Q87039 REGION 490–515 GR-box 1, 540–561 GR-box 2, 591–623 GR-box 3). The isolated C-terminal
NC-equivalent "binds with high affinity to both RNA and DNA, in a sequence-independent
manner, as determined by filter binding assays", and GR box I is the determinant:
"this motif is required for nucleic acid binding and for viral replication"
[PMID:8970944 "the NC domain of HFV Gag binds with high affinity to both RNA and DNA, in a sequence-independent manner, as determined by filter binding assays"].
Systematic GR-box mutagenesis in a four-plasmid vector system confirms the functional
assignment: "the PFV Gag GR boxes are important for RNA encapsidation, genome reverse
transcription, and virion infectivity as well as for particle morphogenesis"
[PMID:21106749 "the PFV Gag GR boxes are important for RNA encapsidation, genome reverse transcription, and virion infectivity as well as for particle morphogenesis"],
with "particle-associated DNA content and infectivity ... drastically reduced for all
deletion mutants". Binding both RNA and DNA is biologically meaningful here, because up
to 20% of extracellular FV particles carry a reverse-transcribed dsDNA genome.

### Microtubule/dynein transport to the centrosome

Incoming FV capsids "traffic along the microtubule network to reach the
microtubule-organizing centre (MTOC)"
[PMID:17530924 "incoming FV capsids traffic along the microtubule network to reach the microtubule-organizing centre (MTOC)"],
and Gag is sufficient and is the adaptor: "the Gag protein, the scaffold component of
viral capsids, targets the pericentrosomal region in transfected cells in the absence of
any other viral components but in a microtubule- and dynein/dynactin-dependent manner",
through "a direct interaction between Gag and dynein light chain 8"
[PMID:12857789 "we describe a direct interaction between Gag and dynein light chain 8 that probably accounts for the specific routing of the incoming capsids to the centrosome prior to nuclear import of the viral genome"].
In resting cells the incoming particle stalls there for weeks and only completes
uncoating on cell-cycle re-entry [PMID:17530924 abstract: "Incoming foamy retroviruses can stably persist at the centrosome, awaiting cell stimulation to initiate capsid cleavage, nuclear import, and viral gene expression"].

### Chromatin tethering

The GRII box contains a chromatin-binding sequence. Mutating it leaves particle
production, entry and trafficking intact but abolishes chromosomal attachment:
"we identify a short domain within the C-terminus of the structural Gag protein that
efficiently binds host chromosomes, by interacting with H2A/H2B core histones ... While
viral particle production, virus entry and intracellular trafficking are not affected by
mutation of this domain, chromosomal attachment of incoming subviral complexes is
abolished, precluding proviral integration"
[PMID:18627573 "we identify a short domain within the C-terminus of the structural Gag protein that efficiently binds host chromosomes, by interacting with H2A/H2B core histones"].
This is the paper that actually supports `GO:0044383 host chromosome` for FV Gag — not
the centrosomal-latency paper the CACAO row cites.

### Nuclear stage: real, but its necessity is contested

Gag genuinely visits the nucleus. In transfected HeLa cells, "Wild-type Gag proteins
were detected in the cytoplasm for 33% ± 2% of transfected cells, including around the
centrosome, within the nucleus (28% ± 2%) or harbored a nucleocytoplasmic distribution
(39% ± 2%)" (Figure 1D)
[PMID:21255441 "Wild-type Gag proteins were detected in the cytoplasm for 33% ± 2% of transfected cells, including around the centrosome, within the nucleus (28% ± 2%) or harbored a nucleocytoplasmic distribution (39% ± 2%)"].
A CRM1-dependent NES at aa 95–112 gets Gag back out, and blocking it traps Gag:
"deleting amino acids 95 to 112 on the full length PFV Gag, and to a lesser extent, point
mutations of conserved residues, led to nuclear redistribution of the corresponding
mutants"
[PMID:21255441 "deleting amino acids 95 to 112 on the full length PFV Gag, and to a lesser extent, point mutations of conserved residues, led to nuclear redistribution of the corresponding mutants"].
Nuclear import is driven by the GRII NLS: "GR box II mutants lacked the typical nuclear
localization pattern of PFV Gag"
[PMID:21106749 "GR box II mutants lacked the typical nuclear localization pattern of PFV Gag"].

Two cautions are on the record and should not be smoothed over:

1. A GRII-less revertant replicates fine, so "it is unlikely that nuclear localization of
   Gag protein plays any critical role during viral infection"
   [PMID:8970944 "it is unlikely that nuclear localization of Gag protein plays any critical role during viral infection"].
   PMID:22393357 likewise notes the NLS claim is "a finding recently challenged".
2. PMID:22393357 — one of the three CACAO references — concludes that the nuclear Gag
   signal *it* observes is an **artefact**: "By using different fixation procedures, we
   established that spreading and nuclear localization of the PFV Gag is due to
   artificial transport occurring during cell fixation"
   [PMID:22393357 "we established that spreading and nuclear localization of the PFV Gag is due to artificial transport occurring during cell fixation"].
   The paper's own real localization statement for Gag is a *citation to prior work*:
   "PFV Gag displays different patterns of subcellular distribution, being localized in
   the cytoplasm, the nucleus and the centrosome in transfected and infected cells
   [5], [21], [22]". So this paper is a poor reference for an IDA on host cell nucleus
   even though the term itself is right.

## CACAO row assessment (summary; details in the review YAML)

| GO term | Code | PMID | Verdict |
|---|---|---|---|
| GO:0042025 host cell nucleus | IDA | 21255441 | Term and assay correct (Fig 1D confocal IF of WT Gag). Only defect: PFV, not SFVcpz → ISS. |
| GO:0042025 host cell nucleus | IMP | 21255441 | Same figure set read through the NES mutants; mutant-phenotype basis for a CC term is unusual but genuine. Same isolate defect. |
| GO:0042025 host cell nucleus | IDA | 22393357 | Term right, **paper wrong**: its nuclear signal is the fixation artefact it set out to expose. |
| GO:0044383 host chromosome | IDA | 17530924 | Term right for FV Gag, **paper has no chromosome or chromatin assay at all** (the word "chromatin" does not occur; "chromosomes" occurs twice, both in a generic Introduction sentence about provirus integration). The supporting paper is PMID:18627573. |

### Failure patterns for the CACAO taxonomy

- **New pattern — right term, wrong paper from the same lab.** The host-chromosome row
  cites PMID:17530924 (centrosomal latency) when the chromatin-tethering result is in
  PMID:18627573, by overlapping authors from the same group, one year later. The claim
  is true, the protein is right, the evidence code fits *some* paper — just not the cited
  one. Mechanical checks pass (the PMID resolves, the title is correct, the paper is
  about FV Gag); only reading it catches this. Distinct from "paper not about gene".
- **New pattern — artefact paper read as positive evidence.** The 22393357 row takes as
  an IDA exactly the observation the paper demonstrates to be a fixation artefact. This
  is the mirror of "mechanism paper read as a localization" catalogued on Ebola GP: there
  the paper never localized the viral protein; here it localized it and then showed the
  localization was not real.
- **Cross-isolate experimental transfer.** All four rows put IDA/IMP on SFVcpz Q87039
  from PFV (P14349) experiments. The biology transfers; the evidence code does not.
  Worth checking whether this is systematic across CACAO's virus rows, since virus
  "species" in UniProt are isolate-level entries and a student reading "foamy virus Gag"
  has no cue that two entries exist.
- **Parent-level restatement (IEA side, not CACAO).** `GO:0043657 host cell` and
  `GO:0075606 transport of viral material towards nucleus` add nothing over the accepted
  `GO:0042025`/`GO:0030430` and `GO:0075521`; marked TOO_GENERAL.
- **Keyword over-reach (IEA side).** `GO:0046718 symbiont entry into host cell` from
  KW-1160: entry is Env's job (receptor binding and fusion); Gag is cargo inside the
  entering particle and begins work after the genome is in. Marked over-annotated.
