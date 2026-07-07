# BCAT2 (human) — curation notes

UniProtKB: O15382 | HGNC:977 | EC 2.6.1.42 | 392 aa (precursor; transit 1–27, chain 28–392)

## Core biology (verified)
BCAT2 is the **mitochondrial** branched-chain-amino-acid aminotransferase (BCAT(m)), a
class-IV PLP-dependent aminotransferase. It catalyses the **first, reversible step of BCAA
catabolism**: transamination of leucine, isoleucine and valine with 2-oxoglutarate
(α-ketoglutarate) to the corresponding branched-chain 2-oxo (keto) acid + L-glutamate. The
branched-chain α-ketoacids are then handed to the mitochondrial BCKDH complex.

Reactions (UniProt CATALYTIC ACTIVITY, ECO:0000269|PubMed:8702755):
- L-leucine + 2-oxoglutarate = 4-methyl-2-oxopentanoate (KIC) + L-glutamate [RHEA:18321]
- L-isoleucine + 2-oxoglutarate = (S)-3-methyl-2-oxopentanoate + L-glutamate [RHEA:24801]
- L-valine + 2-oxoglutarate = 3-methyl-2-oxobutanoate + L-glutamate [RHEA:24813]

Cofactor: **pyridoxal 5'-phosphate (PLP)**, Schiff base to Lys-229 (MOD_RES
N6-(pyridoxal phosphate)lysine; ECO:0000269|PubMed:16141215, PubMed:17050531).
Quaternary structure: homodimer (PubMed:11264579). Has a redox-active CXXC center
(Cys-342/Cys-345); C342A reduces activity ~6-fold (PubMed:17050531). Many X-ray structures.

Localization: mitochondrion / mitochondrial matrix. TRANSIT peptide 1–27. Ubiquitous tissue
expression (PubMed:11170829); HPA tissue-enhanced in choroid. BCAT1 (chr 12) is the cytosolic
paralog; BCAT2 is on chr 19 (PubMed:9165094 proposed the BCAT1/BCAT2 nomenclature).

## Disease
Autosomal-recessive **Hypervalinemia and hyperleucine-isoleucinemia (HVLI; MIM:618850)** —
elevated plasma valine and leucine/isoleucine, headache, mild memory impairment. Caused by
loss-of-function BCAT2 variants (R170Q, E264K reduce catalytic activity; PubMed:25653144;
further variants V182G, 200-392del, A341T in PubMed:31177572). Vitamin B6 (PLP precursor)
supplementation lowered BCAA and improved brain lesions in a patient. This is the *upstream*
BCAA-elevation disorder; classic MSUD is the *downstream* BCKDH defect (ketoacid accumulation).
Dismech MSUD KB notes BCAT2 mediates BCAA transamination in skeletal muscle producing KIC
(~/repos/dismech/.../Maple_Syrup_Urine_Disease.yaml lines 749–752).

## By-similarity / peripheral functions
UniProt FUNCTION notes (By similarity, from mouse O35855/O35854): BCAA catabolism supplies
lipogenic acetyl-CoA in adipocytes; acetyl-CoA is used by EP300 to acetylate/inhibit PRDM16,
preventing adipose browning; may transport branched-chain α-keto acids. These underlie the
ISS brown-fat annotations transferred from mouse.

## Annotation-decision rationale
- **MF transaminase terms** (GO:0004084 branched-chain; GO:0052654/5/6 leu/val/ile-specific):
  core. IDA (PMID:8702755), IBA, IEA(Rhea), TAS(PMID:9165094) all converge. ACCEPT.
- **BCAA catabolic BPs** (GO:0009083, GO:0006550 ile, GO:0006574 val, GO:0006552 leu): core.
  ACCEPT. GO:0009081 (BCAA metabolic process) is a correct but general parent — KEEP_AS_NON_CORE.
- **GO:0009082 branched-chain amino acid BIOSYNTHETIC process** (IEA-ARBA + TAS-PMID:8702755):
  the reaction is reversible, but in humans BCAAs are ESSENTIAL (not synthesised de novo);
  the physiological direction is catabolic. Biosynthesis is a bacterial/plant/fungal role of
  BCAT (ilvE). MARK_AS_OVER_ANNOTATED (not core; direction not physiological in human).
- **Localization** GO:0005739 mitochondrion (IBA/IEA/IDA/ISS/HTP/TAS) and GO:0005759
  mitochondrial matrix (IEA/TAS): ACCEPT; matrix is the specific location.
- **GO:0003824 catalytic activity** (IEA InterPro): correct but uninformative parent of the
  transaminase MF. MARK_AS_OVER_ANNOTATED.
- **protein binding GO:0005515** (4× IPI, interactome/BioID screens PMIDs 28514442, 29568061,
  33961781, 40205054; interactors HSPD1/P10809, HSPB1/P58557... note IntAct lists HSPD1 P10809
  and YBEY P58557): bare "protein binding" from high-throughput screens — MARK_AS_OVER_ANNOTATED
  per policy (do not REMOVE experimental IPIs).
- **Brown-fat ISS** GO:0050873 (acts_upstream_of_negative_effect) and GO:1903444 (negative
  regulation of brown fat cell differentiation): transferred from mouse (O35855). Real but
  indirect/downstream metabolic-signalling role, not the core enzymatic function.
  KEEP_AS_NON_CORE.
- **GO:0097009 energy homeostasis** (IEA Ensembl from mouse): broad downstream physiology;
  KEEP_AS_NON_CORE.

Cached key pubs 8702755 and 9165094 are ABSTRACT-ONLY (full_text_available: false); UniProt
cites their full text for the experimental catalytic/function annotations — defer to curator,
ACCEPT (do not REMOVE).
