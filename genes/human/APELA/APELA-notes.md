# APELA (ELABELA / Toddler / ELA) review notes

## Identity
- UniProt P0DMC3 (ELA_HUMAN), 54 aa precursor; signal peptide 1-22; single mature chain
  23-54 (PRO_0000425557) = ELA-32. HGNC:48925. Transcript was originally annotated as
  non-coding (EMBL AK092578 / AC104620 flagged NOT_ANNOTATED_CDS).
- Discovered independently by two groups mining "non-coding" transcripts:
  - Chng et al. 2013 Dev Cell [PMID:24316148 "We report here the discovery and characterization of a gene, ELABELA (ELA), encoding a conserved hormone of 32 amino acids."]
  - Pauli et al. 2014 Science (zebrafish Toddler) [PMID:24407481 "Toddler drives internalization of G protein-coupled APJ/Apelin receptors, and activation of APJ/Apelin signaling rescues toddler mutants."]
- Coding evidence (microprotein project relevance): [PMID:24407481 "Sixth, wild-type but not frameshifted toddler mRNA rescues toddler mutants (see below), providing direct evidence that it is the peptide product rather than the RNA that is functional in vivo."]
  and secretion depends on the signal peptide [PMID:24407481 "Fourth, enhanced green fluorescent protein (eGFP) fusion proteins containing the wild-type signal sequence of Toddler are found extracellularly, whereas signal peptide cleavage site mutants are retained in the cell"].

## Mature peptide forms / functional_isoforms decision
- ELA-32, ELA-21, ELA-11 (and ELA-14 / ELA(19-32)) are all described pharmacologically.
  Only ELA-32 exists in UniProt as a PRO_ chain (PRO_0000425557, 23-54). ELA-21/ELA-11
  have no PRO_ ids, and their activities are qualitatively the same (all APLNR agonists;
  ELA-11 lower affinity/beta-arrestin potency but full Gi agonist):
  [PMID:28137936 "suggesting that a longer sequence with positively charged residues in the N terminus is required for optimal binding affinity"]
  [PMID:28137936 "The potency of ELA-11 was comparable to the longer ELA peptides, indicating that this short sequence retains full biological activity"]
- Decision: no `functional_isoforms` block. Unlike POMC, the cleavage products are not
  functionally distinct (same receptor, same pathways) and are not separately
  represented in UniProt. Raised as a suggested question.

## Molecular function
- Human ELA binds native human APLNR in heart homogenate:
  [PMID:28137936 "ELA competed for binding of apelin in human heart with overlap for the 2 peptides indicated by in silico modeling."]
- Activates Gi (cAMP inhibition), ERK1/2, calcium, and receptor internalization via human APJ:
  [PMID:25639753 "ELA suppresses cAMP production with EC50 of 11.1 nM, stimulates ERK1/2 phosphorylation with EC50 of 14.3 nM and weakly induces intracellular calcium mobilization"]
  [PMID:25639753 "Thus, ELA's effects on intracellular signaling were APJ-dependent."]
  [PMID:28137936 "ELA-mediated inhibition of cAMP production confirmed as pertussis toxin sensitive"]
- Cryo-EM of APLNR-Gi with ELA (residues 23-54): [PMID:35817871 "Protein preparations, in the presence of the endogenous peptide ligand ELA or a synthetic small molecule, both demonstrate these mixed stoichiometric states."] (abstract only).
- Receptor internalization: [PMID:25639753 "Addition of ELA to HEK293 cells over-expressing GFP-AJP fusion protein resulted in rapid internalization of the fusion receptor."]
- ELA(19-32) fragment: [PMID:26986036 "we demonstrate that ELA and 3 both reduce arterial pressure and exert positive inotropic effects on the heart"]

## Hormone / location
- Circulates in human plasma: [PMID:28137936 "ELA and apelin were detectable in healthy human plasma at 0.34"]
- Placental hormone (mouse): [PMID:28663440 "ELABELA (ELA), an endogenous ligand of the apelin receptor (APLNR, or APJ), is a circulating hormone secreted by the placenta."]

## Physiology / development (downstream of APLNR; non-core)
- Zebrafish endoderm/heart: [PMID:24316148 "ela null embryos have impaired endoderm differentiation potential marked by reduced gata5 and sox17 expression."]
- Zebrafish mesendoderm motogen: [PMID:24407481 "Both absence and overproduction of Toddler reduce the movement of mesendodermal cells during zebrafish gastrulation."]
- Mouse knockout: [PMID:28854362 "We found that loss of Apela results in low-penetrance cardiovascular defects that manifest after the onset of circulation."]
- Coronary vasculature (mouse): [PMID:28890073 "Ela-deficient hearts displayed a phenotype identical to that of Apj mutants, indicating that this endogenous peptide is the bona fide ligand that stimulates coronary growth"]
- Preeclampsia (mouse): [PMID:28663440 "Elabela but not Apelin knockout pregnant mice exhibit PE-like symptoms, including proteinuria and elevated blood pressure due to defective placental angiogenesis."]
- Angiogenesis in HUVEC, APJ-dependent: [PMID:25639753 "Together, the results indicate that ELA exerts angiogenic effect directly through activation of APJ."]
- Adult cardiovascular: [PMID:28137936 "Comparable to apelin, ELA increased cardiac contractility, ejection fraction, and cardiac output and elicited vasodilatation in rat in vivo."]
- hESC self-renewal via an APLNR-independent receptor (abstract only):
  [PMID:26387754 "ELA is also abundantly secreted by human embryonic stem cells (hESCs), which do not express APLNR."]
  [PMID:26387754 "We propose that ELA, acting through an alternate cell-surface receptor, is an endogenous secreted growth factor in human embryos and hESCs that promotes"]
  Not annotated as NEW: receptor unidentified and full text not available; recorded as a question.

## Annotation decisions (summary)
- Core: hormone activity (GO:0005179), apelin receptor binding (GO:0031704),
  apelin receptor signaling pathway (GO:0060183), extracellular region.
- NEW: GO:0007193 adenylate cyclase-inhibiting GPCR signaling pathway (IDA-grade data
  in 25639753, 28137936). Comparator: APLN review carries this as core; mouse Apela
  has GO:0007193 by ISO; the APELA GO-CAM (gomodel:671ae02600002587) places GNAI1 in
  GO:0007193 downstream of APELA. Ligand initiates the pathway (does part of the work:
  receptor activation), consistent with APLN convention.
- GO:0007512 adult heart development ISS with UniProtKB:Q9WV08 (mouse Aplnr - the
  receptor, not a homolog). ISS from a non-homologous receptor is not a sequence
  similarity inference; no Apela ortholog has experimental support for this term.
  REMOVE.
- Developmental/physiological process terms: KEEP_AS_NON_CORE.
- GO:0060183 definition says "initiated by apelin binding"; applies to ELA as the
  second APLNR ligand. Definition should arguably be ligand-agnostic (question raised).
