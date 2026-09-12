# K9IWC0 Research Notes

## Key findings
- UniProt names this protein Natriuretic peptides B [file:DESRO/K9IWC0/K9IWC0-uniprot.txt "RecName: Full=Natriuretic peptides B"].
- UniProt indicates the protein is secreted [file:DESRO/K9IWC0/K9IWC0-uniprot.txt "SUBCELLULAR LOCATION: Secreted"].
- Deep research confirms K9IWC0 as a natriuretic peptide B precursor [file:DESRO/K9IWC0/K9IWC0-deep-research-falcon.md "UniProt K9IWC0 corresponds to a natriuretic peptide B precursor (BNP prohormone)"].
- UniProt assigns this protein to the natriuretic peptide family [file:DESRO/K9IWC0/K9IWC0-uniprot.txt "Belongs to the natriuretic peptide family."].

## 2026-07-31 compliance review

**This is NPPC (CNP), not NPPB (BNP). The UniProt name is a paralogue
misassignment.** Three independent lines say so, and they were all sitting in
plain view:

1. **Internal contradiction in the UniProt record itself.** The ARBA-derived
   name is [file:DESRO/K9IWC0/K9IWC0-uniprot.txt "RecName: Full=Natriuretic
   peptides B"], but the PANTHER subfamily in the same record is
   [file:DESRO/K9IWC0/K9IWC0-uniprot.txt "PANTHER; PTHR12167:SF2; C-TYPE
   NATRIURETIC PEPTIDE; 1."].
2. **The source publication names it CNP.** The EMBL record behind this
   accession (JAA44981.1, TISSUE=Salivary gland) comes from the Vampirome study,
   now cached as PMID:23411029, which has a section headed "C-type natriuretic
   peptide (CNP)" and states [PMID:23411029 "The bat PS SGs express high
   transcriptional levels of CNP (Table 4)."].
3. **Sequence.** Ran a reproducible check in `K9IWC0-bioinformatics/`
   (`classify_natriuretic_peptide.py`; sequences fetched from the UniProt REST
   API at run time, alignment by Biopython, nothing hardcoded):
   72.3% identity to human NPPC vs 31.9% to *each* of NPPB and NPPA, and the
   precursor terminates exactly at the second ring cysteine — the CNP-diagnostic
   pattern, since NPPA and NPPB precursors carry 5 and 6 trailing residues
   respectively. Mature ring `CFGQKLDRIGALSGLGC` vs human CNP
   `CFGLKLDRIGSMSGLGC`: 3 differences out of 17. Against the BNP ring: 8 of 17.

**Why it matters for annotation.** BNP signals through NPR1/GC-A; CNP signals
through NPR2/GC-B. The UniProt FUNCTION sentence [file:DESRO/K9IWC0/K9IWC0-uniprot.txt
"Acts by specifically binding and stimulating NPR1 to"] is therefore BNP biology
attached to the wrong protein, and any NPR1-specific inference drawn from it
would be wrong. The Vampirome paper gets it right: [PMID:23411029 "CNP interacts
with two subtypes of natriuretic peptide receptor, namely NPR-B and NPR-C."].
Recorded as a `CURATION` knowledge gap to be reported upstream to UniProt.

The deep-research file inherited the error wholesale — it opens with
[file:DESRO/K9IWC0/K9IWC0-deep-research-falcon.md "UniProt K9IWC0 corresponds to
a natriuretic peptide B precursor (BNP prohormone) annotated in Desmodus
rotundus (vampire bat)"] and then spends most of its length on human NT-proBNP
heart-failure diagnostic thresholds, NPR1 agonist antibodies, and AF-adjusted
cut-offs — none of which has anything to do with a salivary vasodilator peptide.
Marked `relevance: LOW`.

**Annotation change.** `GO:0097746 blood vessel diameter maintenance` had been
marked over-annotated. It is direction-neutral (covers constriction and
dilation), and the direction is known: [PMID:23411029 "The function of bat CNP
is related to vasodilation."]. Changed to MODIFY → `GO:0042311 vasodilation`
(verified via OLS as a direct child of GO:0097746). The other four annotations
were sound; `GO:0006182` and `GO:0007168` are ACCEPTed with the receptor
identity corrected in the summary, since neither GO term names a receptor.
