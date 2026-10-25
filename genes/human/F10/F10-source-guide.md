# F10 source guide

F10 encodes the secreted factor X precursor. Proteolytic activation generates factor Xa, the serine protease that cleaves prothrombin in the calcium-, phospholipid- and factor Va-dependent prothrombinase system. The same gene therefore appears as a substrate in activation or maturation reactions and as the enzyme in later coagulation reactions. Those roles must be read from the actual participant and catalyst records.

## Precursor, processed chains and experimental preparations

The current [UniProt P00742](https://www.uniprot.org/uniprotkb/P00742/entry) source is 488 residues and has no alternative-products comment. Its annotated light chain is 41–179, heavy chain 183–488, activation peptide 183–234 and activated Xa heavy chain 235–488. Signal 1–31 and propeptide 32–40 are separate processing features. These are processed parts of one precursor, not splice-isoform identifiers. The separately captured NCBI locus records NP_001299603.1 (444 residues) and NP_001299604.1 (332 residues) do not establish their activity, maturation or localization.

The primary studies used purchased human plasma FX/Xa, recombinant FX constructs activated before assay, and deliberately Gla-deleted Xa preparations. None tests all natural products. The 2025 GGCX study uses FX-derived recognition segments in a fusion protein and labels its signal/propeptide split differently from current UniProt; that experimental boundary is retained literally rather than silently remapped.

## Human chemistry and membrane context

[Kamata et al., 1998](https://doi.org/10.1073/pnas.95.12.6630) describe purchased human Xa beta-form and chymotrypsin-generated Des[1–44] Xa. Materials and Methods and the calcium-site/inhibitor Results support peptide-substrate hydrolysis, an active-site inhibitor complex and bound calcium. The preparation lacks the Gla domain, and EGF1 calcium occupancy is partial. It cannot establish the full complement of intact Gla-domain sites or native membrane binding. Residue labels from the paper are kept in its numbering system; no universal offset to the precursor is assumed.

[Monteiro et al., 2008](https://doi.org/10.1110/ps.073016308) distinguish human factor X zymogen binding from factor Xa binding to tick Ixolaris. The inspected Results and Methods include gel filtration, calorimetry, ELISA, surface plasmon resonance and factor X activation by FIXa/FVIIIa in calcium and PC/PS vesicles. Generated Xa is measured afterward. Thus positive zymogen binding is not evidence that uncleaved factor X performs proteolysis. HEK293-expressed coagulation constructs and High Five-produced Ixolaris are separate preparations.

[Manithody et al., 2012](https://doi.org/10.1021/bi300200p) directly measure prothrombin activation using human plasma Xa, Va and prothrombin in a defined calcium/PC/PS system. Experimental Procedures, Results and Discussion also describe RVV-X activation of recombinant FX, full-length versus Gla-domainless preparations, PAR-2 reporter cleavage in EA.hy926 cells and permeability readouts. The lipid-vesicle assay supports peripheral membrane-associated Xa catalysis; it is not an intact-cell binding or transmembrane-topology assay. PAR-2 cleavage is a distinct substrate context. Controls reported as data not shown are not presented as inspected underlying data.

These primary passages were read from genuine full-text normal records. No figure pixels or supplements were inspected in this database assessment. The exact selected sections, rather than a claim to have read every paragraph, delimit the support.

## Biosynthetic locations

The ER and Golgi annotations describe genuine precursor-processing pools. In [Cao et al., 2025](https://doi.org/10.1038/s41586-025-08648-1), selected Results and Methods show FX-derived propeptide/Gla recognition elements fused with TMG2 transmembrane/BRIL/GGCX segments. Human GGCX preparations were expressed using BacMam in HEK293S GnTI cells; Sf9 cells served virus production. The paper's FX segments are signal 1–21, propeptide 22–40 and Gla 41–85. Full-length functional carboxylation assays emphasized FIX, not natural full-length F10. F10 supplies the substrate segment and GGCX performs carboxylation.

Reactome independently models ER-luminal pro-factor X as GGCX substrate, transport to the Golgi, and cleavage by FURIN. ER/Golgi residence is retained as non-core biosynthetic context. It is not turned into F10 carboxylase, transport-motor or furin activity.

## PAINT and automatic mappings

The actual [PTHR24278](https://www.pantherdb.org/panther/family.do?clsAccession=PTHR24278) target leaf PTN002542618 has an exact 488-residue ungapped P00742 alignment. Its ancestor PTN000669108 has positive IBD assertions for serine-type endopeptidase activity and extracellular region; PTN009089245 has proteolysis. No target-path NOT was found. The target's presence in descendant experimental evidence is valid, and donor count is not used as a confidence score. Captured GOA and current IBD dates remain distinct versioned assertions.

Current ARBA matches are [ARBA00027237](https://www.uniprot.org/arba/ARBA00027237) set 0 (serine endopeptidase), [ARBA00027128](https://www.uniprot.org/arba/ARBA00027128) set 24 (extracellular), [ARBA00028691](https://www.uniprot.org/arba/ARBA00028691) set 5 (ER lumen), [ARBA00028705](https://www.uniprot.org/arba/ARBA00028705) sets 0/5 (Golgi lumen), and [ARBA00092062](https://www.uniprot.org/arba/ARBA00092062) set 3 (positive TOR regulation). Actual domain, FunFam and taxonomic conditions were compared with the target; a matched rule does not by itself settle biological relevance.

The inspected InterPro Gla, calcium-binding EGF and S1-protease mappings are IPR000294, IPR001254, IPR001881, IPR012224, IPR018097, IPR018114 and IPR035972. The coagulation-protein family includes protein Z as a nonproteolytic exception; positive human Xa assays establish the target's enzymatic activity independently. [EC 3.4.21.6](https://enzyme.expasy.org/EC/3.4.21.6) explicitly names activated factor Xa and prothrombin cleavage. UniProt SL-0243 maps secreted proteins to extracellular region. Current official GO definitions include membrane-associated proteins in plasma membrane; they do not require a transmembrane helix for this location.

## Reactome participant routes

Every route below reaches human P00742 through reference entity [140617](https://reactome.org/ContentService/data/query/140617), embedded in the captured target-chain records. Location is checked on the chain entity itself, not copied only from the reaction or another participant. Light/activated-heavy chains 140631/140642 are membrane-associated; 140687/140688 are extracellular. The zymogen heavy chain is 140738. ER and Golgi pro-light/heavy chains are separately represented. Released activation/propeptides are not used as a substitute for an available intact-chain route.

| Event | Location context | Representative target route |
|---|---|---|
| [R-HSA-140686](https://reactome.org/content/detail/R-HSA-140686) | Extracellular | 140686 input → 140689 hasComponent → 140687 |
| [R-HSA-140700](https://reactome.org/content/detail/R-HSA-140700) | Extracellular | 140700 catalystActivity → 140768 physicalEntity → 140689 hasComponent → 140687 |
| [R-HSA-140769](https://reactome.org/content/detail/R-HSA-140769) | Extracellular | 140769 catalystActivity → 140768 physicalEntity → 140689 hasComponent → 140687 |
| [R-HSA-158164](https://reactome.org/content/detail/R-HSA-158164) | Extracellular | 158164 input → 140739 hasComponent → 140687 |
| [R-HSA-9015111](https://reactome.org/content/detail/R-HSA-9015111) | Extracellular | 9015111 output → 9015108 hasComponent → 140689 hasComponent → 140687 |
| [R-HSA-9668253](https://reactome.org/content/detail/R-HSA-9668253) | Extracellular | 9668253 input → 140739 hasComponent → 140687 |
| [R-HSA-9668365](https://reactome.org/content/detail/R-HSA-9668365) | Extracellular | 9668365 input → 140739 hasComponent → 140687 |
| [R-HSA-9670874](https://reactome.org/content/detail/R-HSA-9670874) | Extracellular | 9670874 input → 140739 hasComponent → 140687 |
| [R-HSA-9678434](https://reactome.org/content/detail/R-HSA-9678434) | Extracellular | 9678434 input → 140739 hasComponent → 140687 |
| [R-HSA-9769737](https://reactome.org/content/detail/R-HSA-9769737) | Extracellular | 9769737 catalystActivity → 140768 physicalEntity → 140689 hasComponent → 140687 |
| [R-HSA-9822512](https://reactome.org/content/detail/R-HSA-9822512) | Extracellular | 9822512 output → 140689 hasComponent → 140687 |
| [R-HSA-9822513](https://reactome.org/content/detail/R-HSA-9822513) | Extracellular | 9822513 input → 140739 hasComponent → 140687 |
| [R-HSA-9822514](https://reactome.org/content/detail/R-HSA-9822514) | Extracellular | 9822514 input → 140739 hasComponent → 140687 |
| [R-HSA-9823284](https://reactome.org/content/detail/R-HSA-9823284) | Extracellular | 9823284 input → 140689 hasComponent → 140687 |
| [R-HSA-9933742](https://reactome.org/content/detail/R-HSA-9933742) | Extracellular | 9933742 input → 140689 hasComponent → 140687 |
| [R-HSA-159757](https://reactome.org/content/detail/R-HSA-159757) | ER lumen | 159757 input → 159734 hasComponent → 159786 |
| [R-HSA-159819](https://reactome.org/content/detail/R-HSA-159819) | ER lumen | 159819 input → 159754 hasComponent → 159810 |
| [R-HSA-159733](https://reactome.org/content/detail/R-HSA-159733) | Golgi lumen | 159733 input → 159744 hasComponent → 159774 |
| [R-HSA-159757](https://reactome.org/content/detail/R-HSA-159757) | Golgi lumen | 159757 output → 159744 hasComponent → 159774 |
| [R-HSA-140664](https://reactome.org/content/detail/R-HSA-140664) | Plasma membrane | 140664 catalystActivity → 140663 physicalEntity → 140662 hasComponent → 140649 hasComponent → 140631 |
| [R-HSA-140686](https://reactome.org/content/detail/R-HSA-140686) | Plasma membrane | 140686 output → 140662 hasComponent → 140649 hasComponent → 140631 |
| [R-HSA-9015111](https://reactome.org/content/detail/R-HSA-9015111) | Plasma membrane | 9015111 input → 140649 hasComponent → 140631 |
| [R-HSA-9015122](https://reactome.org/content/detail/R-HSA-9015122) | Plasma membrane | 9015122 input → 140662 hasComponent → 140649 hasComponent → 140631 |
| [R-HSA-9822512](https://reactome.org/content/detail/R-HSA-9822512) | Plasma membrane | 9822512 input → 9822516 hasComponent → 140649 hasComponent → 140631 |
| [R-HSA-9822513](https://reactome.org/content/detail/R-HSA-9822513) | Plasma membrane | 9822513 output → 9822515 hasComponent → 140649 hasComponent → 140631 |
| [R-HSA-9822514](https://reactome.org/content/detail/R-HSA-9822514) | Plasma membrane | 9822514 output → 9822516 hasComponent → 140649 hasComponent → 140631 |
| [R-HSA-9822522](https://reactome.org/content/detail/R-HSA-9822522) | Plasma membrane | 9822522 catalystActivity → 9822518 activeUnit → 140649 hasComponent → 140631 |
| [R-HSA-9822556](https://reactome.org/content/detail/R-HSA-9822556) | Plasma membrane | 9822556 input → 9822516 hasComponent → 140649 hasComponent → 140631 |
| [R-HSA-9929060](https://reactome.org/content/detail/R-HSA-9929060) | Plasma membrane | 9929060 input → 9822515 hasComponent → 140649 hasComponent → 140631 |
| [R-HSA-9931624](https://reactome.org/content/detail/R-HSA-9931624) | Plasma membrane | 9931624 input → 9822516 hasComponent → 140649 hasComponent → 140631 |
| [R-HSA-9932951](https://reactome.org/content/detail/R-HSA-9932951) | Plasma membrane | 9932951 input → 140662 hasComponent → 140649 hasComponent → 140631 |
| [R-HSA-9933742](https://reactome.org/content/detail/R-HSA-9933742) | Plasma membrane | 9933742 output → 9930788 hasComponent → 140649 hasComponent → 140631 |

The disease events 9668253, 9668365 and 9670874 alter FIX/FVIII catalyst contexts while retaining native F10 substrate. Drug and serpin/TFPI events contain inhibited Xa; they do not assign inhibitor function to F10. Event 9015111 has membrane Xa input and an inhibitor-product branch containing extracellular Xa; these literal model states are retained without claiming measured translocation. All displayed target routes were recovered, while unrelated graph branches that returned rate-limit responses remain incomplete. The table describes model provenance, not newly inspected kinetic experiments for every event.


## Catalysis, membrane association and inhibitor partners

- [PMID:20427285](https://pmc.ncbi.nlm.nih.gov/articles/PMC2888451/): Experimental Procedures and operative Results, Tables I–III and the Figure 4 discussion were read. Explicitly human Xa hydrolyses peptide substrates and reacts with ZPI/SERPINA10 in systems containing protein Z, calcium and phospholipid. The crystal is ZPI with Gla-domainless protein Z; the Xa-containing ternary assembly is modeled. The Gla-domainless Xa comparison supports membrane-dependent reaction efficiency. The light-scattering experiment measures protein Z/ZPI binding, so it is not recast as direct Xa binding. No figure pixels or supplementary table were inspected.
- [PMID:6323392, original pages 187–195](https://www.jstage.jst.go.jp/article/biochemistry1922/95/1/95_1_187/_pdf/-char/en): extracted full-paper text was read, especially Methods on pages 188–189 and Results on pages 189–191 and 193. Human plasma factor X was activated with Russell's viper venom. Xa hydrolysed a peptide substrate and reacted with human protein C inhibitor/SERPINA5. The small approximately 94-kDa Xa–inhibitor complex is reported as data not shown; the prominently displayed activated-protein-C complexes must not be transferred to Xa. No figure or table pixels were inspected.
- [PMID:22409427](https://pmc.ncbi.nlm.nih.gov/articles/PMC3314109/): Materials, factor-X activation, prothrombin-activation assays and operative Results were read. Explicitly human plasma Xa, Va and prothrombin are used with calcium and PC/PS vesicles, with generated thrombin measured using S2238. This supplies an executed catalytic step in coagulation. Recombinant factor-X constructs and their activation remain distinct from the active enzyme; a HEK293 expression host alone does not establish insert identity. No figure pixels were inspected in this lane.
- [PMID:17469850](https://doi.org/10.1021/bi700136a) remains abstract-only after bounded publisher and author-copy attempts. Its positive phospholipid-binding and TF–VIIa product-inhibition results are retained, without inventing reagent species or intact-cell microscopy. [PMID:12574802](https://doi.org/10.1055/s-0037-1613438) is also abstract-only; the [Ferrara record](https://hdl.handle.net/11392/1197710) has no attached original. Gly381Asp remains a paper-coordinate designation. Independent human Xa experiments support the broad catalytic assertions while preserving these access limits.

## Extracellular protein and sequence sources

- [PMID:6587384](https://pmc.ncbi.nlm.nih.gov/articles/PMC345286/): all four original page images, 3699–3702, including Methods, Results and Figures 1–3, were inspected. This is partial human liver cDNA characterization with human plasma factor-X purification; its introductory coagulation mechanism is not a newly performed functional assay. Historical chain coordinates are not silently equated with current precursor coordinates.
- [PMID:14718574, author original](https://www.researchgate.net/publication/8480883): Data Sources/Methods and Table II were read. P00742 is positive in the literature and 2DE-MS columns and absent from the two LC-MS columns. This supports extracellular protein detection without peptide-level or product-specific assignment. No figure pixels were inspected.
- [PMID:3011603](https://doi.org/10.1016/0378-1119(86)90112-5): identity and the human liver cDNA abstract were verified; the complete original remains unavailable. Independent human plasma and enzyme experiments support the retained broad assertions.

## HuRI pairs and molecular-function specificity

[PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/) main Results, screening overview and Data availability, the [original HuRI interaction file](https://www.interactome-atlas.org/download), and current [IntAct publication records](https://www.ebi.ac.uk/intact/search?query=pubid%3A32296183) were inspected. Original records identify F10 ORF 11685, UBQLN2 ORF 71001 and partner ORF 55237, tested as GAL4 fusions in yeast. Three method records support each pair. ORF 55237 appears under historical Q7Z3S9-1 and ENSP00000462298.1 labels; current IntAct maps the source assertion to P0DPK4/NOTCH2NLC. These representations do not verify historical clone identity with the current sequence, nor native factor-X processing in the assay. Study-wide orthogonal validation is not claimed for these individual pairs.

The four binding assertions remain supported non-core associations. Xa's inhibitor partners do not confer inhibitor activity on Xa. [GO:0005112](https://www.ebi.ac.uk/QuickGO/term/GO:0005112) concerns binding a Notch surface receptor, whereas the inspected NOTCH2NLC record describes a N-terminal-like regulator. The UBQLN2 interaction does not establish [protein-folding chaperone binding](https://www.ebi.ac.uk/QuickGO/term/GO:0051087) or a proteostasis function for F10. No more specific activity was justified by the inspected assays and ontology searches.

## Migration and TOR signaling

[PMID:18612547](https://doi.org/10.1160/TH07-12-0722) has positive abstract findings in an Adriamycin-resistant MCF-7 context, including TF–VIIa–Xa-associated mTOR/p70S6K phosphorylation and rapamycin-sensitive migration. Complete Methods, active-Xa-specific causal controls and receptor attribution were not recovered. Both direct assertions remain UNDECIDED, consistently with the separate database TOR context; this does not deny the reported phenotype.


## Original-access boundaries

Normal publication files remain unchanged. Externally recovered originals are distinguished from abstract-only normal records in the reference assessments. Text inspection and actual image inspection are stated separately above. The complete migration/TOR article remains unavailable; its positive abstract is retained without resolving active-Xa-specific causality. No equivalence is inferred for all natural products or for historical clone accessions.

## Catalytic synthesis and ontology

The core uses current [serine-type endopeptidase activity](https://www.ebi.ac.uk/QuickGO/term/GO:0004252), with prothrombin cleavage specified in its biological description. The former [coagulation factor Xa activity term](https://www.ebi.ac.uk/QuickGO/term/GO:0003804) is obsolete. Calcium and phospholipid binding are retained as supporting facets rather than redundant catalytic units. The soluble extracellular pool and peripheral external membrane location have separate current location terms. No specific prothrombinase-complex identifier was established by the bounded ontology search.

For this synthesis, the human Xa preparation, crystallization and calcium-binding Results in [PMID:9618463](https://doi.org/10.1073/pnas.95.12.6630) and the human plasma reagents/prothrombin-activation Methods and Results in [PMID:22409427](https://doi.org/10.1021/bi300200p) were reread. No new figure pixels or supplements were inspected. The prior direct read of [PMID:20427285](https://pmc.ncbi.nlm.nih.gov/articles/PMC2888451/) supplies the membrane-dependent inhibition and inhibitor-role scope. These data support activated Xa, not intrinsic activity of an uncleaved precursor or equivalence of all natural transcript products.
