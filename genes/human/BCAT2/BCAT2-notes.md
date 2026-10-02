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

## Paired horse benchmark evidence review

The human reference supplies mechanistic evidence for the corresponding selected horse protein; the human conclusion alone is not validation of the horse sequence. The exact horse comparison is in `genes/HORSE/BCAT2/BCAT2-bioinformatics/RESULTS.md`. Research reports are source leads; annotation decisions cite the underlying publication or experimentally supported UniProt passages. Unresolved source-specific results retain UNDECIDED.


## 2026-09-30 BCAT2 source and function reassessment

All 41 distinct source annotations and both UniProt products are retained. The independent annotation consultation yields 28 ACCEPT, 12 KEEP_AS_NON_CORE and one MODIFY. The broad catalytic term is refined to the established branched-chain transaminase activity. The previously authored PLP-binding NEW assertion is withdrawn separately from the source inventory; PLP dependence and homodimer organization remain within one catalytic core.

This reassessment supersedes the earlier argument that dietary essentiality excludes biosynthesis annotations. Reversible BCAT chemistry can regenerate BCAAs from existing ketoacid skeletons, and the human Reactome records include both directions. This is distinct from making the carbon skeleton de novo. The initial transamination is not the irreversible committed step performed downstream by BCKDH. Net human BCAT2-specific reamination flux remains a question rather than a new experimental claim.

Canonical BCAT2 is mitochondrial; the shorter PP18b splice product has separate human placental cytosolic-fraction evidence. It is not the cytosolic paralog BCAT1, and equal catalytic activity of the short product is not assumed. The yeast experiments in the 8702755 abstract and rat expression assays in 9165094 are described with their actual species bounds. The original experimental curator assertions are preserved and corroborated with human BCATm evidence.

The earlier P58557 partner label HSPB1 is corrected to YBEY. All seven HSPD1 or YBEY source interactions are consistently retained as non-core. Individual supplementary interaction records and direct affinities were not independently inspected; no special folding, transport or catalytic mechanism is invented. The human GO-CAM places BCAT2 metabolism upstream in a brown-fat regulatory context and does not assign EP300 activity or direct PRDM16 binding to BCAT2.

The two missing PubMed records and two Reactome records were recovered through Source93 after the initial normal local calls failed DNS, and their normal content was explicitly reassessed before this integration. Source access limits are recorded in each reference review. Existing Falcon output is preserved as AI-generated research background, not independently verified primary evidence. The final review adds no quotations and the historical notes above remain unchanged.


### Focused validation

The focused BCAT2 validation passed with eight advisories. Seven concern the supported generic interaction rows retained as KEEP_AS_NON_CORE under the supplied ActionEnum; no assay-specific replacement was established for those records. The eighth notes that no annotation cites the generated Falcon report directly. The review instead cites primary records and treats the unchanged provider report as research background. These advisories do not change the scientific decisions. Gene HTML rendering and the new history record are checked separately; no global validation pass is claimed.

## 2026-09-30: evidence and cofactor follow-up

This entry supersedes the earlier withdrawal of PLP binding and the citation assignments described above. All 41 source assertions, their identifiers/evidence/qualifiers/partners and both alternative products remain unchanged. The current proposal has 28 ACCEPT, 12 KEEP_AS_NON_CORE, one MODIFY and one NEW. It retains one catalytic core.

The Ile/Val-specific judgments now cite the immutable human UniProt reactions (RHEA:24801 and RHEA:24813) and the human Reactome reaction R-HSA-70724. The abstract of the CXXC study supports catalytic mechanism but does not by itself document these substrate-specific assays [PMID:17050531]. The older source reference is preserved where it belongs: its abstract explicitly describes yeast experiments, so no human assay is invented from it [PMID:8702755].

Human BCATm structural evidence supports the specific PLP-binding MF [PMID:11264579]. The active-site cofactor is part of the same catalytic unit; its binding term is a different MF branch and is not rendered redundant simply by having a transaminase term. The restored NEW is anchored to this structural paper, replacing the old proposal's inappropriate reliance on PMID:8702755. No NEW process is proposed.

Short verbatim anchors now support localization, human catalytic structure, the substrate reaction and the cofactor judgment in the YAML. Original experimental publications are restored alongside corroboration, including the MitoCoP HTP source [PMID:34800366]. Citation correctness distinguishes verified identity/assay context from uninspected supplementary pairs; the exact human experiment behind PMID:8702755 remains explicitly unverified. HPA's GO_REF describes the annotation method and is retained as original_reference_id; it is not presented as an independently inspected image or as biological corroboration.

The broad catalytic row remains MODIFY under the supplied ActionEnum for overly general terms. Its replacement is already represented and is not advertised as new coverage. The broad metabolic source assertion likewise describes chemistry that BCAT2 directly performs. No new parent/child annotation is added. Structured substrates remain omitted from the single core because those substrates are already implied by the named transaminase MF, following the core-function synthesis convention; their names and reaction products are explicit in the biological description and reaction citations.

The notes remain an append-only record. Earlier processing details and decisions are historical, not current conclusions.

### Focused verification of the evidence follow-up

The applied review retains 41 source assertions and two UniProt products, with one directly supported PLP-binding NEW and one catalytic core. Focused gene validation passed with eight advisories: seven supported generic interactions remain non-core under the supplied ActionEnum, and one advisory concerns not directly citing the unchanged generated research report. The biological evidence is instead tied to primary papers and curated records. HTML rendering passed. No global validation result is claimed. Earlier notes remain historical; this follow-up states the current decisions.
