# NUMB (donkey, Equus asinus) - A0A9L0IQ95

DONKEY40 cohort review. Unreviewed TrEMBL entry, 506 aa, "Protein numb homolog".

## Sources
- Donkey UniProt record `NUMB-uniprot.txt` (PIRNR017607 function/location; PTB domain 37-173).
- Donkey GOA `NUMB-goa.tsv`: 5 IEA rows (3 TreeGrafter GO_REF:0000118, 1 SubCell GO_REF:0000044, 1 combined GO_REF:0000120). No experimental rows.
- Human ortholog P49757 UniProt record fetched to `NUMB-bioinformatics/human-P49757-uniprot.txt`. No human or mouse NUMB review exists in the repository.
- Cached publication PMID:18657069 (AAK1 regulates Numb in clathrin-mediated endocytosis; human cells).

## Sequence
- 97.03% identity to human NUMB over 505 aligned residues; exon structure matches human isoform 5 (P49757-5): retains PTB insert (human 68-78), lacks human 219-316 and 366-413 [file:EQUAS/NUMB/NUMB-bioinformatics/RESULTS.md "Its exon structure matches human isoform 5 (P49757-5, 505 aa)"].

## Biology (from human/mouse)
- Endocytic protein regulating clathrin-mediated receptor endocytosis [human UniProt "Regulates clathrin-mediated receptor endocytosis"; PMID:18657069 "Numb is an endocytic protein that is proposed to influence clathrin-coated pit assembly"].
- T102A mutant disrupts transferrin and LDL internalization [PMID:18657069 "potently disrupts transferrin and low-density lipoprotein internalization"].
- Localizes to plasma membrane (peripheral, cytoplasmic side) and endosome membrane [human UniProt SUBCELLULAR LOCATION].
- Neurogenesis: maintains radial glial progenitors (mouse genetics) [human UniProt "Plays a role in the process of neurogenesis"].
- Notch antagonism is classical literature for Numb, but neither human nor mouse GOA carries a Notch-pathway term; not proposed as NEW (comparator/convention check).

## Decisions
- cytoplasm, plasma membrane, basolateral PM, cytoplasmic vesicle: ACCEPT (consistent with human/mouse localization data and the PAINT node).
- positive regulation of neurogenesis: KEEP_AS_NON_CORE (developmental outcome; mouse genetics).
- NEW: regulation of clathrin-dependent endocytosis (GO:2000369), from the human endocytosis data.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Deep research: `just deep-research-falcon EQUAS NUMB --fallback perplexity-lite` failed (falcon "Failed to authenticate"; perplexity-lite HTTP 401 insufficient quota); no deep-research file was produced. The review relies on cached publications and UniProt.

### Identity / gene model
- A0A9L0IQ95 (506 aa) is NOT the canonical donkey NUMB product. The donkey gene ENSEASG00005004756 has six TrEMBL entries; UniProt's gene-centric canonical is A0A9L0IHZ0 (652 aa, counterpart of human canonical P49757-1, 651 aa) [file:EQUAS/NUMB/NUMB-bioinformatics/RESULTS-rereview.md "The UniProt gene-centric canonical protein for this gene is A0A9L0IHZ0 (652 aa)"].
- A0A9L0IQ95 is an alternative isoform (human isoform-5-like): it lacks the region equivalent to human 219-316 and the proline-rich-region insert (human 366-413), 146 residues shorter than the canonical. It retains the full PTB domain (37-173), the Thr-102 AAK1 site, and C-terminal DPF (246, 469) / NPF (492) motifs [file:EQUAS/NUMB/NUMB-bioinformatics/RESULTS-rereview.md "It retains the complete PTB (PID) domain, the threonine equivalent to human Thr-102"]. Not a fragment; no catalytic residues apply (adaptor).

### Evolutionary grounding
- PANTHER PTHR47368:SF5 (PROTEIN NUMB HOMOLOG), same subfamily as human P49757, rat Q2LC84, mouse Q9QZS3 (interpro/panther/PTHR47368/PTHR47368-entries.csv). NUMBL is SF4; Drosophila numb and C. elegans num-1 are SF2, so fly-specific Notch/asymmetric-division terms are not transferred. No PTHR47368 family review exists under interpro/panther/ (only metadata/entries), so no placement disagreement to report.
- PAINT node PTN000132844 (seeded by mouse Numb, MGI:107423) carries cytoplasm, basolateral PM, cytoplasmic vesicle (is_active_in) and positive regulation of neurogenesis. It did NOT propagate the mouse/human experimental clathrin-coated pit, early endosome, endosome membrane, receptor-internalization terms (checked via QuickGO for P49757 and Q9QZS3, 2026-10-21). Treated as deliberate; the NEW endocytosis row is justified as a direct 1:1 ortholog ISS transfer from human experimental data, with this omission stated in its reason, and raised as a suggested question.
- Re-confirmed: neither human nor mouse NUMB carries any Notch-pathway GO term in QuickGO; no Notch NEW proposed.

### Decisions (changed vs previous)
- All 5 GOA rows: same actions as before (4 ACCEPT, neurogenesis KEEP_AS_NON_CORE), with strengthened support: mouse papers PMID:17589506 [basolateral cadherin insertion; "localizes to adherens junction-associated vesicles"] and PMID:12410312 ["play redundant but critical roles in maintaining neural progenitor cells during embryogenesis"] cached and cited; PMID:17174898 cached for postnatal SVZ.
- NEW GO:2000369 retained, reason expanded (participation, subfamily, motif conservation, PAINT omission).
- Description rewritten to mention isoform status, DPF/NPF motifs and adherens-junction role.

### Relative to review next
- same_gene_canonical: donkey NUMB canonical A0A9L0IHZ0 (652 aa), no review exists; folder would be genes/EQUAS/NUMB__A0A9L0IHZ0. The best experimentally characterised ortholog in-subfamily is human NUMB P49757 (no review in repo either; mouse Numb Q9QZS3 also unreviewed).
- Modules: modules/intestinal_sterol_absorption_and_efflux.yaml names NUMB as an endocytic partner of NPC1L1 (line 42, context text); no module models NUMB as a part. No module created.
