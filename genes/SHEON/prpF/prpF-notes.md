# prpF (Q8EJW4, SO_0342) — Shewanella oneidensis MR-1

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: Q8EJW4 is reviewed here in its own right as the experimentally characterised
PTHR43709:SF2 member that seeds the only PAINT IBD in the family (PTN002017920,
GO:0016863). The ProtNLM2 predictions were not consulted.

### Setup / provenance
- `just fetch-gene SHEON Q8EJW4` created `genes/SHEON/Q8EJW4/`. I renamed the folder
  and files I had just created to `genes/SHEON/prpF/` to follow the gene-symbol
  convention used for the other prp genes (e.g. `genes/PSEPK/prpF`).
- Deep research FAILED: falcon gave an authentication error, and the perplexity-lite
  fallback returned HTTP 401 insufficient_quota. No deep-research file exists. The
  review is based on the three cached full-text papers below.
- FEBA fitness: `just fetch-fitness SHEON prpF` failed (no local FEBA DB, no SHEON
  organism mapping; the FEBA orgId for MR-1 would be MR1). No fitness evidence was used.
- PMID:29145506 (Rocco et al. 2017) is not cited in GOA. I fetched it into
  publications/ because it is the definitive functional paper.

### Evidence established in this species (S. oneidensis protein itself)
- In vivo, by heterologous complementation in an S. enterica prpD strain: SoAcnD and
  SoPrpF together, but neither alone, restore growth on propionate, aerobically and
  anaerobically [PMID:14702315 "together, the AcnD and PrpF proteins restored the ability of a prpD mutant strain of Salmonella enterica to grow on propionate"].
  This was not tested by deletion in MR-1 itself.
- Purified PrpF has no dehydratase or hydratase (aconitase-like) activity
  [PMID:14702315 "No aconitase-like activity was found for PrpF"]. The paper's Fe/S
  protection hypothesis was superseded.
- In vitro trans-aconitate -> cis-aconitate isomerase activity, at a low rate
  [PMID:17567742 "Under the assay conditions used, PrpF-dependent synthesis of cis -aconitate was calculated to occur at 4.8"].
  Structures: apo (2PVZ) and trans-aconitate complex (2PW0). The protein is a homodimer
  [PMID:17567742 "The PrpF assembles to form a homodimer"].
- Physiological reaction: PrpF isomerizes the AcnD product (putatively
  4-methyl-cis-aconitate) to 2-methyl-cis-aconitate, the aconitase substrate
  [PMID:29145506 "PrpF (SoPrpF) protein isomerizes the product of the SoAcnD dehydratase (putatively 4-methyl-cis-aconitate (4-MCA) to 2-methyl-cis-aconitate (2-MCA)"].
- K73 and C107 are required in vivo
  [PMID:29145506 "variants with substitutions of residues K73 or C107 failed to support growth"].
  K73E structures were solved at 1.22 A (5K87).

### What is inferred, not established
- The chemical identity of the AcnD product (4-methyl-cis-aconitate) is the authors'
  inference. UniProt's RHEA:37751 (2-methyl-trans-aconitate = 2-methyl-cis-aconitate)
  is tagged ECO:0000269 to PMID:17567742, but that paper assayed only unmethylated
  trans-aconitate. The exact substrate isomer is therefore open.
- No subcellular localization study exists. A cytoplasmic location is likely (soluble,
  no signal peptide) but not annotated here.

### Evolutionary grounding
- PANTHER PTHR43709 (ACONITATE ISOMERASE-RELATED), subfamily SF2 ("DUF453 DOMAIN
  PROTEIN"). SF2 is heterogeneous: it also holds Mii (Q0QLE6, 3-methylitaconate
  isomerase, Eubacterium barkeri), Adi1 (fungal aconitate delta-isomerase), B. subtilis
  YraM and Cupriavidus Q937N7. The family review
  (interpro/panther/PTHR43709/PTHR43709-review.yaml) flags this heterogeneity.
- PAINT: a single IBD of GO:0016863 at PTN002017920, seeded only by Q8EJW4. The curator
  deliberately placed only the EC 5.3.3-level parent and no substrate-specific term.
  This should be respected when transferring to other SF2 members: GO:0016863 is
  transferable within the clade, but the methylaconitate/2-MCC substrate role is
  PrpF-specific. That role is supported by the TIGR02334/IPR012709 PrpF signature
  and by the acnD-prpF operon context, not by SF2 membership.
- For the BORPE Q7VZI5 comparison: Q7VZI5 shares SF2, but it is equidistant to PrpF,
  Mii and Adi1, so only the GO:0016863-level activity should be considered
  transferable without further phylogenetic or genomic-context evidence (e.g. an
  adjacent acnD).

### Annotation decisions (7 GOA rows)
- GO:0016853 isomerase activity (IEA InterPro): MODIFY -> GO:0016863.
- GO:0016863 (IBA, IDA PMID:17567742, IEA ARBA): ACCEPT. This is the most precise
  existing term; no methylaconitate-isomerase term exists, so I proposed one.
  GO:0047614 aconitate delta-isomerase activity (a child of GO:0016863) fits only the
  model-substrate reaction. Curators did not use it, so it was not added as NEW.
- GO:0019543 propionate catabolic process (IDA x2, IEA): ACCEPT. PrpF catalyses a step
  of the pathway. The 2-methylcitrate cycle process terms GO:0019629 and GO:0019679
  are obsolete (checked in the local go.db via OAK).
