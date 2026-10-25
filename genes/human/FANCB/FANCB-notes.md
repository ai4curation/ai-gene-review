# FANCB (Q8NB91) — Gene Review Notes

Human Fanconi anemia group B protein / FAAP95. Gene at Xp22.31; X-linked. 859 aa. HGNC:3583.

## Summary of function

FANCB is a non-catalytic structural subunit of the Fanconi anemia (FA) core complex, the
multisubunit E3 ubiquitin ligase (FANCA/B/C/E/F/G/L/M + FAAPs) that monoubiquitinates the
FANCD2–FANCI (ID2) heterodimer during replication-coupled DNA interstrand crosslink (ICL)
repair. Within the complex FANCB forms, together with the RING E3 ligase FANCL and FAAP100,
the FANCB–FANCL–FAAP100 (BL100) catalytic module. FANCB is the dimerization/scaffold factor:
two BL100 heterotrimers associate through FANCB to give the symmetric "dimer of trimers" that
templates assembly of the whole core complex and positions the two FANCL RING domains to
ubiquitinate both FANCD2 and FANCI. Loss of FANCB abolishes FANCD2 monoubiquitination, causes
crosslinker hypersensitivity, chromosomal instability, and the FA-B clinical phenotype (often
severe VACTERL-H).

## Key provenance

### Identity, X-linkage, essentiality for FANCD2 ubiquitination
- [PMID:15502827 "the protein defective in individuals with Fanconi anemia belonging to complementation group B is an essential component of the nuclear protein 'core complex' responsible for monoubiquitination of FANCD2"] — Meetei 2004, Nat Genet; identified FANCB (=FAAP95) as FA core complex subunit.
- [PMID:15502827 "the gene encoding this protein, FANCB, is localized at Xp22.31 and subject to X-chromosome inactivation"] — X-linked inheritance; single active copy makes FANCB a uniquely vulnerable node.
- UniProt FUNCTION: [file:human/FANCB/FANCB-uniprot.txt "DNA repair protein required for FANCD2 ubiquitination"].
- UniProt SUBUNIT: multisubunit FA complex composed of FANCA, FANCB, FANCC, FANCE, FANCF, FANCG, FANCL/PHF9 and FANCM; "The complex is not found in FA patients." Nucleus (ECO:0000269|PubMed:15502827).

### FANCB is the scaffold / dimerization factor of the BL100 catalytic module
- [PMID:27986592 "leaving the FANCB subunit as the sole candidate for the dimerization element of the BL100 complex"] — Swuec 2017, cryo-EM of the dimeric catalytic module.
- [PMID:27986592 "FANCB plays a key structural function, being the dimerization factor"].
- [PMID:27986592 "its mono-ubiquitination function is stimulated by 6-fold in the presence of FANCB and FAAP100"] — FANCL activity architecturally stimulated by FANCB/FAAP100.
- [PMID:31666700 "A dimer of FANCB-FAAP100 heterodimers is located in the middle region of the structure"] — Shakeel 2019, Nature, full FA core complex structure.
- [PMID:31666700 "deletion of FANCB, FANCL or FAAP100, that comprise the catalytic module and the structural scaffold for the complex, eliminates this residual activity"].
- Note FANCB is the only BL100 protomer carrying disease-associated missense mutations (Swuec 2017), underscoring its structural role.

### Direct interaction with FANCL and FAAP100; subcomplex protects members; nuclear localization
- [PMID:17396147 "directly interacts with FANCB and FANCL to form a stable subcomplex"] — Ling 2007; FAAP100 + FANCB + FANCL = L-B-P100 subcomplex.
- [PMID:17396147 "each member of the L-B-P100 subcomplex has a disturbed nuclear localization in FA-A cells"] — nuclear import of the module is FANCA/FANCM-dependent; the module is cytosolic until chaperoned to the nucleus.

### Chromatin loading and ICL repair context
- [PMID:22343915 "required for DNA-damage-induced chromatin loading of FANCA"] — FAAP20 paper; FA core complex (incl. FANCB, IDA chromatin) loads onto chromatin upon damage.
- [PMID:19965384 "FANCI-FANCD2 is required for replication-coupled ICL repair in S phase"] — Knipscheer 2009; places the FANCD2 monoubiquitination output (which FANCB enables) in replication-coupled ICL repair.
- [PMID:20347428 "FANCM-MHF associates with the Fanconi anemia (FA) core complex"] — Yan 2010; FA core complex (of which FANCB is a subunit) purified; suppresses sister-chromatid exchanges, promotes FANCD2 monoubiquitination.

