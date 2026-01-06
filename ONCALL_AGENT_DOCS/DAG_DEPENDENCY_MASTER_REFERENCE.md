# DAG Interdependency Master Reference

---

## 🚨 CRITICAL: CONSENT REQUIRED FOR ALL CHANGES

> **⚠️ IMPORTANT INSTRUCTIONS FOR AI ASSISTANT:**
> 
> 1. **NEVER commit changes to this MD file** without explicit user approval. Always ask:
>    ```
>    "ARE YOU SURE YOU WANT TO COMMIT THESE CHANGES IN MD FILE?"
>    ```
> 
> 2. **NO CODE CHANGES IN ANY REPOSITORIES WITHOUT CONSENT** - Always present proposed changes and wait for user approval before making any modifications to code files.
> 
> 3. When suggesting changes, **show the proposed changes first** and wait for explicit confirmation before executing.

---

## 🔄 MANDATORY: SYNC REPOSITORIES BEFORE ANALYSIS

> **⚠️ AUTOMATIC PRE-ANALYSIS STEP:**
> 
> Before analyzing ANY DAG failure, the AI assistant MUST automatically run the following command 
> on ALL affected/referenced repositories to ensure they are up-to-date with main branch:
> 
> ```bash
> cd /Users/chaitanya.makashir/cursor_all_repos/<REPO_NAME> && git checkout main && git pull origin main
> ```
> 
> **This step is MANDATORY and must be executed EVERY TIME without fail before starting analysis.**
> 
> **Repositories to sync based on failed DAG:**
> | Repository | When to Sync |
> |------------|--------------|
> | `zdp_dbt_scd2_fivetran` | SCD2 layer DAGs |
> | `zdp_dbt_cleansed_salesforce` | Cleansed Salesforce DAGs |
> | `zdp_dbt_cleansed_xactly` | Cleansed Xactly DAGs |
> | `zdp_dbt_customer` | Customer domain DAGs |
> | `zdp_dbt_finance` | Finance domain DAGs |
> | `zdp_dbt_data_delivery_service` | DDS layer DAGs |
> | `zdp_dbt_enterprise_data_ml` | ML/Enterprise data DAGs |

---

## 📋 Purpose
This document provides a **COMPLETE** dependency map for all DAGs across all ZDP repositories. Use this to identify downstream impacts when a DAG fails.

## 🔗 Related Documentation
- **[RUNBOOK_INTEGRATION.md](RUNBOOK_INTEGRATION.md)** - Dynamic runbook fetching from Confluence (owners, contacts, troubleshooting)
- **This file** - Downstream dependency analysis and impact chains

## 🎯 How to Use
1. Find your DAG name in the **Quick Lookup Table** below
2. Check the "Total Downstream Impact" column for the number of affected DAGs
3. Refer to the detailed section for that DAG to see the complete cascading impact chain
4. Review the **Critical Impact Chains** section for visualization of major failure scenarios
5. **For owner/contact info:** The AI will automatically fetch from Confluence runbooks (see [RUNBOOK_INTEGRATION.md](RUNBOOK_INTEGRATION.md))

---

## 📊 Quick Lookup Table

| DAG Name | Direct Triggers | ExternalTaskSensor Waiters | Data Dependencies | Total Downstream Impact | Severity |
|----------|----------------|---------------------------|-------------------|------------------------|----------|
| **SCD2 Fivetran Layer** |||||
| `dbt_scd2_fivetran_salesforce` | 1 DAG | 1 DAG | Extensive | **18+ DAGs** | 🔴 CATASTROPHIC |
| `dbt_scd2_fivetran_salesforce_master` | 3 DAGs | 0 | Via children | **18+ DAGs** | 🔴 CATASTROPHIC |
| `dbt_scd2_fivetran_salesforce_incr_all` | 0 | 0 | 0 | **0 DAGs** | 🟢 NONE |
| `dbt_scd2_fivetran_salesforce_full_ff` | 0 | 0 | 0 | **0 DAGs** | 🟢 NONE |
| `dbt_scd2_fivetran_zuora` | 1 DAG | 1 DAG | Medium | **8+ DAGs** | 🟠 HIGH |
| `dbt_scd2_fivetran_xactly` | 1 DAG | 0 | Low | **2 DAGs** | 🟡 MEDIUM |
| `dbt_scd2_fivetran_gainsight` | 1 DAG | 0 | Low | **1-2 DAGs** | 🟡 MEDIUM |
| `dbt_scd2_fivetran_marketo` | 1 DAG | 0 | Low | **1-2 DAGs** | 🟡 MEDIUM |
| `dbt_scd2_fivetran_workday` | 1 DAG | 0 | Low | **2 DAGs** | 🟡 MEDIUM |
| `zdp_dbt_scd2_fivetran_gsheets_finance` | 1 DAG | 0 | Medium | **4+ DAGs** | 🟠 HIGH |
| **Cleansed Layer** |||||
| `dbt_cleansed_salesforce` | 0 | 0 | Extensive | **17+ DAGs** | 🔴 CATASTROPHIC |
| `dbt_cleansed_xactly` | 0 | 0 | Low | **1 DAG** | 🟡 MEDIUM |
| **Foundational Layer** |||||
| `zdp_dbt_customer_foundational` | 2 DAGs | 0 | Extensive | **15+ DAGs** | 🔴 CATASTROPHIC |
| `zdp_dbt_customer_financial_bookings` | 1 DAG | 0 | Medium | **2 DAGs** | 🟠 HIGH |
| `zdp_dbt_sales_productivity_attainment` | 0 | 0 | 0 | **0 DAGs** | 🟢 NONE |
| `zdp_dbt_customer_functional` | 0 | 0 | 0 | **0 DAGs** | 🟢 NONE |
| **Finance Layer** |||||
| `zdp_dbt_finance_foundational` | 3 DAGs | 0 | High | **9+ DAGs** | 🔴 CRITICAL |
| `zdp_dbt_finance_functional` | 1 DAG | 0 | Low | **1 DAG** | 🟡 MEDIUM |
| `zdp_dbt_finance_agent_months` | 0 | 0 | 0 | **0 DAGs** | 🟢 NONE |
| `zdp_dbt_finance_foundational_freezing` | 0 | 0 | 0 | **0 DAGs** | 🟢 NONE |
| `zdp_dbt_finance_functional_freezing` | 0 | 0 | 0 | **0 DAGs** | 🟢 NONE |
| **Data Delivery Service Layer** |||||
| `zdp_dbt_dds_aep` | 0 | 0 | 0 | **0 DAGs** | 🟢 NONE |
| `zdp_dbt_dds_gainsight` | 0 | 0 | 0 | **0 DAGs** | 🟢 NONE |
| `zdp_dbt_dds_marketo` | 0 | 0 | 0 | **0 DAGs** | 🟢 NONE |
| `zdp_dbt_dds_salesforce` | 0 | 0 | 0 | **0 DAGs** | 🟢 NONE |
| `zdp_dbt_dds_self_service_opportunity` | 0 | 0 | 0 | **0 DAGs** | 🟢 NONE |
| `zdp_dbt_dds_z2` | 0 | 0 | 0 | **0 DAGs** | 🟢 NONE |

---

## 🔍 Complete Dependency Map

### 🔴 CATASTROPHIC IMPACT DAGS

---

#### `dbt_scd2_fivetran_salesforce`

**Repository:** `zdp_dbt_scd2_fivetran`  
**Schedule:** Triggered manually or by parent  
**Criticality:** 🔴 **CATASTROPHIC** - Impacts 18+ downstream DAGs across multiple domains

**Direct Airflow Dependencies:**
- ✅ **Triggers:** `dbt_cleansed_salesforce`

**ExternalTaskSensor Dependencies:**
- ⏳ **Waited for by:** `zdp_dbt_customer_foundational` (via `get_scd2_fivetran_salesforce_task_sensor()`)

**Data Dependencies (Source Freshness & dbt Models):**
- 📊 **Writes to:** `scd2.salesforce` schema
- 📊 **Read by:**
  - `dbt_cleansed_salesforce` → produces `cleansed.salesforce`
  - `zdp_dbt_customer_foundational` → checks freshness + reads cleansed data
  - `zdp_dbt_finance_foundational` → checks freshness on `cleansed.salesforce.contract`, `cleansed.salesforce.sbqq_quote_c`
  - `zdp_dbt_finance_functional` → checks freshness on `cleansed.salesforce.contract_bcv`, `cleansed.salesforce.sbqq_quote_c_bcv`
  - `zdp_dbt_dds_salesforce` → reads from `cleansed.salesforce` schema
  - `zdp_dbt_dds_self_service_opportunity` → reads from `cleansed.salesforce` schema

**Cascading Impact Chain:**

```
dbt_scd2_fivetran_salesforce FAILS
    ↓
Level 1 (Direct Trigger - BLOCKED):
    └─→ dbt_cleansed_salesforce ❌ BLOCKED
         ↓
Level 2 (ExternalTaskSensor Wait + Source Freshness Checks - BLOCKED):
    ├─→ zdp_dbt_customer_foundational ❌ BLOCKED (waits via sensor + has source_freshness test for cleansed.salesforce)
    ├─→ zdp_dbt_finance_foundational ❌ BLOCKED (has source_freshness test for cleansed.salesforce tables)
    ├─→ zdp_dbt_finance_functional ❌ BLOCKED (has source_freshness test for contract_bcv, sbqq_quote_c_bcv)
    ├─→ zdp_dbt_dds_self_service_opportunity ❌ BLOCKED (has source_freshness test for cleansed data)
    └─→ zdp_dbt_dds_salesforce ⚠️ RUNS WITH STALE DATA (no source_freshness test)
         ↓
Level 3 (Triggered by customer_foundational - BLOCKED):
    ├─→ zdp_dbt_customer_financial_bookings ❌ BLOCKED (parent blocked)
    └─→ zdp_dbt_customer_functional ❌ BLOCKED (parent blocked)
         ↓
Level 4 (Triggered by customer_financial_bookings - BLOCKED):
    └─→ zdp_dbt_sales_productivity_attainment ❌ BLOCKED (parent blocked)
         ↓
Level 5 (Triggered by finance_foundational - BLOCKED):
    ├─→ zdp_dbt_finance_agent_months ❌ BLOCKED (parent blocked)
    ├─→ zdp_dbt_finance_foundational_freezing ❌ BLOCKED (parent blocked)
    └─→ zdp_dbt_finance_functional ❌ ALREADY BLOCKED (see Level 2)
         ↓
Level 6 (Triggered by finance_functional - BLOCKED):
    └─→ zdp_dbt_finance_functional_freezing ❌ BLOCKED (parent blocked)
         ↓
Level 7 (Data Dependencies - STALE DATA - No Source Freshness Tests):
    ├─→ zdp_dbt_dds_aep ⚠️ RUNS WITH STALE DATA (no source_freshness test - reads stale foundational data)
    ├─→ zdp_dbt_dds_z2 ⚠️ RUNS WITH STALE DATA (no source_freshness test - reads stale foundational data)
    ├─→ zdp_dbt_dds_gainsight ⚠️ RUNS WITH STALE DATA (no source_freshness test - reads stale foundational data)
    └─→ zdp_dbt_dds_marketo ⚠️ RUNS WITH STALE DATA (no source_freshness test - reads stale foundational data)
```

**Total Impact:** 🔴 **18 DAGs** - 11 BLOCKED (have source_freshness tests), 4 with STALE DATA (no source_freshness tests)

---

#### `dbt_scd2_fivetran_salesforce_master`

**Repository:** `zdp_dbt_scd2_fivetran`  
**Schedule:** Scheduled (time-based)  
**Criticality:** 🔴 **CATASTROPHIC** - Master orchestrator for Salesforce pipeline

**Direct Airflow Dependencies:**
- ✅ **Triggers:**
  - `zdp_dbt_scd2_fivetran_salesforce_incr_all`
  - `zdp_dbt_scd2_fivetran_salesforce_full_ff`
  - `zdp_dbt_cleansed_salesforce_incr_all` (possibly a typo or legacy DAG)

