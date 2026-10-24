# ZDHHC23: paired evidence notes

Human reference: https://www.uniprot.org/uniprotkb/Q8IYP9/entry

Primary source: [PMID:22399288 Distinct acyl protein transferases and thioesterases control surface expression of calcium-activated potassium channels.](https://pubmed.ncbi.nlm.nih.gov/22399288/).

> Here, we demonstrate that
> palmitoylation of the intracellular S0-S1 loop of BK channels is controlled by
> two of the 23 mammalian palmitoyl-transferases, zDHHC22 and zDHHC23.
> Palmitoylation by these acyl transferases is essential for efficient cell
> surface expression of BK channels.

The horse sequence comparison is in [ZDHHC23-bioinformatics/RESULTS.md](ZDHHC23-bioinformatics/RESULTS.md). Transfer is assessed for this exact accession; human biochemical evidence is not equine experimental validation.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used for this re-review.

### Deep research
`just deep-research HORSE ZDHHC23 --provider falcon` failed with "Exception: Failed to authenticate" (Edison/falcon JWT authentication). No deep-research file was written. Literature for this section comes from the cached full text of PMID:22399288, the cached abstract of PMID:15105416, and the human ortholog's deep-research file (`genes/human/ZDHHC23/ZDHHC23-deep-research-falcon.md`), which was used only as a source of leads.

### Identity of A0A9L0T4E4 (gene model)
- Horse Ensembl gene ENSECAG00000014382 (chr19) has 7 protein-coding transcripts. A0A9L0T4E4 = ENSECAT00000105517, which is the **Ensembl canonical** transcript. No horse ZDHHC23 entry is Swiss-Prot reviewed. The other horse models are A0A3Q2KPV4 (435 aa), F7CNX6 (417), A0A5F5Q1C7 (410), A0A9L0RVS6 (397), A0A9L0R7E2 (426) and A0A9L0SCZ1 (419). [file:HORSE/ZDHHC23/ZDHHC23-bioinformatics/RESULTS-rereview.md]
- At 448 aa, A0A9L0T4E4 is longer than human Q8IYP9 (409) and rat Q76IC6 (429).
  - It starts at the Met equivalent to human M7. The first 6 residues of human (MTQKGS) are not conserved in rodents either.
  - It keeps the whole DHHC cysteine-rich domain (Pfam 251-380, DHHC 280-283, active-site **C283** = human C289) and all predicted TM segments up to the conserved LCGLIVDT anchor (residue 399).
  - After the anchor, an alternative last exon (exon 5 donor chr19:46759456 spliced to chr19:46755009-46755651) encodes a 49-residue tail (AGADCSPGASAAGPRLHGEWRQICQSLWLFRGGLVTYDWSSLPDCTFHF). That tail **lacks the C-terminal -EDIV PDZ-binding motif**, which is conserved in rat, mouse and three other horse models. In rat the -EDIV motif is the mapped NOS1-interaction region [PMID:15105416 "a PDZ-binding motif (-EDIV) at its C-terminal tail"].
  - The reviewed human canonical (tail GLLG) also lacks -EDIV, so the tail varies even among reviewed orthologs.
- Conclusion: A0A9L0T4E4 is an alternative-3'-exon gene model of horse ZDHHC23 with an intact catalytic and membrane core. S-palmitoyltransferase activity transfers. The NOS1 PDZ interaction does **not** transfer and was not proposed.

### Evolutionary grounding
- PANTHER PTHR22883:SF475 (PALMITOYLTRANSFERASE ZDHHC23) contains human Q8IYP9, mouse Q5Y5T3, rat Q76IC6, zebrafish zdhhc23a/b and the horse models. The PANTHER family review `interpro/panther/PTHR22883/PTHR22883-review.yaml` lists A0A9L0T4E4 and Q8IYP9 as SF475 representatives. **No disagreement on subfamily placement.**
- The IBA for GO:0072659 comes from PTN008583751, a narrow ZDHHC23 ortholog-clade node whose donors are human ZDHHC23 (Q8IYP9) and mouse Zdhhc23 (MGI:2685625). This is a strong ortholog transfer.
- The IBAs for GO:0019706, GO:0005794, GO:0005783 and GO:0006612 come from the DHHC-family root PTN000525256. Their donors span many paralogs (Erf2, rice DHHC9, ZDHHC paralogs).
- PAINT did not propagate GO:0018345 (protein palmitoylation, human IMP) to horse. GO:0018345 is mostly implied by GO:0019706, so no NEW row was added.

### Actions (re-review)
- GO:0000139 Golgi membrane IEA: ACCEPT. Now supported by the direct ZDHHC23 co-localization data (GM130/TGN38) instead of the ARBA-derived horse SubCell line.
- GO:0005783 ER IBA: changed from ACCEPT to **KEEP_AS_NON_CORE**. The term comes from a family-root node whose donors are paralogs, while ZDHHC23 itself is Golgi/TGN-predominant. The ER pool is not refuted.
- GO:0005794 Golgi apparatus IBA: changed from ACCEPT to **MODIFY → GO:0000139 Golgi membrane**, because the term is correct but general and the product already carries Golgi membrane.
- GO:0006612 protein targeting to membrane IBA: changed from ACCEPT to **KEEP_AS_NON_CORE**. It is a family-level term. For ZDHHC23 the substrate (KCNMA1) is already an integral membrane protein, and the characterized effect is TGN exit and surface delivery (GO:0072659).
- GO:0016409 and GO:0016746 IEA: MODIFY → GO:0019706 (unchanged).
- GO:0019706 IBA and IEA: ACCEPT (core).
- GO:0072659 IBA: ACCEPT (core BP).
- Description rewritten. Core function now includes GO:0072659 and the Golgi membrane location. Supporting quotes were changed from the repeated abstract block to specific full-text sentences. The old RESULTS.md is kept as a reference but is no longer cited as support.

### Modules
No module in `modules/` covers ZDHHC23, protein S-palmitoylation or BK-channel trafficking. ZDHHC23 does not appear in `gocams/index.tsv`.

### Relative
The closest characterized relative is human ZDHHC23 (Q8IYP9), a 1:1 ortholog in the same PANTHER subfamily (SF475) and a donor to the PTN008583751 IBA. Its review `genes/human/ZDHHC23/ZDHHC23-ai-review.yaml` is complete (13/13 annotations with actions, core_functions present). Rat Q76IC6 (NIDD) is also characterized (PMID:15105416) but has no review. It is lower priority, because its distinguishing NOS1 interaction depends on a tail this horse model lacks.
