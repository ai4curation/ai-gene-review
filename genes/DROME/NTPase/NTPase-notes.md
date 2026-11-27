# NTPase (Drosophila melanogaster, O76268) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used for this review.

### Identity of the benchmark accession
- O76268 is NTPase-PA (FBpp0077367, 461 aa). The gene has five transcripts and four distinct
  polypeptides: PE (Q9VQI8, 464 aa), PF (M9PBV2, 524 aa, the GCRP canonical), and PC/PD (Q8IPZ6,
  271 aa). All four are unreviewed TrEMBL entries, and none is Swiss-Prot reviewed.
- Comparison (`NTPase-bioinformatics/compare_isoforms_rereview.py`, `RESULTS-rereview.md`):
  PA is full-length, with the TM helix at 38-57, ACR1 DAGSTGS, and the predicted proton acceptor
  E202. PE differs only in its first residues. PF additionally carries an insertion of about 63
  residues after the TM helix. PC/PD equals PA 191-461 and lacks the TM helix and ACR1.
- The residues named in the cloning paper (C42 in the TM domain, C447 in the exoplasmic domain)
  match PA numbering, so O76268 is the experimentally characterised product
  [PMID:19467631 "dimer formation required C42 in the transmembrane domain and C447 in the exoplasmic domain"].
- Conclusion: O76268 is not a fragment. It is a full-length alternative isoform, and it is the
  characterised one. The gene-level review in this folder is complete. No same-gene canonical entry
  needs a separate review: PF/M9PBV2 is the GCRP representative, but it is unreviewed, it carries the
  same GO set, and its function is not separately characterised.

### Evolutionary placement
- PANTHER PTHR11782:SF127 ("NTPASE, ISOFORM F") contains fly NTPase and C. elegans uda-1 (Q9XU84,
  Swiss-Prot reviewed). Human ENTPD5 (SF35) and ENTPD6 (SF99) are in different subfamilies.
  Global identity is about 42% to each of the three, so pairwise identity does not resolve them. The
  "NTPDase6" name in the literature is a family-level analogy, not one-to-one orthology.
- uda-1 is a UDP/GDPase with a luminal active site, induced by ER stress through ire-1
  [PMID:15102851 "UDA-1, is a UDP/GDPase encoded by the gene uda-1"]. This matches the fly
  substrate profile and topology, so the luminal NDPase function is conserved within SF127.
- PANTHER family review `interpro/panther/PTHR11782/PTHR11782-review.yaml` lists O76268 as the SF127
  representative. It agrees with the placement used here.
- There are no IBA rows for this gene in GOA, so there is no PAINT node to argue with.

### Changes from the previous review
- cytoplasm (IDA): KEEP_AS_NON_CORE changed to MODIFY with endoplasmic reticulum as the
  replacement, because the paper reports the ER directly.
- plasma membrane (ARBA): UNDECIDED changed to REMOVE. Activity is latent in intact cells, the
  protein is in the ER, and the enzyme resists inhibitors of the surface NTPDases.
- extracellular region (ARBA): UNDECIDED changed to MARK_AS_OVER_ANNOTATED. No isoform has a
  secretion signal, and secreted relatives are in other subfamilies.
- Golgi (ARBA): kept UNDECIDED. UDA-1 fractionates with intermediate ER/Golgi vesicles, but no fly
  data address a Golgi pool.
- MF rows unchanged in substance. No NEW biological-process term was added: glycoprotein processing
  is a hypothesis from the paper and from the uda-1 analogy, and no fly loss-of-function test exists.
- Core function now also gives the location as ER. The description was rewritten.
- No modules under modules/ include NTPase. The dmel glycosylation modules do not list it.
