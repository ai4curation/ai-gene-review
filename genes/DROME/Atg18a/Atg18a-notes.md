# Atg18a (Drosophila melanogaster) review notes

## Entry and fetch

- FlyBase FBgn0035850, CG7986. UniProt has four unreviewed entries for the gene: M9PER1
  (isoform E, 447 aa), M9PEY7 (isoform D), M9PHS3 (isoform F) and Q9VSF0 (isoforms A/B/C/G,
  377 aa). Only M9PER1 carries the full set of GOA rows (31, including all PAINT IBA rows);
  Q9VSF0 and the other two carry only the 13 FlyBase IMP rows plus an ARBA cytoplasm row.
  `just fetch-gene DROME Atg18a` resolves M9PER1, which is the right accession for this review.
- On 2026-11-16 QuickGO's annotation search failed for any request that asked for
  `includeFields=taxonName` (its backend taxonomy service refused connections), so the fetcher
  silently wrote a header-only GOA file. The GOA file here was fetched with the project's
  unmodified `fetch-gene` command, wrapped so that only the `taxonName` include field was
  dropped and the taxon name filled from the taxon id (7227). The rows are otherwise exactly as
  QuickGO serves them.
- Deep research: no Falcon/Perplexity keys in this environment; the FlyBase hand-written
  description (`Atg18a-deep-research-flybase.md`) is the only provider text.

## Literature searches run (PubMed E-utilities, 2026-11-16)

- `Atg18a AND Drosophila` (8 hits), `Atg18[tiab] AND Drosophila[tiab]` (13 hits),
  `Atg18b AND Drosophila` (0 hits), `CG7986` (0 hits).
- `pexophagy[tiab] AND Drosophila[tiab]` (5 hits; PMID:39904371 is the only fly pexophagy
  study and it tests Atg5, not Atg18a).
- `nucleophagy[tiab] AND Drosophila[tiab]` (1 hit, PMID:31937877, a phloroglucinol toxicity
  study of follicle cells, not about Atg18a or a nucleophagy mechanism).
- `(WIPI OR Atg18) AND Drosophila AND (PI3P OR phosphatidylinositol 3-phosphate)` (2 hits),
  `Atg18 AND Atg2 AND Drosophila` (3 hits), fly Atg18 elongation/isolation membrane (2 hits).

## What Atg18a is