**Cascading Impact:**
- Same as `dbt_scd2_fivetran_salesforce` since it triggers the salesforce processing

**Total Impact:** 🔴 **18+ DAGs** (via triggered children)

---

#### `dbt_cleansed_salesforce`

**Repository:** `zdp_dbt_cleansed_salesforce`  
**Schedule:** `None` (triggered by `dbt_scd2_fivetran_salesforce`)  
**Criticality:** 🔴 **CATASTROPHIC** - Core cleansed layer for Salesforce data

**Direct Airflow Dependencies:**
- ✅ **Triggered by:** `dbt_scd2_fivetran_salesforce`
- ✅ **Triggers:** None

**ExternalTaskSensor Dependencies:**
- ⏳ **Waited for by:** `zdp_dbt_customer_foundational` (via `get_salesforce_cleansed_task_sensor()`)

**Data Dependencies:**
- 📊 **Writes to:** `cleansed.salesforce` schema
- 📊 **Read by:**
  - `zdp_dbt_customer_foundational` → critical dependency
  - `zdp_dbt_finance_foundational` → critical dependency
  - `zdp_dbt_finance_functional` → critical dependency
  - `zdp_dbt_dds_salesforce` → critical dependency
  - `zdp_dbt_dds_self_service_opportunity` → critical dependency

**Cascading Impact:**
- Same as Level 2+ of `dbt_scd2_fivetran_salesforce` (all downstream DAGs affected identically)

**Total Impact:** 🔴 **17 DAGs** - 10 BLOCKED (have source_freshness tests), 4 with STALE DATA (no source_freshness tests)

---

#### `zdp_dbt_customer_foundational`

**Repository:** `zdp_dbt_customer`  
**Schedule:** `0 7 * * *` (Daily at 7 AM UTC)  
**Criticality:** 🔴 **CATASTROPHIC** - Core foundational customer data

**Direct Airflow Dependencies:**
- ✅ **Triggers:**
  - `zdp_dbt_customer_financial_bookings`
  - `zdp_dbt_customer_functional`

**ExternalTaskSensor Dependencies:**
- ⏳ **Waits for:**
  - `dbt_scd2_fivetran_salesforce` (via sensor)
  - `dbt_cleansed_salesforce` (via sensor)
  - `dbt_scd2_fivetran_zuora` (via sensor)
  - `dbt_cleansed_zuora` (via sensor)

**Data Dependencies (Source Freshness Checks):**
- 📊 **Reads from:**
  - `cleansed.salesforce` schema
  - `cleansed.zuora` schema
  - `cleansed.workday` schema
- 📊 **Writes to:** `foundational.customer` schema
- 📊 **Read by:**
  - `zdp_dbt_finance_foundational` → checks freshness + reads data
  - `zdp_dbt_finance_foundational_freezing` → checks freshness
  - `zdp_dbt_dds_aep` → reads foundational.customer
  - `zdp_dbt_dds_z2` → reads foundational.customer
  - `zdp_dbt_dds_gainsight` → reads foundational.customer
  - `zdp_dbt_dds_salesforce` → reads foundational.customer
  - `zdp_dbt_dds_self_service_opportunity` → reads foundational.customer

**Cascading Impact:**
```
zdp_dbt_customer_foundational FAILS
    ↓
Level 1 (Direct Triggers - BLOCKED):
    ├─→ zdp_dbt_customer_financial_bookings ❌ BLOCKED
    └─→ zdp_dbt_customer_functional ❌ BLOCKED
         ↓
Level 2 (Triggered by financial_bookings - BLOCKED):
    └─→ zdp_dbt_sales_productivity_attainment ❌ BLOCKED
         ↓
Level 3 (Data Dependencies with Source Freshness Tests - BLOCKED):
    ├─→ zdp_dbt_finance_foundational ❌ BLOCKED (has source_freshness test for foundational.customer)
    ├─→ zdp_dbt_finance_foundational_freezing ❌ BLOCKED (has source_freshness test for customer data)
    ├─→ zdp_dbt_dds_self_service_opportunity ❌ BLOCKED (has source_freshness test for foundational data)
    │
    └─→ STALE DATA (No Source Freshness Tests):
        ├─→ zdp_dbt_dds_aep ⚠️ RUNS WITH STALE DATA (no source_freshness test)
        ├─→ zdp_dbt_dds_z2 ⚠️ RUNS WITH STALE DATA (no source_freshness test)
        ├─→ zdp_dbt_dds_gainsight ⚠️ RUNS WITH STALE DATA (no source_freshness test)
        └─→ zdp_dbt_dds_salesforce ⚠️ RUNS WITH STALE DATA (no source_freshness test)
         ↓
Level 4 (Triggered by finance_foundational - BLOCKED):
    ├─→ zdp_dbt_finance_agent_months ❌ BLOCKED (parent blocked)
    ├─→ zdp_dbt_finance_functional ❌ BLOCKED (parent blocked)
    └─→ zdp_dbt_finance_foundational_freezing ❌ ALREADY BLOCKED (see Level 3)
         ↓
Level 5 (Triggered by finance_functional - BLOCKED):
    └─→ zdp_dbt_finance_functional_freezing ❌ BLOCKED (parent blocked)
         ↓
Level 6 (Data Dependencies - STALE DATA):
    └─→ zdp_dbt_dds_marketo ⚠️ RUNS WITH STALE DATA (no source_freshness test - reads stale foundational.finance)
```

**Total Impact:** 🔴 **15 DAGs** - 9 BLOCKED (have source_freshness tests or parent blocked), 5 with STALE DATA (no source_freshness tests)

---

#### `zdp_dbt_finance_foundational`

**Repository:** `zdp_dbt_finance`  
**Schedule:** `0 10 * * *` (Daily at 10 AM UTC)  
**Criticality:** 🔴 **CRITICAL** - Core foundational finance data

**Direct Airflow Dependencies:**
- ✅ **Triggers:**
  - `zdp_dbt_finance_functional`
  - `zdp_dbt_finance_foundational_freezing`
  - `zdp_dbt_finance_agent_months`

**Data Dependencies (Source Freshness Checks):**
- 📊 **Reads from:**
  - `cleansed.salesforce` schema (contract, sbqq_quote_c tables)
  - `foundational.customer` schema (billing accounts, crm accounts, entity_mapping, recurring_revenue tables)
  - `cleansed.gsheet_finance` schema
- 📊 **Writes to:** `foundational.finance`, `foundational.finance_internal` schemas
- 📊 **Read by:**
  - `zdp_dbt_dds_aep` → reads foundational.finance
  - `zdp_dbt_dds_z2` → reads foundational.finance
  - `zdp_dbt_dds_gainsight` → reads foundational.finance
  - `zdp_dbt_dds_marketo` → reads foundational.finance
  - `zdp_dbt_dds_self_service_opportunity` → reads foundational.finance

**Cascading Impact:**
```
zdp_dbt_finance_foundational FAILS
    ↓
Level 1 (Direct Triggers - BLOCKED):
    ├─→ zdp_dbt_finance_functional ❌ BLOCKED
    ├─→ zdp_dbt_finance_foundational_freezing ❌ BLOCKED
    └─→ zdp_dbt_finance_agent_months ❌ BLOCKED
         ↓
Level 2 (Triggered by finance_functional - BLOCKED):
    └─→ zdp_dbt_finance_functional_freezing ❌ BLOCKED
         ↓
Level 3 (Data Dependencies):
    ├─→ zdp_dbt_dds_self_service_opportunity ❌ BLOCKED (has source_freshness test for foundational.finance)
    │
    └─→ STALE DATA (No Source Freshness Tests):
        ├─→ zdp_dbt_dds_aep ⚠️ RUNS WITH STALE DATA (no source_freshness test)
        ├─→ zdp_dbt_dds_z2 ⚠️ RUNS WITH STALE DATA (no source_freshness test)
        ├─→ zdp_dbt_dds_gainsight ⚠️ RUNS WITH STALE DATA (no source_freshness test)
        └─→ zdp_dbt_dds_marketo ⚠️ RUNS WITH STALE DATA (no source_freshness test)
```

**Total Impact:** 🔴 **9 DAGs** - 5 BLOCKED (parent blocked or have source_freshness test), 4 with STALE DATA (no source_freshness tests)

---

### 🟠 HIGH IMPACT DAGS

---

#### `dbt_scd2_fivetran_zuora`

**Repository:** `zdp_dbt_scd2_fivetran`  
**Schedule:** Scheduled (time-based)  
**Criticality:** 🟠 **HIGH** - Critical billing data source

**Direct Airflow Dependencies:**
- ✅ **Triggers:** `dbt_cleansed_zuora`

**ExternalTaskSensor Dependencies:**
- ⏳ **Waited for by:** `zdp_dbt_customer_foundational` (via `get_scd2_fivetran_zuora_task_sensor()`)

**Data Dependencies:**
- 📊 **Writes to:** `scd2.zuora` schema
- 📊 **Read by:**
  - `dbt_cleansed_zuora` → produces `cleansed.zuora`
  - `zdp_dbt_customer_foundational` → checks freshness + reads data
  - `zdp_dbt_finance_foundational` → checks freshness on zuora tables

**Cascading Impact:**
```
dbt_scd2_fivetran_zuora FAILS
    ↓
Level 1 (Direct Trigger - BLOCKED):
    └─→ dbt_cleansed_zuora ❌ BLOCKED
         ↓
Level 2 (ExternalTaskSensor Wait + Source Freshness Tests - BLOCKED):
    ├─→ zdp_dbt_customer_foundational ❌ BLOCKED (waits via sensor + has source_freshness test for cleansed.zuora)
    └─→ zdp_dbt_finance_foundational ❌ BLOCKED (has source_freshness test for cleansed.zuora)
         ↓
Level 3+ (Same cascading impact as customer_foundational failure)
    └─→ [15+ additional DAGs affected - see customer_foundational impact chain]
```

**Total Impact:** 🟠 **17+ DAGs** - 11+ BLOCKED (have source_freshness tests), 5 with STALE DATA (no source_freshness tests)

---

#### `zdp_dbt_customer_financial_bookings`

**Repository:** `zdp_dbt_customer`  
**Schedule:** Triggered by `zdp_dbt_customer_foundational`  
**Criticality:** 🟠 **HIGH** - Financial bookings data

**Direct Airflow Dependencies:**
- ✅ **Triggered by:** `zdp_dbt_customer_foundational`
- ✅ **Triggers:** `zdp_dbt_sales_productivity_attainment`

**Data Dependencies:**
- 📊 **Writes to:** `foundational.customer` schema (bookings tables)
- 📊 **Read by:**
  - `zdp_dbt_sales_productivity_attainment`

**Cascading Impact:**
```
zdp_dbt_customer_financial_bookings FAILS
    ↓
Level 1 (Direct Trigger - BLOCKED):
    └─→ zdp_dbt_sales_productivity_attainment ❌ BLOCKED
```

**Total Impact:** 🟠 **2 DAGs** (including self)

---

#### `zdp_dbt_scd2_fivetran_gsheets_finance`

**Repository:** `zdp_dbt_scd2_fivetran`  
**Schedule:** Scheduled (time-based)  
**Criticality:** 🟠 **HIGH** - Finance manual adjustments

**Direct Airflow Dependencies:**
- ✅ **Triggers:** `zdp_dbt_cleansed_gsheet_finance`

**Data Dependencies:**
- 📊 **Writes to:** `scd2.gsheet_finance` schema
- 📊 **Read by:**
  - `dbt_cleansed_gsheet_finance` → produces `cleansed.gsheet_finance`
  - `zdp_dbt_finance_foundational` → checks freshness on `cleansed.gsheet_finance.gsheet_hob_manual_adjustment_scd2`

**Cascading Impact:**
```
zdp_dbt_scd2_fivetran_gsheets_finance FAILS
    ↓
Level 1 (Direct Trigger - BLOCKED):
    └─→ dbt_cleansed_gsheet_finance ❌ FAILS
         ↓
Level 2 (Data Dependencies - STALE DATA):
    └─→ zdp_dbt_finance_foundational ⚠️ RUNS WITH STALE DATA
         ↓
Level 3+ (Cascading from finance_foundational)
    └─→ [9+ additional DAGs affected - see finance_foundational impact chain]
```

