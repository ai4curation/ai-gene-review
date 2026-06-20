# DNAJC19 (TIM14 / TIMM14) research notes

## Identity
- UniProt Q96DA6, TIM14_HUMAN, "Mitochondrial import inner membrane translocase subunit TIM14"; DnaJ homolog subfamily C member 19. 116 aa.
- HGNC:30528. Chromosome 3. Belongs to the TIM14 family.
- Topology: short intermembrane-space N-terminus (2-3), single transmembrane helix (4-24), then matrix-side J-domain (62-116). So a single-pass inner-membrane protein with its catalytic J-domain projecting into the matrix.

## Core function
- J-domain co-chaperone of the mitochondrial presequence translocase-associated import motor (PAM), the matrix-side motor of the TIM23 complex.
- Stimulates the ATPase activity of mitochondrial HSP70 (mortalin/HSPA9) to drive ATP-dependent import of presequence-bearing precursor proteins across the inner membrane into the matrix.
- [PMID:19564938 "J-domain containing proteins, DnaJs, usually enhance the ATPase activity of Hsp70 chaperones. Such enhancement of the ATPase activity is required for promoting the tight binding of unfolded substrate proteins to the peptide-binding pocket of mtHsp70. The latter role is played by the membrane-bound J-domain-containing protein named Tim14/Pam18"]
- Human DNAJC19 directly stimulates human mtHSP70 (Mortalin) ATPase activity; this is antagonized by Magmas/PAM16 [PMID:20053669 "we have observed upto 70% reduction in ATPase stimulating activity of human Mortalin by Magmas:DnaJC19 complex"].

## Partner / complex
- Forms a stable heterodimeric subcomplex with Magmas (PAM16/TIMM16) through their related J/J-like domains; this is the regulatory module of the import motor. Demonstrated in human mitochondria by reciprocal coIP.
- [PMID:20053669 "Magmas forms a stable subcomplex with J-protein Pam18 or DnaJC19 through its C-terminal region and is tethered to TIM23 complex of yeast and humans"]
- [PMID:20053669 "equivalent amounts of co-precipitation of Magmas with DnaJC19 (yPam18 ortholog) supports the existence of a similar subcomplex in humans"]
- Part of the human TIM23 translocon: co-IP with Tim17 pulls down hTim44, hTim23, DnaJC19, Magmas [PMID:20053669 "Pull down of Magmas along with other translocon components such as hTim44, hTim23, DnaJC19 provides direct evidence for the association of Magmas with the human translocon"].
- Human Tim14/Pam18 (DNAJC19) and human Tim16/Pam16 form hetero-oligomers and bind yeast mtHsp70 [PMID:19564938 "the soluble domains of the human Tim14/Pam18 and Tim16/Pam16 proteins interact with their yeast counterparts, forming heterodimeric complexes and that these complexes interact with yeast mtHsp70"].
- UniProt SUBUNIT: interacts with PHB2 (associates DNAJC19 with prohibitin complex) and with TIMM16/PAM16; may be component of PAM complex (mtHSP70, GRPEL1/2, TIMM44, TIMM16, TIMM14). (By similarity.)

## Localization
- Mitochondrion inner membrane, single-pass, matrix side [UniProt SUBCELLULAR LOCATION]. Confirmed in human heart mito proteome [PMID:12592411] and human mito proteome [PMID:34800366].

## Second function (cardiolipin)
- UniProt FUNCTION (by similarity): "forms a complex with prohibitins to regulate cardiolipin remodeling." Underlies the 3-methylglutaconic aciduria / DCMA phenotype (a cardiolipin/Barth-like syndrome). This is ISS/by-similarity, kept as non-core but plausible.

## Disease
- DCMA syndrome = dilated cardiomyopathy with ataxia = 3-methylglutaconic aciduria type 5 (MGCA5), autosomal recessive [PMID:16055927]. Also testicular dysgenesis (genitalia development), optic features. The IMP annotations to "genitalia development" and "visual perception" derive from the human disease phenotype description.

## Annotation review reasoning
- Core MF: GO:0001671 ATPase activator activity (stimulates mtHSP70) - ACCEPT, directly demonstrated for human protein.
- Core BP: GO:0030150 protein import into mitochondrial matrix - ACCEPT.
- Core CC: PAM complex (GO:0001405) and mitochondrial inner membrane / matrix side - ACCEPT.
- TIM23 translocase complex (GO:0005744) part_of - ACCEPT, human translocon coIP.
- Cardiolipin regulation (GO:1900208) ISS/IEA - KEEP_AS_NON_CORE (by similarity, disease-relevant but secondary).
- protein binding GO:0005515 IPI with Q9Y3D7 (=PAM16/Magmas) - KEEP_AS_NON_CORE (real interaction, uninformative term; informative is the J-domain/ATPase module).
- protein-containing complex GO:0032991 IDA - KEEP_AS_NON_CORE (generic, real but redundant with PAM/TIM23 complex).
- mitochondrion GO:0005739 IDA/HTP - ACCEPT (less specific than inner membrane but correct).
- membrane GO:0016020 NAS - KEEP_AS_NON_CORE (generic).
- intracellular protein transport GO:0006886 NAS - KEEP_AS_NON_CORE (generic parent of import into matrix).
- Note: genitalia development / visual perception IMP terms are in the DR/UniProt GO set but NOT in the GOA tsv stub, so not reviewed here.
