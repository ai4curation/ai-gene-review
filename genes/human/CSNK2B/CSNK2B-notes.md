# CSNK2B (Casein kinase II subunit beta) — Review notes

UniProt: P67870 (CSK2B_HUMAN); HGNC:2460; gene CSNK2B; 215 aa; chr 6p21.33 (MHC class III region).

## Core biology

CSNK2B is the regulatory **beta subunit** of protein kinase CK2 (casein kinase 2), a
constitutively active, highly pleiotropic acidophilic Ser/Thr kinase. The CK2 holoenzyme is a
heterotetramer: two catalytic subunits (CSNK2A1/alpha and/or CSNK2A2/alpha') bridged by a
**CSNK2B beta dimer** (alpha2beta2). CSNK2B itself has **no catalytic activity**; it dimerizes via a
zinc-finger (Zn-binding residues Cys109, Cys114, Cys137, Cys140 — [file:human/CSNK2B/CSNK2B-uniprot.txt]),
docks the two catalytic subunits, stabilizes the holoenzyme, raises basal catalytic activity, and
modulates substrate specificity/selectivity, sometimes recruiting substrates directly
[PMID:11574463 "Crystal structure of human protein kinase CK2: insights into basic properties of the CK2 holoenzyme"].

CK2 consensus is S/T-X-X-D/E (acidic at +3) and the enzyme phosphorylates hundreds of substrates,
affecting transcription, translation, cell-cycle, DNA repair, Wnt and other signaling, apoptosis
(major recognized role: counteracting apoptosis), and circadian rhythm
[PMID:28031292 "CK2 is a highly pleiotropic and constitutively active enzyme ... It phosphorylates hundreds of substrates (21) and controls many cellular processes, but its major recognized function is in counteracting apoptosis"].

CK2beta is required for assembly, stability and substrate selection of the holoenzyme, and also has
roles independent of CK2 enzymatic activity including negative regulation of cell proliferation
[PMID:19324893 "The CK2beta subunit is important in the assembly of CK2, enzyme stability and enzyme activity. It can interact with modulators of CK2 activity as well as with CK2 substrates and is thought to be required for the selection of substrates. CK2beta also has roles that are independent of CK2 enzymatic activity and these include the negative regulation of cell proliferation"].

## Structure / domains

- Zinc-finger-mediated homodimerization; crystal structures 1QF8 (reg subunit), 1JWH (holoenzyme with CSNK2A1).
  [PMID:11574463]
- C-terminal region 188–193 contacts the alpha subunit.
- **KSSR motif** (residues 147–150) forms a protein-interaction pocket mediating binding to cellular
  and viral partners (ARK2N/ARKL1, EBV EBNA1). KSSR->AAAA abolishes ARK2N and EBNA1 binding but not
  CSNK2A1 binding [PMID:24216761 (UniProt MUTAGEN annotation); file:human/CSNK2B/CSNK2B-uniprot.txt].

## Substrate-recruitment / adaptor functions (CK2beta as docking/scaffold)

CK2beta mediates interactions of the holoenzyme with specific substrates and can redirect CK2 toward
specific substrates [PMID:20719947 "CK2beta is important for enhancing the catalytic activity and stability of the enzyme and can mediate interactions with CK2 substrates ... protein interactions with CK2beta can redirect CK2 to increase CK2 activity toward specific substrates"].

Specific examples:
- **p53 Ser392 phosphorylation**: CK2 forms a CK2–SPT16–SSRP1 (FACT) complex after UV; CK2beta mediates
  assembly [UniProt SUBUNIT; PMID:11239457/12393879 cited in UniProt].
- **MuSK**: CK2-dependent phosphorylation regulates AChR aggregation at the NMJ; CK2beta interacts with MuSK
  [PMID:16818610 cited in UniProt FUNCTION].
- **PRH/HHEX (HHEX homeodomain)**: CK2beta binds PRH (Y2H + cells) and CK2 phosphorylates PRH homeodomain
  (S163/S177), acting as a reversible switch inhibiting PRH DNA binding and transcriptional regulation
  [PMID:19324893]. Source of the GO:0061629 (transcription-factor binding) and GO:0008285 (neg reg
  proliferation) annotations.
- **HSJ1/DNAJB2**: CK2 phosphorylates the UIM2 (Ser250 dominant, Ser247 hierarchical), reducing HSJ1 binding
  to ubiquitylated clients and chaperone activity; CK2 inhibition enhances HSJ1 client binding — i.e. CK2
  negatively regulates proteasomal degradation of HSJ1 clients (GO:0032435)
  [PMID:28031292].
- **ALK1/ACVRL1 signaling**: CK2beta binds ALK-1 cytoplasmic domain (res 181–199 of CK2beta), enhancing
  Smad1/5/8 phosphorylation and ALK-1 reporter activity in response to TGF-beta1/BMP-9, and antagonizing
  endothelial cell migration and tubule formation. siRNA of CK2beta reduces Smad1/5/8 signaling. Basis for
  GO:0060391, GO:0032927, GO:0005102 (ACVRL1/P37023 binding), GO:0043537, GO:0061154
  [PMID:19592636].
- **AdipoR1/adiponectin signaling**: CK2 (regulatory subunit) binds AdipoR1 N-terminus (Y2H, co-IP, co-loc);
  CK2 inhibitor DMAT modulates adiponectin signaling. Basis for GO:0005102 (AdipoR1/Q96A54), GO:0005737,
  GO:0005886, GO:0033211 [PMID:19233263].

## Viral / PML

- EBV EBNA1 binds CK2 directly via CK2beta (KSSR pocket), increasing CK2 occupancy at PML bodies and PML
  phosphorylation (S517), triggering PML polyubiquitylation/degradation — disruption of host PML nuclear
  bodies. Basis for GO:0016605 (PML body, is_active_in), GO:0075342 [PMID:20719947, PMID:24216761].
- ARKL1/ARK2N: CK2beta mediates ARKL1–c-Jun interaction; silencing CK2beta (not CK2alpha) phenocopies ARKL1
  silencing and promotes EBV reactivation — CK2beta is needed for ARKL1's repression of Zp/BZLF1 (negative
  regulation of viral life cycle). Basis for GO:1903901, GO:0030674 (adaptor activity bridging ARK2N–Jun),
  GO:0000785 (chromatin is_active_in at Zp). [PMID:31341047].

