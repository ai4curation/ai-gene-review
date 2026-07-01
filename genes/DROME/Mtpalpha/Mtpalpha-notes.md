# Mtpalpha (Drosophila melanogaster) research notes

UniProt: Q8IPE8 (TrEMBL, unreviewed) — note: the task brief mentioned Q9V397 as an
alternative accession, but the fetched UniProt record and GOA both key on Q8IPE8
(FBgn0028479, CG4389). I use Q8IPE8 throughout to match the derived files.

Gene: Mtpalpha (a.k.a. Mtp alpha, CG4389, Dmel\CG4389); FlyBase FBgn0028479.
Ortholog of human HADHA (mitochondrial trifunctional protein alpha subunit).

## Identity / domain architecture (from UniProt Q8IPE8)

- RecName: Trifunctional enzyme subunit alpha, mitochondrial; EC 1.1.1.211 and EC 4.2.1.17
  [file:DROME/Mtpalpha/Mtpalpha-uniprot.txt lines 6-8].
- AltName: Monolysocardiolipin acyltransferase; AltName: TP-alpha (all ARBA-inferred,
  electronic) [uniprot lines 9-10].
- Two catalytic domains, matching the human alpha subunit: an N-terminal enoyl-CoA
  hydratase/crotonase domain and a central + C-terminal 3-hydroxyacyl-CoA dehydrogenase
  (NAD-binding) domain [uniprot DOMAIN 336..514 "3-hydroxyacyl-CoA dehydrogenase NAD
  binding" and 517..611 "3-hydroxyacyl-CoA dehydrogenase C-terminal"; Pfam PF00378 ECH_1,
  PF02737 3HCDH_N, PF00725 3HCDH].
- ACT_SITE 483 "For hydroxyacyl-coenzyme A dehydrogenase activity"; SITE 123 & 145
  "Important for long-chain enoyl-CoA hydratase activity"; SITE 471 for dehydrogenase.
- SUBUNIT (ARBA): "Heterotetramer of 2 alpha/HADHA and 2 beta/HADHB subunits; forms the
  mitochondrial trifunctional enzyme." [uniprot lines 283-288].
- SUBCELLULAR LOCATION (ARBA): "Mitochondrion inner membrane" [uniprot lines 289-290].
- PATHWAY (ARBA): "Lipid metabolism; fatty acid beta-oxidation." [uniprot lines 281-282].
- SIMILARITY: enoyl-CoA hydratase/isomerase family (N-term) + 3-hydroxyacyl-CoA
  dehydrogenase family (central) [uniprot lines 291-296].

Note: UniProt lists an MLCL (monolysocardiolipin) acyltransferase catalytic-activity block
and the "Monolysocardiolipin acyltransferase" AltName, but ALL of it is ARBA/electronic
(ECO:0000256|ARBA), i.e. inferred by rule/orthology, NOT experimentally demonstrated in
Drosophila. This mirrors the human alpha subunit's demonstrated MLCL acyltransferase /
cardiolipin remodeling moonlighting activity (human HADHA, PMID:23152787, PMID:31604922),
but there is no fly-specific experimental evidence for it.

## Two core enzyme activities are conserved from human HADHA

Human HADHA carries LCEH (EC 4.2.1.17) and LCHAD (EC 1.1.1.211) in the alpha subunit; the
thiolase (3rd) step is on the beta subunit (HADHB). The fly Mtpalpha has the same two-domain
architecture (crotonase + 3-HCDH), so the alpha subunit carries the hydratase and
dehydrogenase but NOT thiolase — thiolase is Mtpbeta's activity. This is why any thiolase MF
annotation on Mtpalpha would be questionable (belongs to the beta subunit). GOA does not in
fact carry a thiolase MF for Mtpalpha, consistent with this.

## Functional evidence in Drosophila

### PMID:22342726 — Kishita, Tsuda, Aigaki 2012 (Drosophila MTP-deficiency model) [abstract-only]
The key functional paper. Generated Mtpα(KO) and Mtpβ(KO) flies.
- "Mitochondrial trifunctional protein (MTP), which consists of the MTPα and MTPβ subunits,
  catalyzes long-chain fatty acid β-oxidation."
- "Both Mtpα(KO) and Mtpβ(KO) flies were viable, but demonstrated reduced lifespan, defective
  locomotor activity, and reduced fecundity..." (supports determination of adult lifespan)
- "Mtpα(KO) flies were hypersensitive to fasting, and retained lipid droplets in their fat
  body cells..." (supports response to starvation)
- "...both Mtpα(KO) and Mtpβ(KO) flies accumulated acylcarnitine and hydroxyacylcarnitine,
  diagnostic markers of MTP deficiencies... both ... were impaired in long-chain fatty acid
  β-oxidation." (supports fatty acid beta-oxidation, IMP)
This is direct loss-of-function (IMP) evidence in the fly for GO:0006635, GO:0008340,
GO:0042594. Full text not cached (full_text_available: false).

