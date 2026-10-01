# csy2 / Cas5f (Q02MM0) — Pseudomonas aeruginosa UCBPP-PA14 — curation notes

Deep research was unavailable in this environment (no provider API keys), so this file
is my own literature journal. Every assertion carries an inline PMID plus a verbatim
quote from the cached record in `publications/`.

## What this protein is

PA14_33320, 327 aa, "CRISPR-associated protein Csy2" = **Cas5f**. It sits with Cas8f in
the PAM-proximal tail of the surveillance complex:
[PMID:32170016 "the maps exhibit an asymmetric spiral, with one Cas6f subunit in the
head, one Cas5f and one Cas8f in the tail, and six Cas7f comprising the spiral
backbone"], within
[PMID:32170016 "The Csy complex is comprised of four types of Cas proteins (Cas5f-8f)
and a single 60-nt crRNA"]. The PA14 complex was first characterised biochemically as
[PMID:21536913 "the Csy proteins (Csy1-4) assemble into a 350 kDa ribonucleoprotein
complex that facilitates target recognition by enhancing sequence-specific
hybridization between the CRISPR RNA and complementary target sequences"]. GOA's two
`GO:0005515` rows are the IntAct Csy2–Csy1 pair (Q02MM0–Q02ML9, NbExp=6).

Structural work is on the *P. aeruginosa* complex:
[PMID:28985564 "The structural studies we describe here are focused on the type I-F Csy
(CRISPR system yersinia) found in Pseudomonas aeruginosa"].

## What Cas5f does

**Caps and reads the crRNA 5' handle.** This is Cas5f's defining job across type I:
[PMID:32170016 "the Cas5f and Cas8f subunits in the tail region also make extensive
interactions with crRNA, causing the 8 nt of crRNA at its 5′ terminus to display an
“S”-shape architecture, called the 5′ handle"], and critically the contacts are base-specific, not backbone-only:
[PMID:32170016 "supporting a sequence-specific recognition of the crRNA 5′ handle by
Cas5f and Cas8f"].

**Contributes a thumb to the target-duplex pocket.**
[PMID:28985564 "the duplex region of the target DNA (including the G-C/G-C PAM) is
sandwiched between the Cas8f N-terminal hook domain (residues 1-166), the Cas5f thumb
domain (residues 48-109), and Cas7"], with one Cas5f residue in the pocket:
[PMID:28985564 "Numerous positively charged residues line this DNA binding pocket,
including residues from Cas7.6f (K299), the Cas5f thumb (R90), and especially the Cas8f
hook (R24, K28, K31, R59, K71 and R78)"]. Note the "especially": the DNA contacts are
dominated by Cas8f. I therefore do **not** propose a DNA-binding term for Cas5f — see
below.

**Required in vivo for crRNA.** Csy2 is in the strict-requirement class:
[PMID:21398535 "proteins Csy4 and Csy2 are essential for small CRISPR RNA (crRNA)
production in vivo, while the Csy1 and Csy3 proteins are not absolutely required for
production of these small RNAs"]. UniProt records this as "Absolutely required for
crRNA production or stability" and, for the disruption mutant, "Loss of production of
crRNA" — a loss, not a decrease, unlike `csy1` and `csy3`. Mechanistically this is
assembly-dependent stabilisation: unprotected crRNA is degraded, and
[PMID:22522703 "We show that this RNA cleavage step is essential for assembly of the
Csy protein-crRNA complex that facilitates target recognition"].

Adaptation also needs the intact complex:
[PMID:26586803 "both modes require, in addition to Cas1 and Cas2, intact Csy complex,
an ortholog of the E. coli Cascade, and crRNA"].

## Curation decisions

- Both `GO:0005515 protein binding` rows (IPI, partner Csy1) → MODIFY to
  `part_of GO:0032991 protein-containing complex`, for the reasons set out in
  `csy1-notes.md`: `protein binding` is uninformative, complex membership is what the
  IPI establishes, and every E. coli Cascade subunit carries `part_of GO:0032991` by
  IDA/IPI. GO has no CC term for a CRISPR surveillance complex (QuickGO "CRISPR" search
  returns only BP terms), and I have not invented one.

## Gaps identified (missing annotations)

- `GO:0003723 RNA binding` (NEW, IDA, PMID:32170016). **Comparator:** casD, the E. coli
  Cas5, carries `GO:0003723` by IDA twice (PMID:25103409, PMID:18703739) plus an IEA;
  casA, casC and casE carry it too. Here the sequence-specific 5'-handle recognition is
  directly resolved.
- `GO:0043571 maintenance of CRISPR repeat elements` (NEW, IMP, PMID:21398535;
  `involved_in`). **Comparator:** casD carries `GO:0043571` (IEA, InterPro IPR021124),
  and the PA14 paralogues `cas6f` and `csy3` already hold it. The term's definition
  explicitly covers "transcription of the CRISPR repeat arrays into RNA and processing",
  which is what a `csy2` null abolishes. This is the one place where the PA14
  gene-by-gene data are sharper than the pipelines: Csy2 is in the *essential* class for
  crRNA, Csy1 and Csy3 are not, and only Csy2 lacks the term.
- `GO:0099048 CRISPR-cas system` (NEW, IDA). **Comparator:** all five E. coli Cascade
  subunits carry it by IDA (PMID:18703739); no PA14 Csy subunit does. Cas5f performs
  part of the crRNA-biogenesis and interference stages named in the term's definition
  (it holds the 5' handle that defines guide register). Checked via QuickGO that
  `GO:0099048` is not an ancestor or descendant of `GO:0043571` or `GO:0051607`.

## Not proposed, and why

- `GO:0003677 DNA binding` / `GO:0003690 double-stranded DNA binding`. Only a single
  Cas5f residue (R90) is placed in the duplex pocket and the paper's own emphasis is on
  Cas8f. **Comparator:** E. coli casD does *not* carry a DNA-binding term — it carries
  `GO:0071667 DNA/RNA hybrid binding` instead, which reflects the Cas5 position on the
  5' handle rather than on the duplex. Rather than transfer `GO:0071667` on that
  analogy, I leave it off: the type I-F hybrid is pinned by Cas7f thumbs, and I have no
  PA14 Cas5f-specific hybrid-contact quote.
- `GO:0051607 defense response to virus`. No `csy2` allele has been assayed for phage
  resistance, and the PA14 locus-level picture is contested (see `cas3-notes.md`).
- No molecular-function term exists for crRNA-guided target recognition, the activity
  the assembled complex has; recorded as an ontology gap in
  `modules/crispr_cas_adaptive_immunity.yaml` and raised in `suggested_questions`
  rather than papered over with an ill-fitting id.
