# SLC22A15 (FLIPT1 / Flipt 1) — curation notes

UniProt: Q8IZD6 (S22AF_HUMAN). Gene: SLC22A15 (HGNC:20301), synonym FLIPT1
("Fly-like putative transporter 1"). 547 aa, 12 predicted TM helices, N-glycosylated.
Member of the major facilitator superfamily (MFS), SLC22 / organic cation transporter
(OCT/OCTN/OAT) family (TC 2.A.1.19). Broad tissue expression (highest in kidney and brain).

## Summary verdict

SLC22A15 was a long-standing **orphan** SLC22 transporter. It was "deorphaned" by a single
comprehensive functional-genomic study [PMID:33124720 (Yee et al. 2020, FASEB J)], which
established it as a **polyspecific, low-affinity plasma-membrane transporter that prefers
zwitterions** (amino-acid betaines and derivatives) over organic cations and anions. The
substrate set is now experimentally grounded, but its **physiological/tissue role and transport
mechanism remain unresolved**. Earlier phylogenetic work had provisionally labelled it a
"carnitine transporter"; the 2020 study confirms carnitine is a genuine (low-affinity) substrate
but shows the preferred substrates are ergothioneine, carnosine and glycine betaine.

## Localization

- Plasma membrane (cell membrane), multi-pass. Direct evidence: western blot of the plasma-membrane
  protein fraction from transfected HEK293 cells.
  [PMID:33124720 "Western blotting of the plasma membrane protein fraction isolated from HEK293 Flp-In cells transiently transfected with SLC22A15 showed that the transporter has a plasma membrane protein expression and the expected molecular size of about 60 kDa."]
- UniProt: [UniProtKB:Q8IZD6 CC:SUBCELLULAR LOCATION "Cell membrane"], Multi-pass membrane protein (ECO:0000255).

## Molecular function — substrates (all from PMID:33124720, HEK293 uptake/efflux + metabolomics)

Preference order: zwitterions > organic cations >> anions.
- Overall: [PMID:33124720 "the experiments indicated that SLC22A15 prefers zwitterions (Fig. 3A) including ergothioneine, carnosine, carnitine and creatine."]
- Top substrates: [PMID:33124720 "The top three metabolites that had the highest fold-uptake over empty vector were the zwitterions: ergothioneine, carnosine and betaine."]
- **Glycine betaine** — confirmed substrate (basis of the curated GO:0015199 amino-acid betaine
  transmembrane transporter activity IDA). [UniProtKB:Q8IZD6 CC:FUNCTION "Displays high transport activity toward zwitterionic substrates such as glycine betaine and diet-derived ergothioneine and carnosine"]
- **Carnitine / acetylcarnitine** — bidirectional (influx + efflux). Km(carnitine) = 99 µM.
  [PMID:33124720 "In our studies, SLC22A15 transports ergothioneine and carnitine, although ergothioneine seems to be preferred over carnitine"];
  [PMID:33124720 "our experiments indicated that SLC22A15 was able to efflux carnitine and this process was inhibited by quinidine"];
  [UniProtKB:Q8IZD6 CC:FUNCTION "Bidirectionally transports carnitine and acetylcarnitine, possibly regulating their cytosolic abundance and further fatty acid catabolism via beta oxidation"]
- **Ergothioneine** (Km 354 µM), **carnosine** (Km 510 µM; specific to SLC22A15 among SLC22),
  **creatine** (Km 291 µM; also SLC22A15-specific among SLC22), dimethylglycine, glycylsarcosine,
  gabapentin (zwitterionic drug). Carnosine/creatine are novel for the SLC22 family:
  [PMID:33124720 "This is the first study to show that a member of the SLC22 family transports carnosine and creatine."]
- Weaker cation substrates: thiamine, MPP+, TEA, cimetidine.
- **Low affinity**: [PMID:33124720 "these data suggest that SLC22A15 serves as a low-affinity transporter for its substrates."]
- Does NOT transport agmatine [UniProtKB:Q8IZD6 CC:FUNCTION "Does not transport agmatine"] — this
  resolves the earlier report (Molderings et al. 2003, PMID:15028572, which characterized an
  agmatine transport system, not attributable to SLC22A15).

## Mechanism (unresolved)

- Uptake of ergothioneine/carnosine/carnitine/creatine is sodium-dependent, but lithium substitutes
  for sodium (unlike OCTN1/OCTN2), and NMDG abolishes uptake.
  [PMID:33124720 "The SLC22A15 mediated uptake of ergothioneine, carnosine, carnitine and creatine were dependent on sodium, though lithium was also able to drive the uptake of these compounds"]
- Also effluxes carnitine (facilitative), so direction is driven by electrochemical gradient.
- UniProt flags the mechanism as open: [UniProtKB:Q8IZD6 CC:FUNCTION "The transport mechanism, symport with sodium or facilitated diffusion allosterically regulated by sodium, remains to be elucidated"]
- Inhibited by GABA, quinidine, levofloxacin [UniProtKB:Q8IZD6 CC:ACTIVITY REGULATION].

## Family / phylogeny

- MFS / SLC22 family [UniProtKB:Q8IZD6 CC:SIMILARITY "Belongs to the major facilitator (TC 2.A.1) superfamily."]
- Closest to the zwitterion transporters SLC22A4 (OCTN1/ERT), SLC22A5 (OCTN2), SLC22A16
  [PMID:33124720 "human SLC22A15 is distinct from known organic cation, anion and zwitterion transporters in SLC22 family, but closest to the zwitterion transporters, SLC22A4, SLC22A5 and SLC22A16"].
- The GOA IBA rows (GO:0005886, GO:0022857) carry the whole SLC22/MFS clade in WITH/FROM, with
  Q8IZD6 itself among the donors (expected, reflects its own experimental grounding; not circular).

## GO annotation review (10 GOA rows)

- Core location = plasma membrane (GO:0005886): the three PM rows (IBA, IDA, IEA) all ACCEPT.
- Core MF = GO:0015199 amino-acid betaine transmembrane transporter activity (IDA + IEA) ACCEPT —
  directly supported by glycine betaine uptake.
- GO:0015838 amino-acid betaine transport (BP, IEA from the MF): ACCEPT — specific process matching
  the MF.
- Generic/uninformative rows → TOO_GENERAL (per maintainer ruling): GO:0016020 membrane,
  GO:0022857 transmembrane transporter activity (IBA + IEA), GO:0055085 transmembrane transport.
- NEW: GO:0015226 carnitine transmembrane transporter activity — carnitine (and acetylcarnitine)
  transport is directly measured (uptake Km 99 µM + quinidine-sensitive efflux) and curated by
  UniProt (Rhea catalytic activities, ECO:0000269|PubMed:33124720) but absent from GOA. Added
  conservatively as the second well-grounded substrate-specific MF.

Conservatism: no over-reaching BP annotations (e.g. fatty-acid oxidation, ergothioneine/carnosine
homeostasis) are asserted — these are physiological speculations in the paper, not demonstrated for
the human protein. No new ontology terms are proposed (existing GO terms cover betaine and carnitine
activities). The physiological role and in vivo substrate(s) are a genuine knowledge gap.

## References

- PMID:33124720 — Yee et al. 2020, FASEB J. Deorphaning SLC22A15. Full text cached. HIGH relevance,
  the single defining functional study.
- PMID:15028572 — Molderings et al. 2003. Agmatine transport system in tumor cells. NOT cached;
  UniProt cites it only to state SLC22A15 does **not** transport agmatine. LOW direct relevance.
- PMID:12372408 — Eraly & Nigam 2002. Original cDNA / tissue distribution (kidney, brain). NOT cached.
