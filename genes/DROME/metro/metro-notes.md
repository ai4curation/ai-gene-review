# metro / A1Z8G0

The exact selected A1Z8G0 is Metro isoform A (595 residues), with two L27 domains, PDZ, SH3, and a guanylate-kinase-like domain. [PMID:20427642](https://pubmed.ncbi.nlm.nih.gov/20427642/) directly identifies junctional localization and L27-dependent DlgS97/DLin-7 complex organization: “Metro stabilizes junctional DlgS97 in a complex with the highly conserved adaptor protein DLin-7.” These findings validate the broad cell-junction prediction (LSP relative to cell-cell junction). The standard cache is abstract-only. The author-institution full PDF was retrieved from https://publications.mpi-cbg.de/Bachmann_2010_4293.pdf and retained with unmodified pdftotext extraction in metro-publication-artifacts. Figure2G explicitly places Metro in the SSR, so the gene-level IDA is accepted. The paper reports Metro-B556aa as the predominant muscle form; the selected A595aa retains the same named scaffold domains. The [reproducible target-specific analysis](metro-bioinformatics/RESULTS.md) identifies Pro422/His488 at conserved GMP-pocket sites and a remodeled ATP loop, with two independent alignments and active-enzyme/MAGUK controls. Primary mutagenesis and MPP-family structural work support an enzyme-to-scaffold transition. Consequently the electronic kinase and transferase annotations are removed; nucleotide/ATP binding remain separate unresolved questions. No generic MAGUK domain is counted as proof of kinase activity.

## Sequence and research provenance

The selected frozen UniProt record is retained in [metro-uniprot-source.json](metro-uniprot-source.json), with the complete original prediction metadata in [metro-predictions-source.json](metro-predictions-source.json). It maps the exact accession to this FlyBase gene; current sequence identity does not establish the historical predictor input. Gene-level experiments support conserved functions unless a relevant isoform difference is established. Falcon research was requested with perplexity-lite fallback alongside publication caching. Primary publications and sequence observations, rather than AI summaries or ARBA assertions, support the curated conclusions.

Falcon report read: it correctly identifies the scaffold complex, the experimentally predominant Metro-B isoform and SSR localization. Its lack-of-catalysis caveat is retained as a knowledge gap; no bare report verdict is used to prove catalytic inactivity.

The catalytic inference uses primary comparator studies [PMID:12482754](https://pubmed.ncbi.nlm.nih.gov/12482754/) and [PMID:22117215](https://pubmed.ncbi.nlm.nih.gov/22117215/), with exact Metro residue observations. It does not require a separate Metro enzyme assay to recognize the established family transition, and does not assert absence of all residual chemistry.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Identity.** A1Z8G0 is Metro isoform A (595 aa, unreviewed UniProt). The metro gene (FBgn0050021) has no
reviewed Swiss-Prot entry; UniProt holds four unreviewed isoform entries: A1Z8G0 isoform A (595 aa),
B7YZF0 isoform C (585 aa), Q8T5S9 (GH12103 cDNA, 556 aa, equivalent to the muscle-predominant Metro-B
studied in PMID:20427642) and A0A0B4LF49 isoform D (546 aa). A1Z8G0 is the longest full-length isoform,
carries L27-L27-PDZ-SH3-GUK (domains 12-65, 66-124, 141-232, 239-309, 389-580) and is not a fragment, so
gene-level experimental annotations apply to it.

**Phylogenetic placement.** PANTHER 19.0 classification files place A1Z8G0 in PTHR23122:SF42 ("MENAGE A
TROIS, ISOFORM A"), whose only other model-organism member is C. elegans magu-1 (Q95XW5). The vertebrate
MPPs Metro most resembles sit in separate subfamilies: MPP7 SF39, MPP3 SF33, MPP4 SF34, MPP2 SF35. This
fits the paper's statement that MPP3, MPP4 and MPP7 are most similar to Metro but that no one-to-one
ortholog can be assigned. The IBA rows come from PTN001137125, a node above these subfamilies (the
MPP/PALS clade), and only convey membrane and junction localization; PAINT did not propagate the MPP-specific
partner-binding or epithelial-polarity process terms, and I do not transfer them.

**Literature.** PubMed search (Drosophila AND (metro OR CG30021) AND (MAGUK/Lin-7/Dlg/L27)) returns only
PMID:20427642 [Bachmann et al. 2010]. Full text (metro-publication-artifacts) read again: tandem L27
domains bind DLin-7 L27 and DlgS97 N-terminal L27; Metro co-IPs with DLin-7 from body wall; Metro is
postsynaptic and "is confined to the SSR (Fig. 2G)"; "Metro is essential for the recruitment of DLin-7 to
NMJs"; metro*47 null has fewer, larger and poorly differentiated Ib boutons, rescued by Metro-B; Metro is
virtually absent from epithelia.

**Changes from the previous review.**
- nucleotide binding / ATP binding (IEA UniRule): UNDECIDED -> MARK_AS_OVER_ANNOTATED. The P-loop Walker A
  lysine is Arg402 (GAPGVGRN vs GPSGTGKS), the GMP-site Ser is Pro422, and MAGUK GUK domains have lost or
  greatly weakened nucleotide binding [PMID:22117215 "the loss or dramatically weakening of GMP binding"].
  Not REMOVE because weak residual binding is not excluded experimentally.
- cell-cell junction (IBA): ACCEPT -> KEEP_AS_NON_CORE. The donor evidence is mostly epithelial junctions,
  and Metro is absent from epithelia; its junction is the NMJ SSR, which GO does not place under cell-cell
  junction.
- cell junction (IEA ARBA): ACCEPT -> MODIFY to subsynaptic reticulum (GO:0071212, a descendant via synapse),
  which the gene already has by IDA.
- kinase / transferase (IEA): REMOVE kept, now also citing PMID:22117215.
- plasma membrane (IBA), SSR (IDA), regulation of synaptic assembly at NMJ (IMP): ACCEPT kept.
- NEW: protein-macromolecule adaptor activity (GO:0030674), from Metro's own L27 pull-down/co-IP data and
  its role linking DlgS97 to DLin-7. I did not add "protein localization to synapse": the evidence is for
  Metro as the anchor of DLin-7, and the adaptor MF plus SSR location already capture it without a process
  term that would rest on loss-of-recruitment phenotypes alone.
- Core function now uses the adaptor MF and SSR location (it previously used cell-cell junction with no MF).
- Added PMID:22117215 and PMID:12482754 to references (they were cited in these notes and RESULTS.md but
  absent from the review's references).

**Relative.** Since A1Z8G0 is a full-length isoform and no reviewed canonical entry exists, the relative is
the nearest characterised relative. SF42's other member, worm magu-1, has little experimental work. The
closest characterised vertebrate relative is MPP7 (human Q5T2T1, SF39). The paper notes that the MPP7-Veli
promotion of hDlg binding is mechanistically conserved with Metro, and MPP7 forms a LIN7-DLG1 tripartite
complex. No review of MPP7 exists in the repo (no genes/*/MPP7 or Mpp7). MPP3 (SF33) is an alternative.

**Family review.** interpro/panther/PTHR23122/PTHR23122-review.yaml puts Metro as representative of a broad
"MPP/CASK MAGUK interaction scaffolds" grouping that is not tied to a PANTHER SF id. This is consistent with,
but coarser than, the SF42 placement. Its claims (no GUK catalysis, no CASK kinase transfer) agree with this
review. **Modules:** none in modules/ contain Metro or its DlgS97/DLin-7 complex. dmel_epithelial_polarity_complexes.yaml
contains dlg1 only in its epithelial Scribble module, which is unrelated to Metro.
