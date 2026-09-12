# GNMT (human) — curation notes

UniProt: Q14749 (GNMT_HUMAN), HGNC:4415, EC 2.1.1.20. 295 aa.

## Function (verified)

GNMT is glycine N-methyltransferase, a class I-like SAM-dependent methyltransferase.
It transfers a methyl group from S-adenosyl-L-methionine (AdoMet/SAM) to glycine,
producing sarcosine (N-methylglycine) and S-adenosyl-L-homocysteine (AdoHcy/SAH)
[RHEA:19937, EC:2.1.1.20]. UniProt FUNCTION: "Catalyzes the methylation of glycine by
using S-adenosylmethionine (AdoMet) to form N-methylglycine (sarcosine) with the
concomitant production of S-adenosylhomocysteine (AdoHcy), a reaction regulated by the
binding of 5-methyltetrahydrofolate. Plays an important role in the regulation of methyl
group metabolism by regulating the ratio between S-adenosyl-L-methionine and
S-adenosyl-L-homocysteine." [file:human/GNMT/GNMT-uniprot.txt]

Physiological role: rather than a biosynthetic route to sarcosine, GNMT's main role is to
regulate cellular methylation capacity (the SAM:SAH ratio) by disposing of excess SAM.
It is highly abundant, mainly hepatic (also pancreas, prostate) [UniProt TISSUE
SPECIFICITY, PMID:9495250]. It is feedback-inhibited by 5-methyltetrahydrofolate
(pentaglutamate > monoglutamate), coupling one-carbon/folate status to methyl-group
disposal [UniProt ACTIVITY REGULATION, from ortholog P13255].

## Structure / subunit

Homotetramer [UniProt SUBUNIT, PMID:15340920, PMID:17660255]. Crystal structures of human
enzyme (PDB 1R74, 2AZT). Ogawa 1993 (PMID:8281755): "The enzymes from human, rat, rabbit
and pig livers are all tetramers and exhibit positive cooperativity toward
S-adenosylmethionine and Michaelis-Menten kinetics toward glycine." Two 5-methyl-THF
molecules bound per tetramer, at intersubunit sites.

## Kinetics

KM ~281 uM for SAM, ~12.2 uM for glycine [UniProt, PMID:14651980]. All GNMTs display
hyperbolic kinetics at neutral pH toward both substrates SAM and glycine [PMID:14651980].

## Disease

GNMT deficiency (hypermethioninemia; MIM:606664). Patients show mild hepatomegaly /
chronic elevation of serum transaminases and elevated methionine + SAM with normal
sarcosine [PMID:14739680, PMID:11810299]. Disease variants L49P (10% activity), N140S
(<0.5% activity), H176N (75% activity; destabilizes tetramer) [PMID:14651980,
PMID:17660255].

## Localization

Cytoplasm/cytosol [UniProt SUBCELLULAR LOCATION; HPA IDA GO:0005829; Reactome
R-HSA-6798317].

## Annotation review decisions (summary)

- Core MF: GO:0017174 glycine N-methyltransferase activity (EXP/IDA/IBA/IEA) — ACCEPT.
- Substrate binding MFs (GO:0016594 glycine binding, GO:1904047 SAM binding) — ACCEPT
  (mechanistic components of the MF).
- BP: GO:0046500 S-adenosylmethionine metabolic process, GO:0006730 one-carbon metabolic
  process — ACCEPT as core process context.
- GO:0006111 regulation of gluconeogenesis (IBA) — KEEP_AS_NON_CORE (secondary/indirect,
  from mouse Gnmt phenotype; not the enzyme's direct MF-derived process).
- GO:0051289 protein homotetramerization — ACCEPT (well-established quaternary structure).
- GO:0042802 identical protein binding IPIs where the partner is GNMT itself
  (UniProtKB:Q14749) — ACCEPT/KEEP: consistent with homotetramer.
- GO:0005515 protein binding IPIs (high-throughput interactome hits with ARRB1, NTAQ1,
  SNRNP200, etc.) — MARK_AS_OVER_ANNOTATED per policy (uninformative bare protein binding).
- Cytosol/cytoplasm (GO:0005829, GO:0005737) — ACCEPT.

## Notes on GO term availability (for core_functions)

- GO:0006577 is "amino-acid betaine metabolic process", NOT sarcosine biosynthesis.
- GO:1901052 (sarcosine metabolic process), GO:1901054 (sarcosine biosynthetic process),
  GO:0046498 (S-adenosylhomocysteine metabolic process) are all OBSOLETE.
- Live BP terms used for core_functions: GO:0046500 (SAM metabolic process),
  GO:0032259 (methylation), GO:0006730 (one-carbon metabolic process).
