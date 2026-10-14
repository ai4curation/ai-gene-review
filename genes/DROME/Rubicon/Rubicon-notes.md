# Rubicon (CG12772, FBgn0030055, UniProt Q9W3C9) notes

## Identity and architecture

- UniProt Q9W3C9 (unreviewed, 827 aa) is the single Drosophila member of PANTHER PTHR45971 (subfamily SF1 "RUBICON, ISOFORM A"). It carries an N-terminal RUN domain (CDD cd17686 RUN_RUBCN), PI3K-binding (PIKBD, Pfam PF21054) segments and a C-terminal Rubicon-homology (RH) domain [file:DROME/Rubicon/Rubicon-uniprot.txt, "DOMAIN          619..826"; file:DROME/Rubicon/Rubicon-uniprot.txt, "CDD; cd17686; RUN_RUBCN; 1."].
- Architecture comparison (see file:worm/Y56A3A.16/Y56A3A.16-bioinformatics/RESULTS.md): fly Rubicon has RUN 50-207, PIKBD 458-483/514-579 and RH 619-826, i.e. the full human RUBCN layout; human Pacer (RUBCNL) lacks a RUN domain. Fly aligns with RUBCN over 733 columns (34.4% identity, score 724) versus a much shorter alignment with Pacer (257 columns). Architecturally the fly protein is Rubicon-like and represents the pre-duplication (single-copy) state; the RUBCN/RUBCNL split is vertebrate (PAINT nodes PTN002915566 and PTN002915558 both at Euteleostomi, taxon:117571).
- Oba et al. 2021 also note the shared architecture: "both human and Drosophila Rubicon bear N-terminal RUN" [PMID:34189208].

## Negative regulation of canonical autophagy (Rubicon-like)

- Nakamura et al. 2019 [PMID:30783089]: dRubicon protein rises with age ("the dRubicon was significantly upregulated in middle-aged female fly (Day 14) compared to young fly (Day 2)"); "Systemic knockdown of dRubicon significantly increased steady-state autophagosome and autolysosome pools in the brain (Fig. 4c, d)." Neuronal knockdown extended female lifespan and reduced polyQ inclusions ("Neuronal knockdown of dRubicon extends lifespan in female fly"). This is the vertebrate-RUBCN behaviour (negative regulator), not Pacer-like (positive).
- Oba et al. 2021 [PMID:34189208] (data brief): "Previously, we focused on Rubicon, a negative regulator of autophagy, and demonstrated that knockdown of the Drosophila homolog of Rubicon (dRubicon) suppressed locomotor dysfunction in a fly model of polyQ disease." Overexpression (WT vs delta-RUN) data on polyQ toxicity: "an increase in Rubicon exacerbates the toxicity of the polyQ protein".

## LC3-associated phagocytosis (positive, also Rubicon-like)

- Szabó et al. 2023 [PMID:37248218] (full text): Rubicon RNAi, CRISPR frameshift alleles and glial tissue-specific KO all impair clearance of engulfed axon debris in wing-nerve glia ("Similar to Rubicon RNAi, Rubiconfs1 hemizygotes and Rubiconfs1/fs2 trans-heterozygotes failed to clear axon debris in injured nerves"); glial overexpression accelerates clearance ("increasing Rubicon level is sufficient to boost debris clearance"). The defect is at the degradation/maturation step: "glial loss of a subset of autophagy genes and of Rubicon impairs debris elimination and phagosome-lysosome fusion".
- Localisation (tagged, overexpressed Rubicon::mRFP in glia): punctate, "rarely overlapped with Rab5-positive early endosomes/phagosomes or Lamp1-marked lysosomes"; "almost all Rubicon dots colocalized with Rab7-positive late endosomes/phagosomes"; colocalises with engulfed debris "indicating that engulfed axon fragments are contained in LAPosomes" [PMID:37248218].
- Ben-Hur et al. 2024 [PMID:38977659]: maternal Rubicon on egg multivesicular bodies drives an LAP-like pathway that eliminates the sperm mitochondrial derivative (paternal mitochondrial elimination). "We demonstrate that mutants and RNAi knockdown of the LAP-specific PI3KC3 component, Rubicon, as well as knockdown of three other main components of the complex, all significantly attenuate degradation of the MD." Rubicon-eGFP "is primarily located at the limiting membrane of the MVBs"; Rubicon is needed for PtdIns(3)P production and Atg8a recruitment on flagellar vesicular sheaths ("Atg8a recruitment to the FVS requires both Rubicon and Atg7").

## Interpretation

- Both arms of vertebrate RUBCN biology are present in fly: inhibition of canonical autophagy (aging/neurons) and promotion of LAP/LAP-like single-membrane Atg8ylation (glia, egg). No fly evidence for Pacer-type promotion of canonical autophagosome maturation. Fly Rubicon therefore behaves like vertebrate Rubicon.
- Direct biochemistry (VPS34/UVRAG binding, Rab7 binding, lipid binding) is not demonstrated for the fly protein; these are inferred from human RUBCN and the conserved RUN/PIKBD/RH domains.
- GO:1901981 (phosphatidylinositol phosphate binding, IBA from root PTN002915557) is seeded only by human Pacer; human RUBCN itself has no direct PIP-binding evidence and the Pacer PIP-binding region is unmapped. Marked MARK_AS_OVER_ANNOTATED in the review (updated from an earlier "kept as non-core" call): the seed is the vertebrate Pacer paralog only, direct lipid binding is not shown for fly Rubicon, and human Rubicon was not pulled down by PtdIns(3)P beads, so the term is treated as an over-propagation from the Pacer lineage, matching the human and mouse RUBCN reviews.
- GO:0043231 (intracellular membrane-bounded organelle, root IBD, fly is a seed) is correct but very general; the specific compartments are late endosome/phagosome (glia) and MVB limiting membrane (egg). Not yet in fly GOA.

## Literature search

- PubMed esearch "Rubicon AND Drosophila" (2026-10-10) returned PMID:38977659, 37248218, 34189208, 30783089 (plus an unrelated genome-assembly paper). No fat-body endocytosis/autophagosome-maturation paper on fly Rubicon was found (no Banta or Tabata paper on fly Rubicon was retrieved by this search).
- No falcon deep-research file was present at time of writing.
