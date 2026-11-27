# vclb notes (Danio rerio, vinculin b; UniProt A0A0S2I7K2)

## 2026-09-28 — session log

**Deep research:** FAILED for this gene (Edison/Falcon returned 402 Payment Required; the OpenAI key is
invalid). Not retried, per instructions. No `-deep-research-*.md` file exists; literature research was done
manually (cached publications, Europe PMC). See also `../vcla/vcla-notes.md` for shared pair literature and
`../vcla/vcla-bioinformatics/RESULTS.md` for the protein comparison.

Accession A0A0S2I7K2 (TrEMBL, 1066 aa; EMBL ALO18748 from Cheng & Zhang) = vinculin-type isoform (no
metavinculin insert). ZFIN:ZDB-GENE-131017-1. vclb was unannotated in Zv9 and cloned by Han et al.
[PMID:28767718 "The vclb locus was not annotated formally in the Zv9 zebrafish genome database, but did contain a GENSCAN prediction sequence."]

### Protein
- Y822F: [PMID:28767718 "The one notable difference between zebrafish vinculin A and B is the change of the otherwise conserved Y at position 822 to F in vinculin B."]
- Y822F does not block junction localization in MDCK: [PMID:28767718 "Curiously, the 822F residue in zebrafish vinculin B does not perturb its localization to cell-cell junctions."]
- But Han note endogenous vinculin was present in their cells: [PMID:28767718 "Alternatively, the fact that endogenous vinculin was depleted in experiments performed by Bays et al. but was still present in our cells, may have rescued the junctional localization of Y822F vinculin or zebrafish vinculin B."]
- Confirmed Y822->F at vclb position 822 by my alignment.

### Expression
- Predominant copy in embryonic heart: [PMID:30635353 "A recent report showed that vclb is the predominant vcl gene expressed in the embryonic heart (Cheng et al., 2016)."]
- Epicardium: vcla absent there [PMID:27578788 "By contrast, cardiac muscle development is relatively normal, probably owing to redundancy with Vcla, a vinculin paralog that is expressed in the myocardium but not epicardium."]
- Endothelium: [PMID:36314606 "As vinculinb is most prominently expressed in zebrafish ECs (Lawson et al., 2020), we generated a vascular restricted transgenic line, Tg(fli1ep:vinculinb-eGFP)uq2al, whereby Vinculinb is tagged with eGFP at the C terminus."]
- Broad: [PMID:38697108 "Live-imaging approaches using the TgKI(vclb-mScarlet) proved challenging due to the widespread expression profile of Vinculin in the surrounding tissues, such as the axial musculature and vasculature."]
- Maternal: little [PMID:28767718 "Moreover, the very low expression of vinculin B at day 5 indicates that indeed very little if any vinculin protein is present due to maternal contribution in the early stages of development of the vcla-/-vclb-/- double mutants."]

### Mutants
- Cheng 2016 gene-trap (abstract only): epicardial hyperplasia, coronary defects, juvenile death, FAK/ERK up.
- Han 2017 hu11202 (7-bp del, PTC at 22). Possible downstream M26 start noted by the authors.
- Gunawan 2019 bns247 (16-bp del): no strong valve defect; not surviving to adulthood [PMID:30635353 "However, we found that vclb mutants did not exhibit strong delays in AV EC migration and valve formation"]
- vclb is the adapting gene for vcla PTC alleles (see vcla notes; PMID:30944477, PMID:36427314). No study tested whether vcla is upregulated in vclb mutants.

### Decisions
- Shared IEA/IBA rows handled identically to vcla (same text), except beta-catenin binding IBA -> UNDECIDED
  because of F822 (target-specific residue change at a residue linked to that interaction; untested).
- heart development, coronary vasculature morphogenesis IMP: ACCEPT (copy-specific by expression).
- NEW GO:0061028 establishment of endothelial barrier (IGI, PMID:36260739) on both copies.
