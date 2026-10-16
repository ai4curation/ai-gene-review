# ESP1 (YGR098C, UniProt Q03018) — curation notes

Budding-yeast separase. Review completed 2026-09-25 against the SGD GOA seed (41 rows),
the falcon deep-research report and the cached publications.

## Identity and biochemistry

- 1,630-aa CD-clan caspase-like cysteine endopeptidase, EC 3.4.22.49; catalytic
  His1505/Cys1531 in the C-terminal peptidase C50 domain; four N-terminal alpha-helical
  domains (I–IV) and a substrate-binding domain precede the catalytic domain
  [PMID:28146474 "The α-helical region of separase (also known as Esp1) contains four domains (I-IV), and a substrate-binding domain immediately precedes the catalytic domain and has tight associations with it."].
- First shown to be a cysteine protease that cleaves Scc1 on its own in vitro
  [PMID:11081625 "separin is a cysteine protease related to caspases that alone can cleave Sccl in vitro"].
- Cleavage after arginine in (D/E)xxR motifs; two Scc1 sites, two Rec8 sites, one Slk19
  site (deep research, Sullivan et al. 2004 — not cached).

## Regulation by Pds1/securin and the APC/C

- Esp1 forms a stable complex with Pds1; APC/C-mediated Pds1 destruction is the anaphase
  trigger [PMID:9635435 "Pds1p forms a stable complex with a 180 kDa protein called Esp1p, which is essential for the dissociation of Scc1p from sister chromatids and for their separation"].
- Securin has a dual role: it inhibits the protease and blocks substrate binding, but is
  also required and sufficient for nuclear accumulation of separase and for full activity
  after its own destruction [PMID:12123570 "securin is required and sufficient to cause accumulation of separase in the nucleus, where its known cleavage targets reside"].
- Crystal structures (2.6 Å): securin residues 258–373 run the full length of separase and
  258–269 occupy the active site as a pseudosubstrate
  [PMID:28146474 "Most importantly, residues 258-269 of securin are located in the separase active site, illuminating the mechanism of inhibition"].
- Residual securin still restrains separase in anaphase; APC/C-Cdh1 clears it at telophase
  [PMID:27418100 "APC/C-Cdh1-mediated securin degradation at telophase further liberated separase, which promotes Cdc14 release and mitotic exit"].

## Localisation

- Esp1-GFP: cytoplasmic early, accumulates in the nucleus in G2 (Pds1-dependent), then on SPBs
  and spindle midzone at anaphase onset
  [PMID:11149918 "The protein accumulates in the nucleus in G2 and is mobilized onto the spindle pole bodies and spindle midzone at anaphase onset, where it persists into midanaphase"].
- SPB association confirmed by colocalisation with Spc29-CFP; spindle by CFP-Tub1
  [PMID:11149918 "The association of Esp1 with SPBs and spindle was confirmed in colocalization experiments with strains expressing galactose-inducible Esp1GFP and endogenous levels of the SPB marker Spc29 fused to CFP"].
- Two mitochondrial-proteome HDA rows (PMID:14576278, PMID:16823961) have no Esp1-specific
  content; no directed study places Esp1 in mitochondria (the apoptosis paper moves the
  cleaved Mcd1 fragment, not Esp1, to mitochondria). Graded REMOVE as probable co-purification.

## Meiosis

- Rec8 cleavage by separin is necessary for chiasma resolution and homologue disjunction
  [PMID:11081626 "cleavage of Rec8 by separin at one of two different sites is necessary for the resolution of chiasmata and the disjunction of homologous chromosomes during meiosis"].
- SGD annotated this paper to "meiosis II" (IDA + IMP). The abstract foregrounds meiosis I;
  the full text (not cached) presumably includes the meiosis II centromeric Rec8 cleavage
  data. Graded MODIFY -> GO:0051307 meiotic chromosome separation (covers both divisions and
  names the step Esp1 performs), not REMOVE.
