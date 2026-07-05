# GAT2 (YMR136W) — research notes

UniProt: P40209 (GAT2_YEAST). SGD: S000004744. Systematic name YMR136W.
Length 560 aa. PE level **4: Predicted** (no protein-level or transcript-level
experimental evidence recorded by UniProt for the protein product beyond
genome/EST inference). Chromosome XIII.

This is an **understudied ("dark") yeast GATA-family zinc-finger protein**. The
deliverable is a rigorous statement of what is and is not known, careful
attribution of GAT2-specific evidence versus evidence for the better-studied
GATA paralogs, and a defensible `knowledge_gaps` section.

## Domain / sequence architecture (KNOWN, from UniProt P40209)

- Single **GATA-type (Cys4 / type-IV) zinc finger** at residues **472–497**
  (`ZN_FING ... /note="GATA-type"`, PROSITE-ProRule PRU00094). Zinc-coordinating
  Cys residues visible in the sequence: `...CFHCGETET PEWRKGPYGT RTLCNACGLF...`
  (C-x2-C ... C-x2-C GATA finger signature).
- InterPro: IPR000679 (Znf_GATA), IPR013088 (Znf_NHR/GATA), IPR051140 (GATA_TF).
  Pfam PF00320 (GATA). SMART SM00401. PROSITE PS00344 + PS50114. CDD cd00202
  (ZnF_GATA). SUPFAM SSF57716 (glucocorticoid-receptor-like DBD).
- Keywords: DNA-binding; Metal-binding; Zinc; Zinc-finger.
- Large **disordered / low-complexity N-terminal and central region**: MobiDB-lite
  disordered regions 274–297, 345–383, 412–461; low-complexity 347–361; basic/acidic
  bias 369–378; basic 414–425; polar 428–456. The DBD sits near the C-terminus and
  most of the protein is intrinsically disordered — typical of a transcription
  factor with a single C-terminal DBD and long regulatory/activation region.

Interpretation: the domain content robustly supports **zinc ion binding** and
**sequence-specific DNA binding by a GATA-type finger**, hence a plausible
**DNA-binding transcription factor**. This is a structural/domain inference, not
a demonstrated activity for GAT2 itself.

## Phylogeny / paralogy (KNOWN; important nuance)

The canonical *S. cerevisiae* nitrogen-catabolite-repression (NCR) GATA network
has **four** DNA-binding GATA factors: activators **Gln3** and **Gat1**, and
repressors **Dal80** and **Gzf3/Deh1/Nil2**
(reviewed in the NCR literature; e.g. PMC2698774, PMC4382002 — searched via web).

Key phylogenetic finding from PANTHER (via UniProt DR lines):
- **GAT2 (P40209) → PANTHER family PTHR45658**, subfamily **PTHR45658:SF18
  "PROTEIN GAT2"**. PTHR45658 is labelled *"Plant GATA Transcription Factor"* and
  its SF18 members are a mixture of **fungal white-collar-2 / circadian
  (WC2) orthologs, Dictyostelium GATA proteins, and plant GATA factors**
  (see `interpro/panther/PTHR45658/PTHR45658-entries.csv`; e.g. Fusarium WC2
  A0A0J9U922, Beauveria WC2 J5JYA0, Dictyostelium gtaP B0G188, Arabidopsis
  GATA12 P69781 — all SF18).
- **GLN3 (P18494), GAT1 (P43574), DAL80 (P26343) → PANTHER family PTHR10071**
  (subfamily PTHR10071:SF281 "BOX A-BINDING FACTOR-RELATED"; verified from
  UniProt DR lines). This is a **different PANTHER family** from GAT2.

So although GAT2 is a *S. cerevisiae* GATA factor superficially similar to the NCR
factors (SGD: "similar to Gln3p and Dal80p"), **PANTHER does not group GAT2 with
the four NCR factors** — GAT2 sits in the separate GATA subfamily that includes
plant/fungal-clock/Dictyostelium GATA proteins. This directly affects how the
IBA annotations should be read (see below): the IBA propagation is from that
plant/Dictyostelium GATA cluster, not from the NCR factors.

