# USP25 (folder labeled USP21) — review notes

## IMPORTANT identity note
The folder is named `USP21`, but the UniProt record (`USP21-uniprot.txt`), GOA file, and
**all** existing annotations are for **USP25** (UniProt `Q9UHP3`, `UBP25_HUMAN`, HGNC:12624).
The UniProt entry lists `GN Name=USP25; Synonyms=USP21` — historically USP25 was briefly
called "USP21" / "USP on chromosome 21" in early papers (PubMed:10644437), which is the
likely source of the folder name. The protein here is USP25, *not* the distinct gene
USP21 (Q9UKM4). All review content below pertains to Q9UHP3 = USP25. The `gene_symbol`
field is set to `USP25` to match the actual record (correct HGNC symbol for Q9UHP3).

## Core identity
USP25 is a cysteine (papain-like, peptidase C19 family) deubiquitinating enzyme (DUB),
EC 3.4.19.12, with an N-terminal UBA + tandem UIM (ubiquitin-interacting motif) region,
a catalytic USP domain (active-site Cys-178), and a C-terminal region mediating
oligomerization (active homodimer vs. inhibited homotetramer).
[file:human/USP21/USP21-uniprot.txt "Belongs to the peptidase C19 family"]
[file:human/USP21/USP21-uniprot.txt "ACT_SITE 178"]

## Catalytic function (well established, EXP/IDA)
Hydrolyzes ubiquitin (and SUMO/ubiquitin-like) from substrates; cleaves both K48- and
K63-linked chains.
[file:human/USP21/USP21-uniprot.txt "Deubiquitinating enzyme that hydrolyzes ubiquitin moieties conjugated to substrates"]
EXP catalytic activity: PMID:23042150 (IL-17/TRAF), PMID:37339955 (KEAP1-NRF2).
C178S abrogates DUB activity. [file:human/USP21/USP21-uniprot.txt "C->S: Abrogates deubiquitinating activity"]

## Substrate / pathway roles (each via deubiquitination)
- **Wnt/beta-catenin**: deubiquitinates and stabilizes tankyrases TNKS1/TNKS2
  (PMID:28619731, PMID:30926243, PMID:38875478). UniProt FUNCTION + interaction with TNKS2.
- **KEAP1-NRF2 oxidative-stress axis**: deubiquitinates/stabilizes KEAP1, promoting NRF2
  degradation; USP25 loss is protective in acetaminophen liver injury (PMID:37339955).
  -> GO:1902883 negative regulation of response to oxidative stress (IDA).
- **IL-17 signaling / inflammation**: removes K63-Ub from TRAF5/TRAF6, negatively
  regulating IL-17 signaling (PMID:23042150).
  -> GO:1903882 negative regulation of IL-17-mediated signaling (IDA).
- **Innate antiviral / endotoxin tolerance**: stabilizes TRAF3 (PMID:30579117); ERLIN1/2
  + cholesterol flux to restrict virus (PMID:37683630).
- **ERAD**: counteracts HRD1-mediated ubiquitination of ERAD substrates, rescuing them
  from degradation; interacts with HRD1/SYVN1 (Q86TM6) and VCP/p97 (P55072)
  [PMID:22590560 "USP25 counteracts ubiquitination of ERAD substrates by the ubiquitin ligase HRD1, rescuing them from degradation by the proteasome"]
  -> GO:1904293 negative regulation of ERAD pathway (IMP), GO:0031625 (HRD1 binding),
     GO:0051117 ATPase binding (VCP).
- **Muscle**: muscle-specific isoform USP25m stabilizes MYBPC1, interacts with ACTA1/FLNC
  (PMID:16501887).

## Regulation
SUMOylated at Lys-99 (SUMO2/3 preferred) which impairs Ub binding/hydrolysis; the N-terminal
SIM mediates paralog-specific SUMO binding (PMID:18538659). -> GO:0032183 SUMO binding.
Ubiquitinated by SMURF1 (K48) -> degradation (PMID:29518389). Phosphorylated by SYK
(PMID:19909739). Oligomerization (tetramer = inhibited; dimer = active) regulates activity
(PMID:30478318, PMID:30926243).

## Localization
Cytoplasm/cytosol (multiple EXP/IDA: PMID:19440361, PMID:28619731, PMID:38875478, HPA).
ER membrane association in ERAD context (PMID:22590560, IDA). Nucleus is IEA-only (from
UniProtKB-SubCell keyword, transient nuclear punctate in myotubes for USP25m) — weak.

## Disease
Heterozygous variants cause idiopathic generalized epilepsy 19 (EIG19); a C-terminal
truncation is a gain-of-function (forms active dimers, not inhibited tetramers)
(PMID:38875478).

## Interactome (IPI protein binding) — WITH partners from GOA
- 21516116, 32707033: SYK (P43405) — validated interaction (PMID:19909739).
- 22153077, 35914814: TNKS2 (Q9H2K2) — substrate, validated (Wnt).
- 28514442, 31515488, 32296183, 40205054, 33961781, 25416956, 32814053: RAD23A/RAD23B
  (P54725/P54727) — recurrent proteasome-shuttle UBA-domain proteins; plausible.
- 33060197, 34232536, 36217029: SARS-CoV-2 rep/nsp3 (P0DTD1) — viral interactome screens.
- 18538659: SUMO3 (P55854) — basis of SUMO binding MF.
- Others (GDI1, MAGEB4, MID2, PRKACA, PUS10, TMEM43, TGFBR2, ZNF426, SUMO2): mostly
  single high-throughput screens; uninformative as bare "protein binding".

## RQC relevance
Despite the batch theme, USP25's documented roles are Wnt/tankyrase, KEAP1-NRF2, IL-17/innate
immunity, and ERAD — not collided-ribosome surveillance. No strong evidence ties USP25 to
ribosome-associated quality control. (The RQC-associated DUB framing in the task note appears
to belong to USP21, a different gene.)
</content>
