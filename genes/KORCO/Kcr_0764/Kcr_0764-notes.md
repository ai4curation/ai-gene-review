# Kcr_0764 (B1L4Y3) notes

Candidatus Korarchaeum cryptofilum OPF8, taxon 374847. Unreviewed TrEMBL entry, PE 3. 648 aa.
ARCHAEA project, pattern 20 ("Korarchaeum check").

## Sequence features (UniProt record, DR/FT lines)

- InterPro IPR039650 HdrA-like family; PANTHER PTHR43498:SF1; Pfam PF12831 FAD_oxidored,
  PF00037 Fer4, PF12838 Fer4_7; Gene3D 3.50.50.60 FAD/NAD(P)-binding (x3).
- Four PROSITE PS51379 4Fe-4S ferredoxin-type domains (234-264, 281-315, 573-602, 603-631),
  three PS00198 conserved-site matches. Cys motifs visible in the sequence, e.g. CVACGICAESCP,
  CTGCGACVEECP, CMGCGICQGACP. Same architecture as methanogen HdrA (P60200, 657 aa).
- No ECO:0000269 statements; FUNCTION, PATHWAY, SUBUNIT lines are ARBA/RuleBase (RU366072) family
  transfers and are not evidence that this protein reduces CoM-S-S-CoB.

## Genome paper (Elkins et al. 2008, PMID:18535141; full text now cached from PMC HTML)

- Peptide fermenter: "The predicted gene functions suggest that the organism relies on a simple mode
  of peptide fermentation for carbon and energy" [PMID:18535141].
- Only terminal reduction is H2 production: "The only terminal reduction reaction predicted from the
  genome sequence is hydrogen production, apparently catalyzed by two soluble [NiFe]-hydrogenases."
  [PMID:18535141]
- Hdr mentioned only as a speculative coupling site: "a system that might involve homologs of the
  methanogen hdrABC -type heterodisulfide reductase complex." [PMID:18535141]
- CODH: "The korarchaeote also encodes a homolog of a single subunit [Ni-Fe] carbon monoxide
  dehydrogenase and its accessory proteins in a cluster of methanogen-like genes." [PMID:18535141]
  The survey shows this cluster is the one containing Kcr_0764 (Kcr_0762 CooS, Kcr_0763 CooC).
- Cofactor gaps: "However, many genes are missing for coenzyme biosynthesis that are conserved in most
  of the other archaea." [PMID:18535141]. The paper does not mention MCR, coenzyme M or coenzyme B.

## Later korarchaeal genomes (McKay et al. 2019, PMID:30833730; abstract cached)

- Title verified: "Co-occurring genomic capacity for anaerobic methane and dissimilatory sulfur
  metabolisms discovered in the Korarchaeota" (Nat Microbiol 4:614-622). Not the "N2 fixation" title
  in the lead.
- The MCR-bearing korarchaeote is a different organism: "One population is closely related to
  'Candidatus Korarchaeum cryptofilum OPF8', while the more abundant korarchaeote, 'Candidatus
  Methanodesulfokores washburnensis', contains genes that are necessary for anaerobic methane and
  dissimilatory sulfur metabolisms." [PMID:30833730]
- From the author manuscript (NSF PAR, https://par.nsf.gov/servlets/purl/10101006, read but not cached,
  so not quoted in the review): ANI between M. washburnensis and K. cryptofilum OPF8 is 70%; mcrA and
  dsrAB lie in gene clusters "belonging exclusively to the divergent korarchaeotal population"; the
  K. cryptofilum WS population is 98.7% ANI to OPF8. So methanogenesis genes in Korarchaeota do not
  extend to K. cryptofilum. M. washburnensis has mvh-hdrAC but no HdrB.

## Hdr-like complexes in non-methanogens

- sHdr of sulfur oxidizers: "a large group of archaeal and bacterial sulfur oxidizers utilize a novel
  pathway of sulfur oxidation involving a heterodisulfide reductase (Hdr)-like enzyme complex
  resembling the HdrABC ... of methanogens, although a coenzyme M-coenzyme B (CoM-S-S-CoB)
  heterodisulfide is not present in the sulfur oxidizers" [PMID:30004385].
- Koch & Dahl 2018 [PMID:29930335]: Hdr-like system oxidizes sulfur from DMS(O)/organosulfur in
  Hyphomicrobium.
- sHdrA structure [PMID:32750208]: core like methanogen HdrA, FAD semiquinone stable; no bifurcation.
- K. cryptofilum is not a sulfur oxidizer (the genome paper finds no dissimilatory sulfur metabolism),
  and its hdr-like gene order (hdrA-mvhD-hdrC-hdrB beside CODH) is not the sHdr hdrC1B1A-hyp-hdrC2B2
  arrangement. So sHdr is not a ready analogy either; the acceptor is unknown.

## CoM/CoB gene survey (Kcr_0764-bioinformatics/, run 2026-11-09)

UniProt REST queries on taxonomy_id:374847 (1602 entries): 0 hits for MCR (IPR003183, IPR003179,
IPR003178), ComA (IPR003830), ComB (IPR005238), ComDE (IPR022502, IPR022494), HdrB family IPR017678,
HdrC family IPR053646; 0 hits for name queries coenzyme M / coenzyme B / sulfolactate / sulfopyruvate /
phosphosulfolactate / 7-mercaptoheptanoyl / homocitrate synthase. 3 HdrA-like (IPR039650) proteins.
See RESULTS.md.

## PAINT node PTN000078336

QuickGO: GO:0051912 IBA rows from this node go to 5 proteins: P60200 (M. jannaschii), Q8TLB0/Q8TM02
(M. acetivorans), B1L4Y3 and B1L5Y2 (K. cryptofilum). Sole with/from donor P60200, whose own IDA
cites a selenoprotein paper (genes/METJA/hdrA). The node spans methanogens and a non-methanogen. The
fold and cofactor set are inherited by K. cryptofilum, but the substrate (CoM-S-S-CoB) needs MCR,
which K. cryptofilum lacks; so the substrate-specific function should have been placed at a node
excluding Korarchaeum (or the Korarchaeum branch marked as loss/divergence).

## Decisions

- IBA GO:0051912: REMOVE (over-propagation; no heterodisulfide in this organism).
- IEA oxidoreductase activity: ACCEPT (as precise as the evidence allows; substrate unknown).
- IEA cytoplasm: ACCEPT (soluble flavoprotein, no TM/signal features; cytoplasmic in methanogens).
- NEW: 4 iron, 4 sulfur cluster binding; FAD binding; electron transfer activity.
