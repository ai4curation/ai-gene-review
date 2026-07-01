# Mcad (Drosophila melanogaster) — Gene Review Notes

- UniProt: Q9VSA3 (ACADM_DROME); FlyBase FBgn0035811; ORF CG12262; 419 aa; EC 1.3.8.7.
- Ortholog of human ACADM (P11310, MCAD). Reviewed Swiss-Prot entry, "Evidence at protein level".

## Identity / function (from UniProt Q9VSA3 record)

UniProt names the protein "Medium-chain specific acyl-CoA dehydrogenase, mitochondrial"
[UniProt Q9VSA3, "Medium-chain specific acyl-CoA dehydrogenase, mitochondrial"], and assigns
EC 1.3.8.7 with experimental evidence from the fly paper
[UniProt Q9VSA3, "EC=1.3.8.7 {ECO:0000269|PubMed:29563254}"].

FUNCTION line: "Medium-chain specific acyl-CoA dehydrogenase that catalyzes the first step of
mitochondrial fatty acid beta-oxidation, an aerobic process that breaks down fatty acids into
acetyl-CoA and allows the production of energy from fats (PubMed:29563254)." The mechanistic
detail (removal of one hydrogen from C-2 and C-3 to form trans-2-enoyl-CoA; ETF as electron
acceptor) is "By similarity" to human/mammalian MCAD (ECO:0000250|UniProtKB:P11310).

CATALYTIC ACTIVITY (Rhea RHEA:14477): "a medium-chain 2,3-saturated fatty acyl-CoA + oxidized
[electron-transfer flavoprotein] + H(+) = a medium-chain (2E)-enoyl-CoA + reduced
[electron-transfer flavoprotein]; ... EC=1.3.8.7; Evidence={ECO:0000269|PubMed:29563254}".

COFACTOR: FAD (ECO:0000250|UniProtKB:P11310, by similarity). SUBUNIT: Homotetramer (by
similarity to P11310). SIMILARITY: acyl-CoA dehydrogenase family (ECO:0000305). InterPro/CDD
carry the MCAD-specific signatures (CDD cd01157 MCAD; InterPro IPR034180 MCAD;
PANTHER PTHR48083:SF2 "MEDIUM-CHAIN SPECIFIC ACYL-COA DEHYDROGENASE, MITOCHONDRIAL").

SUBCELLULAR LOCATION: "Mitochondrion matrix {ECO:0000269|PubMed:29563254}. Cytoplasm, cytosol
{ECO:0000269|PubMed:29563254}." A mitochondrial transit peptide (residues 1..22) is annotated
(ECO:0000255), and the mature chain is 23..419.

## PMID:29563254 (Course et al. 2018, Mol Biol Cell) — full text available

This is the sole primary experimental paper directly on fly Mcad; it is the source of the
EXP/IDA/IMP GOA annotations and of the fly protein-level evidence.

Key verbatim facts:
- Canonical function: 'MCAD's canonical function is to break down medium-chain fatty acids
  (C6-12), and its deficiency is the most common inborn error of β-oxidation in humans'.
- Enzyme identity: 'an enzyme critical to fatty acid β-oxidation, medium-chain acyl-coenzyme A
  dehydrogenase (MCAD), is phosphorylated in a PINK1-dependent manner'.
- Localization (fractionation of fly lysates, endogenous + transgenic): 'both endogenous and
  transgenic MCAD protein localized to the mitochondria as well as the cytosol, consistent with
  a previous report in mammals'.
- A CRISPR deletion fly model (MCADmut), an MCAD-over-Df transheterozygote, and ubiquitous MCAD
  RNAi all showed 'significant elevations in medium-chain acylcarnitines characteristic of human
  MCAD deficiency: C6, C8, and C10:1 acylcarnitines'; the elevations 'were fully rescued by
  expression of MCAD (WT)'. This is direct in vivo (fly) IMP-level evidence for Mcad's role in
  medium-chain fatty acid beta-oxidation. It also shows 'the first time that fly MCAD deficiency
  has been tested for similarity to human MCAD deficiency'.
- Catalytic activity is retained in PINK1 nulls: 'suggesting that MCAD is still enzymatically
  active as an acyl-CoA dehydrogenase in PINK1 null flies'.
- Novel PINK1 axis: MCAD is phosphorylated at Ser347 (mammalian Thr351) in a PINK1-dependent
  manner; phosphomimetic S347D/DD rescues PINK1-null climbing/flight/thorax/wing phenotypes.
  Crucially this rescue is 'independent of its conventional role in β-oxidation' and 'independent
  of ATP production': 'phosphomimetic MCAD S347 likely rescues PINK1 null's organismal phenotypes
  independently of MCAD's acyl-CoA dehydrogenase activity.'
- The abstract frames this as 'a novel function of MCAD' and describes MCAD as 'a mitochondrial
  matrix protein critical to fatty acid metabolism.' UniProt captures this cautiously: 'May
  contribute to Pink1-mediated regulation of fatty acid and amino acid metabolism, through a
  mechanism that is independent of its acyl-CoA dehydrogenase activity.'

