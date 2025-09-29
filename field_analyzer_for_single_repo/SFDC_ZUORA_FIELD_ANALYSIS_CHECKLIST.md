# SFDC → Zuora Field Dependency Analysis Checklist

## Overview
This checklist provides a standardized approach for analyzing SFDC custom fields synced to Zuora and their usage in downstream EDA curation pipelines.

## Analysis Steps

### 1. Field Inventory & Identification
- [ ] **Identify all SFDC custom fields** currently synced to Zuora (fields ending in `_c`)
- [ ] **Document source location** in SFDC and destination in Zuora
- [ ] **Map field transformations** in staging layer macros
- [ ] **Note field data types** and any business logic applied

### 2. Foundational Layer Dependency Analysis
- [ ] **Search staging models** (`src/models/staging/zuora/`) for field usage
- [ ] **Check foundational models** (`src/models/foundational/`) for field consumption
- [ ] **Review dimension tables** that incorporate the fields
- [ ] **Identify fact tables** that depend on the fields

### 3. Functional Layer Impact Assessment
- [ ] **Search functional models** (`src/models/functional/`) for field references
- [ ] **Identify business metrics** that depend on the fields
- [ ] **Document reporting dependencies** and dashboard usage
- [ ] **Check for derived calculations** using the fields

### 4. Business Logic & Use Case Documentation
- [ ] **Document business purpose** of each field
- [ ] **Identify downstream use cases** (reporting, analytics, compliance)
- [ ] **Assess criticality** to business operations
- [ ] **Note any field validation rules** or constraints

### 5. Technical Dependency Mapping
- [ ] **Trace field lineage** from source to consumption
- [ ] **Identify transformation logic** in macros and models
- [ ] **Document any derived fields** created from the source field
- [ ] **Check for joins** that depend on the field

### 6. Alternative Sync Assessment
- [ ] **Evaluate alternative sync methods** (batch vs real-time)
- [ ] **Assess feasibility** of alternative data sources
- [ ] **Consider data quality implications** of different sync approaches
- [ ] **Evaluate cost/complexity** of maintaining sync

### 7. Recommendations & Documentation
- [ ] **Classify fields** as Critical/Important/Optional
- [ ] **Provide sync recommendations** (Keep/Alternative/EOL)
- [ ] **Document rationale** for each recommendation
- [ ] **Identify any migration path** if sync changes are needed

## Field Categories for Analysis

### Subscription-Level Fields
Fields that modify subscription behavior or reporting:
- Contract relationships (`salesforce_contract_id_c`)
- Subscription classification (`subscription_kind_c`)
- Integration flags (`include_in_salesforce_interface_c`)
- Pricing model indicators (`model_type_c`, `price_ramp_c`)

### Product-Level Fields
Fields that define product characteristics:
- Product categorization (`product_type_c`, `product_line_c`)
- Product naming (`addon_name_c`)
- Product features (`elite_status_c`, `temporary_product_c`)
- Pricing attributes (`pricing_model_c`, `plan_type_c`)

### Financial Fields
Fields that impact revenue calculations:
- Multi-currency pricing (`annual_discounted_price_*_c`)
- Revenue recognition (`agent_months_c`, `quantityfor_term_c`)

## Tools for Analysis

### Code Search Commands
```bash
# Find all custom fields in Zuora models
grep -r "_c\b" src/models/staging/zuora/

# Search for specific field usage in functional models
grep -r "field_name" src/models/functional/

# Find all references to a field across codebase
grep -r "field_name" src/
```

### DBT Commands
```bash
# Generate lineage for specific models
dbt docs generate
dbt docs serve

# Test specific models that use the fields
dbt test --models +model_name+
```

## Output Template

For each field, document:

| Field Name | SFDC Source | Zuora Destination | Business Purpose | Foundational Usage | Functional Usage | Criticality | Recommendation |
|------------|-------------|-------------------|------------------|-------------------|------------------|-------------|----------------|
| field_name_c | Object.Field | zuora_table.field | Description | Models using it | Analytics using it | High/Med/Low | Keep/Alt/EOL |

## Validation Steps

- [ ] **Cross-reference** with business stakeholders
- [ ] **Validate** field usage with data lineage tools (Alation)
- [ ] **Test** impact of field removal on downstream models
- [ ] **Review** with Finance and RevOps teams for business context

## Common Red Flags

- Fields with **zero downstream usage** → Candidate for EOL
- Fields used only in **legacy/deprecated models** → Candidate for EOL
- Fields with **alternative data sources** available → Candidate for alternative sync
- Fields critical for **financial reporting** → Keep current sync method
- Fields used in **real-time dashboards** → Keep real-time sync
