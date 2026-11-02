# Arl1 (Drosophila melanogaster; UniProt P25160; FBgn0000115) - manual literature review

No deep-research API provider was available for this session. This file records a manual
literature survey done from cached publications (publications/PMID_*.md) and a PubMed
search (`(Arl1 OR arf72A OR arflike) AND Drosophila`, 22 hits; the hits that concern the
fly protein are listed below). Each assertion carries its source.

## Identity and family

- Arl1 (historical names arflike/arl, Arf72A, CG6025) encodes a 180-aa small GTPase of the
  Arf family [file:DROME/Arl1/Arl1-uniprot.txt "Belongs to the small GTPase superfamily. Arf family."].
- Predicted N-myristoylation of Gly2 (sequence analysis, ECO:0000255) and Arf-type GTP-binding
  motifs (23-30, 66-70, 125-128; by similarity) [file:DROME/Arl1/Arl1-uniprot.txt].
- Fly and human Arl1 are 78% identical [PMID:26116655 "Analysis of protein sequence shows that
  Drosophila and human Arl1 share 78% identity in their amino acids"].

## Biochemistry

- Recombinant arl protein binds and hydrolyses GTP but lacks ARF activity (cholera-toxin
  cofactor assay) [PMID:1901655 "Biochemical analyses of purified recombinant arl-encoded protein
  revealed properties similar to the ARF proteins, including the ability to bind and hydrolyze GTP.";
  "Clear functional differences between arl and ARF proteins, including a complete lack of ARF
  activity, suggest that arl is not a functional homolog of ARF."]. Abstract only.
- Essential gene: recessive lethal allele [PMID:1901655 "A recessive lethal arl mutation was
  recovered, demonstrating that the arl locus is an essential gene."].

## Effectors (GTP-dependent binding partners)

- GRIP-domain golgins: in a Y2H screen of 27 fly G proteins, Arl1 was the only Arf-family member
  binding all four GRIP-domain golgins (dGolgin-245, dGolgin-97, dGCC88, dGCC185), via their
  C-terminal GRIP domains [PMID:19001129 "Of the Arf family, only Arl1 showed an interaction,
  interacting with all four GRIP domain proteins."; "The mapping data indicate that for all four
  proteins, the C-terminal GRIP domain binds to Arl1 but not to any of the interacting Rabs"].
  In vitro binding was GTP-dependent for three of them [PMID:19001129 "We initially confirmed that
  Arl1 was able to bind to dGolgin-245, dGolgin-97, and dGCC88 in a GTP-dependent manner"].
- Sec71 (BIG1/BIG2 ortholog; Arf1 GEF of the trans-Golgi): found by Arl1-GTP liposome affinity
  purification from S2 extracts; binding is direct, via the region N-terminal to the Sec7 domain
  [PMID:22291037 "Applying this to Drosophila melanogaster cell extracts revealed a direct interaction
  between Arl1 and Sec71, the Drosophila ortholog of the trans-Golgi GEFs BIG1/2."]. Arl1
  overexpression recruits the Sec71 N-terminus to the Golgi [PMID:22291037 "However, when it was
  coexpressed with Drosophila Arl1, this N-terminal region was efficiently recruited to the Golgi"].
  Arl1 and Sec71 colocalize on the trans-Golgi in S2 cells [PMID:22291037 "Thus, Sec71 binds to
  Arl1-coated liposomes in vitro and colocalizes with Arl1 on the trans-Golgi in vivo."].
- Arfaptin (Arfip, BAR-domain protein): Arl1 co-immunoprecipitates with Arfip and is required for
  its perinuclear (Golgi) localization in S2 cells [PMID:26116655 "In agreement with the mammalian
  data, perinuclear distribution of endogenous Arfip in S2 cells was abolished in cells treated with
  dsRNA for Arl1"]. Garz (GBF1 ortholog) is proposed as the Arl1 GEF in this pathway, based on
  genetic interactions [PMID:26116655 "These data are consistent with reduction of Garz function
  resulting in decreased levels of Arl1-GTP and reduced Arfip function during synapse growth."].

## Localization

- Golgi / trans-Golgi: Golgi membranes of photoreceptors [PMID:21693198 "ARF72A localizes to the
  Golgi membranes of Drosophila photoreceptor cells, consistent with mammalian Arl1 localization in
  cell culture systems."]; trans-Golgi with Sec71 in S2 cells [PMID:22291037]; Golgi of motor neuron
  soma with Arfip [PMID:26116655 "These data demonstrate that both Arl1 and Garz colocalize with
  Arfip at the GA in motor neurons."].
- ER: more Arl1 on ER in the ninaE(D1) retinopathy model [PMID:21693198 "Interestingly, our study
  indicated that more ARF72A localized on the endoplasmic reticulum in the ninaE(D1) photoreceptor
  cell, a Drosophila model of autosomal-dominant retinitis pigmentosa, compared to that in the
  wild-type."]. Abstract only; this is a disease-model condition.

## In vivo roles

- Golgin recruitment: in arl1 null clones, dGolgin-245, dGolgin-97 and dGCC88 are lost from the
  Golgi, dGCC185 much less so; Golgi integrity is preserved [PMID:24610947 "The gene is essential,
  and examination of clones of cells lacking Arl1 shows that it is required for recruitment of three
  of the four GRIP domain golgins to the Golgi, with Drosophila GCC185 being less dependent on Arl1.";
  "indicating that Arl1 is not required for Golgi integrity but rather has a more specific role in
  GRIP domain protein recruitment"].
- Secretory granule biogenesis in larval salivary gland, with AP-1 dispersed from TGN; model:
  Arl1 -> Sec71 -> Arf1 -> AP-1 [PMID:24610947 "At a functional level, Arl1 is essential for formation
  of secretory granules in the larval salivary gland."; "Taken together, these results are consistent
  with the model that AP-1 is recruited to the TGN and immature secretory granules by Sec71-dependent
  activation of Arf1 downstream of Arl1."].
- ER quality control / ER-to-Golgi: loss of arf72A expands Golgi and accelerates secretion, and
  suppresses ninaE(D1) degeneration [PMID:21693198 "resulting in over-proliferated Golgi complexes
  and accelerated protein secretion"]. Abstract only.
- Synapse growth: Arl1, Garz and Arfip interact genetically for NMJ bouton number [PMID:26116655
  "Our data support a model in which Arl1 and Garz work in the same genetic pathway to regulate the
  recruitment of Arfip to Golgi membranes in the motor neuron."]. This is a Golgi-based role in the
  neuron soma, not a presynaptic one.

## Synaptic vesicle TAS annotations

- PMID:10798391 is a genome-wide homology screen for fly homologs of mammalian synaptic-vesicle
  cycle genes [PMID:10798391 "We screened the fly genome sequence for homologs of mammalian genes
  implicated directly or indirectly in exocytosis and endocytosis of synaptic vesicles."]. It reports
  no experiment on Arl1. No study places fly Arl1 at the presynapse or in synaptic vesicle recycling.
