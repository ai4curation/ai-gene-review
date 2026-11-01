# SAG1 (P13664, Toxoplasma gondii) - curation notes

**Automated deep research was unavailable for this gene (Falcon authentication and
OpenAI key both failed in this environment). These notes are a manual literature
review** built from the UniProt record (`SAG1-uniprot.txt`), the cached PubMed
records in `publications/`, and PubMed searches (E-utilities) used to locate
classic primary papers, which were then cached with `just fetch-pmid`.
Most cached papers are abstract-only; PMID:34950858 and PMID:40607979 are full text.

## Identity

- SAG1 = P30 = SRS29B, the prototypic member of the SAG1-related sequence (SRS)
  superfamily; locus TGME49_233460 / TGGT1_233460. 336 aa precursor with N-terminal
  signal peptide (1-47) and a C-terminal hydrophobic GPI-addition signal; two SRS
  (Pfam PF04092) domains, six disulfides; structures 1KZQ and 1YNT.
- Single-copy, intronless gene; mRNA extremely abundant
  [PMID:3183382 "The P30 gene is single copy and contains no introns."].
- The C terminus predicted a glycolipid anchor
  [PMID:3183382 "carboxy-terminal hydrophobic tail which is predictive of a posttranslational cleavage and modification with a glycolipid anchor"].
- Tachyzoite-specific: [file:TOXGO/SAG1/SAG1-uniprot.txt "Detected only in rapidly dividing and invasive"].

## Localization

- GPI-anchored in the parasite plasma membrane, shown biochemically:
  [PMID:2925621 "These results argue that P30 is anchored by a glycolipid."];
  [PMID:11522346 "The protein is inserted into the parasite's plasma membrane by a glycosyl-phosphatidylinositol anchor"].
  The GPI anchor carries two glycoforms (GalNAc side branch +/- terminal Glc) [PMID:11522346].
- Note: the UniProt record does not carry a GPI-anchor keyword or a "Cell membrane"
  subcellular location; it records only "Parasitophorous vacuole" with the note that
  SAG1 is on the surface of tachyzoites and in the vesicular network of the PV.
- Surface protein is shed on invasion; some is found in vacuolar extensions of the PV
  [PMID:8570580 "SAG1 is present on the surface of daughter zoites and is found throughout the infected cell in distinct vacuoles; these vacuoles represent either direct extensions of the parasitophorous vacuole or true export of parasite surface material."];
  presence on the intravacuolar network immediately post-invasion was contested
  [PMID:8570580 "Conflicting reports exist concerning the presence of SAG1 on the developing intraphagosomal membrane (IPM) network"].
  So the PV (symbiont-containing vacuole) location is real but secondary to the
  parasite-surface location.

## Structure

- 1.7 A structure: homodimer with a basic groove proposed to bind sulfated
  proteoglycans [PMID:12091874 "This basic groove seems to be conserved among SRS proteins and potentially serves as a sulfated proteoglycan-binding site on target cell surfaces"].
- Monomeric SAG1-Fab structure: immunodominant epitope does not overlap the proposed
  ligand pocket [PMID:16242717 "this conformational epitope, located within the SAG1 N-terminal domain, does not overlap with the proposed ligand-binding pocket"].

## Function: adhesion to host cells

- Antibody blocking: [PMID:1730266 "the overall invasion was reduced to 37% of control values"];
  [PMID:8050521 "Treatment of fresh extracellular T. gondii with rabbit polyclonal anti-SAG-1 serum inhibited parasite attachment to host cells by 71%."];
  SAG1-defective mutants bind less [PMID:8050521 "Attachment assays using mutant parasites with defective SAG-1 (PTgA and PTgC) showed significantly reduced binding (26 and 39%)"].
- Recombinant/purified SAG1 binds host cells directly, partly via glucosamine
  [PMID:15151144 "Soluble BSA-glucosamide blocked SAG1 attachment to MDBK cells in a dose-dependent manner, implying that SAGI binding is mediated, in part, via attachment to host cell surface glucosamine."].
  This is the best evidence that SAG1 itself performs the binding (MF host cell surface binding).
