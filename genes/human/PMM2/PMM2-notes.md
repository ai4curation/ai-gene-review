# PMM2 (phosphomannomutase 2, O15305) — research notes

## Summary

PMM2 is a cytosolic phosphomannomutase (EC 5.4.2.8) that catalyzes the reversible
isomerization of mannose 6-phosphate (Man6P) to mannose 1-phosphate (Man1P), the
second of two steps converting fructose 6-phosphate to Man1P en route to GDP-mannose
(UniPathway UPA00126, UER00424; step 2/2). Man1P is the precursor of GDP-mannose and
dolichol-phosphate-mannose, the activated mannose donors used in N-linked glycosylation
(LLO/dolichol pathway), O-mannosylation, C-mannosylation, and GPI-anchor synthesis.
Biallelic loss-of-function variants cause PMM2-CDG (CDG-Ia / Jaeken syndrome), the most
common congenital disorder of glycosylation.

## Core molecular function and pathway

- EC 5.4.2.8, Rhea RHEA:11140: `alpha-D-mannose 1-phosphate = D-mannose 6-phosphate`
  [file:human/PMM2/PMM2-uniprot.txt "Reaction=alpha-D-mannose 1-phosphate = D-mannose 6-phosphate"].
- Catalytic activity and kinetics directly measured: KM=16 uM for alpha-D-mannose
  1-phosphate; KM=13.5 uM for alpha-D-glucose 1-phosphate
  [file:human/PMM2/PMM2-uniprot.txt "KM=16 uM for alpha-D-mannose 1-phosphate"].
  Note PMM also acts on glucose-1,6-bisphosphate-type substrates; the physiologically
  relevant reaction is the mannose phosphomutase reaction supplying GDP-mannose.
- Pathway placement: "Nucleotide-sugar biosynthesis; GDP-alpha-D-mannose biosynthesis;
  alpha-D-mannose 1-phosphate from D-fructose 6-phosphate: step 2/2"
  [file:human/PMM2/PMM2-uniprot.txt].
