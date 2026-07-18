# SLC35A1 (human) — curation notes

UniProt: P78382 (S35A1_HUMAN). Gene: SLC35A1 (HGNC:11021). 337 aa. Chromosome 6.
Family: nucleotide-sugar transporter family, SLC35A subfamily (drug/metabolite transporter, DMT, superfamily; TCDB 2.A.7.12.11).

## Core biology (from local UniProt file: file:human/SLC35A1/SLC35A1-uniprot.txt)

- **Molecular function.** CMP-sialic acid transporter (CMP-SA-Tr / CST). Multipass Golgi-membrane
  nucleotide-sugar transporter. Functions as an **antiporter** that imports CMP-N-acetylneuraminate
  (CMP-Neu5Ac / CMP-sialic acid) from the cytosol into the Golgi lumen **in exchange for CMP**:
  [file:human/SLC35A1/SLC35A1-uniprot.txt "Transports CMP-sialic acid from the cytosol into the Golgi apparatus, functioning as an antiporter that exchanges CMP-sialic acid for CMP"].
  UniProt gives the RHEA reaction (RHEA:67724): CMP-N-acetyl-beta-neuraminate(in) + CMP(out) =
  CMP-N-acetyl-beta-neuraminate(out) + CMP(in), with evidence ECO:0000269|PubMed:12682060 and
  ECO:0000269|PubMed:15576474. KM = 60 uM for CMP-N-acetyl-beta-neuraminate (PubMed:12682060).
- **Secondary substrates.** Can also exchange CMP-sialic acid for AMP and UMP
  [file:human/SLC35A1/SLC35A1-uniprot.txt "Also able to exchange CMP-sialic acid for AMP and UMP"]
  and (by similarity to mouse Q61420) mediates transport of CDP-ribitol
  [file:human/SLC35A1/SLC35A1-uniprot.txt "Also mediates the transport of CDP-ribitol"].
  The CDP-ribitol activity supplies the CDP-ribitol used in matriglycan synthesis on alpha-dystroglycan
  (Reactome R-HSA-9940804 "SLC35A1,4 import CDP-ribitol"; R-HSA-9939291 Matriglycan biosynthesis on DAG1).
