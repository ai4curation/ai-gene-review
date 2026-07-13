# COX16 (human) review notes

UniProtKB: Q9P0S2 · HGNC:20213 · Gene COX16 (syn. C14orf112, HSPC203, PTD019).
106 aa, single-pass mitochondrial **inner membrane** protein (N-terminus in matrix,
TM 15–37, C-terminus in intermembrane space). Belongs to the COX16 family.

Deep research: falcon provider is out of credits (402); no `-deep-research-falcon.md`.
Grounded in UniProt record, GOA TSV, and cached primary literature below.

## Verified function

COX16 is a small mitochondrial inner-membrane **Complex IV (cytochrome c oxidase)
assembly factor**. It is non-catalytic (no canonical copper-binding motif) and acts
as a chaperone-like factor during COX2/MT-CO2 maturation.

- Required for COX assembly. Knockout/ablation in human cells impairs COX assembly;
  RNAi in C. elegans causes COX deficiency [PMID:29355485 abstract: "its
  ablation in HEK293 cells impairs COX assembly"; PMID:29381136: "COX16 is required
  for cytochrome c oxidase biogenesis"].
- Implicated in **MT-CO2 maturation / CuA-site (copper) formation**. Interacts
  specifically with newly synthesized COX2 and the copper-delivery machinery SCO1,
  SCO2, COA6; required for SCO1 (not SCO2) recruitment to COX2 [PMID:29381136: "COX16
  is required for SCO1 but not SCO2 association with COX2, implicating COX16 in CuA
  site formation"; PMID:29355485: "involved in copper delivery to COX2"].
- Escorts/merges the COX2 assembly module onto the COX1-containing MITRAC intermediate
  [PMID:29381136: "COX16 is a constituent of the Copper-insertion machinery and escorts
  COX2 to the MITRAC-COX1 module"; "merging the COX1 and COX2 assembly lines"]. Does
  NOT act on respiratory-chain supercomplexes [PMID:29381136: "COX16 does not act on
  respiratory chain supercomplexes"].
- Deficiency: autosomal-recessive mitochondrial complex IV deficiency, nuclear type 22
  (MC4DN22; MIM 619355) — a homozygous 82–106 deletion variant [PMID:33169484, not
  cached; recorded in UniProt DISEASE].

## Localization

Mitochondrial inner membrane, single-pass; C-terminus faces the IMS
[PMID:29381136: "inner mitochondrial membrane protein with its C-terminus facing the
intermembrane space"; "COX16 was resistant to carbonate extraction"]. IEA
Subcell/InterPro and IDA (both primaries) and HTP mito-proteome all agree.

## Annotation decisions (summary)

- Core BP: **GO:0033617 mitochondrial respiratory chain complex IV assembly** —
  ACCEPT (IBA, 2×IMP/IDA primaries). Directly_involved_in core function.
- Core CC: **GO:0005743 mitochondrial inner membrane** — ACCEPT (IBA is_active_in,
  2× IDA primaries, IEA Subcell). Located_in core.
- GO:0031966 mitochondrial membrane (IEA InterPro) — parent of 0005743; ACCEPT
  (broader but correct).
- GO:0005739 mitochondrion (IDA HPA GO_REF:0000052, HTP PMID:34800366) — ACCEPT
  (correct but less specific than inner membrane).
- GO:0005515 protein binding (3 IPI: PMID:29355485 MT-CO2; PMID:29381136 SCO1/SCO2/
  COA6/MT-CO2; PMID:32296183 FAM25A binary interactome) — bare protein binding, not
  informative MF → MARK_AS_OVER_ANNOTATED (per policy, not REMOVE). The 2018 primary
  IPIs are real experimental co-IPs supporting the assembly role; the 32296183 FAM25A
  Y2H interaction has no known biological role.
- GO:0003674 molecular_function ND (GO_REF:0000015) — ND placeholder; MARK_AS_OVER_ANNOTATED
  (superseded now that assembly-factor role is established; COX16 has no catalytic MF).
- Reactome TAS ×3 → GO:0005743 inner membrane — ACCEPT.

## core_functions

No informative catalytic/binding MF is supportable (only bare protein binding), so MF
is omitted per instructions. Core function = directly_involved_in GO:0033617, located_in
GO:0005743.
