# PLPBP (PLPHP, formerly PROSC; UniProtKB:O94903) review notes

Journal for the review of human PLPBP. Quotes are verbatim from the cached
publication files unless marked otherwise.

## 2026-11-26: literature search

Search (PubMed, 2026-11-26): `PLPBP OR PLPHP OR PROSC[tiab] OR "pyridoxal phosphate
homeostasis protein" OR YggS OR "COG0325" OR YBL036C` returned 106 records. About 25
are unrelated ("P-ROSC" resuscitation scores, "proscillaridin", and similar). The
remainder were triaged by title and abstract and 40 were cached in `publications/`.
Full text was available in the cache for PMID:31825581, 37451483, 39604152, 36218140,
31677193, 30525118, 36324377, 33977028, 31741821, 33728241, 34498310, 42045118,
41820517, 38139332, 36295057 and 28744260. The two founding clinical papers
(PMID:27912044 and PMID:30668673) are abstract-only in the cache; PMC does not
release their XML (the PubMed full-text tool returned an empty body for PMC6391652,
and Europe PMC returned HTTP 500 for both on the day).

### What the protein is

- A single-domain fold-type III PLP barrel with no known catalytic activity.
  [PMID:26872910 "The COG0325 protein family belongs to the fold-type III class of PLP enzymes and binds PLP but has no known biochemical activity although it occurs in all kingdoms of life."]
- The yeast ortholog structure established the fold and the covalent cofactor.
  [PMID:12499548 "A cofactor, pyridoxal 5'-phosphate, is covalently bound near the C-terminal end of the barrel, the usual active site in TIM-barrel folds."]
  The same abstract says "The yeast protein has been shown to have amino-acid racemase activity"; later work on the family did not confirm a physiological racemase role, and no racemase term is annotated to the human protein.
- Recombinant human protein binds PLP as a Schiff base.
  [PMID:29689137 "Normal PLPHP is largely a monomer with PLP bound through a Schiff-base linkage."]
- The lysine was identified directly.
  [PMID:31825581 "Lys47 was determined the PLP-binding site of PLPBP via liquid chromatography combined with tandem MS (LC-MS/MS) analysis after reduction of the PLP adduct to the secondary amine using NaBH4"]
  My structure analysis agrees: the Schiff-base lysine of four PLP-bound homolog structures aligns with K47 (see `PLPBP-bioinformatics/RESULTS.md`).

### Oligomeric state is disputed

- Monomer: PMID:29689137 (above), and
  [PMID:39604152 "in our hands PROSC was almost exclusively in the monomeric form, although a minor fraction of the dimeric protein could be detected"].
- Dimer: [PMID:31825581 "In contrast to previous observations, our data reveal that the protein is predominantly dimeric, shielding the cofactor from the environment."]
- The p.Tyr69Cys mutant dimerises through a disulfide [PMID:29689137 "With p.Tyr69Cys there was extensive protein dimerization due to disulfide bridge formation, and PLP accessibility was decreased"].
- No experimental structure of the human protein exists (PDBe has no entry for O94903), so the interface proposed in PMID:31825581 is a cross-link-guided model. I do not assert a homodimer in the review.

### What the protein does: PLP homeostasis, mechanism unknown