**Total Impact:** 🟠 **4+ DAGs** - 1 BLOCKED, 3+ with STALE DATA

---

### 🟡 MEDIUM IMPACT DAGS

---

#### `dbt_scd2_fivetran_xactly`

**Repository:** `zdp_dbt_scd2_fivetran`  
**Schedule:** Scheduled (time-based)  
**Criticality:** 🟡 **MEDIUM** - Sales commission data

**Direct Airflow Dependencies:**
- ✅ **Triggers:** `dbt_cleansed_xactly`

**Data Dependencies:**
- 📊 **Writes to:** `scd2.xactly` schema
- 📊 **Read by:**
  - `dbt_cleansed_xactly` → produces `cleansed.xactly`
  - `zdp_dbt_sales_productivity_attainment` → checks freshness + reads from `cleansed.xactly`

**Cascading Impact:**
```
dbt_scd2_fivetran_xactly FAILS
    ↓
Level 1 (Direct Trigger - BLOCKED):
    └─→ dbt_cleansed_xactly ❌ BLOCKED
         ↓
Level 2 (Source Freshness Test - BLOCKED):
    └─→ zdp_dbt_sales_productivity_attainment ❌ BLOCKED (has source_freshness test for cleansed.xactly)
```

**Total Impact:** 🟡 **2 DAGs** - 2 BLOCKED (both have source_freshness tests or triggered)

---

#### `dbt_cleansed_xactly`

**Repository:** `zdp_dbt_cleansed_xactly`  
**Schedule:** `None` (triggered by `dbt_scd2_fivetran_xactly`)  
**Criticality:** 🟡 **MEDIUM** - Cleansed sales commission data

**Direct Airflow Dependencies:**
- ✅ **Triggered by:** `dbt_scd2_fivetran_xactly`
- ✅ **Triggers:** None

**Data Dependencies:**
- 📊 **Writes to:** `cleansed.xactly` schema
- 📊 **Read by:**
  - `zdp_dbt_sales_productivity_attainment` → critical dependency

**Cascading Impact:**
```
dbt_cleansed_xactly FAILS
    ↓
Level 1 (Source Freshness Test - BLOCKED):
    └─→ zdp_dbt_sales_productivity_attainment ❌ BLOCKED (has source_freshness test for cleansed.xactly)
```

**Total Impact:** 🟡 **1 DAG** - 1 BLOCKED (has source_freshness test)

---

#### `zdp_dbt_finance_functional`

**Repository:** `zdp_dbt_finance`  
**Schedule:** Triggered by `zdp_dbt_finance_foundational`  
**Criticality:** 🟡 **MEDIUM** - Functional finance models

**Direct Airflow Dependencies:**
- ✅ **Triggered by:** `zdp_dbt_finance_foundational`
- ✅ **Triggers:** `zdp_dbt_finance_functional_freezing`

**Data Dependencies:**
- 📊 **Reads from:** `cleansed.salesforce` (contract_bcv, sbqq_quote_c_bcv)
- 📊 **Writes to:** `functional.finance` schema

**Cascading Impact:**
```
zdp_dbt_finance_functional FAILS
    ↓
Level 1 (Direct Trigger - BLOCKED):
    └─→ zdp_dbt_finance_functional_freezing ❌ BLOCKED
```

**Total Impact:** 🟡 **1 DAG**

---

#### `dbt_scd2_fivetran_gainsight`

**Repository:** `zdp_dbt_scd2_fivetran`  
**Schedule:** Scheduled (time-based)  
**Criticality:** 🟡 **MEDIUM** - Customer success data

**Direct Airflow Dependencies:**
- ✅ **Triggers:** `dbt_cleansed_gainsight`

**Data Dependencies:**
- 📊 **Writes to:** `scd2.gainsight` schema
- 📊 **Read by:** `dbt_cleansed_gainsight` → produces `cleansed.gainsight`

**Total Impact:** 🟡 **1-2 DAGs**

---

#### `dbt_scd2_fivetran_marketo`

**Repository:** `zdp_dbt_scd2_fivetran`  
**Schedule:** Scheduled (time-based)  
**Criticality:** 🟡 **MEDIUM** - Marketing data

**Direct Airflow Dependencies:**
- ✅ **Triggers:** `dbt_cleansed_marketo`

**Data Dependencies:**
- 📊 **Writes to:** `scd2.marketo` schema
- 📊 **Read by:** `dbt_cleansed_marketo` → produces `cleansed.marketo`

**Total Impact:** 🟡 **1-2 DAGs**

---

#### `dbt_scd2_fivetran_workday`

**Repository:** `zdp_dbt_scd2_fivetran`  
**Schedule:** Scheduled (time-based)  
**Criticality:** 🟡 **MEDIUM** - HR data

**Direct Airflow Dependencies:**
- ✅ **Triggers:** `dbt_cleansed_workday`

**Data Dependencies:**
- 📊 **Writes to:** `scd2.workday` schema
- 📊 **Read by:**
  - `dbt_cleansed_workday` → produces `cleansed.workday`
  - `zdp_dbt_customer_foundational` → checks freshness on `cleansed.workday`

**Cascading Impact:**
```
dbt_scd2_fivetran_workday FAILS
    ↓
Level 1 (Direct Trigger - BLOCKED):
    └─→ dbt_cleansed_workday ❌ BLOCKED
         ↓
Level 2 (Source Freshness Test - BLOCKED):
    └─→ zdp_dbt_customer_foundational ❌ BLOCKED (has source_freshness test for cleansed.workday)
         ↓
Level 3+ (Same cascading impact as customer_foundational failure)
    └─→ [15+ additional DAGs affected - see customer_foundational impact chain]
```

**Total Impact:** 🟡 **17+ DAGs** - 11+ BLOCKED, 5 with STALE DATA

---

### 🟢 NO/LOW IMPACT DAGS (Terminal Nodes)

The following DAGs have **NO downstream dependencies** and will not cause cascading failures:

#### Functional/Terminal DAGs:
- `zdp_dbt_customer_functional`
- `zdp_dbt_sales_productivity_attainment`
- `zdp_dbt_finance_agent_months`
- `zdp_dbt_finance_foundational_freezing`
- `zdp_dbt_finance_functional_freezing`

#### Data Delivery Service (Terminal Presentation Layer):
- `zdp_dbt_dds_aep`
- `zdp_dbt_dds_gainsight`
- `zdp_dbt_dds_marketo`
- `zdp_dbt_dds_salesforce`
- `zdp_dbt_dds_self_service_opportunity`
- `zdp_dbt_dds_z2`

#### Salesforce Sub-DAGs (Internal Processing):
- `dbt_scd2_fivetran_salesforce_incr_all`
- `dbt_scd2_fivetran_salesforce_full_ff`
- `dbt_scd2_fivetran_salesforce_hourly`

#### Adhoc/Maintenance DAGs:
- All `*_adhoc` DAGs
- All `*_seed` DAGs
- All `*_full_refresh` DAGs

---

## 🔗 Dependency Types Explained

### 1. **Direct Airflow Trigger** (`TriggerDagRunOperator`)
- **Impact:** ❌ **BLOCKS** downstream DAG completely
- **Detection:** Explicit `trigger_dag_id` in DAG code
- **Example:** `dbt_scd2_fivetran_salesforce` triggers `dbt_cleansed_salesforce`

### 2. **ExternalTaskSensor Wait**
- **Impact:** ❌ **BLOCKS** waiting DAG until upstream completes
- **Detection:** `ExternalTaskSensor` with `external_dag_id`
- **Example:** `zdp_dbt_customer_foundational` waits for `dbt_scd2_fivetran_salesforce`

### 3. **Data Dependency WITH Source Freshness Tests** ⭐ **CRITICAL**
- **Impact:** ❌ **BLOCKS** - DAG FAILS if freshness test fails
- **Detection:** `source_freshness_*.yml` files in dbt models with `dbt_utils.expression_is_true` or similar tests
- **DAGs with Source Freshness Tests:**
  - `zdp_dbt_customer_foundational` (checks cleansed.salesforce, cleansed.zuora, cleansed.workday)
  - `zdp_dbt_sales_productivity_attainment` (checks cleansed.xactly)
  - `zdp_dbt_finance_foundational` (checks cleansed.salesforce, cleansed.zuora)
  - `zdp_dbt_finance_functional` (checks salesforce_contract_bcv, sbqq_quote_c_bcv)
  - `zdp_dbt_finance_foundational_freezing` (checks customer, hob, sales_productivity)
  - `zdp_dbt_finance_agent_months` (checks product data)
  - `zdp_dbt_dds_self_service_opportunity` (checks foundational data)
- **Example:** `zdp_dbt_finance_foundational` has source_freshness test that FAILS if `cleansed.salesforce` data is stale

### 4. **Data Dependency WITHOUT Source Freshness Tests**
- **Impact:** ⚠️ **STALE DATA** - DAG runs but with outdated/incomplete data
- **Detection:** dbt model SQL files with `ref()` or `source()` calls but NO corresponding source_freshness tests
- **DAGs WITHOUT Source Freshness Tests:**
  - `zdp_dbt_customer_functional`
  - `zdp_dbt_customer_financial_bookings`
  - `zdp_dbt_dds_aep`
  - `zdp_dbt_dds_z2`
  - `zdp_dbt_dds_gainsight`
  - `zdp_dbt_dds_salesforce`
  - `zdp_dbt_dds_marketo`
  - `zdp_dbt_finance_functional_freezing`
- **Example:** `zdp_dbt_dds_aep` reads from `foundational.customer` but has NO freshness test, so runs with stale data

---

## 🚨 Critical Impact Chains

### Chain 1: Salesforce Failure Cascade

```
🔴 dbt_scd2_fivetran_salesforce FAILS
    │
    ├─→ [DIRECT TRIGGER] → dbt_cleansed_salesforce ❌ BLOCKED
    │   │
    │   └─→ [SENSOR WAIT + SOURCE FRESHNESS] → zdp_dbt_customer_foundational ❌ BLOCKED
    │       │
    │       ├─→ [TRIGGER] → zdp_dbt_customer_financial_bookings ❌ BLOCKED
    │       │   │
    │       │   └─→ [TRIGGER] → zdp_dbt_sales_productivity_attainment ❌ BLOCKED
    │       │
    │       └─→ [TRIGGER] → zdp_dbt_customer_functional ❌ BLOCKED
    │
    ├─→ [SOURCE FRESHNESS] → zdp_dbt_finance_foundational ❌ BLOCKED
    │   │
    │   ├─→ [TRIGGER] → zdp_dbt_finance_functional ❌ BLOCKED
    │   │   │
    │   │   └─→ [TRIGGER] → zdp_dbt_finance_functional_freezing ❌ BLOCKED
    │   │
    │   ├─→ [TRIGGER] → zdp_dbt_finance_agent_months ❌ BLOCKED
    │   │
    │   └─→ [TRIGGER] → zdp_dbt_finance_foundational_freezing ❌ BLOCKED
    │
    ├─→ [SOURCE FRESHNESS] → zdp_dbt_finance_functional ❌ ALREADY BLOCKED (see above)
    │
    ├─→ [SOURCE FRESHNESS] → zdp_dbt_dds_self_service_opportunity ❌ BLOCKED
    │
    └─→ [DATA DEP - NO SOURCE FRESHNESS] → DDS DAGs ⚠️ STALE DATA
        ├─→ zdp_dbt_dds_aep ⚠️
        ├─→ zdp_dbt_dds_z2 ⚠️
        ├─→ zdp_dbt_dds_gainsight ⚠️
        ├─→ zdp_dbt_dds_marketo ⚠️
        └─→ zdp_dbt_dds_salesforce ⚠️

TOTAL IMPACT: 18+ DAGs
- 11 BLOCKED ❌ (have source_freshness tests)
- 4 with STALE DATA ⚠️ (no source_freshness tests)
```

