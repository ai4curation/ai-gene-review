# arr notes

## 2026-06-13 AMR GO-gap review

Selected because Arr is a classic rifampin-inactivation enzyme with essentially no useful GOA coverage in the fetched file. UniProt O67972 names it "Rifampin ADP-ribosyl transferase" and cross-references CARD `arr-1` as antibiotic inactivation [file:genes/MYCSM/arr/arr-uniprot.txt]. The original M. smegmatis paper states that the organism inactivates rifampin by ribosylating it, that the cloned gene confers low-level resistance, and that targeted disruption increases rifampin susceptibility and removes antibiotic-inactivating ability [PMID:9371349].

The AMR mapping file records `ARO:3000390` as a GO gap because `GO:0003950` is a poly-ADP-ribosyltransferase term and protein-focused mono-ADP-ribosyltransferase terms do not fit a rifampin substrate [file:projects/ANTIMICROBIAL_RESISTANCE/aro2go.sssom.yaml]. The review proposes a new `rifampin mono-ADP-ribosyltransferase activity` term and adds only a broad interim `GO:0016740` transferase candidate.
