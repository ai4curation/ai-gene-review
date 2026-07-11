# MSMO1 (Q15800) review notes

Deep research: falcon provider OUT OF CREDITS (HTTP 402) at time of review — no
`-deep-research-falcon.md` generated. Review grounded in the UniProt record
(`MSMO1-uniprot.txt`), the seeded GOA (`MSMO1-goa.tsv`), and cached publications
(`publications/PMID_21285510.md`, `PMID_8663358.md`, `PMID_32296183.md`) plus cached
Reactome entries.

## Identity / function

- MSMO1 = methylsterol monooxygenase 1; synonyms SC4MOL, ERG25, DESP4; EC 1.14.18.9.
- Non-heme di-iron sterol oxidase (sterol desaturase / fatty acid hydroxylase family;
  three histidine-box motifs) of the ER membrane; multi-pass membrane protein.
- Catalyzes the three-step monooxygenation (methyl -> hydroxymethyl -> carboxaldehyde ->
  carboxylate) that demethylates the C4 methyl group(s) of 4,4-dimethyl and
  4alpha-methylsterols — the oxidative part of C4-demethylation during cholesterol
  biosynthesis, working with NSDHL (C4-decarboxylase/3-dehydrogenase) and SC5D etc.
  [UniProt Q15800 FUNCTION: "demethylation of 4,4-dimethyl and 4alpha-methylsterols, which can be" subsequently metabolized to cholesterol]
- Uses Fe cation cofactor (ECO:0000305|PubMed:8663358); electron donor cytochrome b5 in
  RHEA reactions.
- Also metabolizes the vitamin-D analog eldecalcitol (drug metabolism; PubMed:26038696) —
  peripheral, not core.
- Fine-tuned by sterol levels and degraded by the E3 ligase MARCHF6 (PubMed:36958722).

## Localization

- ER membrane (UniProt SUBCELLULAR LOCATION; Reactome). Older ProtInc (PMID:8663358)
  reports ER + plasma membrane by immunofluorescence of two proteins (34 & 75 kDa);
  the plasma-membrane call is not supported by later curation — treat as
  over-annotation, and the bare "membrane" as too general.

## Disease

- MSMO1 / SC4MOL deficiency = Microcephaly, congenital cataract, and psoriasiform
  dermatitis (MCCPD; MIM:616834); autosomal recessive; accumulation of methylsterols
  (dimethylsterols). PMID:21285510 (index case, variants), PMID:24144731 (further
  variant / epidermal biology). C4-methylsterols are meiosis-activating sterols and LXR
  ligands.

## GOA review decisions (summary)

- Core MF: GO:0000254 C-4 methylsterol oxidase activity — ACCEPT (EXP PMID:21285510,
  IBA, IEA RHEA/EC, and older TAS PMID:8663358). Multiple redundant lines all ACCEPT.
- GO:0005506 iron ion binding — ACCEPT (di-iron; Fe cofactor; histidine boxes).
- BP cholesterol biosynthetic process GO:0006695 (TAS Reactome x3, IEA UniPathway) —
  ACCEPT as core pathway context.
- GO:0036197 zymosterol biosynthetic process (IBA) — ACCEPT; UniProt PATHWAY places
  MSMO1 at zymosterol-from-lanosterol step 3/6.
- CC GO:0005789 ER membrane (IBA, IEA SubCell, TAS Reactome x4) — ACCEPT.
- GO:0005783 endoplasmic reticulum (TAS ProtInc) — ACCEPT (parent CC, correct compartment).
- GO:0005886 plasma membrane (TAS PMID:8663358) — MARK_AS_OVER_ANNOTATED (old IF, not
  supported by later ER consensus).
- GO:0016020 membrane (TAS PMID:8663358) — MARK_AS_OVER_ANNOTATED (too general; ER membrane preferred).
- GO:0008610 lipid biosynthetic process (IEA InterPro) — MARK_AS_OVER_ANNOTATED (too
  general; sterol/cholesterol biosynthesis captures it better) — but IEA family-level,
  keep as non-core-ish. Chose KEEP_AS_NON_CORE (broadly correct, just general).
- GO:0006631 fatty acid metabolic process (TAS PMID:8663358) — MARK_AS_OVER_ANNOTATED.
  The 1996 paper reported fatty-acid accumulation in an *iron-limited yeast* mutant, an
  indirect metabolic consequence, not an MSMO1 fatty-acid function. Not core.
- GO:0008202 steroid metabolic process (TAS PMID:8663358) — KEEP_AS_NON_CORE (correct
  but general parent of sterol biosynthesis).
- GO:0005515 protein binding (IPI, 15 IntAct partners, PMID:32296183 HuRI) —
  MARK_AS_OVER_ANNOTATED (uninformative bare protein binding; HuRI Y2H high-throughput;
  ERG28 partner is biologically plausible scaffold but term itself uninformative). Not REMOVE.

## core_functions

- MF GO:0000254 C-4 methylsterol oxidase activity (+ contributes iron ion binding GO:0005506).
- directly_involved_in GO:0006695 cholesterol biosynthetic process.
- located_in GO:0005789 endoplasmic reticulum membrane.
</content>
