# Serpinh1 curation notes

Deep research status: `just deep-research-falcon mouse Serpinh1 --timeout 1800 --fallback perplexity-lite` completed on 2026-05-03 and created `Serpinh1-deep-research-falcon.md`. Earlier short-timeout Falcon attempts failed before the required long run was used.

Core evidence: Serpinh1/Hsp47 is an ER-resident, collagen-specific protein folding chaperone. It is a serpin-family protein by fold, but the reviewed biology supports collagen chaperone activity rather than serine protease inhibitor activity.

Falcon synthesis: The Falcon report independently supports that SERPINH1/HSP47 is an ER-luminal collagen-specific chaperone that adopts a serpin fold but lacks serine protease inhibitory activity; it binds triple-helical procollagen/collagen in the ER, stabilizes collagen triple helices, prevents aggregation, and is retrieved to the ER after transient early secretory pathway transit [file:mouse/Serpinh1/Serpinh1-deep-research-falcon.md "SERPINH1 encodes **HSP47**, an **ER-resident, collagen-specific molecular chaperone** that adopts a **serpin fold** but **lacks serine protease inhibitory activity**"; file:mouse/Serpinh1/Serpinh1-deep-research-falcon.md "HSP47 binds **triple-helical procollagen** in the ER and **stabilizes the triple helix**"; file:mouse/Serpinh1/Serpinh1-deep-research-falcon.md "The dominant functional localization of SERPINH1/HSP47 is the **ER lumen**"].

Collagen-binding evidence: Koide et al. state that "The collagen binding chaperone HSP47 interacts with procollagen in the endoplasmic reticulum and plays a crucial role in the biosynthesis of collagen" and conclude that "HSP47 preferentially recognizes collagenous Gly-X-Y repeats in triple-helical conformation" [PMID:10862616].

Knockout evidence: Nagai et al. state that "Hsp47 is an ER-resident stress inducible glycoprotein that specifically and transiently binds to newly synthesized procollagens" and that type I collagen "is unable to form a rigid triple-helical structure without the assistance of molecular chaperone Hsp47" [PMID:10995453].

Developmental evidence: The chondrocyte conditional knockout supports cartilage and endochondral-bone phenotypes downstream of collagen maturation. These are valid non-core biological consequences of the collagen chaperone defect [PMID:22492985].

Curation rule: GO:0004867 serine-type endopeptidase inhibitor activity should be removed for Serpinh1 despite the serpin fold. GO:0051082 unfolded protein binding should be modified to GO:0044183 protein folding chaperone because the supported activity is collagen-specific chaperoning.
