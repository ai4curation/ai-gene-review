# GET3 (ASNA1 / TRC40) — review notes

UniProt: O43681 (GET3_HUMAN). HGNC:752. Synonyms: ARSA (HGNC), ASNA1, TRC40.
348 aa, homodimer, arsA ATPase family (HAMAP MF_03112). EC=3.6.4.-.

## Core function: cytosolic ATPase that TARGETS tail-anchored (TA) proteins to the ER

GET3/TRC40/ASNA1 is the central cytosolic ATPase of the GET/TRC pathway. It selectively
recognizes the C-terminal transmembrane domain (TMD) of TA proteins in the cytosol, captures
them (handed off from SGTA via the GET4/UBL4A/BAG6 "bridging"/pre-targeting complex), and
delivers them to the ER-resident WRB/CAML (GET1/GET2) receptor-insertase, where ATP hydrolysis
drives TA release and insertion. **GET3 is the targeting factor / chaperone, NOT the insertase**
(insertase = WRB/CAML = GET1/GET2).

- [file:human/GET3/GET3-uniprot.txt "ATPase required for the post-translational delivery of tail-anchored (TA) proteins to the endoplasmic reticulum"]
- [file:human/GET3/GET3-uniprot.txt "Recognizes and selectively binds the transmembrane domain of TA proteins in the cytosol."]
- [file:human/GET3/GET3-uniprot.txt "This complex then targets to the endoplasmic reticulum by membrane-bound receptors GET1/WRB and CAMLG/GET2, where the tail-anchored protein is released for insertion."]
- [PMID:17382883 "we reveal a cytosolic TMD recognition complex (TRC) that targets TA proteins for insertion into the ER membrane. The highly conserved, 40 kDa ATPase subunit of TRC (which we termed TRC40) was identified as Asna-1."]
- [PMID:17382883 "Subsequent release from TRC40/Asna-1 and insertion into the membrane depends on ATP hydrolysis."]
- [PMID:17382883 "an ATPase-deficient mutant of TRC40/Asna-1 dominantly inhibited TA protein insertion selectively"] — supports MUTAGEN G46R abolishing ATPase + dominantly inhibiting pathway (UniProt FT).
- [PMID:21444755 "Membrane insertion of TA proteins in mammalian cells is mediated by the ATPase TRC40/Asna1 (Get3 in yeast) and a receptor in the ER membrane."]
- [PMID:21444755 "TRC40 is a conserved cytosolic ATPase that recognizes the TMD of TA proteins and delivers them to the ER membrane for insertion"]
- [PMID:23041287 "We identify calcium-modulating cyclophilin ligand (CAML) as a mammal-specific receptor for TRC40, an ATPase targeting newly synthesized TA proteins"]

## ATPase / ATP binding (MF)

- [PMID:9712828 "The GST-hASNA-I exhibited a basal level of ATPase activity of 18.5 +/- 8 nmol/min/mg in the absence of arsenite."] — IDA ATP hydrolysis. Also gives KM/Vmax for ATP (UniProt biophysicochemical).
- [PMID:8884272 "Biochemical analysis using the GST/hARSA-I fusion protein indicated that hARSA-I is an ATPase analogous to the bacterial ArsA."] — IDA ATPase.
- ATP binding/hydrolysis drives the targeting cycle: [file:human/GET3/GET3-uniprot.txt "ATP binding drives the homodimer towards the closed dimer state, facilitating recognition of newly synthesized TA membrane proteins. ATP hydrolysis is required for insertion."]
- ATPase cycle regulated by upstream/downstream factors: [PMID:23610396 "the Get4/5 TA loading complex locks Get3 in the ATP-bound state and primes it for TA protein capture, whereas the TA substrate induces tetramerization of Get3 and activates its ATPase reaction 100-fold."]

## Protein carrier / chaperone activity (MF)

GO:0140597 "protein carrier chaperone" (label in DR line; GOA labels it "protein carrier activity").
GET3 is a TMD chaperone that shields the hydrophobic TA-TMD and carries it to the ER.
- [PMID:23610396 "guided entry of tail-anchored protein 3 (Get3), coordinates the delivery of TA proteins to the endoplasmic reticulum"]
- [PMID:23610396 "Our results establish a precise model for how Get3 harnesses the energy from ATP to drive the membrane localization of TA proteins"]
- [PMID:34887561 "The GET pathway centers around the cytosolic TMD chaperone Get3 (also known as TRC40 or Asna1 in metazoans), a homodimeric ATPase"]

## GET complex / receptor (CC + targeting)

- [file:human/GET3/GET3-uniprot.txt "Component of the Golgi to ER traffic (GET) complex, which is composed of GET1/WRB, CAMLG/GET2 and GET3/TRC40"]
- WRB = receptor: [PMID:21444755 "We have identified tryptophan-rich basic protein (WRB), also known as congenital heart disease protein 5 (CHD5), as the ER membrane receptor for TRC40/Asna1."]
- CAML = receptor, with WRB: [PMID:23041287 "identification of CAML and WRB as components of the TRC40 receptor complex represents a crucial mechanism for driving ER membrane insertion of TA proteins in mammalian cells."]
- Cryo-EM of GET insertase complex: [PMID:32910895 "an insertase (yeast Get1/Get2 or mammalian WRB/CAML) that captures the TA from a cytoplasmic chaperone (Get3 or TRC40, respectively)"] — note: the INSERTASE is WRB/CAML; GET3 is the chaperone.
- ComplexPortal CPX-6464 = GET complex; GOA GET complex part_of annotations (IDA/IPI PMID:32910895, IPI PMID:23041287) are correct.

