# CAMK2A Review Notes

## 2025-01-14: Removed annotations not in GOA

Removed the following annotations from existing_annotations as they were not present in the GOA file:
- GO:0004674 (protein serine/threonine kinase activity) - IDA - PMID:40281343
- GO:0110076 (negative regulation of ferroptosis) - IDA - PMID:40281343

These annotations were based on PMID:40281343 "PSAT1 impairs ferroptosis and reduces immunotherapy efficacy via GPX4 hydroxylation", which shows CaMKII phosphorylates PSAT1 at Ser337 in cancer cells, affecting ferroptosis resistance. While this is valid experimental evidence, these specific annotations with this PMID are not in the current GOA dataset and must be removed to pass validation.

The ferroptosis regulation represents a peripheral, non-neuronal function of CAMK2A discovered in cancer biology context, not central to its primary role in synaptic plasticity.