- The NAS row from PMID:38413836 (Koch et al. 2024 meiotic phosphoproteome): the cached full
  text has no sentence naming Esp1/separase; accepted on the strength of PMID:11081626, with
  the reference flagged UNVERIFIED for that specific statement.

## Anaphase spindle elongation (protease-dependent, cohesin-independent)

- Stringent esp1 ts alleles across the ORF block spindle elongation even when Mcd1 is
  depleted or TEV-cleaved; esp1-C1531S cannot rescue
  [PMID:18430955 "Therefore, like Mcd1 cleavage, anaphase spindle elongation functions of Esp1 require endoproteolytic activity"].
- Slk19 is a substrate but non-cleavable Slk19 does not phenocopy; the relevant substrate is
  unknown. Curators used "regulation of mitotic spindle elongation" — appropriate, ACCEPTed.

## FEAR network / mitotic exit (non-proteolytic)

- Esp1 acts upstream of Slk19, parallel to Spo12/Bns1; esp1-1 delays Cdc14 release and
  mitotic exit even in mcd1-1
  [PMID:14551257 "In summary our epistasis analyses indicate that ESP1 and SLK19 function in the same pathway and that SLK19 functions downstream of ESP1"];
  protease activity not required
  [PMID:14551257 "Esp1's protease activity seems not to be required for its mitotic exit function"].
- Mechanism: separase interacts with and down-regulates PP2A-Cdc55, permitting Cdk-dependent
  Net1 phosphorylation [PMID:16713564 "The sister chromatid-separating protease separase, activated at anaphase onset, interacts with and downregulates PP2A(Cdc55), thereby facilitating Cdk-dependent Net1 phosphorylation"];
  Zds1/Zds2 act downstream [PMID:18762578 "Zds1 and Zds2 are required downstream of separase to facilitate nucleolar Cdc14 release"];
  direct inhibition judged unlikely on stoichiometric grounds
  [PMID:18762578 "A model by which separase binding to PP2ACdc55 directly inhibits its phosphatase activity nevertheless appears unlikely, as PP2ACdc55 is present in a large stoichiometric excess over separase."].
- Because the MF behind the Cdc55 interaction is unresolved, the two Cdc55 protein-binding IPI
  rows were REMOVEd as uninformative rather than MODIFIED to a phosphatase-inhibitor term; the
  FEAR biology is carried by GO:0031536 and GO:1904750 (all ACCEPTed).

## Apoptosis row

- H2O2-induced death: Esp1 released from Pds1 cleaves Mcd1; Esp1 depletion blocks cleavage
  [PMID:18321989 "No obvious Mcd1 decrease was observed in the presence of H 2 O 2 when Esp1 was depleted"].
  Esp1 performs the step, so participation holds; single study, stress-specific ->
  KEEP_AS_NON_CORE (contrast: human ESPL1 apoptosis TAS was REMOVEd because caspases, not
  separase, cleave RAD21 there).

## Protein-binding (GO:0005515) policy applied

- Pds1 partners (PMID:18719252 Y2H; PMID:28146474 structure): REMOVE; complex captured by
  GO:1990520 (ACCEPT).
- Cdc55 partners (PMID:16713564; PMID:18762578): REMOVE (see above). No Scc1-substrate IPI rows
  exist in the seed, so no MODIFY-to-GO:0004197 was needed.

## Action tally (41 rows)

ACCEPT 31 · MODIFY 3 (nuclear division IEA -> GO:0051306; meiosis II IDA/IMP -> GO:0051307) ·
REMOVE 6 (4 protein binding, 2 mitochondrion HDA) · KEEP_AS_NON_CORE 1 (apoptotic process).

## Open items

- Identity of the spindle-elongation substrate.
- Whether an MF term for the FEAR/PP2A-Cdc55 role is justified (scaffold vs inhibitor).
- Ty1 retrotransposition role (Ho et al. 2015, not cached) not represented in GOA; not
  proposed as NEW pending comparator check.
