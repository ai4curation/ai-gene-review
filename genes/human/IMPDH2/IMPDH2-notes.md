# IMPDH2 (human, UniProtKB:P12268) — review notes

## Summary of gene function

IMPDH2 is inosine-5'-monophosphate dehydrogenase 2 (EC 1.1.1.205), the ubiquitous,
proliferation-associated isozyme of IMP dehydrogenase. It catalyzes the NAD+-dependent
oxidation of IMP to xanthosine-5'-monophosphate (XMP):

    IMP + NAD+ + H2O -> XMP + NADH + H+   (RHEA:11708)

This is the first committed and rate-limiting step of de novo guanine-nucleotide
biosynthesis; GMP synthase (GMPS) then aminates XMP to GMP, and downstream kinases give
GDP/GTP/dGTP. Because de novo GTP supply is tightly coupled to cell proliferation, IMPDH2
is a validated drug target.

## Key established facts (with provenance)

- Enzymatic activity / reaction. UniProt CATALYTIC ACTIVITY: "IMP + NAD(+) + H2O = XMP +
  NADH + H(+)"; EC=1.1.1.205; PATHWAY: "Purine metabolism; XMP biosynthesis via de novo
  pathway; XMP from IMP: step 1/1" [file:human/IMPDH2/IMPDH2-uniprot.txt].
- Kinetics and isozyme comparison. Type II Km(IMP)=9.3 uM, Km(NAD)=32 uM; both type I and
  II are tetramers; product-inhibited by XMP and NADH; MPA inhibits type II with ~4.8-fold
  lower Ki than type I [PMID:7903306 "with Km values of 18 and / 9.3 microM, respectively,
  for IMP, and 46 and 32 microM"; "Both recombinant isoforms were / tetramers"].
- Inhibitor binding. Recombinant type I/II purified from E. coli; MPA is a potent
  tight-binding uncompetitive inhibitor (Ki 11 and 6 nM); mizoribine-5'-monophosphate a
  competitive inhibitor [PMID:7763314].
- Rate-limiting role in de novo GTP/guanine-nucleotide synthesis. "IMP dehydrogenase (EC
  1.1.1.205), the rate-limiting enzyme of de novo GTP / biosynthesis" [PMID:1969416];
  "IMPDH is the rate-limiting enzyme in / the de novo biosynthesis of guanine nucleotides"
  [PMID:14766016].
- Two isoforms / tissue distribution. Two distinct cDNAs (type I=IMPDH1, type II=IMPDH2),
  84% identical, 514 residues; type I predominant in normal leukocytes, type II
  predominates in tumor [PMID:1969416].
- CBS/Bateman subdomain and nucleic-acid binding. The catalytic domain carries a subdomain
  of two CBS (cystathionine-beta-synthase) domains; human IMPDH isoforms bind
  single-stranded nucleic acids with nanomolar affinity via this subdomain; IMPDH found in
  the nucleus and binds RNA and DNA in vivo [PMID:14766016]. This is a secondary,
  moonlighting activity, not the core catalytic function. UniProt features: CBS 1
  (114–173), CBS 2 (179–237) [file:human/IMPDH2/IMPDH2-uniprot.txt].
- Filament / macro-assembly ("rods and rings" / cytoophidia). IMPDH2 polymerizes into
  filaments upon guanine-nucleotide depletion; UniProt: "Can form fiber-like subcellular
  structures termed 'cytoophidia'"; ANKRD9 controls IMPDH2 abundance and macro-assembly
  and drives its ubiquitin-dependent degradation [PMID:31337707; PMID:30293565].
- Subcellular location. Cytosol is the principal, experimentally supported location
  [PMID:31337707 IDA; HPA IDA GO_REF:0000052]. Also reported cytoplasm and nucleus
  [PMID:14766016].
- Regulation / PTMs. Acetylated by CLOCK in a circadian manner; interacts with CLOCK
  [PMID:28985504]. Phosphorylated (S122, S160, Y400, S416), SUMOylated (K195/K208/K438),
  ubiquitinated (ANKRD9/proteasome).
- Pharmacology. Principal target of the immunosuppressant mycophenolic acid /
  mycophenolate mofetil and the antiviral ribavirin; also tiazofurin, mizoribine
  [file:human/IMPDH2/IMPDH2-uniprot.txt; PMID:7763314; PMID:7903306].
