# TLL1 (human, O43897) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: TLL1 was reviewed as the experimentally characterised relative of a short
bullfrog CUB-domain fragment (AQUCT A0A2G9RZF1). This review treats human TLL1 in its
own right. No ProtNLM2 files or prediction-evidence folders were consulted.

### Deep research

`just deep-research-falcon human TLL1 --fallback perplexity-lite` failed: falcon failed and
the perplexity-lite fallback timed out after 600 s. No deep-research file exists. The review
is based on the UniProt record, the Reactome entries cited by GOA, and primary papers
cached in `publications/` (found by a PubMed title/abstract search for TLL1 / Tll1 /
"tolloid-like 1" / "mammalian tolloid-like").

### Evolutionary placement

- UniProt: `DR   PANTHER; PTHR24251:SF45; METALLOENDOPEPTIDASE; 1.`
- In `interpro/panther/PTHR24251/PTHR24251-entries.csv`, SF45 holds the reviewed TLL1
  orthologs (human O43897, mouse Q62381, chicken Q9DER7, Xenopus Q8JI28) **and** the
  TLL2 paralogs (human Q9Y6L7, mouse Q9WVM6, Xenopus O57382). BMP1 (mouse P98063) sits in
  a different subfamily, SF53.
- Consequence for transfer: SF45 is a TLL1+TLL2 subfamily, not a TLL1-only orthogroup.
  Functions shared by TLL1 and TLL2 (metalloendopeptidase activity, pro-lysyl oxidase,
  procollagen VII, myostatin propeptide cleavage) are subfamily-wide. Procollagen
  I-III C-proteinase activity and chordin cleavage are NOT subfamily-wide: Scott et al.
  1999 showed TLL2 lacks pCP activity and does not cleave chordin
  [PMID:10479448 "mTLL-1 is shown to specifically process procollagen C-propeptides at the physiologically relevant site, while mTLL-2 is shown to lack this activity"].
  (Note that a later in vitro study reports TLL2 can cleave chordin
  [PMID:26902455 "we show that TLL-2 can cleave chordin in vitro"], so the chordin
  difference is assay-dependent.) Transfer of the pCP activity therefore needs TLL1
  orthology (TLL1 clade inside SF45), not just SF45 membership.
- PAINT: the IBA rows come from PTN000013301 (eukaryote-level node; metalloendopeptidase
  activity, extracellular region) and PTN001298759 (Bilateria-level node; dorsal/ventral
  pattern formation, protein processing; seeds Drosophila tolloid/tolkin and zebrafish
  tolloid genes). The PAINT curators did not propagate a collagen-related process to these
  nodes.

### Experimental evidence on the human protein

- Human TLL-1 enzyme cleaves human procollagen I and II C-propeptides (Scott et al. 1999,
  as stated in Reactome R-HSA-2002440: "TLL-1 (human types I, II, human enzyme, Scott et
  al. 1999)"); Scott et al. also showed TLL-1 cleaves chordin and counteracts Chordin
  dorsalisation in Xenopus embryos [PMID:10479448 "BMP-1 and mTLL-1 are shown to cleave Chordin, at sites similar to procollagen C-propeptide cleavage sites, and to counteract dorsalizing effects of Chordin upon overexpression in Xenopus embryos"].
- Recombinant human TLL1 (cloned from NTERA-2 cells) cleaves chordin and procollagen I;
  ASD6 missense variants reduce activity [PMID:30538173].
- Human TLL1 cleaves human SLIT2 in S2 cells, requiring furin-type activation
  [PMID:41626796 "The Tolloid-related protease TLL1 cleaved SLIT2 in cultured cells, with TLL1 requiring activation by furin/prohormone convertases."].
- Human TLL-1 protease domain crystal structure [PMID:18824173].
- Heterozygous TLL1 variants: ASD6 (loss of function, PMID:18830233, PMID:30538173);
  p.T253A gain of function causing mitral valve prolapse (PMID:39880331).

### Evidence from mouse / unspecified mammalian enzymes (ortholog-level, same TLL1 clade)

- Tll1-/- mice: mid-gestation lethal, incomplete interventricular septum, abnormal heart
  position [PMID:10331975]. Phenotype is necessity, not a participation claim.
- Bmp1/Tll1 double-null cells: TLL1 is an in vivo pCP and with BMP1 accounts for chordin
  cleavage [PMID:12808086].
- Pro-lysyl oxidase processing [PMID:11313359]; probiglycan (low activity) [PMID:10896944];
  procollagen VII [PMID:11986329]; latent myostatin activation [PMID:14671324];
  PCOLCE1 binding and Ca2+-independence for some substrates [PMID:16507574];
  Ca2+-dependent dimerisation that limits activity [PMID:20043912].
- Induced postnatal Bmp1+Tll1 ablation produces osteogenesis imperfecta-like bones
  [PMID:24419319]; this is the main basis for a skeletal role, and it is a combined-gene
  necessity result.

### Decisions

- Serine-type endopeptidase activity (ARBA IEA, Reactome TAS): REMOVE. TLL1 is an
  astacin-family (M12A) zinc metalloprotease with an HEXXH zinc-binding active site; no
  serine-protease domain.
- Metalloendopeptidase, zinc binding, extracellular region, protein processing, collagen
  fibril organization: ACCEPT.
- Proteolysis and metallopeptidase activity: TOO_GENERAL (entailed by protein processing
  and metalloendopeptidase activity).
- Calcium ion binding (cbEGF domains): KEEP_AS_NON_CORE.
- Dorsal/ventral pattern formation (IBA): KEEP_AS_NON_CORE; chordinase activity supports
  it mechanistically, but there is no mammalian D/V patterning evidence and BMP1 is the
  major mammalian chordinase.
- Skeletal system development (TAS, PMID:8661043): KEEP_AS_NON_CORE; the cited paper is a
  cloning/expression study, the real support is the Bmp1/Tll1 double ablation.
- No NEW annotations. Heart septum morphogenesis was considered and not added: the
  evidence is knockout necessity, and which TLL1 substrate is responsible is unknown.