- Human disease paper: [PMID:27912044 "our studies suggest that PROSC is involved in intracellular homeostatic regulation of PLP, supplying this cofactor to apoenzymes while minimizing any toxic side reactions"].
- Cross-species complementation shows conserved function: [PMID:27912044 "An E.coli mutant lacking the PROSC homolog (ΔYggS) is pyridoxine sensitive; complementation with human PROSC restored growth whereas hPROSC encoding p.Leu175Pro, p.Arg241Gln, and p.Ser78Ter did not."] and [PMID:24097949 "The plasmid-borne expression of YggS and orthologs from Bacillus subtilis, Saccharomyces cerevisiae, and humans fully rescued the ΔyggS phenotypes."]
- The function needs the cofactor: [PMID:24097949 "Expression of a mutant YggS lacking PLP-binding ability, however, did not reverse the ΔyggS phenotypes."]
- Loss in human cells lowers PLP and raises the PNPO substrates: [PMID:37451483 "PLPHP deficiency leads to decreased cellular PLP level and accumulation of PNPO substrates"]. The same paper reads the data as a chaperone that protects PLP from phosphatases: [PMID:37451483 "Increased susceptibility of PLP for degradation by PDXP or other phosphatases in PLPHP-deficient cells is in line with a PLP-binding/chaperone function of PLPHP that regulates concentration of free PLP"].
- A direct PNPO complex was not found: [PMID:37451483 "We did not detect co-immunoprecipitation of PLPHP in a PNPO IP in control HEK293"].
- Interactome data argue against simple delivery to apo-enzymes: [PMID:31825581 "We did not observe an over-representation of PLP-DEs among the PLPBP-binding proteins"].
- The plant orthologs can exchange PLP with enzymes in vitro: [PMID:38954500 "Assays in vitro show that Arabidopsis PLPHP can coordinate PLP transfer and withdrawal from other enzymes."] This is not shown for the human protein.
- In bacteria the characteristic defect is PNP accumulation, which then inhibits PLP enzymes: [PMID:34978460 "Our results indicate that PLPBP is involved in the homeostasis of pyridoxamine 5'-phosphate, and that its disruption may lead to the accumulation of PNP in PLPBP deficiency."]; [PMID:35803498 "In the yggS-deficient E. coli strain, inhibition of PLP-dependent enzymes, such as the glycine cleavage system by PNP, is the root cause of metabolic perturbation."]
- A second, RNA-binding activity was reported in 2024 for E. coli YggS and seen with the human protein in vitro: [PMID:39604152 "The interaction with RNA is evidently conserved, since it is also observed with human PLP-BP."] The key E. coli residue Lys137 aligns with human Lys153. One laboratory, in vitro, no cellular RNA targets for the human protein: recorded as a question, not as an annotation.
- Field summary of the open problem: [PMID:39604152 "Yet, how PLP-BP is involved in PLP homeostasis, and thus what its actual function is in cellular metabolism, is entirely unknown."]

### Where it is

- Predicted cytoplasmic at cloning: [PMID:10496079 "The gene product is likely to be a soluble cytoplasmic protein, but its function remains to be determined."]
- Mitochondrial as well: [PMID:30668673 "Additional studies in human cells and yeast provide the first empirical evidence that PLPHP is localized in mitochondria and may play a role in mitochondrial metabolism."]
- Both, by fractionation of HEK293 cells: [PMID:37451483 "Western blot analysis of mitochondrial and cytosolic fractions showed that PLPHP protein was present in both fractions"]. The authors note GAPDH signal in their mitochondrial fraction, so the fraction was not pure.
- MitoCarta3.0 lists it (the HTP GO row, PMID:34800366); the mouse ortholog has an HDA mitochondrion row from PMID:18614015.
- Mouse mitochondria lacking the matrix protease CLPP accumulate PLPBP: [PMID:38139332 "A CLPP absence caused the accumulation and dispersion of CLPX-VWA8 as AAA+ unfoldases, and of PLPBP."] This is indirect evidence for a matrix pool (CLPXP is a matrix protease) in mouse; it is one line, so the human review stays at the root organelle term.
- Mitochondrial effects of loss: [PMID:37451483 "PLPHP deficiency had a distinct effect on mitochondrial PLP and PMP, suggesting impaired activity of mitochondrial transaminases."]
- UniProt annotates no transit peptide. My N-terminal descriptors do not settle it. An OpenScientist job on the mitochondrion annotation was launched (see below).

### Disease: vitamin B6-dependent early-onset epilepsy (EPEO1, MIM 617290; MONDO:0015005 is the parent grouping used in dismech)

