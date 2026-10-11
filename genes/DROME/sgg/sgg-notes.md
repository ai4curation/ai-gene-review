# sgg (shaggy / zeste-white 3) notes — Drosophila melanogaster, UniProt P18431

## Provenance / process

- Files fetched beforehand (`just fetch-gene DROME sgg`); publications cached with
  `just fetch-gene-pmids DROME sgg` (46 PMIDs; 21 with full text, 25 abstract-only).
- Deep research (falcon) is known to fail for this batch (HTTP 402) and was not attempted.
  No `-deep-research-*.md` file exists; these notes are built from cached publications,
  the UniProt record and Reactome cached entries.
- Context: sgg is a representative of PANTHER PTHR24057:SF0 in
  `interpro/panther/PTHR24057/PTHR24057-review.yaml`; it is also an experimental seed of the
  PTN000624299 (kinase, nucleus, cytoplasm) and PTN001173193 (Wnt negative regulation,
  cytosol, proteasomal catabolism, microtubule regulation) PAINT nodes.

## Identity

- Fly ortholog of vertebrate GSK3A/GSK3B; CMGC Ser/Thr kinase, GSK-3 subfamily
  [file:DROME/sgg/sgg-uniprot.txt "Belongs to the protein kinase superfamily. CMGC Ser/Thr"].
- Cloned as a segment-polarity gene encoding a kinase homolog
  [PMID:2113617 "encodes proteins that have homology to serine-threonine protein kinases"],
  and identified as the GSK-3 homolog [PMID:1335365 "zw3 encodes the Drosophila homolog of mammalian glycogen synthase kinase-3"].
- Multiple isoforms (Zygotic/B,C major; SGG46 maternal; SGG39; G). Sgg46 is activated by
  caspase cleavage [PMID:16222340 "This cleavage converts it to an active kinase"].

## Core activity: primed Ser/Thr kinase

Direct/biochemical evidence of fly Sgg phosphorylating substrates:
- Armadillo: CKIalpha primes Ser56, then Zw3 phosphorylates Thr52/Ser48/Ser44
  [PMID:14966281 "Zw3-directed Arm phosphorylation requires CKIalpha-mediated priming phosphorylation"].
  Earlier genetic data: [PMID:7529201 "Zeste-white 3, a serine/threonine protein kinase, promotes Armadillo phosphorylation"].
- Ci (Cubitus interruptus): PKA-primed GSK3 sites
  [PMID:11955435 "these phosphoserines prime further phosphorylation at adjacent Glycogen Synthase Kinase 3 (GSK3) and Casein Kinase I (CK1) sites"];
  [PMID:11912487 "Ci is phosphorylated by GSK3 after a primed phosphorylation by protein kinase A (PKA)"].
- Mad linker [PMID:25377173 "Cyclin dependent kinase 8 and Shaggy phosphorylate three Mad linker serines"].
- Axin [PMID:29408853 "Axin is “fully” phosphorylated by GSK3 in the Wnt-off state"].
- Timeless (circadian) [PMID:11440719 "Lowered sgg activity decreased TIMELESS phosphorylation"].
- Sarah/RCAN at a primed GSK3 consensus (Ser215 primed by Ser219) [PMID:22421435].
- dMyc degradation [PMID:19364825 "sgg/gsk3beta in Drosophila wing imaginal discs results in the accumulation of dMyc protein"].
- Futsch (MAP1B homolog) at NMJ [PMID:15269269].

Common theme: Sgg acts on substrates primed by another kinase (CK1, PKA, Cdk8) and creates
phospho-degrons recognized by SCF(Slimb) (Arm, Ci) or otherwise changes substrate stability /
localization. This matches the vertebrate GSK3B mechanism.

## Wingless / destruction complex (core pathway role)

- Genetic epistasis places zw3 downstream of wg as a repressor
  [PMID:1335365 "wg signaling operates by inactivating the zw3 repression of en autoactivation"].
- Overexpression blocks Wg signalling [PMID:9630748 "elevated levels of zeste white 3 in the ectoderm and mesoderm result in phenotypes that resemble a loss of wingless"].
- In vivo BiFC of the destruction complex (Axin–Sgg) in wing discs; the complex is cytoplasmic
  [PMID:31189665 "Axin/APC/GSK3β destruction complex (DC), which, under unstimulated conditions, targets cytoplasmic β-catenin for degradation"].
