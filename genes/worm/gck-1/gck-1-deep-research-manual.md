# gck-1 (C. elegans, UniProt H2L099) - manual literature research

No deep-research API was available; this summary was compiled by hand from the cached
publications in `publications/` and a PubMed search ("gck-1 elegans", 6 hits, Oct 2026).

## Identity and domain architecture
- Germinal center kinase 1, ORF T19A5.2, 653 aa, four splice isoforms (a-d). STE20 family,
  GCK-III subfamily (orthologous to human STK24/MST3, STK26/MST4, STK25/YSK1).
- N-terminal protein kinase domain (aa 34-285; PROSITE PS50011, Pfam PF00069), active-site
  proton acceptor at residue 154; C-terminal PDCD10_N region (Pfam PF20929), the GCK-III
  dimerisation interface used by CCM3/PDCD10.
- UniProt: "Belongs to the protein kinase superfamily. STE Ser/Thr protein kinase family. STE20 subfamily."
  Catalytic activity is annotated by similarity to human STK26/MST4 (Q9P289); no in vitro kinase
  assay of worm GCK-1 is in the cached literature.

## Germline: oogenesis, MPK-1 and apoptosis
- First RNAi hint: T19A5.2 RNAi in a screen of MEN/SIN homologues caused germline degeneration
  [PMID:12213836 "In the case of the ORF T19A5.2, a potential homologue of the fission yeast kinase Sid1p, a striking degeneration of the germline in both RNAi-injected and -fed worms was observed."]
- Schouest et al. 2009 [PMID:19826475] (full text): gck-1(km15) deletion and RNAi give sterility,
  disorganized oogenesis, loss of rachis and increased germ cell apoptosis, independent of the DNA
  damage checkpoint. Loss of GCK-1 increases activated MPK-1 (isoform a) in pachytene; gck-1
  phenotypes depend on MAPK pathway components. GCK-1 N-terminus binds MPK-1a in vitro via an ERK
  docking site ["These data indicate that GCK-1 and MPK-1 can directly interact through an ERK docking site in the GCK-1 N-terminus"].
  GCK-1 acts in the germline ["indicating that GCK-1 functions in the germline"].

## Excretory canal and STRIPAK
- Lant et al. 2015 [PMID:25743393] (abstract only): CCM-3 localizes to the apical membrane of the
  excretory canal and "in cooperation with GCK-1 and STRIPAK, promotes CDC-42 signalling, Golgi
  stability and endocytic recycling". UniProt (ECO:0000269 to this paper) records GCK-1 in cytoplasm
  and apical cell membrane (peripheral), interacting with CCM-3.
- Lu et al. 2022 [PMID:35298637] (abstract only): STRIPAK core components including GCK-1 inhibit
  katanin in mitosis and activate it in meiosis.

## Intercellular bridges and contractility
- Rehain-Bell et al. 2017 [PMID:28285996] (full text): GCK-1 co-purifies with anillin; with CCM-3
  it promotes germline intercellular bridge stability by limiting ANI-1 and NMY-2 on bridges.
- Pal et al. 2017 [PMID:28285997] (abstract only): CCM-3 in germline tube development (rachis).
- Schouest/Maddox lab 2020 [PMID:32491957] (full text): GCK-1::GFP localizes to the cytokinetic
  ring and cortical pulses of the zygote, depending on CCM-3 and ANI-1; GCK-1/CCM-3 limit RHO-1
  activity and contractility, partly via the RhoGAP RGA-3/4. GCK-1 is required for CCM-3 stability.

## Synthesis
GCK-1 is a CCM-3-bound GCK-III Ser/Thr kinase, a STRIPAK core subunit, that acts at the cell cortex
(apical membrane of excretory canal, intercellular bridges, cytokinetic ring) to dampen RhoA-driven
actomyosin contractility and to support tube extension; in the germline it restrains MPK-1 activation
during pachytene. Direct kinase substrates in C. elegans are not identified.