- **Location.** Golgi apparatus membrane; Multi-pass membrane protein
  [file:human/SLC35A1/SLC35A1-uniprot.txt "SUBCELLULAR LOCATION: Golgi apparatus membrane"].
  10 predicted transmembrane helices (FT TRANSMEM records). Golgi localization confirmed experimentally
  by immunofluorescence (PubMed:9644260; PubMed:23873973). The C-terminus is cytosolic
  (PubMed:9644260: "the C-terminus of the human CMP-Sia transporter is exposed to the cytosol on the
  outer surface of the Golgi membrane").
- **Quaternary structure.** Monomer (PubMed:30985278, SUBUNIT; abstract-only, not cached).
- **Biological role.** Supplies the CMP-sialic acid substrate to Golgi-lumenal sialyltransferases,
  thereby enabling sialylation (terminal capping) of N-glycans, O-glycans, and glycolipids. It is a
  transporter, not itself a glycosyltransferase.

## Disease

- **SLC35A1-CDG / CDG type IIf (CDG2F; MIM:603585).** Autosomal-recessive congenital disorder of
  glycosylation with a generalized sialylation defect.
  - First case: PubMed:15576474 (Martinez-Duncker et al. 2005, Blood). Patient lacked sialyl-Lewis-x
    on polymorphonuclear cells; genetic complementation in Lec2 CHO cells showed neither patient
    SLC35A1 allele restored sialylation
    [PMID:15576474 "No complementation was obtained with either of the 2 patient alleles, whereas full restoration of the sialylated phenotype was obtained in the Lec2 cells transfected with the corresponding human wild-type transcript"].
    Named "a new type of congenital disorder of glycosylation (CDG) of type IIf affecting the transport
    of CMP-sialic acid into the Golgi apparatus".
  - Second patient / p.Gln101His: PubMed:23873973 (Mohamed et al. 2013, Neurology). Homozygous
    c.303G>C (p.Gln101His) missense; combined N- and O-glycosylation abnormalities, specific reduction
    in sialylation, macrothrombocytopenia, intellectual disability, seizures, ataxia, bleeding diathesis
    [PMID:23873973 "Functional analysis of mutant SLC35A1 showed normal Golgi localization but 50% reduction in transport activity of CMP-sialic acid in vitro"].
    Note the variant does NOT mislocalize the protein — it lowers transport activity.
  - Further variants p.Thr156Arg and p.Glu196Lys (PubMed:28856833, Ng et al. 2017; abstract-only,
    not cached) — encephalopathy.
- Phenotype prominently includes **thrombocytopenia / macrothrombocytopenia and bleeding diathesis**,
  reflecting the role of platelet-surface sialylation.

## Key annotation-relevant references

- PubMed:9010752 (Ishida et al. 1996) — original cDNA cloning (isoform 1).
- PubMed:9644260 (Ishida et al. 1998, J Biochem) — functional expression corrects Lec2 CHO mutant;
  Golgi localization by IF; C-terminus cytosolic. TAS source for several ProtInc annotations. Cached.
- PubMed:12682060 (Aoki et al. 2003, JBC) — transporter activity, substrate specificity, KM. Abstract
  not cached; used by UniProt as ECO:0000269 for the antiport reaction. (Do not quote as file:/PMID:.)
- PubMed:15576474 (Blood 2005) — CDG2F, IDA for CMP-Neu5Ac transport. Cached (abstract-only).
- PubMed:23873973 (Neurology 2013) — CDG2F p.Q101H; EXP Golgi localization. Cached (abstract-only).
- PubMed:30985278 (Ahuja & Whorton 2019, eLife) — structural basis, monomer. Abstract-only, not cached.
- PubMed:32296183 (Luck et al. 2020, Nature; HuRI) — high-throughput binary interactome (Y2H). Source
  of the 35 IntAct "protein binding" (GO:0005515) IPI calls. These are systematic Y2H interactors with
  no established functional relationship to CMP-sialic acid transport; treat as over-annotation, not
  core function. Cached (full text available).

## Curation decisions summary

- Core MF/BP/CC: CMP-N-acetylneuraminate transmembrane transporter activity (GO:0005456),
  antiporter activity (GO:0015297), CMP-N-acetylneuraminate transmembrane transport (GO:0015782),
  Golgi membrane (GO:0000139). All verified via OLS 2026-07.
- ACCEPT the experimental / phylogenetic / ISS annotations for CMP-sialic acid transport, antiport,
  and Golgi membrane/apparatus.
- protein binding (GO:0005515) IPI x35 (all one HuRI reference) → MARK_AS_OVER_ANNOTATED (never REMOVE
  an IPI per policy; uninformative bare term from HT Y2H).
- pyrimidine-nucleotide / pyrimidine-nucleotide-sugar / organophosphate-ester / nucleobase-containing-
  compound transport IEA (InterPro/ARBA/inter-ontology) → over-general family-level electronic
  inferences; MARK_AS_OVER_ANNOTATED (they are true-ish superclasses but not the specific function).
- plasma membrane (GO:0005886, TAS ProtInc PMID:9644260) → the actual paper localizes the protein to
  the **Golgi** membrane, not the plasma membrane; the TAS PM call is not supported → MARK_AS_OVER_ANNOTATED
  (keep, do not REMOVE; TAS legacy ProtInc).
- CDP-ribitol import (Reactome R-HSA-9940804 → GO:0015218 pyrimidine nucleotide transmembrane
  transporter activity TAS) — a real, By-similarity secondary activity; KEEP_AS_NON_CORE.
- protein O-linked glycosylation (GO:0006493) / carbohydrate metabolic process (GO:0005975) /
  protein modification process (GO:0036211) — downstream processes SLC35A1 enables by supplying
  substrate, but it is a transporter not a glycosyltransferase → KEEP_AS_NON_CORE.
