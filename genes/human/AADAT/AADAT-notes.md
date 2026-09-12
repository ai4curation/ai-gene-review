# AADAT (KAT II / KYAT2) — review notes

UniProt: Q8N5Z0 (AADAT_HUMAN). HGNC:17929. Gene synonyms KAT2, KYAT2. 425 aa precursor,
mitochondrial transit peptide 1..29, mature chain 30..425.

## Identity and core biology

AADAT is a **PLP-dependent, class-I (fold-type I) aminotransferase** that is one and the
same protein as **kynurenine aminotransferase II (KAT II)**. It is a broad-specificity
transaminase with two physiologically prominent activities:

1. **2-aminoadipate aminotransferase (AADAT; EC 2.6.1.39)** — transaminates
   L-2-aminoadipate + 2-oxoglutarate → 2-oxoadipate + L-glutamate, an intermediate step in
   **L-lysine degradation** (saccharopine/aminoadipate pathway).
   [file:human/AADAT/AADAT-uniprot.txt "Reaction=L-2-aminoadipate + 2-oxoglutarate = 2-oxoadipate + L-"]
   [PMID:12126930 "the conversion of alpha-aminoadipate to alpha-ketoadipate by \nalpha-aminoadipate aminotransferase (AADAT) is an intermediate step in lysine \ndegradation"]

2. **Kynurenine aminotransferase II (KAT II; EC 2.6.1.7)** — transaminates L-kynurenine +
   2-oxoglutarate → kynurenate (kynurenic acid, KYNA) + L-glutamate, the committed step of
   **kynurenic acid biosynthesis** in the tryptophan/kynurenine pathway.
   [PMID:18056995 "Human kynurenine aminotransferase II (hKAT-II) efficiently catalyzes the \ntransamination of knunrenine to kynurenic acid (KYNA)"]
   KYNA is a neuroactive metabolite: "KYNA is the only known \nendogenous antagonist of N-methyl-D-aspartate (NMDA) receptors and is also an \nantagonist of 7-nicotinic acetylcholine receptors" [PMID:18056995].

KAT II "is a primary enzyme in the brain for catalysing the transamination of kynurenine
to KYNA" [PMID:18620547], and is "the principal enzyme responsible for the synthesis of
KYNA in the rodent and human brain" (KAT II knockout mice show a substantial decrease in
brain KYNA) [PMID:18620547].

## Substrate breadth (broad-specificity aminotransferase)

The definitive biochemical study (Han et al. 2008, PMID:18620547, full text available)
screened 24 amino acids and 16 α-oxo acids and found "very broad substrate specificity, is
capable of catalysing the transamination of 16 out of 24 tested amino acids and could
utilize all 16 tested alpha-oxo acids as amino-group acceptors." On kinetic grounds "hKAT
II should be equally efficient in catalysing the transamination of aminoadipate,
kynurenine, methionine and glutamate" [PMID:18620547]. Preferred amino-group acceptors:
"α-oxoglutarate, α-oxocaproic acid, phenylpyruvate and α-KMB" [PMID:18620547]. Glyoxylate
is a usable but low-affinity acceptor (used experimentally as the assay acceptor), giving
rise to the various "…:glyoxylate transaminase" activities (glycine, methionine, aromatic
amino acids). These glyoxylate-linked activities are real in vitro but secondary/assay
artifacts of the broad site rather than the principal physiological reactions.

UniProt FUNCTION: "Transaminase with broad substrate specificity. Has transaminase
activity towards aminoadipate, kynurenine, methionine and glutamate. Shows activity also
towards tryptophan, aspartate and hydroxykynurenine." [file:human/AADAT/AADAT-uniprot.txt]

## Cofactor

PLP-dependent: "belongs to the fold-type I pyridoxal 5-phosphate \n(PLP)-dependent enzymes"
[PMID:18056995]; UniProt COFACTOR pyridoxal 5'-phosphate (evidence PubMed:12126930,
18056995, 18056996). Lys263 forms the internal Schiff base (N6-(pyridoxal phosphate)lysine
at position 263 in UniProt FT).

## Subcellular location — mito vs cytosol ambiguity

