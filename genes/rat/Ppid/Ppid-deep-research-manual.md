# Ppid (rat, Q6DGG0) - manual literature research

No deep-research API was available; this summary was compiled by hand from cached
publications (publications/PMID_*.md) and PubMed searches. Almost all experimental work
on cyclophilin 40 (CyP40, PPID) was done with the human, bovine or mouse protein; there
are no rat-specific functional studies of Ppid. Rat Ppid is the 1:1 ortholog (RGD:1303174,
GeneID 361967) and its UniProt record propagates function from human Q08752 and mouse Q9CR16.

## Identity and nomenclature trap

- Ppid encodes cyclophilin 40 (CyP-40), a 370-aa protein with an N-terminal
  cyclophilin-type PPIase domain (res. 19-183), a linker (185-215, "chaperone activity")
  and three C-terminal TPR repeats that bind the EEVD tail of Hsp90/Hsc70.
- "Cyclophilin D" / "CyP-D" / "CypD" in the mitochondrial permeability transition
  literature is a different gene, Ppif (rat P29117, RGD:628670). UniProt carries a
  CAUTION on this entry: "This protein should not be confused with mitochondrial
  peptidyl-prolyl cis-trans isomerase F (PPIF) which is often referred to as cyclophilin D
  or CypD."
- Two of the three rat experimental papers annotated to Ppid by RGD are CypD (Ppif) papers:
  - PMID:12077116 (Lin & Lechleiter 2002, abstract only): "Cyclophilin D (CyPD) is thought
    to sensitize opening of the mitochondrial permeability transition pore (mPTP)" and
    "CyPD binding to the adenine nucleotide translocator (ANT)" - the mitochondrial PPIF
    protein. RGD rows (PPIase IDA; IMP response to oxidative stress, negative regulation of
    apoptotic process, regulation of mitochondrial membrane potential) are probably
    mis-attributed to Ppid.
  - PMID:19832699 (Malouitre et al. 2009, full text read): "CyP-D, a mitochondrial isoform
    that facilitates formation of the permeability transition pore in the mitochondrial
    inner membrane"; the paper measures recombinant CyP-D and CyP-A; CyP40 is never
    mentioned (grep for Cyp40/cyclophilin 40 = 0 hits). The RGD IDA "cyclosporin A
    binding" row is therefore about Ppif, not Ppid.

## Molecular function

- PPIase: recombinant human CyP-40 "showed peptidyl-prolyl cis-trans isomerase activity
  (kcat/Km = 1.12 x 10(6) M-1.s-1) comparable to that of bovine brain CyP-40"
  [PMID:7744028]. Pirkl & Buchner: "in the mammalian system, in contrast to the yeast
  system, the catalytic activity of prolyl isomerization corresponds well to that of the
  respective small PPIases" [PMID:11350175].
- Cyclosporin A binding: CyP-40 was isolated as "a 40-kDa cyclosporin A (CsA)-binding
  protein" [PMID:8509368]; its weak CsA affinity is due to His141 in place of the
  conserved Trp [PMID:7744028].
- Hsp90 binding: GST-CyP-40 pulls down hsp90 as "the predominant associated protein in
  all tissue extracts examined" [PMID:7717993]; binding maps to the TPR domain plus
  flanking residues [PMID:8621687]; "Both purified CyP-40 and hsp56 bind directly to
  purified hsp90" [PMID:7657624]; "two PPIase monomers bind to an Hsp90 dimer"
  [PMID:11350175].
- Hsc70 binding: "we have identified the constitutively expressed form of Hsp70, heat
  shock cognate (Hsc70), as an additional target for CyP40" [PMID:15497503].
- Chaperone (holdase-like) activity: "Cyp-40 and p23 functioned as molecular chaperones"
  and "both proteins interacted with the substrate to maintain a nonnative
  folding-competent intermediate" [PMID:8939864]; chaperone function maps to the linker
  [PMID:16650407]; "Cyp40 and FKBP51 are the more potent chaperones" [PMID:11350175].
- MYB: "Cyp-40 ... could inhibit c-Myb DNA binding activity", requiring both the TPR and
  catalytic domains [PMID:9659917].
- S100 regulation: "S100A1 and S100A2 specifically interact with the TPR domains of FKBP52
  and CyP40 in a Ca(2+)-dependent manner" [PMID:20188096].

## Steroid receptor / AHR complexes

- CyP40 is a component of unactivated estrogen receptor and glucocorticoid receptor
  heterocomplexes, via Hsp90 [PMID:8621687, PMID:7657624]; PPIase activity is not
  required for GR-hsp90 heterocomplex assembly [PMID:7657624].
- AHR: "When the CyP40 content in MCF-7 cells is reduced, up-regulation of cyp1a1 and
  cyp1b1 by 3-methylchloranthrene (3MC) is also reduced, suggesting that CyP40 is
  essential for maximal AhR function"; residues 186-215 are needed for forming the
  AhR/Arnt/DRE complex [PMID:18708059]. This is a positive effect on AHR-dependent
  transcription; the human IMP annotation of this paper to "negative regulation of
  transcription by RNA polymerase II" (propagated to rat) inverts the direction.

## Localization

- Human CyP40 in MCF-7 cells: "a predominantly nucleolar localization, with some nuclear
  and cytoplasmic staining" that redistributes to nucleoplasm after heat shock
  [PMID:11525244]. Monoclonal antibody staining showed "preferential localization in
  cytoplasm" [PMID:8860948].

## Cell-level phenotypes (non-core)

- UVA: CyP40-knockdown keratinocytes show less apoptosis, less MMP dissipation and less
  mitochondrial superoxide after UVA [PMID:23220213] (human).
- HCV: siRNA to cyp40 enlarged lipid droplets and blocked apoB secretion in HCV
  replicon/infected Huh7 cells [PMID:21711559]; multiple cyclophilins support HCV
  replication [PMID:19932913]. These are host-factor phenotypes in a human virus model.
- Tau: CyP40 dissolves tau amyloids in vitro and in a mouse model [PMID:28654636].
