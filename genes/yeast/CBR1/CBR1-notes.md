# CBR1 review notes

## 2026-10-10

### Setup and literature search

- Seeded `genes/yeast/CBR1/CBR1-ai-review.yaml` with `just fetch-gene yeast CBR1`
  and then cached all GOA PMIDs with `just fetch-gene-pmids yeast CBR1`.
- Tried to run automated deep research with
  `just deep-research-falcon yeast CBR1 --fallback perplexity-lite`; the local
  `agentapi` executable and provider API keys were unavailable, so this review
  is based on manual PubMed/web search, cached publications, UniProt, and the
  local PAINT cache.
- Manual web/PubMed search for newer `Saccharomyces` Cbr1/Dph3/diphthamide
  papers found the expected Cbr1/Dph3 discovery paper from 2016, follow-up
  Dph1-Dph2 mechanism papers from 2019 and 2021, and no newer primary paper
  that changes the core assignment.

### Core activity synthesis

- Cbr1 is the CBR1-like, membrane-anchored NADH-cytochrome b5 reductase in
  PANTHER family `PTHR19370`, subfamily `PTHR19370:SF184`. The old
  microsomal purification paper directly characterized NADH-specific
  ferricytochrome-b5 reduction in yeast: "The presence of NADH-cytochrome b5
  reductase [EC 1.6.2.2] in microsomes from anaerobically grown yeast was
  confirmed by its isolation and purification" and "The reductase required NADH
  as a specific electron donor, and could reduce some redox dyes as well as
  cytochrom b5." [PMID:14930]
- Lin et al. identified Cbr1 as the major yeast Dph3 reductase by a Dph3 SILAC
  interactome, in vitro Dph3 reduction, reconstitution of Dph1-Dph2 activity
  with Cbr1/Dph3/NADH, and reductase deletion phenotypes. Useful exact snippets:
  "Here, using a proteomic approach, we identified Saccharomyces cerevisiae
  cytochrome b5 reductase (Cbr1) as a NADH-dependent reductase for Dph3";
  "Upon addition of NADH to initiate the reaction, Dph3 was rapidly reduced by
  Cbr1"; "formation of tRNA modifications was partially impaired"; and "In
  summary, we identified Cbr1 as the major physiological reductase of Dph3".
  [PMID:27694803]
- Dong et al. 2014 established the Dph1-Dph2/Dph3 radical-SAM system but did
  not identify Cbr1; the Cbr1 assignment comes from the later Lin et al.
  reductase paper. The paper's own summary is that "yeast Dph3 (also known as
  KTI11), a CSL-type zinc finger protein, can bind iron and in the reduced state
  can serve as an electron donor to reduce the Fe-S cluster in Dph1-Dph2".
  [PMID:24422557]
- Zhang et al. 2019 refined the Dph1-Dph2 heterodimer mechanism using Cbr1,
  Dph3, and NADH as the natural reducing system. The key distinction for GO is
  that Dph1-Dph2 performs ACP transfer, while Cbr1 reduces Dph3 upstream:
  "Dph1-Dph2 heterodimer is a non-canonical radical SAM enzyme that transfers
  the ACP group from SAM to EF2" and "the Dph1 Fe-S cluster serves a catalytic
  role while the Dph2 Fe-S cluster facilitates the reduction of Dph1 cluster by
  the Dph3/Cbr1/NADH system." [PMID:31463593]
- Zhang et al. 2021 showed that Dph3 can donate the fourth iron to oxygen-
  damaged Dph1-Dph2, with the Cbr1/Dph3/NADH system both supplying electrons
  and enabling Fe-S cluster repair during aerobic diphthamide biosynthesis. The
  abstract states that "the small iron-containing protein Dph3 donates one Fe
  atom to convert the [3Fe-4S] cluster in Dph1-Dph2 to a functional [4Fe-4S]
  cluster during the radical-SAM enzyme catalytic cycle." [PMID:34154323]

### PAINT and IBA notes

- `PANTHER:PTN001064671` is the Saccharomycetales CBR1-like node. It carries
  `GO:0004128` from `SGD:S000001305` and `GO:0005886` from
  `CGD:CAL0000182794`. Yeast CBR1 is inside this node, and the SGD CBR1 self
  seed for cytochrome-b5 reductase activity is expected because PAINT used the
  experimental yeast annotation to place the ancestral IBD.
- `PANTHER:PTN001064672` records a fungal-branch negative for the broad
  eukaryotic mitochondrial IBD and a positive plasma-membrane IBD seeded by SGD
  `MCR1`. Treat that as a PAINT-localization split, not as evidence that
  Cbr1 has lost mitochondrial-outer-membrane localization in yeast: yeast Cbr1
  has direct mitochondrial outer-membrane proteomics evidence and literature
  describes Cbr1 on the ER and mitochondrial outer membrane with a cytosolic
  catalytic domain [PMID:16407407; PMID:27694803].
- `PANTHER:PTN001833551` puts the very broad `GO:0016491 oxidoreductase
  activity` at the family root. For Cbr1 this is true but far less informative
  than the exact NADH:ferricytochrome-b5 and NADH:Dph3 reductase activities.

### Annotation calls to watch

- The GO:0090560 rows should not be accepted literally as Cbr1 itself enabling
  2-(3-amino-3-carboxypropyl)histidine synthase activity. That reaction is
  catalyzed by Dph1-Dph2; Cbr1 reduces Dph3 upstream and should be captured as
  NADH-dependent Dph3 reductase activity, plus a `contributes_to` relationship
  to the Dph1-Dph2 complex function if the model treats Cbr1 as a component of
  the reducing system.
- `GO:0003954 NADH dehydrogenase activity` and `GO:0016491 oxidoreductase
  activity` are broad ancestors. Prefer the Rhea-backed
  `GO:0090524 cytochrome-b5 reductase activity, acting on NADH` and a proposed
  NADH-dependent Dph3 reductase term for the two known electron acceptors.
- Mitochondrion and mitochondrial outer-membrane rows are high-throughput or
  subcellular-location mappings but match the expected Cbr1 membrane topology.
  The nucleus row comes from an N-terminal GFP SWAp-Tag library whose tag sits
  directly upstream of Cbr1's only transmembrane helix at residues 7-27, so it
  is best treated as over-annotated.
