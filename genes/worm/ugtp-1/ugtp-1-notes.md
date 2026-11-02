# ugtp-1 (Q02334, ZK370.7) review notes

## Sources checked (2026-10-28)
- UniProt Q02334: 355 aa, six predicted TM helices, "Belongs to the nucleotide-sugar transporter
  family. SLC35A subfamily" (ECO:0000305); no FUNCTION comment. Name "UDP-galactose translocator 1"
  is by similarity only. Subcellular location: cytoplasmic granule membrane, localizes to cortical
  granules in meiotic prometaphase I/metaphase I [PMID:17913784, via UniProt ECO:0000269].
- PubMed search ("ugtp-1", "ZK370.7", "UDP-galactose transporter" + elegans) found no paper that
  assays UGTP-1 transport activity. The protein is used only as a GFP marker.
- PMID:23840591 (Ackema et al. 2013, GBF-1; full text): strain WHO351 ojIs37[GFP::ugtp-1];
  "GBF-1 partially co-localized with the medial Golgi marker UGTP-1::GFP." This is the basis of
  the IDA to Golgi medial cisterna. The paper uses UGTP-1 as an established medial-Golgi marker
  (its ref 18), it does not itself test where UGTP-1 is in the Golgi stack.
- PMID:17913784 (Bembenek et al. 2007; abstract only in cache): cortical granules identified in
  C. elegans oocytes; UGTP-1 GFP marks them (per UniProt curation of this paper).
- Alliance orthology (WB:WBGene00022721): best-score orthologs are SLC35A1 (human, mouse, rat,
  frog, zebrafish), i.e. the CMP-sialic acid transporter.
- PMID:34015330 (Ury et al. 2021): human SLC35A1 also transports CDP-ribitol into the Golgi
  ["We discovered that CDP-ribitol transport relies on the CMP-sialic acid transporter SLC35A1"].
  So the SLC35A1 clade is not restricted to CMP-sialic acid.
- Bioinformatics (ugtp-1-bioinformatics/RESULTS.md): no UniProtKB C. elegans entry has NANS,
  CMAS or sialyltransferase EC numbers; human and fly controls do. The worm therefore apparently
  lacks CMP-sialic acid, so the IBA CMP-sialic acid transport annotations (PTN008496232, seeded by
  mouse Slc35a1 and human SLC35A1 only, placed at Bilateria) do not describe a function UGTP-1 can
  perform in vivo.
- PAINT: PTN000027695 (family root) gives Golgi membrane / transmembrane transport; sound.

## Interpretation
UGTP-1 is a Golgi (medial cisterna) multi-pass membrane nucleotide-sugar antiporter of the SLC35A
subfamily, SLC35A1-like, whose physiological substrate in the worm is unknown. Candidate substrates
are UDP-sugars (name, by similarity) or CDP-linked compounds (as for SLC35A1, which handles CMP- and
CDP- nucleotide sugars). The general "pyrimidine nucleotide-sugar transmembrane transporter
activity" is as precise as the evidence allows.

## Decisions
- Golgi membrane (IBA, IEA): ACCEPT.
- Golgi medial cisterna (IDA): ACCEPT.
- cortical granule (IDA): KEEP_AS_NON_CORE (oocyte-stage location, Golgi-derived secretory granule).
- membrane / endomembrane system (IEA): MODIFY -> Golgi membrane.
- pyrimidine nucleotide-sugar transmembrane transporter activity / transport (IEA): ACCEPT (core).
- CMP-Neu5Ac transporter activity (IBA): MARK_AS_OVER_ANNOTATED (capacity untested, substrate absent).
- CMP-Neu5Ac transmembrane transport (IBA): REMOVE (process cannot occur without CMP-sialic acid).
- No NEW terms proposed.