Interpretation: the PINK1/MCAD-phosphorylation axis is a genuine, novel, catalysis-independent
role, but its molecular mechanism is undefined (no GO MF/BP term is well-supported for it in
fly beyond the canonical FAO function). No new GO term is proposed for it because the mechanism
is unknown; it is flagged as a suggested question/experiment instead.

## Proteomics / localization support (abstract-only)

- PMID:19317464 (Tan et al. 2009, LOPIT organelle mapping of Drosophila embryos): abstract only
  (full_text_available: false). HDA mitochondrion annotation. Abstract does not name Mcad;
  supporting text at the level of the specific protein is not extractable, so this is treated as
  full_text_unavailable and localization is accepted as consistent (mitochondrion), not core.
- PMID:16212416 (Alonso et al. 2005, Drosophila mitochondrial proteome 2-D gel/MALDI): abstract
  only. HDA mitochondrion annotation; same treatment.

Both HDA mitochondrion calls are consistent with the well-supported mitochondrial localization
but are less specific than mitochondrial matrix (the EXP-supported compartment from PMID:29563254).

## Cytosol annotations

Two cytosol/cytoplasm annotations exist (IDA PMID:29563254 GO:0005829; IEA SubCell GO:0005829;
IBA GO:0005737). Course et al. did observe MCAD in the cytosolic fraction of fly lysates
('localized to the mitochondria as well as the cytosol'), so the IDA cytosol call has direct
support in fly and is kept (non-core). The mitochondrial matrix is the primary/core compartment
for a mitochondrially-targeted FAO flavoenzyme; cytosolic pool is a secondary observation, also
seen for mammalian MCAD (Du et al. 2013, cited in the paper).

## Annotation-by-annotation plan

Molecular function:
- GO:0070991 medium-chain fatty acyl-CoA dehydrogenase activity — CORE MF. IBA + IEA(Rhea/EC) +
  IMP(PMID:29563254). ACCEPT (the IMP is the fly-specific support via the deficiency model + EC
  1.3.8.7 experimental assignment).
- GO:0003995 acyl-CoA dehydrogenase activity (IEA, ISS) — correct general parent of GO:0070991;
  KEEP_AS_NON_CORE.
- GO:0016627 oxidoreductase activity, acting on CH-CH group of donors (IEA InterPro) — broad
  correct parent; KEEP_AS_NON_CORE.
- GO:0050660 flavin adenine dinucleotide binding (IEA InterPro) — MCAD is an FAD flavoprotein
  (FAD cofactor annotated by similarity, InterPro FAD-binding signatures); ACCEPT (cofactor
  binding, real but supporting/non-core relative to the dehydrogenase MF). Treated as a genuine
  molecular function to include in core_functions as second MF, matching the human review.

Biological process:
- GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase — CORE BP. IBA + IMP
  (PMID:29563254, fly deficiency model). ACCEPT.
- GO:0051793 medium-chain fatty acid catabolic process — CORE BP (specific). IBA. ACCEPT.
- GO:0006635 fatty acid beta-oxidation (IEA InterPro) — correct parent; ACCEPT (core process,
  redundant with GO:0033539).

Cellular component:
- GO:0005759 mitochondrial matrix — CORE location. EXP(PMID:29563254) + IEA SubCell. ACCEPT.
- GO:0005739 mitochondrion — correct, less specific than matrix; multiple lines (IBA, IEA, IDA
  PMID:29563254, HDA x2). KEEP_AS_NON_CORE.
- GO:0005737 cytoplasm (IBA) — over-general placeholder relative to matrix; MARK_AS_OVER_ANNOTATED
  (same reasoning as human review; mitochondrion is within cytoplasm but uninformative).
- GO:0005829 cytosol (IDA PMID:29563254, IEA SubCell) — direct fly observation of a cytosolic
  pool; KEEP_AS_NON_CORE (real but secondary; primary compartment is matrix).

No spurious ortholog-transfer over-propagations are present in the fly GOA (unlike human, which
had glycogen/gluconeogenesis/carnitine Ensembl-Compara transfers). So no REMOVE actions are
warranted here; all annotations are either core, correct-but-non-core, or over-general.

## Core functions summary
1. Medium-chain acyl-CoA dehydrogenase activity (GO:0070991); FAD-dependent, ETF-coupled
   alpha,beta-dehydrogenation of medium-chain acyl-CoA (C6-C12) — first step of mitochondrial
   FAO; in mitochondrial matrix; part of GO:0033539 / GO:0051793.
2. FAD binding (GO:0050660) — obligate flavoprotein cofactor for catalysis.

## Open question (novel, non-core)
PINK1-dependent phosphorylation of Mcad at Ser347 and its catalysis-independent contribution to
rescue of PINK1-null neuromuscular/metabolic phenotypes — mechanism unknown; not annotatable to
a specific GO term yet. Captured as suggested question/experiment.
</content>
</invoke>
