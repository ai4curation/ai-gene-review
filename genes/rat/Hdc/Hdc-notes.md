# Hdc notes

- UniProtKB:P16453 states: FUNCTION: Catalyzes the biosynthesis of histamine from histidine. [UniProtKB:P16453].
- Core interpretation: pyridoxal-phosphate-dependent histidine decarboxylation to histamine.
- Accepted direct GO terms include: L-histidine catabolic process, histamine biosynthetic process, histidine decarboxylase activity.
- Non-core/context terms are mostly localization, binding/cofactor, inferred pathway context, or exposure-response annotations; generic parent terms are modified when a specific catalytic term is available.

## Re-review 2026-10-10

GOA refresh (commit a3cf70b6d): 5 new rows, no retired rows.

- GO:0001694 histamine biosynthetic process, GO:0004398 histidine decarboxylase activity, GO:0006548 L-histidine catabolic process: ISO from human HDC (UniProtKB:P19113), donor-splits of the existing mouse-donor (MGI:96062) ISO rows; all ACCEPT.
- GO:0005737 cytoplasm, IBA from PANTHER:PTN007556042 (group II decarboxylase node): KEEP_AS_NON_CORE; consistent with cytosolic HDC [PMID:9525922 "the 74-kDa form of HDC, synthesized in the cytosol"].
- GO:0042401 biogenic amine biosynthetic process, IEA (ARBA): MODIFY to GO:0001694 histamine biosynthetic process (correct but broad parent of a term the gene already carries with IDA support).

Corrections to existing rows (no action changes):
- GO:0006520 amino acid metabolic process (IEA): MODIFY retained, but the proposed replacement was a molecular-function term (GO:0004398) for a biological-process annotation. Replaced with GO:0006548 L-histidine catabolic process and GO:0001694 histamine biosynthetic process.
- GO:0016597 amino acid binding (IDA, four papers): all four rows previously quoted PMID:7075603 regardless of the annotated reference. The PMID:5898 row now cites its own abstract [PMID:5898 "a Michaelis-Menten constant of 2.4 X 10(-4) histidine"]; the PMID:4449071 and PMID:9525922 rows note that their abstracts do not describe substrate binding (curator full-text decision deferred to).

UniProt quotes: 0 stale (current P16453 FUNCTION text unchanged).

Description rewritten to remove curation commentary.

Open question: amino acid binding (GO:0016597) IDA from PMID:4449071 (a gastrin/HDC activity correlation study) and PMID:9525922 (HDC processing and localization in RBL-2H3) is not obviously supported by their abstracts; a curator with full text could check whether these should stand.