- Autosomal recessive, biallelic: [PMID:30668673 "Biallelic pathogenic variants in PLPBP (formerly called PROSC) have recently been shown to cause a novel form of vitamin B6-dependent epilepsy"].
- Biochemistry in patients: [PMID:27912044 "Pre-treatment cerebrospinal fluid samples showed low PLP concentrations and evidence of reduced activity of PLP-dependent enzymes. However, cultured fibroblasts showed excessive PLP accumulation."] Note the tension with the later cell work, which found lower PLP in deficient fibroblasts and HEK293 cells (PMID:37451483); culture medium vitamer composition differs between the studies.
- Genotype and severity: [PMID:30668673 "The most severe phenotypes were associated with variants leading to loss of function of PLPBP or significantly affecting protein stability/PLP-binding."]; [PMID:41671913 "Genotype-phenotype analysis revealed an association of missense variants and compound heterozygous variants with an attenuated phenotype, while biallelic truncating variants and homozygous variants were linked to severe phenotypes and/or early mortality."]
- Zebrafish knockout reproduces the disease and its treatment: [PMID:30668673 "Our model recapitulates the disease, with plpbp-/- larvae showing behavioural, biochemical, and electrophysiological signs of seizure activity by 10 days post-fertilization and early death by 16 days post-fertilization."]; [PMID:30668673 "Larvae had disruptions in amino acid metabolism as well as GABA and catecholamine biosynthesis, indicating impairment of PLP-dependent enzymatic activities."]
- Missense mechanism, biochemical: [PMID:29689137 "The p.Leu175Pro mutation grossly misfolded PLPHP."]; [PMID:29689137 "The p.Arg241Gln and p.Tyr69Cys mutants respectively lacked PLP or had a decreased amount of this cofactor."]; [PMID:29689137 "Overall, the six missense mutations caused ill effects and five of them impaired folding or decreased stability"].
- Founder allele: c.370_373del p.Asp124Lysfs*2 in French-Canadian families (PMID:33977028, PMID:36324377) and the most frequent allele in the 54-patient review [PMID:41671913 "the variant c.370-373del being the most frequently reported (18.5%)"].
- Mitochondrial-encephalopathy-like presentation with lactic acidosis in some neonates (PMID:36324377, PMID:33728241), in line with the mitochondrial findings above.

All of the evidence is loss of function. There is no report of a heterozygous phenotype, of gain of function, or of a dominant-negative allele; gnomAD shows 63 high-confidence loss-of-function alleles in heterozygotes and none homozygous (bioinformatics folder).

## 2026-11-26: structure and variant analysis

See `PLPBP-bioinformatics/RESULTS.md`. Main points:

- CDS and canonical sequence agree, and all 24 reported protein changes are reproduced from their c. changes; literature numbering is canonical numbering.
- PLP site from four homolog structures: K47 (Schiff base), N68, R241 (ring), S226, G243, S244 (phosphate), V45, I94, M181, I183, M225 (pocket wall).
- Patient missense variants are more conserved, more buried and closer to PLP than other gnomAD missense variants.
- Unexplained by structure: p.Pro87Leu, p.Ala107Thr (exposed, poorly conserved) and p.His275Asp (disordered C-terminal residue).

## 2026-11-26: annotation review decisions

- `GO:0030170` pyridoxal phosphate binding (IBA, IEA): accept, core. Direct evidence on the human protein (PMID:29689137, PMID:31825581).
- `GO:0042816` vitamin B6 metabolic process (IBA): accept. GO has no PLP homeostasis term (QuickGO search 2026-11-26 for "pyridoxal phosphate homeostasis" and "vitamin B6 homeostasis" returned only binding, transport, metabolic and biosynthetic terms), so a new term is proposed. The protein does not catalyse a vitamer interconversion; it is kept in this process because loss changes the vitamer pools in human cells, zebrafish, yeast and bacteria, and because no narrower term fits.
- `GO:0005737` cytoplasm (IBA, IEA, NAS): accept. The protein is in both cytosol and mitochondria, so cytoplasm is the accurate umbrella here and I do not refine it to cytosol.
- `GO:0005829` cytosol (IDA, HPA): accept; supported by fractionation (PMID:37451483).
- `GO:0005739` mitochondrion (HTP): accept. Root organelle policy: direct evidence, sub-compartment not resolved. No sub-compartment row added: the only line for the matrix is the mouse CLPP result.
- No NEW rows. RNA binding is a single in vitro report; "PLP carrier" has no GO term and no direct evidence for the human protein.

## 2026-11-26: family, GO-CAM, module

