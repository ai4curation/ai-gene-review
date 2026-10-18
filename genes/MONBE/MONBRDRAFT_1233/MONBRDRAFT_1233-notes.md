# MONBRDRAFT_1233 (Monosiga brevicollis Warts/LATS, A9UVF9) - curation notes

**Automated deep research was unavailable** (no deep-research provider key in this
environment). These notes were built manually on 2026-10-01 from cached publications in
`publications/`, the UniProt record, the PANTHER PAINT table
(`interpro/panther/PTHR24356/PTHR24356-paint.tsv`) and a UniProt REST query. No
`-deep-research-*.md` file exists for this gene.

## Identity and gene model

- UniProt A9UVF9 (TrEMBL, unreviewed), ORF MONBRDRAFT_1233, EMBL EDQ90574.1,
  RefSeq XP_001744625.1, strain MX1 genome [PMID:18273011].
- **Fragment.** UniProt flags the entry "Flags: Fragment" with NON_TER at both residue 1
  and residue 380. The 380-aa model is essentially the kinase domain (PROSITE PS50011,
  78-368; ATP-binding K107; catalytic D201 proton acceptor) with ~77 residues upstream and
  12 downstream. Full-length Warts/LATS proteins are ~830 aa (S. rosetta F2U943) to
  ~1,100 aa (human LATS1), so this model lacks the N-terminal region that in LATS
  kinases carries the MOB1-binding segment and other regulatory sequence, and the
  AGC-kinase C-terminal extension carrying the hydrophobic-motif phosphorylation site.
  The proteome is "Unassembled WGS sequence", consistent with a partial gene model.
- UniProt REST (2026-10-01): A9UVF9 is the only M. brevicollis protein in PANTHER
  PTHR24356:SF418 "SERINE_THREONINE-PROTEIN KINASE WARTS"; the other M. brevicollis
  PTHR24356 members are in SF1 (A9UZ33, A9UZ34), SF163 (A9VCG3), SF414 (A9UP31, also a
  fragment). So there is no second gene model covering the missing Warts sequence.

## Biology

- M. brevicollis is strictly unicellular [PMID:18273011 "Although M. brevicollis is
  strictly unicellular, other choanoflagellates facultatively form colonies"]; it has no
  organs and is not known to form rosettes.
- Wts homologs occur across opisthokonts; Hpo homologs are absent from M. brevicollis
  [PMID:22832104 "except for M. brevicollis and non-chytrid fungi, most likely due to
  secondary loses"].
- Hippo pathway erosion specific to M. brevicollis [PMID:38729842]: mbYki lacks consensus
  HXRXXS Warts motifs ("mbYki has no consensus"), the M. brevicollis Hippo gene carries an
  insertion "predicted to truncate the protein at the beginning of the kinase domain", and
  the authors suggest "M. brevicollis may be an example of an organism that encodes a
  Yorkie ortholog but has lost the capacity to be regulated by Hippo pathway signaling".
  Caveat: the same draft assembly also gives a fragmentary Warts model, so the Hippo
  "truncation" could be an assembly/gene-model artefact; not resolved here.
- **No experimental data exist for M. brevicollis Warts** (no localization, kinase assay
  or genetics; the organism has no published gene-knockout data for this locus).
- Closest functional evidence:
  - S. rosetta warts KO: larger rosettes (~2x cells), slower proliferation
    [DOI:10.1101/2024.07.13.603360 "warts pac1 cells grew into giant rosettes containing
    about twice as many cells as wild-type ones"; "On the other hand, hippopac1 and warts
    pac1 KO clones proliferated markedly slower"]. Reviewed in genes/SALRS/warts.
  - Capsaspora coWts KO: coYki becomes nuclear [PMID:38517944 "Together, these results show
    that the Capsaspora Hippo kinase cascade regulates coYki by cytoplasmic sequestration"].
    Reviewed in genes/CAPO3/coWts.

## PANTHER / IBA (Track C)

- M. brevicollis is a PANTHER reference genome, so it gets real IBA rows (GO_REF:0000033).
- PTN000683254 (deep AGC node): GO:0004674 IBD, seeded by many AGC kinases across
  eukaryotes. Sound; the catalytic residues are retained.
- PTN002390470 ("Metazoa-Choanoflagellida" Warts/LATS speciation node) carries four IBDs:
  - GO:0035329 hippo signaling (fly wts, mouse Lats1/2, human LATS1/2; 2020-08-09)
  - GO:0046620 regulation of organ growth (mouse Lats2 only; 2022-04-15)
  - GO:0043065 positive regulation of apoptotic process (fly wts only; 2017-02-28)
  - GO:0000082 G1/S transition of mitotic cell cycle (mouse Lats2, human LATS2; 2017-02-28)
- Same terms reached S. rosetta warts by TreeGrafter (graft onto this very protein's leaf,
  PTN001220369). Decisions kept consistent with genes/SALRS/warts: organ growth REMOVE
  (no organs; taxon constraints do not exclude choanoflagellates), apoptosis and G1/S
  MARK_AS_OVER_ANNOTATED.
- Hippo signaling: S. rosetta accepted it. For M. brevicollis there is target-specific
  comparative-genomic evidence of pathway divergence (no consensus Wts sites on Yki;
  Hippo gene truncated/absent), which is the kind of evidence that can argue against an
  IBD node placement for one descendant. Not strong enough to remove (prediction only; the
  kinase may be activated by other upstream kinases; assembly artefacts possible), so
  UNDECIDED.
