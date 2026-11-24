# MIA40 (At5g23395, UniProt Q8GYJ4) curation notes

## 2026-11-11/13 initial review

### Sources and access
- Carrie et al. 2010 (PMID:20829360) is the only primary study of this locus and the source of every experimental GOA row. Only the abstract could be read: PMC (HTTP 403), Europe PMC full-text XML (HTTP 500), BioC and the JBC site all refused on 2026-11-11. Experimental rows were therefore deferred to the curators rather than overruled.
- Full text was available for Peleh et al. 2017 (PMID:29117860), Zannini et al. 2023 (PMID:38001802), Carrie et al. 2010 BMC Plant Biol (PMID:21078193) and the Carrie & Soll 2017 commentary (PMID:29241459). Uhrig et al. 2016 (PMID:27923987, SLP2) is abstract-only.
- Literature search (PubMed, 2026-11-11): `MIA40 Arabidopsis` (7 hits) and `(Mia40 OR CHCHD4) AND (plant OR Arabidopsis OR Physcomitrella OR rice) AND (intermembrane OR peroxisom)` (12 hits). PMID:33856743 (glioma) is retracted and off-topic; PMID:18779329 and PMID:18639549 are yeast/trypanosome background and were not cited.

### Key evidence
- Dual location: [PMID:20829360 "A. thaliana Mia40 is targeted to and accumulates in mitochondria and peroxisomes."]; peroxisomal targeting via C-terminal SKL [PMID:29117860 "Mia40 (AtMia40) is located both in mitochondria and peroxisomes (due to a C-terminal SKL targeting signal)"]. The UniProt sequence ends `...GNSKL`.
- Not essential: [PMID:20829360 "inactivation of Mia40 results in no detectable deleterious phenotype"]; small TIM and carrier import normal in mutants [PMID:21078193 "the import of the small Tim proteins and carrier proteins is normal in Arabidopsis plants that lack Mia40"].
- Activity: AtMIA40 catalytic disulfide −295 mV [PMID:38001802]; with AtERV1 it drives near-complete AtCOX19 oxidation [PMID:38001802 "the combined presence of AtMIA40 and AtERV1 promoted a near-complete AtCOX19 oxidation"]; with glutathione AtERV1 no longer needs it [PMID:38001802 "the reaction was not improved by the presence of AtMIA40"]. AtCCMH was oxidized efficiently only when AtMIA40 was paired with yeast Erv1; with AtERV1 the reaction was very inefficient.
- Dependent proteins: mitochondrial CSD1, CCS, complex I; peroxisomal CSD3, AIM1 [PMID:20829360].

### Judgment calls
- **GO:0015035 "protein-disulfide reductase activity" accepted.** The GO definition is direction-neutral ("a protein with reduced sulfide groups = a protein with oxidized disulfide bonds"), so it covers Mia40's oxidation of substrates. GO:0015036 disulfide oxidoreductase activity is its parent (OLS ancestors, 2026-11-11), so the human CHCHD4 review's MODIFY to GO:0015036 generalizes rather than refines; the ECOLI dsbA/dsbB reviews accept GO:0015035 for an enzyme that is likewise physiologically an oxidase.
- **GO:0045041 → GO:0160203.** GO:0160203 is an is_a child of GO:0045041 (OLS). The project ontology build labels it "mitochondrial disulfide relay system"; current OLS labels it "protein import into the intermembrane space via the disulfide relay system". The project label is used so validation passes.
- **GO:0070585 obsolete.** GOA labelled it obsolete on fetch (2026-11-11); an OLS fetch on 2026-11-12 still returned it as active. QuickGO (2026-11-13) confirms obsoletion on 2026-11-05 as "an unnecessary grouping term", with consider-terms including GO:7770058. Row changed to MODIFY → GO:0160203, with GO:7770058 named as the fallback.
- **Chloroplast ISM (GO_REF:0000122) removed.** Sequence-only prediction; experimental localization to two other organelles, each with a mechanism; no transit peptide in UniProt.
- **No NEW annotations.** The SLP2 interaction and the CSD1/CCS/complex I dependency data were not turned into new process terms: they establish necessity, not which step MIA40 performs.
