# BID manual curation notes

## 2026-09-30

- BID is the BH3-only relay between initiator caspases and the mitochondrial
  BAX/BAK pore. The original death-receptor papers support cleavage of
  full-length cytosolic BID and movement of the C-terminal tBID fragment to
  mitochondria, where it stimulates cytochrome-c release
  [PMID:9727491, "Caspase-8 cleaves Bid, and the COOH-terminal part translocates
  to mitochondria where it triggers cytochrome c release"];
  [PMID:9727492, "truncated BID (tBID) translocates to mitochondria and thus
  transduces apoptotic signals from cytoplasmic membrane to mitochondria"].
- The direct BAX/BAK evidence supports BID as an activator BH3-only protein, not
  as the MOMP pore itself. Walensky et al. detected direct BID BH3-BAX binding
  and BAX activation [PMID:17052454, "model in which BID directly engages BAX to
  trigger mitochondrial apoptosis"], and Moldoveanu et al. solved the human BID
  BH3-BAK complex and described a hit-and-run mechanism
  [PMID:23604079, "BID dissociates from the trigger site, which allows BAK
  oligomerization at an overlapping interface"].
- BID's `GO:0001836 release of cytochrome c from mitochondria` rows should be
  moved to positive regulation of cytochrome-c release. BAX and BAK execute the
  pore-forming release step; BID contributes the upstream BH3 trigger that
  activates those effectors.
- `GO:0005123 death receptor binding` is not supported for BID. The 1996 paper
  used "death ligand" figuratively for BAX and BCL2-family binding
  [PMID:8918887, "represents a death ligand for the membrane-bound receptor BAX"],
  not literal binding to FAS/TNFR/TRAIL death receptors.
- Generic IntAct-imported `GO:0005515 protein binding` rows cover a mix of
  useful BCL2-family biochemistry, viral BCL2 inhibition, contextual scaffolds
  such as CAV1 and PLEKHN1, and large-scale interactome edges. BID generally
  supplies a BH3 helix to a BCL2-family groove rather than binding another BH3
  domain, so the BAX/BAK/MCL1 replacement term `GO:0051434 BH3 domain binding`
  would be the wrong direction for BID.
- CASP6 cleavage of purified BID at Asp59 and Asp75 in the NASH study supports a
  hepatocyte feed-forward context in which BID promotes cytochrome-c release
  [PMID:32029622, "active caspase-6 cleaved purified Bcl2 family protein Bid"].
  This is direct but contextual, so `GO:0097284 hepatocyte apoptotic process`
  should remain non-core.
- Humanin sequesters BID into fibers and prevents its activation rather than
  representing canonical BID pro-apoptotic activity [PMID:33106313, "inhibition
  and sequestering of BID into amyloid-like fibers along with HN"]. Keep the
  supramolecular-fiber row as a non-core inhibitory context.
