# MET8 (YBR213W) notes

## Identity
- Bifunctional siroheme synthase Met8p: precorrin-2 dehydrogenase (EC 1.3.1.76) and sirohydrochlorin ferrochelatase (EC 4.99.1.4); 274 aa; homodimer [UniProt:P15807].
- PANTHER PTHR35330 (siroheme biosynthesis protein MET8); InterPro IPR028161 Met8-like [UniProt:P15807].

## Evidence
- Purified His-tagged Met8p performs dehydrogenase and chelatase reactions in vitro [PMID:10051442 "The results demonstrated that Met8p acts as a dehydrogenase and chelatase in the biosynthesis of sirohaem."].
- Crystal structure (PDB 1KYQ, 2.2 A), homodimer, NAD bound; single active site with Asp141 needed for both activities [PMID:11980703 "Met8p is a bifunctional enzyme that carries out both of these reactions."; "Asp141 plays an essential role in both dehydrogenase and chelatase processes"].
- Chelatase assays used sirohydrochlorin with Co2+ as metal surrogate [PMID:11980703 "The chelatase activity was assayed by incubating sirohydrochlorin with enzyme and cobalt, since cobalt is more stable than ferrous iron"]. No protoporphyrin IX substrate was tested; Met8p is structurally unrelated to protoporphyrin ferrochelatase HemH [PMID:11980703 "There is no structural similarity between any region of Met8p and the known structures of the anaerobic cobalt chelatase, CbiK, or protoporphyrin IX ferrochelatase (HemH)"].
- Met1p and Met8p both required for siroheme synthesis [PMID:9003798].

## Annotation issues
- GO:0004325 protoporphyrin ferrochelatase activity (IDA PMID:11980703; IEA InterPro IPR028161) is wrong: the substrate is sirohydrochlorin, not protoporphyrin IX. Protoheme ferrochelatase in yeast is HEM15. The correct term GO:0051266 sirohydrochlorin ferrochelatase activity is already annotated (EXP).
- "heme biosynthetic process" RCA comes from superpathway PWY3O-69; true only through siroheme being is_a heme in GO.