- PANTHER PTHR10146, three PAINT IBD rows on two nodes (cytoplasm and PLP binding at PTN000015833; vitamin B6 metabolic process at PTN000015836). `just paint-losses human PLPBP` reports no IRD or IKR on the lineage. Family review written at `interpro/panther/PTHR10146/PTHR10146-review.yaml`.
- GO-CAM: `gocams/index.tsv` has no row for O94903, PLPBP or PLPHP, so there is no model to review.
- Module: PLPBP added to `modules/vitamin_b6_plp_metabolism.yaml` as a second PLP homeostasis annoton (PLP binding), alongside PDXP.

## OpenScientist

- `just deep-research-openscientist human PLPBP` (gene deep research). Launched 2026-11-26.
- Hypothesis job on the `GO:0005739` mitochondrion row (`--as-function-hypothesis`), asking for presequence analysis. Launched 2026-11-26.
- Hypothesis job `surface-variant-interface`: do the exposed patient variants (R41Q/W, Y69C, P87L, A107T) define an interaction surface rather than destabilise the fold? Launched 2026-11-26.

Status of each is recorded at the end of this file when the session closes.

## 2026-11-26 (later): OpenScientist deep research returned

`PLPBP-deep-research-openscientist.md` (run time 6955 s). It agrees with this review on the
molecular function (non-catalytic PLP binding on Lys47), on loss of function, and on the
absence of a canonical cleavable presequence. Two points where I do not follow it:

- Mitochondrion. The report calls the `GO:0005739` HTP row "transferred from a *Drosophila*
  study". That is wrong: the row cites MitoCarta3.0 (PMID:34800366) and FlyBase is the assigning
  group. The report also does not weigh PMID:30668673 and PMID:37451483. I keep the row
  (ACCEPT) and record the disagreement in the reference's `reference_review` (DISPUTED).
- Mechanism. The report states PLP handover to apo-enzymes as the mechanism. The transfer
  assays are on bacterial orthologs: [PMID:36218140 "is able to slowly transfer it to a model PLP-dependent"]
  and [PMID:42045118 "first demonstration that YggS of S. enterica can mediate transfer of PLP to a"].
  Nothing equivalent exists for the human protein, and the human interactome argues against
  simple delivery (PMID:31825581), so the mechanism stays a knowledge gap.

Useful additions taken from it: the two bacterial transfer papers (added as references), and
the PNP arm of the bacterial phenotype (PNP inhibits the glycine cleavage system,
PMID:31677193), which is a candidate explanation for the raised glycine seen in some patients.
The report's own variant test used only five ClinVar pathogenic missense variants and found no
enrichment near Lys47; my test with the 18 literature variants on modelled residues does find
patient variants closer to PLP, more buried and more conserved (bioinformatics RESULTS.md,
section 4). The two analyses agree that most missense alleles act through stability.

## 2026-11-26 (21:25 UTC): OpenScientist job status and PR review follow-up

- Gene deep research: completed, committed.
- Hypothesis job on the `GO:0005739` row: the process ended after about two hours without
  writing a report (empty output directory, nothing in the wrapper log). Not relaunched: the
  presequence question it asked was answered inside the deep-research report (no canonical
  cleavable presequence), and that does not change the organelle row.
- Hypothesis job `surface-variant-interface`: same failure (no report after about two hours).
  Relaunched once in narrowed form (p.Pro87Leu and p.Ala107Thr only, surface conservation only,
  two iterations). The outcome will be appended here if it returns; until then the two
  variants stay "unexplained by structure".
- PR review (automated reviewer): the `GO:0042816` row's reason wrongly said it was the most
  specific term available. `GO:0042822` pyridoxal 5'-phosphate metabolic process is an is_a
  child (QuickGO ancestors query, 2026-11-26). The row stays ACCEPT, with the reason rewritten:
  the evidence concerns the balance of several vitamers (PLP down, PNP and PMP up), which is
  the scope of the vitamin B6-wide term and not of the PLP-only child. The homeostasis term
  request is separate. Also: the cytoplasm IEA and NAS rows now state the same umbrella
  argument as the IBA row; the deep-research quote was moved off the PLP-binding row; a paper
  title was corrected in the family review.