- HAD (haloacid dehalogenase) superfamily / eukaryotic PMM family; two-domain cap+core
  architecture; Asp nucleophile (Asp12 in mature human numbering / Asp19 in PMM1) and
  Mg2+ cofactor [PMID:16540464 "the core domain phosphoryl-transfer site defined by the
  Asp(19) nucleophile and Mg(2+) cofactor"]. UniProt: ACT_SITE 12 (nucleophile), ACT_SITE
  14 (proton donor/acceptor), multiple Mg2+ binding residues, requires metal ion (KW
  Magnesium, Metal-binding; GO:0046872 metal ion binding IEA-UniProtKB-KW).
- Homodimer [file:human/PMM2/PMM2-uniprot.txt "SUBUNIT: Homodimer"].
- Cytoplasmic/cytosolic localization [file:human/PMM2/PMM2-uniprot.txt
  "SUBCELLULAR LOCATION: Cytoplasm"]; HPA IDA localizes to cytosol (GO_REF:0000052).

## Structural / mechanistic literature

- PMID:16540464 (Silvaggi et al. 2006, JBC): X-ray structures of human alpha-PMM1 with
  and without bound substrate; HADSF cap/core domains; "The two isozymes, alpha-PMM1 and
  alpha-PMM2, are shown to have a conserved active-site structure and to display similar
  kinetic properties." Provides the EXP support for GO:0004615 phosphomannomutase activity
  for PMM2 (also the structural basis of CDG-1a genotype-phenotype). Abstract foregrounds
  PMM1, but PMM2 is explicitly assayed/compared; this is the ECO:0000269/EXP Reactome
  annotation for PMM2 phosphomannomutase activity. Do NOT remove as "wrong gene."

## Disease / CDG biology

- PMID:9140401 (Matthijs et al. 1997, Nat Genet): cloned PMM2 on 16p13; 11 missense
  mutations in 16 CDG1 patients with documented PMM deficiency; "Our results give
  conclusive support to the biochemical finding that the phosphomannomutase deficiency is
  the basis for CDG1." Establishes PMM2 = enzyme, role in GDP-mannose synthesis and
  glycoprotein biosynthesis. This is the TAS source for GO:0004615, GO:0009298,
  GO:0009101 [PMID:9140401 "phosphomannomutase (PMM)8, an enzyme necessary for the
  synthesis of GDP-mannose"].
- PMM2-CDG (CDG-Ia, MIM:212065): autosomal recessive multisystem disorder; severe
  encephalopathy, axial hypotonia, abnormal eye movements, psychomotor retardation,
  peripheral neuropathy, cerebellar hypoplasia, retinitis pigmentosa, inverted nipples,
  abnormal fat distribution, coagulopathy [file:human/PMM2/PMM2-uniprot.txt DISEASE].
  Underglycosylation of serum glycoproteins (hypoglycosylated transferrin) is the
  diagnostic hallmark.
- R141H is the most common allele, never homozygous (homozygosity lethal) — supports a
  hypomorphic/balanced-genotype model [reactome/R-HSA-3781926.md "The R141H mutation is
  never observed in the homozygous state"; file:human/PMM2/PMM2-uniprot.txt VARIANT 141
  "homozygosis of this mutation is incompatible with life"].
- Reactome R-HSA-446201 ("PMM1,2 isomerise Man6P to Man1P"), R-HSA-3781926 ("Defective
  PMM2 does not isomerise Man6P to Man1P"), R-HSA-446205 ("Synthesis of GDP-mannose"),
  R-HSA-4043911 ("Defective PMM2 causes PMM2-CDG").

## PMID:9525984 — CAUTION: this is about CDG-Ib / PMI (MPI), NOT PMM2

- The FlyBase IMP annotation of GDP-mannose biosynthetic process (GO:0009298) to PMM2
  cites PMID:9525984. But that paper is about phosphomannose ISOMERASE (PMI/MPI) deficiency
  causing CDG type Ib and mannose therapy — a DIFFERENT enzyme and a different gene
  [PMID:9525984 "Phosphomannose isomerase (PMI) deficiency is the cause of a new type of
  carbohydrate-deficient glycoprotein syndrome ... The disorder is caused by mutations in
  the PMI1 gene"]. The cached publication is full-text-available (abstract+full text both
  present and concordant — they describe PMI, not PMM2). PMM2 catalyzes the Man6P<->Man1P
  mutase step, whereas PMI catalyzes F6P<->Man6P (the isomerase step). The IMP evidence in
  this paper does not concern PMM2's catalytic step. The GO TERM (GDP-mannose biosynthetic
  process) is still biologically correct for PMM2, and the function is independently and
  strongly supported (EXP PMID:16540464, TAS PMID:9140401, IEA pathway). So the right
  action is ACCEPT the term but flag the citation as MISCITED/likely wrong reference in
  reference_review, rather than REMOVE the annotation. (Per CLAUDE.md: do not REMOVE an
  experimental annotation merely on cached-text grounds; here we keep the term and document
  the citation problem.)

## Protein interactions (IPI / GO:0005515 protein binding)

- Three IPI "protein binding" annotations from high-throughput binary interactome maps:
  PMID:25416956 (Rolland et al. 2014, proteome-scale interactome), PMID:26871637 (Yang et
  al. 2016, alternative-splicing interactome expansion), PMID:32296183 (Luck et al. 2020,
  HuRI reference binary interactome). Partners listed in GOA: ACY3 (Q96HD9), MEOX2 (Q6FHY5),
  SGK2 isoform (Q9HBY8-2). UniProt INTERACTION lists ACY3 (NbExp=9), MEOX2, SGK2.
- These are generic Y2H/binary-map hits with no demonstrated functional/biological meaning
  for a cytosolic metabolic enzyme. Per curation guidance, "protein binding" (GO:0005515)
  is uninformative and should not be treated as a core molecular function. Mark as
  over-annotated / non-core; no specific adapter or scaffold function is established.

## Localization annotations

- cytosol (GO:0005829): supported by HPA IDA (GO_REF:0000052), IBA, IEA, Reactome TAS, and
  UniProt "Cytoplasm". Core. cytoplasm (GO:0005737) IEA is a correct but less precise parent.
- neuronal cell body (GO:0043025): single Ensembl-orthology IEA (GO_REF:0000107) transferred
  from mouse Q9Z2M7. PMM2 is a ubiquitously expressed cytosolic housekeeping enzyme (HPA:
  "Low tissue specificity"). No evidence of a neuron-cell-body-specific function; this is a
  by-product of where the enzyme happens to be detectable in a neuron and is an
  over-annotation at the gene/function level. Keep as non-core at most; better treated as
  over-annotated for a soluble cytosolic enzyme.

## Process annotations: core vs downstream (substrate guilt-by-association)

- CORE process: GDP-mannose biosynthetic process (GO:0009298) and mannose metabolic
  process (GO:0006013) — these directly describe what the enzyme product (Man1P) feeds and
  what the enzyme acts on. PMM2's reaction is the committed mutase step.
- DOWNSTREAM processes: protein N-linked glycosylation (GO:0006487, IBA) and glycoprotein
  biosynthetic process (GO:0009101, TAS PMID:9140401). PMM2 only SUPPLIES a precursor
  (GDP-mannose) many steps upstream; it is not itself a glycosyltransferase and does not
  act on protein substrates. By the GO "supplies precursor for" / substrate-guilt-by-
  association pattern these are true at the whole-organism level (loss causes
  hypoglycosylation) but are downstream consequences, not the molecular role of the enzyme.
  Treat as KEEP_AS_NON_CORE (involved_in is defensible because biallelic loss disrupts
  N-glycosylation, the basis of the disease) rather than core MF/BP. glycoprotein
  biosynthetic process is the most general of these and the most over-annotated.

## FlyBase orthology process terms (in UniProt DR but not in GOA core list)

- GO:0061728 (GDP-mannose biosynthetic process from mannose) and GO:0061729 (GDP-D-mannose
  biosynthetic process from fructose-6-phosphate), IMP from FlyBase — more specific children
  of GO:0009298 that precisely describe the two GDP-mannose biosynthetic routes the PMM step
  participates in. These are good candidate refinements but are not in the supplied GOA TSV
  rows; noted for proposed refinement.

## Conclusions for core_functions

- molecular_function: GO:0004615 phosphomannomutase activity (enables); metal ion binding
  (GO:0046872) is a cofactor requirement, not a standalone core function.
- directly_involved_in: GO:0009298 GDP-mannose biosynthetic process; GO:0006013 mannose
  metabolic process.
- locations: GO:0005829 cytosol.
- substrates: D-mannose 6-phosphate / alpha-D-mannose 1-phosphate (CHEBI:58735 / CHEBI:58409).
