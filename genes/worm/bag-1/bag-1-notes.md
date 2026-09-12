# bag-1 (C. elegans) research notes

UniProt: **O44739** (BAG1_CAEEL), "BAG family molecular chaperone regulator 1".
Gene: `bag-1`; ORF `F57B10.11`; WormBase `WBGene00000236`; Chromosome I. 210 aa, 24 kDa.
NCBITaxon:6239.

## Identity check
Confirmed the record is the BAG-domain Hsp70/Hsc70 co-chaperone (nucleotide-exchange
factor), not a mis-named gene. UniProt DE = "BAG family molecular chaperone regulator 1";
domains: a **ubiquitin-like domain (8–85)** and a **BAG domain (108–194)**; PDB **1T7S**
(BAG domain, residues 74–210). Family founder for the C. elegans BAG proteins together
with UNC-23 (BAG2 ortholog).

## Domain architecture / structure
- Ubiquitin-like (UBL) domain FT 8–85 (PROSITE PRU00214); BAG domain FT 108–194
  (PROSITE PRU00369). Pfam PF02179 (BAG) + PF00240 (ubiquitin). InterPro IPR017093
  (BAG-1), IPR003103/IPR036533 (BAG domain + superfamily), IPR000626 (ubiquitin-like).
- Crystal structure of the worm BAG domain solved by structural genomics
  [PMID:15333932 "Binding of the BAG domain to the eukaryotic chaperone heat-shock protein (Hsp70) promotes ATP-dependent release of the protein substrate from Hsp70"].
  Notably the worm BAG domain adopts an unusual fold: "the Caenorhabditis elegans BAG
  domain is formed by two antiparallel helices, while the third helix is extended away"
  [PMID:15333932 "the Caenorhabditis elegans BAG domain is formed by two antiparallel helices, while the third helix is extended away and stabilized by crystal-packing interactions"].
  The paper infers oligomerization: "stable functional dimers and tetramers can be formed
  in solution" [PMID:15333932 "intermolecular three-helix bundles are observed throughout the crystal packing and suggest that stable functional dimers and tetramers can be formed in solution"].
  UniProt SUBUNIT: "Homodimer or homotetramer" (ECO:0000269|PubMed:15333932).

## KNOWN (well-supported) function
1. **BAG-domain co-chaperone / Hsp70(Hsc70) nucleotide-exchange factor (NEF).** The
   defining activity of the BAG family. Founding paper describing the family (incl. worm
   BAG-1/BAG-2) [PMID:9873016 "BAG-1 binds the ATPase domains of Hsp70 and Hsc70, modulating their chaperone activity and functioning as a competitive antagonist of the co-chaperone Hip"].
   The BAG domain binds the Hsp70 ATPase (nucleotide-binding) domain and drives
   ATP-dependent substrate release [PMID:15333932 "Binding of the BAG domain to the eukaryotic chaperone heat-shock protein (Hsp70) promotes ATP-dependent release of the protein substrate from Hsp70"].
   → supports GO:0000774 adenyl-nucleotide exchange factor activity, GO:0051087
   protein-folding chaperone binding.

2. **Stimulation of Hsc70 ATPase (experimental, worm).** Papsdorf, Sacherl & Richter 2014
   measured worm BAG proteins as Hsc70 cofactors; C-terminal fragments of UNC-23 perform
   "all Hsc70-related functions, like ATPase stimulation and regulation of folding
   activity, albeit with lower affinity than BAG-1"
   [PMID:25053410 "C-terminal fragments of UNC-23 instead perform all Hsc70-related functions, like ATPase stimulation and regulation of folding activity, albeit with lower affinity than BAG-1"].
   This directly establishes that worm BAG-1 stimulates the Hsc70 ATPase and regulates its
   folding activity, with higher affinity than the muscle paralog UNC-23. WormBase used
   this paper for the experimental IDA to GO:0001671 ATPase activator activity.
   Context: worm Hsc70 (HSP-1) is regulated by two antagonistic cofactor classes — the
   J-domain protein DNJ-13 (Hsp40) and the BAG-domain protein UNC-23/BAG-1
   [PMID:25053410 "The molecular chaperone Hsc70 assists in the folding of non-native proteins together with its J domain- and BAG domain-containing cofactors"].

3. **Regulation of the Hsp70 folding/refolding cycle (mechanism, from family biology).**
   BAG proteins act as NEFs that accelerate ADP→ATP exchange, thereby tuning (and, at
   excess, antagonizing) the Hsp70 chaperone cycle
   [PMID:9873016 "The human BAG-1, BAG-2, and BAG-3 proteins bind with high affinity (KD congruent with 1-10 nM) to the ATPase domain of Hsc70 and inhibit its chaperone activity in a Hip-repressible manner"].
   UniProt FUNCTION (by similarity): "May inhibit the chaperone activity of HSP70/HSC70 by
   promoting substrate release in an ATP-dependent manner."