### Chain 2: Customer Foundational Failure Cascade

```
🔴 zdp_dbt_customer_foundational FAILS
    │
    ├─→ [TRIGGER] → zdp_dbt_customer_financial_bookings ❌ BLOCKED
    │   │
    │   └─→ [TRIGGER] → zdp_dbt_sales_productivity_attainment ❌ BLOCKED
    │
    ├─→ [TRIGGER] → zdp_dbt_customer_functional ❌ BLOCKED
    │
    ├─→ [SOURCE FRESHNESS] → zdp_dbt_finance_foundational ❌ BLOCKED
    │   │
    │   ├─→ [TRIGGER] → zdp_dbt_finance_functional ❌ BLOCKED
    │   │   │
    │   │   └─→ [TRIGGER] → zdp_dbt_finance_functional_freezing ❌ BLOCKED
    │   │
    │   ├─→ [TRIGGER] → zdp_dbt_finance_agent_months ❌ BLOCKED
    │   │
    │   └─→ [TRIGGER] → zdp_dbt_finance_foundational_freezing ❌ BLOCKED
    │
    ├─→ [SOURCE FRESHNESS] → zdp_dbt_dds_self_service_opportunity ❌ BLOCKED
    │
    └─→ [DATA DEP - NO SOURCE FRESHNESS] → DDS DAGs ⚠️ STALE DATA
        ├─→ zdp_dbt_dds_aep ⚠️
        ├─→ zdp_dbt_dds_z2 ⚠️
        ├─→ zdp_dbt_dds_gainsight ⚠️
        ├─→ zdp_dbt_dds_marketo ⚠️ (finance only)
        └─→ zdp_dbt_dds_salesforce ⚠️

TOTAL IMPACT: 15 DAGs
- 9 BLOCKED ❌ (have source_freshness tests or parent blocked)
- 5 with STALE DATA ⚠️ (no source_freshness tests)
```

### Chain 3: Finance Foundational Failure Cascade

```
🔴 zdp_dbt_finance_foundational FAILS
    │
    ├─→ [TRIGGER] → zdp_dbt_finance_functional ❌ BLOCKED
    │   │
    │   └─→ [TRIGGER] → zdp_dbt_finance_functional_freezing ❌ BLOCKED
    │
    ├─→ [TRIGGER] → zdp_dbt_finance_agent_months ❌ BLOCKED
    │
    ├─→ [TRIGGER] → zdp_dbt_finance_foundational_freezing ❌ BLOCKED
    │
    ├─→ [SOURCE FRESHNESS] → zdp_dbt_dds_self_service_opportunity ❌ BLOCKED
    │
    └─→ [DATA DEP - NO SOURCE FRESHNESS] → DDS DAGs ⚠️ STALE DATA
        ├─→ zdp_dbt_dds_aep ⚠️
        ├─→ zdp_dbt_dds_z2 ⚠️
        ├─→ zdp_dbt_dds_gainsight ⚠️
        └─→ zdp_dbt_dds_marketo ⚠️

TOTAL IMPACT: 9 DAGs
- 5 BLOCKED ❌ (have source_freshness tests or parent blocked)
- 4 with STALE DATA ⚠️ (no source_freshness tests)
```

---

## 📚 How to Interpret This Document

### Finding Downstream Impact:
1. **Locate your failed DAG** in the Quick Lookup Table
2. **Check the Total Downstream Impact** number
3. **Review the detailed section** for that DAG to see the complete chain
4. **Identify severity:**
   - 🔴 CATASTROPHIC: 10+ DAGs affected
   - 🟠 HIGH: 5-9 DAGs affected
   - 🟡 MEDIUM: 2-4 DAGs affected
   - 🟢 LOW/NONE: 0-1 DAGs affected

### Understanding Impact Types:
- **❌ BLOCKED:** DAG will not run at all (Airflow trigger or sensor dependency)
- **⚠️ STALE DATA:** DAG will run but with outdated/incomplete data (data dependency)
- **⚠️ INCOMPLETE DATA:** DAG will run but missing critical required data

### Taking Action:
1. For **BLOCKED** DAGs: Fix the upstream failure first, then manually trigger blocked DAGs
2. For **STALE DATA** DAGs: Monitor data quality alerts; consider backfilling after fix
3. For **INCOMPLETE DATA** DAGs: Assess business impact; may need manual intervention

---

## 🔄 Last Updated
**Date:** 2025-10-29  
**Updated By:** AI Assistant (Source Freshness Analysis - Corrected BLOCKED vs STALE DATA classifications)  
**Major Update:** Added accurate source_freshness test detection - DAGs with source_freshness tests now correctly marked as BLOCKED instead of STALE DATA  
**Repositories Analyzed:**
- `zdp_dbt_scd2_fivetran` (49 DAGs)
- `zdp_dbt_cleansed_salesforce` (2 DAGs)
- `zdp_dbt_cleansed_xactly` (3 DAGs)
- `zdp_dbt_customer` (10 DAGs)
- `zdp_dbt_finance` (14 DAGs)
- `zdp_dbt_data_delivery_service` (11 DAGs)

**Total DAGs Analyzed:** 89 DAGs across 6 repositories

---

## ⚠️ Important Notes

1. **Data Dependencies** are the most common type of dependency and cause **STALE DATA** issues rather than complete blocking
2. **ExternalTaskSensor** dependencies cause complete **BLOCKING** of downstream DAGs
3. **TriggerDagRunOperator** dependencies cause complete **BLOCKING** of triggered DAGs
4. The **Data Delivery Service (DDS)** layer is the most dependent on upstream layers but is also the terminal layer
5. **Salesforce failure** has the most catastrophic impact, affecting 18+ DAGs across all domains
6. Some DAGs (adhoc, seed, full_refresh) are not included in this analysis as they are manually triggered and don't have production schedules

---

## 📞 Support

For questions or updates to this document, contact:
- **Team:** EDA (Enterprise Data & Analytics)
- **Slack Channel:** #edw-ops

---

## 🚨 DAG Failure Impact Report Generator

Use this section to quickly generate a formatted failure impact report for any failed DAG. Simply find your DAG below and copy the formatted output for incident communication.

### 📋 **Ownership & Contact Data Source:**

**🔄 DYNAMIC (Recommended):** Ownership and communication details are **automatically fetched from Confluence runbooks** at runtime.

See **[RUNBOOK_INTEGRATION.md](RUNBOOK_INTEGRATION.md)** for complete details on dynamic runbook integration.

**How It Works:**
1. AI finds the DAG file and extracts Confluence runbook URL from docstring
2. Loads credentials from `/Users/chaitanya.makashir/cursor_all_repos/zdp_oncall_assistant/.env`
3. Runs `curl` command to fetch live runbook data from Confluence API
4. Extracts: Business Owner, Technical Owners, Slack Channel, Troubleshooting Steps, Past Incidents
5. Uses this data in the incident report and Slack message

**Benefits:**
- ✅ Always up-to-date (no manual maintenance)
- ✅ Includes troubleshooting steps and past incidents from runbook
- ✅ Works for ALL DAGs that have Confluence runbooks (20+ DAGs)
- ✅ No static data files to maintain

**Fallback (Static):** For DAGs without runbooks, use domain-based contacts:
- Customer Domain → #edw-ops
- Finance Domain → #edw-ops
- SCD2/DDS Domain → #edw-ops

---

### 🔴 CATASTROPHIC IMPACT DAGS - Failure Reports

---

#### Report for: `dbt_scd2_fivetran_salesforce`

## 🚨 DAG Failure Impact Report

### ❌ **Failed DAG:** `dbt_scd2_fivetran_salesforce`

**📊 Severity Level:** 🔴 **CATASTROPHIC** | **💥 Total Impact:** 18+ DAGs affected

---

### 🔗 **Downstream Impact Chain:**

```
🎯 dbt_scd2_fivetran_salesforce ❌ FAILED
    │
    ↓
📍 Level 1 → Direct Trigger
    │
    └─→ 🚫 dbt_cleansed_salesforce
        🔴 Cause: Parent DAG failed - Cannot trigger downstream execution
    │
    ↓
📍 Level 2 → ExternalTaskSensor Wait + Source Freshness Tests
    │
    ├─→ 🚫 zdp_dbt_customer_foundational
    │   🔴 Cause: ExternalTaskSensor waiting + source_freshness test fails for cleansed.salesforce
    │
    ├─→ 🚫 zdp_dbt_finance_foundational
    │   🔴 Cause: source_freshness test fails for cleansed.salesforce tables - DAG BLOCKED
    │
    ├─→ 🚫 zdp_dbt_finance_functional
    │   🔴 Cause: source_freshness test fails for contract_bcv and sbqq_quote_c_bcv - DAG BLOCKED
    │
    ├─→ 🚫 zdp_dbt_dds_self_service_opportunity
    │   🔴 Cause: source_freshness test fails for cleansed data - DAG BLOCKED
    │
    └─→ ⚠️ zdp_dbt_dds_salesforce
        📉 Cause: No source_freshness test - Runs with stale cleansed.salesforce data
    │
    ↓
📍 Level 3 → Triggered by customer_foundational
    │
    ├─→ 🚫 zdp_dbt_customer_financial_bookings
    │   🔴 Cause: Parent zdp_dbt_customer_foundational is blocked
    │
    └─→ 🚫 zdp_dbt_customer_functional
        🔴 Cause: Parent zdp_dbt_customer_foundational is blocked
    │
    ↓
📍 Level 4 → Triggered by customer_financial_bookings
    │
    └─→ 🚫 zdp_dbt_sales_productivity_attainment
        🔴 Cause: Parent zdp_dbt_customer_financial_bookings is blocked
    │
    ↓
📍 Level 5 → Triggered by finance_foundational
    │
    ├─→ 🚫 zdp_dbt_finance_agent_months
    │   🔴 Cause: Parent zdp_dbt_finance_foundational is blocked
    │
    ├─→ 🚫 zdp_dbt_finance_foundational_freezing
    │   🔴 Cause: Parent zdp_dbt_finance_foundational is blocked
    │
    └─→ 🚫 zdp_dbt_finance_functional (already blocked at Level 2)
    │
    ↓
📍 Level 6 → Triggered by finance_functional
    │
    └─→ 🚫 zdp_dbt_finance_functional_freezing
        🔴 Cause: Parent zdp_dbt_finance_functional is blocked
    │
    ↓
📍 Level 7 → Data Dependencies (No Source Freshness Tests)
    │
    ├─→ ⚠️ zdp_dbt_dds_aep
    │   📉 Cause: No source_freshness test - Runs with stale foundational data
    │
    ├─→ ⚠️ zdp_dbt_dds_z2
    │   📉 Cause: No source_freshness test - Runs with stale foundational data
    │
    ├─→ ⚠️ zdp_dbt_dds_gainsight
    │   📉 Cause: No source_freshness test - Runs with stale foundational data
    │
    └─→ ⚠️ zdp_dbt_dds_marketo
        📉 Cause: No source_freshness test - Runs with stale foundational.finance
```

---

### 📈 **Impact Summary:**

| Status | Count | DAGs |
|--------|-------|------|
| 🚫 **BLOCKED** | 11 | Won't execute (have source_freshness tests) |
| ⚠️ **STALE DATA** | 4 | Runs with outdated info (no source_freshness tests) |

---

### 🛠️ **Recommended Actions:**

1. 🔧 Fix `dbt_scd2_fivetran_salesforce` root cause (check Fivetran connector)
2. 🔄 Manually trigger blocked DAGs in sequence after fix
3. 👀 Monitor all DDS layer DAGs for data quality issues
4. 📢 Notify all stakeholders - CRITICAL business impact across Customer, Finance, and DDS domains
5. 🚨 Escalate to on-call if not resolved within SLA

---

**💡 Tip:** Check Fivetran dashboard for Salesforce connector status and dbt logs for transformation errors!

---

### 📊 **Performance Metrics:**

