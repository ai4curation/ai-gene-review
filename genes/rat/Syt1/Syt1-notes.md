# Syt1 (rat, P21707) review notes

## Session 2026-10-28

- `just fetch-gene rat Syt1` resolved P21707 (Swiss-Prot SYT1_RAT; RGD:3803; GeneID 25716);
  207 GOA rows seeded. `just fetch-gene-pmids` cached 56 PMIDs; PMID:18508778 and
  PMID:20688915 (both full text) read; PMID:19412166 additionally cached for the
  spontaneous-release role.
- No deep-research API; literature synthesis written by hand in
  `Syt1-deep-research-manual.md`.

### Picture of the gene

Syt1 is the vesicular Ca2+ sensor for fast synchronous release
[PMID:12526776 "in synaptotagmin 1 knockout mice, the fast component of both Ca(2+)- and
Sr(2+)-induced release is selectively impaired"]. Its C2 domains bind Ca2+ and anionic
lipids [PMID:8253763 "this C2 domain by itself binds Ca2+ and phospholipids with high
affinity"], PIP2 [PMID:22447935], and t-SNAREs in a Ca2+-promoted manner
[PMID:20688915 "rat SYT1, fly SYT1, and fly SYT4 all exhibited weak t-SNARE binding
activity in the absence of Ca2+ and much stronger binding in the presence of Ca2+"].
It also tethers vesicles before SNAREpin assembly [PMID:22810233] and clamps fusion
without Ca2+ [PMID:20688915 "this isoform also serves to clamp or inhibit fusion in the
absence of Ca2+"]; deletion unclamps spontaneous release [PMID:19412166].

### Main curation decisions

- Core MFs: calcium ion sensor activity; calcium-dependent phospholipid binding; SNARE
  binding; vesicle membrane tethering activity. calcium ion binding rows MODIFIED to
  calcium ion sensor activity; phospholipid/lipid binding MODIFIED to
  calcium-dependent phospholipid binding.
- Core BP: calcium-dependent activation of synaptic vesicle fusion and fast
  Ca2+-dependent exocytosis of neurotransmitter; broad ancestors (SV exocytosis,
  vesicle-mediated transport, regulation of SV exocytosis, Ca2+-regulated exocytosis)
  MODIFIED down to these.
- Core CC: synaptic vesicle membrane; cytoplasm/membrane/synaptic vesicle/intracellular
  vesicle/exocytic vesicle MODIFIED to it. Dense core granule accepted (neuroendocrine
  Ca2+ sensor with Syt9 [PMID:17686463]).
- REMOVE: calcium activated phospholipid scrambling (two RGD rows; full texts read show
  lateral PS demixing and inter-membrane PS asymmetry, not transbilayer movement;
  source_defects recorded). Bare protein binding rows removed or MODIFIED (SNARE
  binding, AP-2 adaptor complex binding, small GTPase binding).
- MARK_AS_OVER_ANNOTATED: Golgi (biosynthetic transit), SNARE complex and vesicle
  tethering complex membership, xenobiotic transmembrane transport (toxin receptor, not
  transporter; source_defect CHECK), glycosylation-dependent protein binding (Syt1 is the
  glycosylated protein; source_defect CHECK), protein insertion into membrane,
  inhibitory postsynaptic potential (presynaptic necessity, not participation),
  membraneless organelle assembly, pre/postsynaptic cytosol (TM protein).
- UNDECIDED: LDL particle receptor binding (IEA/ISO from human; source not traced).
- regulation of calcium-dependent activation of SV fusion (RGD IMP) MODIFIED laterally to
  calcium-dependent activation of SV fusion, with a REPOINT source defect.
- No NEW rows proposed.

### Caveats

- PMID:18179895 (CNTNAP2 paper) mentions synaptotagmin only in figures; plasma membrane
  and synaptic vesicle rows from it were kept/refined on general biology.
- The shared scratchpad directory is used by other concurrent agents; an earlier helper
  script of mine was overwritten there.
