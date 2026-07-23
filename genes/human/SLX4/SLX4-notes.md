# SLX4 (FANCP / BTBD12) — gene review notes

UniProt: Q8IY92 (SLX4_HUMAN), 1834 aa, chromosome 16. HGNC:23845.
Synonyms: BTBD12, KIAA1784, KIAA1987. Disease: Fanconi anemia complementation group P (FANCP, MIM:613951).

## Core biology (synthesis)

SLX4 is a large multidomain scaffold protein that assembles and coordinates three
structure-specific endonucleases — SLX1, XPF-ERCC1 (ERCC4-ERCC1), and MUS81-EME1 —
and stimulates their nucleolytic activity. It is itself catalytically inert (nuclease-dead):
it activates and positions its partner nucleases rather than cutting DNA on its own.

Provenance:
- [PMID:19595721 "Here we describe the identification of human SLX4, a scaffold for DNA repair nucleases XPF-ERCC1, MUS81-EME1, and SLX1."]
- [PMID:19595721 "SLX4 immunoprecipitates show SLX1-dependent nuclease activity toward Holliday junctions and MUS81-dependent activity toward other branched DNA structures."]
- [PMID:19595721 "Furthermore, SLX4 enhances the nuclease activity of SLX1, MUS81, and XPF."]
- [PMID:19596235 "Human SLX4 forms a multiprotein complex with the ERCC4(XPF)-ERCC1, MUS81-EME1, and SLX1 endonucleases and also associates with MSH2/MSH3 mismatch repair complex, telomere binding complex TERF2(TRF2)-TERF2IP(RAP1), the protein kinase PLK1 and the uncharacterized protein C20orf94."]
- [PMID:19596235 "unlike other endonucleases associated with SLX4, the SLX1-SLX4 module promotes symmetrical cleavage of static and migrating Holliday junctions (HJs), identifying SLX1-SLX4 as a HJ resolvase. Thus, SLX4 assembles a modular toolkit for repair of specific"]
- UniProt FUNCTION: [Q8IY92 "Regulatory subunit that interacts with and increases the activity of different structure-specific endonucleases."]
- [PMID:21240275 "SLX4 is a multidomain scaffold protein interacting with three distinct nucleases SLX1, ERCC4/XPF-ERCC1, and MUS81-EME1... While the SLX4-SLX1 interaction is largely responsible for the Holliday junction resolvase activity seen in the complex, SLX4 can also stimulate the activity of ERCC4/XPF and MUS81 nucleases, both of which have been previously implicated in the processing of interstrand crosslinks (ICLs)."]

## Domains (UniProt Q8IY92 feature table)
- Tandem UBZ4-type zinc fingers (aa 293-323, 333-361): ubiquitin binding; bind K63 ubiquitin chains
  [PMID:21240275 "showed binding of the isolated UBZ domains of SLX4 to the K63 chains of ubiquitin"]
- BTB/POZ domain (aa 691-764): oligomerization/dimerization module (BTB_POZ_BTBD12_SLX4, cd18288).
- SAP domain (SAP_SLX4, cd22999): DNA-binding motif (MLR/SAP).
- Coiled coil (aa 801-870).
- Interaction regions: 1..669 with SLX4IP, ERCC4/XPF and MSH2; 1328-1648 with MUS81; 1632-1834 with SLX1;
  684-1834 with PLK1 and TERF2-TERF2IP.
- Heavily SUMOylated (many SUMO2 isopeptide crosslinks); phosphoprotein (mitotic phosphosites incl. Ser1469).

## Function domains / roles
- Interstrand crosslink (ICL) repair "unhooking": biallelic loss causes Fanconi anemia (FA-P / FANCP).
  [PMID:21240275 "biallelic mutations in SLX4/FANCP cause a new subtype of Fanconi anemia, FA-P"]
  [PMID:21240277 abstract "SLX4, which coordinates three separate endonucleases, was recently recognized as an important regulator of DNA repair. Here we report the first human individuals found to have biallelic mutations in SLX4."]
  SLX4 depletion does NOT affect FANCD2 monoubiquitination — SLX4 acts downstream of / parallel to the ID2 complex:
  [PMID:21240275 "As depletion of SLX4 in a U2OS cell line does not affect FANCD2 ubiquitination"]
- Holliday junction resolution (mitotic): SLX1-SLX4 symmetrical HJ cleavage (see 19596235 above).
- DSB repair via homologous recombination / single-strand annealing: SLX4 depletion reduces DSB-induced HR and SSA.
  [PMID:19595721 "Depletion of SLX4 causes a decrease in DSB-induced homologous recombination."]
- Telomere maintenance (ALT / telomere trimming): SLX4-TRF2 scaffold bridges SLX1/XPF/MUS81 to telomeres;
  negatively regulates telomere length by nucleolytic resolution, generating telomeric circles (t-circles).
  [PMID:24012755 "SLX4 assembles an endonuclease toolkit that negatively regulates telomere length via SLX1-catalyzed nucleolytic resolution of telomere DNA structures."]
  [PMID:24012755 "the SLX4-TRF2 complex serves as a double-layer scaffold bridging multiple endonucleases with telomeres for recombination-based telomere maintenance."]

## Complexes / localization
- Slx1-Slx4 complex (GO:0033557) — structure-specific endonuclease complex (ComplexPortal CPX-8175).
- SLX4-TERF2 complex (ComplexPortal CPX-484).
- Localizes to nucleus, nucleoplasm, chromatin, nuclear chromosome, telomeric region; recruited to sites of DNA damage.
  [PMID:19596235 SUBCELLULAR LOCATION Nucleus; "Localizes to sites of DNA damage."]

## Notes on specific GOA annotations
- GO:0008047 enzyme activator activity (IDA, PMID:19596235): the most informative MF — SLX4 stimulates
  the nuclease activity of its partners. Core.
- GO:0005515 protein binding: many IPI entries (endonuclease partners + high-throughput interactome screens
  PMID:25852190/29892012/32296183/32707033/33961781/40205054). Uninformative parent term → over-annotated;
  the informative content is captured by molecular adaptor + enzyme activator activity in core_functions.
- GO:0072429 response to intra-S DNA damage checkpoint signaling (IMP, PMID:23361013): the cached abstract of
  PMID:23361013 (Fugger et al.) concerns FBH1/MUS81, not SLX4; MGI made this acts_upstream_of_or_within
  annotation. Cannot verify an SLX4-specific role from available text → UNDECIDED (experimental, not removed).
- GO:0006260 DNA replication (IEA, NAS): SLX4 acts on replication-associated intermediates/forks, not on
  replication per se → over-annotated (broad/misleading process parent).
- GO:0006289 nucleotide-excision repair (IMP, PMID:19596236): XPF-ERCC1 is the NER nuclease; SLX4 modulates it
  but is not a canonical NER factor → keep as non-core.