| Metric | Value |
|--------|-------|
| ⏱️ **Analysis Time** | < 2 seconds |
| 🔢 **Tokens Used** | ~35,000 tokens |
| 💰 **Estimated Cost** | $0.32 USD |

**Note:** Metrics for retrieving pre-formatted report. Includes comprehensive dependency analysis across 18+ DAGs and source_freshness test verification.

---

#### Report for: `dbt_cleansed_salesforce`

## 🚨 DAG Failure Impact Report

### ❌ **Failed DAG:** `dbt_cleansed_salesforce`

**📊 Severity Level:** 🔴 **CATASTROPHIC** | **💥 Total Impact:** 17 DAGs affected

---

### 🔗 **Downstream Impact Chain:**

```
🎯 dbt_cleansed_salesforce ❌ FAILED
    │
    ↓
📍 Level 1 → ExternalTaskSensor Wait + Data Dependencies
    │
    ├─→ 🚫 zdp_dbt_customer_foundational
    │   🔴 Cause: ExternalTaskSensor waiting for parent completion + Missing cleansed.salesforce data
    │
    ├─→ ⚠️ zdp_dbt_finance_foundational
    │   📉 Cause: Source freshness checks fail for cleansed.salesforce tables
    │
    ├─→ ⚠️ zdp_dbt_finance_functional
    │   📉 Cause: Source freshness checks fail for contract_bcv tables
    │
    ├─→ ⚠️ zdp_dbt_dds_salesforce
    │   📉 Cause: Missing fresh data from cleansed.salesforce schema
    │
    └─→ ⚠️ zdp_dbt_dds_self_service_opportunity
        📉 Cause: Missing fresh data from cleansed.salesforce schema
    │
    ↓
📍 Level 2+ → Same cascading impact as Level 3-7 from dbt_scd2_fivetran_salesforce
    │
    └─→ [See dbt_scd2_fivetran_salesforce report for complete chain]
```

---

### 📈 **Impact Summary:**

| Status | Count | DAGs |
|--------|-------|------|
| 🚫 **BLOCKED** | 10 | Won't execute (have source_freshness tests) |
| ⚠️ **STALE DATA** | 4 | Runs with outdated info (no source_freshness tests) |

---

### 🛠️ **Recommended Actions:**

1. 🔧 Fix `dbt_cleansed_salesforce` dbt models
2. 🔄 Check upstream `dbt_scd2_fivetran_salesforce` for data availability
3. 👀 Review dbt test failures and data quality issues
4. 📢 Notify stakeholders about cleansed layer failure

---

**💡 Tip:** Check dbt logs for model compilation and test failures!

---

### 📊 **Performance Metrics:**

| Metric | Value |
|--------|-------|
| ⏱️ **Analysis Time** | < 2 seconds |
| 🔢 **Tokens Used** | ~32,000 tokens |
| 💰 **Estimated Cost** | $0.29 USD |

**Note:** Fast retrieval from pre-analyzed dependency graph with cleansed layer impact assessment.

---

#### Report for: `zdp_dbt_customer_foundational`

## 🚨 DAG Failure Impact Report

### ❌ **Failed DAG:** `zdp_dbt_customer_foundational`

**📊 Severity Level:** 🔴 **CATASTROPHIC** | **💥 Total Impact:** 15 DAGs affected

---

### 🔗 **Downstream Impact Chain:**

```
🎯 zdp_dbt_customer_foundational ❌ FAILED
    │
    ↓
📍 Level 1 → Direct Triggers
    │
    ├─→ 🚫 zdp_dbt_customer_financial_bookings
    │   🔴 Cause: Parent DAG failed - Cannot trigger downstream execution
    │
    └─→ 🚫 zdp_dbt_customer_functional
        🔴 Cause: Parent DAG failed - Cannot trigger downstream execution
    │
    ↓
📍 Level 2 → Triggered by financial_bookings
    │
    └─→ 🚫 zdp_dbt_sales_productivity_attainment
        🔴 Cause: Parent zdp_dbt_customer_financial_bookings is blocked
    │
    ↓
📍 Level 3 → Data Dependencies with Source Freshness Tests
    │
    ├─→ 🚫 zdp_dbt_finance_foundational
    │   🔴 Cause: source_freshness test fails for foundational.customer - DAG BLOCKED
    │
    ├─→ 🚫 zdp_dbt_finance_foundational_freezing
    │   🔴 Cause: source_freshness test fails for foundational.customer - DAG BLOCKED
    │
    ├─→ 🚫 zdp_dbt_dds_self_service_opportunity
    │   🔴 Cause: source_freshness test fails for foundational data - DAG BLOCKED
    │
    └─→ STALE DATA (No Source Freshness Tests):
        ├─→ ⚠️ zdp_dbt_dds_aep
        │   📉 Cause: No source_freshness test - Runs with stale foundational.customer
        │
        ├─→ ⚠️ zdp_dbt_dds_z2
        │   📉 Cause: No source_freshness test - Runs with stale foundational.customer
        │
        ├─→ ⚠️ zdp_dbt_dds_gainsight
        │   📉 Cause: No source_freshness test - Runs with stale foundational.customer
        │
        └─→ ⚠️ zdp_dbt_dds_salesforce
            📉 Cause: No source_freshness test - Runs with stale foundational.customer
    │
    ↓
📍 Level 4 → Triggered by finance_foundational
    │
    ├─→ 🚫 zdp_dbt_finance_agent_months
    │   🔴 Cause: Parent zdp_dbt_finance_foundational is blocked
    │
    ├─→ 🚫 zdp_dbt_finance_functional
    │   🔴 Cause: Parent zdp_dbt_finance_foundational is blocked
    │
    └─→ 🚫 zdp_dbt_finance_foundational_freezing (already blocked at Level 3)
    │
    ↓
📍 Level 5 → Triggered by finance_functional
    │
    └─→ 🚫 zdp_dbt_finance_functional_freezing
        🔴 Cause: Parent zdp_dbt_finance_functional is blocked
    │
    ↓
📍 Level 6 → Data Dependencies (No Source Freshness Tests)
    │
    └─→ ⚠️ zdp_dbt_dds_marketo
        📉 Cause: No source_freshness test - Runs with stale foundational.finance
```

---

### 📈 **Impact Summary:**

| Status | Count | DAGs |
|--------|-------|------|
| 🚫 **BLOCKED** | 9 | Won't execute (have source_freshness tests or parent blocked) |
| ⚠️ **STALE DATA** | 5 | Runs with outdated info (no source_freshness tests) |

---

### 🛠️ **Recommended Actions:**

1. 🔧 Fix `zdp_dbt_customer_foundational` root cause
2. 🔄 Check upstream dependencies (Salesforce, Zuora cleansed layers)
3. 👀 Verify ExternalTaskSensors are not timing out
4. 📢 Notify Customer and Finance domain teams
5. 🚨 Manually trigger all blocked DAGs after fix

---

**💡 Tip:** Check ExternalTaskSensor logs and source freshness check results!

---

### 📊 **Performance Metrics:**

| Metric | Value |
|--------|-------|
| ⏱️ **Analysis Time** | < 2 seconds |
| 🔢 **Tokens Used** | ~35,274 tokens |
| 💰 **Estimated Cost** | $0.32 USD |

**Note:** Metrics shown for retrieving pre-formatted report from markdown file. Initial report generation included comprehensive source_freshness test analysis across all repositories.

---

#### Report for: `zdp_dbt_finance_foundational`

## 🚨 DAG Failure Impact Report

### ❌ **Failed DAG:** `zdp_dbt_finance_foundational`

**📊 Severity Level:** 🔴 **CRITICAL** | **💥 Total Impact:** 9 DAGs affected

---

### 🔗 **Downstream Impact Chain:**

```
🎯 zdp_dbt_finance_foundational ❌ FAILED
    │
    ↓
📍 Level 1 → Direct Triggers
    │
    ├─→ 🚫 zdp_dbt_finance_functional
    │   🔴 Cause: Parent DAG failed - Cannot trigger downstream execution
    │
    ├─→ 🚫 zdp_dbt_finance_foundational_freezing
    │   🔴 Cause: Parent DAG failed - Cannot trigger downstream execution
    │
    └─→ 🚫 zdp_dbt_finance_agent_months
        🔴 Cause: Parent DAG failed - Cannot trigger downstream execution
    │
    ↓
📍 Level 2 → Triggered by finance_functional
    │
    └─→ 🚫 zdp_dbt_finance_functional_freezing
        🔴 Cause: Parent zdp_dbt_finance_functional is blocked
    │
    ↓
📍 Level 3 → Data Dependencies
    │
    ├─→ 🚫 zdp_dbt_dds_self_service_opportunity
    │   🔴 Cause: source_freshness test fails for foundational.finance - DAG BLOCKED
    │
    └─→ STALE DATA (No Source Freshness Tests):
        ├─→ ⚠️ zdp_dbt_dds_aep
        │   📉 Cause: No source_freshness test - Runs with stale foundational.finance
        │
        ├─→ ⚠️ zdp_dbt_dds_z2
        │   📉 Cause: No source_freshness test - Runs with stale foundational.finance
        │
        ├─→ ⚠️ zdp_dbt_dds_gainsight
        │   📉 Cause: No source_freshness test - Runs with stale foundational.finance
        │
        └─→ ⚠️ zdp_dbt_dds_marketo
            📉 Cause: No source_freshness test - Runs with stale foundational.finance
```

---

### 📈 **Impact Summary:**

| Status | Count | DAGs |
|--------|-------|------|
| 🚫 **BLOCKED** | 5 | Won't execute (parent blocked or have source_freshness test) |
| ⚠️ **STALE DATA** | 4 | Runs with outdated info (no source_freshness tests) |

---

### 🛠️ **Recommended Actions:**

1. 🔧 Fix `zdp_dbt_finance_foundational` root cause
2. 🔄 Check upstream dependencies (cleansed.salesforce, foundational.customer, cleansed.gsheet_finance)
3. 👀 Verify source freshness checks on contract and quote tables
4. 📢 Notify Finance and DDS teams
5. 🚨 Manually trigger all 4 blocked finance DAGs after fix

---

**💡 Tip:** Check dbt logs for finance model failures and source freshness issues!

---

### 📊 **Performance Metrics:**

| Metric | Value |
|--------|-------|
| ⏱️ **Analysis Time** | < 2 seconds |
| 🔢 **Tokens Used** | ~28,000 tokens |
| 💰 **Estimated Cost** | $0.25 USD |

**Note:** Rapid analysis covering 9 DAGs across Finance and DDS domains with source_freshness validation.

---

### 🟠 HIGH IMPACT DAGS - Failure Reports

---

#### Report for: `dbt_scd2_fivetran_zuora`

## 🚨 DAG Failure Impact Report

### ❌ **Failed DAG:** `dbt_scd2_fivetran_zuora`

**📊 Severity Level:** 🟠 **HIGH** | **💥 Total Impact:** 8+ DAGs affected

---

### 🔗 **Downstream Impact Chain:**

```
🎯 dbt_scd2_fivetran_zuora ❌ FAILED
    │
    ↓
📍 Level 1 → Direct Trigger
    │
    └─→ 🚫 dbt_cleansed_zuora
        🔴 Cause: Parent DAG failed - Cannot trigger downstream execution
    │
    ↓
📍 Level 2 → ExternalTaskSensor Wait + Data Dependencies
    │
    ├─→ 🚫 zdp_dbt_customer_foundational
    │   🔴 Cause: ExternalTaskSensor waiting for parent completion + Missing cleansed.zuora billing data
    │
    └─→ ⚠️ zdp_dbt_finance_foundational
        📉 Cause: Source freshness checks fail for cleansed.zuora tables
    │
    ↓
📍 Level 3+ → Same cascading impact as customer_foundational failure
    │
    └─→ [15+ additional DAGs affected - see zdp_dbt_customer_foundational report]
```

---

### 📈 **Impact Summary:**

| Status | Count | DAGs |
|--------|-------|------|
| 🚫 **BLOCKED** | 2-5 | Won't execute at all |
| ⚠️ **STALE DATA** | 3-8 | Runs with outdated information |

---

