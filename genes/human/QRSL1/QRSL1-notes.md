# QRSL1 notes

## Deep research

`QRSL1-deep-research-claude-code.md` came from `just deep-research-claude-code human QRSL1 --timeout 1700`.
It ran for 32 s with 2 web searches (`web_search_requests: 2`) and 5 citations, and states that it did not
read any full text and could not confirm the Friederich 2018 PMID. It was used only for leads; the PMID
for Friederich et al. 2018 (PMID:30283131) was obtained from the GATC review and fetched with `just fetch-pmid`.

## Function

- QRSL1 = human GatA, the amidase-signature subunit of mitochondrial GatCAB (QRSL1-GATB-GATC).
  UniProt active sites: Lys76 and Ser171 (charge relay), Ser195 (acyl-ester intermediate).
- GatCAB converts Glu-tRNA(Gln) (made by EARS2) to Gln-tRNA(Gln) with glutamine and ATP; GatA hydrolyses
  glutamine and channels NH3 to GatB [UniProt FUNCTION; PMID:30283131 "In the bacterial GatCAB complex, GatA and GatB possess the catalytic amidase and kinase functions, respectively, while GatC serves as a stabilizing linker between them"].
- Human GatCAB identified, siRNA of any subunit accumulates Glu-tRNA(Gln), reconstituted in vitro [PMID:19805282, abstract only].
- Kohda 2016: QRSL1 patient variants "were associated with severe transamidation activity defects" [PMID:26741492].
- Friederich 2018: QRSL1 patients (family 2, 3) with lethal cardiomyopathy; mt-tRNA(Gln) charging and
  mitochondrial translation defective under glutamine restriction [PMID:30283131].
- Mouse/human cell work (Echevarria 2014, PMID:24579914, cached without abstract text) is cited by UniProt for GatA being required for GATB stability; not quoted.

## Curation decisions

- GO:0070681 is obsolete (QuickGO: "Annotations require review rather than migration"; consider GO:0043039,
  GO:0050567). Replaced with GO:0019988 charged-tRNA amino acid modification, matching the GATC review, since
  GatCAB modifies an amino acid already attached to tRNA(Gln).
- GO:0004359 glutaminase activity (IEA from HAMAP/EC 3.5.1.2): kept as non-core. QRSL1 does catalyse the
  glutamine-hydrolysis half-reaction, but the ammonia is channelled rather than released, so the meaningful
  activity is the complex-level GO:0050567.
- Protein binding IPI rows (partners GATB, GATC) removed; captured by GO:0030956 membership.
