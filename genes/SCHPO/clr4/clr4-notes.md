# clr4 (Cryptic loci regulator 4 / Kmt1) — S. pombe — Curation Notes

UniProt: O60016 (CLR4_SCHPO). PomBase SPBC428.08c. 490 aa. Synonym kmt1.
EC 2.1.1.355 (H3K9 trimethyl), 2.1.1.366 (H3K9me2), 2.1.1.367 (H3K9 monomethyl), plus protein-lysine activities.

## Core identity
Clr4 is the SOLE histone H3 lysine 9 (H3K9) methyltransferase of fission yeast and the catalytic
subunit of the CLRC (Clr4 methyltransferase complex). It is the homolog of metazoan SUV39H1/2 and
Drosophila Su(var)3-9. Domain architecture: N-terminal chromodomain (8–69), disordered linker,
pre-SET (258–325), SET (328–452), post-SET (473–489).

- [PMID:11283354 "We provide in vivo evidence that lysine 9 of histone H3 (H3 Lys9) is preferentially methylated by the Clr4 protein at heterochromatin-associated regions in fission yeast. Both the conserved chromo- and SET domains of Clr4 are required for H3 Lys9 methylation in vivo."]
- [PMID:10949293 "human SUV39H1 and murine Suv39h1--mammalian homologues of Drosophila Su(var)3-9 and of Schizosaccharomyces pombe clr4--encode histone H3-specific methyltransferases that selectively methylate lysine 9 of the amino terminus of histone H3 in vitro. We mapped the catalytic motif to the evolutionarily conserved SET domain, which requires adjacent cysteine-rich regions to confer histone methyltransferase activity."]
- [PMID:24449894 "Cryptic loci regulator 4 (Clr4), the only known H3K9 methyltransferase in this organism, is a subunit of the Clr4 methyltransferase complex (CLRC)"]
- [PMID:34524082 "Clr4 is the sole H3K9me2/3 methyltransferase in the fission yeast Schizosaccharomyces pombe"]

## Catalytic activity / methylation states
Catalyzes H3K9 mono-, di-, and trimethylation. Also methylates non-histone substrates (Mlo3 and
others) — "protein-lysine N-methyltransferase activity".
- [PMID:28143796 "the catalytic activity of the protein lysine methyltransferase (PKMT) Clr4, the sole homolog of the mammalian SUV39H1 and SUV39H2 enzymes, majorly contributes to the formation of heterochromatin. The enzyme introduces histone 3 lysine 9 (H3K9) di- and tri-methylation, a central heterochromatic histone modification, and later it was also found to methylate the Mlo3 protein"]
- [PMID:28143796 "Peptide methylation was observed on Mlo3 and 7 novel target sites"]

## Reader/writer (chromodomain)
The chromodomain reads H3K9me; together with the SET writer it gives a read-write feedback that
spreads/maintains heterochromatin.
- [PMID:18345014 "the chromodomain of Clr4 binds specifically to H3K9me that is essential for the spreading of heterochromatin... the ability of Clr4 to both 'write' and 'read' H3K9me facilitates heterochromatin maintenance through successive cell divisions."]
- [PMID:31165882 "the Clr4 chromodomain binds the H3K9me3 tail and that both, the chromodomain and the disordered region connecting the chromodomain and the SET domain, bind the nucleosome core... contributes to H3K9me in vitro and in vivo."]

## CLRC complex (E3 ligase / methyltransferase)
Clr4 + Rik1 + Cul4(Pcu4) + Raf1/Dos1 + Raf2/Dos2 + Rbx1/Pip1; resembles a CRL4 cullin-RING ligase.
Preferred ub substrate is H3K14 (H3K14ub), which stimulates Clr4 H3K9 methylation.
- [PMID:16127433 "We show that Clr4 associates with Cul4, a cullin family protein that serves as a scaffold for assembling ubiquitin ligases. Mutations in Cul4 result in defective localization of Clr4 and loss of silencing at heterochromatic loci."]
- [PMID:16024659 "the Rik1 protein functions with the Clr4 histone methyltransferase at an early step in heterochromatin formation... subunits of a cullin-dependent E3 ubiquitin ligase are associated with Rik1 and Clr4"]
- [PMID:31468675 "CLRC-dependent H3 ubiquitylation regulates Clr4's methyltransferase activity"]
- [PMID:34524082 "the H3K14ub substrate binds specifically and tightly to the catalytic domain of Clr4, and thereby stimulates the enzyme by over 250-fold... identified a ubiquitin binding region (UBR) in the catalytic domain of Clr4"]
- [PMID:34010645 "This selective sequestration of Clr4 depends not only on H3K9M but also on H3K14 ubiquitylation (H3K14ub), a modification deposited by a Clr4-associated E3 ubiquitin ligase complex."]

