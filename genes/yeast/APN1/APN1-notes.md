# APN1 (YKL114C, P22936) — curation notes

Saccharomyces cerevisiae Apn1: the major apurinic/apyrimidinic (AP) endonuclease and
DNA 3'-repair diesterase, the eukaryotic counterpart of *E. coli* endonuclease IV (Nfo).
Reviewed for the CACAO project (four GOA rows carry `ASSIGNED BY = CACAO`, all from
PMID:12767225).

**Provenance note on this file.** No deep-research provider keys were available in this
container, so `just deep-research` was not run and no `-deep-research-<provider>.md` file
exists for APN1. Everything below was assembled by hand from the cached publications in
`publications/`, the UniProt flat file, PubMed, and QuickGO/OLS term lookups. Two cached
papers have full text (PMID:12397185, PMID:16024777); the rest are abstract-only, which is
flagged where it limits a judgement.

## Identity and family

- AP endonuclease 2 / endonuclease IV (Nfo) family; InterPro IPR001719 (AP_endonuc_2),
  Pfam PF01261, NCBIfam TIGR00587 `nfo`, HAMAP MF_00152, PANTHER PTHR21445:SF0
  [file:yeast/APN1/APN1-uniprot.txt "HAMAP; MF_00152; Nfo; 1."].
- 367 aa, monomer, binds a trinuclear zinc cluster
  [file:yeast/APN1/APN1-uniprot.txt "Note=Binds 3 Zn(2+) ions.;"].
