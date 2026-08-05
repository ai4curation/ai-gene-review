# FANCI (Q9NVI1) review notes

Human Fanconi anemia group I protein. HGNC:25568. 1328 aa. Chromosome 15.

## Core biology (synthesized)

FANCI is the obligate heterodimeric partner of FANCD2, forming the FANCI-FANCD2
(ID2) complex, the central effector of the Fanconi anemia (FA) DNA-repair pathway.
Both proteins are monoubiquitinated (FANCI on Lys523) by the FANCL/UBE2T ligase
acting downstream of the multi-subunit FA core complex. Monoubiquitination is
mutually interdependent, and FANCI is required to promote FANCD2 monoubiquitination.
The ID2 complex binds and scans dsDNA with preference for branched structures
(Holliday junctions, overhangs, replication forks); upon monoubiquitination it
rearranges into a closed sliding clamp that encircles duplex DNA to coordinate ICL
repair (nucleolytic incision/unhooking, translesion synthesis, homologous
recombination). FANCI phosphorylation by ATR (S/TQ cluster) acts as a molecular
switch turning the pathway on. Disease: Fanconi anemia complementation group I
(biallelic FANCI mutations).

## Provenance

- Identity / paralog / monoubiquitination at K523 / FANCD2 interaction:
  [PMID:17460694 "A FANCD2 protein sequence-based homology search facilitated the discovery of FANCI, a second monoubiquitinated component of the FA pathway. Biallelic mutations in the gene coding for this protein were found in cells from four FA patients, including an FA-I reference cell line."]

- ID2 complex required for ICL repair; monoubiquitination essential:
  [PMID:32269332 "The ID complex, involving the proteins FANCI and FANCD2, is required for the repair of DNA interstrand crosslinks (ICL) and related lesions"]
  [PMID:32269332 "Monoubiquitination of ID is essential for ICL repair by excision, translesion synthesis and homologous recombination"]

- DNA clamp / encircles DNA:
  [PMID:32269332 "we report a cryo-electron microscopy structure of the monoubiquitinated human ID complex bound to DNA, and reveal that it forms a closed ring that encircles the DNA"]
  [PMID:32269332 "the monoubiquitinated ID complex loses its preference for ICL and related branched DNA structures, and becomes a sliding DNA clamp that can coordinate the subsequent repair reactions"]

- DNA binding, preference for branched DNA:
  [PMID:32269332 "FANCI and FANCD2 are paralogs that bind to DNA with preference for branched structures including Holliday junction, overhang and replication fork DNA"]

- FANCI required for replication-coupled ICL repair in S phase:
  [PMID:19965384 "Using a cell-free system, we showed that FANCI-FANCD2 is required for replication-coupled ICL repair in S phase."]
  [PMID:19965384 "A central event in the activation of the Fanconi anemia pathway is the mono-ubiquitylation of the FANCI-FANCD2 complex"]

- FANCI phosphorylation = molecular switch that promotes FANCD2 monoubiquitination:
  [PMID:18931676 "FANCI carrying phosphomimic mutations on the same six residues induces constitutive monoubiquitination and focus formation of FANCI and FANCD2, and protects against cell killing and chromosome breakage by DNA interstrand cross-linking agents. We propose that the multiple phosphorylation of FANCI serves as a molecular switch in activation of the Fanconi anemia pathway."]
  [PMID:18931676 "FANCI phosphorylation exerts an evolutionarily conserved function in inducing FANCD2 monoubiqutination in human cells as well."]

- FANCD2 monoubiquitination targets ID to chromatin:
  [PMID:18931676 "In turn, FancD2 and FancI are both targeted to chromatin and form colocalizing foci together with the HR proteins BRCA1 and Rad51"]

- FAN1 interaction (FAN1 recruited by monoubiquitinated FANCD2; FANCI co-purifies):
  [PMID:20603015 "a highly conserved protein, KIAA1018/MTMR15/FAN1, that interacts with, and is recruited to sites of DNA damage by, the monoubiquitinated form of FANCD2"]

- POLN interaction / role in crosslink repair and HR:
  [PMID:19995904 "we obtained evidence for physical and functional interaction of POLN with factors belonging to the Fanconi anemia pathway, a master regulator of cross-link repair"]

- CTDP1 interaction / regulation of FANCI:
  [PMID:31240132 "CTDP1 was found to regulate multiple aspects of FANCI activity, including chromatin localization, interaction with γ-H2AX, and SQ motif phosphorylations."]

## Localization caveats

- Cytoplasm (UniProt SL / IDA PMID:18445686): PMID:18445686 is an EML3-focused
  mitotic-spindle proteomics paper; FANCI is overwhelmingly a nuclear DNA-repair
  protein. Cytoplasmic annotation is at best a minor/incidental pool -> over-annotated.
- Membrane GO:0016020 (HDA PMID:19946888): from a bulk NK-cell membrane-fraction
  mass-spec survey. FANCI has NO transmembrane region (UniProt) and is a soluble
  nuclear protein. The paper itself notes ~60% of identified proteins are NOT
  plausible membrane proteins and are "transiently associated with membranes"
  [PMID:19946888 "approximately 40% of the identified proteins were predicted as plausible membrane proteins. The remaining species were largely involved in cellular processes and molecular functions that could be predicted to be transiently associated with membranes."]
  -> co-purification artifact; REMOVE.

## MF gap

GOA export lacks a DNA-binding MF term for FANCI even though UniProt carries the
DNA-binding keyword and DNA binding is FANCI's defining biochemical activity
(branched/duplex DNA binding; clamp). Added GO:0003677 as NEW.
</content>
