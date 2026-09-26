# CGAS (Cyclic GMP-AMP synthase) — curation notes

UniProt: Q8N884 | HGNC: CGAS (HGNC:21367) | synonyms: C6orf150, MB21D1 | EC 2.7.7.86
Family: mab-21 family / cGAS-DncV-like nucleotidyltransferase (cGLR); OAS1-like NTase + Mab21 domain.

Provenance note: `just deep-research` was attempted with `--provider perplexity` (not
configured; only `falcon` and `openscientist` available) and then `--provider falcon`.
Findings below are drawn from the cached UniProt record and cached `publications/PMID_*.md`
full texts/abstracts, with inline provenance. No `-deep-research-<provider>.md` file was
fabricated.

## Core molecular function

cGAS is a cytosolic double-stranded DNA sensor and a DNA-activated nucleotidyltransferase
that catalyzes synthesis of the cyclic dinucleotide second messenger 2',3'-cGAMP from ATP
and GTP.

- Discovery / cGAMP synthase activity: cGAS was purified as the cGAMP synthase; "cGAS bound
  to DNA in the cytoplasm and catalyzed cGAMP synthesis" and "purified cGAS catalyzes the
  synthesis of cGAMP from ATP and GTP" [PMID:23258413 "purified cGAS catalyzes the synthesis of cGAMP from ATP and GTP"].
  The synthesis requires both ATP and GTP and is DNA-dependent [PMID:23258413 "The synthesis of cGAMP by cGAS required both ATP and GTP, but not CTP or UTP"].
- The product is specifically 2',3'-cGAMP with mixed 2'-5'/3'-5' linkages: catalysis
  "involves both the formation of a 2',5' phosphodiester linkage at the GpA step and the
  formation of a 3',5' phosphodiester linkage at the ApG step, producing c[G(2',5')pA(3',5')p]"
  (UniProt FUNCTION; structural basis in [PMID:38740774] and [PMID:28214358]).
- 2',3'-cGAMP is the endogenous second messenger [PMID:23258412 second-messenger paper];
  the noncanonical 2',3' linkage is the universal metazoan signal [PMID:26300263].
- EC 2.7.7.86; RHEA:42064. Many independent EXP/IDA confirmations (PMID:23707061, 23722159,
  25131990, 28934246, 29976794, 30799039, 31142647, 32814054, 37802025, and others).

## DNA binding / activation mechanism

- Directly binds dsDNA in a sequence-independent, length-dependent manner; the catalytic
  domain + N-terminal disordered region both contribute [PMID:23258413; PMID:28363908].
- DNA binding drives liquid-liquid phase separation (LLPS): "DNA binding to cGAS robustly
  induced the formation of liquidlike droplets in which cGAS was activated" and "The
  disordered and positively charged cGAS N terminus enhanced cGAS-DNA phase separation by
  increasing the valencies of DNA binding" [PMID:29976794]. These DNA-cGAS condensates are
  the sites of activation → basis of GO:0140693 molecular condensate scaffold activity
  (also PMID:32911482, 32912999, 35322803, 38421872, 38740774, 39322678).
- Forms a 2:2 dimer with dsDNA (structural: PMID:30007416, 30799039, 31142647).
- Human cGAS preferentially recognizes curved long dsDNA (>~40 bp) via K187/L195 substitutions
  [UniProt DOMAIN; PMID:30007416].

## Downstream pathway (cGAS/STING)

- cGAMP binds and activates STING1 (TMEM173), triggering TBK1/IRF3 and type I interferon
  (IFN-beta) production: "cGAS functions upstream of STING and is required for IFNβ induction
  by cytosolic DNA" [PMID:23258413]. This is the cGAS/STING signaling pathway (GO:0140896) and
  positive regulation of type I interferon production (GO:0032481).
- Defense against DNA viruses (HSV-1, vaccinia) [PMID:23258413] and retroviruses (HIV-2;
  HIV-1 poorly sensed due to capsid cloaking) [PMID:23929945; PMID:26046437 PQBP1 co-sensor].
- Paracrine/bystander spread: "cGAMP(2'-5') is transferred from producing cells to
  neighbouring cells through gap junctions, where it promotes STING activation" [PMID:24077100]
  → basis of GO:0038001 paracrine signaling.

## Sensing endogenous/self DNA and sterile inflammation

