# HSD17B12 (Q53GQ0) review notes

## Summary of identity and core function

HSD17B12 / SDR12C1, historically "17-beta-hydroxysteroid dehydrogenase 12" and better known biochemically as **3-ketoacyl-CoA reductase (KAR)**, is an endoplasmic-reticulum membrane, NADPH-dependent short-chain dehydrogenase/reductase (SDR) that catalyzes the **second of the four reactions of the microsomal fatty-acid elongation cycle**: reduction of the 3-ketoacyl-CoA (3-oxoacyl-CoA) produced by the ELOVL condensing enzymes to (3R)-3-hydroxyacyl-CoA. It is the sole/main KAR of the long- and very-long-chain fatty-acid (VLCFA) elongation machinery.

- UniProt RecName is **"Very-long-chain 3-oxoacyl-CoA reductase"** with EC 1.1.1.330 [file:human/HSD17B12/HSD17B12-uniprot.txt "RecName: Full=Very-long-chain 3-oxoacyl-CoA reductase"; "EC=1.1.1.330"].
- FUNCTION: "Catalyzes the second of the four reactions of the long-chain fatty acids elongation cycle." and "This enzyme has a 3-ketoacyl-CoA reductase activity, reducing 3-ketoacyl-CoA to 3-hydroxyacyl-CoA, within each cycle of fatty acid elongation." [file:human/HSD17B12/HSD17B12-uniprot.txt].
- Catalytic activity (canonical): "a very-long-chain (3R)-3-hydroxyacyl-CoA + NADP(+) = a very-long-chain 3-oxoacyl-CoA + NADPH + H(+)"; EC 1.1.1.330 [file:human/HSD17B12/HSD17B12-uniprot.txt]. UniProt additionally lists specific-substrate Rhea reactions for 3-oxooctadecanoyl-CoA and several polyunsaturated 3-oxoacyl-CoAs (docosatetraenoyl-, docosapentaenoyl-, eicosatrienoyl-CoA), supporting a role in supply of VLCFA/arachidonate-derived acyl chains.

## Subcellular location and topology

- ER membrane, multi-pass: "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane ... Multi-pass membrane protein" [file:human/HSD17B12/HSD17B12-uniprot.txt]. Three predicted TM helices (4-24, 182-202, 271-291) and a C-terminal di-lysine motif (308-312) conferring ER retention [file:human/HSD17B12/HSD17B12-uniprot.txt].

## Cofactor / active site

- NADP(+)-binding region BINDING 50..79 [file:human/HSD17B12/HSD17B12-uniprot.txt]. Keyword: NADP. Active-site Tyr202 (proton acceptor, SDR catalytic residue). Hence NADP binding (GO:0050661) is the appropriate cofactor MF.

## Key primary literature

- **Moon & Horton 2003 (PMID:12482854)** — identified the mammalian 3-ketoacyl-CoA reductase and 2,3-trans-enoyl-CoA reductase of microsomal fatty-acyl elongation. Abstract: "Here, we report the identification and characterization of two mammalian enzymes that catalyze the 3-ketoacyl-CoA and trans-2,3-enoyl-CoA reduction reactions in long and very long chain fatty acid elongation, respectively." Basis for the FUNCTION, CATALYTIC ACTIVITY (EC 1.1.1.330), PATHWAY (fatty-acid biosynthesis), and ER location assertions in UniProt. Abstract-only in cache; full text read by the original curators (EXP/IDA annotations). [PMID:12482854]

- **Luu-The, Tremblay & Labrie 2006 (PMID:16166196)** — characterized "type 12 17beta-HSD" as an enzyme that "transforms estrone (E1) into estradiol (E2)"; "the enzyme catalyzes selectively and efficiently the transformation of E1 into E2, thus identifying its role in estrogen formation"; F234 mutagenesis. Basis for the estradiol 17-beta-dehydrogenase (EC 1.1.1.62 / GO:0004303) EXP annotation and estrogen-biosynthesis process. This is the historical steroidogenic characterization; it is a genuine measured activity in a heterologous overexpression system but is NOT the primary physiological role (see below). [PMID:16166196]

