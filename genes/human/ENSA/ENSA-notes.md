# ENSA (alpha-endosulfine, O43768) - curation notes

## Identity and paralog caveat

- ENSA (ARPP-19e) and ARPP19 are separate endosulfine-family genes; the conserved central region
  (ENSA Ser67 / ARPP19 Ser62 = Greatwall site; ENSA Ser109 / ARPP19 Ser104 = PKA site) is nearly
  identical and many antibodies/siRNA designs hit both, so "ENSA/ARPP19" statements cannot be
  assigned to ENSA alone [PMID:32085646 "microtubule-associated serine/threonine kinase-like (MASTL), which phosphorylates the cAMP-regulated phosphoproteins 19 (ARPP19) at S62 and 19e/α-endosulfine (ENSA) at S67and converts them into protein phosphatase 2A (PP2A) inhibitors"].
- Human ENSA is intrinsically disordered with three transient helices [PMID:34346186 "The results clearly indicate that ENSA is an intrinsically disordered protein containing three transient α-helical structures."]. No signal peptide [PMID:9653196 "There is no obvious signal peptide sequence at the N terminus, suggesting that α-endosulfine is an intracellular protein."].

## Core function: Greatwall-gated PP2A-B55 inhibitor

- Discovery in Xenopus egg extracts: Gwl-phosphorylated Ensa is the mitotic PP2A-B55δ inhibitor
  [PMID:21164013 "This converts Ensa into a potent and specific inhibitor of PP2A-B55δ."]; the companion paper found both Arpp19 and Ensa are Gwl substrates but Arpp19 is limiting for mitotic entry in extracts [PMID:21164014 "Although both proteins can inhibit PP2A, endogenous Arpp19, but not α-Endosulfine, is responsible for PP2A inhibition at mitotic entry in Xenopus egg extracts."].
- Mechanism: inhibition by unfair competition - pEndos is a high-affinity, slowly processed PP2A-B55 substrate [PMID:24618897 "As the name suggests, during M phase PP2A-B55's attention is diverted to pEndos, which binds much more avidly and is dephosphorylated more slowly than other substrates."]. The Ser67 region docks at the B55/C-subunit interface over the catalytic centre [PMID:24354984 "the most-conserved middle region of ENSA containing S67 physically interacts with PP2A-B55 at the interface of the B55 and C subunits, where the catalytic centre of PP2A is located."].
- Human cells: in HeLa, ENSA rather than ARPP19 is the major MASTL substrate [PMID:24120663 "ENSA is the major target of Greatwall/MASTL in these cells."]; PP2A-B55 is the ENSA Ser67 phosphatase [PMID:24120663 "indicating that PP2A-B55 is the ENSA phosphatase in this system."]; the ENSA/Greatwall timer delays PP2A-B55 reactivation so cytokinesis follows chromosome separation [PMID:24120663 "Removal of the ENSA/Greatwall (EG) timer module eliminates this second threshold, as well as associated delay in PRC1 dephosphorylation and initiation of cytokinesis"]. Fcp1 also contributes to Ensa/ARPP19 Ser67 dephosphorylation at mitotic exit [PMID:24391510 "Ensa/ARPP19 dephosphorylation is mediated by the RNA Polymerase II carboxy terminal domain phosphatase Fcp1."].
- Only the MASTL-site phosphoform inhibits PP2A; the PKA/PKG Ser109 form is a substrate but not an inhibitor [PMID:32085646 "only MASTL-phosphorylated ENSA/ARPP19 are PP2A inhibitors."]. Present at ~7,800 copies in anucleate platelets (deep research summary of the same paper).
- Structural note: in vitro, human ENSA binds the PP2A A subunit more strongly than the B56 subunits tested; B55 was not among the tested B subunits [PMID:34346186 "ENSA was observed to interact PP2A mainly via A-subunit"].

## S-phase role (human)

- Ensa knockdown in HeLa/U2OS dramatically extends S phase with fewer active origins; Treslin protein falls and Treslin overexpression rescues [PMID:28785014 "Unexpectedly, Ensa knockdown promotes a dramatic extension of S phase associated with a lowered density of replication forks."]. Nuclear ENSA increases in S phase [PMID:28785014 "nuclear localisation of Ensa was significantly increased in S-phase cells"]. Mechanism proposed: phospho-ENSA prevents PP2A-mediated Treslin dephosphorylation and hence Cullin-dependent degradation.
- Not annotated in GOA. Raised as a suggested question rather than a NEW term (single study; holoenzyme not pinned down).

