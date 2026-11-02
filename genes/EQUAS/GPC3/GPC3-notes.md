# GPC3 (donkey, Equus asinus; UniProt A0A9L0J2B1) - review notes

## Sources used

- Donkey UniProt record (unreviewed, Ensembl ENSEASP00005043430.1), 565 aa: `GPC3-uniprot.txt`.
- Donkey GOA: 8 IEA rows (5 TreeGrafter GO_REF:0000118 from PANTHER:PTN001327382; 2 InterPro2GO GO_REF:0000002 from IPR001863; plasma membrane via GO_REF:0000120).
- Human GPC3 (P51654) UniProt record fetched 2026-10-14: `GPC3-bioinformatics/human-GPC3-P51654-uniprot.txt`.
- Alignment: `GPC3-bioinformatics/RESULTS.md`.
- Cached publications (already present in `publications/`): PMID:24496449 (GPC3 binds Frizzled; abstract only), PMID:14610063 (furin processing of GPC3; full text), PMID:17549790 (GPC3 inhibits CD26/DPP4; abstract only).
- Human QuickGO (2026-10-14) comparator: IDA positive regulation of canonical Wnt signaling (PMID:24496449); IBA extracellular region, plasma membrane, cell surface, cell migration, regulation of protein localization to membrane; ISS negative regulation of smoothened signaling pathway; the extracellular matrix and regulation of signal transduction rows on human GPC3 are InterPro2GO only.

## Sequence

- [RESULTS.md "The donkey GPC3 protein matches human GPC3 at 92.61% identity over 555 paired residues"]
- [RESULTS.md "The furin-like cleavage site (human R358/S359), the two heparan sulfate attachment serines (human S495, S509) and the GPI-anchor asparagine (human N554) are all conserved in the donkey sequence."]

## Function

- GPI-anchored heparan sulfate proteoglycan [human UniProt "Cell membrane {ECO:0000269|PubMed:14610063}; Lipid-anchor, GPI-anchor"].
- Wnt: [PMID:24496449 "GPC3 stimulates HCC growth by promoting canonical Wnt signaling."]; [human UniProt "Positively regulates the canonical Wnt signaling pathway by binding to the Wnt receptor Frizzled"].
- Hedgehog: [human UniProt "Negatively regulates the hedgehog signaling pathway when attached via the GPI-anchor to the cell surface by competing with the hedgehog receptor PTC1 for binding to hedgehog proteins"] (by similarity to mouse).
- Processing: [PMID:14610063 "This processing is essential for GPC3 modulating Wnt"]; cell movements [PMID:14610063 "for supporting embryonic cell movements"].
- Shedding: [human UniProt "leading to its shedding from the cell surface"].

## Review decisions (summary)

- plasma membrane, cell surface, positive regulation of canonical Wnt signaling: ACCEPT.
- extracellular region (shed form), cell migration, regulation of protein localization to membrane: KEEP_AS_NON_CORE.
- regulation of signal transduction: TOO_GENERAL (entailed by positive regulation of canonical Wnt signaling, and by the NEW Hh term).
- extracellular matrix: MARK_AS_OVER_ANNOTATED (GPC3 is GPI-anchored to the cell surface, not an ECM constituent; InterPro2GO family mapping).
- NEW: negative regulation of smoothened signaling pathway (GO:0045879).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Everything below comes from the UniProt/GOA records, PAINT, cached literature and new sequence checks.

### Deep research
- `just deep-research-falcon EQUAS GPC3 --fallback perplexity-lite` failed: falcon returned "Failed to authenticate" and perplexity-lite returned HTTP 401 (insufficient quota). No deep-research file was produced. The review relies on the cached literature listed below.

### Identity of the benchmark accession (gene-model problem)
- A0A9L0J2B1 (565 aa) is an **alternative-first-exon model** of donkey GPC3 (Ensembl transcript ENSEAST00005057340, gene ENSEASG00005018489). Its residues 1-43 (MSFQFAPGGCYGHARVFDCQMVMMMEARMFIFWPRFWKGTPNK) are not homologous to human P51654 1-58, and the human signal peptide (P51654 SIGNAL 1..24) is absent. From donkey 44 / human 59 (GSDLQVCLPK) onward the two are 502/522 identical (96.17%) [file:EQUAS/GPC3/GPC3-bioinformatics/RESULTS-rereview.md "Human signal peptide present verbatim in donkey: False"].
- The 92.61% figure in the earlier `RESULTS.md` includes the non-homologous N-terminus forced into register. The site-conservation conclusions there still hold.
- The canonical donkey GPC3 product is **A0A9L0JGR2** (580 aa, ENSEAST00005069329). It has a human-like signal peptide and is the GPC3 entry in the UniProt one-protein-per-gene reference proteome (UP000694387). The Ensembl canonical transcript ENSEAST00005080949 (A0A9L0J383, 611 aa) has the same signal peptide plus a 31-residue net insertion. Horse A0A3Q2GY79 has the same divergent N-terminus as A0A9L0J2B1.
- Consequence: the secretory-pathway annotations (plasma membrane, cell surface, GPI-anchored HSPG, Frizzled binding via HS chains) describe the canonical product of the gene. They are not established for this transcript model as such. I kept the gene-level actions and recorded the caveat in the review rows and in a suggested question.