- Surveys micronuclei from genome instability: "cGAS localizes to micronuclei arising from
  genome instability" [PMID:28738408]; links genome instability/DNA damage to innate immunity.
- Cellular senescence (SASP via cytoplasmic chromatin fragments) — mouse ISS (GO:2000774).
- Sensed in autoinflammatory disease from defective histone pre-mRNA processing [PMID:33230297].

## Nuclear cGAS, chromatin/nucleosome inhibition, and DNA-repair suppression

- cGAS is predominantly nuclear at steady state and tightly tethered to chromatin to prevent
  autoreactivity [PMID:31808743; PMID:32792394 BAF]; localizes to nucleus (many EXP: PMID:29263269,
  30270045, 30811988, 31299200, 31808743, 33476576, 34111399, 35438208) and chromosomes/centromeres
  (PMID:30811988, 31299200, 31544964, 32351706, 32912999, 33051594).
- Nucleosome binding inactivates cGAS: cGAS binds the histone H2A-H2B acidic patch via an
  arginine anchor, blocking DNA binding/activation — structural basis established by multiple
  cryo-EM studies [PMID:32911482; PMID:32912999 "two cGAS monomers bridge two NCPs by binding
  the acidic patch of the histone H2A-H2B dimer and nucleosomal DNA"; PMID:33051594]. This is
  the mechanism of GO:0031491 nucleosome binding and (uninformatively) chromatin binding.
- Enzyme-independent nuclear moonlighting function: nuclear cGAS suppresses homologous
  recombination and promotes tumorigenesis: "Here we demonstrate that cGAS inhibits homologous
  recombination in mouse and human models" [PMID:30356214]; "cGAS is a chromatin-bound protein
  that restrains HR and that this function is independent of its enzymatic activity or the
  canonical STING-IFN-I pathway" [PMID:31544964]. It interacts with PARP1 and impedes the
  PARP1-TIMELESS complex [PMID:30356214]. → GO:2000042 (neg reg of DSB repair via HR),
  GO:0045738 (neg reg of DNA repair, mouse IEA), and it localizes to sites of DSB (GO:0035861).

## Regulation / interactors (context; mostly not core function terms)

- Positive: ZCCHC3 co-sensor [PMID:30135424]; PQBP1 (HIV sensing) [PMID:26046437]; G3BP1 promotes
  DNA binding [PMID:30510222]; TRIM56 monoUb K347 [PMID:29426904]; KAT5 acetylation [PMID:32817552];
  HERC5 ISGylation [PMID:38421872]; MYO1F positions cGAS at plasma membrane [PMID:39694035].
- Negative: nucleosomes; PCBP2 antagonizes condensation [PMID:35322803]; PARP1 PARylation
  [PMID:35460603]; acetylation blocks activity [PMID:30799039]; PRMT5 methylation [PMID:33762328];
  CDK1 phosphorylation in mitosis [PMID:32351706, 33542149]; CRL5-SPSB3 degradation [PMID:38418882];
  AARS1/2 lactylation [PMID:39322678]; LYPLAL1 depalmitoylation [PMID:37802025].
- PIP2/PI(4,5)P2 binding positions cGAS at plasma membrane [PMID:30827685] → GO:0005546.
- Metal/cofactor: Mn2+ directly activates cGAS [PMID:32814054]; Zn2+ enhances activity [PMID:29976794].

## Localization summary

Nucleus (predominant, chromatin-tethered), cytosol (activation upon dsDNA), plasma membrane
(peripheral, PIP2/MYO1F-dependent). Cytosol is where cGAS carries out active DNA sensing;
nucleus is where it is largely sequestered/inactivated and performs its enzyme-independent
DNA-repair-suppressing moonlighting role.

## Core-function conclusions (for core_functions block)

1. Double-stranded DNA binding (GO:0003690) — the sensing/input activity.
2. 2',3'-cyclic GMP-AMP synthase activity (GO:0061501) — the catalytic output.
3. Molecular condensate scaffold activity (GO:0140693) — DNA-driven LLPS platform for activation.
4. Process: cGAS/STING signaling pathway (GO:0140896) / activation of innate immune response.

Notable non-core but real: nucleosome binding (inhibitory regulatory), negative regulation of
DSB repair via HR (enzyme-independent nuclear moonlighting), positive regulation of cellular
senescence, paracrine signaling.