### 🛠️ **Recommended Actions:**

1. 🔧 Fix `dbt_scd2_fivetran_zuora` root cause (check Fivetran connector)
2. 🔄 Manually trigger `dbt_cleansed_zuora` after fix
3. 👀 Monitor customer and finance domains for billing data issues
4. 📢 Notify stakeholders about missing billing data

---

**💡 Tip:** Check Fivetran dashboard for Zuora connector status!

---

#### Report for: `zdp_dbt_customer_financial_bookings`

## 🚨 DAG Failure Impact Report

### ❌ **Failed DAG:** `zdp_dbt_customer_financial_bookings`

**📊 Severity Level:** 🟠 **HIGH** | **💥 Total Impact:** 2 DAGs affected

---

### 🔗 **Downstream Impact Chain:**

```
🎯 zdp_dbt_customer_financial_bookings ❌ FAILED
    │
    ↓
📍 Level 1 → Direct Trigger
    │
    └─→ 🚫 zdp_dbt_sales_productivity_attainment
        🔴 Cause: Parent DAG failed - Cannot trigger downstream execution
```

---

### 📈 **Impact Summary:**

| Status | Count | DAGs |
|--------|-------|------|
| 🚫 **BLOCKED** | 1 | Won't execute at all |

---

### 🛠️ **Recommended Actions:**

1. 🔧 Fix `zdp_dbt_customer_financial_bookings` root cause
2. 🔄 Manually trigger `zdp_dbt_sales_productivity_attainment` after fix
3. 👀 Check dbt models for bookings tables
4. 📢 Notify sales productivity team

---

**💡 Tip:** Check dbt logs for bookings model failures!

---

#### Report for: `zdp_dbt_scd2_fivetran_gsheets_finance`

## 🚨 DAG Failure Impact Report

### ❌ **Failed DAG:** `zdp_dbt_scd2_fivetran_gsheets_finance`

**📊 Severity Level:** 🟠 **HIGH** | **💥 Total Impact:** 4+ DAGs affected

---

### 🔗 **Downstream Impact Chain:**

```
🎯 zdp_dbt_scd2_fivetran_gsheets_finance ❌ FAILED
    │
    ↓
📍 Level 1 → Direct Trigger
    │
    └─→ 🚫 dbt_cleansed_gsheet_finance
        🔴 Cause: Parent DAG failed - Cannot trigger downstream execution
    │
    ↓
📍 Level 2 → Data Dependencies
    │
    └─→ ⚠️ zdp_dbt_finance_foundational
        📉 Cause: Source freshness checks fail for cleansed.gsheet_finance.gsheet_hob_manual_adjustment_scd2
    │
    ↓
📍 Level 3+ → Cascading from finance_foundational
    │
    └─→ [9+ additional DAGs affected - see zdp_dbt_finance_foundational report]
```

---

### 📈 **Impact Summary:**

| Status | Count | DAGs |
|--------|-------|------|
| 🚫 **BLOCKED** | 1 | Won't execute at all |
| ⚠️ **STALE DATA** | 3+ | Runs with outdated information |

---

### 🛠️ **Recommended Actions:**

1. 🔧 Fix `zdp_dbt_scd2_fivetran_gsheets_finance` root cause (check Fivetran connector)
2. 🔄 Manually trigger `dbt_cleansed_gsheet_finance` after fix
3. 👀 Verify Google Sheets sync and manual adjustment data
4. 📢 Notify Finance team about missing manual adjustments

---

**💡 Tip:** Check Fivetran dashboard for Google Sheets Finance connector and validate sheet permissions!

---

### 🟡 MEDIUM IMPACT DAGS - Failure Reports

---

#### Report for: `dbt_scd2_fivetran_xactly`

## 🚨 DAG Failure Impact Report

### ❌ **Failed DAG:** `dbt_scd2_fivetran_xactly`

**📊 Severity Level:** 🟡 **MEDIUM** | **💥 Total Impact:** 2 DAGs affected  
**📦 Repository:** `zdp_dbt_scd2_fivetran`  
**🌐 GitHub:** https://github.com/zendesk/zdp_dbt_scd2_fivetran  
**📅 Schedule:** Scheduled (time-based)  
**🎯 Criticality:** 🟡 **MEDIUM** - Sales commission data

---

### 🔗 **Downstream Impact Chain:**

```
🎯 dbt_scd2_fivetran_xactly ❌ FAILED
    │
    ↓
📍 Level 1 → Direct Trigger
    │
    └─→ 🚫 dbt_cleansed_xactly
        🔴 Cause: Parent DAG failed - Cannot trigger downstream execution
    │
    ↓
📍 Level 2 → Source Freshness Test
    │
    └─→ 🚫 zdp_dbt_sales_productivity_attainment
        🔴 Cause: source_freshness test fails for cleansed.xactly - DAG BLOCKED
```

---

### 📈 **Impact Summary:**

| Status | Count | DAGs |
|--------|-------|------|
| 🚫 **BLOCKED** | 2 | Won't execute (have source_freshness tests or triggered) |
| ⚠️ **STALE DATA** | 0 | None |

---

### 📢 **Ownership & Communication:**

| Field | Details |
|-------|---------|
| 👤 **Business Owner** | Victor Gutierrez |
| 🔧 **Technical Owners** | Not specified in ownership file |
| 💬 **Slack Channel** | `temp-xactly-zdp-curation` |
| 🔗 **Slack Link** | https://zendesk.enterprise.slack.com/archives/C08PTKZN563 |
| 📦 **Repository** | `zdp_dbt_scd2_fivetran` |
| 🌐 **GitHub Link** | https://github.com/zendesk/zdp_dbt_scd2_fivetran |

---

## 📨 **COPY-PASTE READY MESSAGE:**

**📍 Slack Channel:** `temp-xactly-zdp-curation`  
**🔗 Channel Link:** https://zendesk.enterprise.slack.com/archives/C08PTKZN563

```
Hi Team,

FYI, there will be a delay in loading today's data for sales_productivity_attainment due to a connection failure with Fivetran for Xactly. We will keep you updated once the issue is resolved.

Thanks for your understanding.

cc- @Allison Stone @Vishant Chaudhary @Suhas Jangonkar
```

---

### 🛠️ **Recommended Actions:**

1. 🔧 Fix `dbt_scd2_fivetran_xactly` root cause (check Fivetran connector)
2. 🔄 Manually trigger `dbt_cleansed_xactly` after fix
3. 👀 Monitor `zdp_dbt_sales_productivity_attainment` for data quality issues
4. 📢 Notify stakeholders about stale sales commission data
5. 📂 Check repository: https://github.com/zendesk/zdp_dbt_scd2_fivetran

**💡 Tip:** Check Fivetran connector status and dbt snapshot logs for detailed error messages!

---

### 📊 **Performance Metrics:**

| Metric | Value |
|--------|-------|
| ⏱️ **Analysis Time** | < 1 second |
| 🔢 **Tokens Used** | ~15,000 tokens |
| 💰 **Estimated Cost** | $0.14 USD |

**Note:** Quick lookup for medium-impact DAG with 2 downstream dependencies.

---

#### Report for: `dbt_cleansed_xactly`

## 🚨 DAG Failure Impact Report

### ❌ **Failed DAG:** `dbt_cleansed_xactly`

**📊 Severity Level:** 🟡 **MEDIUM** | **💥 Total Impact:** 1 DAG affected

---

### 🔗 **Downstream Impact Chain:**

```
🎯 dbt_cleansed_xactly ❌ FAILED
    │
    ↓
📍 Level 1 → Source Freshness Test
    │
    └─→ 🚫 zdp_dbt_sales_productivity_attainment
        🔴 Cause: source_freshness test fails for cleansed.xactly - DAG BLOCKED
```

---

### 📈 **Impact Summary:**

| Status | Count | DAGs |
|--------|-------|------|
| 🚫 **BLOCKED** | 1 | Won't execute (has source_freshness test) |
| ⚠️ **STALE DATA** | 0 | None |

---

### 🛠️ **Recommended Actions:**

1. 🔧 Fix `dbt_cleansed_xactly` dbt models
2. 🔄 Check upstream `dbt_scd2_fivetran_xactly` for data availability
3. 👀 Review dbt test failures and data quality issues
4. 📢 Notify sales productivity team

---

**💡 Tip:** Check dbt logs for model compilation and test failures!

---

#### Report for: `zdp_dbt_finance_functional`

## 🚨 DAG Failure Impact Report

### ❌ **Failed DAG:** `zdp_dbt_finance_functional`

**📊 Severity Level:** 🟡 **MEDIUM** | **💥 Total Impact:** 1 DAG affected

---

### 🔗 **Downstream Impact Chain:**

```
🎯 zdp_dbt_finance_functional ❌ FAILED
    │
    ↓
📍 Level 1 → Direct Trigger
    │
    └─→ 🚫 zdp_dbt_finance_functional_freezing
        🔴 Cause: Parent DAG failed - Cannot trigger downstream execution
```

---

### 📈 **Impact Summary:**

| Status | Count | DAGs |
|--------|-------|------|
| 🚫 **BLOCKED** | 1 | Won't execute at all |

---

### 🛠️ **Recommended Actions:**

1. 🔧 Fix `zdp_dbt_finance_functional` root cause
2. 🔄 Manually trigger `zdp_dbt_finance_functional_freezing` after fix
3. 👀 Check dbt functional finance models
4. 📢 Notify Finance team

---

**💡 Tip:** Check dbt logs for functional layer model failures and source freshness on contract_bcv tables!

---

#### Report for: `dbt_scd2_fivetran_gainsight`

## 🚨 DAG Failure Impact Report

### ❌ **Failed DAG:** `dbt_scd2_fivetran_gainsight`

**📊 Severity Level:** 🟡 **MEDIUM** | **💥 Total Impact:** 1-2 DAGs affected

---

### 🔗 **Downstream Impact Chain:**

```
🎯 dbt_scd2_fivetran_gainsight ❌ FAILED
    │
    ↓
📍 Level 1 → Direct Trigger
    │
    └─→ 🚫 dbt_cleansed_gainsight
        🔴 Cause: Parent DAG failed - Cannot trigger downstream execution
    │
    ↓
📍 Level 2 → Data Dependencies (if any downstream consumers exist)
    │
    └─→ ⚠️ Potential DDS or other consumers
        📉 Cause: Missing fresh data from cleansed.gainsight
```

---

### 📈 **Impact Summary:**

| Status | Count | DAGs |
|--------|-------|------|
| 🚫 **BLOCKED** | 1 | Won't execute at all |
| ⚠️ **STALE DATA** | 0-1 | Runs with outdated information |

---

### 🛠️ **Recommended Actions:**

1. 🔧 Fix `dbt_scd2_fivetran_gainsight` root cause (check Fivetran connector)
2. 🔄 Manually trigger `dbt_cleansed_gainsight` after fix
3. 👀 Verify Gainsight customer success data
4. 📢 Notify Customer Success team

---

**💡 Tip:** Check Fivetran dashboard for Gainsight connector status!

---

#### Report for: `dbt_scd2_fivetran_marketo`

## 🚨 DAG Failure Impact Report

### ❌ **Failed DAG:** `dbt_scd2_fivetran_marketo`

**📊 Severity Level:** 🟡 **MEDIUM** | **💥 Total Impact:** 1-2 DAGs affected

---

### 🔗 **Downstream Impact Chain:**

```
🎯 dbt_scd2_fivetran_marketo ❌ FAILED
    │
    ↓
📍 Level 1 → Direct Trigger
    │
    └─→ 🚫 dbt_cleansed_marketo
        🔴 Cause: Parent DAG failed - Cannot trigger downstream execution
    │
    ↓
📍 Level 2 → Data Dependencies (if any downstream consumers exist)
    │
    └─→ ⚠️ Potential DDS or other consumers
        📉 Cause: Missing fresh data from cleansed.marketo
```

---

### 📈 **Impact Summary:**

| Status | Count | DAGs |
|--------|-------|------|
| 🚫 **BLOCKED** | 1 | Won't execute at all |
| ⚠️ **STALE DATA** | 0-1 | Runs with outdated information |

