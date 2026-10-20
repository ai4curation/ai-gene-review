# EYA1 (Q99502) curation notes

Automated deep research was not available for this session (falcon 402, OpenAI 401); these notes
are from cached publications, the UniProt record and targeted web searches.

## Identity and domains
- Eyes absent homolog 1; N-terminal proline/serine/threonine-rich transactivation region and a
  conserved ~270 aa C-terminal Eya domain (ED) that belongs to the HAD phosphatase superfamily.
  [PMID:19497856 "There are four mammalian members ( EYA1–4 ), each containing an N-terminal transactivation domain ( 5 ), and a highly conserved ∼270-amino acid C-terminal Eya domain (ED), also referred to as the eya homologous region."]
- Family-level: Eya is a non-thiol HAD protein tyrosine phosphatase (Drosophila eya)
  [PMID:14628053 "propose a function for it as a non-thiol-based protein tyrosine phosphatase"].

## Transcriptional coactivator for SIX proteins
- EYA has no DNA-binding domain; SIX supplies DNA binding, EYA transactivation
  [PMID:19497856 "As a complex, the SIX and EYA proteins are believed to form a bipartite transcription factor where SIX confers DNA binding and EYA confers transactivation activity."].
- Six2/4/5 translocate Eya1 into the nucleus; synergistic activation of myogenin promoter
  [PMID:10490620 "Coexpression of Six2, Six4, or Six5 induced nuclear translocation of Eya1, Eya2, and Eya3, which were otherwise distributed in the cytoplasm."].
- Human EYA1 is cytoplasmic without SIX1 and nuclear with SIX1; SIX1 V17E BOR mutant fails
  [PMID:19497856 "we observed that in the absence of SIX1, EYA1 was localized in the cytoplasm"].
- Eya phosphatase switches Six1-Dach from repression to activation
  [PMID:14628042 "The phosphatase function of Eya switches the function of Six1-Dach from repression to activation, causing transcriptional activation through recruitment of co-activators."].
- SUMO1 modification of EYA1 inhibits its transcriptional activity; Akt phosphorylation reduces it
  [PMID:24954506 "SUMOylation inhibits Eya1 transcription activity"]. EYA1 is the substrate, so
  "protein sumoylation" (ISS) is a substrate-type annotation, not participation.

## Protein tyrosine phosphatase / H2AX pY142
- Cook et al. 2009: HA-Eya1 dephosphorylates H2AX pY142 in vitro; D323A dead mutant inactive;
  Eya1 siRNA increases pY142 after IR; rescue requires catalytic activity
  [PMID:19234442 "Wild-type Eya effectively removed the phosphotyrosine mark from H2AX, while the phosphatase-inactive mutant Eya proteins (Eya1 D323A or Eya3 D246A) had little or no effect"].
- Ser/Thr activity: the same paper reports minimal activity toward a pSer H2AX peptide (Eya3 ED) and
  says Eya primarily acts as a tyrosine phosphatase in vivo
  [PMID:19234442 "subsequent data has indicated that, in-vivo, Eya primarily functions as a tyrosine phosphatase"].
  Ser/Thr phosphatase annotations (EXP + IEA) therefore look like over-annotation for EYA1.
- Krishnan et al. 2009 showed EYA2/EYA3 (not EYA1) specificity for H2AX Y142 [PMID:19351884].
- BOR missense mutations abolish EYA1 phosphatase activity whereas ocular-defect mutations do not
  [PMID:16797546 "BOR-associated mutations lead to a loss of phosphatase activity in Eya1 proteins, while mutations associated with ocular defects yield Eya1 proteins with near normal levels of phosphatase activity."].

## Organ development
- Mouse Eya1-/- lack ears and kidneys; Six but not Pax expression depends on Eya1
  [PMID:10471511 "Eya1 homozygotes lack ears and kidneys due to defective inductive tissue interactions and apoptotic regression of the organ primordia."].
- Human: BOR syndrome (branchial, ear, kidney), usually no eye anomalies; rare EYA1 missense variants
  in congenital cataract / anterior segment anomalies
  [PMID:10655545 "with usually no anomalies in the eye"].

## Relevance to retinal determination network module
- EYA1 is the human ortholog used as representative of the Eya node. Molecular functions
  (coactivator, PTP) are conserved, but mammalian EYA1's organ roles are ear/kidney/branchial/muscle;
  eye involvement is minor (cataract/anterior segment), not retinal specification. A family-level
  annoton is fine, but the "eye development" process should be grounded on fly eya, not EYA1.
