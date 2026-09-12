# TPH1 (Tryptophan 5-hydroxylase 1) — review notes

UniProt: P17752 (TPH1_HUMAN), 444 aa. Gene HGNC:12008. EC 1.14.16.4.
Source of truth for biology below is the local UniProt record
`file:human/TPH1/TPH1-uniprot.txt` unless a PMID is cited.

## Core biochemistry / function

- Rate-limiting enzyme of serotonin (5-HT) biosynthesis. UniProt FUNCTION:
  "Oxidizes L-tryptophan to 5-hydroxy-l-tryptophan in the rate-determining step of
  serotonin biosynthesis." [file:human/TPH1/TPH1-uniprot.txt]
- Catalytic activity (RHEA:16709, EC 1.14.16.4):
  "(6R)-L-erythro-5,6,7,8-tetrahydrobiopterin + L-tryptophan + O2 = 5-hydroxy-L-tryptophan
  + (4aS,6R)-4a-hydroxy-L-erythro-5,6,7,8-tetrahydrobiopterin"
  [file:human/TPH1/TPH1-uniprot.txt]. This is a tetrahydrobiopterin (BH4)- and O2-dependent
  aromatic amino acid monooxygenase → GO:0004510 tryptophan 5-monooxygenase activity.
- Cofactor: Fe(2+) (ChEBI:29033), experimentally established from the crystal structure
  [PMID:12379098]. UniProt COFACTOR: "Name=Fe(2+)" with Evidence ECO:0000269|PubMed:12379098.
  Three Fe-coordinating residues in the FT table (His272, His277, Glu317 — "Fe cation").
  → GO:0005506 iron ion binding / GO:0008198 ferrous iron binding.
- Pathway: "Aromatic compound metabolism; serotonin biosynthesis; serotonin from
  L-tryptophan: step 1/2." [file:human/TPH1/TPH1-uniprot.txt] (UniPathway UPA00846/UER00799).
- Family: "Belongs to the biopterin-dependent aromatic amino acid hydroxylase family."
  [file:human/TPH1/TPH1-uniprot.txt] — same family as PAH (phenylalanine hydroxylase) and
  TH (tyrosine hydroxylase). Domain architecture: N-terminal ACT regulatory domain
  (res 19–94) + catalytic aromatic-amino-acid-hydroxylase domain (Fe/BH4 binding).
- Quaternary structure: "Homotetramer (By similarity)." Interacts with DNAJC12 (By
  similarity) — DNAJC12 is a co-chaperone of the aromatic amino acid hydroxylases.
  [file:human/TPH1/TPH1-uniprot.txt]
- 3D structure: X-ray crystallography of the catalytic domain (102-402) in complex with
  iron and cofactor [PMID:12379098]; many PDB entries (1MLW, 5TPG, 8CJ* etc.).
- Regulation/PTM: Phosphorylated (Ser58, by PKA per FT) and ubiquitinated → proteasomal
  degradation (by similarity to P09810). [file:human/TPH1/TPH1-uniprot.txt]

## Isoforms / tissue

- Two isoforms by alternative splicing at the 3' end (isoform 2 = VSP_000546, C-terminal
  tail swap). Isoform 2 "Seems to be less widely expressed than isoform 1"
  [PMID:9751214, via file:human/TPH1/TPH1-uniprot.txt].
- TPH1 is the peripheral / non-neuronal paralog. Reactome R-HSA-9621048 summary:
  "TPH1 is expressed in the gut, the periphery and in the pineal gland and additionally
  has roles during neuronal development. In contrast, TPH2 is expressed at high levels
  in the brain and the gut." Expression (HPA): "Group enriched (choroid plexus, intestine,
  stomach)." [file:human/TPH1/TPH1-uniprot.txt]. Peripheral 5-HT feeds pineal melatonin
  synthesis (Reactome R-HSA-209931 "Serotonin and melatonin biosynthesis").

## Two paralogs (do not confuse)

- TPH1 = P17752 (this gene): peripheral serotonin synthesis (gut enterochromaffin cells,
  pineal, mast cells, platelets are loaded from gut-derived 5-HT).
- TPH2 = Q8IWU9: neuronal isoform, brain serotonergic neurons. Note the IBA GO:0004510
  annotation lists UniProtKB:Q8IWU9 (TPH2) among with/from, i.e. shared family MF.

## Annotation review rationale (summary)

- MF core: GO:0004510 tryptophan 5-monooxygenase activity — the defining, experimentally
  and structurally supported activity. Kept as core (ACCEPT for IBA; the redundant IEA/ISS
  copies also ACCEPT as the gene's own correct MF).
- MF core: GO:0005506 iron ion binding — supported by the crystal-structure Fe site
  [PMID:12379098] and FT Fe-binding residues. Fe is Fe(2+), so GO:0008198 ferrous iron
  binding is the most precise MF (added as core; existing GO:0005506 IEA kept/ACCEPT).
- BP core: GO:0042427 serotonin biosynthetic process — central biological role; also the
  more precise GO:0006587 (from L-tryptophan) is used in core_functions.
- GO:0004497 monooxygenase activity (IEA) and GO:0016714 (the oxidoreductase parent class)
  are correct-but-general parents of GO:0004510 → MODIFY to the specific term / mark as
  redundant-general (KEEP as non-core parent). GO:0009072 aromatic amino acid metabolic
  process (IEA) is a correct but general BP parent.
- Platelet degranulation (GO:0002576) and regulation of hemostasis (GO:1900046): these are
  ISS/IEA transferred from mouse (P17532). TPH1-derived gut serotonin is taken up and stored
  by platelets and released on degranulation, contributing to hemostasis; this is a
  downstream physiological role, not TPH1's molecular action → KEEP_AS_NON_CORE.
- neuron projection (GO:0043005, IBA is_active_in): family-level PAN-GO location driven by
  neuronal TPH2; TPH1 is the non-neuronal paralog, so this location is over-annotated for
  TPH1 specifically → MARK_AS_OVER_ANNOTATED (IBA, not experimental, so not removed).
- cytosol (GO:0005829): correct subcellular location (soluble cytosolic enzyme); ISS + TAS
  Reactome → ACCEPT (non-core CC).
- protein binding (GO:0005515, IPI ×4 references): high-throughput interactome screens
  (Huttlin 2017/2021 BioPlex AP-MS; Luck 2020 HuRI Y2H; Haenig 2020 neurodegeneration Y2H).
  None of the cached full texts mention TPH1 in prose (hits are only in supplementary data
  tables); the biologically meaningful interactor is DNAJC12 (Q9UKB3, a hydroxylase
  co-chaperone), captured by UniProt SUBUNIT. Bare "protein binding" is uninformative →
  MARK_AS_OVER_ANNOTATED (per policy: never REMOVE a bare protein-binding IPI).
</content>
</invoke>