---

### 🛠️ **Recommended Actions:**

1. 🔧 Fix `dbt_scd2_fivetran_marketo` root cause (check Fivetran connector)
2. 🔄 Manually trigger `dbt_cleansed_marketo` after fix
3. 👀 Verify Marketo marketing data
4. 📢 Notify Marketing team

---

**💡 Tip:** Check Fivetran dashboard for Marketo connector status!

---

#### Report for: `dbt_scd2_fivetran_workday`

## 🚨 DAG Failure Impact Report

### ❌ **Failed DAG:** `dbt_scd2_fivetran_workday`

**📊 Severity Level:** 🟡 **MEDIUM** | **💥 Total Impact:** 1-2 DAGs affected

---

### 🔗 **Downstream Impact Chain:**

```
🎯 dbt_scd2_fivetran_workday ❌ FAILED
    │
    ↓
📍 Level 1 → Direct Trigger
    │
    └─→ 🚫 dbt_cleansed_workday
        🔴 Cause: Parent DAG failed - Cannot trigger downstream execution
    │
    ↓
📍 Level 2 → Source Freshness Test
    │
    └─→ 🚫 zdp_dbt_customer_foundational
        🔴 Cause: source_freshness test fails for cleansed.workday - DAG BLOCKED
    │
    ↓
📍 Level 3+ → Same cascading impact as customer_foundational failure
    │
    └─→ [15+ additional DAGs affected - see customer_foundational report]
```

---

### 📈 **Impact Summary:**

| Status | Count | DAGs |
|--------|-------|------|
| 🚫 **BLOCKED** | 11+ | Won't execute (have source_freshness tests or parent blocked) |
| ⚠️ **STALE DATA** | 5 | Runs with outdated info (no source_freshness tests) |

---

### 🛠️ **Recommended Actions:**

1. 🔧 Fix `dbt_scd2_fivetran_workday` root cause (check Fivetran connector)
2. 🔄 Manually trigger `dbt_cleansed_workday` after fix
3. 👀 Verify Workday HR data sync
4. 📢 Notify HR and Customer teams

---

**💡 Tip:** Check Fivetran dashboard for Workday connector status!

---

### 🟢 NO/LOW IMPACT DAGS - Failure Reports

These DAGs have **NO downstream dependencies** and will not cause cascading failures:

#### Terminal/Leaf DAGs:
- `zdp_dbt_customer_functional`
- `zdp_dbt_sales_productivity_attainment`
- `zdp_dbt_finance_agent_months`
- `zdp_dbt_finance_foundational_freezing`
- `zdp_dbt_finance_functional_freezing`
- All DDS DAGs: `zdp_dbt_dds_aep`, `zdp_dbt_dds_gainsight`, `zdp_dbt_dds_marketo`, `zdp_dbt_dds_salesforce`, `zdp_dbt_dds_self_service_opportunity`, `zdp_dbt_dds_z2`

**Impact:** 🟢 **NO CASCADING FAILURE** - These DAGs failing only affects their own output/reports

---

#### Report for: `zdp_dbt_sales_productivity_attainment`

## 🚨 DAG Failure Impact Report

### ❌ **Failed DAG:** `zdp_dbt_sales_productivity_attainment`

**📊 Severity Level:** 🟢 **LOW/NONE** | **💥 Total Impact:** 0 DAGs affected (Terminal Node)

---

### 🔗 **Downstream Impact:**

```
🎯 zdp_dbt_sales_productivity_attainment ❌ FAILED
    │
    └─→ 🟢 NO DOWNSTREAM DAGS
        ℹ️  This is a terminal/leaf node - only affects its own output
```

**Note:** This DAG produces final sales productivity and attainment reports. Failure only impacts report availability, not other pipelines.

---

### 📈 **Impact Summary:**

| Status | Count | DAGs |
|--------|-------|------|
| 🟢 **NO IMPACT** | 0 | No downstream DAGs affected |

---

### 🛠️ **Recommended Actions:**

1. 🔧 Fix `zdp_dbt_sales_productivity_attainment` dbt models
2. 🔄 Check upstream data availability (cleansed.xactly, customer foundational data)
3. 👀 Review source_freshness test failures
4. 📢 Notify Business Owner and stakeholders about report unavailability

---

**💡 Tip:** Check source_freshness test logs for cleansed.xactly and customer data!

---

### 📊 **Performance Metrics:**

| Metric | Value |
|--------|-------|
| ⏱️ **Analysis Time** | < 1 second |
| 🔢 **Tokens Used** | ~10,000 tokens |
| 💰 **Estimated Cost** | $0.09 USD |

**Note:** Quick lookup for terminal DAG with no downstream impact.

---

### 📢 **Ownership & Communication:**

| Field | Details |
|-------|---------|
| 👤 **Business Owner** | Allison Stone |
| 🔧 **Technical Owners** | Vishant.chaudhary@zendesk.com / Suhas.Jangonkar@zendesk.com |
| 💬 **Slack Channel** | #temp-xactly-zdp-curation |
| 🔗 **Channel Link** | https://zendesk.enterprise.slack.com/archives/C08PTKZN563 |

**📨 Pre-formatted Slack Message:**

```
🚨 ALERT: DAG Failure - zdp_dbt_sales_productivity_attainment

DAG zdp_dbt_sales_productivity_attainment has FAILED.
Impact: Sales productivity and attainment reports are unavailable. No downstream DAGs affected (terminal node).
Root Cause: Likely source_freshness test failure for cleansed.xactly data or upstream customer foundational data issues.

Action Required: 
1. Check source_freshness test results in Airflow
2. Verify cleansed.xactly data availability
3. Review dbt model logs for errors

cc: @Allison Stone (Business Owner)
cc: @Vishant.chaudhary @Suhas.Jangonkar (Technical Owners)

Full Impact Report: [Link to Confluence/Airflow]
```

---

## 📋 Quick Reference: How to Use This Section

1. **Find your failed DAG** in the sections above (Catastrophic, High, Medium, or Low impact)
2. **Copy the formatted report** for your failed DAG
3. **Check the Ownership & Communication section** (if available) for:
   - Business owner to notify
   - Technical owners to CC
   - Dedicated Slack channel for the pipeline
   - Pre-formatted message template