## Curation reasoning highlights
- MF "protein binding" (GO:0005515, IPI with FAAP100): uninformative; the real, well-supported MF is a protein-macromolecule adaptor/scaffold activity (GO:0030674) — FANCB bridges/dimerizes FANCL and FAAP100 and templates core-complex assembly. MODIFY.
- HR/SCE regulation IBA terms (GO:1905168, GO:2000042, GO:1990414) are phylogenetic (mouse Fancb) and reflect broad FA-pathway roles downstream of FANCB's direct scaffolding function → KEEP_AS_NON_CORE.
- Multiple redundant Reactome nucleoplasm TAS lines and cytosol TAS: locations are correct (cytosolic assembly pool + nuclear function) → ACCEPT.
- Structural PDBs: 7KZP/7KZQ etc. (human FA core complex, PMID:32939280); 6SRI (chicken, PMID:31666700).
</content>

## 2026-10-25 — Structural scaffold synthesis and source clarification

FANCB supplies an integral structural scaffold in the FANCL–FANCB–FAAP100 module. Human cellular association and reconstituted-complex experiments support this organizing role (PMID:17396147, Figure 2 and hybrid/purification Methods; PMID:27986592, assembled-module/dropout Results and XL-MS Methods). FANCL and UBE2T supply ubiquitin-transfer chemistry. Isolated FANCB self-association was not demonstrated, and human BL100, Xenopus ID2 and conserved chicken structures must remain separate experimental contexts. The core retains ICL repair participation, nucleoplasm and FA nuclear-complex membership, without asserting FANCB nuclease, polymerase, kinase or ligase activity.

The scaffold term is now GO:0140378. The earlier use of GO:0030674 overlooked its explicit usage comment directing integral protein-complex scaffolds to GO:0140378. This corrects the molecular-function representation without changing the underlying assembly evidence. The three inherited core quotations remain exact and refer to assembled-module or conserved structural evidence; they do not establish an autonomous FANCB homodimer. The 2016 study used both BL100 cryo-EM and negative-stain EM, with negative-stain ID2 reconstruction; the retained historical Cryo-EM shorthand does not describe every preparation. The 2019 conserved chicken core-complex cryo-EM study is separate.

The final annotation assessment is **17 ACCEPT, 4 KEEP_AS_NON_CORE, 1 MODIFY and 1 UNDECIDED** across the 23 inherited source objects. The unresolved chromatin context is separate from positively supported core membership: the inspected PMID:22343915 main Figure 5H labels FANCA, FANCG and FAAP20, while Figure 1 and authentic supplemental Figure S1C establish FANCB membership. All supplemental extracted Methods/captions and Figure S1 pixels were inspected; no FANCB-specific chromatin readout was identified. This does not establish absence from chromatin. Cytosolic BL100 recovery is positive, and the bounded PKR model is retained non-core without calling cytosolic FANCB inactive.

Verified PANTHER v19 ancestry and actual mouse Fancb experiments support the three context-dependent repair-regulatory annotations. PMID:25520194 and PMID:21458466 address different genetic, lesion and cellular settings; their results do not grant FANCB recombinase or helicase chemistry. Current Q8NB91 has 859 residues and no alternative-products comment. Processing and external transcript models are kept distinct from natural-product or construct equivalence.

All 17 inherited quotation paths, texts and reference associations remain unchanged. The 25 original reference identities/findings are retained, with PMID:25520194 and PMID:15299030 added from genuine existing sources. Four shared manual assessments retain both complete labeled reading scopes. Cache metadata, external original availability and actual reading are distinct; the [source guide](FANCB-source-guide.md) gives public paper, figure and database locators. No new publication quotation or NEW annotation is introduced. Earlier counts and biological shorthand in this journal describe the historical review. Its inherited COMPLETE status is preserved in this private synthesis for subsequent canonical recomputation, not a new status determination.
