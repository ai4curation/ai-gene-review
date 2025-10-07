# L-lactate oxidase (haox, UniProt C0XIJ3) in *Lentilactobacillus hilgardii*

**Primary role:** The haox-encoded enzyme is annotated as an **L-lactate oxidase** (LOX). It catalyzes the oxidation of L-(S)-lactate to pyruvate, with O₂ serving as the electron acceptor and producing H₂O₂[\[1\]](https://www.genome.jp/dbget-bin/www_bget?ec:1.1.3.2#:~:text=Reaction). In lactic acid bacteria, such an oxidase likely functions in **lactate utilization** (providing pyruvate for metabolism) and in generating H₂O₂. For example, in related *Lentilactobacillus* (formerly *Lactobacillus*) species, LOX is implicated in oxygen-dependent conversion of lactate into acetate[\[2\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5648907/#:~:text=phosphoketolase%20pathway%2C%20but%20no%20acetate,PDH%29%20might%20be). This suggests haox allows the bacterium to use lactate as an energy source under aerobic conditions (and possibly inhibit competitors via H₂O₂ production).

* **Reaction:** (S)-lactate \+ O₂ → pyruvate \+ H₂O₂[\[1\]](https://www.genome.jp/dbget-bin/www_bget?ec:1.1.3.2#:~:text=Reaction). The enzyme requires flavin mononucleotide (FMN) as a cofactor.

* **Products:** Pyruvate (used for downstream metabolism) and hydrogen peroxide (H₂O₂). The H₂O₂ may act as a byproduct that must be detoxified by peroxidases or similar.

## Enzymatic activity and mechanism

* **Enzyme class:** LOX is an FMN-dependent oxidoreductase (EC 1.1.3.2) acting on the CH–OH group of (S)-lactate with oxygen as acceptor. It belongs to the family of α-hydroxyacid oxidases/dehydrogenases.

* **Mechanism:** Studies (mainly on the Aerococcus viridans enzyme) show LOX operates via a flavin-mediated **α-hydroxyacid oxidation** mechanism[\[3\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC23227/#:~:text=has%20been%20interpreted%20as%20supporting,bond%20interaction). In this model, the enzyme abstracts the α-hydrogen from L-lactate to form a carbanion (often via an active-site base, e.g. a conserved His)[\[3\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC23227/#:~:text=has%20been%20interpreted%20as%20supporting,bond%20interaction). Electrons from the substrate are transferred to the FMN cofactor. The reduced FMN then reacts rapidly with molecular oxygen, yielding H₂O₂ and regenerating the oxidized flavin[\[4\]](https://pubmed.ncbi.nlm.nih.gov/8589073/#:~:text=oxidase%2C%20the%20complex%20dissociates%20rapidly%2C,observed%20products%2C%20pyruvate%20and%20H2O2)[\[3\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC23227/#:~:text=has%20been%20interpreted%20as%20supporting,bond%20interaction). In summary, the substrate’s α-hydrogen is removed (carbanion or hydride transfer to FMN) and the resulting reduced flavin transfers electrons to O₂ to form H₂O₂[\[4\]](https://pubmed.ncbi.nlm.nih.gov/8589073/#:~:text=oxidase%2C%20the%20complex%20dissociates%20rapidly%2C,observed%20products%2C%20pyruvate%20and%20H2O2)[\[3\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC23227/#:~:text=has%20been%20interpreted%20as%20supporting,bond%20interaction).

* **Kinetics:** The enzyme shows strict specificity for (S)-lactate (L-lactate)[\[1\]](https://www.genome.jp/dbget-bin/www_bget?ec:1.1.3.2#:~:text=Reaction). Kinetic studies indicate large kinetic isotope effects for α-H abstraction, consistent with direct C–H bond cleavage in the rate-limiting step[\[5\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC23227/#:~:text=The%20rate%20constants%20for%20reduction,The%20results%20are%20compatible%20with). (In LOX the oxidized and reduced forms of FMN are stabilized by conserved residues, similar to other α-hydroxyacid oxidases[\[3\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC23227/#:~:text=has%20been%20interpreted%20as%20supporting,bond%20interaction).)

## Metabolic pathway involvement

* **Lactate oxidation pathway:** LOX provides a route to feed lactate into central metabolism. Under aerobic conditions, LOX converts L-lactate to pyruvate[\[1\]](https://www.genome.jp/dbget-bin/www_bget?ec:1.1.3.2#:~:text=Reaction). The pyruvate can then enter the pyruvate metabolism network (KEGG map 00620), for example being converted by pyruvate oxidase (POX) or the pyruvate dehydrogenase (PDH) complex into acetyl-CoA and ultimately acetate (with ATP generation)[\[2\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5648907/#:~:text=phosphoketolase%20pathway%2C%20but%20no%20acetate,PDH%29%20might%20be). Indeed, in *L. buchneri* (a close relative) a pathway has been proposed where LOX (or LDH) supplies pyruvate which is then converted via POX to acetate under oxygen, yielding extra ATP[\[2\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5648907/#:~:text=phosphoketolase%20pathway%2C%20but%20no%20acetate,PDH%29%20might%20be).

* **Energy metabolism:** This LOX-driven pathway effectively allows the cells to derive extra energy from lactate when oxygen is present. In heterofermentative lactobacilli, such as *L. hilgardii/buchneri*, the conversion of lactate to acetate (instead of ethanol) yields additional ATP and raises pH, stabilizing aerobic growth[\[2\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5648907/#:~:text=phosphoketolase%20pathway%2C%20but%20no%20acetate,PDH%29%20might%20be).

* **Physiological context:** *L. hilgardii* often inhabits fermentations (e.g. wine, silage) where lactate accumulates. By expressing LOX, the cells can scavenge lactate aerobically. The concomitant H₂O₂ production may also inhibit competing microbes. Thus, haox is part of the organism’s aerobic lactate catabolism pathway, linking lactate oxidation to downstream acetate-production pathways[\[2\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5648907/#:~:text=phosphoketolase%20pathway%2C%20but%20no%20acetate,PDH%29%20might%20be)[\[1\]](https://www.genome.jp/dbget-bin/www_bget?ec:1.1.3.2#:~:text=Reaction).

**Sources:** Enzyme classification and reaction from KEGG (EC 1.1.3.2)[\[1\]](https://www.genome.jp/dbget-bin/www_bget?ec:1.1.3.2#:~:text=Reaction); mechanistic details from enzymology studies[\[4\]](https://pubmed.ncbi.nlm.nih.gov/8589073/#:~:text=oxidase%2C%20the%20complex%20dissociates%20rapidly%2C,observed%20products%2C%20pyruvate%20and%20H2O2)[\[3\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC23227/#:~:text=has%20been%20interpreted%20as%20supporting,bond%20interaction); pathway context from studies of *Lactobacillus/Lentilactobacillus* lactate metabolism[\[2\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5648907/#:~:text=phosphoketolase%20pathway%2C%20but%20no%20acetate,PDH%29%20might%20be).

---

[\[1\]](https://www.genome.jp/dbget-bin/www_bget?ec:1.1.3.2#:~:text=Reaction) KEGG ENZYME: 1.1.3.2

[https://www.genome.jp/dbget-bin/www\_bget?ec:1.1.3.2](https://www.genome.jp/dbget-bin/www_bget?ec:1.1.3.2)

[\[2\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC5648907/#:~:text=phosphoketolase%20pathway%2C%20but%20no%20acetate,PDH%29%20might%20be)  Oxygen-Inducible Conversion of Lactate to Acetate in Heterofermentative Lactobacillus brevis ATCC 367 \- PMC 

[https://pmc.ncbi.nlm.nih.gov/articles/PMC5648907/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5648907/)

[\[3\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC23227/#:~:text=has%20been%20interpreted%20as%20supporting,bond%20interaction) [\[5\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC23227/#:~:text=The%20rate%20constants%20for%20reduction,The%20results%20are%20compatible%20with)  On the reaction mechanism of l-lactate oxidase: Quantitative structure-activity analysis of the reaction with para-substituted l-mandelates \- PMC 

[https://pmc.ncbi.nlm.nih.gov/articles/PMC23227/](https://pmc.ncbi.nlm.nih.gov/articles/PMC23227/)

[\[4\]](https://pubmed.ncbi.nlm.nih.gov/8589073/#:~:text=oxidase%2C%20the%20complex%20dissociates%20rapidly%2C,observed%20products%2C%20pyruvate%20and%20H2O2) L-lactate oxidase and L-lactate monooxygenase: mechanistic variations on a common structural theme \- PubMed

[https://pubmed.ncbi.nlm.nih.gov/8589073/](https://pubmed.ncbi.nlm.nih.gov/8589073/)