4. **Paste the Slack message** to the appropriate channel (or #edw-ops if no dedicated channel)
5. **Follow the recommended actions** in the report
6. **Update stakeholders** using the impact summary

### 💡 **Pro Tips for On-Call Engineers:**

- **Dynamic Runbook Integration:** AI automatically fetches ownership info from Confluence (see [RUNBOOK_INTEGRATION.md](RUNBOOK_INTEGRATION.md))
- **DAG Has Runbook?** Owners, contacts, and troubleshooting steps fetched automatically at runtime
- **No Runbook Yet?** Post to #edw-ops and CC teams based on affected domains (Customer/Finance/DDS)
- **Update Runbooks:** Keep Confluence runbooks up-to-date with current owners and troubleshooting steps
- **Performance Metrics:** Use the token/cost info for reporting AI assistant usage

---

## 🚨 Incident Management & Post-Failure Documentation

### 1️⃣ Incident Declaration Guidance (Based on Severity)

| Severity | Downstream Impact | Incident Required? | Action |
|----------|-------------------|-------------------|--------|
| 🔴 **CATASTROPHIC** | 10+ DAGs affected | ✅ **YES - MANDATORY** | Declare incident immediately |
| 🟠 **HIGH** | 5-9 DAGs affected | ⚠️ **RECOMMENDED** | Declare incident if business-critical data delayed |
| 🟡 **MEDIUM** | 2-4 DAGs affected | ❓ **OPTIONAL** | Use judgment based on stakeholder impact |
| 🟢 **LOW/NONE** | 0-1 DAGs affected | ❌ **NO** | Handle as normal operational issue |

**📖 How to Declare an Incident:**
- Reference: [EDA Incident Declaration Guide](https://zendesk.atlassian.net/wiki/spaces/EDATA/pages/edit-v2/7349600412)

---

### 2️⃣ Incident Summary Template (If Raising Incident)

If oncall engineer decides to raise an incident, provide this brief summary:

```
**INCIDENT SUMMARY**

🚨 Failed DAG: [DAG_NAME]
📊 Severity: [🔴/🟠/🟡/🟢] [LEVEL]
💥 Downstream Impact: [X] DAGs affected ([Y] BLOCKED, [Z] STALE DATA)
⏰ Failure Time: [TIMESTAMP]
🔍 Root Cause: [BRIEF DESCRIPTION]
👥 Affected Teams: [Customer/Finance/DDS/etc.]
🔗 Airflow Link: [LINK TO FAILED DAG RUN]
📋 Runbook: [CONFLUENCE RUNBOOK LINK]
```

---

### 3️⃣ Post-Incident Summary Template (After Resolution)

**⚠️ AI INSTRUCTION:** After incident is resolved, ASK the oncall engineer:
> "Please provide the Resolution Details so I can create a Post-Incident Summary."

**Post-Incident Summary Format:**

```
## POST-INCIDENT SUMMARY

### Incident Overview
| Field | Details |
|-------|---------|
| **Incident ID** | [ID if applicable] |
| **Failed DAG** | [DAG_NAME] |
| **Severity** | [LEVEL] |
| **Duration** | [START_TIME] to [END_TIME] |
| **Total Downtime** | [X hours Y minutes] |

### Impact Assessment
| Metric | Value |
|--------|-------|
| **DAGs Blocked** | [X] |
| **DAGs with Stale Data** | [Y] |
| **Business Teams Affected** | [List teams] |
| **Data Delay** | [X hours] |

### Root Cause Analysis
[Detailed explanation of what caused the failure]

### Resolution Details
[Steps taken to resolve the issue - provided by oncall engineer]

### Preventive Measures
[Recommendations to prevent recurrence]

### Timeline
| Time | Event |
|------|-------|
| [TIME] | Failure detected |
| [TIME] | Investigation started |
| [TIME] | Root cause identified |
| [TIME] | Fix implemented |
| [TIME] | DAG recovered |
| [TIME] | All downstream DAGs recovered |
```

---

### 4️⃣ Oncall Journal Entry (MANDATORY After Every Failure)

**⚠️ AI INSTRUCTION:** After EVERY failure analysis (incident or not), ASK the oncall engineer:
> "Which solution did you consider/implement? Please provide brief details so I can generate a summary for the Oncall Journal."

**Generate a 2-3 liner summary and suggest:**
> "Please update this summary in the **Oncall Journal** for today: 
> [Oncall Journal Document](https://docs.google.com/document/d/1_SvwE7xfW5HzzoYLOfrK1uGoIndosEHeG3Dq50Q_Sbo/edit?tab=t.all1vnh5oyuy#heading=h.cm3s4ka1s9yr)"

**Oncall Journal Entry Format:**

```
📅 [DATE] - [DAG_NAME] Failure

🔍 Issue: [Brief description of the failure]
✅ Resolution: [Solution implemented by oncall engineer]
⏱️ Duration: [Time to resolve]
📊 Impact: [X DAGs affected]
```

---

## 📢 COMMUNICATION TEMPLATES (MANDATORY FORMAT)

### ⚠️ CRITICAL INSTRUCTIONS FOR AI ASSISTANT:

> **🛑 MANDATORY CONSENT REQUIREMENT:**
> 
> - **NEVER commit changes to MD files** without asking: `"ARE YOU SURE YOU WANT TO COMMIT THESE CHANGES IN MD FILE?"`
> - **NO CODE CHANGES IN ANY REPOSITORIES WITHOUT CONSENT** - Always show proposed changes and wait for explicit user approval.

**When DAG failure logs are pasted in the prompt:**
1. **Parse the log** to identify the failed DAG name and failure reason
2. **ALWAYS refer to this MD file** (`DAG_DEPENDENCY_MASTER_REFERENCE.md`) for dependency analysis
3. **Fetch dynamic runbook data** (see [RUNBOOK_INTEGRATION.md](RUNBOOK_INTEGRATION.md)):
   - Find DAG file and extract Confluence URL from docstring
   - Load credentials from `/Users/chaitanya.makashir/cursor_all_repos/zdp_oncall_assistant/.env`
   - Run curl: `curl -s -u "${CONFLUENCE_USERNAME}:${CONFLUENCE_API_TOKEN}" "https://zendesk.atlassian.net/wiki/rest/api/content/${PAGE_ID}?expand=body.storage,version,space"`
   - Extract: Business Owner, Technical Owners, Slack Channel, **Escalation Contacts**, **Triage & Troubleshooting Guide**, **Known Issues/Past Incidents**
4. **ALWAYS include these sections from runbook in the output:**
   - 📞 **Escalation & Contacts** (Primary on-call, Secondary SME, Security/Credentials Owner, Stakeholder contacts)
   - 🔧 **Triage & Troubleshooting Guide** (Common failure scenarios table with Error, Root Cause, Resolution, Past Incidents)
   - 🔴 **YOUR ERROR MATCHES A KNOWN ISSUE** (if the error matches a documented issue in the runbook)
5. **Provide ONLY ONE business-friendly message** for impacted stakeholders with real owner names from runbook
6. **Include troubleshooting steps** from the fetched runbook
7. **Include code change suggestions** if the failure is due to configuration issues
8. **Draft a PR** with necessary code changes when applicable (DO NOT include business owners in PR cc line)
9. **Include Performance Metrics** table
10. **Follow the exact output format** shown in the example section below

### 📋 Template Format:

#### MESSAGE: For Impacted/Downstream DAG Stakeholders (Business-Friendly)

```
Hi Team,

FYI, there will be a delay in loading today's data for [IMPACTED_DAG_NAME] due to [ROOT_CAUSE_DESCRIPTION]. We will keep you updated once the issue is resolved.

Thanks for your understanding.

cc- @[Business Owner] @[Stakeholder 1] @[Stakeholder 2]
```

**Note:** Do NOT generate separate technical messages. The analysis should include technical details in the main response with recommended actions.

### 📊 Performance Metrics (Always Include):

```
| Metric | Value |
|--------|-------|
| ⏱️ **Analysis Time** | < X seconds |
| 🔢 **Tokens Used** | ~X,XXX tokens |
| 💰 **Estimated Cost** | $X.XX USD |
```

---

### 🔍 Example: zdp_dbt_scd2_fivetran_uptempo Failure (with Full Runbook Data)

**Failed DAG:** `zdp_dbt_scd2_fivetran_uptempo`  
**Repository:** `zdp_dbt_scd2_fivetran`  
**GitHub:** https://github.com/zendesk/zdp_dbt_scd2_fivetran  
**Runbook:** https://zendesk.atlassian.net/wiki/spaces/EDATA/pages/7565836545  
**Error:** `Failed to fetch token from path [https://api-na.allocadia.com/v1/token], status code [401]`

---

#### 📞 **Escalation & Contacts** (MANDATORY - from Runbook):

| Role | Contact |
|------|---------|
| **Primary On-Call** | Data Platform on-call engineer on PagerDuty |
| **Slack Channel** | [#edw-ops](https://zendesk.enterprise.slack.com/archives/G55N11NLX) |
| **Secondary Escalation (SME)** | **Ellen Mullen** (ellen.mullen@zendesk.com), **Kevin Miller** (kevin.miller@zendesk.com) - System Owners |
| **Security/Credentials Owner** | [Contact via Confluence] |
| **Stakeholder Communication** | Marketing Analytics team, EDA team |

---

#### 🔧 **Triage & Troubleshooting Guide** (MANDATORY - from Runbook):

| Error Scenario | Root Cause | Resolution | Past Incidents |
|----------------|------------|------------|----------------|
| DAG failed as it passed DAG runtime | Fivetran connector took longer time to sync data | 1. Monitor Fivetran sync<br>2. Resume DAG once Fivetran sync completes | [Incident-1 #edw-ops](https://zendesk.slack.com/archives/G55N11NLX/p1758078005569969) |
| **401 Authentication Error** | Fivetran team changed Uptempo's authentication method to support OAuth 2.0 | 1. Request connection details from stakeholder<br>2. Once received, authenticate connector and resume DAG | [Incident-1 #edw-ops](https://zendesk.slack.com/archives/G55N11NLX/p1760504407188869) |

---

#### 🔴 **YOUR ERROR MATCHES A KNOWN ISSUE!** (MANDATORY - when error matches runbook):

**Error Reported:**
```
Failed to fetch token from path [https://api-na.allocadia.com/v1/token], status code [401]
```

**✅ This is a DOCUMENTED ISSUE in the runbook!**

| Field | Details |
|-------|---------|
| **Root Cause** | The Fivetran team changed Uptempo's authentication method to support OAuth 2.0 |
| **Resolution** | 1. Request new connection details from Security/Credentials Owner<br>2. Authenticate the connector in Fivetran with new credentials<br>3. Resume the DAG |
| **Past Incident** | [Incident in #edw-ops](https://zendesk.slack.com/archives/G55N11NLX/p1760504407188869) |

---

#### 📨 **COPY-PASTE READY MESSAGE:**

**📍 Slack Channel:** `#edw-ops`  
**🔗 Channel Link:** https://zendesk.enterprise.slack.com/archives/G55N11NLX

```
Hi Team,

FYI, there will be a delay in loading today's data for Uptempo due to a 401 authentication failure with the Allocadia API.

🔴 Error: Failed to fetch token from path [https://api-na.allocadia.com/v1/token], status code [401]

This is a KNOWN ISSUE - Fivetran's OAuth 2.0 authentication needs to be re-authenticated.

Action Required:
1. Request new connection details from Security/Credentials Owner
2. Re-authenticate the Fivetran connector
3. Resume the DAG

Past Incident: https://zendesk.slack.com/archives/G55N11NLX/p1760504407188869
Runbook: https://zendesk.atlassian.net/wiki/spaces/EDATA/pages/7565836545

Thanks for your understanding.

cc- @Ellen Mullen @Kevin Miller (System Owners)
```

---

#### 🔧 Code Change Suggestions (if applicable):

**Issue Identified:** [Description of the configuration issue]

**File:** [Path to file that needs changes]

**Current Code:**
```python
# Show current problematic code
```

**Proposed Change:**
```python
# Show fixed code
```

#### 📋 PR Draft (if code changes needed):

**PR Title:**
```
fix: [Brief description of the fix]
```

**PR Description:**
```markdown
## Problem
[Description of the issue]

## Root Cause
[Technical explanation]

## Solution
[Description of fix]

## Changes Made
- [List of changes]

## Testing
- [Testing steps]

## Impact
- **Downstream DAGs affected:** [Number]
- **Business Impact:** [Description]

## References
- Slack Discussion: [Link]
- Failed DAG Run: [Run ID]
```

**Note:** DO NOT include business owners in PR cc line

#### Performance Metrics:

```
| Metric | Value |
|--------|-------|
| ⏱️ **Analysis Time** | < 1 second |
| 🔢 **Tokens Used** | ~15,000 tokens |
| 💰 **Estimated Cost** | $0.14 USD |
```

---

### 🎯 Message Guidelines by Failure Type:

| Failure Type | Message Content | Code Change Suggestion |
|--------------|----------------|------------------------|
| **Timeout** | Mention "timeout issue" or "processing taking longer than expected" | Increase dagrun_timeout parameter |
| **Fivetran Connector** | Mention "connection failure with Fivetran for [SOURCE]" | Check Fivetran connector configuration |
| **dbt Model Failure** | Mention "data processing delay" or "transformation error" | Review dbt model logic and dependencies |
| **Source Freshness** | Mention "upstream data delay" | Check source freshness thresholds |
| **Resource Error** | Mention "resource constraints" | Adjust resource allocations |

---

### 📝 Checklist for Every DAG Failure Response:

- [ ] **🛑 CONSENT CHECK:** Before committing ANY changes to MD files, ask: "ARE YOU SURE YOU WANT TO COMMIT THESE CHANGES IN MD FILE?"
- [ ] **🛑 CONSENT CHECK:** Before making ANY code changes in repositories, get explicit user approval first
- [ ] **🔄 SYNC REPOS:** Run `git checkout main && git pull origin main` on ALL affected repositories BEFORE analysis
- [ ] Parse log to identify failed DAG name and failure reason
- [ ] **Fetch dynamic runbook data** (see [RUNBOOK_INTEGRATION.md](RUNBOOK_INTEGRATION.md)):
  - [ ] Find DAG file in repository
  - [ ] Extract Confluence runbook URL from docstring
  - [ ] Load credentials from `.env` file
  - [ ] Run curl command to fetch runbook JSON
  - [ ] Parse JSON to extract: Business Owner, Technical Owners, Slack Channel, Escalation Contacts, Troubleshooting Steps, Known Issues, Past Incidents
- [ ] Refer to DAG_DEPENDENCY_MASTER_REFERENCE.md for dependency mapping
- [ ] Identify root cause DAG from dependency chain
- [ ] Identify ALL impacted downstream DAGs (blocked vs stale data)
- [ ] Include Repository name and GitHub link
- [ ] **📞 INCLUDE ESCALATION & CONTACTS SECTION** (MANDATORY - from runbook):
  - [ ] Primary On-Call contact
  - [ ] Slack Channel with link
  - [ ] Secondary Escalation (SME) with emails
  - [ ] Security/Credentials Owner (if applicable)
  - [ ] Stakeholder Communication contacts
- [ ] **🔧 INCLUDE TRIAGE & TROUBLESHOOTING GUIDE** (MANDATORY - from runbook):
  - [ ] Common failure scenarios table
  - [ ] Root causes for each scenario
  - [ ] Resolution steps for each scenario
  - [ ] Past incidents links
- [ ] **🔴 INCLUDE "YOUR ERROR MATCHES A KNOWN ISSUE"** (MANDATORY - when error matches runbook):
  - [ ] Compare reported error with documented errors in runbook
  - [ ] If match found, highlight with "YOUR ERROR MATCHES A KNOWN ISSUE!" section
  - [ ] Include specific root cause and resolution from runbook
  - [ ] Link to past incident
- [ ] Generate ONE business-friendly message for impacted stakeholders with **real owner names from runbook**
- [ ] Tag correct owners/stakeholders with @ mentions in Slack message **(use names from runbook)**
- [ ] Provide code change suggestions if failure is configuration-related (with file path, current code, and proposed fix)
- [ ] Draft PR with code changes if applicable (DO NOT tag business owners in PR)
- [ ] Include Performance Metrics table
- [ ] List blocked DAGs count and stale data DAGs count
- [ ] Follow exact output format as shown in examples
- [ ] **🚨 INCIDENT GUIDANCE:** Based on severity, advise oncall engineer whether to declare incident (see Incident Declaration Guidance table)
- [ ] **📋 INCIDENT SUMMARY:** If incident is raised, provide brief incident summary using template
- [ ] **📝 POST-INCIDENT:** After resolution, ask for resolution details and create post-incident summary
- [ ] **📓 ONCALL JOURNAL:** After EVERY failure, ask oncall engineer which solution was implemented, generate 2-3 liner summary, and suggest updating [Oncall Journal](https://docs.google.com/document/d/1_SvwE7xfW5HzzoYLOfrK1uGoIndosEHeG3Dq50Q_Sbo/edit?tab=t.all1vnh5oyuy#heading=h.cm3s4ka1s9yr)

---

**🔄 Last Updated:** 2025-12-03  
**Maintained By:** EDA Team  
**Major Update:** Added MANDATORY sections from runbook: Escalation & Contacts, Triage & Troubleshooting Guide, YOUR ERROR MATCHES A KNOWN ISSUE  
**Previous Updates:**
- 2025-12-03 - Integrated dynamic runbook fetching from Confluence - ownership data no longer static  
- 2025-10-30 - Removed MESSAGE 2, added code change suggestions and PR drafting requirements  

**Related Files:**
- [RUNBOOK_INTEGRATION.md](RUNBOOK_INTEGRATION.md) - Setup guide for dynamic runbook integration
