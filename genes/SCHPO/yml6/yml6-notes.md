# yml6: functional evidence

Yml6 is the mitochondrial large-subunit ribosomal protein uL4m. It is a conserved structural component of the mitoribosome that supports mitochondrial translation. The uL4 family contributes to the nascent-polypeptide exit-tunnel constriction, a feature retained in the characterized budding-yeast mitoribosome.

- [file:SCHPO/yml6/yml6-uniprot.txt] "DR   InterPro; IPR002136; Ribosomal_uL4."
- [PMID:24675956] "Beyond the entrance, the tunnel is lined by conserved elements (Fig. 6C), including the constriction site formed by uL22 and uL4."

Evidence interpretation: sequence/domain records are used for family placement; AI descriptions and ARBA labels are not independent validation. Family transfer is limited to conserved properties and is identified as inference. Genome-scale localization annotations are retained where consistent with the biology; an abstract does not expose every individual observation. All original annotation rows are preserved.

ProtNLM provenance: pre-release `post-processed-2026_02_28k.xml`, exact entry and all evidence keys preserved in the source XML/JSON. These current Swiss-Prot entries are absent from the public TrEMBL pilot. Known-function overlap does not establish model training membership. See the function sidecar for atom-by-atom paragraph assessments.

Research provenance: the gene-focused Falcon report was generated concurrently with publication caching. The report was inspected for source leads; the biological decisions above rely on the cited primary records and specified family evidence.

The completed Falcon search has retrieval gaps: its inability to locate target-level localization is not used to override PomBase’s HDA records. Curated genomic-screen observations and the directly inspected papers take precedence over an empty literature-search result.

Target association [PMID:34119521]: "Mass spectrometry (MS) analysis of Ppr10-copurified proteins revealed that some proteins were specifically detected in the Ppr10-TAP preparation, albeit at low levels. These proteins included mt-SSU proteins (Nam9, Mrps28, Mrp4, and Mrps9), mt-LSU proteins (Aco2-Mrpl49, Mrpl7, and Yml6), SPAC750.08c (a putative NAD-dependent malic enzyme), SPBP4H10.18c (a Schizosaccharomyces specific protein of unknown function), and Anc1 (a mitochondrial ADP/ATP carrier)". This is low-level mass-spectrometry copurification, not a selective Yml6 functional perturbation. The full text of correction PMID:35932618 was checked at Europe PMC; it corrects funding information only.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files in this folder were not opened or used.

Identity: benchmark accession O74801 is the canonical, reviewed (Swiss-Prot) product of yml6/SPBC2D10.08c, 261-aa precursor with predicted transit peptide 1-35 (ECO:0000255) and mature chain 36-261 (PRO_0000314628). It is not an isoform, fragment or alternative gene model. It carries the complete Ribosomal_uL4 domain (IPR002136, PF00573).

Evolutionary grounding:
- PANTHER PTHR10746:SF6 (LARGE RIBOSOMAL SUBUNIT PROTEIN UL4M). The same subfamily contains S. cerevisiae Yml6 (P51998) and human MRPL4 (Q9BYD3), per interpro/panther/PTHR10746/PTHR10746-entries.csv. Note that SF6 as catalogued also contains bacterial uL4 (e.g. E. coli rplD P60723, Listeria) and a misassigned Xenopus magainin precursor (P11006). The SF6 label is therefore not mitochondrion-specific. The mitochondrial clade is better defined by PAINT node PTN000078780, whose donors are S. cerevisiae Yml6, human MRPL4 and trypanosome Q385G8. The family review (interpro/panther/PTHR10746/PTHR10746-review.yaml) places Yml6 in SF6, with no disagreement about subfamily placement. It records the P11006 outlier.
- The family-root node PTN000078778 carries structural constituent of ribosome and ribosome, from bacterial, plastid and mitochondrial donors. It also carries regulation of translation, from E. coli L4 (P60723) alone.

Decisions (changes from the previous review):
- GO:0006417 regulation of translation (IBA): UNDECIDED -> MARK_AS_OVER_ANNOTATED. The sole donor is E. coli L4. Its regulatory role is autogenous control of the bacterial S10 operon, which has no counterpart for a nuclear-encoded fungal mitoribosomal protein. No eukaryotic donor at PTN000078780 contributes a regulatory term.
- All other rows keep their previous actions: ACCEPT for structural constituent of ribosome, mitochondrion, mitochondrial large ribosomal subunit and mitochondrial translation; MODIFY ribosome -> GO:0005762; MODIFY translation -> GO:0032543. The supporting quotes were rewritten to cite curated UniProt statements (SUBCELLULAR LOCATION with ECO:0000269 PubMed:16823372; the SUBUNIT/FUNCTION text, ECO:0000250 from P51998; the family note) rather than DR GO lines. The repeated duplicate supporting entries from the earlier file were removed.
- The NAS source PMID:18245278 (Bot1) does not mention Yml6 in its cached full text. It is marked MISCITED in reference_review, and the NAS claims are accepted on independent support.
- PMID:28154081 and PMID:29514071 contain no uL4m-specific text. They are retained as LOW-relevance context and not quoted.

Relative to review next: S. cerevisiae YML6 (P51998, SGD:S000004487), the same-subfamily ortholog and the experimental donor of the IBA/ISS rows. It has no review in the repo (genes/yeast/ has no YML6 folder). Human MRPL4 (Q9BYD3) is also unreviewed.

Modules: none in modules/ reference O74801, P51998 or Q9BYD3.
