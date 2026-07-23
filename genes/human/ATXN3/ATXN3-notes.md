# ATXN3 (Ataxin-3) — Gene Review Notes

UniProt: P54252 | HGNC: ATXN3 | Gene aliases: MJD, MJD1, SCA3, ATX3
Organism: *Homo sapiens* (NCBITaxon:9606)

> Note on naming: the review was requested as "SCA3". SCA3 (spinocerebellar
> ataxia type 3 / Machado-Joseph disease) is the *disease*; the HGNC gene
> symbol is **ATXN3**. Per project convention (human = HGNC symbols) the
> review is filed under ATXN3.

> Provenance note: automated deep-research providers were unavailable in this
> session (falcon returned HTTP 402 Payment Required; perplexity/asta/openscientist
> not wired into the CLI provider enum). These notes are synthesized from the
> cached UniProt record, the 18 cached publications, and Reactome. No
> `-deep-research-<provider>.md` file was fabricated, per CLAUDE.md.

## Summary

Ataxin-3 is a **deubiquitinating enzyme (DUB)** of the Josephin (Machado-Joseph
domain, MJD) cysteine-protease family. It is the protein whose gene, when its
CAG/polyglutamine tract expands beyond ~52 repeats, causes **spinocerebellar
ataxia type 3 (SCA3) / Machado-Joseph disease**, the most common dominantly
inherited ataxia worldwide.

Domain architecture:
- **Josephin domain (aa 1–180)**: catalytic papain-like cysteine-protease
  DUB domain. Catalytic triad **Cys14–His119–Asn134** (UniProt ACT_SITE 14,
  119, 134; MUTAGENESIS of Cys-14 abolishes activity, PMID:23625928,
  PMID:16118278, PMID:33157014).
- **Ubiquitin-interacting motifs (UIMs)**: UIM1 (224–243), UIM2 (244–263),
  and (isoform-dependent) UIM3 (331–349). UIMs bind ubiquitin and are
  required to limit the length of ubiquitin chains.
- **PolyQ tract** (~aa 292 onward): normal 12–40 Gln; pathogenic when
  expanded (~>52). The poly-Gln region also mediates interaction with BECN1.
- Multiple splice isoforms (P54252-1..-5); isoform composition affects the
  C-terminal UIM3 and the tail (see PMID:30455355).

## Molecular function — DUB activity and linkage specificity