UniProt calls **Mitochondrion** (ECO:0000305) based on the N-terminal mitochondrial transit
peptide (1..29) [file:human/AADAT/AADAT-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion"];
Reactome places the aminoadipate/kynurenine reactions in the **mitochondrial matrix**
[Reactome:R-HSA-508561, R-HSA-70952, R-HSA-893583]. AADAT is also detected in high-confidence
mitochondrial proteome studies (HTP) [PMID:34800366].
HOWEVER, PMID:18620547 introduction states KAT II "is localized in the soluble cytoplasm,"
and Reactome R-HSA-9972889 places a **cytosolic** AADAT activity (3-hydroxykynurenine →
xanthurenate), noting "The cytosolic localization of human AADAT is inferred from work in
rats (Rzeski et al., 2005)." So both mitochondrial and cytosolic pools/annotations exist in
the literature; mitochondrion/mitochondrial matrix is the UniProt-authoritative core call.

## Structure / subunit

Homodimer [PMID:18056995, PMID:18056996, PMID:18620547]; many crystal structures (e.g. 2R2N
KAT II + PLP + kynurenine; 3DC1 + 2-oxoglutarate). N-terminal fragment (res 15-33) is a
flexible lid that adapts to substrates of different sizes — the structural basis of broad
specificity [PMID:18620547].

## Tissue / disease context

Highest expression in liver (also heart, brain, kidney, pancreas, prostate, testis, ovary)
[file:human/AADAT/AADAT-uniprot.txt "TISSUE SPECIFICITY: Higher expression in the liver"].
Directionality: hKAT II favours aminoadipate → 2-oxoadipate (Km 0.9 mM for aminoadipate vs
20.9 mM for oxoadipate), consistent with a lysine-degradation role [PMID:18620547]; the
kynurenine → KYNA direction is effectively irreversible because the α-oxo intermediate
cyclizes spontaneously to KYNA [PMID:18620547].

## Annotation review summary

- Two catalytic MFs are the core: **GO:0047536** L-2-aminoadipate:2-oxoglutarate
  transaminase activity (EXP PMID:12126930, IDA PMID:18620547) and **GO:0016212**
  L-kynurenine:2-oxoglutarate transaminase activity (EXP PMID:18056995, IDA PMID:18620547).
  Both ACCEPT.
- **GO:0030170** pyridoxal phosphate binding — obligate cofactor; ACCEPT (upgrade the IEA
  from InterPro; well supported experimentally by cofactor studies and Lys263 Schiff base).
- Broad-specificity/glyoxylate-linked MFs (GO:0047315 kynurenine:glyoxylate; GO:0047958
  glycine:2-oxoglutarate; GO:0050094 methionine:glyoxylate; GO:0047313 aromatic-amino-acid:
  glyoxylate) are genuine in vitro activities from the broad active site; the IDA ones
  (PMID:18620547) are experimentally supported — KEEP_AS_NON_CORE (non-physiological/assay
  acceptor); IEA duplicates likewise non-core.
- **GO:0008483** transaminase activity (IEA) — correct but too general given the specific
  activities; MARK_AS_OVER_ANNOTATED (redundant parent).
- Location: mitochondrion / mitochondrial matrix ACCEPT (core, UniProt-authoritative);
  cytosol TAS KEEP_AS_NON_CORE (documented but secondary/inferred-from-rat pool).
- IBA GO:0016212 (MF) and GO:0005739 (is_active_in mitochondrion) — ACCEPT, consistent with
  experimental data.

## Core functions chosen (author term ids)

- MF GO:0047536 (2-aminoadipate transaminase) — lysine catabolism
- MF GO:0016212 (kynurenine:2-oxoglutarate transaminase) — KYNA biosynthesis
- MF GO:0030170 (pyridoxal phosphate binding) — cofactor
BP context: GO:0019477 L-lysine catabolic process; GO:0034276 kynurenic acid biosynthetic
process; GO:0070189 kynurenine metabolic process. CC: mitochondrion / mitochondrial matrix.
(Note: old GO:0006554 "lysine catabolic process" is OBSOLETE; current term is GO:0019477.)
</content>
