# Nicotine bioRxiv preprint notes

## Source

- Schwabe BTW, Angstman IM, Vollheyde K, Ingold Z, Li J, Stankevich KS, Spicer CD, Fascione MA, Grogan G, Geu-Flores F, Lichman BR. 2025. **Nicotine biosynthesis completed by cryptic activating glucosylation**. bioRxiv. DOI: `10.64898/2025.12.04.692101`.
- Direct preprint page: `https://www.biorxiv.org/content/10.64898/2025.12.04.692101v1`
- Supporting lab pages: `https://lichmanlab.weebly.com/research-articles.html` and `https://lichmanlab.weebly.com/news.html`

## Key findings from the full preprint

- The paper identifies an **A622-MATE1-beta-GD1 gene cluster** in tobacco, plus a homeologous **A622L-MATE2-beta-GD2** cluster; these clustered genes are root enriched and tightly co-expressed with known nicotine biosynthesis genes.
- A **UGT1** candidate is nominated because its expression mirrors **A622** after topping and correlates with the nicotine pathway gene set.
- The authors reconstitute a **four-enzyme nicotine synthase cascade** in vitro using **UGT1, A622, BBLa, and beta-GD1** together with nicotinic acid, N-methylpyrrolinium, UDP-glucose, and NADPH, producing **(S)-nicotine**.
- The paper assigns explicit catalytic roles to those four enzymes:
  - **UGT1 = NaGT**, a nicotinic acid N-glucosyltransferase
  - **A622 = NaGR**, a nicotinic acid N-glucoside reductase
  - **BBLa = NicGS**, an `(S)`-nicotine glucoside synthase that drives pathway stereoselectivity
  - **beta-GD1 = NicGH**, a nicotine glucoside hydrolase
- Structural work strongly supports the late-pathway assignments:
  - **A622/NaGR** was solved at **1.3 A** with NADP+ and nicotinic acid N-glucoside
  - **BBLa/NicGS** was solved with FAD and with `(S)`-nicotine glucoside product
- In **N. benthamiana** leaves, the in planta reconstruction uses **ODC, PMT, and MPO** to generate N-methylpyrrolinium, then depends on the glucosylation-late-pathway module to make labelled nicotine.
- Dropout and knockout experiments support the mechanistic assignments:
  - removing **beta-GD1/NicGH** causes nicotine glucoside accumulation
  - removing **BBL/NicGS** reduces nicotine and leaves residual racemic product
  - removing **A622/NaGR** blocks conversion beyond nicotinic acid N-glucoside
- The paper's coexpression tables keep several classical nicotine genes tied to the new glucosylation model:
  - genes most correlated with **A622** include **MATE1, PMT3, PMT2, PMT1, beta-GD1, AO2B, and MPO1**
  - genes most correlated with **UGT1** include **BBLa, QPT2, beta-GD1, A622, PMT1, PMT2, PMT3, and MATE1**

## Boundary conditions for NICAT curation

- The mechanistic reconstruction and structural work are centered on **tobacco** enzymes plus **N. benthamiana** reconstitution, not directly on fetched NICAT accessions.
- For the NICAT project, this paper is therefore strongest for **pathway-role assignment** and weakest for **exact paralog/accession resolution**.
- The paper materially strengthens **UGT1, A622, BBL, beta-GD/BGL, MATE1, PMT, MPO, ODC, QPT2, and AO2-like** genes as the right biological module to curate, but it does **not** by itself resolve which current NICAT public accession is the correct paralog in every duplicated family.
- The paper does **not** materially resolve the remaining NICAT **NaNAMNH** accession gap.

## Usable implications for this project

- **A622** and **BBL** should be treated as core late-pathway enzymes with direct mechanistic support, not as loose historical candidates.
- **BGL/beta-GD** and **UGT1** are now clearly pathway-core rather than side chemistry.
- **MATE1** should remain in the core set because it is genomically and expression-linked to the late-pathway module.
- **ODC, PMT, and MPO** remain part of the minimal upstream module needed to feed the completed pathway.
- **QPT2** and **AO2** are supported at the level of coordinated pathway expression and pathway framing, but this paper does not directly assay their enzymatic roles.
