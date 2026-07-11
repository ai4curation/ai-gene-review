# HOGA1 (Q86XE5) review notes

## Summary
HOGA1 = 4-hydroxy-2-oxoglutarate aldolase, mitochondrial (EC 4.1.3.16; formerly DHDPSL /
C10orf65). Mitochondrial matrix enzyme catalysing the **terminal step of the hydroxyproline
(4-Hyp) degradation pathway**: retro-aldol cleavage of 4-hydroxy-2-oxoglutarate (HOG) into
**glyoxylate + pyruvate**. Belongs to the DapA (dihydrodipicolinate synthase, DHDPS) family;
Schiff-base type I aldolase using Lys196 as the catalytic nucleophile. Forms a homotetramer
(dimer of dimers). Loss-of-function mutations cause **primary hyperoxaluria type 3 (PH3 /
HP3, MIM 613616)**.

Key point on directionality of disease: HOGA1 itself produces glyoxylate (a precursor of
oxalate), yet its *loss* causes hyperoxaluria. Mechanism is debated (loss-of-function with
accumulation of HOG/upstream intermediates that dysregulate glyoxylate detoxification /
possible dominant-negative effect), but the enzymatic reaction and the disease association
are both firmly established.

## Molecular function
- EC 4.1.3.16; Rhea:35639 [(4S)-HOG = glyoxylate + pyruvate] and Rhea:30687 [(4R)-HOG].
  Enzyme cleaves both R- and S-forms of HOG (racemic-active), consistent with GO:0008700
  "(R,S)-4-hydroxy-2-oxoglutarate aldolase activity". GO:0106009 is the (4S)-specific term
  from the Rhea:35639 mapping; GOA carries both.
- [PMID:21998747 "hHOGA performs a retro-aldol cleavage reaction reminiscent of the trimeric
  2-keto-3-deoxy-6-phosphogluconate aldolases"]
- [PMID:21998747 "The activity of recombinant hHOGA proves that it is indeed the aldolase
  identified in the genomic analysis of PH3 patients."]
- Catalytic residues (mutagenesis): Lys196 nucleophile (K196A dead), Tyr168 (Y168F dead),
  Ser77/Asn78/Ser198 modulate substrate binding [PMID:21998747].
- Homotetramer: [PMID:21998747 "reveal a tetrameric structure composed of a dimer of dimers"].
  UniProt SUBUNIT = Homotetramer; the GOA GO:0042803 "protein homodimerization activity"
  (IDA, PMID:21998747) captures the tight-dimer interface but tetramer is the biological
  assembly; homodimerization is a real, structurally-supported sub-assembly.

## Biological process
- Terminal step of hydroxyproline catabolism [PMID:21998747 "The degradation pathway for
  4-Hyp ... 4-hydroxy-2-oxoglutarate aldolase (HOGA...). ... In the terminal reaction, HOG
  is cleaved by HOGA to produce pyruvate and glyoxylate."]
  -> GO:0019470 trans-4-hydroxy-L-proline catabolic process (IDA). CORE BP.
- UniProt FUNCTION: "Catalyzes the final step in the metabolic pathway of hydroxyproline."
- Glyoxylate metabolic/catabolic process (GO:0046487 / GO:0009436): HOGA produces glyoxylate.
  Note glyoxylate is a *product*, so "glyoxylate metabolic process" (0046487) fits well;
  "glyoxylate catabolic process" (0009436) is arguably a stretch (HOGA makes glyoxylate, it
  does not itself degrade it) but is the standard IBA/IMP call for this pathway and is not
  wrong at the pathway level -> keep, non-core-ish but accept as pathway participation.
- Pyruvate biosynthetic process (GO:0042866, IDA): pyruvate is the co-product -> accept.
- Oxalate metabolic process (GO:0033609, IMP, PMID:21896830): HOGA1 loss/variants influence
  urine oxalate; disease connection to oxalate. Keep as non-core (regulatory/disease-level
  link, not the direct catalysed reaction).

## Localization
- Mitochondrion (GO:0005739) / mitochondrial matrix (GO:0005759). N-terminal transit peptide
  (1..25). Multiple orthogonal lines: IBA, IEA(SubCell), ISS from bovine Q0P5I5, HTP
  mito-proteome (PMID:34800366), TAS Reactome matrix. All consistent. Accept mitochondrion;
  mitochondrial matrix is the more precise CC.

## protein binding IPIs
Four IPI GO:0005515 "protein binding" annotations from high-throughput interactome / mito
protein-interaction screens (PMID:27499296 STARD7; PMID:28514442 & 33961781 USP47;
PMID:32296183 CIMAP1A). Bare "protein binding" is uninformative and these are HT screens;
per policy -> MARK_AS_OVER_ANNOTATED (do NOT REMOVE bare protein-binding IPIs). No evidence
these interactions are functionally relevant to the aldolase activity.

## lyase activity (GO:0016829, IEA InterPro)
Correct but very general parent of the specific aldolase MF -> MARK_AS_OVER_ANNOTATED
(redundant with GO:0008700). Not wrong.

## Core functions
1. MF: GO:0008700 (R,S)-4-hydroxy-2-oxoglutarate aldolase activity
2. BP: GO:0019470 trans-4-hydroxy-L-proline catabolic process
3. CC: GO:0005759 mitochondrial matrix (mitochondrion GO:0005739 also correct)

## Disease
PH3 / HP3 (MIM 613616): [PMID:20797690 "mutations in an uncharacterized gene, DHDPSL, on
chromosome 10 cause a third type of PH (PH III)"]. Loss-of-function mechanism supported
[PMID:21896830 "support a loss-of-function mechanism for HOGA1, with potential for a
dominant-negative effect"].

## Deep research note
falcon deep-research provider is out of credits (HTTP 402); no -deep-research-falcon.md
generated. Review grounded in UniProt Q86XE5, seeded GOA, and cached publications
(PMID:20797690, 21896830, 21998747) plus Reactome R-HSA-6784423.
