# SHMT2 (human) review notes

UniProt: P34897 (GLYM_HUMAN), 504 aa precursor. Gene SHMT2, HGNC:10852, chr 12q13.3.
All provenance below is anchored to local files: the UniProt record
(`file:human/SHMT2/SHMT2-uniprot.txt`) and cached publications (`publications/PMID_*.md`).

## Core identity and catalytic function

SHMT2 is the **mitochondrial** isoform of serine hydroxymethyltransferase (the cytosolic
paralog is SHMT1, P34896). It is a PLP-dependent enzyme, EC 2.1.2.1.

- RecName in UniProt: "Serine hydroxymethyltransferase, mitochondrial" with AltName
  "Glycine hydroxymethyltransferase" and EC=2.1.2.1
  [file:human/SHMT2/SHMT2-uniprot.txt "RecName: Full=Serine hydroxymethyltransferase, mitochondrial"].
- Catalytic activity (UniProt CATALYTIC ACTIVITY, RHEA:15481):
  "(6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine; ... EC=2.1.2.1"
  [file:human/SHMT2/SHMT2-uniprot.txt]. The physiological (serine-consuming) direction is
  right-to-left (serine + THF -> glycine + 5,10-methylene-THF).
- FUNCTION: "Catalyzes the cleavage of serine to glycine accompanied with the production of
  5,10-methylenetetrahydrofolate, an essential intermediate for purine biosynthesis ...
  Serine provides the major source of folate one-carbon in cells by catalyzing the transfer
  of one carbon from serine to tetrahydrofolate"
  [file:human/SHMT2/SHMT2-uniprot.txt]. Evidence: PubMed 24075985, 25619277, 29364879, 33015733.
- Cofactor: pyridoxal 5'-phosphate (PLP) [file:human/SHMT2/SHMT2-uniprot.txt "Name=pyridoxal 5'-phosphate"].
  PLP binds at Lys-280 (Schiff base). Kinetics: KM=278 uM L-serine, KM=23 uM THF (PubMed:25619277).
- Catalytic MF experimentally supported for the human protein by IDA/IMP in multiple papers:
  PMID:8505317 (functional complementation of E. coli glyA mutant), PMID:17482557, PMID:24075985,
  PMID:25619277, PMID:29180469, PMID:29364879, PMID:29452640, PMID:33015733 (all GO:0004372 IDA/IMP in GOA).

**Core molecular function: GO:0004372 glycine hydroxymethyltransferase activity + GO:0030170 pyridoxal phosphate binding.**

## Pathway / biological process context

SHMT2 is the entry point of mitochondrial one-carbon (folate) metabolism.

- UniProt PATHWAY: "One-carbon metabolism; tetrahydrofolate interconversion"
  [file:human/SHMT2/SHMT2-uniprot.txt] (UniPathway UPA00193). Supports GO:0006730 one-carbon
  metabolic process, GO:0046653 tetrahydrofolate metabolic process, GO:0035999 THF interconversion.
- Produces glycine and 5,10-methylene-THF; supplies one-carbon units / formate to the cytosol for
  nucleotide (purine, thymidylate) synthesis. PMID:11516159 (13C NMR MCF-7): "Formate is formed in
  the mitochondria from carbon 3 of serine" and "Carbon 3 of serine accounts for about 95% of the
  one-carbon pool" — establishes the mitochondrial serine->one-carbon route (GO:0006730).
- Contributes to de novo mitochondrial thymidylate biosynthesis (with TYMS and DHFRL1);
  PMID:21876188: "Mitochondria ... converted dUMP to dTMP in the presence of NADPH and serine,
  through the activities of mitochondrial serine hydroxymethyltransferase (SHMT2)..." and this
  prevents uracil accumulation in mtDNA (supports GO:0046653, mitochondrial localization).
- Disease/BP validation: PMID:33015733 — biallelic SHMT2 variants cause a neurodevelopmental
  syndrome (NEDCASB, MIM:619121); patient fibroblasts show decreased glycine/serine ratio and
  altered 5-methyl-THF, i.e. IMP support for GO:0006563 L-serine metabolic process, GO:0006544
  glycine metabolic process, GO:0006730 one-carbon metabolic process, GO:0004372 (variant P499A
  "decreased glycine hydroxymethyltransferase activity"). "it transfers one-carbon units from
  serine to tetrahydrofolate (THF), generating glycine and 5,10-methylene-THF".

