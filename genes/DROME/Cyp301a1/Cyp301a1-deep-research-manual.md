# Cyp301a1 (Drosophila melanogaster) - manual literature research

No deep-research API was available; this summary was compiled manually from the cached
publication (publications/PMID_22574182.md, full text from PMC3344891), the UniProt record
(Q9V6D6, CP301_DROME) and a PubMed search ("Cyp301a1 OR CYP301A1 OR CYP301", 8 hits,
2026-10-28).

## Identity
- UniProt Q9V6D6 (Swiss-Prot, 553 aa), "Probable cytochrome P450 301a1, mitochondrial";
  FlyBase FBgn0033753; CG8587; GeneID 36378.
- Family: cytochrome P450, insect mitochondrial clan (InterPro IPR050479 CYP11_CYP27_families;
  PANTHER PTHR24279). UniProt predicts an N-terminal mitochondrial transit peptide
  (ECO:0000255) and assigns "Mitochondrion membrane" by curator inference (ECO:0000305).
- Heme-binding (axial) Cys502 by similarity; the heme-binding motif reads PYGYGARMCLG in the
  displayed sequence (Tyr instead of the usual Phe at the second position).

## Literature
### Sztal et al. 2012, PLoS One (PMID:22574182) - the only functional study in Drosophila
- Conservation: "A single Cyp301a1 ortholog was found in each genome of the 12 Drosophila species
  with available sequence [30], as well as in representative genomes from sequenced insect orders"
  [PMID:22574182].
- Heme motif: "Cyp301A1 in all insect species analysed has a Tyr (Y) instead of the highly conserved
  Phe (F) present in the second position of the heme-binding domain (PFxxGxxxCxG)" [PMID:22574182].
  The authors note such changes are "characteristic for P450s that act as atypical monooxygenases"
  (e.g. allene oxide synthase, thromboxane synthase) [PMID:22574182].
- Expression: RT-PCR at all stages; in situ in embryonic hindgut and epidermis, larval/pupal/adult
  hindgut; RT-PCR detection in adult integument [PMID:22574182].
- Phenotype: piggyBac insertion Cyp301a1[f02301] (alters the last 5 residues, mRNA unchanged) and
  ubiquitous RNAi (three independent lines, 70-90% knockdown) both give a partially penetrant
  dorsal-midline adult abdominal cuticle defect, "ranging from a slight malformation of the cuticle
  between the tergites to a complete loss of the tanned cuticle layer down the dorsal midline of the
  abdomen" [PMID:22574182]. Precise excision of the insertion reverts the phenotype.
- Histology: central region lacks cells and chitin ("Calcofluor staining shows that chitin is not
  secreted in these areas") and lacks sensory bristles; authors suggest failure of histoblast
  migration / larval epidermal cell replacement [PMID:22574182].
- 20E feeding of third-instar larvae partially suppresses the phenotype; the authors explicitly state
  "we cannot conclude that CYP301A1 is directly involved in 20E regulation" [PMID:22574182].
- No biochemical substrate, product, or subcellular localization was determined.

### Other organisms (expression-only; not used for annotation)
- Calanus finmarchicus (copepod): CYP301A1 expression higher in males and post-spawning females,
  speculated role in ecdysteroid degradation (PMID:18586244, abstract).
- Induction/up-regulation of CYP301A1 orthologs after insecticide or nicotine exposure in honeybee
  (PMID:26790026), Plutella xylostella (PMID:29463402), Aphis gossypii (PMID:32980055),
  Liriomyza trifolii (temperature, PMID:33965778), Spodoptera frugiperda (PMID:41159929),
  Orius nagaii (PMID:41461426). These are transcriptional correlations only; none shows
  CYP301A1-catalysed metabolism.

## Synthesis
Cyp301a1 is a conserved, single-copy insect mitochondrial-clan P450 of unknown substrate. Its only
functional evidence is a loss-of-function adult abdominal cuticle/tergite closure phenotype that is
partially suppressed by 20E. Catalytic activity is inferred from family membership only, and the
conserved Tyr in the heme-binding motif leaves open an atypical (non-monooxygenase) P450 chemistry.