GAT2's closest *S. cerevisiae* GATA relatives by simple similarity are the NCR
factors, but the yeast genome also has the smaller GATA proteins GAT3 (Q07928)
and GAT4 (P40569); those two are in yet another subfamily (SF149 "PROTEIN
GAT3-RELATED"), not with GAT2.

## GAT2-specific functional evidence (what is actually KNOWN about GAT2)

- SGD description (yeastgenome.org, S000004744): *"protein containing GATA family
  zinc finger motifs; similar to Gln3p and Dal80p; expression repressed by
  leucine."*
- SGD molecular-function/process annotations are **ISA (inferred from sequence
  alignment)** for DNA-binding TF activity and regulation of transcription by
  RNA pol II — i.e. inferred from homology, **not** from a direct GAT2 assay.
  The zinc-binding annotation is **RCA** (computational, from the zinc-proteome
  study PMID:30358795).
- SGD lists **cellular component = unknown** (localization not experimentally
  determined). No GFP-localization compartment call is represented in GOA.
- SGD reports **zero characterized target genes** for GAT2 (BioGRID/SGD; web).
- Reported null-mutant/large-scale phenotypes (SGD summary, web): decreased
  invasive growth; abnormal bud and vacuolar morphology; decreased vegetative
  growth; decreased chemical resistance; increased protein/peptide modification.
  These are unfocused high-throughput phenotypes, none of which pins a specific
  molecular target or condition.
- Regulation of *GAT2* transcription (SGD, web): negatively regulated by Sut2p
  during filamentous growth; regulated by Rgr1p/Ume6p; by Fkh1p in stationary
  phase; expression repressed by leucine. These describe how *GAT2* is
  controlled, not what Gat2 protein does.

### The two PMIDs cited in GOA

- **PMID:10392447** (Cox, Pinchak, Cooper 1999, *Yeast*, "Genome-wide
  transcriptional analysis in S. cerevisiae by mini-array membrane
  hybridization") — abstract only in cache (`full_text_available: false`). This
  is a **methods paper** validating mini-array membrane hybridization; the
  abstract states the method *"can correctly identify genes whose expression is
  known to be controlled by the GATA-factor regulatory network in S. cerevisiae"*
  and *"can reliably identify genes not previously reported to be associated with
  this nitrogen control system."* It is a study of the GATA regulatory network as
  a test case, not a demonstration of GAT2's specific function. SGD used it as the
  **ISA** reference (with_from pointing to *other* GATA-factor SGD ids
  S000001742 = ?, S000000842, S000001873, S000003646). I.e. the ISA annotation
  is a similarity transfer keyed to this paper's discussion of the GATA network.
- **PMID:30358795** (Wang et al. 2018, *Metallomics*, "The cellular economy of
  the S. cerevisiae zinc proteome") — abstract only. Bioinformatic + MS survey
  identifying *"582 known or potential zinc-binding proteins"* via *"a
  bioinformatics analysis that combined global domain searches with local motif
  searches."* GAT2 is a GATA zinc-finger protein, so its inclusion in the zinc
  proteome is a reasonable **RCA/computational** inference — consistent with the
  domain, but not a direct GAT2 metal-binding measurement.

## KNOWN vs NOT-KNOWN summary

**KNOWN (well supported):**
- GAT2 has a single C-terminal GATA-type (Cys4) zinc finger → binds zinc and, by
  strong domain homology, sequence-specific DNA (5'-GATA-3'-type sites).
- It is a member of the GATA transcription-factor superfamily.
- *GAT2* transcription is condition-responsive (repressed by leucine; regulated by
  Sut2/Rgr1/Ume6/Fkh1).

**NOT KNOWN (genuine gaps):**
- No direct experimental demonstration that Gat2 protein binds DNA, binds zinc,
  or activates/represses transcription (all functional annotations are ISA/RCA/IBA).
- No identified direct target genes.
- No experimentally determined subcellular localization (nucleus is IBA-inferred;
  SGD lists CC unknown).
- The condition/biological process in which Gat2 acts is undefined — whether it
  participates in the NCR nitrogen network like Gln3/Gat1/Dal80/Gzf3, or in a
  distinct process, is unresolved. Notably PANTHER places GAT2 **outside** the
  four-factor NCR family (PTHR10071), so simple assimilation to NCR is not
  automatically warranted.
- Whether Gat2 is functionally redundant with, antagonistic to, or independent of
  the other GATA factors is unknown.

## Attribution caution

Most "GATA factor in nitrogen catabolite repression" statements in the literature
concern **Gln3/Gat1/Dal80/Gzf3**, NOT GAT2. Do not transfer their demonstrated NCR
functions to GAT2. GAT2 remains an understudied paralog whose specific role is not
established.

## Deep-research status (documented, not fabricated)

Automated deep research did **not** succeed for GAT2. `just deep-research-falcon yeast
GAT2 --fallback perplexity-lite` was run and then **retried once**; on both runs the
falcon provider timed out at its 600s limit, and the perplexity-lite fallback failed
with an HTTP 401 quota error ("You exceeded your current quota"). No genuine
`GAT2-deep-research-*.md` file was produced. Per repo policy, **no deep-research file
was fabricated**. This review is instead grounded in: the UniProt record (P40209),
the GOA table, the PANTHER family data (PTHR45658 vs PTHR10071), the two cached GOA
publications (PMID:10392447, PMID:30358795), the SGD locus summary (S000004744), and
the reproducible in-repo bioinformatics analysis (`GAT2-bioinformatics/RESULTS.md`).

## Provenance index
- Domain/sequence: `genes/yeast/GAT2/GAT2-uniprot.txt` (UniProt P40209).
- PANTHER family: `interpro/panther/PTHR45658/PTHR45658-metadata.yaml` and
  `-entries.csv`; GLN3/GAT1/DAL80 PANTHER assignments verified from UniProt REST
  (P18494, P43574, P26343 DR lines).
- PMID:10392447, PMID:30358795 cached in `publications/`.
- SGD summary and phenotypes: yeastgenome.org S000004744 (web fetch, 2026-07).
