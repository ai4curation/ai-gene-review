# PDZD7 (human, Q9H5P4) — curation notes

## 2026-09-04 — annotation review of all GOA rows

### Protein architecture

- 1033 aa, three PDZ domains (86–168, 210–293, 862–934), a harmonin-N-like (HN-like) domain
  (InterPro IPR042786), a central proline-rich/disordered region, and extensive disorder in the
  C-terminal third (UniProt feature table, `PDZD7-uniprot.txt`). No catalytic domain.
- Paralog of the two other Usher PDZ scaffolds: [PMID:25406310 "WHRN ( Fig. 1 ) and PDZD7 ( Fig. 1 )
  proteins are paralogs sharing 55% similarity in amino acid sequence."]; the 2009 discovery paper
  makes the same point for harmonin/whirlin [PMID:19028668 "PDZD7 shares sequence homology with the PDZ
  domain-containing genes, USH1C (harmonin) and DFNB31 (whirlin)"].
- Three annotated isoforms (Q9H5P4-3 displayed, -1, -2); the deep-research report notes shorter
  transcripts terminating before PDZ3 dominate adult retina while the developing cochlea expresses
  N-terminal and rarer full-length forms. Isoform biology is unresolved and I made no
  isoform-specific annotation calls.

### Core function: ankle-link / USH2 complex scaffold

- Site of action: cytoplasmic face of the stereociliary membrane at the **ankle region**, i.e. the
  tapered base of developing hair-cell stereocilia — explicitly *not* the tip/tip-link apparatus
  [file:human/PDZD7/PDZD7-deep-research-falcon.md "Immunofluorescence and tagged-protein studies placed
  PDZD7 immediately above the tapered stereociliary base, peripheral to the actin core. It overlaps
  USH2A, ADGRV1 and WHRN but is distinct from the upper tip-link insertion site where MYO7A clusters."]
  UniProt says the same [file:human/PDZD7/PDZD7-uniprot.txt "Note=Localizes at the ankle region of the
  stereocilia."].
- Complex composition and colocalization [PMID:25406310 "In hair cells, proteins encoded by the four
  genes are colocalized at the ankle link region of the mechanosensitive structure, the hair bundle,
  during development"].
- Assembly logic (the key mechanistic result): [PMID:25406310 "both WHRN and PDZD7 are required for the
  complex formation with USH2A and GPR98"] and [PMID:25406310 "Interaction between WHRN and PDZD7 is the
  bridge between USH2A and GPR98."]. The complex is non-obligate — [PMID:25406310 "the USH2 quaternary
  complex has a variable stoichiometry"] — and partner preference differs [PMID:25406310 "WHRN prefers to
  bind to USH2A, whereas PDZD7 prefers to bind to GPR98"].
- Homodimerization: [PMID:25406310 "PDZD7 is able to form homodimers through the interaction between its
  PDZ2 domains"], matching UniProt [file:human/PDZD7/PDZD7-uniprot.txt "Homodimerizes (via PDZ2 domain).
  Component of USH2 complex,"]. This multivalency is what the 2023 phase-separation work (Wang et al.,
  Nat Commun, not in the publication cache) builds on.
- Direct partner mapping from the 2010 paper: [PMID:20440071 "revealed interaction of PDZD7 (PDZ2
  domain) with the C-terminal intracellular domain of GPR98"] and [PMID:20440071 "the first and second
  PDZ domains of PDZD7 interact with USH2A by coimmunoprecipitation studies"].
- Requirement for partner localization: [PMID:25406310 "where PDZD7 is essential for the normal
  localizations of USH2A, GPR98, and WHRN"]; [file:human/PDZD7/PDZD7-deep-research-falcon.md "PDZD7 loss
  disrupts or redistributes USH2A, ADGRV1 and WHRN in developing cochlear hair cells."]
- Loss of function: [file:human/PDZD7/PDZD7-deep-research-falcon.md "-null mice show congenital profound
  deafness by auditory brainstem response"]; [PMID:25406310 "causes disorganization and gradual
  degeneration of hair bundles in mice"]. Human: DFNB57 [PMID:19028668 "deafness-causing gene and also a
  prime candidate gene for Usher syndrome."], with expression confirmed in the target tissue
  [PMID:19028668 "PDZD7 expression in the human inner ear"].

### Retina / cilium — real but secondary

- Direct localization [PMID:20440071 "we detected the newly predicted C-terminal epitope of PDZD7 at the
  ciliary base of cultured human retinal pigment epithelial (RPE) cells"] and [PMID:20440071 "strong
  labeling at the base of the photoreceptor connecting cilium"]; functional consequence in fish
  [PMID:20440071 "Pdzd7 apparently localizes Gpr98 in the connecting cilium region"].
- But the mouse knockout uncouples this from an essential retinal role [PMID:25406310 "knockout of Pdzd7
  expression in mouse photoreceptors does not affect the localizations of the three USH2 proteins at the
  periciliary membrane complex"]. Hence all cilium rows were kept as **non-core** rather than accepted
  as core.

### Nucleus — over-annotated

- UniProt lists Nucleus from PMID:20440071, but that paper qualifies its own nuclear signal:
  [PMID:20440071 "We also noted some nuclear labeling in the inner retina"] followed by [PMID:20440071
  "we conclude that this label is nonspecific to Pdzd7a"]. Only the perinuclear observation survives
  [PMID:20440071 "PDZD7 is also present in the perinuclear region"]. No nuclear partner, NLS or function
  has been described. Both nucleus rows (IEA and IDA) → MARK_AS_OVER_ANNOTATED (not REMOVE: a curator
  read the full text and cultured-cell signal is reported).

### Judgement calls worth recording

1. **GO:0032426 stereocilium tip (IBA) → REMOVE.** The WITH/FROM of this row is mouse whirlin
   (MGI:2682003) + rat whirlin (RGD:631330) only. Contrast the ankle-link-complex row on the same node
   PTN000563297, which is seeded by mouse Pdzd7 (MGI:3608325). Whirlin is the canonical row-1
   tip-elongation scaffold; PDZD7 has never been reported at tips. Classified as PROPAGATION_BAD /
   WRONG_ORTHOLOG_OR_PARALOG + COMPARTMENT_OR_COMPLEX_MISMATCH — the sources are right for whirlin, the
   transfer is what fails. Donor identities resolved through the GO API
   (`api.geneontology.org/api/bioentity/<id>`): MGI:1919338 = harmonin, MGI:2682003 = whirlin,
   MGI:3608325 = Pdzd7, RGD:1303329 = harmonin, RGD:631330 = whirlin.
2. **GO:0005576 extracellular region (HDA, PMID:22664934) → REMOVE.** Pooled tear-fluid MALDI-TOF-TOF de
   novo proteomics from a breast-cancer biomarker study; PDZD7 is never mentioned in the text. No signal
   peptide, no TM segment; contradicted by every targeted localization study.
3. **GO:0005515 protein binding.** Three rows. The PMID:20440071 (USH2A, ADGRV1) and PMID:19028668
   (USH1G/SANS) rows → MODIFY to GO:0030674 protein-macromolecule adaptor activity, which is what the
   assays actually demonstrate. The PMID:36115835 row → MARK_AS_OVER_ANNOTATED: >30 partners imported
   from one holdup PDZ-PBM affinity matrix, including HPV E6 / HTLV1 Tax and non-co-expressed human
   proteins, with the authors themselves noting [PMID:36115835 "PDZ-PBM interactions are rather transient
   and promiscuous"] and [PMID:36115835 "interactomics using AP-MS from cell extracts may generate false
   negatives (potential preys that are too weakly expressed) as well as false positives (indirect
   interactions)"].
4. **GO:0050910 detection of mechanical stimulus … sound (ISS) → MARK_AS_OVER_ANNOTATED.** Reduced MET
   currents in Pdzd7 mutants are secondary to bundle disorganization; PDZD7 has no described association
   with the MET channel complex (TMC1/2, TMIE, LHFPL5, PCDH15) and is absent from tip-link insertion
   sites. `acts_upstream_of_or_within` keeps it defensible, so not REMOVE.
5. **GO:0045184 establishment of protein localization (ISS) → MODIFY to GO:1990778 protein localization
   to cell periphery.** GO has no "protein localization to stereocilium/ankle link" term (checked
   QuickGO: only stereocilium GO:0032420, stereocilium base GO:0120044, ankle link GO:0002141 exist on
   the CC side). GO:1990778 is the closest informative existing term; a stereocilium-specific term would
   be the right long-term fix.
6. **GO:0060113 inner ear receptor cell differentiation (NAS, ComplexPortal) → MODIFY to GO:0060088.**
   Hair cells differentiate; what fails in mutants is bundle organization.

### Open questions

- Do human PDZD7 isoforms differ in ankle-link vs periciliary function? Mouse data suggest
  tissue-specific isoform usage but human isoform-level data are absent.
- Is the "blocks inhibition of adenylate cyclase activity mediated by ADGRV1" statement in the UniProt
  FUNCTION line (ECO:0000250 from mouse E9Q9W7) supported well enough to warrant a signalling-related GO
  annotation? Not annotated in GOA; left alone here.
- Is there any evidence for the ankle-link condensate (LLPS) in vivo at physiological concentrations?
  The 2023 Nat Commun work is in vitro/ex vivo only; no GO annotation was proposed on that basis.
