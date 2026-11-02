# Bacillus phage phi29 gene 3 — terminal protein p3 (TP, gp3), UniProt P03681

Curation notes for the CACAO annotation audit (`projects/CACAO.md`).

**Deep research was unavailable for this gene.** No deep-research API keys are
configured in this container, so `just deep-research` was not run and no
`-deep-research-<provider>.md` file exists. The notes below were assembled by
reading the cached publications, the UniProt flat file, PubMed (abstracts and,
where PMC allows, full text) and targeted web search. The GONUTS wiki
(`gowiki.tamu.edu`), which keeps a page per CACAO paper and would record the
student's evidence for the four CACAO rows, is **offline** ("This site is
temporarily offline while we perform upgrades"; checked 2026-10-29 for
`PMID:4630506`), as `projects/CACAO.md` already notes.

## What the protein is

266-residue early phage protein, the paradigm terminal protein (TP) of
protein-primed DNA replication. Covalently attached to both 5' ends of the
linear 19,285-bp phi29 genome through a phosphoester bond between a serine
hydroxyl and the terminal 5'-dAMP
[PMID:6779279 "indicate that protein p3 is covalently linked to phi 29 DNA through a phosphoester bond between L-serine and 5'-dAMP, namely a O,5'-deoxyadenylyl-L-serine bond"].
The linking residue is Ser-232; the S232T mutant protein "has been purified to
homogeneity and shown to be inactive in the formation of the initiation
complex; nevertheless, the mutant protein retains its ability to interact with
the phi 29 DNA polymerase and with the DNA" [PMID:3135531].

Three domains (crystal structure of the DNA polymerase/TP heterodimer, PDB
2EX3): a disordered N-terminal domain (1-73) that makes no contact with the
polymerase, an intermediate domain (74-172) conferring specificity of the
polymerase interaction, and a C-terminal priming domain (173-266) carrying
Ser-232
[PMID:16511564 "The 3.0 A resolution structure shows one domain of terminal protein making no interactions, a second binding the polymerase and a third domain containing the priming serine occupying the same binding cleft in the polymerase as duplex DNA does during elongation"].

## Core role 1: the protein primer

DNA polymerases cannot start de novo synthesis; phi29 solves the end-replication
problem by using the TP's serine hydroxyl as the primer
[PMID:16511564 "The DNA polymerase of bacteriophage phi29 solves this problem by using a serine hydroxyl of terminal protein to prime replication"].
Mechanism, from the review in PMID:22210885: "the DNA polymerase forms a
heterodimer with a free TP that recognizes the origins and initiates
replication using as primer the hydroxyl group of TP residue Ser232"; the
polymerase then "catalyses the formation of a covalent bond between the
initiator dAMP and the hydroxyl group of Ser232 of the primer TP in the
initiation reaction". The heterodimer also "excludes initiation of replication
at internal sites of the genome", and the structure explains why: "this
heterodimer of polymerase and terminal protein cannot accommodate upstream
template DNA, thereby explaining its specificity for initiating DNA synthesis
only at the ends of the bacteriophage genome" [PMID:16511564].

The TP is not a passive acceptor. Its priming domain chooses which template
nucleotide is used: "we show that this domain is the main structural
determinant that dictates the internal 3' nucleotide used as template during
initiation" [PMID:19011105], and the TP-dAMP product then slides back to
recover the terminal nucleotide. Residues of the intermediate and priming
domains (R158, R169, E191, D198, Y250, E252, Q253, R256) are needed for a
stable, functional heterodimer [PMID:22210885], and the RGD motif at 256-258
"is primarily involved in interaction with the viral DNA polymerase"
[PMID:9705251].

Direct evidence for the initiation reaction (the two CACAO GO:0006270 rows):
- PMID:6813861 (IDA): incubation of phi29-infected *B. subtilis* extracts with
  [alpha-32P]dATP labelled a protein with p3's mobility; "These results,
  together with those of acid hydrolysis and partial proteolysis, indicated
  that a covalent complex between protein p3 and 5'-dAMP is formed in vitro",
  and "The initiation complex (protein p3-dAMP) formed in the presence of 0.5
  microM [alpha-32P]dATP can be elongated by addition of 40 microM dNTPs".
  The reaction "was strongly inhibited by anti-p3 serum".
- PMID:6402761 (IMP): the title foregrounds gene 2 (the DNA polymerase), but
  the abstract states the requirement for p3 explicitly: "The formation of the
  initiation complex is completely dependent on the presence of a functional
  gene 2 product, in addition to protein p3 and phi29 DNA-protein p3 as
  template." The assay used extracts of *B. subtilis* infected with phi29
  mutants in genes 2, 3, 5, 6 and 17.

## Core role 2: anchoring replication at the host nucleoid

The N-terminal domain binds DNA sequence-independently and tethers the phage
genome and the replication machinery to the *B. subtilis* nucleoid
[PMID:20823229 "the terminal proteins (TPs) of phages ϕ29 and PRD1, infecting the distantly related bacteria Bacillus subtilis and Escherichia coli , respectively, associate with the host bacterial nucleoid independently of other viral-encoded proteins"],
and
[PMID:20823229 "Analyses of phage ϕ29 revealed that the TP N-terminal domain (residues 1–73) possesses sequence-independent DNA-binding capacity and is responsible for its nucleoid association"].
This matters functionally: "in the absence of the TP N-terminal domain the
efficiency of ϕ29 DNA replication is severely affected" and "the TP recruits
the phage DNA polymerase to the bacterial nucleoid" [PMID:20823229, Figs 1-4].
Mutating the basic residues of the N-terminal domain identifies the residues
responsible for genome binding and shows they "are important to recruit the DNA
polymerase at the bacterial nucleoid and, subsequently, for an efficient phage
DNA replication" [PMID:24205926]; the same residues raise the Km of the
polymerase for the initiating nucleotide [PMID:25722367]. No interaction with
the nucleoid-associated proteins HBsu, SMC, ScpA or Noc was detected
[PMID:20823229, Fig. S6], so how the TP is held at the nucleoid beyond generic
DNA binding is unknown.

