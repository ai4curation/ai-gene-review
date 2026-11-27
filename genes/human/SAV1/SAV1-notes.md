# SAV1 review notes

SAV1/WW45 is the human Salvador scaffold in the Hippo pathway. The GO-CAM
activity `gomodel:65a1f4f800003542/65a1f4f800003565` uses SAV1 as a cytoplasmic
`GO:0043539` protein serine/threonine kinase activator in `GO:0035329` Hippo
signaling, with WWC2 as an input molecule and a positive causal edge to the STK3
activity. This agrees with the gene-level picture, because WWC1/2/3 bind LATS1/2
and SAV1, and SAV1 brings MST1/2 into the complex to phosphorylate and activate
LATS1/2 [PMID:35429439, "WWC proteins (WWC1/2/3) directly interact with
LATS1/2 and SAV1, and SAV1, in turn, brings in MST1/2 to phosphorylate and
activate LATS1/2."]. No GO-CAM correction is needed for this activity; the gene
review records the more specific `GO:0030674` protein-macromolecule adaptor
activity as the mechanistic molecular function that explains the
kinase-activator annotation.

SAV1 also promotes MST1/2 activation by antagonizing STRIPAK-SLMAP PP2A.
SAV1-MST2 SARAH heterodimers dimerize through the SAV1 WW domains to form a
heterotetramer in which MST2 trans-autophosphorylates, and the SAV1 N terminus
binds STRIPAK to inhibit dephosphorylation of the MST2 activation loop
[PMID:29063833, "SAV1 directly binds to STRIPAK and inhibits its phosphatase
activity, protecting MST2 activation-loop phosphorylation."].

The older MST/SAV literature supports physical association, self-association and
the apoptotic branch but is mostly too generic for GO curation beyond the
existing process and binding terms. Callus et al. showed that Mst and hSav
heterodimerize through their C-terminal coiled-coil/SARAH regions, that hSav can
homodimerize, and that Mst phosphorylates and stabilizes hSav [PMID:16930133,
"hSav was also able to homodimerize, but this did not require its coiled-coil
domain."]. Luo et al. detected hWW45 in the cytoplasm and nucleus and found that
hWW45 augments MST1-induced apoptosis [PMID:19212654, "hWW45 was present in
both the cytoplasm and nucleus."]. These apoptotic annotations are real but are
not the main contact-inhibition Hippo module reviewed here.

The adipocyte-differentiation paper reports a separable PPARgamma branch in
which SAV1 binds and stabilizes PPARgamma and increases PPARgamma
transactivation during 3T3-L1 adipocyte differentiation. These rows should be
kept as non-core because they are not part of the WWC/MST/LATS/YAP contact
inhibition module.

Two additional UniProt-curated SAV1 branches were considered but left as expert
questions rather than new annotations. Mardin et al. showed that hSav1 and Mst2
directly interact with Nek2A and regulate Nek2A centrosome localization and
phosphorylation of C-Nap1 and rootletin, implicating SAV1 in centrosome
disjunction [PMID:21076410, "the mammalian sterile 20-like kinase 2 (Mst2) and
the scaffold protein Salvador (hSav1), directly interact with Nek2A and regulate
its ability to localize to centrosomes, and phosphorylate C-Nap1 and rootletin"].
Park et al. reported that MST2 and hSAV co-expression activates ERalpha
transactivation in MCF-7 cells, with attenuation after hSAV knockdown
[PMID:21104395, "overexpression of MST2 and hSAV leads to ligand-independent
activation of ERα in human breast cancer MCF-7 cells, which was attenuated by
the knockdown of hSAV"]. Both branches are separate from the cytosolic WWC/MST/LATS
Hippo module, and the ESR1 paper is abstract-only in the cache.

All unqualified `GO:0005515` protein-binding annotations were removed under the
project protein-binding policy. They are true interaction reports in many cases,
but the informative assertion for SAV1 is scaffold/adaptor activity in Hippo
kinase complexes, plus the separate, specific `GO:0042802` identical protein
binding rows for SAV1 self-association.

Manual deep research note: Falcon and Perplexity were unavailable in the shared
runtime, and this branch was asked not to launch extra provider workers on the
2-CPU host. I therefore used the cached PMID/Reactome records and GO-CAM review
as manual research inputs rather than creating a provider-named deep-research
file.
