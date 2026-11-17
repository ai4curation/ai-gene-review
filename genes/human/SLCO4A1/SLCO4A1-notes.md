# SLCO4A1 (OATP4A1 / OATP-E) — curation notes

UniProt: Q96BD0 (SO4A1_HUMAN). Gene: SLCO4A1 (HGNC:10953), chr 20. Synonyms:
OATP4A1, OATP-E, OATP1, SLC21A12, POAT, "colon organic anion transporter".
722 aa, 12-TM multi-pass plasma-membrane protein of the SLCO/OATP family
(PANTHER PTHR11388; TC 2.A.60; Pfam OATP PF03137 + Kazal-like domain).

## Summary of function

SLCO4A1 encodes OATP4A1, a broadly/ubiquitously expressed, Na+-independent,
multispecific organic anion transporter of the SLCO (OATP) family. UniProt
curates it as an "Organic anion antiporter with apparent broad substrate
specificity" whose recognized substrates include the thyroid hormones T3
(3,3',5-triiodo-L-thyronine), T4 (L-thyroxine) and reverse-T3, the conjugated
steroids estrone 3-sulfate and estradiol-17β-glucuronide, the bile acid
taurocholate, and the prostanoid prostaglandin E2
[file:human/SLCO4A1/SLCO4A1-uniprot.txt "Organic anion antiporter with apparent broad substrate specificity"].
The physiological dominant substrate is not firmly established; UniProt notes it
"May be involved in uptake of metabolites from the circulation into organs such
as kidney, liver or placenta."

### Mechanism (Na+-independent organic anion exchange)

OATPs generally operate as electroneutral anion exchangers rather than
Na+- or primary ATP-coupled pumps. Leuthold et al. characterized OATPs as
mediating uptake of amphipathic organic compounds "probably by acting as anion
exchangers," with transport stimulated at low extracellular pH and accompanied
by bicarbonate efflux
[PMID:19129463 "variety of amphipathic organic compounds such as bile salts, steroid conjugates,"],
[PMID:19129463 "oligopeptides, and a large list of drugs, probably by acting as anion"].
A conserved His in TM3 (His-191 in OATP4A1) underlies this pH sensitivity
[file:human/SLCO4A1/SLCO4A1-uniprot.txt "His-191) may"].
For OATP4A1 specifically, Lofthouse et al. proposed that placental uptake of
thyroid hormones and estrogens is coupled to an outward glutamate gradient
(organic anion/glutamate antiport); UniProt curates estrone-3-sulfate, T3, T4
and taurocholate / L-glutamate exchange reactions from that work
[file:human/SLCO4A1/SLCO4A1-uniprot.txt "coupled to an outward"].
Nonetheless UniProt flags that "The transport mechanism, its electrogenicity and
potential tissue-specific counterions remain to be elucidated."
Note: GO places thyroid-hormone transmembrane transporter activity (GO:0015349)
under secondary-active (antiporter) transporter activity (GO:0015291), which is
consistent with the exchanger model for OATPs (unlike the facilitative MCT8).

### Substrates (experimental)

- Estrone 3-sulfate: common OATP substrate; OATP-E (SLCO4A1) showed estrone-
  3-sulfate transport activity [PMID:10873595 "exhibited transport activity for [(3)H]estrone-3-sulfate as a common"].
- Thyroid hormones T3/T4/rT3: Fujiwara et al. identified OATP-E as a human
  thyroid hormone transporter (PMID:11316767, UniProt ref 2; abstract-only,
  not cached). UniProt curates T3/T4/rT3 transport reactions from this paper.
- Prostaglandin E2: UniProt curates a PGE2 transport reaction with evidence
  PMID:10873595 (OATP4A1 is NOT the dedicated prostaglandin transporter; that is
  SLCO2A1/OATP2A1/PGT). PGE2 is one of several substrates.
- Taurocholate, estradiol-17β-glucuronide: additional curated substrates
  (PMID:11316767, PMID:19129463).

### Expression and localization

Ubiquitous / widely expressed (pancreas, kidney, skeletal muscle, liver, lung,
brain, heart, colon, intestine, ovary, testis, prostate, thymus, spleen)
[file:human/SLCO4A1/SLCO4A1-uniprot.txt "Widely expressed"]. Expressed in
placental trophoblasts (PMID:10873595, PMID:12409283). In testis it localizes
primarily to Leydig cells, where it may act as a thyroid hormone transporter
[PMID:35307651 "OATP4A1 was also observed in LCs"],
[PMID:35307651 "where it may also function as a thyroid hormone transporter"].
Placental membrane polarity is unsettled: OATP4A1 has been reported at the basal
(fetal-facing) membrane in some studies but Lofthouse et al. assayed estrone
sulphate uptake at the MICROVILLOUS (apical, maternal-facing) membrane of the
syncytiotrophoblast (PMID:30343886). The family-level IBA "basolateral plasma
membrane" assignment is therefore not firmly established for human OATP4A1.

Core subcellular location: plasma membrane (cell membrane, multi-pass)
[file:human/SLCO4A1/SLCO4A1-uniprot.txt "Cell membrane"]. Reactome places it at
the plasma membrane transporting T3/T4 (R-HSA-879575)
[Reactome:R-HSA-879575 "able to mediate the transport of thyroid hormones"].

## GOA review decisions (15 rows)

Core MF: GO:0015349 thyroid hormone transmembrane transporter activity (QuickGO:
is_a ancestors include GO:0022857, GO:0015291; the specific, well-supported,
non-obsolete MF). NOTE: the broad grouping MF terms GO:0015347 (sodium-
independent organic anion transmembrane transporter activity) and GO:0008514
(organic anion transmembrane transporter activity) are BOTH OBSOLETE (unnecessary
grouping terms, no replacement), so the broad multispecific character is captured
in the process term GO:0043252 and the description, not as an MF id.

Core processes: GO:0043252 sodium-independent organic anion transport; GO:0070327
thyroid hormone transport. Core location: GO:0005886 plasma membrane.

- GO:0005515 protein binding (IPI, GPR25/O00155) → REMOVE (protein-binding policy;
  bare, uninformative).
- GO:0005886 plasma membrane (IEA SubCell; TAS Reactome) → ACCEPT x2 (core location).
- GO:0015132 prostaglandin transmembrane transporter activity (IDA 10873595) →
  KEEP_AS_NON_CORE (genuine curated PGE2 substrate; secondary, not dedicated PGT).
- GO:0015349 thyroid hormone transmembrane transporter activity (IBA) → ACCEPT (core MF).
- GO:0015732 prostaglandin transport (IEA) → KEEP_AS_NON_CORE (process counterpart of PGE2).
- GO:0016020 membrane (IEA InterPro) → TOO_GENERAL (plasma membrane asserted).
- GO:0016323 basolateral plasma membrane (IBA) → MARK_AS_OVER_ANNOTATED (domain
  polarity not established for human OATP4A1; apical/microvillous reported in placenta).
- GO:0022857 transmembrane transporter activity (IDA 10873595, IDA 19129463, IEA) →
  TOO_GENERAL x3 (ancestor of asserted specific transporter terms).
- GO:0030054 cell junction (IDA HPA) → KEEP_AS_NON_CORE (direct HPA IF; peripheral).
- GO:0043252 sodium-independent organic anion transport (IBA) → ACCEPT (core process).
- GO:0055085 transmembrane transport (IEA InterPro) → TOO_GENERAL.
- GO:0070327 thyroid hormone transport (IEA) → ACCEPT (core process; consistent with GO:0015349).
