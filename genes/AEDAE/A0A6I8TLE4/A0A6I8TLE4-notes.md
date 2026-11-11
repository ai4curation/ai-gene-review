# A0A6I8TLE4 notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 files or prediction-evidence folders were opened or used.

### Identity

- A0A6I8TLE4 = AAEL019982-PE (transcript RE), 1442 aa, gene AAEL019982 / NCBI Gene 5579847, TrEMBL, PE 4.
- The gene has five UniProt products, all unreviewed: A0A6I8TXX4 (1609 aa), A0A6I8TX88 (1431), A0A6I8TX83 (1381), A0A6I8TXT3 (1376) and A0A6I8TLE4 (1442). There is no Swiss-Prot canonical entry.
- MAFFT comparison (`A0A6I8TLE4-bioinformatics/compare_isoforms_rereview.py`) shows all differences lie in the first ~130 residues; the SynGAP-like PH core (157-267), C2 (259-378), RasGAP (391-735) and DAB2P_C (1357-1421) regions are shared. A0A6I8TLE4 is an alternative splice product with the full domain set, not a fragment, and lacks no catalytic residue [file:AEDAE/A0A6I8TLE4/A0A6I8TLE4-bioinformatics/RESULTS-rereview.md].

### Evolutionary placement

- PANTHER PTHR10194:SF60 (RAS GTPASE-ACTIVATING PROTEIN RASKOL). SF60 members in the local entry list: Drosophila raskol Q8T498, C. elegans gap-2 Q8MLZ5, yeast BUD2 P33314, C. albicans BUD2, Dictyostelium ngap.
- Identity to raskol 61.2%; to gap-2 34%; to human DAB2IP (SF26), RASAL2 (SF52) and SYNGAP1 (SF25) 31-34%; to BUD2 20%. Raskol is the dipteran ortholog. SF60 is heterogeneous, with fungal members no closer than the human paralog subfamilies, so BUD2's Rsr1 substrate is not transferred.
- Arginine finger conserved: R483 in TFRGNS, identical to raskol and aligned with p120GAP R789 / NF1 R1276.
- PAINT (interpro/panther/PTHR10194/PTHR10194-paint.tsv): root node PTN008939999 carries GO:0005096 and GO:1902531 IBD. No subfamily-level node; GO:0046580 was not propagated even though seed DAB2IP has it by IMP (PMID:20154697 per QuickGO). Treated as deliberate.
- QuickGO: raskol, gap-2 and BUD2 all carry GO:0005096 and GO:1902531 by IBA. GOA has no rows for A0A6I8TLE4 (GOA file is header-only), probably because the protein is not in a PANTHER/PAINT reference proteome.

### Literature on relatives

- Raskol (CG42684): [PMID:30763317 "In Drosophila stage 8 embryos, before BCs have delaminated, Raskol localized to the cell membrane of BCs and PCs and was enriched at the PC apical membrane"]; it colocalises with DE-cad and regulates border-cell adhesion and actin protrusions. GAP activity is inferred, not measured. The adhesion and border-cell migration phenotypes are RNAi phenotypes in fly and were not transferred.
- gap-2: [PMID:9619631 "GAP-2 appears to function as a negative regulator of LET-60 Ras during larval development"].
- BUD2: [PMID:8371782 "Bud2p purified from yeast stimulates GTP hydrolysis by Bud1p"].

### Deep research

The falcon report retrieved no contexts and is ungrounded; it misreads IPR039360 (the PANTHER RasGAP family entry) as a Ras GTPase switch domain and invokes intersectins. Marked LOW_QUALITY and not used as support.

### Changes to the review

- GOA has no annotations; all rows are proposals (NEW).
- Kept GO:0005096 GTPase activator activity (core). original_reference_id changed from GO_REF:0000002 (InterPro2GO, which produced no GOA row) to the re-review bioinformatics file.
- Withdrew GO:0007265 Ras protein signal transduction (a GAP regulates the cassette rather than relaying the signal, and the substrate is unknown) and GO:0046580 negative regulation of Ras protein signal transduction (PAINT deliberately propagated only the general term; substrate unknown for this branch). Replaced by GO:1902531 regulation of intracellular signal transduction, matching the PAINT root node. GO:0046580 is raised as a suggested question.
- Withdrew GO:0005829 cytosol (no supporting evidence; the ortholog is at the membrane and cortex).
- Kept GO:0005886 plasma membrane, now supported by the raskol localisation (ISS from PMID:30763317).
- Rewrote the description and core function; added references PMID:30763317, PMID:9619631, PMID:8371782, the UniProt file and RESULTS-rereview.md. Existing references retained with review notes.

### Relative to review next

Drosophila raskol (Q8T498, SF60 ortholog). No review in the repo (searched genes/*/*/ for raskol, CG42684 and Q8T498).
Modules: `modules/erk_cascade.yaml` references the PTHR10194 PAINT node PTN008939999 (generic RasGAP family descriptor); no module names this gene.
