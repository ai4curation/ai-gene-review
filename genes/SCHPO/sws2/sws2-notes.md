# sws2: functional evidence

Sws2 is the mitochondrial small-subunit ribosomal protein uS13m. Its conserved uS13 RNA-binding fold and mitochondrial localization support a structural role in the mitoribosome and mitochondrial protein synthesis. Detailed bacterial intersubunit contacts cannot be assumed for this mitochondrial protein.

- [file:SCHPO/sws2/sws2-uniprot.txt] "DR   InterPro; IPR001892; Ribosomal_uS13."
- [PMID:28154081] "The mitoribosomal
small subunit has been built de novo and includes 15S ribosomal RNA (rRNA) and
34 proteins, including 14 without homologs in the evolutionarily related
bacterial ribosome."

Evidence interpretation: sequence/domain records are used for family placement; AI descriptions and ARBA labels are not independent validation. Family transfer is limited to conserved properties and is identified as inference. Genome-scale localization annotations are retained where consistent with the biology; an abstract does not expose every individual observation. All original annotation rows are preserved.

ProtNLM provenance: pre-release `post-processed-2026_02_28k.xml`, exact entry and all evidence keys preserved in the source XML/JSON. These current Swiss-Prot entries are absent from the public TrEMBL pilot. Known-function overlap does not establish model training membership. See the function sidecar for atom-by-atom paragraph assessments.

Research provenance: the gene-focused Falcon report was generated concurrently with publication caching. The report was inspected for source leads; the biological decisions above rely on the cited primary records and specified family evidence.

The completed Falcon search has retrieval gaps: its inability to locate target-level localization is not used to override PomBase’s HDA records. Curated genomic-screen observations and the directly inspected papers take precedence over an empty literature-search result.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Identity: O59772 is the reviewed, canonical, full-length S. pombe Sws2 entry (151 aa; SPCC1795.07). It is not a fragment, isoform or alternative gene model. It carries the complete uS13 domain set (IPR001892, IPR010979 H2TH, IPR027437 C-terminal, IPR018269 signature).

Evolutionary grounding:
- PANTHER PTHR10871:SF1 "SMALL RIBOSOMAL SUBUNIT PROTEIN US13M" contains S. pombe sws2, S. cerevisiae SWS2 (P53937), N. crassa uS13m (Q7S2C2) and bacterial rpsM proteins, i.e. the bacterial-derived lineage [file:interpro/panther/PTHR10871/PTHR10871-entries.csv "sws2,151,PTHR10871:SF1,SMALL RIBOSOMAL SUBUNIT PROTEIN US13M"]. Cytosolic uS13 (human RPS18 P62269) is in a different subfamily (SF42), so cytosolic-specific properties are not transferred.
- PAINT: structural constituent of ribosome and small ribosomal subunit are placed at the family root PTN000093238; mitochondrion is placed at PTN000093341 (eukaryotic uS13m node), which also carries NOT cytosol (IRD) — a deliberate curator block of the root cytosol propagation [file:interpro/panther/PTHR10871/PTHR10871-paint.tsv "AGI_LocusCode:AT1G77750|SGD:S000005025|UniProtKB:Q7S2C2"]. Sws2 carries no cytosol annotation, consistent with this.
- S. cerevisiae Sws2 is modelled as uS13m (chain MM) in the yeast mitoribosome [PMID:28154081 supplement "uS13m!     Sws2!         P53937!"], with bridge contacts mB8 (mL46), mB9 (uL5), mB10 and mB13 (21S rRNA H62) [supplement table S3 "mB13!      uS13m:!34,!37B38,!41!"].

Decisions changed vs previous version:
- nucleic acid binding and RNA binding (IEA): both MODIFY -> rRNA binding (GO:0019843), based on the ortholog's rRNA H62 contact; previously RNA binding was ACCEPT and nucleic acid binding MODIFY to RNA binding.
- small ribosomal subunit IBA: MODIFY -> mitochondrial small ribosomal subunit, with propagation_review (GRANULARITY_MISMATCH; source node supports transfer).
- Reasons rewritten per row (previously boilerplate); supporting quotes switched from restating DR lines to curated UniProt SIMILARITY / experimental SUBCELLULAR LOCATION text, PANTHER membership and the structure supplement.
- PMID:18245278 (Bot1p) cached full text does not name sws2; NAS rows ACCEPTed in deference to PomBase, the claims being independently supported.
- Added second core function (rRNA binding).

No S. pombe sws2 mutant phenotype or direct structural data was found; the Falcon report likewise found none.

Relative: S. cerevisiae SWS2 (P53937, SGD:S000005025), same PANTHER subfamily SF1 and PAINT node PTN000093341; no review in the repo (genes/yeast/SWS2 absent). The PTHR10871 family review places Sws2 in SF1 as here; no disagreement on subfamily placement. No module in modules/ covers the fungal mitoribosome (only dmel_mitochondrial_ribosome).
