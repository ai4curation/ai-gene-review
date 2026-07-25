# DHDDS (Q86SQ9) review notes

Human **DHDDS** = dehydrodolichyl diphosphate synthase complex catalytic subunit
(a.k.a. hCIT / cis-isoprenyltransferase / cis-IPTase). HGNC:20603. 333 aa.
UPP synthase family (cis-prenyltransferase / undecaprenyl-PP-synthase-like fold).

## Core biology (grounded in UniProt Q86SQ9 and cited literature)

DHDDS is the **catalytic subunit** of the human **cis-prenyltransferase (cis-PT)**
complex. Together with the non-catalytic partner **NUS1 / NgBR**, it catalyzes the
**committed / first step of dolichol biosynthesis**: sequential *cis* (Z) head-to-tail
condensation of many **isopentenyl diphosphate (IPP)** units onto **(2E,6E)-farnesyl
diphosphate (FPP)** to make long-chain **dehydrodolichyl (polyprenyl) diphosphate**
(C85-100). This product is dephosphorylated/reduced (SRD5A3) and phosphorylated (DOLK)
to **dolichyl phosphate (Dol-P)**, the essential glycan carrier lipid for N-linked
glycosylation, O-mannosylation and GPI-anchor synthesis in the ER.

- EC 2.5.1.87; Rhea RHEA:53008. Requires **Mg2+** (1 per subunit).
  [file:human/DHDDS/DHDDS-uniprot.txt "EC=2.5.1.87"; "Name=Mg(2+)"]
- Reaction: "n isopentenyl diphosphate + (2E,6E)-farnesyl diphosphate = a di-trans,poly-cis-polyprenyl diphosphate + n diphosphate"
  [file:human/DHDDS/DHDDS-uniprot.txt].
- FUNCTION: "With NUS1, forms the dehydrodolichyl diphosphate synthase (DDS) complex,
  an essential component of the dolichol monophosphate (Dol-P) biosynthetic machinery"
  and "Synthesizes long-chain polyprenols, mostly of C95 and C100 chain length"
  [file:human/DHDDS/DHDDS-uniprot.txt].
- SUBUNIT: "The active dehydrodolichyl diphosphate synthase complex is a heterotetramer
  composed of a dimer of heterodimer of DHDDS and NUS1" [file:human/DHDDS/DHDDS-uniprot.txt].
- SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane"; "Peripheral membrane protein";
  "colocalizes with calnexin" [file:human/DHDDS/DHDDS-uniprot.txt].

## Catalytic subunit vs partner (important curation caveat)

Several key papers (25066056, 28842490, 32817466) foreground **NgBR/NUS1** in title/abstract,
but throughout they co-assay **hCIT = DHDDS**. DHDDS carries the catalytic (FPP+IPP) active
site; NgBR is a **pseudo-cis-prenyltransferase** that lacks its own substrate-binding cavity
but contributes an RXG motif to the DHDDS active site and allosterically enhances activity.
- PMID:33077723 (full text): "the only active-site of the complex is situated within the
  cis-prenyltransferase homology domain of DHDDS"; the S1 site binds FPP, S2 binds IPP; Mg2+
  is coordinated by the conserved D34 of DHDDS. NgBR "lacks detectable catalytic activity".
- PMID:28842490 (abstract): "both NgBR and hCIT subunits function in catalysis and substrate
  binding" — DHDDS is genuinely catalytic, not a scaffold.
- PMID:25066056 (full text): human hCIT (DHDDS) + NgBR reconstitute cis-PTase in a yeast
  triple-KO (nus1 rer2 srt1) strain; both required for a functional enzyme.

## Annotation review decisions (summary)

MF:
- GO:0045547 ditrans,polycis-polyprenyl diphosphate synthase [(2E,6E)-FPP specific] activity —
  the correct specific catalytic MF. Multiple EXP/IDA (25066056, 32817466, 33077723, 28842490)
  plus IBA/IEA. This is the CORE molecular function. Note mixed qualifiers in GOA:
  `enables` vs `contributes_to`. Because the active site is fully within DHDDS (33077723),
  `enables` is appropriate; `contributes_to` (used because it is a complex subunit) is also
  defensible and kept as ACCEPT.
- GO:0004659 prenyltransferase activity (IDA, 25066056, contributes_to) — parent of GO:0045547;
  correct but general → MODIFY to GO:0045547.
- GO:0016765 transferase activity, transferring alkyl/aryl (IEA, InterPro) — grandparent;
  correct branch but general → MARK_AS_OVER_ANNOTATED (redundant parent of the specific term).
- GO:0005515 protein binding (IPI x3): 32817466 & 33961781 both with NUS1/Q96E22 — real, but
  bare "protein binding" is uninformative → MARK_AS_OVER_ANNOTATED (the informative capture is
  GO:1904423 complex membership). 15110773 with NPC2/P61916 (yeast 2-hybrid) → KEEP_AS_NON_CORE
  (NPC2 interaction, cholesterol trafficking side role).

BP:
- GO:0006489 dolichyl diphosphate biosynthetic process (IDA, 32817466, ComplexPortal) — this is
  literally the reaction product; CORE. ACCEPT.
- GO:0043048 dolichyl monophosphate biosynthetic process (IDA x2, 28842490 & 33077723) — the
  committed step feeds Dol-P; supported by 14652022 (Dol-P biosynthesis) and full-length work.
  CORE. ACCEPT.
- GO:0016094 polyprenol biosynthetic process (IBA) — the polyprenyl-PP product is the polyprenol
  precursor; correct pathway process. ACCEPT (non-redundant BP framing).

CC:
- GO:1904423 dehydrodolichyl diphosphate synthase complex (IDA/IPI/IBA) — the cis-PT complex;
  CORE location/complex. ACCEPT. Modeled via in_complex.
- GO:0005789 endoplasmic reticulum membrane (IDA 14652022; NAS/TAS/IEA) — correct location.
  ACCEPT the IDA (14652022, is_active_in). Others redundant → ACCEPT (own correct CC, not over-annot).
- GO:0005783 endoplasmic reticulum (IBA) — parent of the membrane term; correct but less specific
  → KEEP_AS_NON_CORE / ACCEPT as broader location.

## Disease (context only, not core molecular function)
- Retinitis pigmentosa 59 (RP59) [MIM:613861]; founder K42E in Ashkenazi Jews
  [file:human/DHDDS/DHDDS-uniprot.txt; PMID:21295282; PMID:21295283].
- Developmental delay and seizures with/without movement abnormalities (DEDSM) [MIM:617836];
  variants R37H, R211Q [file:human/DHDDS/DHDDS-uniprot.txt; PMID:29100083; PMID:33077723].
- A fatal type I CDG case with low DHDDS activity [PMID:27343064].

## GO id verification (semantic-sql go.db, 2026-07)
All labels confirmed current. GO:0006486 "protein glycosylation" is obsolete; current N-glyc term
is GO:0006487 (not added to core_functions — glycosylation is downstream of DHDDS's direct role).
Branch checks: GO:0045547∈MF; GO:0043048,GO:0006489∈BP; GO:0005789∈CC; GO:1904423∈protein-containing complex.