- Disease. Variants cause an autosomal-dominant neurodevelopmental disorder with dystonia
  (IMPDH2-related dystonia / DYT; MIM:617995 in UniProt entry; Orphanet
  dopa-responsive-dystonia cross-ref). The L263F polymorphism reduces activity ~10-fold
  [PMID:17496727 via UniProt].

## Annotation review reasoning (per-annotation notes)

- Core molecular function: GO:0003938 IMP dehydrogenase activity — multiple, mutually
  reinforcing lines (EXP PMID:7763314, IDA PMID:7903306, TAS PMID:1969416, IBA, IEA). All
  ACCEPT; this is THE core function.
- BP: de novo guanine-nucleotide synthesis. GOA has GO:0006183 (GTP biosynthetic process,
  IBA + IDA), GO:0006177 (GMP biosynthetic process, IEA), GO:0006164 (purine nucleotide
  biosynthetic process, IEA), GO:0097294 ('de novo' XMP biosynthetic process, IEA). The
  reaction product is XMP directly; GMP/GTP synthesis follows downstream. The most precise
  process term for the catalyzed step is 'de novo' XMP biosynthetic process; GMP/GTP
  biosynthetic process are correct one-step-removed pathway terms. All ACCEPT (the enzyme
  is genuinely the committed/rate-limiting step and is standardly annotated to the guanine
  nucleotide pathway); purine nucleotide biosynthetic process is broader but correct.
- Nucleotide binding (GO:0000166) / NAD binding: substrate/cosubstrate binding. NAD is a
  cosubstrate. ACCEPT the IDA (PMID:14766016 reports nucleic-acid binding but the
  large-scale entry has NAD/IMP binding features). Note: GO:0000166 nucleotide binding is
  generic; kept as supporting, non-core.
- metal ion binding (GO:0046872) / K+ binding: UniProt documents K(+) cofactor and
  multiple K+ binding sites (shared between tetrameric partners). ACCEPT the IEA as
  consistent with structural evidence.
- catalytic activity (GO:0003824), oxidoreductase activity (GO:0016491): correct but
  uninformative parents of GO:0003938. MARK_AS_OVER_ANNOTATED (root/parent-level IEA).
- Localization CC terms:
  - cytosol (GO:0005829): ACCEPT (IDA x2 + IEA) — core location.
  - cytoplasm (GO:0005737): ACCEPT (IBA/IDA/IEA) — broader but correct.
  - nucleus (GO:0005634): IDA PMID:14766016 (nucleic-acid binding context) + IEA. KEEP as
    non-core / minor pool; genuine but secondary.
  - membrane (GO:0016020), peroxisomal membrane (GO:0005778), extracellular exosome
    (GO:0070062), extracellular region (GO:0005576), secretory granule lumen (GO:0034774),
    ficolin-1-rich granule lumen (GO:1904813): high-throughput proteomics / Reactome
    neutrophil-degranulation propagation. IMPDH2 is a soluble cytosolic enzyme with no TM
    segment, signal peptide, or PTS. These are contaminant / bystander / pathway-membership
    localizations, not bona fide functional locations. MARK_AS_OVER_ANNOTATED (HDA/TAS,
    not clearly-wrong IEA, so not REMOVE per policy).
- protein binding (GO:0005515) IPIs (PMID:25416956, 32296183, 38884001, 28985504): bare
  "protein binding" from large-scale Y2H / HuRI / HaloMS / interactome screens — per
  curation policy, uninformative; MARK_AS_OVER_ANNOTATED (do not REMOVE experimental IPIs).
- circadian rhythm (GO:0007623) IDA PMID:28985504: IMPDH2 identified as a CLOCK acetylation
  substrate in a paper about circadian ureagenesis. The abstract shows IMPDH2 is a CLOCK
  substrate but does not establish IMPDH2 itself functions in the circadian clock; the
  process is a regulatory context. KEEP_AS_NON_CORE.
- 'de novo' XMP biosynthetic process (GO:0097294) IEA: most precise BP for the catalyzed
  step. ACCEPT.

## Deep research

Falcon deep research was NOT run for this gene (provider out of credits, HTTP 402). No
-deep-research-*.md file exists. Review grounded in UniProt (P12268), the seeded GOA, and
cached publications/PMID_*.md.
