# Hn (P17276) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: full-length Henna (Hn-PA/PC, UniProt P17276, Swiss-Prot reviewed, GCRP canonical for FBgn0001208).
The short Hn-PD product (E8NH57) is reviewed separately in `genes/DROME/Hn/`. Folder named
`Hn__P17276` following the one-folder-per-accession convention (`dl__P15330`, `awd__P08879`).
ProtNLM2 files were not opened.

### Data and deep research
- `just fetch-gene DROME P17276 --alias Hn__P17276`; 32 GOA rows seeded.
- `just deep-research-falcon DROME Hn__P17276 --fallback perplexity-lite` FAILED (falcon: "Failed to
  authenticate"; perplexity: HTTP 401 insufficient quota). Proceeded with cached literature.
- Cached additionally: PMID:28441450, PMID:23082175, PMID:7913853, PMID:10333570, PMID:8769124.
- DOI:10.1016/0965-1748(92)90041-C resolved via Crossref to Bel, Jacobson, Silva, Ferre 1992 Insect Biochem
  Mol Biol "Developmental and biochemical studies on the phenylalanine hydroxylation system in Drosophila
  melanogaster" (not in PubMed; not readable here).

### Evolutionary grounding
- PANTHER: P17276 is in PTHR11473:SF24 (PHENYLALANINE-4-HYDROXYLASE) with human/rat/mouse PAH and
  C. elegans pah-1 (interpro/panther/PTHR11473/PTHR11473-entries.csv). Fly paralogs ple (TH) are in SF15.
- PAINT (PTHR11473-paint.tsv):
  - PTN000895564 (taxon 33213, Bilateria): GO:0004505, GO:0006559, GO:0006571. Donors include Hn itself.
  - PTN002607638 (taxon 33317, Protostomia): GO:0004510, GO:0042416, GO:0042427. Donors Hn (+ WB gene for 0004510).
  - Human PAH (P00439) has no GO:0004510 annotation (QuickGO, 0 hits). So TPH activity is a deliberate
    protostome-node assertion; do NOT transfer TPH/serotonin to vertebrate PAH.

### Experimental findings in Drosophila (what is established here)
- PAH activity: recombinant enzyme [PMID:1371286 "A nonfusion protein generated in Escherichia coli
  hydroxylates both tryptophan and phenylalanine."]; mutant activity/protein [PMID:1417795]; in vivo
  [PMID:17376153 "DTPHu functions in vivo as a phenylalanine hydroxylase in addition to its role as the
  peripheral TPH in Drosophila"].
- Tyrosine synthesis: RNAi makes Tyr essential, rescued by Tyr not Pro; fat-body Cg-Gal4 knockdown
  sufficient [PMID:28441450].
- TPH activity: in vitro [PMID:1371286, PMID:15480914]; peripheral serotonin [PMID:17376153]; neuronal
  serotonin is Trhn (CG9122) [PMID:23082175].
- Expression: larval fat body, adult head [PMID:1417795]; larval dopaminergic neurons [PMID:23082175].
- DOPA surge after eclosion altered in Hnr3 [PMID:7913853]; pteridine eye pigments [PMID:10333570].

### Inferred only (family level)
- Fe(2+) cofactor, iron ligands H284/H289/E329 (ECO:0000250); Ser272 CaMKII phosphorylation site (ECO:0000250);
  cytosol (ISS from rat PAH). Full-length Hn retains human PAH substrate/pterin loops
  (genes/DROME/Hn/Hn-bioinformatics/RESULTS.md, positive control).

### Decisions
- MODIFY general terms (GO:0004497, GO:0016714 -> GO:0004505 + GO:0004510; GO:0009072 -> GO:0006559 +
  GO:0006571; GO:0048066 -> GO:0006726).
- Dopamine biosynthesis: KEEP_AS_NON_CORE (Hn supplies Tyr; does not perform Tyr->DOPA->DA).
- Germ-band extension (acts_upstream_of) and eye pigment: KEEP_AS_NON_CORE.
- Long-term memory IGI (PMID:22323813): UNDECIDED; abstract does not mention Hn, full text unavailable.
- No NEW terms added.