### PMID:22758915 — Faust et al. 2012, peroxisomal inventory in Drosophila [abstract-only]
Bioinformatic + limited experimental inventory of Drosophila peroxisomal proteins. FlyBase
used this to make peroxisome localization annotations for Mtpalpha (IDA, ISS transfer from
UniProtKB:Q08426 = rat/mouse ortholog, and ISM prediction). The abstract states "The
subcellular localization of five of these predicted peroxisomal proteins was confirmed."
It does not name Mtpalpha in the abstract; the curator (FlyBase) had the full data. The
peroxisomal localization is plausible for a beta-oxidation enzyme but the primary/canonical
location is the mitochondrion; treat peroxisome as a secondary/non-core location.

### PMID:19884309 — Campos et al. 2010, embryonic epithelial repair screen [abstract avail.]
Forward-genetics transposon-insertion screen for embryonic epithelial (wound) repair;
"identification of 30 lethal insertional mutants with defects in embryonic epithelia repair."
The abstract foregrounds karst/beta-Heavy-spectrin, DJUN and scab, and does NOT name
Mtpalpha, but FlyBase made the GO:0042060 (wound healing) annotation with evidence code HMP
(inferred from high-throughput mutant phenotype) from this screen — i.e., Mtpalpha was one of
the 30 insertional hits. This is a high-throughput screen hit, not a focused study of
Mtpalpha's role in wound healing; energy metabolism / beta-oxidation defects can pleiotropically
disrupt many developmental processes, so this is best treated as non-core (KEEP_AS_NON_CORE).

### Localization / proteomics
- PMID:19317464 (Tan et al. 2009, LOPIT organelle mapping of Drosophila embryos) — HDA
  mitochondrion. Abstract-only; large-scale organelle map.
- PMID:16212416 (Alonso et al. 2005, Drosophila mitochondrial proteome) — HDA mitochondrion.
  Abstract-only; 2D-gel/MALDI-TOF mitochondrial proteome. Both support GO:0005739
  (mitochondrion). The specific/core location is the mitochondrial inner membrane
  (GO:0005743), and complex membership is GO:0016507.

## Retinal degeneration / photoreceptor context
Task suggested a fly retinal-degeneration angle. WebSearch (July 2026) did not surface any
paper specifically linking Mtpalpha/CG4389 to photoreceptor degeneration; the human ortholog
HADHA (LCHAD/MTP) deficiency causes pigmentary retinopathy, but I found no citable fly-specific
Mtpalpha retinal study. I therefore do NOT add a retinal-degeneration annotation; it would be
unsupported. (General fly mito-dysfunction retinal-degeneration reviews exist but do not
implicate this gene.)

## Annotation-review plan (summary)
- MF hydratase (GO:0004300, ISS from UniProtKB:Q64428 rat MTP alpha; also IEA) — ACCEPT, core.
- MF long-chain 3-hydroxyacyl-CoA dehydrogenase (GO:0016509, ISS + IEA) — ACCEPT, core.
- MF generic (3S)-3-hydroxyacyl-CoA dehydrogenase (GO:0003857, IEA) — MODIFY -> GO:0016509
  (long-chain specific), as done for human HADHA.
- MF 3-hydroxyacyl-CoA dehydratase (GO:0018812, RHEA IEA) — MODIFY -> GO:0004300 (reverse
  framing of the hydratase reaction), as done for human HADHA.
- MF broad/parent terms GO:0003824 catalytic activity, GO:0016491 oxidoreductase,
  GO:0016616 (CH-OH donor, NAD/NADP), GO:0070403 NAD+ binding — KEEP_AS_NON_CORE.
- BP fatty acid beta-oxidation (GO:0006635; IMP PMID:22342726 + ISS + IEA) — ACCEPT, core.
- BP fatty acid metabolic process (GO:0006631, IEA) — KEEP_AS_NON_CORE (parent).
- BP determination of adult lifespan (GO:0008340, IMP PMID:22342726) — KEEP_AS_NON_CORE
  (downstream/pleiotropic consequence of beta-oxidation deficiency).
- BP response to starvation (GO:0042594, IMP PMID:22342726) — KEEP_AS_NON_CORE (physiological
  consequence; fly can't mobilize lipid without FAO).
- BP wound healing (GO:0042060, HMP PMID:19884309) — KEEP_AS_NON_CORE (HT screen hit;
  pleiotropic, not a direct molecular role).
- CC mitochondrial inner membrane (GO:0005743, IEA) — ACCEPT, core.
- CC mitochondrion (GO:0005739; HDA PMID:19317464, PMID:16212416; ISM PMID:22758915) —
  KEEP_AS_NON_CORE (less specific than inner membrane).
- CC mitochondrial FAO multienzyme complex (GO:0016507, part_of, IEA) — ACCEPT, core.
- CC peroxisome (GO:0005777; IDA, ISS, ISM PMID:22758915) — KEEP_AS_NON_CORE (secondary
  localization; canonical location is mitochondrion).

## Core functions
1. Enoyl-CoA hydratase (GO:0004300) in FAO, in the MTP complex, at the inner membrane.
2. Long-chain 3-hydroxyacyl-CoA dehydrogenase (GO:0016509) in FAO, in the MTP complex.
(Not proposing an MLCL-acyltransferase core function for the fly: only ARBA/electronic,
no fly experimental evidence. Noted as a suggested question/experiment instead.)
</content>
</invoke>
