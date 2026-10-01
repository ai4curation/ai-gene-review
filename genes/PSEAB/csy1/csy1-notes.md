# csy1 / Cas8f (Q02ML9) — Pseudomonas aeruginosa UCBPP-PA14 — curation notes

Deep research was unavailable in this environment (no provider API keys), so this file
is my own literature journal. Every assertion carries an inline PMID plus a verbatim
quote from the cached record in `publications/`.

## What this protein is

PA14_33330, 434 aa, "CRISPR-associated protein Csy1" = **Cas8f, the large subunit** of
the type I-F surveillance complex. It occupies the PAM-proximal tail:
[PMID:32170016 "the maps exhibit an asymmetric spiral, with one Cas6f subunit in the
head, one Cas5f and one Cas8f in the tail, and six Cas7f comprising the spiral
backbone"], in a complex of defined composition
[PMID:32170016 "The Csy complex is comprised of four types of Cas proteins (Cas5f-8f)
and a single 60-nt crRNA"]. The original biochemistry on the PA14 proteins:
[PMID:21536913 "the Csy proteins (Csy1-4) assemble into a 350 kDa ribonucleoprotein
complex that facilitates target recognition by enhancing sequence-specific
hybridization between the CRISPR RNA and complementary target sequences"]. GOA's two
`GO:0005515` rows are the IntAct Csy1–Csy2 pair (Q02ML9–Q02MM0, NbExp=6) from that work
and from PMID:26416740.

The structures behind the claims below are of the *P. aeruginosa* complex:
[PMID:28985564 "The structural studies we describe here are focused on the type I-F Csy
(CRISPR system yersinia) found in Pseudomonas aeruginosa"].

## What Cas8f actually does

This is the structural-subunit problem, but Cas8f is not a passive scaffold — it has
three assignable jobs, all resolved in cryo-EM of the PA14 complex.

**1. Binds the PAM-containing target DNA duplex.**
[PMID:28985564 "the duplex region of the target DNA (including the G-C/G-C PAM) is
sandwiched between the Cas8f N-terminal hook domain (residues 1-166), the Cas5f thumb
domain (residues 48-109), and Cas7"], with the pocket dominated by Cas8f side chains:
[PMID:28985564 "Numerous positively charged residues line this DNA binding pocket,
including residues from Cas7.6f (K299), the Cas5f thumb (R90), and especially the Cas8f
hook (R24, K28, K31, R59, K71 and R78)"].

**2. Splits the duplex and reads the PAM.** A Cas8f loop wedges into the fork:
[PMID:28985564 "Wedged into this fork is the tip of a loop (residues 246-250, sequence
TKPQN) emanating from the central domain of Cas8f"] and
[PMID:28985564 "The placement of this loop, which we refer to as the lysine-containing
wedge (or K-wedge), would sterically block a 1TS-1NTS base pair"]. Independently
confirmed as functionally required:
[PMID:32170016 "Residue K247 of Cas8f has been shown to promote foreign DNA duplex
splitting by wedging into the strands, which is a prerequisite for DNA binding to Csy"].

**3. Anchors the crRNA 5' handle, sequence-specifically.**
[PMID:32170016 "the Cas5f and Cas8f subunits in the tail region also make extensive
interactions with crRNA, causing the 8 nt of crRNA at its 5′ terminus to display an
“S”-shape architecture, called the 5′ handle"], and
[PMID:32170016 "supporting a sequence-specific recognition of the crRNA 5′ handle by
Cas5f and Cas8f"].

**4. Recruits Cas3.**
[PMID:32170016 "The Cas3 protein (P. aeruginosa) was proposed to interact with the
C-terminal helical bundle of Cas8f"]. This is the function AcrIF3 neutralises from the
Cas3 side ([PMID:27455460 "masks the linker region and C-terminal domain of PaCas3,
thereby preventing recruitment by Cascade"], read with PMID:26416740).

## In vivo

Csy1 is required for the phage-dependent phenotype but, unlike Csy2 and Csy4, it is not
strictly required for crRNA accumulation:
[PMID:21398535 "proteins Csy4 and Csy2 are essential for small CRISPR RNA (crRNA)
production in vivo, while the Csy1 and Csy3 proteins are not absolutely required for
production of these small RNAs"]. UniProt records a reduction rather than a loss
("Decreased production of crRNA"). This asymmetry is why I propose `GO:0043571` for
`csy2` but **not** for `csy1`.

The complete Csy complex is required for adaptation as well as interference:
[PMID:26586803 "both modes require, in addition to Cas1 and Cas2, intact Csy complex,
an ortholog of the E. coli Cascade, and crRNA"] — but the gene-level alleles tested in
that study were `csy3` and `csy4`, not `csy1`, so I do not transfer an IMP to Csy1.

## Curation decisions

- Both `GO:0005515 protein binding` rows (IPI, partner Csy2) → MODIFY to
  `part_of GO:0032991 protein-containing complex`. `protein binding` says nothing about
  function; what the Csy1–Csy2 IPI establishes is Csy complex membership.
  **Comparator check:** all five E. coli Cascade subunits (casA/casB/casC/casD/casE)
  carry `part_of GO:0032991` by IDA or IPI (`genes/ECOLI/*/`-goa.tsv), casE's row being
  an IPI of exactly this shape. GO has no CC term for a CRISPR surveillance complex — a
  QuickGO text search for "CRISPR" returns only BP terms — so `GO:0032991` is what the
  consortium actually uses, and I have not invented a narrower id.

## Gaps identified (missing annotations)

- `GO:0003677 DNA binding` (NEW, IDA). **Comparator:** casA (Cas8e, Q46901) carries
  `GO:0003677` by IDA from PMID:25123481. Cas8f's hook and K-wedge are the main
  protein contacts to the target duplex (quotes above).
- `GO:0003723 RNA binding` (NEW, IDA). **Comparator:** casA carries `GO:0003723` by IDA
  twice. Here it is the sequence-specific 5'-handle recognition.
- `GO:0099048 CRISPR-cas system` (NEW, IDA). **Comparator:** all five E. coli Cascade
  subunits carry it by IDA (PMID:18703739); no PA14 Csy subunit does. Cas8f performs
  part of the "target interference" stage named in the term's definition — PAM reading
  and duplex splitting are steps of the process, not merely a requirement for it.
  Checked via QuickGO that `GO:0099048` is not an ancestor or descendant of
  `GO:0043571` or `GO:0051607`.

## Not proposed, and why

- **No molecular-function term for crRNA-guided, PAM-licensed target recognition
  exists.** That is the activity the assembled Csy complex has, and Cas8f is the subunit
  that licenses it. `modules/crispr_cas_adaptive_immunity.yaml` records this as an open
  ONTOLOGY gap and falls back to `GO:0003690` for the complex. I have not substituted
  any existing id for the missing concept; I annotate the component activities that are
  real (`GO:0003677`, `GO:0003723`) and raise the gap in `suggested_questions`.
- `GO:0043571 maintenance of CRISPR repeat elements`: declined, per the PMID:21398535
  asymmetry above.
- `GO:0051607 defense response to virus`: declined. No `csy1` allele has been assayed
  for phage resistance, and the PA14 locus-level evidence is contested (see
  `cas3-notes.md`).
- A Cas3-recruitment molecular function: "proposed to interact with" is a structural
  inference in PMID:32170016, and the direct structure is of the Cas3–AcrF3 pair, not
  Cas8f–Cas3. Raised as a question rather than annotated.
