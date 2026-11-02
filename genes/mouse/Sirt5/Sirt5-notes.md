# Sirt5 (mouse, Q8K2C6) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was consulted for this review.

### Deep research

`just deep-research-falcon mouse Sirt5 --fallback perplexity-lite` failed: falcon
returned "Failed to authenticate" and the perplexity-lite fallback returned HTTP 401
(insufficient quota). No deep-research file exists; the review is built from the
cached GOA references (all in `publications/`), the UniProt record and the existing
human SIRT5 review's references.

### Evolutionary grounding

- Mouse Sirt5 is in PANTHER PTHR11085:SF10 with human SIRT5 (UniProt DR lines).
- PAINT node PTN000119399 (SIRT5 subfamily) carries IBDs for mitochondrion
  (GO:0005739), cytosol (GO:0005829), demalonylase (GO:0036054), desuccinylase
  (GO:0036055) and deglutarylase (GO:0061697); its seeds are MGI:1915596 (this gene)
  and human Q9NXA8 (`interpro/panther/PTHR11085/PTHR11085-paint.tsv`).
- Nucleus (GO:0005634) and NAD-dependent histone deacetylase (GO:0017136) IBAs come
  from deep sirtuin nodes (PTN008492176, PTN008718612) seeded by the nuclear/class I
  deacetylases, not from the SIRT5 node. The PAINT curator placed neither on the
  SIRT5 node.
- Gapless comparison mouse vs human: 86.1% identity; Y102, R105 (acyl pocket), H158
  and the four Zn cysteines identical (`Sirt5-bioinformatics/RESULTS.md`).

### What is established in mouse itself (vs inferred)

Mouse-experimental:
- Desuccinylation in vivo: Sirt5 KO mice show CPS1 K1291 hypersuccinylation
  without change in K1291 acetylation [PMID:22076378 "For Lys1291, succinylation
  level increased dramatically in Sirt5 KO mice compared with the level in wt mice"];
  global hypersuccinylation in KO MEFs and liver [PMID:23806337]; liver mitochondrial
  succinylome, HMGCS2 hypersuccinylation and decreased beta-hydroxybutyrate
  [PMID:24315375]; cardiac mitochondrial hypersuccinylation [PMID:26388266].
- Deglutarylation in vivo: KO liver hyperglutarylation, CPS1 hyperglutarylation and
  reduced CPS1 activity [PMID:24703693 "Hyperglutarylation was associated with reduced
  hepatic CPS1 enzymatic activity in SIRT5KO mouse liver"].
- Demalonylation: Peng et al. report demalonylation in vitro and in vivo
  [PMID:21908771, abstract-only in cache].
- No effect on global acetylation: [PMID:23806337 "SIRT5 deficiency does not
  significantly impact global Lys acetylation"]; [PMID:17923681 "no mitochondrial
  hyperacetylation was detectable in mice lacking the two other mitochondrial
  sirtuins, SIRT4 and SIRT5"].
- Localization: mitochondrial matrix by mouse liver mitochondrial fractionation
  [PMID:19410549 "These results all indicate that SIRT5 is a mitochondrial matrix
  protein."]; substantial cytosolic and a very small nuclear pool in mouse liver
  [PMID:23806337].
- Endogenous interaction with CPS1 in mouse liver mitochondrial matrix [PMID:19410549].
  The original deacetylation-of-CPS1 interpretation was superseded by Du et al. 2011.

Inferred only (from human, via ortholog/PAINT):
- Weak in vitro deacetylase activity and the kinetics showing 29->1000-fold preference
  for malonyl/succinyl (measured with human enzyme, PMID:22076378).
- Intermembrane-space pool (human: PMID:18680753).
- SOD1 activation / ROS reduction (human cells, PMID:24140062).

### Decisions worth flagging

- GO:0005743 inner membrane IDA from PMID:18054327 is abstract-only and conflicts with
  matrix fractionation in PMID:19410549 -> UNDECIDED.
- GO:0002931 response to ischemia (IMP, cardiac I/R): KO phenotype attributed to SDH
  hypersuccinylation; marked over-annotated rather than a process Sirt5 executes.
- Protein binding (CPS1, IPI) removed per protein-binding policy; CPS1 is a deacylation
  substrate and the activity is captured by the deacylase MF terms.
- GO:0006476 protein deacetylation: the NOT (ISS) row is accepted on mouse KO
  acetylation data; the positive ISO row from human is removed, so the review does not
  keep both a claim and its negation.
- The deep-node NAD-dependent histone deacetylase IBA (PTN008718612) is refined to the
  three acidic deacylase activities, matching the human SIRT5 review.

Validation: `just validate mouse Sirt5` passes with no warnings.
