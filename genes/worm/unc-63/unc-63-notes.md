# unc-63 notes

## 2026-11-21

- Fetched `worm/unc-63` with UniProt Q9N587, cached all eight GOA
  PMIDs, cached the WormBase hand-written MOD description, and checked PAINT:
  `just paint-losses worm unc-63` reported no IRD or IKR loss on the
  UNC-63 lineage.
- Deep research was attempted with `just deep-research-falcon worm unc-63
  --fallback perplexity-lite`, but both providers were unavailable in this
  environment. The review instead used cached primary papers, the WormBase
  MOD description, UniProt, the PTHR18945 family review, and the existing
  `unc-29`, `lev-1`, and `unc-38` L-AChR reviews.
- UNC-63 is one of the three alpha subunits in the
  levamisole-sensitive acetylcholine receptor. Native UNC-29 purifications
  recovered peptides from UNC-29, UNC-38, UNC-63, LEV-8, and LEV-1 in all
  four purifications [PMID:15990870, "Multiple peptides of each of the
  levamisole receptor subunits"], and functional Xenopus oocyte
  reconstitution needed all five pore subunits plus RIC-3, UNC-50, and
  UNC-74 [PMID:19020092, "functional receptors were virtually eliminated
  when 1 or more of the 5 receptor subunits were omitted"].
- UNC-63 also acts with UNC-38 and ACR-12 in the neuronal ACR-2 receptor.
  Loss-of-function mutations in `unc-63` suppress `acr-2(n2420gf)`
  convulsions, cholinergic-motor-neuron expression of `unc-63` restores the
  phenotype, and adding `acr-3` to ACR-2/ACR-12/UNC-38/UNC-63 plus the same
  three ancillary factors yields an acetylcholine-gated oocyte current
  [PMID:20027209, "robust expression of an acetylcholine-gated ion channel
  was observed"].
- The strongest target-specific localization comes from the 2011 UNC-63
  Cys-loop paper: non-permeabilized cultured muscle cells stained
  preferentially at the periphery, adult worms stained for UNC-63 in
  body-wall muscle and ventral-nerve-cord puncta, and no staining was seen in
  the `unc-63(x37)` null [PMID:20966081, "UNC-63 is localized in the plasma
  membrane"]. The 2007 caveolin paper is abstract-only locally but directly
  describes UNC-63 as a postsynaptic marker that colocalizes with CAV-1.
- `PMID:7498734`, `PMID:11290716`, `PMID:17629760`, `PMID:1945043`, and
  `PMID:23351035` stayed abstract-only after forced refresh. I deferred to
  WormBase for rows where the gene and phenotype match later UNC-63 biology,
  but left the nicotine-motivated locomotory-behavior row from
  PMID:23351035 undecided because the accessible abstract names ACR-5 and
  ACR-15, not UNC-63.
- The calcium-specific IDA row from PMID:20027209 has the same caveat as on
  the UNC-38 review. Calcium import is a real secondary property of
  UNC-63-containing nicotinic cation channels based on direct L-AChR calcium
  permeability in PMID:19020092, but PMID:20027209 itself measured an ACR-2R
  acetylcholine-gated cation channel and only inferred increased calcium
  influx as a possible consequence of ACR-2 hyperactivity. I kept the row
  while recording a WormBase `WRONG_TERM` query about that source paper.
- WormBase's MOD gene description has the core receptor-subunit role right,
  but its coexpression sentence is stale because it implies UNC-63 with
  UNC-29 and LEV-1 is enough to form levamisole-gated channels. The mature
  C. elegans L-AChR requires UNC-29, LEV-1, UNC-38, UNC-63, and LEV-8.