## Polycomb / chromatin

- CK2 (CSNK2A/B) is a bona fide component of a subset of non-canonical PRC1 complexes (PRC1-AUTS2 / PCGF
  variants). In PRC1-AUTS2, the CK2 component phosphorylates RING1B and **neutralizes PRC1 repressive
  activity**, converting it to an activating complex; AUTS2 recruits P300
  [PMID:25519132 "the CK2 component of PRC1-AUTS2 neutralizes PRC1 repressive activity, whereas AUTS2-mediated recruitment of P300 leads to gene activation"].
- CSNK2B co-purifies with PcG/CBX proteins and RING1B/RNF2 [PMID:21282530; PMID:22325352; PMID:27705803].
  ComplexPortal/NAS annotations assign CSNK2B to PRC1 complex (GO:0035102), chromatin (GO:0000785),
  heterochromatin formation (GO:0031507) and positive regulation of transcription (GO:0045893) on this
  basis. These are complex-membership / process transfers driven by the broader PRC1-AUTS2 complex;
  CSNK2B's direct contribution is its kinase-regulatory role within the embedded CK2.

## Localization

- Nucleus (EXP, IDA: PMID:31341047, PMID:21282530); nucleoplasm/fibrillar center (HPA IDA); cytoplasm and
  plasma-membrane co-localization in adiponectin signaling context (PMID:19233263). CK2 is broadly
  cytosolic and nuclear. Reactome assigns cytosol/nucleoplasm. "Extracellular region", "secretory granule
  lumen", "ficolin-1-rich granule lumen", "extracellular exosome" are bulk-secretome/neutrophil-degranulation
  transfers (Reactome TAS, HDA) — not the core localization of an intracellular kinase subunit.

## Disease

- Poirier-Bienvenu neurodevelopmental syndrome (POBINDS; MIM 618732): autosomal dominant, seizures in
  infancy, developmental delay, intellectual disability; de novo / splice-site / missense variants;
  haploinsufficiency mechanism [PMID:28585349; PMID:31784560; PMID:36833176].

## Interactome (mostly high-throughput Y2H/AP-MS GO:0005515 "protein binding")

The bulk of GO:0005515 IPI annotations are from large-scale interactome / AP-MS / Y2H screens (e.g.
PMID:32296183, 33961781, 35271311, 32707033, 21988832, 23555304, 40205054, 26496610, etc.). The
biologically central, repeatedly recovered partners are the CK2 catalytic subunits CSNK2A1 (P68400) and
CSNK2A2 (P19784) and CSNK2B itself (homodimer, identical protein binding GO:0042802). Many other partners
(RPS6KA3/RSK2, RNF2, SIRT1, etc.) are reported but "protein binding" is uninformative as a function term.

## Summary of curation stance

- Core MF: protein kinase regulator activity (GO:0019887) within the CK2 holoenzyme; molecular adaptor /
  scaffold (GO:0030674) recruiting substrates/partners. CSNK2B does NOT itself have kinase activity, so
  GO:0004674 enables/contributes_to annotations are problematic (see below).
- Core CC: protein kinase CK2 complex (GO:0005956).
- Direct biological role best captured as protein phosphorylation (the holoenzyme activity it regulates);
  most downstream BP terms (Wnt, transcription, circadian, viral, SMAD, etc.) are substrate-driven
  pleiotropy and are non-core.
- The GO:0004674 "protein serine/threonine kinase activity" annotations: with `contributes_to` qualifier
  (PMID:28031292, PMID:1856204) this is the accepted way to annotate a non-catalytic subunit of an active
  kinase complex (the subunit contributes to the complex's activity) — ACCEPT/KEEP. The single `enables`
  GO:0004674 IDA (PMID:15723517) is misleading because CSNK2B does not enable kinase activity on its own;
  better is contributes_to / the regulator term — MODIFY.