Note on *host cell nucleus* (GO:0042025). The only localization evidence for a
nucleus is heterologous: phi29 TP, and TPs of Nf, PRD1, Bam35 and Cp-1, "were
found to localize to the nucleus when expressed in mammalian cells"
[PMID:23091024], via a bona fide NLS at residues 1-37. Mammalian cells are not
phi29's host; the host is *B. subtilis*, which has no nucleus. The in-host
location is the bacterial nucleoid, and GO has no `host cell nucleoid` term
(`GO:0009295 nucleoid` and `GO:0043590 bacterial nucleoid` are not host-scoped;
`GO:0033643 host cell part` has no nucleoid child). Proposed as a new term in
the review.

## Secondary role: the genome end during packaging

The parental TP is a virion component and the DNA-gp3 end is what the packaging
motor engages. gp3 itself compacts the ends: "Bacteriophage phi29 DNA with
covalently bound terminal protein (DNA-gp3) and its left and right-end
restriction fragments ... sedimented faster in sucrose density gradients than
their proteinase K-treated counterparts, and the faster sedimentation was both
gp3 and Mg2+-dependent", and "DNA-gp3 has a maturation pathway in which the
packaging proteins gp3 and gp16 supercoil the DNA ends, probably as a
prerequisite for efficient interaction with the prohead" [PMID:9086269].
PMID:18674782, the reference on the GOA packaging and terminase rows, is about
gp16 oligomerization on the prohead/pRNA; its gp3 content is that the
prohead/pRNA/gp16 complex "was capable of supercoiling DNA-gp3 as observed
previously for gp16 alone".

## The peptidoglycan-hydrolase attribution is superseded

UniProt carries a second FUNCTION line, "Hydrolyzes host peptidoglycans during
virus entry. {ECO:0000269|PubMed:14763988}", and with it the keywords
Hydrolase (KW-0378), Virus entry into host cell (KW-1160) and the two
cell-envelope/peptidoglycan-degradation keywords (KW-1235, KW-1236). These
produce four IEA GOA rows. The source is
[PMID:14763988 "The activity associated with virions of Bacillus subtilis phage ø29 and its relatives lies in the terminal protein gp3"].

That attribution has since been overturned. The phi29 tail protein gp13
(UniProt P15132, annotated by UniProt itself as "Lysozyme-like glycosidase"
plus "Probable metalloendopeptidase") carries the enzyme: a 1.8 A structure
"shows that this tail protein has spatially well separated N- and C-terminal
domains, whose structures resemble lysozyme-like enzymes and
metallo-endopeptidases, respectively", it sits "at the distal end of the phi29
tail knob", and "this finding suggests that gp13 functions as a
tail-associated, peptidoglycan-degrading enzyme able to cleave both the
polysaccharide backbone and peptide cross-links of the peptidoglycan cell wall"
[PMID:18606992]. The gp3 crystal structure (2EX3) is a three-domain priming
protein with no hydrolase fold and no catalytic residues. The GOA hydrolase and
virus-entry rows on P03681 are therefore recorded as REMOVE, with a UniProt
source defect re-pointing the activity to P15132.

## Summary of what p3 does

1. Supplies the Ser-232 hydroxyl that the phi29 DNA polymerase deoxyadenylylates
   to prime replication at both genome ends, and specifies which template
   nucleotide is used; stays covalently bound to the 5' ends as parental TP.
2. Binds DNA sequence-independently through its N-terminal domain, tethering the
   phage genome and recruiting the DNA polymerase to the *B. subtilis* nucleoid,
   which is required for efficient replication in vivo.
3. Secondarily, as the covalently attached genome-end protein, condenses and
   supercoils the DNA ends with gp16 ahead of packaging.
4. Carries a eukaryotic-functional NLS whose biological role in a phage is
   unexplained; proposed to facilitate horizontal gene transfer to eukaryotes.
5. Is **not** the virion peptidoglycan hydrolase (that is gp13).

## CACAO row verdicts (detail in the review YAML)

| Term | Evidence | PMID | Action |
|---|---|---|---|
| GO:0006270 DNA replication initiation | IDA | 6813861 | ACCEPT |
| GO:0006270 DNA replication initiation | IMP | 6402761 | ACCEPT |
| GO:0039693 viral DNA genome replication | IMP | 4630506 | ACCEPT (deference; cached record has no abstract) |
| GO:0039693 viral DNA genome replication | IMP | 820555 | ACCEPT |

All four are on the right protein, from papers that assay it, with evidence
codes matching the assays, and all four sit at a defensible level of
granularity. This gene is a clean case for CACAO: no phenotype-as-process, no
sign inversion, no paper-not-about-the-gene. PMID:6402761 is a near miss for
"paper is about another gene" — its title and principal claim concern gene 2 —
but its abstract names p3 as a required component, so the row stands. The
defective rows on this gene are UniProt's, not CACAO's.
