# Kcr_0764 (B1L4Y3): methanogenesis, CoM/CoB and Hdr gene survey of *K. cryptofilum* OPF8

Script: `survey_com_cob_genes.py` (run `uv run python survey_com_cob_genes.py > survey_output.txt`).
Raw output: `survey_output.txt` (run 2026-11-09). All counts below are copied from that output.

## Queries and results (UniProtKB, taxonomy_id:374847, 1602 entries)

- Methyl-coenzyme M reductase signatures IPR003183 (alpha N-terminal domain), IPR003179 (beta subunit),
  IPR003178 (gamma subunit): 0 hits each. Name query "methyl-coenzyme M reductase": 0 hits.
- Coenzyme M biosynthesis: IPR003830 (ComA, phosphosulfolactate synthase), IPR005238 (ComB-like),
  IPR022502 / IPR022494 (sulfopyruvate decarboxylase alpha/beta, ComDE): 0 hits each. Name queries
  "coenzyme M", "sulfolactate", "sulfopyruvate", "phosphosulfolactate": 0 hits.
- Coenzyme B biosynthesis: name queries "coenzyme B", "7-mercaptoheptanoyl", "homocitrate synthase":
  0 hits. Caveat: the CoB chain-elongation steps use LeuA/LeuCD-like enzymes that are not specific
  signatures, so name queries cannot exclude them; this line of evidence is weak on its own.
- Hdr subunits: IPR039650 (HdrA-like family) has 3 hits: Kcr_0764, Kcr_1115, Kcr_1116.
  IPR017678 (HdrB family) and IPR053646 (HdrC family) have 0 hits. The HdrB-named protein Kcr_0767
  carries only IPR004017 (cysteine-rich, CCG domain) and IPR051278; the HdrC-named Kcr_0766 carries
  only the generic alpha-helical ferredoxin signature IPR009051.
- Hydrogenase: two [NiFe] large-subunit / small-subunit / delta clusters named "F420-reducing
  hydrogenase" (Kcr_0321/0322; Kcr_1117-1119), plus Hyp maturation factors.

## Neighbourhood of Kcr_0764

Kcr_0761 (4Fe-4S ferredoxin) - Kcr_0762 (Ni-containing CO dehydrogenase, IPR010047) - Kcr_0763 (CooC
accessory protein) - **Kcr_0764 (HdrA-like)** - Kcr_0765 (named HdrA, but carries IPR003813, the
F420-non-reducing hydrogenase subunit D / MvhD signature) - Kcr_0766 (HdrC-like) - Kcr_0767 (HdrB-like,
CCG domain). The Hdr-like genes sit beside a single-subunit CO dehydrogenase, not beside a hydrogenase.

## QuickGO IBA reach of GO:0051912

Five IBA rows, all with/from PANTHER:PTN000078336 and UniProtKB:P60200: M. jannaschii HdrA (P60200),
M. acetivorans HdrA1/HdrA2 (Q8TLB0, Q8TM02), and K. cryptofilum Kcr_0764 (B1L4Y3) and Kcr_1115
(B1L5Y2). Kcr_1116 does not receive the row.

## Interpretation

No protein for the reaction that makes CoM-S-S-CoB (MCR) and no ComA/ComB/ComDE are encoded. Without
MCR there is no source of the heterodisulfide, so a CoB--CoM heterodisulfide reductase function for
Kcr_0764 is not supported. The HdrA-like FAD and four ferredoxin-type [4Fe-4S] domains are present,
so an electron-transfer role in an Hdr-like complex with an unknown disulfide (or other) acceptor
remains plausible. This is an absence-of-signature argument from a single complete genome (the
genome paper reports one 1.59 Mb contig); it is not proof that no CoM is scavenged.