### Evolutionary grounding (PAINT, PTHR10822)
- Donkey, human (P51654) and mouse (Q8CFZ4) GPC3 are all in PTHR10822:SF4 (GLYPICAN-3).
- PAINT IBDs in `interpro/panther/PTHR10822/PTHR10822-paint.tsv` that cover the GPC3 lineage: positive regulation of canonical Wnt (PTN000850517, Bilateria; seeds dally + human GPC3); cell surface, extracellular region, cell migration, regulation of protein localization to membrane (PTN002247069, Eumetazoa); plasma membrane (PTN002585559, Euteleostomi; seeds mouse Gpc3, rat Gpc3, human GPC3). These match the donkey TreeGrafter rows exactly.
- Not inherited by the GPC3 lineage: extracellular matrix and synapse (PTN000088172), FGF binding / negative regulation of FGFR signaling (PTN002585522, seed mouse Gpc1), and the synaptic terms at PTN000088293. Human GPC3 has no IBA for these. This supports MARK_AS_OVER_ANNOTATED for the InterPro2GO extracellular matrix row.
- No PAINT node carries any hedgehog term. Mouse Gpc3's hedgehog annotations are IMP/IGI acts_upstream_of_or_within [PMID:18477453; PMID:19590577] plus an IPI with Shh. I read the omission as a deliberate decision not to make this a family-wide (all-glypican) function. Following that decision, the hedgehog NEW terms are transferred only within the GPC3 subfamily (ISS from mouse, as the human GPC3 ISS rows already do), not from glypicans in general.
- No PANTHER family review (`PTHR10822-review.yaml`) exists, so there is no subfamily-placement disagreement to report.

### Literature used (cached)
- PMID:18477453 (abstract only): [PMID:18477453 "GPC3 interacts with high affinity with Hedgehog but not with its receptor, Patched, and that GPC3 competes with Patched for Hedgehog binding"]; [PMID:18477453 "GPC3 induces Hedgehog endocytosis and degradation"]. Newly cached and cited.
- PMID:19590577 (abstract): Gpc3-null overgrowth is partly Ihh-dependent. Newly cached and cited.
- PMID:24496449 (abstract): [PMID:24496449 "GPC3 and Frizzled interact directly through the glycosaminoglycan chains of GPC3"].
- PMID:14610063 (full text): convertase processing; zebrafish morphant gastrulation defects; and [PMID:14610063 "increasing the amount of wild-type GPC3 repressed Wnt1-mediated pTOPFLASH activation in a dose-dependent manner"]. The sign of the canonical Wnt effect is therefore context-dependent.

### Changes to the review
- Description: rewritten to state the gene-model identity (alternative first exon, no signal peptide, canonical = A0A9L0JGR2).
- Existing rows: actions unchanged (plasma membrane, cell surface and positive regulation of canonical Wnt ACCEPT; extracellular region, cell migration and regulation of protein localization to membrane KEEP_AS_NON_CORE; regulation of signal transduction TOO_GENERAL; extracellular matrix MARK_AS_OVER_ANNOTATED). Reasons now cite the PAINT node placements. The cell-migration row explicitly does not use the zebrafish morphant phenotype as proof of participation.
- NEW rows: frizzled binding changed from IDA to **ISS** (the experiment is on human GPC3). The negative regulation of smoothened signaling and hedgehog family protein binding rows are re-sourced to PMID:18477453 (mouse, same subfamily) as ISS.
- Not added: peptidyl-dipeptidase inhibitor activity (human IDA, PMID:17549790, DPP4/CD26). It is a single study in a cancer-cell context, not part of the core signaling roles.
- New analysis files: `GPC3-bioinformatics/compare_nterm_rereview.py`, `nterm_rereview_output.txt`, `RESULTS-rereview.md`. Existing bioinformatics files are untouched.

### Relative to review next
- Same-gene canonical product: donkey **GPC3 A0A9L0JGR2** (folder would be `genes/EQUAS/GPC3__A0A9L0JGR2`). It has no review yet.