- Axin scaffolds Sgg and Arm [PMID:19850033 "The scaffolding protein Axin plays a key role in this process through interactions with Drosophila Shaggy and Armadillo"].
- Caveat: Wg signal can also act through Arrow/Axin independently of Zw3 activity
  [PMID:12636921 "The intracellular pathway bypasses Gsk3beta/Zw3"] — sgg is a negative regulator but not the sole mode of Wg control.
- Reactome Drosophila Wnt pathway models SGG phosphorylating ARM and Arrow (R-DME-209109, R-DME-209118).

## Hedgehog pathway

- Sgg antagonizes Hh signalling by promoting Ci processing to the repressor form
  [PMID:11912487 "Here we show that Sgg is also a negative regulator in the Hedgehog (Hh) pathway"];
  kinases are recruited via Cos2 [PMID:15691767 "PKA, GSK3, and CKI directly bind the N- and C-terminal regions of Cos2"].

## Circadian clock

- Sgg phosphorylates TIM, controls PER/TIM nuclear entry and period length [PMID:11440719].
- Serotonin/5-HT1B effects on light entrainment are mediated by Sgg [PMID:15996552].
- Circadian role separable from habituation [PMID:17360579].

## Other roles (pleiotropic / context-specific)

- NMJ growth: Sgg negatively controls bouton number, presynaptically, via Futsch/microtubules
  [PMID:15269269 "Shaggy negatively controlled the NMJ growth"]; also [PMID:18832361], [PMID:25764078].
- Mitosis: zw3 mutants have bent metaphase spindles and metaphase delay; GFP-Zw3 on centrosomes
  and transiently in nucleus [PMID:19029800]; GFP protein-trap localization to centrosomes [PMID:16570248].
- Female meiosis completion via Sarah phosphorylation and calcineurin activation [PMID:22421435].
- BMP gradient restriction via Mad linker phosphorylation [PMID:25377173].
- Insulin/TOR inhibit Sgg to stabilize Myc [PMID:21951762]; ovarian insulin–Myc relay [PMID:31612862].
- Developmental phenotypes: segment polarity/naked cuticle, wing margin, bristle/SOP formation,
  ovarian somatic stem cells, follicle cell mitotic-endocycle switch (Notch), epidermal morphogenesis
  with aPKC, habituation, anesthetic sensitivity.

## Curation decisions summary

- Core: Ser/Thr kinase activity (primed substrates); destruction-complex member and negative
  regulator of canonical Wnt/Wg signalling (Arm phospho-degron); negative regulator of Hh signalling
  via Ci phosphorylation/processing; circadian TIM phosphorylation; presynaptic microtubule/NMJ growth control.
- Developmental phenotype BP terms -> KEEP_AS_NON_CORE.
- ComplexPortal NAS "proteasome-mediated ubiquitin-dependent protein catabolic process" -> MODIFY to
  positive regulation of proteasomal ubiquitin-dependent protein catabolic process (Sgg marks substrates;
  it does not perform proteolysis).
- "regulation of calcineurin-NFAT signaling cascade" -> MODIFY to positive regulation of
  calcineurin-mediated signaling (no NFAT in the meiotic egg-activation context).
- "synaptic assembly at neuromuscular junction" -> MODIFY to negative regulation of that process.
- Protein binding IPIs: Cos2 -> MODIFY to kinesin binding; Axin -> REMOVE (bare protein binding; biology captured by destruction complex); Cry (abstract-only, unverifiable) -> UNDECIDED.
- heart development (TAS, vertebrate-focused review, abstract only) -> UNDECIDED.

## Family-review implications (PTHR24057)

- sgg experimentally supports the metazoan-scoped Wnt terms (GO:0090090 by IMP/IGI/IDA from many
  papers; GO:0030877 by IDA, PMID:31189665) and family-wide Ser/Thr kinase activity (many IDA).
- No tau-protein kinase annotation exists for sgg; consistent with scoping tau to vertebrates
  (fly has tau but the GO term was not propagated; Futsch is the characterized neuronal MAP substrate).
- sgg also gives in vivo evidence of Hh (Ci) and circadian (TIM) roles that are not part of the
  PAINT-propagated set; these are fly/bilaterian-specific pathway uses of the same primed-kinase mechanism.
