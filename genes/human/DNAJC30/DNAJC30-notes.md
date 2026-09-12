# DNAJC30 (WBSCR18) research notes

## Identity
- UniProt Q96LL9 (DJC30_HUMAN), 226 aa precursor. HGNC:16410. Synonym WBSCR18 (Williams-Beuren syndrome chromosomal region 18 protein). Located in 7q11.23 WBS critical region.
- Mitochondrial J-domain (HSP40/DnaJ subfamily C) protein. N-terminal mitochondrial transit peptide (1-38); J domain 49-114; single-pass transmembrane helix 208-225. Inner mitochondrial membrane.

## Function (well-supported)
- Mitochondrial inner-membrane protein; auxiliary component of the ATP synthase machinery; facilitates ATP synthesis.
  [PMID:30318146 "we identify DNAJC30 as an auxiliary component of ATP-synthase machinery"; "the 7q11.23 protein DNAJC30, which interacts with mitochondrial ATP-synthase machinery."]
  [UniProt FUNCTION "Associates with the ATP synthase complex and facilitates ATP synthesis (By similarity)."]
- Chaperone in complex I (NADH:ubiquinone oxidoreductase) "repair": facilitates the efficient exchange/turnover of complex I N-module subunits damaged by reactive oxygen species, integral to a complex I repair mechanism; contributes to complex I functional efficiency.
  [PMID:33465056 "DNAJC30 is a chaperone protein needed for the efficient exchange of complex I subunits exposed to reactive oxygen species and integral to a mitochondrial complex I repair mechanism"]
  [UniProt FUNCTION "May be a chaperone protein involved in the turnover of the subunits of mitochondrial complex I N-module. It facilitates the degradation of N-module subunits damaged by oxidative stress, and contributes to complex I functional efficiency (PubMed:33465056)."]

## Interactions
- Direct interaction with MT-ATP6 (P00846) and ATP5MC2 (Q06055); associates with ATP synthase complex (PMID:30318146).
- Large set of binary HuRI interactions (PMID:32296183) with mostly membrane proteins (AQP6, BEST2, EBP, MGST2, MRM1, etc.) — likely membrane-protein Y2H artifacts, uninformative bare protein binding.

## Localization
- Mitochondrion inner membrane (IDA, PMID:30318146); single-pass membrane protein.
- HTP mitochondrion (PMID:34800366, FlyBase high-throughput).
- Highly expressed in brain; enriched in pyramidal neurons.

## Disease
- Autosomal-recessive Leber hereditary optic neuropathy (LHONAR1/arLHON, MIM:619382): biallelic DNAJC30 mutations (e.g. Y51C, P78S, L101Q) recapitulate all hallmarks of mtDNA LHON (incomplete penetrance, male predominance, idebenone responsivity). Variants reduce turnover of complex I N-module subunits and impair complex I function.
  [PMID:33465056 "We describe biallelic mutations in a nuclear encoded gene, DNAJC30, in 33 unsolved patients from 29 families and establish an autosomal recessive mode of inheritance for LHON (arLHON)"]
- DNAJC30 deletion contributes to mitochondrial dysfunction in Williams-Beuren syndrome neurodevelopmental phenotypes (PMID:30318146).

## GO annotation review reasoning
- mitochondrial inner membrane (IDA, IEA) — ACCEPT (core localization, experimentally demonstrated).
- mitochondrion (HTP) — ACCEPT (consistent, less specific).
- regulation of mitochondrial ATP synthesis coupled proton transport (ISS/IEA from mouse P59041) — ACCEPT; supported by ATP synthase association and facilitation of ATP synthesis.
- brain development (ISS/IEA) — KEEP_AS_NON_CORE; reflects neurodevelopmental phenotype/high brain expression but is a downstream pleiotropic outcome, not the molecular core.
- protein binding (IPI) — the MT-ATP6/ATP5MC2 interactions (PMID:30318146) are biologically meaningful (ATP synthase) — could MODIFY toward a specific term; the HuRI set (PMID:32296183) is uninformative -> KEEP_AS_NON_CORE.
- Core MF: chaperone/co-chaperone activity in complex I subunit exchange + ATP synthase auxiliary subunit. Best MF terms: protein-folding chaperone binding / unfolded protein binding not directly shown; the gene acts as a holdase/chaperone facilitating subunit exchange. The clearest experimentally-grounded MF for the ATP-synthase role is enzyme/structural association; for complex I it's chaperone activity. Use GO:0051082 unfolded protein binding? Not demonstrated. Better core: biological processes (complex I repair / ATP synthesis regulation). For MF, GO:0140662? (ATP-dependent protein folding chaperone) is not apt (it's not ATP-dependent foldase). Will use a chaperone-binding/holdase framing carefully.