## Autoregulation (automethylation)
An internal autoregulatory loop autoinhibits the SET pocket; automethylation of Lys455 switches it on.
- [PMID:30051891 "we reveal an autoinhibited conformation in the conserved H3K9 methyltransferase Clr4 (also known as Suv39h)... an internal loop in Clr4 inhibits the catalytic activity of this enzyme"]
- IDR also regulates activity: [PMID:40923761 "The N-terminus of Clr4 interacts with its C-terminal catalytic domain and represses its enzymatic activity... basic amino acid residues in the IDR are involved in this interaction."]

## Biological processes (silencing / heterochromatin)
H3K9me recruits Swi6/HP1 -> silencing at centromeres, telomeres, mating-type locus, rDNA.
- Mating-type silencing: [PMID:8001791 "the transcription and recombination blocks require three newly defined trans-acting loci, clr2, clr3 and clr4"]
- Pericentric/silencing via RNAi self-enforcing loop: [PMID:15615848 "its localization at centromeric repeats depends on components of RITS and Dicer as well as heterochromatin assembly factors including Clr4/Suv39h and Swi6/HP1 proteins"]
- Co-transcriptional gene silencing / RNA turnover: [PMID:17512405 "the RNAi pathway is required for heterochromatin-dependent silencing... Clr4 promoting H3K9 methylation and heterochromatin formation"] (Clr4 IMP for GO:0033562)
- Facultative heterochromatin islands at meiotic genes: [PMID:22144463 "RNA elimination machinery is enriched at meiotic loci and interacts with Clr4/SUV39h, a methyltransferase involved in heterochromatin assembly."]
- Subtelomeric: [PMID:24240238 deletion of shelterin restores pericentric heterochromatin in RNAi mutants — Clr4 IMP for subtelomeric formation] ; [PMID:32269268 "Abo1 in stabilising directly or indirectly Clr4 recruitment to allow the H3K9me2 to H3K9me3 transition in heterochromatin."]
- siRNA processing/antisense suppression via Mlo3: [PMID:21436456 "Clr4 and the RNAi effector RITS... interact with Mlo3... required for centromeric siRNA production and antisense suppression."]

## Localization
Nucleus; active in pericentric, mating-type, subtelomeric heterochromatin. SPB localization from a
single high-throughput GFP study (16823372) — weak/likely non-core; nucleus is the functional site.
- [PMID:16823372 global GFP localization study] ; [PMID:18345014 ClrC components distributed throughout heterochromatic domains]

## DNA/RNA/nucleosome binding
PMID:22727667 is actually about the Chp1 chromodomain, not Clr4 — the dsDNA/ssDNA/ssRNA binding IDA
annotations attributed to clr4 from this paper look mis-attributed/over-annotated (paper title and
abstract concern Chp1). Treat with caution. Nucleosome binding (31165882) is genuine and core-relevant.
ssRNA binding ARBA IEA is generic.

## Stc1 interaction (GO:0005515 IPI, PMID:20211136)
Stc1 links RNAi (Ago1) to CLRC; bridges RITS to Clr4 complex. Adapter/recruitment interaction.
- [PMID:20211136 "Stc1, that is required for centromeric heterochromatin integrity... interacts both with the RNAi effector Ago1, and with the chromatin-modifying CLRC complex... recruits CLRC, thereby coupling RNAi to chromatin modification."]

## Summary of action plan
- Core MF: histone H3K9 methyltransferase (mono/di/tri) — ACCEPT specific terms; generalize generic
  "methyltransferase activity" and "histone methyltransferase activity".
- Core MF: H3K9me reader / chromodomain (GO:0062072) — ACCEPT.
- Core BP: heterochromatin formation at pericentric, subtelomeric, mating-type; RNAi-related — ACCEPT/KEEP.
- protein binding (GO:0005515) bare terms — replace/mark; capture as complex membership / adapter.
- DNA binding IEA, ssRNA IEA, zinc IEA — keep_as_non_core / accept low-value structural.
- SPB localization — KEEP_AS_NON_CORE (single HTP study).
- 22727667 DNA/RNA binding IDA — likely mis-attributed (paper is about Chp1) -> MARK_AS_OVER_ANNOTATED / UNDECIDED.