## Localization
- No experimental localization for worm BAG-1 in the cached literature. No transmembrane
  segment, no signal peptide (KW: Chaperone; 3D-structure; Reference proteome only).
- IBA propagates cytoplasm/cytosol (defensible for a soluble co-chaperone), plus **nucleus**
  and **membrane** from mammalian/fungal orthologs. Human nuclear localization is a property
  of the BAG-1L isoform (an N-terminally extended isoform with a nuclear-localization
  region); the single short (210 aa) worm protein lacks that N-terminal extension, so the
  nucleus IBA is a weak, isoform-driven inference. Membrane is not expected for a soluble
  cytosolic NEF with no TM domain.

## Interactions (interactome / IPI)
- Two HT-Y2H "protein binding" (GO:0005515) IPI annotations both report the **same** partner
  **Q9XWX7 = Y43F8B.2**, a DUF727-domain protein of largely unknown function
  [PMID:14704431 worm interactome WI5; PMID:19123269 WI-2007/WI8]. These are systematic
  yeast-two-hybrid maps, not BAG-1-focused studies; UniProt records the interaction
  (IntAct EBI-323218/EBI-323231, NbExp=3). GO:0005515 "protein binding" is uninformative
  per curation guidelines; the partner is not an Hsp70 and its biological meaning is unclear.

## NOT known / knowledge gaps (see review knowledge_gaps)
- **No in-vivo client/substrate repertoire** for worm BAG-1. Whether it channels Hsc70
  clients toward refolding vs. proteasomal degradation (as mammalian BAG-1 does via its UBL
  domain engaging the 26S proteasome) has not been tested in the worm, despite BAG-1
  carrying a UBL domain (FT 8–85).
- **No loss-of-function phenotype** described for `bag-1` itself. The muscle-attachment
  phenotype in this cofactor system belongs to the paralog **unc-23** (BAG2 ortholog), not
  bag-1 [PMID:25053410 "one of them being UNC-23, whose mutation induces severe motility dysfunctions"].
  Whether bag-1 is essential, redundant with unc-23, or has a tissue-restricted role is open.
- **Direct partner of worm BAG-1 in vivo** unconfirmed: family biology predicts HSP-1/Hsc70
  binding via the BAG domain, but a physical worm BAG-1–HSP-1 complex has not been
  demonstrated in the cached literature (the demonstrated worm Y2H partner is the DUF727
  protein Y43F8B.2, biologically unexplained).

## Annotation-by-annotation reasoning (summary; see YAML for detail)
- GO:0000774 adenyl-nucleotide exchange factor activity (IBA) — ACCEPT, core.
- GO:0051087 protein-folding chaperone binding (IBA/IEA/ISS ×3) — ACCEPT (BAG domain binds Hsp70); one kept as core, redundant copies non-core.
- GO:0001671 ATPase activator activity (IDA, PMID:25053410) — ACCEPT, core (experimental, worm).
- GO:0006457 protein folding (ISS) — KEEP_AS_NON_CORE (co-chaperone regulates the folding cycle; does not itself fold).
- GO:0050821 protein stabilization (IBA) — KEEP_AS_NON_CORE (plausible, unverified in worm).
- GO:0005737 cytoplasm / GO:0005829 cytosol (IBA) — ACCEPT/KEEP_AS_NON_CORE (soluble co-chaperone).
- GO:0005634 nucleus (IBA) — MARK_AS_OVER_ANNOTATED (isoform-specific mammalian property; worm lacks BAG-1L-type N-terminal extension).
- GO:0016020 membrane (IBA) — MARK_AS_OVER_ANNOTATED (no TM domain; soluble protein).
- GO:0005515 protein binding (IPI ×2, Q9XWX7) — KEEP_AS_NON_CORE (uninformative HT-Y2H interaction).

## Cached literature status
All five cited PMIDs are cached; four are abstract-only (9873016, 15333932, 25053410,
14704431), 19123269 has full text (methods/discussion only, no BAG-1 specifics). The single
experimental worm annotation (GO:0001671, PMID:25053410) is supported by the abstract text.

## Knowledge-gap statements (plain text, for provenance quoting)
No in-vivo client or substrate has been identified for C. elegans BAG-1, and it is untested whether worm BAG-1 channels Hsc70 clients toward productive refolding or toward proteasomal degradation.
No loss-of-function phenotype has been reported for the bag-1 gene itself in C. elegans, so it is unknown whether bag-1 is essential, redundant with the paralog unc-23, or has a tissue-restricted role.
The only experimentally demonstrated physical partner of worm BAG-1 is the DUF727 protein Y43F8B.2, and a direct BAG-1 to HSP-1/Hsc70 complex in C. elegans has not been shown; the subcellular site of BAG-1 action in the worm is untested.
