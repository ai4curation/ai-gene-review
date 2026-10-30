# CSN5 review notes

The selected PB protein differs from reviewed PA by two residues beyond the MPN/JAMM region. [PMID:12183637](https://pubmed.ncbi.nlm.nih.gov/12183637/) directly tests the JAMM motif and links it to cullin deneddylation. This supports the catalytic role within COP9, represented with contributes_to_molecular_function. No autonomous CSN5 protease activity is asserted. Neuronal developmental effects do not establish the external synaptic-vesicle claim, which remains UNC. Three seeded annotations are reviewed; exact prediction metadata are retained.

## Provider research assessment

The completed Falcon synthesis was inspected. Its interpretation of cullin deneddylation within COP9 agrees with the conserved MPN/JAMM analysis and PMID:12183637. Nuclear enrichment in fly immune cells and cullin-dependent neuronal branching provide context, but neither establishes a synaptic-vesicle location. The core function remains complex-dependent deNEDDylation; neuronal phenotypes do not identify an additional direct protease substrate.

COP9 membership is proposed as NEW with ISS for exact PB, supported by the primary eight-subunit isolation study PMID:10531038 and same-gene sequence conservation. This is the biological context for the deneddylase contribution.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 files were opened or used.

**Identity.** A0A0B4KHM2 is the unreviewed TrEMBL entry for FlyBase CSN5-PB (FBpp0306602, transcript CSN5-RB FBtr0334535, NP_001262639; 325 aa, PE 3). It is an alternative isoform of the same gene as the reviewed canonical Swiss-Prot entry Q9XZ58 (CSN5-PA, FBpp0082743, 327 aa). The existing alignment (CSN5-bioinformatics/results/results.json) gives 325/325 identical aligned residues. PB lacks only Gly278-Arg279, which lie outside the MPN domain (52-189). The JAMM motif (135-148) and the metal ligands His135, His137 and Asp148 are retained. It is neither a fragment nor a broken gene model; no domain or catalytic residue is lost.

**Evolutionary grounding.** Both accessions are in PANTHER PTHR10410. InterPro does not report a subfamily for either accession. The PANTHER subfamily named for this protein is PTHR10410:SF6, "COP9 SIGNALOSOME COMPLEX SUBUNIT 5", but I could not confirm the assignment programmatically, so I do not assert it in the review. QuickGO IBA rows on Q9XZ58 identify the PAINT node: PTN000045369, the CSN5 clade, which propagates COP9 signalosome, deNEDDylase activity, cytoplasm (is_active_in) and regulation of cell cycle. A deeper node, PTN000045368, propagates metal-dependent deubiquitinase activity from PSMD14/BRCC3-type donors. That node is not used here, because CSN5's established substrate is NEDD8-cullin, not ubiquitin. The function transfer to PB is a same-gene transfer (identical sequence over the catalytic region), not an inference across orthologs.

**Decisions** (3 GOA rows plus 2 NEW):
- nucleus IEA: ACCEPT. Q9XZ58 records cytoplasm and nucleus, and FlyBase has an IDA for nuclear periphery from hemocytes (PMID:17295838); nucleus is the right breadth.
- cytoplasm IEA: ACCEPT. FlyBase IDA on PA (PMID:11779478, PMID:17295838) and the PAINT IBA from PTN000045369 support it.
- peptidase activity IEA: MODIFY to GO:0140758 metal-dependent deNEDDylase activity. FlyBase has this IDA on PA (PMID:12737805); JAMM mutants abolish deneddylation (PMID:12183637). The core function uses contributes_to because the activity requires the holo-complex.
- COP9 signalosome: NEW (ISS), kept from the prior review and re-justified (PMID:10531038).
- protein deneddylation GO:0000338: NEW (ISS). CSN5's JAMM site performs the cleavage, so this is participation, not substrate necessity; PA has IMP annotations (PMID:12737805).
- The developmental IMP terms on PA (oocyte axis, GSC maintenance, R-cell differentiation, glial migration, hemocyte proliferation, protein stabilization, and others) are deliberately not proposed for PB. They are downstream consequences of altered CRL activity.

**Prior review corrections.** The earlier UniProt SUBCELLULAR LOCATION quote dropped the inline evidence tag; it now quotes the line verbatim. Added PMID:12737805, PMID:11779478 and PMID:17295838 as references. Added nucleus and cytoplasm as core-function locations and protein deneddylation as a directly_involved_in process. The description was rewritten as a standalone biological summary.

**Family review.** interpro/panther/PTHR10410/PTHR10410-review.yaml lists A0A0B4KHM2 under "Benchmark members without resolved subfamily placement". This does not conflict with the CSN5-clade placement from PAINT (PTN000045369). The family review does not assign a subfamily. A future revision could place CSN5 in the COP9 SIGNALOSOME COMPLEX SUBUNIT 5 subfamily once the member index confirms it.

**Modules.** modules/dmel_cop9_signalosome.yaml (CSN5 grounded as UniProtKB:Q9XZ58 in the CSN5-CSN6 MPN dimer).

**Next relative.** The canonical same-gene product Q9XZ58 (CSN5-PA) has no complete review in the repo (genes/DROME/CSN5 is keyed to A0A0B4KHM2), so it is the next target: genes/DROME/CSN5__Q9XZ58. It carries the experimental FlyBase/UniProt annotations (IDA, IMP, IPI, IBA).

## 2026-10-21 — NEW rows withdrawn: already annotated on another product of the same gene

The re-review proposed NEW rows (GO:0008180, GO:0000338) on this accession. GOA already carries the same terms on
another product of the same gene, reviewed in `genes/DROME/CSN5__Q9XZ58/`. GOA propagates gene-level
annotations to one representative product per gene, so adding them to a second product fills a
convention rather than a curation gap. The rows were withdrawn, following the rule applied across the
ProtNLM2 re-review cohorts (first raised in the review of PR #5303). The gene-level function is unchanged.
