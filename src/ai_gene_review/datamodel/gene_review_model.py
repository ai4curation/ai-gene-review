from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'gene_review',
     'default_range': 'string',
     'description': 'Schema for gene curation Top level entity is a GeneReview, '
                    'which is about a single gene (and its equivalent swiss-prot '
                    'entry). It contains a high level summary of the gene, plus a '
                    'review of all existing annotations. It also contains a list '
                    'of core functions, which are GO-CAM-like annotons describing '
                    'the core evolved functions of the gene.',
     'id': 'https://w3id.org/ai4curation/gene_review',
     'imports': ['linkml:types'],
     'name': 'gene_curation',
     'prefixes': {'dcat': {'prefix_prefix': 'dcat',
                           'prefix_reference': 'http://www.w3.org/ns/dcat#'},
                  'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'gene_review': {'prefix_prefix': 'gene_review',
                                  'prefix_reference': 'https://w3id.org/ai4curation/gene_review/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'owl': {'prefix_prefix': 'owl',
                          'prefix_reference': 'http://www.w3.org/2002/07/owl#'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'source_file': 'src/ai_gene_review/schema/gene_review.yaml'} )

class EvidenceType(str, Enum):
    IDA = "IDA"
    IBA = "IBA"
    ISS = "ISS"
    TAS = "TAS"
    IEP = "IEP"
    IGC = "IGC"


class ActionEnum(str, Enum):
    ACCEPT = "ACCEPT"
    """
    Accept the existing annotation as-is, no modifications, and retain as representing the core function of the gene
    """
    KEEP_AS_NON_CORE = "KEEP_AS_NON_CORE"
    """
    Keep the existing annotation as-is, but mark it as non-core. For pleiotropic genes, this may be the developmental processes, or other processes that are not the core function of the gene.
    """
    REMOVE = "REMOVE"
    """
    Remove the existing annotation, as it is unlikely to be correct based on combined evidence
    """
    MODIFY = "MODIFY"
    """
    The essence of the annotation is sound, but there are better terms to use (use in combination with proposed_replacement_terms). if the term is too general, then MODIFY should be used, with a proposed replacement term for the correct specific function. sometimes terms can also be overly specific and contorted, so in some cases you might want to generalize
    """
    MARK_AS_OVER_ANNOTATED = "MARK_AS_OVER_ANNOTATED"
    """
    The term is not entirely wrong, but likely represents an over-annotation of the gene
    """
    UNDECIDED = "UNDECIDED"
    """
    The annotation is not clear, and the reviewer is not sure what to do with it. ALWAYS USE THIS IF YOU ARE UNABLE TO ACCESS RELEVANT PUBLICATIONS
    """
    PENDING = "PENDING"
    """
    The review entry is a stub, and the review has not been completed yet.
    """



class GeneReview(ConfiguredBaseModel):
    """
    Complete review for a gene
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/gene_review', 'tree_root': True})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['GeneReview', 'Term', 'Reference']} })
    gene_symbol: str = Field(default=..., description="""Symbol of the gene""", json_schema_extra = { "linkml_meta": {'alias': 'gene_symbol', 'domain_of': ['GeneReview']} })
    aliases: Optional[list[str]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'aliases', 'domain_of': ['GeneReview']} })
    description: Optional[str] = Field(default=None, description="""Description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['GeneReview', 'Term', 'CoreFunction']} })
    taxon: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'taxon', 'domain_of': ['GeneReview']} })
    references: Optional[list[Reference]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'references', 'domain_of': ['GeneReview']} })
    existing_annotations: Optional[list[ExistingAnnotation]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'existing_annotations', 'domain_of': ['GeneReview']} })
    core_functions: Optional[list[CoreFunction]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'core_functions', 'domain_of': ['GeneReview']} })


class Term(ConfiguredBaseModel):
    """
    A term in a specific ontology
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/gene_review'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['GeneReview', 'Term', 'Reference']} })
    label: str = Field(default=..., description="""Human readable name of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'label', 'domain_of': ['Term']} })
    description: Optional[str] = Field(default=None, description="""Description of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['GeneReview', 'Term', 'CoreFunction']} })
    ontology: Optional[str] = Field(default=None, description="""Ontology of the term. E.g `go`, `cl`, `hp`""", json_schema_extra = { "linkml_meta": {'alias': 'ontology', 'domain_of': ['Term']} })


class Reference(ConfiguredBaseModel):
    """
    A reference is a published text  that describes a finding or a method. References might be formal publications (where the ID is a PMID), or for methods, a GO_REF. Additionally, a reference to a local ad-hoc analysis or review can be made by using the `file:` prefix.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/gene_review'})

    id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'id', 'domain_of': ['GeneReview', 'Term', 'Reference']} })
    title: str = Field(default=..., description="""Title of the entity""", json_schema_extra = { "linkml_meta": {'alias': 'title', 'domain_of': ['Reference'], 'slot_uri': 'dcterms:title'} })
    findings: Optional[list[Finding]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'findings', 'domain_of': ['Reference']} })
    is_invalid: Optional[bool] = Field(default=None, description="""Whether the reference is invalid (e.g., retracted or replaced)""", json_schema_extra = { "linkml_meta": {'alias': 'is_invalid', 'domain_of': ['Reference']} })


