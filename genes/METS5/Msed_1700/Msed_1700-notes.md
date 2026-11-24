# Msed_1700 (A4YHF3): curation notes

*Metallosphaera sedula* DSM 5348. UniProt A4YHF3 is an unreviewed TrEMBL entry, 348 aa.
UniProt (via ARBA00067001) names it "malonyl CoA reductase (malonate semialdehyde-forming),
EC 1.2.1.75". This review concludes that it is the aspartate-semialdehyde dehydrogenase
(ASD, EC 1.2.1.11) of *M. sedula*. ARCHAEA project gene, reviewed alongside the MCR
paralog Msed_0709.

**Provenance note.** Automated deep research was unavailable in this session because the
provider API keys failed. No `-deep-research-*.md` file was created. The literature work
used NCBI E-utilities, the cached publications, the PMC article page, and UniProt and NCBI
REST queries (2026-10-15).

## Experimental evidence for this protein: none

- No publication reports cloning, expression, purification or assay of Msed_1700. A PubMed
  search for "Msed_1700" returns nothing. A search for M. sedula ASD returns only the two
  MCR papers (PMID:17041055, PMID:19684143).
- **Alber et al. 2006 (PMID:17041055).** The cached copy is abstract-only. I read the
  full text on the PMC page (PMC1698253) through a summarizing fetch, so the wording below
  is not quoted from a cached file. The paper partially purified MCR from *M. sedula*
  extracts, then cloned and expressed only the *S. tokodaii* MCR gene. The *M. sedula*
  genome was not yet available. The authors identified a second *S. tokodaii* ORF
  (NP_377174, 38% identical to MCR) as the true asd, "because it is located on a gene
  cluster together with aspartokinase and threonine synthase". That ORF was not
  expressed or assayed. Msed_1700 itself is not discussed.
  Abstract: [PMID:17041055 "Malonyl-CoA reductase has 38% amino acid sequence identity to aspartate-semialdehyde dehydrogenase, suggesting a common ancestor for both proteins."]
  - NP_377174 is the *S. tokodaii* ST1242 / STK_12420 protein (Q971Y6). Its NCBI GenPept
    record has locus_tag ST1242. A RIKEN structural-genomics structure exists for it
    (PDB 2EP5) but has no publication.
- **Kockelkorn & Fuchs 2009 (PMID:19684143).** Full text is cached. Peptide mass
  fingerprinting of the succinyl-CoA reductase matched only Msed_0709:
  [PMID:19684143 "The only hit was with the gene gi|146303492 (100% identity, 54% coverage) annotated as an aspartate-semialdehyde dehydrogenase gene coding for a 39.2-kDa protein (Msed_0709; 357 amino acids)."]
  The paper does not mention Msed_1700. It discusses the duplication only in general terms:
  [PMID:19684143 "A phylogenetic tree of the gene ( 1 , 9 ) suggests that there was duplication of the aspartate semialdehyde dehydrogenase gene in the ancestor of the Sulfolobales and that there was independent evolution of the two genes to perform different functions."]
- Neither paper tested Msed_1700 directly. The only *M. sedula* protein assigned to
  malonyl-CoA (and succinyl-CoA) reduction is Msed_0709. Every judgment below therefore
  rests on genomic context, sequence signatures, and comparison with the paralog and with
  characterised archaeal ASDs.

## Genomic context (UniProt REST, organism 399549)

- Msed_1697: 3-octaprenyl-4-hydroxybenzoate decarboxylase
- **Msed_1698 (A4YHF1): threonine synthase, EC 4.2.3.1 (TIGR00260)**
- **Msed_1699 (A4YHF2): aspartokinase, EC 2.7.2.4 (TIGR00657)**
- **Msed_1700 (A4YHF3): this gene**
- Msed_1701: PHP-domain protein

This is the asd context described for Sulfolobales:
[PMID:23325803 "The asd gene clusters together with threonine synthase, aspartokinase, and ornithine carbamoyltransferase, among other genes, which is in line with its role in the biosynthesis of amino acids of the aspartate family."]
By contrast, the mcr gene has no conserved neighbours:
[PMID:23325803 "The mcr gene occurs only in autotrophic Sulfolobales underlining its role in the carbon fixation cycle and its neighbor genes are generally not conserved among different species."]
Aspartokinase makes 4-phospho-L-aspartate, the ASD substrate. ASD turns it into
L-aspartate 4-semialdehyde, which leads via homoserine to threonine (threonine synthase).
Sulfolobales make lysine by the alpha-aminoadipate/LysW route; the *M. sedula* LysW-pathway
reductase Msed_0164 is a different family. So the aspartate-semialdehyde branch here
mainly serves homoserine, threonine and methionine.

## Sequence signatures (UniProt file)

- Family: "Belongs to the aspartate-semialdehyde dehydrogenase family."
- CDD: cd18130 ASADH_C_arch_fung_like and cd02315 ScASADH_like_N, which are the
  archaeal/fungal ASD models. Msed_0709 instead has cd23940 ASADH_C_MCR and cd24150
  ASADH_MCR_N.
- NCBIfam TIGR00978 asd_EA and NF006416 PRK08664; PIRSF000148 ASA_dh; PANTHER
  PTHR46718:SF1; FunFam 3.40.50.720:FF:000411.
- Active-site features: ACT_SITE 150, "Acyl-thioester intermediate"; ACT_SITE 242,
  "Proton acceptor" (PIRSR). These are the catalytic Cys and His of the family.

