# CG33453 (A1ZBI2, CG33453-PA) review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. This folder holds the canonical PA product (A1ZBI2, FBpp0085748, 175 aa) of FlyBase gene FBgn0053453. The PB product (A0A0B4LFV5, 174 aa) is reviewed separately in `genes/DROME/CG33453/`. The folder name follows the `<HOST>__<ACC>` convention for a second UniProt entry that shares the host symbol.

### Sources

- UniProt A1ZBI2 (unreviewed TrEMBL; PE 4). Usable evidence: SignalP signal peptide 1..23, Pfam PF06477 DUF1091, SMART DM8, PANTHER PTHR20898 and PTHR20898:SF0. The RecName comes from ProtNLM (ECO:0008006) and is not used as evidence.
- Deep research: `just deep-research-falcon DROME A1ZBI2 --alias CG33453__A1ZBI2 --fallback perplexity-lite` failed on 2026-10-21. Falcon raised "Failed to authenticate", and the perplexity-lite fallback returned HTTP 401 (quota exceeded). No deep-research file was written for this folder. I used the gene-level Falcon report already present for the PB accession (`genes/DROME/CG33453/CG33453-deep-research-falcon.md`), which covers the same gene.
- Europe PMC search for `"CG33453" OR "FBgn0053453"` (2026-10-21): 0 hits.
- UniProt REST `xref:panther-PTHR20898 AND reviewed:true`: no entries.
- Cached full text of PMID:32502405, Wilson et al. 2020, on daedalus/CG33690 and decima/CG34351.
- Sibling analysis `genes/DROME/CG33453/CG33453-bioinformatics/RESULTS-rereview.md`. It shows that PA and PB differ by one two-residue indel in the signal peptide (PA 20-21) and one one-residue indel in the mature chain, with no substitutions.

### Evolutionary grounding

- A1ZBI2 is in PTHR20898:SF0, the same subfamily as the PB isoform and as daedalus/CG33690 (Q4ABJ0). PTHR20898 is insect-restricted (about 3,090 UniProt entries, about 2,997 of them dipteran) and has no Swiss-Prot entries. Apart from four Aspergillus entries that were not examined, it has no members outside insects.
- No PAINT/IBA annotation exists anywhere in the family, so there is no curated phylogenetic node to inherit from.
- daedalus is the only experimentally studied SF0 member. It has diet-dependent climbing and activity phenotypes, and no molecular function has been proposed for it [PMID:32502405 "No biological function has been suggested for dls, and the protein it encodes contains a conserved domain of unknown function (InterPro DUF1091)."]. These are organismal phenotypes of a different paralog and are not transferred.
- The CheA/CheB chemosensory hypothesis (Torres-Oliva et al. 2016, GBE, doi:10.1093/gbe/evw108, not cached) rests on family-level expression of other members and on weak profile similarity. It is recorded only as a suggested question and experiment.

### Decisions

- GOA has three ND root rows (MF, CC, BP; GO_REF:0000015, FlyBase). All are ACCEPTed as accurate statements that the function is unknown. This matches the PB review.
- No NEW terms. An extracellular-region CC term would rest only on a SignalP prediction. Chemosensation or locomotion process terms would rest on paralog phenotypes or family expression, and fail the grounding and participation tests.
- core_functions is left empty.
- What is experimentally established for CG33453 in D. melanogaster: nothing beyond the existence of the gene model. Everything else is sequence inference: a predicted signal peptide, DUF1091 domain membership and PANTHER SF0 placement. This should be kept in mind if A1ZBI2 is used as a reference for transfer, because it has no experimental function to transfer.
