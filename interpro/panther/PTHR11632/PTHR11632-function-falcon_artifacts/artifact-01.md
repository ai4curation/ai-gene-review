> HOMOGENEOUS vs HETEROGENEOUS VERDICT:
>
> - The PTHR11632 family is **HETEROGENEOUS**. It includes both succinate dehydrogenase (SQR/SDH) and fumarate reductase (QFR/FRD) flavoprotein subunits. These enzymes share the same Rossmann-fold flavoprotein core and covalent FAD chemistry, but differ in preferred catalytic directionality; SDH branches are tuned for succinate oxidation, whereas FRD branches are tuned for fumarate reduction. Therefore, propagating **GO:0000104 succinate dehydrogenase activity** from the family root would over-annotate fumarate reductase branches. (pqac-00000001, pqac-00000002, pqac-00000018, pqac-00000019, pqac-00000020)
>
> GRANULARITY LEADS FOR CURATION:
>
> - **Family-level safe term:** a broader parent term such as **oxidoreductase activity, acting on the CH-CH group of donors (GO:0016627)**, or an equivalent higher-level succinate/fumarate oxidoreductase concept, is safer than GO:0000104 at the PTHR11632 family level. (pqac-00000001, pqac-00000008, pqac-00000016)
> - **SDH/SQR subfamilies:** **GO:0000104 succinate dehydrogenase activity** is appropriate for bona fide SDH branches, including **PTHR11632:SF51**. Experimental evidence in *Desulfovibrio vulgaris* shows the representative Q72DT2 branch functions as SDH rather than FRD. (pqac-00000009, pqac-00000010, pqac-00000011, pqac-00000013, pqac-00000014)
> - **FRD/QFR subfamilies:** these should instead receive **GO:0008177 fumarate reductase activity**, because their preferred physiological role is fumarate reduction despite the shared fold and partially reversible chemistry. (pqac-00000018, pqac-00000019, pqac-00000021, pqac-00000022)
> - **Extracellular flavinylated reductases** (if they fall within this PANTHER family boundary) require **clade-specific annotation**. Some retain fumarate reductase activity, whereas others are neofunctionalized extracellular reductases, including urocanate-reducing branches and additional unresolved specificities. (pqac-00000025, pqac-00000026, pqac-00000028, pqac-00000030)
> - **Bottom line:** the currently propagated **GO:0000104** is supported for **SF51 specifically**, but it is **not safe at the family level**. (pqac-00000009, pqac-00000010, pqac-00000018, pqac-00000019)


*Blockquote: This blockquote gives the curator-facing verdict on whether PTHR11632 is functionally homogeneous enough for GO:0000104 propagation. It highlights the SDH versus FRD split and specifies where the current annotation is appropriate versus over-broad.*