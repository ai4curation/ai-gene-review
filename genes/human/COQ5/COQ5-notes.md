# COQ5 (human) — gene review notes

UniProt: Q5HYK3 · HGNC:28722 · Chr 12 · 327 aa precursor (mature chain 43–327 after cleavage of an N-terminal mitochondrial transit peptide, residues 1–42).

## Summary of function

COQ5 is the mitochondrial **2-methoxy-6-polyprenyl-1,4-benzoquinol methylase** (EC 2.1.1.201), a Class I SAM-dependent methyltransferase of the MenG/UbiE family. It carries out the **sole C-methylation** step of the coenzyme Q (ubiquinone/CoQ10) head-group biosynthetic pathway, transferring a methyl group from S-adenosyl-L-methionine (SAM) onto the C2 position of the benzoquinol ring, producing S-adenosyl-L-homocysteine (SAH). In humans it converts 2-methoxy-6-(all-trans-decaprenyl)benzene-1,4-diol (DDMQ10H2) to 5-methoxy-2-methyl-3-(all-trans-decaprenyl)benzene-1,4-diol (DMQ10H2).

- UniProt RecName / EC: "2-methoxy-6-polyprenyl-1,4-benzoquinol methylase, mitochondrial ... EC=2.1.1.201" [file:human/COQ5/COQ5-uniprot.txt].
- Catalytic activity (UniProt): "Reaction=2-methoxy-6-(all-trans-decaprenyl)benzene-1,4-diol + S-adenosyl-L-methionine = 5-methoxy-2-methyl-3-(all-trans-decaprenyl)benzene-1,4-diol + S-adenosyl-L-homocysteine + H(+)" [file:human/COQ5/COQ5-uniprot.txt].
- "Coq5 catalyzes the only C-methylation involved in the biosynthesis of coenzyme Q (Q or ubiquinone) in humans and yeast Saccharomyces cerevisiae" [PMID:25152161 "catalyzes the only C-methylation involved in the biosynthesis of coenzyme Q"].
- In vitro reconstitution confirmed COQ5 performs the C2 methylation of substrate 4b using SAM (kcat 2.4 min⁻¹, KM 444 µM): "The remaining enzymatic steps include C2 methylation of 4b by COQ5 ... COQ5 was incubated overnight at 30 °C with SAM and its substrate, 4b; GC/MS analysis confirmed enzymatic activity and production of 5" [PMID:38425362].

## Pathway

Ubiquinone (coenzyme Q10) biosynthesis; UniPathway UPA00232; Reactome R-HSA-2142789 (Ubiquinol biosynthesis).
- UniProt: "PATHWAY: Cofactor biosynthesis; ubiquinone biosynthesis" [file:human/COQ5/COQ5-uniprot.txt].
- The head-group modification pathway is carried out by the COQ metabolon (COQ3, COQ4, COQ5, COQ6, COQ7, COQ9), assembled on the matrix side of the inner mitochondrial membrane [PMID:38425362 "a composite of COQ proteins bands together on the matrix side of the inner mitochondrial membrane to build the final aromatic ring of CoQ. These include COQ3, COQ4, COQ5, COQ6, COQ7 and COQ9"].

## Subcellular localization

Mitochondrial inner membrane, peripheral (extrinsic) membrane protein on the **matrix side**; also annotated as mitochondrial matrix.
- UniProt: "SUBCELLULAR LOCATION: Mitochondrion inner membrane ... Peripheral membrane protein ... Matrix side" [file:human/COQ5/COQ5-uniprot.txt].
- "the COQ5 polypeptide is associated with the mitochondrial inner membrane on the matrix side" [PMID:25152161 "associated with the mitochondrial inner membrane on the matrix side"].
- N-terminome / mass-spec studies confirm mitochondrial localization (PMID:25944712 in UniProt; HPA IDA GO:0005739; FlyBase HTP PMID:34800366).

## Complex / interactions (COQ synthome / COQ metabolon)

COQ5 is a component of the multi-subunit COQ enzyme complex (CoQ synthome), composed of at least COQ3, COQ4, COQ5, COQ6, COQ7 and COQ9.
- UniProt: "SUBUNIT: Component of a multi-subunit COQ enzyme complex, composed of at least COQ3, COQ4, COQ5, COQ6, COQ7 and COQ9 (PubMed:27499296). Interacts with PYURF; the interaction is direct, stabilizes COQ5 protein and associates PYURF with COQ enzyme complex (PubMed:35614220)" [file:human/COQ5/COQ5-uniprot.txt].
- IntAct binary interactions in UniProt: COQ3 (Q9NZJ6), COQ4 (Q9Y3A0), COQ6 (Q9Y2Z9), COQ7 (Q99807), COQ9 (O75208).
- PYURF is Q96I23 (IPI PMID:35614220 with:from UniProtKB:Q96I23).
- COQ4 co-IP: "immune-precipitation of COQ4-V5 captures COQ5-myc and vice versa, indicating that these COQ proteins physically associate in a complex in human cells" [PMID:25152161 "physically associate in a complex in human cells"].

