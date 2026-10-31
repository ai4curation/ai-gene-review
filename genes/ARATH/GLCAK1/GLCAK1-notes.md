# GLCAK1 (At3g01640, Q93ZC9) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: GLCAK1 is the closest experimentally characterised relative of the wheat ProtNLM2
benchmark protein A0A3B6NKR6. This review does not use ProtNLM2 output.

### Deep research
- `just deep-research-falcon ARATH GLCAK1 --fallback perplexity-lite` failed. Falcon/Edison
  returned 403 at authentication and perplexity returned 401 (quota exhausted). There is no
  gene-level deep-research file. I worked from the primary literature, found through a Europe
  PMC search for "glucuronokinase OR GlcAK OR At3g01640" and cached with `just fetch-pmid`.
- The family-level falcon report (`interpro/panther/PTHR38710/PTHR38710-deep-research-falcon.md`)
  has errors. It gives GO:0047938 as "glucuronokinase activity"; the correct id is GO:0047940.
  It also says GlcAK is outside the GHMP superfamily, which the primary paper contradicts.
  I did not use it as evidence.

### Evolutionary grounding
- PANTHER: GLCAK1 and its paralog GLCAK2 (At5g14470, Q9LY82) are both in PTHR38710:SF1
  (`interpro/panther/PTHR38710/PTHR38710-entries.csv`). The wheat target is in the same
  subfamily.
- PAINT (`PTHR38710-paint.tsv`) has glucuronokinase activity (GO:0047940) IBD at PTN008680403.
  Its only seed is AGI_LocusCode:AT3G01640 (GLCAK1 itself). A separate GO:0047940 IBD sits at
  PTN001475528, seeded by zebrafish (ZFIN:ZDB-GENE-080204-36, the bifunctional GlcAK/pyrophosphorylase
  of PMID:24586965). The cytosol IBA on GLCAK1 comes from the deep node PTN000048555, whose seeds
  are mevalonate kinases. GLCAK1 did not receive the mevalonate kinase activity or isoprenoid-process
  terms from that node, and I treat that omission as a deliberate PAINT decision.
- GOA does not yet carry an IBA glucuronokinase row for GLCAK1, probably because the
  PTN008680403 IBD is recent (2026-06-17).

### Evidence summary
- Biochemistry [PMID:19951951, "These experiments confirm that the purified enzyme indeed is a GlcAK."]:
  The study used recombinant At3g01640. Its sugar specificity is strict
  ["The Arabidopsis enzyme only catalyzed the conversion of d-GlcA into its corresponding
  sugar-1-phosphate but failed to utilize any other monosaccharide tested in the assays"]. Of
  the nucleotides tested only ATP works ["Apart from ATP none of the nucleotides was able to
  phosphorylate GlcA."]. It needs Mg2+, and Mn2+ or Co2+ can substitute. Km is 0.70 mM for GlcA
  and 0.56 mM for ATP, the ATP response is sigmoidal (Hill coefficient 1.54), and the pH
  optimum is 7.5.
- Localisation has not been tested experimentally
  ["The protein is assumed to be localized in the cytosol as no transmembrane spanning domains
  and transit peptides are predicted (iPSORT software)."].
- In vivo genetics [PMID:30102814]: CRISPR frameshift alleles glcak1-3 and glcak1-4 accumulate
  GlcA (about 26-fold more 3H label in the GlcA peak) and put less 3H-myo-inositol into cell
  walls (32–40% vs 73–79%). Ascorbate is unchanged. The SALK lines glcak1-1 (SALK_076931) and
  glcak1-2 (SALK_127949c) have their insertions in the promoter, keep wild-type expression, and
  are NOT knockouts. Phenotypes reported for them by other groups should not be attributed to
  loss of GLCAK1.
- GLCAK2: the residual cell-wall flux in glcak1 mutants is attributed to GLCAK2, and
  "preliminary" enzyme data from the Tenhaken lab call it a true GlcAK [PMID:30102814]. An
  earlier paper (Zhao et al. 2013, cited there) proposed galactokinase activity. No GLCAK2
  kinase assay has been fully published, so do not take GLCAK2 data as reference.
- USP coupling [PMID:23857351]: total glucuronokinase activity falls in USP-silenced lines.
  This is pathway coupling, not an interaction.
- Wheat GlcAK overexpression in Arabidopsis lowered ascorbate [PMID:36931562, abstract only].
  This conflicts with the knockout data, and I did not use it.

### Annotation decisions (13 GOA rows)
- 4 NOT rows (galactokinase, glucokinase, L-arabinokinase, galacturonokinase; IDA): ACCEPT. All
  four sugars were tested directly in Table 3.
- glucuronokinase activity (IDA, IEA): ACCEPT. This is the core function.
- ATP binding (IEA): KEEP_AS_NON_CORE.
- cytoplasm (ISM): MODIFY to cytosol. cytosol (IBA): ACCEPT, since it is the best-supported
  location although it is inferred.
- inositol metabolic process (TAS): MODIFY to UDP-glucuronate biosynthetic process (GO:0006065).
  GLCAK1 acts on GlcA, not on inositol. Comparator: the UGD1-4 enzymes of the other UDP-GlcA
  route carry GO:0006065 (IDA) in Arabidopsis. GLCAK1 catalyses one step of the pathway, so it
  passes the participation test.
- cell wall biogenesis (TAS): KEEP_AS_NON_CORE. GLCAK1 acts upstream as a precursor supplier,
  and the knockout flux data support this.
- poly(U) RNA binding (IDA, PMID:17511964): MARK_AS_OVER_ANNOTATED. The row comes from a
  proteome-wide polyU column used to enrich nucleotide-binding proteins, and there is no
  biological RNA-binding role.
- pollen tube development (TAS): REMOVE. The only basis is pollen-preferred expression and a
  hypothesis in the Discussion. No mutant pollen phenotype has been reported, and the term
  would describe a downstream organismal process.

### For transfer to orthologs (e.g. wheat A0A3B6NKR6)
- Experimentally established in Arabidopsis GLCAK1: glucuronokinase activity (GO:0047940); strict
  GlcA and ATP specificity; the NOT activities on glucose, galactose, L-arabinose and galacturonic
  acid; and an in vivo role in channelling MIOX-derived GlcA into cell-wall precursors (IMP).
- Inferred only: cytosolic location, and any salvage-pathway or pollen-specific role.
