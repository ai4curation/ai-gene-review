# PIGA (P37287) review notes

Human PIGA / PIG-A / Phosphatidylinositol N-acetylglucosaminyltransferase subunit A.
HGNC:8957, X-linked (Xp22.2), 484 aa, EC 2.4.1.198. CAZy GT4 (glycosyltransferase group 1 family, GT4 subfamily).

Deep research: falcon provider was OUT OF CREDITS (HTTP 402) at the time of review, so no
`-deep-research-falcon.md` was generated. This review is grounded in the UniProt record,
the seeded GOA, cached primary publications, and the two cached Reactome entries.

## Core biology

PIGA is the **catalytic subunit** of the **GPI-GlcNAc transferase (GPI-GnT) complex** that
catalyses the **first, committed step of GPI (glycosylphosphatidylinositol) anchor biosynthesis**:
transfer of N-acetylglucosamine (GlcNAc) from UDP-GlcNAc onto phosphatidylinositol (PI) to give
GlcNAc-PI, on the **cytoplasmic face of the ER membrane** [PMID:8900170; PMID:9463366; PMID:16162815].

- Reaction (RHEA:14789, EC 2.4.1.198): PI + UDP-GlcNAc -> GlcNAc-PI + UDP + H+
  [file:human/PIGA/PIGA-uniprot.txt CATALYTIC ACTIVITY block].
- UniProt FUNCTION: "Catalytic subunit of the glycosylphosphatidylinositol-N-acetylglucosaminyltransferase
  (GPI-GnT) complex that catalyzes the transfer of N-acetylglucosamine from UDP-N-acetylglucosamine to
  phosphatidylinositol and participates in the first step of GPI biosynthesis" [ECO:0000305|PubMed:16162815].

## GPI-GnT complex composition

At least PIGA, PIGC, PIGH, PIGP, PIGQ, PIGY and DPM2 (PIGA is the catalytic component)
[UniProt SUBUNIT; PMID:16162815]. Historical assembly picture:
- PMID:8900170 (1996): PIG-A + PIG-H form an ER complex; PIG-A is a transmembrane protein with a large
  cytoplasmic (catalytic) domain homologous to a bacterial GlcNAc transferase and a small lumenal domain;
  small lumenal domain targets it to the rough ER. GlcNAc-PI is made on the cytoplasmic side of the ER.
- PMID:9463366 (1998): four-component complex PIG-A/PIG-H/PIG-C/GPI1 (=PIGQ) in the ER membrane; complex
  has GPI-GlcNAc transferase (GPI-GnT) activity in vitro; PIG-L (2nd step, de-N-acetylation) not in complex.
- PMID:10944123 (2000): adds PIG-P as essential component; DPM2 associates and regulates (enhances activity
  ~3-fold), coupling GPI-GnT to Dol-P-Man synthase.
- PMID:16162815 (2005): adds PIG-Y (7th component); PIG-Y associates directly with catalytic PIG-A and
  regulates GPI-GnT activity. Establishes catalytic activity/function; assigns EC 2.4.1.198.

IntAct/BioPlex interactors used in GOA GO:0005515 IPIs map to complex members:
O94777=DPM2, P57054=PIGP, Q14442=PIGH, Q9BRB3=PIGQ, Q3MUY2=PIGY (all confirmed in UniProt INTERACTION block).
PMID:33961781 = BioPlex 3.0 AP-MS (high-throughput interactome) — recovers PIGP, PIGH.

## Localization / topology

Rough ER membrane; single-pass membrane protein. TOPO_DOM 1..421 cytoplasmic (catalytic), TRANSMEM
422..442, TOPO_DOM 443..484 lumenal; region 443..465 required for rough-ER localization [PMID:8900170].
GOA carries both GO:0030867 (rough ER membrane) and GO:0005789 (ER membrane); the latter is the general
parent and is the cleaner "located_in" for core functions.

## Disease

- **PNH (paroxysmal nocturnal hemoglobinuria, PNH1, MIM:300818)**: somatic PIGA loss-of-function in
  hematopoietic stem cells -> GPI-anchor deficiency on blood cells (loss of CD55/CD59) -> complement-
  mediated hemolysis. Many somatic variants in UniProt (e.g. S155F, N297D).
- **MCAHS2 (multiple congenital anomalies-hypotonia-seizures syndrome 2, MIM:300868)**: X-linked recessive
  germline hypomorphic mutations; developmental disorder with seizures. Variants R77L, P93L, R119W, I206F,
  L355S, 412-484 del, etc.
- **NEDEPH (MIM:301072)**: germline; epilepsy + juvenile hemochromatosis (failure to GPI-anchor hemojuvelin/HJV
  disrupts hepcidin/HAMP regulation).

## GOA annotation review summary (32 GOA rows)

MF:
- GO:0017176 phosphatidylinositol N-acetylglucosaminyltransferase activity — CORE. IBA, IEA(EC 2.4.1.198/RHEA:14789),
  TAS(PMID:16162815). ACCEPT (the specific, correct catalytic activity).
- GO:0016757 glycosyltransferase activity (IEA InterPro) — parent of GO:0017176; MARK_AS_OVER_ANNOTATED
  (correct but less informative; the specific child is annotated).
- GO:0008194 UDP-glycosyltransferase activity (TAS Reactome) — describes UDP-sugar donor; less specific/slightly
  off-branch vs the exact EC. MODIFY -> GO:0017176.
- GO:0005515 protein binding (IPI x several, partners = complex members) — bare "protein binding";
  MARK_AS_OVER_ANNOTATED (real interactions but uninformative MF; captured by GPI-GnT complex membership).

BP:
- GO:0006506 GPI anchor biosynthetic process — CORE. IBA, IEA, TAS(Reactome). ACCEPT.

CC:
- GO:0000506 GPI-GnT complex — CORE. IBA, IEA, IPI, IDA(PMID:16162815). ACCEPT (part_of).
- GO:0005789 endoplasmic reticulum membrane — IDA(PMID:16162815), TAS(Reactome). ACCEPT (core location).
- GO:0030867 rough endoplasmic reticulum membrane — EXP(PMID:8900170), IEA. ACCEPT (specific location, verified).
- GO:0016020 membrane (HDA, PMID:19946888 NK membrane proteome) — MARK_AS_OVER_ANNOTATED (too general;
  high-throughput proteome; ER membrane is the informative location).
