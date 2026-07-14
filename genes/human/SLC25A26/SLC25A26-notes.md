# SLC25A26 (SAMC) — review notes

UniProt: Q70HW3 (SAMC_HUMAN). HGNC:20661. Gene: SLC25A26. Synonym: SAMC.
274 aa, mitochondrial carrier (TC 2.A.29) family, 6 predicted TM helices, 3 Solcar repeats.

## Core identity

SLC25A26 encodes the **mitochondrial S-adenosyl-L-methionine carrier (SAMC)**, the only
known transporter that imports S-adenosylmethionine (SAM/AdoMet) into the mitochondrial
matrix. It is a multi-pass inner-membrane antiporter that exchanges cytosolic SAM for
matrix S-adenosylhomocysteine (SAH/AdoHcy), the by-product of intramitochondrial
methylation reactions. Imported SAM is the methyl donor for matrix methyltransferases
acting on mtDNA/mt-RNA, proteins, and cofactor biosynthesis (lipoic acid, coenzyme Q10).

- UniProt FUNCTION: "Mitochondrial S-adenosyl-L-methionine/S-adenosyl-L-homocysteine
  antiporter. Mediates the exchange of cytosolic S-adenosyl-L-methionine, the predominant
  methyl-group donor for macromolecule methylation processes, for mitochondrial
  S-adenosylhomocysteine(SAH), a by-product of methylation reactions."
  [file:human/SLC25A26/SLC25A26-uniprot.txt]
- UniProt CATALYTIC ACTIVITY (Rhea:RHEA:75479): SAH(out) + SAM(in) = SAH(in) + SAM(out).
  [file:human/SLC25A26/SLC25A26-uniprot.txt]
- UniProt SUBCELLULAR LOCATION: "Mitochondrion inner membrane ... Multi-pass membrane protein"
  [file:human/SLC25A26/SLC25A26-uniprot.txt]
- KM=23 uM for SAM (25 C); "Strongly inhibited by tannic acid and Bromocresol Purple."
  [file:human/SLC25A26/SLC25A26-uniprot.txt]

## Foundational functional characterization

Agrimi et al. 2004 [PMID:14674884] identified and biochemically characterized human SAMC:
the cDNA was overexpressed in bacteria, the purified protein reconstituted into liposomes,
and its transport properties established it as the human mitochondrial SAM carrier. Key
findings (abstract; full text not in cache):
- "SAM (S-adenosylmethionine) has to be transported into the mitochondria where it is
  converted into S-adenosylhomocysteine in methylation reactions of DNA, RNA and proteins."
- "its product was purified, reconstituted into phospholipid vesicles and identified from
  its transport properties as the human mitochondrial SAM carrier (SAMC)."
- "Unlike the yeast orthologue, SAMC catalysed virtually only countertransport, exhibited a
  higher transport affinity for SAM and was strongly inhibited by tannic acid and Bromocresol
  Purple."
- "SAMC was found to be expressed in all human tissues examined and was localized to the
  mitochondria."
- "The physiological role of SAMC is probably to exchange cytosolic SAM for mitochondrial
  S-adenosylhomocysteine."
[PMID:14674884 abstract]

This paper is the experimental basis (EXP/IMP by UniProt and Reactome) for MF terms
GO:0000095 (SAM transmembrane transporter activity), GO:0180003 (SAM:SAH antiporter
activity), and BP terms GO:0015805 / GO:1990543 (SAM transport / mitochondrial SAM
transmembrane transport).

## Disease and downstream methylation dependence

Kishita et al. 2015 [PMID:26522469] — COXPD28; full text available. Three families with
recessive SLC25A26 mutations; the paper both re-establishes the transporter function and
demonstrates the downstream methylation consequences:
- "The human mitochondrial SAM carrier (SAMC), encoded by SLC25A26 (MIM: 611037), is
  expressed in all human tissues examined and is believed to be the only route of SAM entry
  into mitochondria." [PMID:26522469 full text]
- Reconstituted-liposome SAM transport assays on COXPD28 variants (A102V, V148G, P199L) and
  a SAMCΔ1–88 splice product: "demonstrated a severe abrogation of SAM transport capacity for
  all altered proteins ... SAMCΔ1–88 was completely inactive, whereas p.Ala102Val and
  p.Pro199Leu variants exhibited negligible activity, and p.Val148Gly strongly inhibited SAMC
  activity (15% of wild-type SAMC)." [PMID:26522469 full text] — supports GO:0000095 /
  GO:0180003 (IMP) and GO:1990543 (IMP).