- Cloned by immunological screening and shown to be homologous to *nfo*
  [PMID:1693433 "The DNA and predicted amino acid sequences for the APN1 gene are
  homologous to those for the nfo gene encoding DNA endonuclease IV of Escherichia coli."].

## Core enzymology

**AP endonuclease / 3'-repair diesterase, and it is the major one.** Gene disruption
showed the protein accounts for essentially all of both activities in extracts
[PMID:1693433 "Gene disruption experiments confirm that the Apn1 protein accounts for
greater than or equal to 97% of both AP endonuclease and DNA 3'-repair diesterase
activities in yeast cell-free extracts."]. UniProt's FUNCTION states the same
[file:yeast/APN1/APN1-uniprot.txt "APN1 accounts for > 97% of both apurinic/apyrimidinic (AP)"].

**3'-diesterase was the activity the protein was first purified by.** Johnson & Demple
purified the enzyme on a 3'-phosphoglycolaldehyde substrate
[PMID:3056935 "We have used a synthetic DNA substrate containing
3'-phosphoglycolaldehyde esters to identify and purify to physical homogeneity the major
yeast diesterase that removes such nucleotide fragments."]. The same paper reports that
purification stripped a tightly bound metal and that activity was restored by Co2+, Mn2+,
Ni2+ or Zn2+ [PMID:3056935 "Purification of the enzyme removed a tightly bound metal, but
the activity of the purified enzyme could be restored by the addition of Co2+, Mn2+, Ni2+,
or Zn2+, with Co2+ the most effective cofactor."]. That the enzyme also hydrolyses a
3'-phosphoglycolate terminus is stated in the Nash-lab full text
[PMID:12397185 "Recently, it has been demonstrated that, like Apn1 and Apn2 ( 30 , 36 ),
purified Tdp1 can hydrolyze a PG residue from the 3′ end of DNA ( 16 )."], and *APN1*/*APN2*
loss is what sensitises cells to bleomycin, a 3'-PG-generating agent
[PMID:12397185 "However, when APN1 and APN2 have been inactivated, some of the residual repair
of bleomycin damage depends on TDP1 (Fig. 3 D )."]. This argues for the specific GO term
`GO:0090580` (phosphodiesterase activity, acting on 3'-phosphoglycolate-terminated DNA strands),
which human APEX1 carries, rather than the top-level `GO:0008081`.

**Active-site zinc cluster; two substitutions abolish function.** The Endo IV active site
coordinates three Zn2+ via nine residues, and the corresponding Apn1 residues Glu158 and
Asp192 are essential
[PMID:12767225 "Both Glu145 and Asp179 are among nine amino acid residues within the active
site pocket of endonuclease IV that coordinate the position of a trinuclear Zn cluster
required for efficient phosphodiester bond cleavage."],
[PMID:12767225 "We show that glycine substitutions at the corresponding conserved amino acid
residues of yeast Apn1, i.e., Glu158 and Asp192, abolish the biological function of this
enzyme."]. The E158G variant still binds DNA while D192G is catalytically dead
[PMID:12767225 "Indeed, the Apn1 Glu158Gly mutant, but not the E. coli endonuclease IV
Glu145Gly mutant, is able to bind DNA."],
[PMID:12767225 "Moreover, Apn1 Asp192Gly completely lacks enzymatic activity, while the
activity of the E. coli counterpart Asp179Gly is reduced by approximately 40-fold."].

**Progressive 3'→5' exonuclease on duplex (not single-stranded) DNA.** Ishchenko et al.
characterised this directly: purified Apn1 degraded duplex but not ssDNA
[PMID:16024777 "Using these substrates, we found that increasing concentrations of the
purified Apn1 protein degraded the duplex DNAs (Fig. 1B , lanes 7 to 17) but not the
single-stranded DNA (lanes 3 to 5)."], with kinetics comparable to its AP endonuclease
activity [PMID:16024777 "In the case of Apn1, we demonstrate that it contains progressive
exonuclease activity, which is as efficient as its AP endonuclease."]. It removes 3'-terminal
8oxoG, mismatches and 3'-blocking groups
[PMID:16024777 "We show that the 3′-terminal THF residue is a preferred substrate for Apn1 (
k cat / K m = 0.68), which suggests that the 3′→5′ exonuclease serves to eliminate
3′-blocking groups (Table 1 )."], and genetically this constitutes an Ogg1-independent 8oxoG
repair route [PMID:16024777 "Remarkably, the apn1Δ ogg1Δ double mutant exhibited a synergistic
45-fold increase in the rate of spontaneous can1 r mutations (Table 2 )."]. The duplex-specific
reading matters for term choice: `GO:0008311` (double-stranded DNA 3'-5' DNA exonuclease
activity) rather than its parent `GO:0008296`.

**Tdp1-like 3'-tyrosyl-DNA phosphodiesterase activity — real in vitro, incidental in vivo.**
Purified Apn1 removes a 3'-tyrosine from nicked/tailed duplexes
[PMID:12397185 "The purified enzyme removed tyrosine efficiently from the 3′ end of a
synthetic oligonucleotide in the context of a nicked duplex or tailed duplex substrate."],
and extracts lose the activity in *apn1* cells
[PMID:12397185 "This activity is unaffected by a tdp1 mutation, as expected from the behavior
of purified Tdp1 ( 7 ), but is greatly depressed in extracts of apn1 cells."]. The authors'
own genetics argue the activity does not contribute to Top1-lesion repair
[PMID:12397185 "Thus, we infer that the esterase activity shown in Fig. 3 A is incidental,
and it is some other activity of the AP endonucleases that works in the same pathway as does
Tdp1."]. So the MF is well supported but should not be read as a core biological role.

## Pathway role

Apn1 is required for BER in yeast extracts; the 5'-incision at AP sites is undetectable
without it [PMID:9295360 "In extracts of an apn1 deletion mutant, the 5'-incision at AP
(apurinic/apyrimidinic) sites is not detectable, supporting the notion that yeast contains
only one major 5'-AP endonuclease."]. Apn2 is a minor, partly redundant second AP endonuclease
[PMID:12397185 "Although Apn1 accounts for >90% of the AP endonuclease activity in yeast ( 31
), the sensitivity of an apn1 apn2 double mutant to agents that induce depurination is
substantially greater than that of either single mutant ( 32 , 33 )."].

## Localization

- **Nucleus (primary).** Indirect immunofluorescence plus C-terminal NLS dissection
  [PMID:7690756 "We show here by indirect immunofluorescence that Apn1 is localized to the
  yeast nucleus."]; delocalised truncations fail to complement
  [PMID:7690756 "These delocalized derivatives also failed to restore wild-type resistance to
  oxidative or alkylating agents in a delta apn1 strain."]. UniProt: `SUBCELLULAR LOCATION: Nucleus.`
- **Mitochondrion (secondary).** One lab's finding, mediated by Pir1p
  [PMID:11238901 "Here we demonstrate for the first time that yeast Apn1p is also localized to
  the mitochondria."], functionally supported by mitochondrial mutation rates
  [PMID:11238901 "pir1 Delta and apn1 Delta mutants exposed to MMS exhibited 3.6- and 5.8-fold
  increases, respectively, in the rate of mitochondrial mutations, underscoring the importance
  of Apn1p in repair of the mitochondrial genome."]. Treated as non-core: a single-laboratory
  localisation that UniProt has not adopted (the flat file lists only `Nucleus`).

## Zinc

`GO:0008270` has an InterPro IEA row and an RCA row from the yeast zinc-proteome survey
[PMID:30358795 "The yeast zinc proteome of 582 known or potential zinc-binding proteins was
identified using a bioinformatics analysis that combined global domain searches with local
motif searches."]. Both are consistent with the structurally characterised trinuclear cluster
quoted above and with UniProt's curated COFACTOR note, so both are kept.

## CACAO rows (all PMID:12767225, dated 2013-11-10)

GOA has four CACAO rows on APN1 — `GO:0003906` (also independently made by SGD from the same
paper), `GO:0005634` nucleus, `GO:0008296`, `GO:0017005` — all IDA from Jilani et al. 2003
*Biochemistry*. The cached record is **abstract-only** (`full_text_available: false`) and the
paper is paywalled (pubs.acs.org returned 403). The GONUTS wiki, where the student's evidence
statement would be recorded, is offline: `https://gowiki.tamu.edu/wiki/index.php/PMID:12767225`
returns only "temporarily offline while we perform upgrades", and the Internet Archive is not
reachable from this container. So the student's figure-level justification could not be read.

What the abstract does and does not show, taken row by row:

- `GO:0003906` AP endonuclease: directly supported — the paper is a structure–function
  analysis of Apn1's abasic-site cleavage, and SGD curated the same term from the same paper.
- `GO:0005634` nucleus: not mentioned in the abstract at all. The claim is nonetheless true
  and independently IDA-supported (PMID:7690756), so it is kept rather than challenged;
  the full text plausibly shows the mutant proteins are nuclear.
- `GO:0008296` 3'-5'-DNA exonuclease: not mentioned in the abstract. The activity is real but
  **duplex-specific**, so the granularity is wrong: `GO:0008311` is the term the data support
  (PMID:16024777 Fig. 1B), and APN1 already carries it.
- `GO:0017005` 3'-tyrosyl-DNA phosphodiesterase: not mentioned in the abstract; the activity
  was shown by PMID:12397185 (Fig. 3A), from which SGD made the parallel row. True MF, but the
  same paper's genetics call it incidental, so it is kept as non-core.

Pattern for the CACAO taxonomy: these are **not** phenotype-as-process errors and not the
wrong protein. They look like **over-harvesting one paper** — a single highly-cited
structure–function paper annotated with the protein's whole known activity repertoire,
including activities established in *other* papers, and at the family-level granularity
(`GO:0008296`) rather than the granularity the yeast data support (`GO:0008311`). Compare SGD,
which curated exactly one term from this paper and sourced each other activity to the paper
that demonstrated it.

## Comparator check (for the `NEW` decision)

`GO:0000012 single-strand break repair` looked like a candidate `NEW` term, since Apn1 cleans
3'-blocking groups at single-strand breaks
[PMID:16024777 "Results obtained with the cell extracts support the idea that in vivo Apn1
exonuclease might be involved in the repair of single-strand breaks containing 3′-blocking
groups and mismatched nucleotides."]. Comparator query (QuickGO, 2026-10-29): neither human
APEX1 (UniProtKB:P27695) nor *E. coli* Nfo (UniProtKB:P0A6C1) carries `GO:0000012`; both are
annotated to `GO:0006284` and `GO:0006281` only. The absence across species and MODs reads as a
convention, not a gap, so no `NEW` row was proposed. No other process term survived the
participation test either (the elevated mitochondrial mutation rate in *apn1Δ* is a phenotype,
not a process Apn1 performs).