- WD40 beta-propeller of the PROPPIN (Atg18/WIPI) family; the WIPI1/2-like fly gene named
  Atg18 because it is required for autophagy [PMID:24374083 "the WIPI1/2 homolog CG7986 is
  referred to as Atg18, as it is required for autophagy in Drosophila"]. The second fly
  WIPI1/2-like gene, CG8678 (Atg18b), and the WIPI3/4-like CG11975 had no known roles
  [PMID:24374083 "The roles of another WIPI1/2 family Drosophila protein, CG8678, and of the
  WIPI3/4-like CG11975 are unknown"].
- Sequence (bioinformatics folder, `Atg18a-bioinformatics/RESULTS.md`): fly Atg18a has LRRG
  (residues 222-225 of M9PER1) at the position of the WIPI2 FRRG phosphoinositide-binding motif;
  the arginine pair is conserved, as in human WDR45/WIPI4 (LRRG), which binds PI3P.
  Fly Atg18b has FRRG (208-211).

## Function in the fly (experimental)

- Required for starvation-induced Atg8a puncta and acts upstream of Atg8a, unlike Atg2
  [PMID:24374083 "in Drosophila, both Atg9 and Atg18 are required for Atg8a puncta formation,
  unlike Atg2"; "Loss of Atg18 suppressed Atg8a puncta formation unlike the lack of Atg2
  function, indicating that Atg18 acts upstream of Atg8a in Drosophila"]. Rescued by
  mCherry-Atg18.
- Required for Atg9 recruitment to the phagophore assembly site marked by Ref(2)P aggregates;
  FIP200 still arrives [PMID:24374083 "FIP200 was also enriched on Ref(2)P aggregates in cells
  lacking Atg2, Atg18 or Vps34 function (Fig. 3H–J), suggesting that Atg9 recruitment to PAS
  may specifically be affected by the absence of Atg18 or Vps34"].
- Binds Atg9 and Ref(2)P and bridges them in co-IP from cultured cells [PMID:24374083
  "HA-Atg9 showed strong binding to FLAG-Atg18, but not to FLAG-Ref(2)P"; "coexpression of
  HA-Atg18 resulted in coprecipitation of HA-Atg9 with FLAG-Ref(2)P"]. Atg2 co-IPs with Atg18a
  but more efficiently with the paralog CG8678/Atg18b [PMID:24374083 "Immunoprecipitation
  experiments suggested that Atg2 may interact with Drosophila Atg18, and more efficiently with
  its paralog CG8678"].
- Binds the mitophagy receptor BNIP3 through the BNIP3 MER motif (co-IP, attenuated by MER
  deletion) [PMID:40801807 "We confirmed that HA-tagged Drosophila Atg18a co-immunoprecipitated
  with GFP-tagged full-length Drosophila BNIP3, and that this interaction was attenuated by the
  deletion of the MER (residues 42–53)"].
- Localization: mCherry-Atg18 on Ref(2)P-positive stalled PAS in Atg2 and Atg8a RNAi cells
  [PMID:24374083 "overlapping mCherry-Atg18 and Ref(2)P structures were readily observed in Atg2
  and Atg8a RNAi cells"]; Atg18a-GFP puncta at synaptic boutons increase on starvation, sometimes
  colocalize with Atg8, and accumulate on nascent autophagosomes in synaptojanin SAC1 mutants;
  Atg18a-GFP rescues atg18a null lethality [PMID:28331029]. The puncta depend on both Vps34 (PI3P)
  and PIKfyve (PI(3,5)P2) activity [PMID:28331029 "indicating that Atg18a GFP likely binds both
  PI(3)P and PI(3,5)P 2 during autophagy at synapses"]. No direct in vitro lipid-binding assay
  on fly Atg18a was found.
- Processes, all by loss of function: starvation-induced autophagy in fat body
  (PMID:22952930, PMID:24374083), midgut autophagic cell death and histolysis (PMID:19818615,
  PMID:22555456, PMID:23873149, PMID:25882046), mitophagy in midgut, heart and remodelling
  muscle (PMID:23873149, PMID:30571977, PMID:40801807), glycogen autophagy in muscle
  (PMID:24265594), autophagy-dependent T-tubule remodelling (PMID:28063257), antiviral
  autophagy against VSV and RVFV (PMID:19362021, PMID:24374193), adult midgut enterocyte growth
  (PMID:29144896).

## IBA rows (PANTHER PTHR11227, all IBDs at the family root PTN000132136)

- The PAINT file `interpro/panther/PTHR11227/PTHR11227-paint.tsv` places every IBD at
  PTN000132136, the root of the whole PROPPIN family (yeast Atg18, Atg21, Hsv2; human
  WIPI1-4; worm ATG-18, EPG-6; fly Atg18a, Atg18b, CG11975). There are no IKR/losses.
- PI3P binding (seeds: yeast Atg18/Atg21/Hsv2, human WIPI1-4, mouse Wipi2, worm ATG-18/EPG-6):
  family-defining; fly pharmacology agrees. ACCEPT, core.
- PI(3,5)P2 binding: genuine family property (yeast Atg18 on the vacuole), fly YM201636 data
  consistent; secondary to PI3P for autophagy. KEEP_AS_NON_CORE.
- protein-macromolecule adaptor activity (seed WIPI1): fly Atg18a bridges Atg9 to Ref(2)P and
  binds BNIP3; ACCEPT.
- protein localization to PAS (seeds Wipi2, WIPI2, yeast Atg21): fly Atg18a needed for Atg9
  recruitment to the PAS and for Atg8a puncta; ACCEPT.
- PAS membrane GO:0034045: obsolete in current GO (replaced_by GO:7770114 phagophore membrane);
  fly localization data fit the phagophore; MODIFY to GO:7770114, as in the worm EPG-6 and human
  WIPI2 reviews.
- pexophagy (seed yeast Atg18 only): pexophagy exists in the fly and is Atg5-dependent
  (PMID:39904371) but Atg18a has not been tested; Atg18a is general autophagosome-forming
  machinery that every selective macroautophagy tested in the fly requires. KEEP_AS_NON_CORE.
- nucleophagy (seeds yeast Atg18, Atg21, Hsv2): no nucleophagy of any kind has been described in
  Drosophila, and the yeast seeds rest on yeast-specific routes (piecemeal microautophagy of the
  nucleus at nucleus-vacuole junctions, Atg39-dependent macronucleophagy). The root placement
  extends a yeast-defined process to every PROPPIN. MARK_AS_OVER_ANNOTATED.

## FlyBase description

"Autophagy-related 18a (Atg18a) encodes a protein that regulates autophagy by participating in
isolation membrane elongation around cytoplasmic cargoes."

- Role in autophagy: verified. "Isolation membrane elongation": not traced to any fly paper. The
  fly data place Atg18a upstream, at Atg9 recruitment and Atg8a puncta formation (PMID:24374083),
  and Atg2, the yeast Atg18 partner in phagophore expansion, is not needed for Atg8a puncta in
  the fly. The elongation framing comes from yeast/mammalian Atg2-Atg18 work. Not shown wrong,
  so correctness UNVERIFIED, not DISPUTED.
- UniProt: unreviewed record without a FUNCTION comment, so no UniProt text to check.