- Ataxin-3 is an active DUB: Josephin-domain proteins from many species are
  active de-ubiquitinating enzymes [PMID:17696782 "Josephin domain-containing
  proteins from a variety of species are active de-ubiquitination enzymes"].
- It is a **chain-trimming / editing DUB**, not a broad rescue DUB: it binds
  long polyubiquitin chains and trims them, with weak/no activity on chains of
  4 or fewer ubiquitins (UniProt FUNCTION, from PMID:17696782).
- **Linkage specificity**: cleaves both **K48-linked** and **K63-linked**
  chains; VCP/p97 stimulates activity [PMID:22970133 "Valosin-containing
  protein (VCP/p97) is an activator of wild-type ataxin-3"]. This paper is the
  IDA source for the K48-linked (GO:1990380) and K63-linked (GO:0061578)
  deubiquitinase-activity terms and their process terms (GO:0070536,
  GO:0071108).
- The core MF term **cysteine-type deubiquitinase activity (GO:0004843)** is
  well supported by direct assay (EXP PMID:17696782; IDA PMID:33157014).

## Biological processes

1. **ERAD / retrotranslocation (endoplasmic-reticulum-associated degradation)**
   Ataxin-3 is a p97/VCP-associated DUB that regulates retrotranslocation of
   ERAD substrates [PMID:17000876 "Regulation of retrotranslocation by
   p97-associated deubiquitinating enzyme ataxin-3"]. A later study shows it
   negatively regulates retro-translocation of *nonubiquitinated* substrates
   [PMID:24068323]. Supports GO:1904294 (positive regulation of ERAD pathway,
   IMP PMID:17000876) and ER-membrane colocalization (GO:0005789).

2. **Protein quality control / proteasomal degradation**
   Interacts with STUB1/CHIP and the proteasome shuttle factors RAD23A/RAD23B
   (HHR23A/B) [PMID:10915768 "Ataxin-3 ... interacts with the two human
   homologs of yeast DNA repair protein RAD23, HHR23A and HHR23B"]. Restricts
   ubiquitin-chain length on CHIP substrates. Supports GO:0006515, GO:0043161.

3. **mTORC1 signaling (amino-acid starvation)**
   Lysosome-localized ataxin-3 deubiquitinates RHEB; amino acids block this
   activity, so RHEB stays polyubiquitinated and mTORC1 is activated
   [PMID:33157014 "Amino Acids Enhance Polyubiquitination of Rheb and Its
   Binding to mTORC1 by Blocking Lysosomal ATXN3 Deubiquitinase Activity"].
   Supports GO:1904262 (negative regulation of TORC1 signaling),
   GO:0034198 (cellular response to amino acid starvation), and the
   lysosomal-membrane localization (GO:0005765).

4. **Autophagy**
   Deubiquitinates BECN1 at Lys-402, stabilizing it and promoting
   starvation-induced autophagy; poly-Gln domain mediates the BECN1
   interaction (UniProt FUNCTION, PMID:28445460 — not in GOA set).

5. **Transcription regulation**
   Histone-binding protein that represses transcription (UniProt FUNCTION,
   PMID:12297501). Acts with FOXO4 to regulate the SOD2 (MnSOD) promoter
   (Reactome R-HSA-9617832, R-HSA-9617927; Reactome pathway
   R-HSA-9615017 "FOXO-mediated transcription of oxidative stress ...").

6. **Cytoskeleton regulation**
   Loss of ataxin-3 causes cytoskeletal disorganization and increased cell
   death [PMID:20637808 "Absence of ataxin-3 leads to cytoskeletal
   disorganization and increased cell death"]. Source for the four
   cytoskeleton `acts_upstream_of_or_within` IMP terms (GO:0000226,
   GO:0030036, GO:0045104, GO:0010810). These are downstream/pleiotropic
   phenotypes of a knockdown, best kept as non-core.

## Localization

Predominantly cytoplasmic but shuttles to the nucleus and associates with the
**nuclear matrix** [PMID:9580663 "Ataxin-3 is transported into the nucleus and
associates with the nuclear matrix"; PMID:9124802 "Machado-Joseph disease gene
product is a cytoplasmic protein widely expressed in brain"]. Both cytosol
(GO:0005829) and nucleus/nucleoplasm (GO:0005634, GO:0005654) are supported.
Lysosomal membrane (GO:0005765) is supported in the mTORC1 context
(PMID:33157014). Nuclear inclusion bodies (GO:0042405) are the pathological
polyQ-aggregate hallmark.

## Interactions of note (IPI protein-binding annotations)

- **RAD23A/RAD23B (HHR23A/B)** — proteasome shuttle / NER factors (PMID:10915768)
- **VCP/p97** — DUB activator, ERAD (PMID:16525503, PMID:22970133, PMID:17000876)
- **PRKN/parkin** — ataxin-3 is a multivalent ligand for the parkin Ubl domain
  (PMID:24063750); deubiquitinates parkin (Reactome R-HSA-5688837)
- **STUB1/CHIP** — ubiquitin ligase partner (GO:0031625 sources incl. PMID:24068323)
- **HSJ1a (DNAJB2)** co-chaperone — regulates ataxin-3 proteasomal degradation (PMID:21625540)
- **NOD2/TLR2** innate immune signaling in myeloid cells (PMID:31379806)
- Interactome / aggregation network (PMID:32814053), ataxia PPI network (PMID:16713569)

## Curation considerations for the annotation review

- **`protein binding` (GO:0005515, IPI)**: multiple instances. Per project
  guidance this uninformative term is not a *core function*; where a more
  specific MF exists (ubiquitin ligase binding GO:0031625, ATPase binding
  GO:0051117) that is preferable. Keep IPI protein-binding as accepted
  evidence-of-interaction but non-core.
- **DUB activity (GO:0004843) and linkage-specific DUB (GO:1990380,
  GO:0061578)**: these are the **core molecular function** — accept.
- **ERAD, PQC, mTORC1, autophagy, transcription**: genuine biological roles —
  accept; mTORC1/ERAD/PQC are strong. Some are non-core relative to the
  central DUB activity.
- **Cytoskeleton IMP terms (PMID:20637808)**: downstream/indirect phenotypes
  from ataxin-3 depletion — keep as non-core (KEEP_AS_NON_CORE), not core MF.
- **Mitochondrial ISS terms (GO:0005759, GO:0031966, GO_REF:0000024)**: transfer
  by sequence similarity to mouse Q9CVD2; ataxin-3 is not primarily a
  mitochondrial-matrix protein. Treat with caution — over-annotation risk.
- **nucleotide-excision repair (GO:0006289, TAS PMID:10915768)**: the paper
  shows interaction with RAD23 (a NER/shuttle factor), not that ataxin-3
  itself does NER. Likely over-annotation of an interaction into a process.
- **chemical synaptic transmission (GO:0007268, TAS PMID:7655453)** and
  **nervous system development (GO:0007399, TAS PMID:9124802)**: the cited
  papers are the disease-gene cloning / expression papers; these processes are
  not demonstrated molecular roles of ataxin-3 — over-annotation candidates.
- **synapse (GO:0045202, IEA GO_REF:0000108)**: inter-ontology inferred; weak.