class Finding(ConfiguredBaseModel):
    """
    A finding is a statement about a gene, which is supported by a reference. Similar to \"comments\" in uniprot
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/gene_review'})

    statement: Optional[str] = Field(default=None, description="""Concise statement describing an aspect of the gene""", json_schema_extra = { "linkml_meta": {'alias': 'statement', 'domain_of': ['Finding']} })
    supporting_text: Optional[str] = Field(default=None, description="""Supporting text from the publication. Can be interleaved text if there are multiple lines of evidence. Can also be annotated""", json_schema_extra = { "linkml_meta": {'alias': 'supporting_text', 'domain_of': ['Finding', 'Review']} })


class ExistingAnnotation(ConfiguredBaseModel):
    """
    An existing annotation from the GO database, plus a review of the annotation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/gene_review'})

    term: Optional[Term] = Field(default=None, description="""Term to be annotated""", json_schema_extra = { "linkml_meta": {'alias': 'term', 'domain_of': ['ExistingAnnotation', 'AnnotationExtension']} })
    extensions: Optional[list[AnnotationExtension]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'extensions', 'domain_of': ['ExistingAnnotation']} })
    negated: Optional[bool] = Field(default=None, description="""Whether the term is negated""", json_schema_extra = { "linkml_meta": {'alias': 'negated', 'domain_of': ['ExistingAnnotation']} })
    evidence_type: Optional[str] = Field(default=None, description="""Evidence code (e.g., IDA, IBA, ISS, TAS)""", json_schema_extra = { "linkml_meta": {'alias': 'evidence_type', 'domain_of': ['ExistingAnnotation']} })
    original_reference_id: Optional[str] = Field(default=None, description="""ID of the original reference""", json_schema_extra = { "linkml_meta": {'alias': 'original_reference_id', 'domain_of': ['ExistingAnnotation']} })
    supporting_entities: Optional[list[str]] = Field(default=None, description="""IDs of the supporting entities""", json_schema_extra = { "linkml_meta": {'alias': 'supporting_entities', 'domain_of': ['ExistingAnnotation']} })
    review: Optional[Review] = Field(default=None, description="""Review of the gene""", json_schema_extra = { "linkml_meta": {'alias': 'review', 'domain_of': ['ExistingAnnotation'], 'recommended': True} })


class Review(ConfiguredBaseModel):
    """
    A review of an existing annotation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/gene_review'})

    summary: Optional[str] = Field(default=None, description="""Summary of the review""", json_schema_extra = { "linkml_meta": {'alias': 'summary', 'domain_of': ['Review']} })
    action: Optional[ActionEnum] = Field(default=None, description="""Action to be taken""", json_schema_extra = { "linkml_meta": {'alias': 'action', 'domain_of': ['Review']} })
    reason: Optional[str] = Field(default=None, description="""Reason for the action""", json_schema_extra = { "linkml_meta": {'alias': 'reason', 'domain_of': ['Review']} })
    proposed_replacement_terms: Optional[list[Term]] = Field(default=None, description="""Proposed replacement terms""", json_schema_extra = { "linkml_meta": {'alias': 'proposed_replacement_terms', 'domain_of': ['Review']} })
    additional_reference_ids: Optional[list[str]] = Field(default=None, description="""IDs of the references""", json_schema_extra = { "linkml_meta": {'alias': 'additional_reference_ids', 'domain_of': ['Review']} })
    supporting_text: Optional[str] = Field(default=None, description="""Supporting text from the publication. Can be interleaved text if there are multiple lines of evidence. Can also be annotated""", json_schema_extra = { "linkml_meta": {'alias': 'supporting_text', 'domain_of': ['Finding', 'Review']} })


class CoreFunction(ConfiguredBaseModel):
    """
    A core function is a GO-CAM-like annotation of the core evolved functions of a gene. This is a synthesis of the reviewed core annotations, brought together into a unified GO-CAM-like representation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/gene_review'})

    description: Optional[str] = Field(default=None, description="""Description of the core function""", json_schema_extra = { "linkml_meta": {'alias': 'description', 'domain_of': ['GeneReview', 'Term', 'CoreFunction']} })
    molecular_function: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'molecular_function', 'domain_of': ['CoreFunction']} })
    directly_involved_in: Optional[list[Term]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'directly_involved_in', 'domain_of': ['CoreFunction']} })
    locations: Optional[list[Term]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'locations', 'domain_of': ['CoreFunction']} })
    anatomical_locations: Optional[list[Term]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'anatomical_locations', 'domain_of': ['CoreFunction']} })
    substrates: Optional[list[Term]] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'substrates', 'domain_of': ['CoreFunction']} })
    in_complex: Optional[Term] = Field(default=None, json_schema_extra = { "linkml_meta": {'alias': 'in_complex', 'domain_of': ['CoreFunction']} })


class AnnotationExtension(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4curation/gene_review'})

    predicate: Optional[str] = Field(default=None, description="""Predicate of the extension""", json_schema_extra = { "linkml_meta": {'alias': 'predicate', 'domain_of': ['AnnotationExtension']} })
    term: Optional[Term] = Field(default=None, description="""Term to be annotated""", json_schema_extra = { "linkml_meta": {'alias': 'term', 'domain_of': ['ExistingAnnotation', 'AnnotationExtension']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
GeneReview.model_rebuild()
Term.model_rebuild()
Reference.model_rebuild()
Finding.model_rebuild()
ExistingAnnotation.model_rebuild()
Review.model_rebuild()
CoreFunction.model_rebuild()
AnnotationExtension.model_rebuild()

