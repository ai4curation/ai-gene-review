# ATP6AP2 notes

## Research workflow

- Ran `just fetch-gene human ATP6AP2`, which seeded the UniProt record, GOA file, cached publications, and review YAML.
- Ran `just deep-research-falcon human ATP6AP2 --fallback perplexity-lite`. Falcon timed out after 600 seconds; the `perplexity-lite` fallback failed with a 401 quota error. No provider-labeled deep-research file was created.
- Used cached UniProt, GOA, publications, and the PN projection artifacts for this review.

## Curation synthesis

- ATP6AP2 is best treated as a V-ATPase accessory/regulatory protein rather than as a canonical chaperone or protease. UniProt summarizes it as "involved in the assembly of the lysosomal proton-transporting V-type ATPase (V-ATPase) and the acidification of the endo-lysosomal system" [file:human/ATP6AP2/ATP6AP2-uniprot.txt].
- The strongest primary evidence comes from ATP6AP2 disease and perturbation studies: missense mutations impair interaction with ATP6AP1 and V-ATPase assembly, with downstream defects in glycosylation and autophagy [PMID:29127204 "Our results suggest that ATP6AP2 has a crucial role in V-ATPase assembly, both in invertebrates and vertebrates."].
- The neuronal disease paper supports the PN proteostasis angle because ATP6AP2 deficiency caused "severe deficiency in lysosomal acidification and protein degradation" and decreased V-ATPase membrane assembly [PMID:30985297 "severe deficiency in lysosomal acidification and protein degradation leading to neuronal cell death"].
- The EV-A71/autophagy paper provides direct knockdown support for lysosomal pH control: ATP6AP2 was described as an auxiliary V-ATPase component, and ATP6AP2 knockdown significantly increased lysosomal pH [PMID:32276428 "ATP6AP2 is an important auxiliary component of the V-ATPase complex and coordinates correct V-ATPase assembly"].
- The PN projection proposes ATP6AP2 to `GO:0060590 ATPase regulator activity` from lysosomal V-ATPase regulator leaves and already recognizes `GO:0007042 lysosomal lumen acidification` as present in GOA [file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv].

## PN decision

- Accept ATP6AP2 for the Proteostasis PN batch only through the Autophagy-Lysosome Pathway / lysosomal acidification / V-ATPase regulator branch.
- Add `GO:0060590 ATPase regulator activity` conservatively: ATP6AP2 is not the proton-pumping catalytic subunit, but multiple lines of evidence support an accessory/regulatory role in V-ATPase assembly and lysosomal acidification.
- Add `GO:0070072 vacuolar proton-transporting V-type ATPase complex assembly` because the primary literature explicitly supports assembly-factor biology.
- Keep Wnt signaling, CNS development, angiotensin maturation, MAPK signaling, TGF-beta production, plasma membrane/external side, and high-throughput exosome/granule localizations as non-core or over-broad where appropriate. These are real or plausible contexts but should not be used to broaden the PN proteostasis projection.