## Pre-targeting / bridging complex interactions (IPI partners)

- GET4 (TRC35): [file:human/GET3/GET3-uniprot.txt "Interacts with GET4 (PubMed:34887561)."]; GOA IPI partners include UniProtKB:Q7L5D6 (GET4). [PMID:34887561 "interacts with Get4 (also known as TRC35 in metazoans), a subunit of a 'bridging' complex that facilitates client loading onto Get3"]
- CAMLG (P49069): [file:human/GET3/GET3-uniprot.txt "GET3 shows a higher affinity for CAMLG than for GET1"]; IPI partner UniProtKB:P49069 (CAMLG) in PMID:28514442, 33961781, 40205054, 32296183.
- Bag6 complex transfers TA from SGTA to TRC40: [PMID:25535373 "the minimal Bag6 complex defined here facilitates tail-anchored substrate transfer from small glutamine-rich tetratricopeptide repeat-containing protein α to TRC40."] — basis for GO:0071816 IDA (MUTAGEN K86D reduces pathway).
- IntAct binary-interactome IPI captures (PMID:21516116, 25416956, 28514442, 32296183, 33961781, 40205054) include many TA-protein-like ER/secretory partners (AGR2, GPX7/8, PGRMC1/2, FKBP7, PDIA6, RCN1, TMX1, etc.) consistent with TA-client capture, plus GET4/CAMLG. Bare "protein binding" is uninformative; keep non-core. PMID:21911467 is a Yersinia pestis–human PPI screen (xeno partner yscD Q56975) — incidental, non-core.

## Subcellular location

- Cytoplasm/cytosol (site of action): [file:human/GET3/GET3-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm"]; EXP PMID:17382883, 21444755; TAS PMID:9736449.
- ER: [file:human/GET3/GET3-uniprot.txt "Endoplasmic reticulum"]; EXP PMID:17382883, 21444755, 31461301. GET3 visits the ER membrane to dock on WRB/CAML. ER membrane (GO:0005789) NAS from ComplexPortal is reasonable as the GET complex resides there.
- Nucleus/nucleolus: [file:human/GET3/GET3-uniprot.txt "Nucleus, nucleolus"]; reported in early arsenite-ATPase papers [PMID:9736449 "showed a cytoplasmic, perinuclear, and nucleolar distribution"] and HPA IDA. This is a secondary/legacy localization not tied to the core TA-targeting function — keep as non-core.
- Extracellular exosome (HDA, PMID:19056867, urinary exosome proteomics): high-throughput proteomic catalog hit; non-core.

## Legacy / secondary role: arsenite-stimulated ATPase (arsA homolog)

ASNA1 was originally cloned as the human homolog of bacterial arsA (arsenite transporter ATPase
component). The arsenite stimulation is modest and antimonite does NOT stimulate. This is a
legacy biochemical observation reflecting the ancestral arsA ATPase fold; the gene's bona fide
cellular role is TA-protein targeting. Treat arsenite/antimonite transport framing as
secondary/legacy.
- [PMID:8884272 "We have isolated the human homolog of the bacterial arsA (hARSA-I), a member of the ATPase superfamily with no transmembrane domain."]
- [PMID:9712828 "Arsenite produced a 1.6 +/- 0.1-fold stimulation of activity (p = 0. 0044), which was related to an increase in Vmax; antimonite did not stimulate activity."]
- No arsenite/antimonite *transport* GO annotation actually appears in the current GOA (only ATP hydrolysis IDA from these papers) — so there is nothing to MARK_AS_OVER_ANNOTATED here; the IDA ATP-hydrolysis annotations are accepted as the genuine MF.

## Disease

- CMD2H (dilated cardiomyopathy 2H), autosomal recessive, rapidly progressive infantile.
  [PMID:31461301 "Biallelic variants in ASNA1 cause severe pediatric cardiomyopathy and early death."]
  Val163Ala mutant: folded protein captures TA but is "inefficient in facilitating TA protein
  insertion into the ER membrane" — directly supports GO:0071816 IMP. asna1-null zebrafish
  cardiac failure rescued by WT but not mutant human ASNA1 mRNA.

## Annotation decisions summary

- ATP hydrolysis (IBA, IEA, IDA x2): ACCEPT (core MF). ATP binding (IEA): KEEP_AS_NON_CORE (structural, subsidiary to ATPase).
- GO:0071816 TA insertion into ER (IBA/IEA/IMP x2/IDA): ACCEPT as core BP for the experimental/IBA ones; the BP label says "insertion" but is the standard GO term for the GET-pathway role of the targeting factor — accept.
- GO:0045048 protein insertion into ER membrane (IEA InterPro2GO; NAS ComplexPortal): KEEP_AS_NON_CORE / parent-of-71816, redundant general term.
- GO:0140597 protein carrier activity/chaperone (IDA PMID:23610396): ACCEPT (core MF — TMD chaperone/carrier).
- GET complex part_of (IEA/IPI/IDA): ACCEPT.
- protein binding (IPI, 7 refs): KEEP_AS_NON_CORE (bare term; informative partners captured in notes/complex annotations).
- cytoplasm (IEA/EXP/TAS): ACCEPT. ER (IEA/EXP): ACCEPT. ER membrane (NAS): ACCEPT (GET complex resides there).
- nucleolus (IEA/IDA/TAS), nucleoplasm (IDA): KEEP_AS_NON_CORE (legacy/HPA localization, not core function).
- extracellular exosome (HDA): KEEP_AS_NON_CORE (proteomic catalog).
</content>
</invoke>