## Mitochondrial translation / OXPHOS regulation (downstream, non-core)

Two 2018 papers show SHMT2 catalytic output is required for mitochondrial translation and thus
oxidative phosphorylation — these are downstream physiological consequences of the one-carbon
function, not a distinct molecular activity:
- PMID:29364879 (Nature, Morscher): "loss of the catalytic activity of the mitochondrial folate
  enzyme serine hydroxymethyltransferase 2 (SHMT2) ... leads to defective oxidative phosphorylation
  in human cells due to impaired mitochondrial translation" and "SHMT2, presumably by generating
  mitochondrial 5,10-methylenetetrahydrofolate, provides methyl donors to produce the
  taurinomethyluridine base at the wobble position of select mitochondrial tRNAs." Supports
  GO:0070129 regulation of mitochondrial translation, GO:0002082 regulation of OXPHOS,
  GO:1903715 regulation of aerobic respiration (all IMP).
- PMID:29452640 (Mol Cell, Minton): "the mitochondrial serine hydroxymethyltransferase (SHMT2) is
  required for robust mitochondrial oxygen consumption and low glucose proliferation" — required
  for mt translation initiation / fMet-tRNA maintenance. Same three regulatory BP terms (IMP).

These regulatory BP terms are genuine (IMP, experimental) but are downstream/pleiotropic effects
of the enzyme; keep as non-core.

## Moonlighting: BRISC-SHMT2 deubiquitinase complex (catalysis-independent)

PMID:24075985 (Zheng, Cell Rep) — SHMT2 is a bona fide component of the cytoplasmic BRISC
deubiquitinase complex, a role independent of its metabolic catalysis:
- "we identify serine hydroxymethyltransferase (SHMT) as a previously unappreciated component that
  fulfills this function. SHMT directs BRISC activity at K63-Ub chains conjugated to the type 1
  interferon (IFN) receptor chain 1 (IFNAR1). BRISC-SHMT2 complexes localize to and deubiquitinate
  actively engaged IFNAR1, thus limiting its K63-Ub-mediated internalization and lysosomal degradation."
- UniProt captures this: "also plays a role in the deubiquitination of target proteins as component
  of the BRISC complex: required for IFNAR1 deubiquitination by the BRISC complex" and SUBUNIT
  "Interacts with ABRAXAS2 ... Identified in a complex with ABRAXAS2 and the other subunits of the
  BRISC complex" [file:human/SHMT2/SHMT2-uniprot.txt].
- GOA moonlighting annotations (all from PMID:24075985, experimental): GO:0070552 BRISC complex
  (IDA, part_of), GO:0070536 protein K63-linked deubiquitination (IMP), GO:0034340 response to
  type I interferon (IDA), plus IDA cytoplasm/nucleus localizations.
- ComplexPortal CPX-9341 "BRISC-SHMT2 complex"; DR ComplexPortal in UniProt.

Policy: this is a genuine, experimentally supported moonlighting function -> KEEP_AS_NON_CORE
(SHMT2 itself is not the DUB; BRCC3/BRCC36 is the catalytic DUB; SHMT2 is a structural/targeting
subunit). SHMT2 does not "enable" a DUB MF, so no DUB MF is placed in core_functions.

## Subcellular localization

- Mitochondrion is the primary location: TRANSIT 1..29 mitochondrial targeting peptide;
  SUBCELLULAR LOCATION "Mitochondrion ... Mitochondrion matrix, mitochondrion nucleoid ...
  Mitochondrion inner membrane ... Cytoplasm ... Nucleus. Note=Mainly localizes in the
  mitochondrion. Also found in the cytoplasm and nucleus as part of the BRISC complex"
  [file:human/SHMT2/SHMT2-uniprot.txt].
- Experimental localizations in GOA: GO:0005739 mitochondrion (IDA PMID:24075985, PMID:17482557,
  PMID:24075985; EXP PMID:21876188; HTP PMID:34800366; HPA IDA), GO:0005759 mitochondrial matrix
  (IDA PMID:21876188, PMID:11516159), GO:0005743 mitochondrial inner membrane (IDA PMID:21876188),
  GO:0042645 mitochondrial nucleoid (IDA PMID:18063578), GO:0005737 cytoplasm & GO:0005634 nucleus
  (IDA PMID:24075985, BRISC-related).