- Clean genetics (CRISPR KO + complement, 2025): fitness defect only in IFNg-treated
  cells; attachment reduced, more so with IFNg; sialic acid dependence
  [PMID:40607979 "SAG1-deficient parasites had reduced attachment efficiency, which was exacerbated in IFNγ-treated cells."];
  [PMID:40607979 "the Δsag1 strain displayed a significantly reduced attachment, with only 81% of WT attachment levels, indicating the important role of SAG1 in mediating adhesion"];
  replication unaffected [PMID:40607979 "suggesting that parasite replication is not affected by SAG1 deletion"].
- Rachinel et al. Deltasag1 still replicates in vitro [PMID:15294991 "In vitro, the mutant parasites replicate in both enterocytes and dendritic cells."].
- Conclusion: SAG1 is a non-essential, partially redundant surface adhesin; its
  participation in attachment is direct (it is the binding molecule), so
  "adhesion of symbiont to host cell" (GO:0044650) and "host cell surface binding"
  (GO:0046812) are appropriate and pass the participation test (SAG1 does the binding;
  it is not a substrate). Comparator: P. falciparum CSP in this repo carries both.
- Receptor identity unresolved: sulfated proteoglycans (structure prediction),
  glucosamine (PMID:15151144), sialic acid (PMID:40607979; heparan sulfate minimal role).

## Host interactions / immune modulation

- Immunodominant antigen; SAG1 alone drives lethal ileitis in C57BL/6
  [PMID:15294991 "C57BL/6 mice orally infected with Deltasag1 parasites failed to develop ileitis."].
- Stage-restricted expression matters for persistence: constitutive SAG1 gives
  encephalitis and high cyst burden later [PMID:15944311].
- Lekutis review: KO suggests immune modulation / virulence attenuation
  [PMID:11566296 "Analyses of a SAG1 knockout in rodents, however, indicate that this surface antigen may play a crucial role in immune modulation or virulence attenuation."].
- Host interactors from single labs, mostly abstract-only: KRCC1 (Y2H, ITC;
  PMID:31165984, PMID:29351065), S100A6 (TurboID proximity, co-IP; PMID:34950858),
  RACK1 (PMID:38157925; intracellular host protein - topologically odd for a
  GPI-anchored surface protein, needs caution).
- S100A6 study (full text): TgSAG1 inhibits S100A6-vimentin interaction and promotes
  TNF via S100A6-vimentin/PKCtheta-NF-kB [PMID:34950858 "As an immunogen, TgSAG1 could promote the secretion of tumor necrosis factor alpha (TNF-α) through S100A6-Vimentin/PKCθ-NF-κB signaling pathway."].
  Treated as preliminary; not annotated as a new process.

## GOA annotations (2 rows, both IEA CC)

1. GO:0016020 membrane (InterPro IPR007226 SRS domain) - true but general; SAG1 is a
   GPI-anchored protein on the outer leaflet of the parasite plasma membrane -> MODIFY to
   plasma membrane (GO:0005886) and external side of plasma membrane (GO:0009897).
2. GO:0020003 symbiont-containing vacuole (UniProt SubCell PV) - supported by EM
   (PMID:8570580) and UniProt note; secondary location of shed/exported surface material ->
   KEEP_AS_NON_CORE. Organelle check: PV is a genuine Toxoplasma compartment; term is
   used correctly for a symbiont protein.

## Proposed NEW

- GO:0044650 adhesion of symbiont to host cell (IMP, PMID:40607979; also PMID:8050521).
- GO:0046812 host cell surface binding (IDA, PMID:15151144).
- Not proposed: immune-modulation/TNF process terms (single-lab, mechanism unclear);
  "protein homodimerization" (crystal-only, no functional relevance shown).
