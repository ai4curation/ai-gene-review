# Ets1 (Sp-Ets1/2) — Strongylocentrotus purpuratus — curation notes

## Identity of the UniProt entry

- UniProt Q26645 (TrEMBL, "ETS homologue") is the translation of EMBL L19541 /
  AAA30048.1, an embryonic S. purpuratus cDNA submitted in 1993 by Rao & Childs
  ("Role of the sea urchin ETS homologue in early embryonic gene regulation and
  development"; unpublished submission, no PMID). RefSeq NP_999698.1 / NM_214533.1
  and NCBI GeneID 373306 are derived from the same mRNA.
- NCBI Gene 373306 (queried via eutils esummary, 2026-09-26) carries the official
  symbol `ets1`, description "ets homolog", on scaffold NW_022145594.1
  (41,398,221–41,450,047; 11 exons). PANTHER places the protein in PTHR11849
  (ETS family), subfamily SF289 (the Ets1/Ets2/Pointed subfamily; label not
  verified against panther.obo here and not used in the review).
- Rizzo et al. 2006 surveyed the genome and found a single sea urchin orthologue
  for each vertebrate ets subfamily, naming the Ets1/Ets2 orthologue Sp-Ets1/2
  [PMID:16997294 "almost all vertebrate ets subfamilies, with the exception of one, so far found only in mammals, are each represented by one orthologous sea urchin gene"].
  Because there is only one Ets1/2-class gene in the genome, the 1993 cDNA, the
  RefSeq/NCBI `ets1` locus, and the GRN gene called ets1 / ets1/2 by Davidson,
  Ettensohn and McClay labs are the same gene.
- Sequence check: the Q26645 sequence contains a P-P-T(107)-P motif
  (…PAVPPPTPGTNA…, residues 101–112), i.e. the threonine-107 ERK consensus site
  whose phosphorylation is required for Ets1 activity in Paracentrotus lividus
  [PMID:14973284 "mutations in the consensus phosphorylation motif substituting threonine 107 by an aspartic or an alanine residue resulted respectively in a constitutively active form of Ets1 that could not be inhibited by U0126 or in an inactive form of Ets1"].
  The numbering coincides exactly, which further supports that Q26645 is the
  Ets1 orthologue studied functionally.
- Confidence that Q26645 = GRN ets1 (Sp-Ets1/2): HIGH.

## What the protein is

ETS-domain (winged helix) transcription factor with an N-terminal PNT/SAM
(pointed) domain (UniProt features: PNT 120–205, ETS DNA-binding domain 448–528),
559 aa. Orthologue of vertebrate ETS1/ETS2 and Drosophila Pointed.

## Place in the skeletogenic (micromere/PMC) GRN

- Maternal + zygotic expression. Maternal ets1 transcript is ubiquitous through
  cleavage; zygotic expression is restricted to the skeletogenic micromere lineage
  and later expands to non-skeletogenic mesoderm
  [PMID:18413610 "Although zygotically expressed in the skeletogenic micromere lineage because it is one of the double negative gate targets, the ets1 gene is also maternally expressed, and WMISH shows that in cleavage-blastula-stage embryos the maternal transcript is present everywhere"]
  [PMID:18413610 "ets1 also is later expressed in nonskeletogenic mesoderm"]
  [PMID:16997294 "Five ets genes (Sp-Ets1/2, Sp-Tel, Sp-Pea, Sp-Ets4, Sp-Erf) are also maternally expressed"].
  Same pattern in Hemicentrotus HpEts
  [PMID:10096062 "HpEts, which is maternally expressed ubiquitously during the cleavage stage and which expression becomes restricted to the skeletogenic primary mesenchyme cells (PMC) after the hatching blastula stage"].
- Inputs: ets1 is one of the direct targets of the Pmar1 → HesC double-negative
  gate, together with alx1, tbr, tel and delta
  [PMID:17636127 "if expression of pmar1 is forced to occur globally (by injection into the egg of the mRNA), then the delta , tbr , ets1 , alx1 , and downstream genes are transcribed in all cells of the embryo, and all cells thereby adopt skeletogenic micromere lineage fate"]
  [PMID:17636127 "by 24 h, that of ets1 and tbr had similarly increased"]
  [PMID:18413610 "They are four essential regulators of downstream micromere lineage function: alx1 ( 29 ), ets1 ( 9 , 33 ), tbr ( 34 , 35 ), and tel ( 9 )"].
  Oliveri 2008 ref 9 is Oliveri, Carrick & Davidson 2002 [PMID:12027443], whose
  abstract reports derepression "of skeletogenic genes, including several
  transcription factors normally expressed only in micromere descendants" upon
  Pmar1 mRNA injection (ets1 not named in the abstract; full text not cached).
- Post-translational input: activation of Ets1 in the micromere lineage requires
  Raf/MEK/ERK phosphorylation at T107
  [PMID:14973284 "These results show that the MAP kinase pathway, working through phosphorylation of Ets1, is required for full specification of the PMCs and their subsequent transition from epithelial to mesenchymal state"]
  (P. lividus).
- Outputs (regulatory genes):
  - alx1 — Ets1 is a cross-regulatory input into alx1 (maintenance rather than
    initial activation)
    [PMID:18413610 "This gene is also a cross-regulatory target of the ets1 gene, among the initial double negative gate genes, and ets1 expression may lock itself on by autoactivation"]
    [PMID:20181745 "this gene is regulated by MAPK signaling and by the transcription factor Ets1; however, these inputs influence only the maintenance of alx1 expression and not its activation"].
  - tbr — the tbr distal cis-regulatory module carries positive Ets1/2 inputs;
    Ets1/2 MASO reduces the module's activity and ets1/2 mRNA drives it ectopically
    [PMID:19679118 "a dedicated distal module utilizing positive Ets1/2 inputs contributes to definitive expression in the skeletogenic mesenchyme"]
    [PMID:19679118 "both pmar mRNA and hesC MASO injection cause the ectopic expression of ets1/2, an activator of tbr"].
  - foxN2/3 — requires Ets1 (dominant-negative Ets1 blocks micromere expression;
    L. variegatus)
    [PMID:21303847 "Expression of dominant-negative Ets1 blocked foxN2/3 expression in the micromeres"].
- Outputs (differentiation genes): Ets1 is the most common "A driver" of the
  skeletogenic differentiation gene batteries
  [PMID:18413610 "the ets1 gene ( 9 ) is used in these gene batteries only as the A driver, and it is the most common of these"].
  Direct cis-regulatory evidence in S. purpuratus: the Sp-cyp1 218-bp module
  requires Ets1 target sites
  [PMID:16574094 "elimination of either Ets1 or Dri inputs severely depresses the activity of expression constructs containing this DNA fragment; and that Ets1 and Dri target sites within the 218 bp fragment are required for normal expression. This indicates that the predicted inputs are direct."].
  In Hemicentrotus the SM50 promoter has a functional ets site
  [PMID:10096062 "In the upstream region of the SM50 gene there exists an ets binding site that functions as a positive cis-regulatory element"].
  Genome-wide, Ets1 (with Alx1) has inputs into ~half of known PMC effector genes
  and Ets1 sites are enriched in PMC CRMs
  [PMID:24496631 "functional targets of Ets1 and Alx1, two pivotal, early transcription factors in the PMC GRN"]
  [PMID:29558892 "Binding sites for Ets1 and Alx1, two PMC-enriched transcription factors that have direct or indirect inputs into half of the known PMC effector genes in the PMC gene regulatory network [21], were found to be significantly enriched"].

## Loss- and gain-of-function phenotypes

- S. purpuratus ets1 MASO: skeleton-minus embryos and failure of PMC ingression
  [PMID:18413610 "interference with their expression produces a skeleton-minus phenotype, as illustrated in Fig. 3 B–G for tbr , hex , tgif , ets1 , and alx1"]
  [PMID:18413610 "both it and alx1 target genes are required for ingression of the skeletogenic cells (ref. 36 and Fig. 3 F and G )"].
- Gain of function converts non-PMC cells to PMC / mesenchymal fate:
  Hemicentrotus [PMID:10096062 "The overexpression of HpEts by mRNA injection into fertilized eggs alters the cell fate of non-PMC to migratory PMC"];
  P. lividus [PMID:14973284 "Overexpression of ets1 by injection of synthetic mRNA in the egg caused a dramatic increase in the number of cells becoming mesenchymal at the blastula stage"].
- Dominant-negative (N-terminally truncated) Ets blocks SM50 expression and
  spicule formation
  [PMID:10096062 "The overexpression of dominant negative delta HpEts which lacks the N terminal domain, in contrast, specifically represses SM50 expression and development of the spicule"].
- Summary statements: [PMID:16997294 "Functional analysis of Sp-Ets1/2 has previously demonstrated an essential role of this gene in the specification of the skeletogenic mesenchyme lineage"];
  [PMID:20680330 "In sea urchins, Ets1/2 plays a central role in the differentiation of larval skeletogenic mesenchyme cells"].

## Organism caveats

Functional papers span several euechinoids: S. purpuratus (Oliveri 2008,
Revilla-i-Domingo 2007, Amore & Davidson 2006, Wahl 2009, Rafiq 2014, Sharma &
Ettensohn 2010, Shashikant 2018), Hemicentrotus pulcherrimus (Kurokawa 1999,
Koga 2010), Paracentrotus lividus (Röttinger 2004) and Lytechinus variegatus
(Rho & McClay 2011). Non-S. purpuratus data are used as corroboration; the
S. purpuratus perturbation and cis-regulatory papers are the primary support.

## Not verified here

- A specific Ets1 + Tbr requirement for delta transcription is not stated in the
  cached texts (Oliveri 2008 places delta directly under the double-negative gate);
  not asserted in the review.
- No EMSA/ChIP with purified or tagged Sp-Ets1 is cached; sequence-specific
  cis-regulatory binding is inferred from required target sites and motif
  enrichment.
