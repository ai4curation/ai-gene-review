# Curatorial Notes for Mouse Abhd10 (UniProtKB:Q6PE15)

## Summary of Gene Product & Structure

- **Protein**: Palmitoyl-protein thioesterase ABHD10, mitochondrial (`UniProtKB:Q6PE15`, sequence version 1; 297 aa precursor; `MGI:2442422`, chromosome 16).
- **Mitochondrial Matrix Targeting & Maturation**: Precursor residues `1..43` form a cleavable N-terminal mitochondrial transit peptide (`FT TRANSIT 1..43`), yielding the 254-aa mature mitochondrial matrix protein (`44..297`, `PRO_0000280734`).
- **X-Ray Crystal Structure & Catalytic Triad (`PDB:6NY9`, `PMID:31740833`)**:
  - Cao et al. (`PMID:31740833`) determined the 1.66-A X-ray crystal structure of mature mouse ABHD10 (`PDB:6NY9`, residues 44-293), revealing a canonical alpha/beta-hydrolase fold with an alpha-helical hydrophobic cap domain and a charge-relay catalytic triad at **Ser143**, **Asp240**, and **His270** in precursor `Q6PE15-1` numbering (reported in `PMID:31740833` on the cleaved mature chain `44..297` as `Ser100–His227–D197`, i.e., `+43` offset to precursor coordinates).
  - Alternative splice isoform `Q6PE15-2` (`VSP_023893`, `VSP_023894`) replaces Asp269 and deletes C-terminal residues `270..297`, removing general base **His270** of the catalytic triad.

## Experimental Biology in Mouse

1. **Mitochondrial S-Depalmitoylase & Redox Homeostasis (`PMID:31740833`, `PMID:37400491`)**:
   - Purified recombinant mature mouse ABHD10 directly cleaves S-palmitoylated fluorescent peptide substrates in vitro (`PMID:31740833`), and mouse `Abhd10` is targeted by serine hydrolase activity-based probes and aza-beta-lactam `ABL303` (`PMID:22400490`).
   - In two murine alcoholic liver disease (ALD) models (`PMID:37400491`), hepatic `Abhd10` is transcriptionally repressed by ELK-3, elevating inhibitory S-palmitoylation of PRDX5 Cys100 and oxidative injury; ectopic `Abhd10` overexpression ameliorates liver damage in vivo.
2. **Testis Mitochondrial Matrix Localization, Sperm Mitochondrial Sheath Organization & Male Fertility (`PMID:41285782`)**:
   - Zhou et al. (`PMID:41285782`) generated endogenous HA-tagged `Abhd10` knock-in mice (inserting the HA tag downstream of the `1..43` transit peptide) and `Abhd10` knockout (`Abhd10Del/Del`) mice.
   - Subcellular fractionation of mouse testes (purified nuclei, mitochondria, and mitochondria-depleted cytoplasm: `"Our data indicated that ABHD10 was specifically localized in the mitochondria of the testes (Fig. 5e)."`), structured illumination microscopy (SIM), and immunoelectron microscopy (`"ABHD10 is localized in the mitochondrial matrix of testes (Fig. 5h)."`) establish that mouse ABHD10 resides specifically inside the **mitochondrial matrix** (`GO:0005759`). Note that `PMID:41285782`'s statement calling ABHD10 `"testis-specific"` is adjudicated as `DISPUTED` because ABHD10 is detected across 14 mouse tissues in MitoCarta (`PMID:18614015`), expressed and functionally regulated by ELK-3 in mouse hepatocytes (`PMID:37400491`), and purified from mammalian liver (`PMID:22294686`).
   - `Abhd10` knockout males are viable but completely sterile with severe asthenozoospermia and malformed sperm mitochondrial sheaths. Mitochondrial acyl-biotin exchange proteomics, co-IP, and proximity labeling show that loss of `Abhd10` causes hyper-palmitoylation of mitochondrial sheath factors (`SPATA19`, `GK2`) and respiratory/pyruvate dehydrogenase subunits (`PDHX`, `NDUFV1`, `SDHB`). Importantly, `PMID:41285782` showed that overexpressing ABHD10 does not directly induce mitochondrial aggregation (`"ABHD10 did not induce mitochondrial aggregation"`), confirming ABHD10 acts enzymatically upstream as an S-depalmitoylase (`acts_upstream_of_positive_effect` on `GO:0120317` `sperm mitochondrial sheath assembly`) rather than as an outer-membrane structural mitochondrial-tethering scaffold (`SPATA19`/`GK2`).

## Key Curation Decisions

- **`GO:0008474` (`palmitoyl-(protein) hydrolase activity`)**: `ACCEPT` across `IDA` (`PMID:31740833`), `IBA` (`PTN001043685`), `ISO`, and `IEA`.
- **`GO:0002084` (`obsolete protein depalmitoylation`)**: `MODIFY` (`IDA` and `ISO`) -> `GO:0008474` (obsoleted in GOA in favor of the molecular function `GO:0008474`).
- **`GO:0004553` (`hydrolase activity, hydrolyzing O-glycosyl compounds`)**: `REMOVE` (`IBA`, `ISO`, `IEA` transferred from erroneous human `Q9NUJ1` annotation based on `PMID:22294686`, where acyl-glucuronide carboxylic-ester cleavage was misclassified as O-glycosyl bond hydrolysis).
- **`GO:0005829` (`cytosol`)**: `REMOVE` (`ISO` and `IEA` transferred from human `Q9NUJ1` post-mortem liver homogenate supernatant in `PMID:22294686`; directly refuted in mouse testis fractionation with mitochondria removed in `PMID:41285782`).
- **`GO:0005739` (`mitochondrion`)**: `ACCEPT` (`HDA` `PMID:18614015` MitoCarta, `IBA` `PTN001043685`, `ISO`, `ISS`, `IEA`) per the Root Organelle Policy, alongside **`NEW` `GO:0005759` (`mitochondrial matrix`, `IDA`, `PMID:41285782`)**.
- **`GO:0102390` (`mycophenolic acid acyl-glucuronide esterase activity`) & `GO:0006805` (`xenobiotic metabolic process`)**: `KEEP_AS_NON_CORE` on mammalian ortholog transfer rows (`ISO`, `ISS`, `IEA` from human `Q9NUJ1`), noting that hepatic drug acyl-glucuronide esterolysis is secondary to conserved mitochondrial S-depalmitoylation and has not been directly assayed in mouse.
- **`GO:0045454` (`cell redox homeostasis`)**: `NEW` (`IMP`, `PMID:37400491`, corroborated by `PMID:31740833`), listed in `core_functions[0].directly_involved_in` because ABHD10 directly regenerates peroxidatic Cys100 of PRDX5.
- **`GO:0120317` (`sperm mitochondrial sheath assembly`)**: `NEW` (`IMP`, `PMID:41285782`, `qualifier: acts_upstream_of_positive_effect`), kept out of `core_functions[0].directly_involved_in` per `AGENTS.md` necessity-vs-participation rules because outer-membrane tether proteins SPATA19 and GK2 physically assemble the sheath, whereas matrix ABHD10 acts enzymatically upstream by S-depalmitoylating SPATA19, GK2, and PDHX.
