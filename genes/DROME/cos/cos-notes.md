# cos (Costal-2, O16844) curation notes

Deep research: the falcon wrapper reported a 600 s timeout (perplexity fallback unavailable), but the
falcon run completed later and wrote `cos-deep-research-falcon.md`, folded in as an EDIT.

## Literature journal

- Cos2 is a kinesin-related protein, cytoplasmic, binds microtubules, associates with Ci
  [PMID:9244298 "COS2 is cytoplasmic and binds microtubules."]
- HSC: Fu, Ci, Cos2 complex binds microtubules in an Hh-reversible way
  [PMID:9244297 "The complex binds with great affinity to microtubules in the absence of HH, but binding is reversed by HH."]
- Direct trimeric Cos2-Fu-Ci complex
  [PMID:10825151 "three members of this complex, Costal2 (Cos2), Fused (Fu), and Cubitus interruptus (Ci), bind each other directly to form a trimeric complex"]
- Cytoplasmic tethering of Ci, and positive role at high Hh
  [PMID:11090136 "We show that Cos2 binds Ci, prevents its nuclear import, and inhibits its activity via this domain."]
  [PMID:11090136 "Cos2 is required for transducing high levels of Hh signaling activity"]
- Scaffold for PKA, GSK3, CK1
  [PMID:15691767 "PKA, GSK3, and CKI directly bind the N- and C-terminal regions of Cos2, both of which are essential for Ci processing."]
- Smo C-tail binds Cos2/Fu
  [PMID:14597665 "Smo physically interacts with Costal2 (Cos2) and Fused (Fu) through its C-tail."]
- Fu phosphorylates Cos2 at S572 (feedback on Smo)
  [PMID:17671093 "Fu antagonizes Cos2 by phosphorylating Cos2 at Ser572"]
- Motor domain: atypical kinesin; motility reported (Farzan et al., cited) and nucleotide-state mutants
  [PMID:20850429 "Cos2 has been shown to move along microtubules and this activity is perturbed by alterations, including S182N, expected to block nucleotide binding or hydrolysis"]
- Ciliary transport of Smo in olfactory neurons
  [PMID:24768000 "We show that Cos2 and Fused are required for the ciliary transport of Smoothened"]
- Ubr3 ubiquitinates Cos2
  [PMID:27195754 "Here we show that Ubr3 promotes Hh signaling by mediating the ubiquitination and degradation of Cos2/Kif7."]

## Curation decisions

- Core MF: signaling adaptor activity (scaffold for kinases + Ci), molecular sequestering (Ci tethering),
  smoothened binding; complex = Hedgehog signaling complex (same as fu/ci reviews).
- Motor activity: the deep-research report summarizes single-molecule data (Yue et al. 2018) showing
  purified Cos2(1-743) is immotile on microtubules (static binding/diffusion, 0 nm/s)
  [file:DROME/cos/cos-deep-research-falcon.md "Purified **DmCos2(1–743)** showed static binding or diffusion on microtubules"],
  in contrast to an earlier motility report cited in PMID:20850429. Motor activity, MT-based movement and
  intracellular transport rows were therefore marked over-annotated (initially kept non-core); ATP
  hydrolysis UNDECIDED (not measured for Cos2).
- Generic locations (cytoplasm, cytoskeleton, MT cytoskeleton) MODIFY -> cytosol / microtubule;
  microtubule associated complex MODIFY -> Hedgehog signaling complex (round-2 convention).
- protein binding rows: MODIFY to smoothened binding, protein kinase binding (Fu, Sgg, CK1) or
  Pol II TF binding (Ci); Sxl co-complex rows REMOVE.
- negative regulation of transcription by Pol II (NAS) over-annotated: Cos2 acts in the cytoplasm upstream of Ci-75.