- Mitochondrial nucleoid / mtDNA association: PMID:18063578 (nucleoid proteomics) is cited by
  UniProt for "Associates with mitochondrial DNA" and mitochondrion nucleoid location. The
  chromatin binding IDA (GO:0003682, PMID:18063578) is best read as mtDNA/nucleoid association;
  the more specific & appropriate CC term is GO:0042645 mitochondrial nucleoid.
- GO:0070062 extracellular exosome (HDA, PMID:19056867 urinary exosomes, PMID:20458337 B-cell
  exosomes) — high-throughput proteomics catch-all; over-annotation for a mitochondrial matrix enzyme.

## Oligomeric state

Homotetramer in presence of PLP; homodimer without PLP (PMID:25619277, PMID:29180469). Supports
GO:0051289 protein homotetramerization / GO:0051262 protein tetramerization (IDA) and GO:0042802
identical protein binding (self-interaction). UniProt SUBUNIT: "Homotetramer; in the presence of
bound pyridoxal 5'-phosphate ... Homodimer; in the absence of bound pyridoxal 5'-phosphate ...
Pyridoxal 5'-phosphate binding mediates an important conformation change that is required for
tetramerization" [file:human/SHMT2/SHMT2-uniprot.txt].

## Notable IEA over-/mis-annotations to watch

- GO:0120567 hydroxytrimethyllysine aldolase activity (IEA GO_REF:0000117 ARBA; and IDA
  PMID:38615009 via FlyBase). PMID:38615009: "the top-ranked candidates, serine hydroxymethyl
  transferase (SHMT) 1 and 2, catalyze the HTMLA reaction. However, a mouse protein absent in
  humans (threonine aldolase; Tha1) catalyzes the reaction more efficiently ... with HTMLA
  activity of SHMT partially compensating for its function." Real but promiscuous/secondary
  in-vitro side activity; not the core function. The IDA is experimental -> KEEP_AS_NON_CORE;
  the redundant IEA -> MARK_AS_OVER_ANNOTATED.
- GO:0008732 L-allo-threonine aldolase activity (IEA GO_REF:0000107 from rat ortholog) — SHMTs
  have promiscuous threonine aldolase side activity; not human-experimentally established core
  function. Over-annotation.
- GO:0016597 amino acid binding (IEA, Ensembl) — generic; substrate binding is captured by the
  catalytic MF + PLP binding. Over-annotation.
- GO:0008284 positive regulation of cell population proliferation (IEA, from rat ortholog) — SHMT2
  supports proliferation in cancer (PMID:29180469 abstract "drives cancer cell proliferation") but
  this is an indirect metabolic consequence; not a core function; keep non-core / over-annotated IEA.
- GO:0006545 glycine biosynthetic process (IBA + IEA) — direction ambiguity. SHMT2's physiological
  direction is serine catabolism (serine -> glycine), so glycine *biosynthesis* is defensible, but
  glycine metabolic process (GO:0006544) is the better-supported experimental framing.

## Protein binding (GO:0005515) IPI annotations

Nine bare "protein binding" IPI annotations from interactome/screen papers (PMID:19615732 DUB
interactome/BRCC3; PMID:25416956, PMID:26871637, PMID:29892012, PMID:32296183, PMID:33961781
various interactome maps; PMID:25902260 KIRREL3; PMID:37398436 AI PPI pipeline). Per policy, bare
protein binding is uninformative for MF -> MARK_AS_OVER_ANNOTATED (never REMOVE IPI). The BRCC3
interaction (PMID:19615732, PMID:33961781, PMID:37398436) is mechanistically the BRISC association.
GO:0042802 identical protein binding (IPI PMID:37398436; IEA) reflects homo-oligomerization — real,
keep non-core.

## Summary of core

- MF: GO:0004372 glycine hydroxymethyltransferase activity (EC 2.1.2.1); GO:0030170 PLP binding.
- BP: GO:0006730 one-carbon metabolic process (mitochondrial folate one-carbon entry point).
- CC: GO:0005759 mitochondrial matrix (with GO:0005739 mitochondrion).
- Moonlighting (non-core): BRISC complex / K63-deubiquitination / type I IFN response.
</content>
</invoke>