- Downstream methylation defects: 12S rRNA adenine dimethylation reduced; protein methylation
  (ANT1/ANT2, ETFB) reduced; lipoic acid (PDHC-E2, α-KGDH-E2) and CoQ10 reduced.
  "impaired SAM transport into mitochondria causes a complex syndrome causing multiple primary
  defects, including those affecting RNA stability, protein modification, mitochondrial
  translation, and the biosynthesis of CoQ10 and LA." [PMID:26522469 full text] — supports
  GO:0043414 macromolecule methylation (acts_upstream_of, IMP).

Schober/Rosenberger et al. 2022 [PMID:35024855] — full text available. Two adult-onset
COXPD28 cases (variants R142Q, E135G). Establishes that these milder variants impair the SAH
limb of the antiport rather than SAM import:
- "The SLC25A26 gene encodes a mitochondrial inner membrane carrier that transports
  S-adenosylmethionine (SAM) into the mitochondrial matrix in exchange for
  S-adenosylhomocysteine (SAH)." [PMID:35024855]
- "SAMC is the only entry route for SAM into the mitochondrial matrix." [PMID:35024855]
- "impairment of SAH, rather than SAM, transport across the mitochondrial membrane is likely
  the cause of this milder, late-onset phenotype." [PMID:35024855] — supports GO:0180003
  (antiporter activity, EXP): both SAM and SAH limbs are functional properties of the same
  antiporter.

Ji et al. 2021 [PMID:34375635] — case report, novel compound-het variants (A12P, A66E) in a
Chinese COXPD28 patient; abstract only. Corroborates SAMC as "the mitochondrial
S-adenosylmethionine carrier (SAMC) that responsible for the transport of
S-adenosylmethionine (SAM) into the mitochondria." Note: this paper reports/analyzes variants
in silico and by structural modeling; used by UniProt as IMP for GO:0180003 and GO:1990543.

## Localization evidence

- IDA mitochondrial inner membrane, PMID:14674884 (also UniProtKB DR line: GO:0005743 IDA).
- HPA IDA mitochondrion (GO_REF:0000052), GO:0005739.
- HTP mitochondrion, PMID:34800366 (Morgenstern et al., quantitative mito proteome) — SAMC/
  Q70HW3 detected in curated mitochondrial proteome. Consistent; non-core supporting evidence.

## Annotation assessment summary

Core molecular functions:
- GO:0000095 S-adenosyl-L-methionine transmembrane transporter activity — CORE MF (EXP/IMP).
- GO:0180003 SAM:SAH antiporter activity — CORE MF, the specific mechanism (EXP/IMP; both SAM
  and SAH limbs experimentally supported).

Core cellular component:
- GO:0005743 mitochondrial inner membrane — CORE (IDA, PMID:14674884; also IBA is_active_in).

Core biological process:
- GO:1990543 mitochondrial S-adenosyl-L-methionine transmembrane transport — CORE (IMP).
- GO:0015805 S-adenosyl-L-methionine transport — parent/general form of the above; ACCEPT but
  the mitochondrial-specific 1990543 is the better term.

Non-core / supporting:
- GO:0005739 mitochondrion (IEA/IDA/HTP) — correct but less specific than 0005743; keep,
  non-core.
- GO:0043414 macromolecule methylation, acts_upstream_of (IMP) — indirect/downstream effect;
  SAMC is a transporter, not a methyltransferase. Keep as non-core (acts_upstream_of correctly
  captures the indirect relationship).

Over-annotations / removals:
- GO:0015860 purine nucleoside transmembrane transport (IEA, GO_REF:0000108, with/from
  GO:0180003) — logical-inference artifact: SAM/SAH contain an adenosyl (purine nucleoside)
  moiety, but SAMC does not transport free purine nucleosides. Clearly-wrong IEA → REMOVE.
- GO:1902475 L-alpha-amino acid transmembrane transport (IEA, GO_REF:0000108, with/from
  GO:0180003) — same artifact: SAM/SAH contain a methionine/homocysteine-derived amino-acid
  moiety, but SAMC does not transport free L-amino acids. Clearly-wrong IEA → REMOVE.
- GO:0015837 amine transport (TAS, Reactome:R-HSA-549127) — the Reactome pathway
  R-HSA-549127 is "SLC-mediated transport of organic cations" (OCT/SLC22 family, ergothioneine,
  carnitine), NOT the SAMC AdoMet/AdoHcy reaction (which is R-HSA-8855062). "amine transport"
  is a mischaracterization of SAMC's substrate (SAM is a sulfonium metabolite, not transported
  as a generic amine). Over-annotation via a mismatched Reactome pathway → MARK_AS_OVER_ANNOTATED
  (TAS, do not REMOVE experimental/authored assertions per policy; flag as over-annotated).
</content>
