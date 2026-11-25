# XccOpgD identity and primary assay scope

Q8P3C6 is XCC4145/opgD of Xanthomonas campestris pv. campestris ATCC 33913 (taxon 190485). Official RCSB 8X18 entity1 identifies this source strain and a BL21(DE3) expression host; deposited sequence equals the frozen 533-residue precursor except D379N and the C-terminal LEHHHHHH extension. The accompanying script verifies this exact comparison. PDB metadata describes a precursor sequence and does not establish that the signal peptide was retained experimentally.

The genuine ACS supporting information was downloaded from Figshare article26062998, DOI10.1021/jacs.4c02579.s001 (file47133267), and independently from the EuropePMC PMC11228985 supplementaryFiles ZIP. The PDFs are byte-identical: SHA256 410c83b9c3f422807877d272bdf062b81db1cf7239213704f1a8090627507eb0. Full PDF and extracted text remain in ignored cache; only these scoped facts/excerpts and identity proof are retained here. Tables S3/S4 were visually checked on PDF pages14/15.

Table S3, selected entries (units U/mg; relative percent): wild-type 0.29,100; D379N ND,ND. The source states: “All specific activities were measured using 0.1 mM linear β-1,2-glucan as the substrate.” ND is explicitly below0.00029U/mg (below0.1% relative activity); it is not absolute zero. This is cyclization-product activity, not hydrolysis.

Table S4 wild-type forward primer, joined over the printed line wrap:
`actttaagaaggagatatacatatggccaaggcagtggggctgcgtcgc`

Exact source clause: “The forward primer for wild-type was designed to eliminate the N-terminal signal sequence predicted”. Translation after the NdeI start is MAKAVGLRR, corresponding to an added initiation methionine followed by Q8P3C6 residues29 onward. The paper describes C-terminal His6. Thus the wild-type assay is a tagged, signal-deleted recombinant enzyme, not the D379N crystal or a native localization assay. The exact physiological Tat-cleavage site is predicted, not experimentally established.

Main primary PMID38957137 identifies the dominant product using ESI-MS and NMR as a cyclic16-glucose chain with fifteen beta1,2 bonds and one alpha1,6 bond. NoteS3 identifies putative DP32/48 peaks as aggregates of the purified DP16 product; a very weak possible DP17 peak was insufficient for confirmation. No alternative major product or whole-family hydrolase function should be inferred. The paper demonstrates intrinsic cyclization chemistry; it does not provide a native XCC4145 deletion/rescue or prove that every GH186/OpgD homolog makes this product.

Official QuickGO searches for glucohexadecaose, glucan cyclase and transglycosylase did not establish an exact matching activity term. GO0033913 names hydrolysis and is inappropriate for this cyclization; generic glycosyltransferase GO0016757 does not capture substrate, stereochemistry or DP16 specificity. The proposed term in the review records that missing specificity without inventing a GO identifier.

The original IBA node PTN001253664 asserts periplasmic location (seed P40120) and beta-glucan biosynthesis (seed P33136). These are ancestral role claims, not direct assignments of E. coli hydrolase chemistry. The normal PAINT-loss check found no IRD/IKR on the target lineage. Target product chemistry supports OPG biosynthetic participation despite changed linkage mechanism; Tat-like signal plus curated periplasmic inference support location, not direct experimental localization.