## Family / domain

Class I-like SAM-binding methyltransferase superfamily; MenG/UbiE family. Pfam PF01209 (Ubie_methyltran); PROSITE PS51608 (SAM_MT_UBIE); InterPro IPR004033 (UbiE/COQ5_MeTrFase). SAM-binding residues (BINDING) at 117, 171, 199–200.
- UniProt: "SIMILARITY: Belongs to the class I-like SAM-binding methyltransferase superfamily. MenG/UbiE family" [file:human/COQ5/COQ5-uniprot.txt].

## Disease

Primary coenzyme Q10 deficiency, type 9 (COQ10D9; MIM:619028), autosomal recessive; cerebellar ataxia and static encephalomyopathy due to COQ5 C-methyltransferase deficiency [PMID:29044765 — Malicdan et al. 2018 Hum Mutat; not cached locally, cited from UniProt DISEASE section].
- UniProt: "DISEASE: Coenzyme Q10 deficiency, primary, 9 (COQ10D9) [MIM:619028]" [file:human/COQ5/COQ5-uniprot.txt].

## Tissue expression

Widely expressed; highest in liver, lung, placenta and skeletal muscle (UniProt TISSUE SPECIFICITY, PMID:25152161).

## Curation reasoning (for the review)

### Core molecular function
- **GO:0008425 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase activity** — the exact, specific MF. go.db definition matches the UniProt catalytic activity (SAM → SAH, C-methylation of benzoquinol). Supported experimentally (IDA PMID:25152161, IDA PMID:38425362) and by IBA/IEA/TAS. This is THE core function → ACCEPT the experimental IDA annotations; IBA/IEA/TAS to same term ACCEPT (redundant but correct).
- GO:0008168 methyltransferase activity (IEA, InterPro) — correct but a generic parent of GO:0008425 → MARK_AS_OVER_ANNOTATED (less informative than the specific term already present).

### Core biological process
- **GO:0006744 ubiquinone biosynthetic process** — core BP. Multiple experimental/phylogenetic supports (IGI PMID:25152161, IDA PMID:38425362, IBA). ACCEPT the strongest; keep others.
- GO:0032259 methylation (IDA PMID:25152161) — this is a generic BP grouping term; the specific ubiquinone-biosynthesis BP + the specific MF already capture the methylation. Keep but MARK_AS_OVER_ANNOTATED (redundant generic term). Note UniProt DR also carries GO:0032259 as P:methylation IDA.

### Cellular component
- **GO:0005759 mitochondrial matrix** (IDA PMID:25152161) — core location (matrix-side peripheral IM protein). ACCEPT experimental; Reactome TAS duplicates KEEP_AS_NON_CORE.
- GO:0005743 mitochondrial inner membrane — peripheral, matrix side. IDA (ComplexPortal PMID:27499296), EXP (PMID:35614220), colocalizes_with IDA (PMID:25152161) → ACCEPT/KEEP. IEA SubCell also correct.
- GO:0031314 extrinsic component of mitochondrial inner membrane (IEA UniRule) — precise and consistent with "peripheral membrane protein, matrix side"; ACCEPT (informative CC).
- GO:0005739 mitochondrion — correct but least specific CC; HPA IDA and FlyBase HTP → KEEP_AS_NON_CORE (parent of matrix/IM).
- **GO:0110142 ubiquinone biosynthesis complex** (IPI PMID:27499296, ComplexPortal) — the COQ synthome; part_of. ACCEPT (core, matches SUBUNIT).
- GO:0032991 protein-containing complex (IDA PMID:25152161) — generic parent of GO:0110142 → MARK_AS_OVER_ANNOTATED.

### Protein binding (GO:0005515) IPI
Five IntAct IPIs (PMID:27499296: COQ9 O75208, COQ7 Q99807, COQ3 Q9NZJ6, COQ6 Q9Y2Z9, COQ4 Q9Y3A0) + PMID:35614220 (PYURF Q96I23) + PMID:25152161 (COQ4 Q9Y3A0). All are bona fide COQ synthome / PYURF interactions but "protein binding" is uninformative → MARK_AS_OVER_ANNOTATED each (per policy, never REMOVE an IPI protein binding). The interactions are better captured by GO:0110142 part_of and by core MF.

### Reactome TAS (matrix + reaction terms)
Multiple Reactome TAS to GO:0005759 (matrix) and to GO:0008425 / GO:0006744. The reaction-specific ones (R-HSA-2162188 "COQ5 methylates MDMQ10H2") are correctly COQ5's step; others (R-HSA-2162186 COQ3, -2162187 COQ6, -2162193 COQ3, -2162194 COQ7:COQ9, -2162195 COQ4) are other pathway steps but Reactome co-annotates all synthome members to the matrix location. TAS location annotations: KEEP_AS_NON_CORE (correct location, non-experimental, redundant with IDA matrix). The R-HSA-2162188 GO:0008425 TAS is directly COQ5 → ACCEPT.