**Correction to the Msed_0709 notes and review.** They say TIGR00978 is found on
Msed_1700 but not on Msed_0709. In current UniProt, A4YEN2 (Msed_0709, entry version 101)
**also** carries TIGR00978 and NF006416 (checked in the local `Msed_0709-uniprot.txt` and
on live REST). TIGR00978 does not separate the paralogs, so it is not a usable negative
condition for the ARBA rule. The **CDD subfamily models do** separate them. The
annotation-patterns catalogue (entry 1, "Possible fix") repeats the TIGR00978
suggestion. I have reported this but not edited those files, which belong to the other
gene and the project.

## Bioinformatics (Msed_1700-bioinformatics/)

`compare_asd_mcr.py` makes live UniProt calls; the results are in `RESULTS.md` and
`results.txt`.

- Identity of Msed_1700 to the *S. tokodaii* asd ST1242 (Q971Y6) is 69.0%. To the
  M. jannaschii ASD it is 44.3%. To the MCRs it is only 38.8% (Msed_0709) and 40.5%
  (S. tokodaii MCR). Msed_1700 is therefore the ortholog of the asd gene that Alber et al.
  assigned by context.
- The catalytic Cys150 and His242 align with MCR Cys153 and His248, the family
  nucleophile and acid/base. Every member conserves these residues, so they say nothing
  about substrate.
- ARBA reach: 40 archaeal UniProt entries are named EC 1.2.1.75. Of these, 19 carry
  MCR-type CDD models, 17 carry ASD-type models (including Msed_1700 and ST1242), and 4
  carry neither. The rule's only conditions are FunFam 3.40.50.720:FF:000411 and taxon
  Archaea (ARBA REST: 38 unreviewed hits, 0 reviewed). The rule cannot tell the paralogs
  apart, so about half of its hits are probably misnamed ASDs. The same FunFam is itself
  named "Aspartate-semialdehyde dehydrogenase".

## Archaeal ASD biochemistry (by homology)

- M. jannaschii ASD (archaeal/fungal branch) keeps all the active-site residues and uses
  both NAD and NADP:
  [PMID:16225889 "However, the entire repertoire of functionally important active site amino acid residues is conserved, suggesting an identical catalytic mechanism but with lower catalytic efficiency."]
  [PMID:16225889 "A new coenzyme-binding conformation and dual NAD/NADP coenzyme specificity further distinguish this archaeal branch from the bacterial ASADHs."]
  [PMID:23325803 "This difference rationalizes its dual specificity for NADPH and NADH as electron donor, albeit still with a clear preference for NADPH ( 18 )."]
  Whether *M. sedula* ASD also uses NADH is unknown.
- Oligomeric state: ASDs of the archaeal/fungal branch are dimers of dimers (tetramers):
  [PMID:26869335 "Further, our structural analyses and native PAGE results with other fungal ASADHs demonstrated that ASADH tetramerization is universal in the archaeal/fungal branch."]
  [PMID:26869335 "Crystal packing analysis was performed for the structures of caASADH and mjASADH, which also identified the presence of GAPDH-like homotetramers in each of these structures."]

## Annotation decisions (summary)

All 7 GOA rows are IEA (2 TreeGrafter, 5 InterPro2GO).

- GO:0004073 ASD (NADP+) activity (TreeGrafter): **ACCEPT**. The core activity, inferred
  from context, orthology and signatures.
- GO:0009088 L-threonine biosynthetic process (TreeGrafter): **ACCEPT**. Aspartokinase
  and threonine synthase genes are adjacent.
- GO:0008652 amino acid biosynthetic process (InterPro2GO): **MODIFY** to GO:0009088.
  The term is correct but general.
- GO:0016620 aldehyde/oxo oxidoreductase, NAD(P) acceptor: **MODIFY** to GO:0004073
  (correct parent).
- GO:0050661 NADP binding: **KEEP_AS_NON_CORE**. This is the cofactor of the reaction
  defined by GO:0004073.
- GO:0051287 NAD binding: **UNDECIDED**. M. jannaschii ASD is dual-specific, but there are
  no data for this enzyme. A REMOVE would not be justified, as it was for the
  NADPH-specific MCR.
- GO:0046983 protein dimerization activity: **KEEP_AS_NON_CORE**. Archaeal/fungal ASDs
  are dimers of dimers.
- **ARBA naming is wrong:** the "malonyl CoA reductase, EC 1.2.1.75" RecName and the
  CATALYTIC ACTIVITY line (ARBA00052213) should be replaced. No GO row derives from them,
  so the error is in UniProt naming only. It could leak into GO if an EC2GO mapping for
  1.2.1.75 is ever created.

## Open questions

- Has Msed_1700 lost any malonyl-CoA reductase activity? No one has assayed it. The
  low-level ASD/MCR cross-activity of the paralogs is unknown.
- Does it use NADH as well as NADPH, like the M. jannaschii enzyme?

## Rule reviews (2026-10-15)

The ARBA naming and catalytic-activity rules that misannotate this protein now have
structured reviews: `rules/arba/ARBA00067001/ARBA00067001-review.yaml` and
`rules/arba/ARBA00052213/ARBA00052213-review.yaml` (both MODIFY). Across all 38 archaeal
entries the rules annotate, 17 are ASD-type like Msed_1700 (see
`rules/arba/ARBA00067001/RESULTS.md`).