## Meiosis (mouse)

- Ensa RNAi in mouse oocytes blocks exit from prophase I, rescued by okadaic acid or Ppp2r2d co-depletion [PMID:24675883 "The majority of ENSA-deficient oocytes fail to exit from prophase I arrest. This function of ENSA in oocytes is dependent on PP2A, and specifically on the regulatory subunit PPP2R2D (also known as B55δ)."]. Not in human GOA; consistent with the core function.

## Historical K-ATP channel / insulin-secretion story

- Cloning paper: recombinant human alpha-endosulfine displaces [3H]glibenclamide from MIN6 membranes (ED50 ~1 μM), reduces Kir6.2/SUR1 currents (~75% at 2 μM; no effect on Kir1.1) and stimulates insulin release at 1 mM glucose [PMID:9653196 "The recombinant protein displaces binding of the sulfonylurea [3H]glibenclamide to beta cell membranes, inhibits cloned KATP channel currents, and stimulates insulin secretion."]. Caveats stated by the authors: interacting subunit unknown [PMID:9653196 "We therefore cannot exclude the alternative possibility that α-endosulfine binds to Kir6.2"]; effect from both sides of the membrane [PMID:9653196 "α-endosulfine blocked K ATP currents when applied both intracellularly and extracellularly"].
- Later assessment: no evidence ENSA is extracellular [PMID:28167675 "However, there is no evidence that ENSA is found extracellularly."]. Mouse brain work links Ensa to a SUR1/Kir6.2 K-ATP-dependent regulation of neprilysin downstream of somatostatin [PMID:34737456 "we identified α-endosulfine (ENSA), an endogenous ligand of the ATP-sensitive potassium (KATP) channel, as a negative regulator of NEP downstream of SST signaling."], keeping the channel connection alive without a biochemical binding demonstration.
- Grading: GO:0019870 potassium channel inhibitor activity IDA -> KEEP_AS_NON_CORE (direct assay, channel-selective, but micromolar and mechanistically unresolved). GO:0050796 regulation of insulin secretion IDA -> MARK_AS_OVER_ANNOTATED (exogenous extracellular protein on a cell line; no loss-of-function support). GO:0005102 signaling receptor binding (IDA, TAS) and GO:0008200 ion channel inhibitor activity (TAS) -> MODIFY to GO:0019870 (displacement assay is indirect; SUR1 is a drug-receptor ABC subunit, not a signalling receptor; the direct readout is channel inhibition). GO:0007584 response to nutrient (TAS) -> REMOVE (full text has no nutrient-response experiment; derived from speculative discussion).

## Other annotations

- GO:0005515 protein binding IPI with ACD/TPP1 [PMID:21044950]: genome-wide BiFC screen hit, ENSA absent from main text, no follow-up -> REMOVE as uninformative (not asserting the signal is false).
- Xenopus ISS transfers (Q7ZXH9): GO:0000086 ACCEPT; GO:0000278 ACCEPT (legitimately broad: G2/M, mitotic exit timing, S phase); GO:0051721 PP2A binding ACCEPT (specific, mechanistic); GO:0019212 and GO:0019888 MODIFY -> GO:0004864.
- IBA GO:0004864 (PTN001309504; Endos, Igo1, Igo, ARPP19) ACCEPT; IBA/IEA cytoplasm ACCEPT; Reactome nucleoplasm TAS ACCEPT (nuclear pool shown in human cells).
- NEW: GO:0010923 negative regulation of phosphatase activity (IDA, PMID:24120663) - the BP counterpart of the inhibitor activity; ARPP19 carries it by IDA and the ARPP19 GO-CAM (gocams/69729a3800000481) uses it.
- SNCA interaction (UniProt SUBUNIT, PMID:17893145): NMR on SDS micelles only; not in GOA, not annotated here.

## Publications fetched for this review (new cache files)

PMID:28785014, 32085646, 34346186, 24391510, 24120663, 24675883, 34686773, 17893145, 24618897,
34737456, 24354984 (via `ai-gene-review fetch-pmid`). 34346186, 34686773, 17893145 and 24354984 are
abstract-only.