- **Naganuma & Kihara 2014 (PMID:25003994)** — full text available. Biochemical dissection of KAR (=HSD17B12) with the elongase ELOVL6 in proteoliposomes. "The second step is catalyzed by 3-ketoacyl-CoA reductase (KAR), which reduces 3-ketoacyl-CoA to 3-hydroxyacyl-CoA using NADPH as a cofactor". KAR stimulates ELOVL6 both enzyme-activity-independently (direct interaction / conformational change) and enzyme-activity-dependently (product release from a "presumed ELOVL6-KAR complex"). Basis for the IDA annotations to VLC 3-oxoacyl-CoA reductase activity (GO:0141040), fatty acid elongation saturated fatty acid (GO:0019367), and fatty acid elongase complex (GO:0009923). [PMID:25003994]

- **Ohno et al. 2010 (PMID:20937905)** — "ELOVL1 production of C24 acyl-CoAs is linked to C24 sphingolipid synthesis." UniProt SUBUNIT: "Interacts with ELOVL1 and LASS2 (=CERS2)." Abstract-only in cache (does not name KAR/HSD17B12 in the abstract) but underpins the IPI physical-interaction annotations linking KAR to the ELOVL1/CERS2 elongation-sphingolipid machinery. [PMID:20937905]

## Steroid vs fatty-acid activity — interpretation

HSD17B12 is a classic case of a mis-leading historical name. It was cloned/named as a 17beta-HSD (estradiol dehydrogenase) [PMID:16166196], and the estradiol 17-beta-dehydrogenase [NAD(P)+] activity (GO:0004303, EC 1.1.1.62) is a real, experimentally measured activity in a heterologous overexpression system. However, the enzyme's **physiological substrate is fatty-acyl-CoA**, and its established biological role is the KAR step of VLCFA elongation (UniProt RecName; PMID:12482854; PMID:25003994). VLCFA-elongation phenotypes in model organisms (yeast Ybr159w, Drosophila sc2) and the retention of the KAR step across eukaryotes support this as the core function. I therefore treat:
- KAR / VLC 3-oxoacyl-CoA reductase (GO:0141040) + NADP binding + ER membrane + fatty-acid elongation as **CORE**.
- estradiol 17-beta-dehydrogenase activity (GO:0004303) and estrogen biosynthetic process (GO:0006703) as **KEEP_AS_NON_CORE** (EXP-supported for GO:0004303; retain but not core) or over-annotated (for the electronic estrogen-pathway / androgen / testosterone-dehydrogenase mappings), never REMOVE where experimental.

## Annotation-specific notes

- **GO:0018454 acetoacetyl-CoA reductase activity (IEA, RHEA GO_REF:0000116)** — this Rhea-mapping IEA is a *less-precise / arguably wrong-branch* label: the mapped Rhea reactions (RHEA:39151/39311/39323/39459) are the very-long-chain 3-oxoacyl-CoA reductions (C18 and PUFA 3-oxoacyl-CoAs), i.e. exactly the KAR reaction, not the short-chain acetoacetyl-CoA (C4) reductase (poly-hydroxybutyrate/PHB-type) activity. GO:0141040 already captures this precisely with experimental support. Marked MODIFY -> GO:0141040 (the IEA over-generalizes to a bacterial-flavored acetoacetyl-CoA reductase term).
- **GO:0016491 oxidoreductase activity (IBA)** and **GO:0016614 oxidoreductase activity, acting on CH-OH group of donors (IEA)** — correct but far too general; the specific GO:0141040 is available. MARK_AS_OVER_ANNOTATED (parent terms of the specific activity).
- **GO:0005515 protein binding (IPI, x9)** — bare "protein binding"; uninformative per curation policy. The ELOVL1/CERS2 (PMID:20937905) interactions are biologically meaningful (elongase machinery) but the term itself is uninformative; the high-throughput interactome hits (HCV screen PMID:24169621; HuRI PMID:32296183, 25416956; neurodegeneration interactome PMID:32814053; RTK interactome PMID:35384245; UBQLN1/2, HRAS, GSN, FGFR3, CHAT) are non-functional. All MARK_AS_OVER_ANNOTATED per policy (never REMOVE an IPI protein-binding).
- **GO:0031012 extracellular matrix; GO:0005518 collagen binding; GO:0001968 fibronectin binding; GO:0008201 heparin binding; GO:0047045 testosterone dehydrogenase (NADP+) activity; GO:0006702 androgen biosynthetic process** — these appear only in the UniProt DR GO block as Ensembl-projected IEA and are NOT present in the GOA TSV, so they are not in the review set. They would be spurious for an ER-membrane KAR (ECM/collagen/fibronectin/heparin) or paralog-projected (testosterone/androgen from HSD17B3 family). Noted for completeness only.
</content>
</invoke>
