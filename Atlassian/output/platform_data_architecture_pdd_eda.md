# Platform Data Architecture
## Data Engineering Perspective: PDD, EDA, and Platform Data

**Document Type:** Technical Architecture Documentation  
**Perspective:** Platform Data Domain (PDD), Enterprise Data Architecture (EDA)  
**Focus:** Data Engineering & Product Analytics  
**Exported:** 2025-11-27 18:25:04  
**Source:** [Platform Data Architecture](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/970330740)  

---

## Executive Summary

This document provides a comprehensive overview of Zendesk's Platform Data Architecture from a **data engineering and product analytics perspective**. It covers:

- **PDD (Platform Data Domain)**: Core data infrastructure and pipelines
- **EDA (Enterprise Data Architecture)**: Enterprise-wide data strategy
- **Data Engineering**: Technical implementation and best practices
- **Product Analytics**: Data models supporting product insights

---

## Table of Contents

### Core Architecture
1. [Platform Data Architecture](#platform-data-architecture)
2. [Standard Objects](#standard-objects)
3. [Platform Data Registry](#platform-data-registry)
4. [Schema Onboarding](#schema-onboarding)
5. [Platform Schema & Metadata Working Group](#platform-schema--metadata-working-group)
6. [What exactly are ZObjects?](#what-exactly-are-zobjects)
7. [Platform Schema & Meta WG: Meeting Notes](#platform-schema--meta-wg-meeting-notes)
8. [Platform Schema & Meta WG: Requirements Gathering](#platform-schema--meta-wg-requirements-gathering)
9. [Platform Schema & Metadata WG: Proof of Concept](#platform-schema--metadata-wg-proof-of-concept)
10. [Platform Schema & Metadata WG: Research - Competitor analysis](#platform-schema--metadata-wg-research---competitor-analysis)
11. [Platform Schema & Metadata WG: POC - Schema Description Language](#platform-schema--metadata-wg-poc---schema-description-language)
12. [Platform Schema & Metadata WG: POC - Using service.yml to register PDA data sets](#platform-schema--metadata-wg-poc---using-serviceyml-to-register-pda-data-sets)
13. [Platform Schema & Metadata WG: POC - Data Catalog as a store for schema & metadata](#platform-schema--metadata-wg-poc---data-catalog-as-a-store-for-schema--metadata)
14. [Platform Schema & Metadata WG: Research - should ZD and customer-defined data types be described by the same system](#platform-schema--metadata-wg-research---should-zd-and-customer-defined-data-types-be-described-by-the-same-system)
15. [Platform Data Architecture Refresh, April 2021](#platform-data-architecture-refresh-april-2021)

### Related Documentation
16. [Export item by timestamp.html](#export-item-by-timestamphtml)
17. [How to drive testing at scale for cross functional projects](#how-to-drive-testing-at-scale-for-cross-functional-projects)
18. [Platform Data Architecture Program](#platform-data-architecture-program)
19. [Platform Data Architecture Program - Meeting minute](#platform-data-architecture-program---meeting-minute)
20. [2025-30-09 EDA, ZAP and B-Team discuss Lineage project](#2025-30-09-eda-zap-and-b-team-discuss-lineage-project)
21. [2025-08-08 EDA and Wollemi discuss Workday Data Location](#2025-08-08-eda-and-wollemi-discuss-workday-data-location)
22. [Re: ZDP_META for CADD](#re-zdp_meta-for-cadd)
23. [2025-07-29 Foundation CADD Alignment](#2025-07-29-foundation-cadd-alignment)
24. [ZDM Snowflake Access Details Page Performance Analysis](#zdm-snowflake-access-details-page-performance-analysis)
25. [Alation Feedback](#alation-feedback)
26. [Foundational Models - workshop - Decisions](#foundational-models---workshop---decisions)
27. [2025-07-02 EDA and B-Team Sync on DEV DBT ROLE](#2025-07-02-eda-and-b-team-sync-on-dev-dbt-role)
28. [Legacy Data Lake Deprecation](#legacy-data-lake-deprecation)
29. [2025-05-20 EDA and Wollemi discuss Feature Databases and Shared Sandboxes](#2025-05-20-eda-and-wollemi-discuss-feature-databases-and-shared-sandboxes)
30. [Re: Sandbox Sharing Rules and Restrictions](#re-sandbox-sharing-rules-and-restrictions)
31. [Re: Sandbox Sharing Rules and Restrictions](#re-sandbox-sharing-rules-and-restrictions)
32. [DEV_DBT_ROLE analysis](#dev_dbt_role-analysis)
33. [S3 Ingester](#s3-ingester)
34. [SOC2 Controls for User Roles](#soc2-controls-for-user-roles)
35. [ZDP Enablement Videos](#zdp-enablement-videos)
36. [Deleted Legacy Datastore Cost Savings](#deleted-legacy-datastore-cost-savings)
37. [ZDP: Cost Modelling](#zdp-cost-modelling)
38. [Integrating Pendo for to track MCT activation and adoption](#integrating-pendo-for-to-track-mct-activation-and-adoption)
39. [2022-07-28: Kick Off - ECR Migration](#2022-07-28-kick-off---ecr-migration)
40. [Re: 2023-04-26: Restoring JIG metrics to PDW](#re-2023-04-26-restoring-jig-metrics-to-pdw)
41. [Re: Ibises](#re-ibises)
42. [2022-02-26: Data Platform Knowledge Building - Zendesk Data Catalog](#2022-02-26-data-platform-knowledge-building---zendesk-data-catalog)
43. [2021-01-28: Platform Schema & Metadata Working Group](#2021-01-28-platform-schema--metadata-working-group)
44. [2020-06-27: Instacart Taskforce learnings - Shift PDW tasks from Production Shard DB](#2020-06-27-instacart-taskforce-learnings---shift-pdw-tasks-from-production-shard-db)
45. [2020-01-15: Engineering promotions](#2020-01-15-engineering-promotions)
46. [2019-07-03:PDW MySql User Survey and Deprecation](#2019-07-03pdw-mysql-user-survey-and-deprecation)
47. [Snowflake Access System: User Types](#snowflake-access-system-user-types)
48. [Onboarding Customers to Snowflake Access System](#onboarding-customers-to-snowflake-access-system)
49. [Snowflake Access System Phase 2: Data Owners](#snowflake-access-system-phase-2-data-owners)
50. [Legacy Tableau Migration to Snowflake](#legacy-tableau-migration-to-snowflake)
51. [Snowflake Access System: Worked Examples](#snowflake-access-system-worked-examples)
52. [Snowflake Access System](#snowflake-access-system)
53. [Finance Analysis Access Requirements](#finance-analysis-access-requirements)
54. [b081a6c8-c41e-4ba3-9bcd-2b74cd5df828.csv](#b081a6c8-c41e-4ba3-9bcd-2b74cd5df828csv)
55. [Archived: New Engineer Onboarding Guide](#archived-new-engineer-onboarding-guide)
56. [Re: Glossary](#re-glossary)
57. [Should we integrate the new PDA ingestion to the legacy Hudi pipeline](#should-we-integrate-the-new-pda-ingestion-to-the-legacy-hudi-pipeline)
58. [Store Data Lake L0 Raw Data in Zendesk Partition Based Buckets](#store-data-lake-l0-raw-data-in-zendesk-partition-based-buckets)
59. [PDA Customer Survey Results](#pda-customer-survey-results)
60. [Shein research](#shein-research)
61. [Platform Schema & Meta WG: Meeting Notes](#platform-schema--meta-wg-meeting-notes)
62. [Platform Schema & Meta WG: Requirements Gathering](#platform-schema--meta-wg-requirements-gathering)
63. [2018 Q2 Planning - Dev and Operations Estimates](#2018-q2-planning---dev-and-operations-estimates)
64. [Glossary](#glossary)
65. [FinOps-G&M Sync Up Meeting Minutes](#finops-gm-sync-up-meeting-minutes)
66. [Intro to Scala training waitlist](#intro-to-scala-training-waitlist)
67. [2014-08-18 Program Management Tech Talk.pdf](#2014-08-18-program-management-tech-talkpdf)
68. [Engineering Tech Talks archive](#engineering-tech-talks-archive)
69. [Sample Technical Interview Questions](#sample-technical-interview-questions)
70. [Aurora Customer Summary](#aurora-customer-summary)
71. [Global Event Bus (GEB) run book](#global-event-bus-geb-run-book)
72. [Aurora Technical Discovery](#aurora-technical-discovery)
73. [Bunyip](#bunyip)
74. [Aurora Compliance Discovery](#aurora-compliance-discovery)
75. [Aurora Security Discovery](#aurora-security-discovery)
76. [Channels - Architecture Document](#channels---architecture-document)
77. [Foundation - Storage - Glider](#foundation---storage---glider)
78. [Standard Objects](#standard-objects)
79. [Data storage @ Zendesk](#data-storage--zendesk)
80. [ObjectStore Operator (S3)](#objectstore-operator-s3)
81. [Ticket Platform Onboarding Plan](#ticket-platform-onboarding-plan)
82. [Engineering Review](#engineering-review)
83. [I am a Reliability Champion](#i-am-a-reliability-champion)
84. [Clickhouse Operator Plan](#clickhouse-operator-plan)
85. [Foundation Data - Analytics](#foundation-data---analytics)
86. [Streamlit in ZDP: Write access](#streamlit-in-zdp-write-access)
87. [Frontend Usage Instrumentation POC Handover (22nd Oct 2025)](#frontend-usage-instrumentation-poc-handover-22nd-oct-2025)
88. [Fullstack Onboarding](#fullstack-onboarding)
89. [015 - Storing Platform Feature State Tables in Aurora](#015---storing-platform-feature-state-tables-in-aurora)
90. [Spike - Adding a Rich Text Editor in Lotus for AI Agent Simple Setup](#spike---adding-a-rich-text-editor-in-lotus-for-ai-agent-simple-setup)
91. [[WIP] Frontend Product Usage Data Instrumentation Discovery](#wip-frontend-product-usage-data-instrumentation-discovery)
92. [Gmail Connector - Operability checklist](#gmail-connector---operability-checklist)
93. [Attribute for Zendesk-1.pdf](#attribute-for-zendesk-1pdf)
94. [[ADR] Gmail Sending - ESG](#adr-gmail-sending---esg)
95. [Granular Permissions Team Charter](#granular-permissions-team-charter)
96. [Bootstrap metadata and lineage tables](#bootstrap-metadata-and-lineage-tables)
97. [Classic User API - Reliability](#classic-user-api---reliability)
98. [Billing Growth](#billing-growth)
99. [Looker Dashboards and ZDP access](#looker-dashboards-and-zdp-access)
100. [Building a Test Strategy for a Program](#building-a-test-strategy-for-a-program)
101. [Supercharge Setup Phase 2 - RFC](#supercharge-setup-phase-2---rfc)
102. [Global Event Bus Delivery](#global-event-bus-delivery)
103. [Alation Slowness & Capacity Escalation – Evidence Summary](#alation-slowness--capacity-escalation--evidence-summary)
104. [Communication Templates](#communication-templates)
105. [Staff service development tips and tricks (& calling production)](#staff-service-development-tips-and-tricks--calling-production)
106. [Weekly Engineering Meeting](#weekly-engineering-meeting)
107. [AI agent simple setup documentation](#ai-agent-simple-setup-documentation)
108. [Technical Design - Offers in OES](#technical-design---offers-in-oes)
109. [Supercharge Setup Phase 1 - RFC](#supercharge-setup-phase-1---rfc)
110. [SPIKE: Cleansed Layer Completeness Checks using Formatted Layer](#spike-cleansed-layer-completeness-checks-using-formatted-layer)
111. [How to respond to Snowflake incidents?](#how-to-respond-to-snowflake-incidents)
112. [009 - Ticket Platform Field Migrations](#009---ticket-platform-field-migrations)
113. [Re: Platform Data Architecture Program](#re-platform-data-architecture-program)
114. [Platform Data Architecture](#platform-data-architecture)
115. [Platform Data Registry](#platform-data-registry)
116. [Dark Knight](#dark-knight)
117. [Architecture Directions 2020-2022](#architecture-directions-2020-2022)
118. [DevLeads Summit 2014](#devleads-summit-2014)
119. [One Zendesk: Strategy](#one-zendesk-strategy)
120. [ProgInScala3ed.pdf](#proginscala3edpdf)
121. [Ticket Domain Events](#ticket-domain-events)
122. [Quick Assist](#quick-assist)
123. [Repairing the Incomplete Backfill of Archived Tickets](#repairing-the-incomplete-backfill-of-archived-tickets)
124. [Data Masking GA: Drive E2E Testing](#data-masking-ga-drive-e2e-testing)
125. [[Research] How Yuki Works ?](#research-how-yuki-works-)
126. [Attribute Data Flow.pdf](#attribute-data-flowpdf)
127. [Attribute Sensor Overview.pdf](#attribute-sensor-overviewpdf)
128. [[WIP] Attrib.io Proof of Concept](#wip-attribio-proof-of-concept)
129. [Ticket Platform Field Deactivation](#ticket-platform-field-deactivation)
130. [014 - Platform Features State Table Schema](#014---platform-features-state-table-schema)
131. [ML EAP (Production) - Test run 7 (25773741)](#ml-eap-production---test-run-7-25773741)
132. [Ticket Platform Fields - On-call Runbook](#ticket-platform-fields---on-call-runbook)
133. [Hidden Ticket Platform Fields - On-Call Runbook](#hidden-ticket-platform-fields---on-call-runbook)
134. [ML EAP - Test run 6 (20250918)](#ml-eap---test-run-6-20250918)
135. [ML EAP - Test run 5](#ml-eap---test-run-5)
136. [ML EAP - Test run 4](#ml-eap---test-run-4)
137. [ML EAP - Test run 3](#ml-eap---test-run-3)
138. [ML EAP - Test run 2](#ml-eap---test-run-2)
139. [013 - Installer - install and update (migrate) behavior](#013---installer---install-and-update-migrate-behavior)
140. [Review process for dataset collection and security classification](#review-process-for-dataset-collection-and-security-classification)
141. [012 - Platform Fields will not support tag synchronization](#012---platform-fields-will-not-support-tag-synchronization)
142. [Documentation - How Tos](#documentation---how-tos)
143. [Theming Center Refactoring Plan](#theming-center-refactoring-plan)
144. [011 - Ticket Platform Field and Option Inactivation](#011---ticket-platform-field-and-option-inactivation)
145. [How to Write a Funfiller Backfill](#how-to-write-a-funfiller-backfill)
146. [CDC Ingestion into ZDP via Snowpipe Streaming](#cdc-ingestion-into-zdp-via-snowpipe-streaming)
147. [Acryl: Previous Data Catalog Solution](#acryl-previous-data-catalog-solution)
148. [Data Quality integration request: Legacy epic status, unified solution approach, and effort recommendation](#data-quality-integration-request-legacy-epic-status-unified-solution-approach-and-effort-recommendation)
149. [010 - Hidden Fields v1](#010---hidden-fields-v1)
150. [How to integrate with ZDP account moves?](#how-to-integrate-with-zdp-account-moves)
151. [Escape v2 Runbook](#escape-v2-runbook)
152. [Logging in depth](#logging-in-depth)
153. [Foundation Interface Assessment](#foundation-interface-assessment)
154. [mail-parsing-queue](#mail-parsing-queue)
155. [Pod validation](#pod-validation)
156. [S3v1 Final Battle](#s3v1-final-battle)
157. [Spike: A catchup job to fetch the missed metadata](#spike-a-catchup-job-to-fetch-the-missed-metadata)
158. [Solution Options for Frontend Instrumentation](#solution-options-for-frontend-instrumentation)
159. [Detect Derivable relationships](#detect-derivable-relationships)
160. [2025-10-15 Foundation Data meets Edge on LDL EOL](#2025-10-15-foundation-data-meets-edge-on-ldl-eol)
161. [Cleansed Models Account Move Integration Guide](#cleansed-models-account-move-integration-guide)
162. [Optimization runbook - TICKET_FIELDS_STRING Filtered tables](#optimization-runbook---ticket_fields_string-filtered-tables)
163. [Optimization runbook - TICKET_FIELD_CHANGES Filtered tables](#optimization-runbook---ticket_field_changes-filtered-tables)
164. [Support S3V2 External in ZDM](#support-s3v2-external-in-zdm)
165. [Support SQS External in ZDM](#support-sqs-external-in-zdm)
166. [[2025 August] CDC Snowpipe Streaming Post Release Cost Review](#2025-august-cdc-snowpipe-streaming-post-release-cost-review)
167. [Alation Analytics ETL](#alation-analytics-etl)
168. [Re: Supercharge Setup Phase 1 - RFC](#re-supercharge-setup-phase-1---rfc)
169. [CDC Snowpipe Streaming Cutover Procedure](#cdc-snowpipe-streaming-cutover-procedure)
170. [Snowpipe Streaming Escalated Response](#snowpipe-streaming-escalated-response)
171. [Sparrow Job Overview](#sparrow-job-overview)
172. [Migrating Monitor off Legacy Data Lake buckets](#migrating-monitor-off-legacy-data-lake-buckets)
173. [ZDP Compliance - Account Moves](#zdp-compliance---account-moves)
174. [Ongoing Maintenance](#ongoing-maintenance)
175. [TM-Spinnaker Plugin Integration for CS teams](#tm-spinnaker-plugin-integration-for-cs-teams)
176. [System Overview](#system-overview)
177. [Support SQS on ZDM](#support-sqs-on-zdm)
178. [2025-05-20 Edge and Wollemi](#2025-05-20-edge-and-wollemi)
179. [Snowflake Row Metadata Feature to Replace Ingest Timestamp](#snowflake-row-metadata-feature-to-replace-ingest-timestamp)
180. [Snowflake: Security Data Lake](#snowflake-security-data-lake)
181. [Re: Managed Data Pipeline Tasks](#re-managed-data-pipeline-tasks)
182. [Managed Data Pipeline Tasks](#managed-data-pipeline-tasks)
183. [Writing a PDA Compliant ZDP Pipeline in Classic](#writing-a-pda-compliant-zdp-pipeline-in-classic)
184. [2025-05-23: Dev environment vulnerabilities in the OpEx dashboard](#2025-05-23-dev-environment-vulnerabilities-in-the-opex-dashboard)
185. [[2025 April]  PDA Snowpipe Streaming First Release Cost Review](#2025-april--pda-snowpipe-streaming-first-release-cost-review)

---

# Core Platform Data Architecture

## Platform Data Architecture

**Page ID:** 970330740  
**Version:** 9  
**Last Updated:** 2023-04-07  
**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/970330740](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/970330740)  

#### Data Engineering Context

*This section covers platform-level data engineering concepts relevant to PDD and EDA initiatives.*

# Updates

Platform Data Architecture Refresh, April 2021

# Background

Over the past few years, Zendesk has been transitioning from a collection of more or less integrated products into a cohesive suite with unified, extensible workflows, centralised administration, and shared notions of users and other core concepts. (See the [_One Zendesk strategy_](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/786935424/One+Zendesk+Strategy) doc written in late 2019.) We are more tightly and deeply integrating data sets originating in one application into other applications and features, existing as well as new.

Additionally, as we seek to evolve as a platform for Enterprise solutions, we will need to present not a fragmented landscape of domain models that make sense only within their respective products, but rather a cohesive set of core models, covering the breadth of our offerings, coupled with powerful practical capabilities that allow ourselves and third parties to efficiently integrate, extend, and build upon the Zendesk Platform.

#   
Data at the Centre

2falseleftrich10821f4b3-8b30-48fa-b644-beaf428795acConfluence:2083817226700dc441e2d-7f53-4541-a802-3aa1415fe1a3dc441e2d-7f53-4541-a802-3aa1415fe1a3|103589275|970330740|byzlXLxITB14pfx97hwbRCc0+3stHGVpXCMoouHedeQ=1584697098296500

In order to reach our Platform goals, we need to move to an architecture that puts our core data sets at the center and enables practical applications to be built using powerful, scalable primitives that take full advantage of those data sets.

Platform Data Architecture can be understood as the formal way we think about data in the Platform. To date we have identified three main pillars (and more may be described later). 

## Standard Objects 

These a set of **native types** defined and owned by Zendesk as well as the **collection of data** conforming to those types. The Platform Data Architecture defines a set of **standard access patterns** to use Standard Objects within the Zendesk platform. Standard Objects are published to Entity Streams and can be consumed by multiple services from these streams.

## Standard Events

These a set of **native events** defined, published and owned by Zendesk. The Platform Data Architecture will define a set of **standard access patterns** to use Standard Events within the Zendesk platform. Standard Events are published to Event Streams and can be consumed by multiple services from these streams.

## Custom Objects 

These are a set of types defined and created by customers or integrators (see [the documentation](https://develop.zendesk.com/hc/en-us/articles/360002073807-Custom-objects-handbook)). These custom objects, when created, can be associated with Standard Objects without our platform. This allows our platform partners to extend Zendesk data with their own data types. 

2falseleftrich1ae8fcdbf-6cb6-4026-84c3-496537be1511Confluence:20838172267004c6144c2-2c84-4ec1-ac27-47ff2565fcb44c6144c2-2c84-4ec1-ac27-47ff2565fcb4|103589275|970330740|Grxp/AXBEWTDzuSyfAvvYMJXs6oAeeWZ9cz0IMFZZoI=1584697162541500

# Documentation and Standards

Docs for PDA now live in the TechMenu (VPN required) at [Platform Data Architecture (PDA) Standards](https://techmenu.zende.sk/standards/pda-standards/).

We also have the Platform Data Registry Confluence page, where we list the PDA-related types that have been implemented so far. As part of the Zendesk Data and Analytics Transformation initiative, these will eventually be moved to our Data Catalog.

---

### Standard Objects

**Page ID:** 829821236  
**Version:** 13  
**Last Updated:** 2025-07-28  
**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/829821236](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/829821236)  

#### Data Engineering Context

This documentation is pending an update and migration to the TechMenu as a Standard in 2025-H2. If you want to read other (stale) definitions, see:

  1. https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6248464471/What+exactly+are+ZObjects

  2. <https://docs.google.com/presentation/d/1yU9ApsiLsWyM5XuunITchQSATwlRrsK9mu1qm2T1G58/edit?slide=id.g7d7fef748e_0_220#slide=id.g7d7fef748e_0_220>

  3. <https://techmenu.zende.sk/adrs/platform-data-architecture-zendesk-objects/>




# What is a Standard Object?

Standard Objects are a set of **native types** defined and owned by Zendesk, the **collection of data** conforming to those types along with a set of **standard access patterns** to use this data within the Zendesk platform.

In practice, Standard Objects are:

  * A set of native Zendesk types, each represented by a well-known schema, which are easily discoverable to Zendesk engineers.

  * An API associated with each type to allow write operations to create or mutate or read instances of the type. This API allows us to surface a Standard Object in the Zendesk platform.

  * A set of **compacted** Kafka topics, one per type (Ticket, Article, Deal etc.) that provide an [entity stream](https://techmenu.zende.sk/standards/events/#entity-streams) firehose.

  * A "collections" API which provides a mechanism to bulk-load all entities associated with a particular Standard Object type **for a single account only**.




# What is a Standard Object _not_?

  * A Standard Object is _not_ a product offering, we will not be selling or monetising Standard Objects directly, like we do today with Custom Objects. 

  * Some of the Standard Object attributes (e.g. has an entity stream) are really **engineering standards and mechanisms** to allow us **share data between internal services** more effectively, and to provide a **foundation** to build other **shared** platform capabilities like Search. 

  * **NEW!** A Standard Object is not an event, it is only an entity. We are working on defining what a Standard Event is, so stay tuned.




See also: Standard _  Objects for Engineers - _[_presentation_](https://docs.google.com/presentation/d/1yU9ApsiLsWyM5XuunITchQSATwlRrsK9mu1qm2T1G58/edit#slide=id.g7d7fef748e_0_0) _,_[_recording_](https://drive.google.com/file/d/1iiPkPEw5n8vIK4bUA2FO4HcOOZMJuNwQ/view)

# So why are Standard Objects important to us? 

### Data at the Core 

Following the One Zendesk strategy, Zendesk will transition from a collection of more or less integrated products into a cohesive suite with unified, extensible workflows, centralised administration, and shared notions of users and other core concepts. We will need to more tightly and deeply integrate data sets originating in one application into other applications and features, existing as well as new.

Additionally, as we seek to become a platform for Enterprise solutions, we will need to present not a fragmented landscape of domain models that make sense only within their respective products, but rather a cohesive set of standard models, covering the breadth of our offerings, coupled with powerful practical capabilities that allow ourselves and third parties to efficiently integrate, extend, and build upon the Zendesk Platform. In the view of the architecture team, our data sets are our primary competitive advantage as we push into Platform.

In order to reach these goals, we need to move to an architecture that puts the standard data sets at the centre and enables practical applications to be built using powerful, scalable primitives that take full advantage of those data sets. 

Standard Objects describes the standards we expect this data to adhere to, as well as the mechanisms to access this data.

### Building Platform Capabilities

To align with the One Zendesk strategy we need a standardised way to share data between data producers and many consumers in a way that allows us to scale the number of producers and consumers over time. Sharing data in this way allows us concentrate on leveraging capabilities built and run in one place. Critically once the capability is in place, the standardisation in place allows other sources of data to adopt the Standard Objects conventions and feed into that capability too, at a low cost of onboarding. 

The goal is to avoid bespoke integrations between data producers and consumers which are costly to build and maintain and don't address our goal of unifying our platform around a common set of data types and capabilities. Instead we extract the maximum leverage from these shared capabilities and focus the rest of our energy on other work. 

### Reliability & Decoupling

Our applications are moving away from being logically and temporally coupled, communicating over HTTP, to being decoupled and asynchronous, communicating through events. We are pursuing these changes in support of increased reliability, adapting to the continued growth of our engineering teams and as a way to enable new capabilities such as workflow and platform integration inline with the One Zendesk strategy. 

The Standard Objects strategy represents a standardisation of our [event and entity stream approach](https://techmenu.zende.sk/standards/events/) to date. In adopting Standard Objects we expect to see applications materialise and maintain views of another application's data based on standardised and easily discoverable entity streams, thus becoming more resilient and robust.

We also expect to see downstream applications that need to observe changes to another application to do so through subscription to common Standard Objects topics, rather than having the upstream application have to notify every (known) downstream consumer of changes through HTTP calls. This will result in an event driven architecture where there are natural buffers in places to guard against failures and outages. 

Of course this also means we are going to be dealing with an increasingly eventually-consistent world, and that will bring its own challenges. But we feel that at the scale we are operating at, we should make this trade-off at this time. 

# Relationship to other Platform concepts (Standard Events, Custom Objects etc.)

See Platform Data Architecture.

# Further Information

  * #platform-data-architecture in Slack

  * Platform Data Architecture Program

---

### Platform Data Registry

**Page ID:** 952048005  
**Version:** 82  
**Last Updated:** 2025-01-23  
**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/952048005](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/952048005)  

#### Data Engineering Context

*This section covers platform-level data engineering concepts relevant to PDD and EDA initiatives.*

For now, this is where we will list the types available for use in our platform. These will include Standard Objects, Core Events, Custom Objects, and other types we introduce in the future. 

**Platform Data Category 1**| **Name**| **ZRN Type Prefix**| **Schema Location**| **Checklist Link**| **Kafka topic**| **Kafka key**  
| **Kafka headers**| **Approval Details**| **Estimated Metrics**  
---|---|---|---|---|---|---|---|---|---  
Standard Object| Ticket| zen:ticket| | | | | | |   
Standard Object| User| zen:user| | | | | | |   
Standard Object| User Authentication| | [platform/standard/users/user_authentication_events.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/standard/users/user_authentication_events.proto)| | `platform.standard.user_authentication_events`| | | [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/736)| (as of 13th Nov 2020)  
**# events/entities** 520,000 per pod per day**Avg message size**  
100 bytes**Throughput**  
360/min  
Standard Object| Article| zen:article| [platform/standard/article.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/standard/articles/article.proto) | [Checklist](https://docs.google.com/document/d/1MXPxvIaCSTuwDIUCZBOvws-neIfsB-LCccKzq8Wp8hc/edit?usp=sharing)| `platform.core.articles`| TBC: `"account_id/entity_id"` where `entity_id` is a concatenation of article id and locale for a unique identifier| | |   
Standard Object | Community Post| zen:community_post| [platform/standard/community_posts/community_post.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/standard/community_posts/community_post.proto) | [Checklist](https://docs.google.com/document/d/1MXPxvIaCSTuwDIUCZBOvws-neIfsB-LCccKzq8Wp8hc/edit?usp=sharing)| `platform.standard.community_posts`| TBC:`"account_id/community_post_id"`| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| |   
Standard Object| Deal| zen:deal| [platform/core/deal.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/deal.proto) | [Checklist](https://docs.google.com/document/d/1AMaeQqRFegiJ80A4dXxCjRy97K4ATYHACii3_e_Ief8/edit)| `mirror.platform.core.deals`| `account_id/entity_id`

  * `entity_id` \- Deal ID, autoincremented PK from database

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/583)| (as of 19th Aug 2020)  
**# events/entities**  
`29,475,632`**Avg message size**  
Max limit of 2KB per deal**Throughput**  
Up-to of 1000 for all accounts per minute.   
Standard Object| Sales Pipeline| | [platform/core/sales_pipeline.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/sales_pipeline.proto)| [Checklist](https://docs.google.com/document/d/1caS6wDxKlbY4nFhY8bqxeT4Qg74dRodeCn3HaWn83zI/edit)| `mirror.platform.core.sales_pipelines`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR ](https://github.com/zendesk/zendesk_protobuf_schemas/pull/614)| (as of 30th Sep 2020)  
**# events/entities**  
`12,415,829`**Avg message size**  
Max limit of 700B per deal**Throughput**  
Up-to of 2000 for all accounts per minute.   
Standard Object| Sales Pipeline Stage| | [platform/core/sales_pipeline_stage.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/sales_pipeline_stage.proto)| [Checklist](https://docs.google.com/document/d/1JLByagmrrDzuNleL4ynzPRFpLE2p8-rTtBVzIq4sSzc/edit)| `mirror.platform.core.sales_pipeline_stages`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR ](https://github.com/zendesk/zendesk_protobuf_schemas/pull/614)| (as of 30th Sep 2020)  
**# events/entities**  
`8,632,584`**Avg message size**  
Max limit of 700B per deal**Throughput**  
Up-to of 1500 for all accounts per minute.  
Standard Object| Deal Unqualified Reason| | [platform/core/deal_unqualified_reason.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/deal_unqualified_reason.proto)| [Checklist](https://docs.google.com/document/d/1xhBzpbfMLu0Vc1u98M0ZA9ZQfjpFVtKOJ3Ulub1QlMw/edit)| `mirror.platform.core.deal_unqualified_reasons`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/610)| (as of 30th Sep 2020)  
**# events/entities**  
`5,104,331`**Avg message size**  
Max limit of 700B per deal**Throughput**  
Up-to of 1000 for all accounts per minute.  
Standard Object| Deal Loss Reason| | [platform/core/deal_loss_reason.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/deal_loss_reason.proto)| [Checklist](https://docs.google.com/document/d/1TglAjnRz5ivu1KewNlNs0VZvJpAw3J_pkDAsJWp0VYk/edit)| `mirror.platform.core.deal_loss_reasons`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/610)| (as of 30th Sep 2020)  
**# events/entities**  
`4,382,555`**Avg message size**  
Max limit of 700B per deal**Throughput**  
Up-to of 5 for all accounts per minute.  
Standard Object| Deal Source| | [platform/core/deal_source.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/deal_source.proto) | [Checklist](https://docs.google.com/document/d/1OGdzYXNQBV4mmPWkCIePFlCyfls4aKoPumVZPEosEy8/edit)| `mirror.platform.core.deal_sources`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/610)| (as of 30th Sep 2020)  
**# events/entities**  
`4,893,848`**Avg message size**  
Max limit of 700B per deal**Throughput**  
Up-to of 5 for all accounts per minute.  
Standard Object| Lead| | [platform/core/lead.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/lead.proto) | [Checklist](https://docs.google.com/document/d/1ZGzvJCwfMWxbC4dqSwEXP1dgIRoxpGT7ET6X94Q0spM/edit)| `mirror.platform.core.leads`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/611)| (as of 26th Oct 2020)  
**# events/entities**  
`138,584,727`**Avg message size**  
Max limit of 700B per lead**Throughput**  
Up-to of 2000 for all accounts per minute.  
Standard Object| Lead Source| | [platform/core/lead_source.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/lead_source.proto) | [Checklist](https://docs.google.com/document/d/1N1mthZEV8CZp1vixIazWmL9jCwRNXeeq08tUcQYbTc0/edit)| `mirror.platform.core.lead_sources`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/611)| (as of 26th Oct 2020)  
**# events/entities**  
`1,016,593`**Avg message size**  
Max limit of 700B per lead**Throughput**  
Up-to of 5 for all accounts per minute.  
Standard Object| Lead Status| | [platform/core/lead_status.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/lead_status.proto) | [Checklist](https://docs.google.com/document/d/14hp_gCAcZ-8txSFKdzmgEiekTqcseM7Tu8AVOthd3oc/edit)| `mirror.platform.core.lead_statuses`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/611)| (as of 26th Oct 2020)  
**# events/entities**  
`2,784,059`**Avg message size**  
Max limit of 700B per status**Throughput**  
Up-to of 5 for all accounts per minute.  
Standard Object| Lead Status Change| | [platform/standard/leads/lead_status_change.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/standard/leads/lead_status_change.proto)| [Checklist](https://docs.google.com/document/d/1afFRkppmhb4VUV6zuhFGorVz53ppomXGwO9zdKr2Jao/edit?usp=sharing)| `mirror.platform.core.lead_status_changes`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/779)|   
Standard Object| Lead Unqualified Reason| | [platform/standard/leads/lead_unqualified_reason.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/standard/leads/lead_unqualified_reason.proto)| [Checklist](https://docs.google.com/document/d/1563nBQlOi0TTbC2O1XPR7UcVtqp4oRXu4KnhtL-ZWVk/edit?usp=sharing)| `mirror.platform.core.lead_unqualified_reasons`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/685)|   
Standard Object| Lead Conversion| | [platform/core/lead_conversion.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/lead_conversion.proto) | [Checklist](https://docs.google.com/document/d/13i7_yePCt9Fn44WOfv-H1Wj0pvslfTN9aDlzAuTWTFE/edit)| `mirror.platform.core.lead_conversions`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/701)| (as of 26th Oct 2020)  
**# events/entities**  
`9,599,192`**Avg message size**  
Max limit of 700B per message**Throughput**  
Up-to of 1000 for all accounts per minute.  
Standard Object| Contact| zen:contact| [platform/core/contact.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/contact.proto) | [Checklist](https://docs.google.com/document/d/1rO8syY5-PCqOtm40zmUH11utRwRviqJ_hbMInvP4OSg/edit)| `mirror.platform.core.contacts`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/706)| (as of 26th Oct 2020)  
**# events/entities**  
`123,935,440`**Avg message size**  
Max limit of 700B per message**Throughput**  
Up-to of 3000 for all accounts per minute.  
Standard Object| Sell Tag| | [platform/core/sell_tag.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/sell_tag.proto) | [Checklist](https://docs.google.com/document/d/1BQx1Nto3WrNYzlHrvRfUSaLgM3iivziURUePL1mFDXE/edit)| `mirror.platform.core.sell_tags`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/608)| (as of 30th Sep 2020)  
**# events/entities**  
`3,196,350`**Avg message size**  
Max limit of 700B per message**Throughput**  
MissingRed  
Standard Object| Sell Custom Field| | [platform/core/sell_custom_field.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/sell_custom_field.proto) | [Checklist](https://docs.google.com/document/d/1BQx1Nto3WrNYzlHrvRfUSaLgM3iivziURUePL1mFDXE/edit)| `mirror.platform.core.sell_custom_fields`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/608)| (as of 30th Sep 2020)  
**# events/entities**  
`2,726,198`**Avg message size**  
MissingRed**Throughput**  
MissingRed  
Standard Object| Sell Team| | [platform/core/sell_team.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/sell_team.proto) | [Checklist](https://docs.google.com/document/d/1IM-dhD6uwBPyq2kfAaRXRh4JvHlqmOHqOBPzEgRX5nk/edit)| `mirror.platform.core.sell_teams`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/613)| as of 30th Sep 2020)  
**# events/entities**  
`76,829`**Avg message size**  
Max limit of 700B per message**Throughput**  
MissingRed  
Standard Object| Sell Group| | [platform/core/sell_group.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/sell_group.proto) | [Checklist](https://docs.google.com/document/d/1I2Xq2RunBDk7sDzbja5o-akCGVmPlpVoFM5MPFv2K8A/edit)| `mirror.platform.core.sell_groups`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/613)| as of 30th Sep 2020)  
**# events/entities**  
`17,053`**Avg message size**  
Max limit of 700B per message**Throughput**  
MissingRed  
Standard Object| Sell User| | [platform/core/sell_user.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/sell_user.proto) | [Checklist](https://docs.google.com/document/d/14j6mWJHGBVwBtGFtCd12olJJfBByfWOY2mBKVuKZBJM/edit)| `mirror.platform.core.sell_users`| `account_id/entity_id`

  * `entity_id` \- autoincremented PK of database entity

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/613)| as of 30th Sep 2020)  
**# events/entities**  
`2,049,902`**Avg message size**  
Max limit of 700B per message**Throughput**  
MissingRed  
Custom Object| Custom Object Record| zen:custom_object:$custom_object_key| [custom_objects/v2/custom_object_record.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/custom_objects/v2/custom_object_record.proto) | | `platform.custom_objects.records`| `account_id/entity_id` where `entity_id` is a string ULID representation of a CustomObjectRecordID| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/1441)|   
Custom Object| Custom Object Record | zen:custom_object:$custom_object_key:$record_id| [custom_objects/v2/custom_object_record_events.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/custom_objects/v2/custom_object_record_events.proto)| | `support.custom-object-record-events`| `account_id/entity_id` where `entity_id` is a string ULID representation of a CustomObjectRecordID| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/2404)|   
Custom Object| Sunshine Profile| | [platform/sunshine/profile.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/sunshine/profile.proto) | [Checklist](https://docs.google.com/document/d/13eC22JgRixSnHvTbEpGsQz7A1GGKj_elReU4rQr9vRA/edit#heading=h.lctd3jevdyr0)| platform.sunshine.profiles| `account_id/entity_id` where `entity_id` is a string ULID representation of a ProfileID| `ZENDESK_ACCOUNT_ID`  
`ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/505)| (as of 11th May 2020)  
**# events/entities**  
25,764,710 **Avg message size**  
Max limit of 2KB per profile**Throughput**  
Max of 1000 per account per minute.   
Custom Object| Sunshine Event| | [platform/sunshine/event.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/sunshine/event.proto)| [Checklist](https://docs.google.com/document/d/1cCB4CdEXCqkx7Dn7neiqIyqrgl9it_eb9UI8MTE6mrI/edit#heading=h.lctd3jevdyr0)| platform.sunshine.events| `account_id/entity_id` where `entity_id` is a string ULID representation of a EventID| `ZENDESK_ACCOUNT_ID`  
`ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/502)| (as of 12th May 2020)  
**# events/entities**  
380,834,043**Avg message size**  
Max limit of 2KB per event**Throughput**  
Max of 500 per account per minute.  
* Internal events throughput estimation is WIP  
Standard Event| Answer Bot Flow Director Activity Events| | [answer_bot/guided_flows/flow_director/activity_events.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/answer_bot/guided_flows/flow_director/activity_events.proto) | [Checklist](https://docs.google.com/document/d/1xTQktZSwuG8Cm39hOcke7yy-WXaJB8vmzWXyHWMMgeg/edit#)| `flow_director.conversations.activity`| `account_id/header.message_id``message_id` in header is generated ULID| `ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/data-lake-v2/pull/77)| (as of 03 March 2021)**# events**  
73,018 per day across all pods**Avg message size**  
600 bytes**Throughput**  
73,018 per day across all pods  
Standard Event| Answer Bot Flow Director Reporting Events| | [answer_bot/guided_flows/flow_director/reporting_events.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/answer_bot/guided_flows/flow_director/reporting_events.proto) | [Checklist](https://docs.google.com/document/d/1X8uW51Bn14VNIQjzCn-DGb-qqALowNs1CcqBwsPHJ3U/edit?usp=sharing)| `flow_director.conversations.reporting`| `account_id/header.message_id``message_id` in header is generated ULID| `ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/collections-service/pull/250)| (as of 23 June 2021)[Estimated](https://docs.google.com/spreadsheets/d/1HbBWOj7xV_KR4zspXVBktJdFmGO4gOvekHSds6m89HM/edit#gid=1757679128) based on actual activity events data**# events**  
87,651 per day across all pods**Avg message size**  
200 bytes**Throughput**  
87,651 per day across all pods  
Standard Object| Trigger Entity| | [support/business_rules/trigger.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/support/business_rules/trigger.proto) | TODO| `support.trigger_entities`| `account_id/entity_id` where `entity_id` is autoincremented PK of database entity| `ZENDESK_ACCOUNT_ID`  
`ZENDESK_PB_HEADER`| TODO| **# entities**  
? per day across all pods**Avg message size**  
? bytes**Throughput**  
? per day across all pods  
Standard Event| [Help Center Searched](https://github.com/zendesk/help_center/blob/master/doc/events/activity/search.md#help_center_searched)| | [guide/activity/help_center_searched.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/help_center_searched.proto) | TODO| `help_center.activity.help_center_searched`| `account_id/message_id` | `ZENDESK_ACCOUNT_ID` | | As of 23. Mar 2022 based on [this](https://zendesk.datadoghq.com/dashboard/pp2-wcr-gqg/help-center---activity-events-piratos?tpl_var_event=help_center.activity.help_center_searched&from_ts=1645435228208&to_ts=1648027228208&live=true)**# events**  
2.5M per day across all pods**Avg message size**  
~600 bytes**Throughput**  
2.5M per day across all pods  
Standard Event| [Article Search Result Clicked](https://github.com/zendesk/help_center/blob/master/doc/events/activity/search.md#article_search_result_clicked)| | [guide/activity/article_search_result_clicked.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/article_search_result_clicked.proto) | TODO| `help_center.activity.article_search_result_clicked`| `account_id/message_id` | `ZENDESK_ACCOUNT_ID` | | As of 23. Mar 2022 based on [this](https://zendesk.datadoghq.com/dashboard/pp2-wcr-gqg/help-center---activity-events-piratos?tpl_var_event=help_center.activity.help_center_searched&from_ts=1645435228208&to_ts=1648027228208&live=true)**# events**  
800K per day across all pods**Avg message size**  
~450 bytes**Throughput**  
800K per day across all pods  
Standard Event| [Community Post Search Result Clicked](https://github.com/zendesk/help_center/blob/master/doc/events/activity/search.md#community_post_search_result_clicked)| | [guide/activity/community_post_search_result_clicked.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/community_post_search_result_clicked.proto) | TODO| `help_center.activity.community_post_search_result_clicked`| `account_id/message_id` | `ZENDESK_ACCOUNT_ID` |  | As of 23. Mar 2022 based on [this](https://zendesk.datadoghq.com/dashboard/pp2-wcr-gqg/help-center---activity-events-piratos?tpl_var_event=help_center.activity.help_center_searched&from_ts=1645435228208&to_ts=1648027228208&live=true)**# events**  
20K per day across all pods**Avg message size**  
~450 bytes**Throughput**  
20K per day across all pods  
Standard Event| [Answers Suggested](https://github.com/zendesk/help_center/blob/master/doc/events/activity/search.md#answers_suggested)| | [guide/activity/answers_suggested.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/answers_suggested.proto) | TODO| `help_center.activity.answers_suggested`| `account_id/message_id` | `ZENDESK_ACCOUNT_ID` | | As of 23. Mar 2022 based on [this](https://zendesk.datadoghq.com/dashboard/pp2-wcr-gqg/help-center---activity-events-piratos?tpl_var_event=help_center.activity.help_center_searched&from_ts=1645435228208&to_ts=1648027228208&live=true)**# events**  
3.2M per day across all pods**Avg message size**  
~300 bytes**Throughput**  
3.2M per day across all pods  
Standard Event| [Article Instant Search Result Clicked](https://github.com/zendesk/help_center/blob/master/doc/events/activity/search.md#article_instant_search_result_clicked)| | [guide/activity/article_instant_search_result_clicked.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/article_instant_search_result_clicked.proto) | TODO| `help_center.activity.article_instant_search_result_clicked`| `account_id/message_id` | `ZENDESK_ACCOUNT_ID` | | As of 23. Mar 2022 based on [this](https://zendesk.datadoghq.com/dashboard/pp2-wcr-gqg/help-center---activity-events-piratos?tpl_var_event=help_center.activity.help_center_searched&from_ts=1645435228208&to_ts=1648027228208&live=true)**# events**  
267K per day across all pods**Avg message size**  
~350 bytes**Throughput**  
267K per day across all pods  
Standard Event| [Instant Search Suggestions Viewed](https://github.com/zendesk/help_center/blob/master/doc/events/activity/search.md#instant_search_suggestions_viewed)| | [guide/activity/instant_search_suggestions_viewed.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/instant_search_suggestions_viewed.proto) | TODO| `help_center.activity.instant_search_suggestions_viewed`| `account_id/message_id` | `ZENDESK_ACCOUNT_ID` | | As of 23. Mar 2022 based on [this](https://zendesk.datadoghq.com/dashboard/pp2-wcr-gqg/help-center---activity-events-piratos?tpl_var_event=help_center.activity.help_center_searched&from_ts=1645435228208&to_ts=1648027228208&live=true)**# events**  
4.3M per day across all pods**Avg message size**  
~200 bytes**Throughput**  
4.3M per day across all pods  
Standard Event| [Community post viewed](https://github.com/zendesk/help_center/blob/master/doc/events/activity/community.md#community_post_viewed)| | [guide/activity/community_post_viewed.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/community_post_viewed.proto) | TODO| `help_center.activity.community_post_viewed`| `account_id/message_id`| `ZENDESK_ACCOUNT_ID`| | Estimated Metrics:  
**# events** : 447K per day**Avg message size** : ~200 bytes**Throughput** : 447K per day  
Standard Event| [User profile viewed](https://github.com/zendesk/help_center/blob/master/doc/events/activity/community.md#user_profile_viewed)| | [guide/activity/user_profile_viewed.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/user_profile_viewed.proto) | TODO| `help_center.activity.user_profile_viewed`| `account_id/message_id`| `ZENDESK_ACCOUNT_ID`| | Estimated Metrics:  
**# events** : 100K per day across all pods**Avg message size** : ~220 bytes**Throughput** : 100K per day  
Standard Event| [Article viewed](https://github.com/zendesk/help_center/blob/master/doc/events/activity/knowledge_base.md#article_viewed)| | [guide/activity/article_viewed.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/article_viewed.proto) | | `help_center.activity.article_viewed`| `account_id/message_id`| `ZENDESK_ACCOUNT_ID`| | **# entities** : 24.7M per day across all pods  
**Avg message size** : ~200 bytes  
**Throughput** : 24.7M per day across all pods  
Standard Event| [Section Viewed](https://github.com/zendesk/help_center/blob/master/doc/events/activity/knowledge_base.md#section_viewed)| | [guide/activity/section_viewed.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/section_viewed.proto) | | `help_center.activity.section_viewed`| `account_id/message_id`| `ZENDESK_ACCOUNT_ID`| | **# entities** : 3.3M per day across all pods  
**Avg message size** : ~220 bytes**Throughput** : 3.3M per day across all pods  
Standard Event| [Front page viewed](https://github.com/zendesk/help_center/blob/master/doc/events/activity/knowledge_base.md#front_page_viewed)| | [guide/activity/front_page_viewed.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/front_page_viewed.proto) | | `help_center.activity.front_page_viewed`| `account_id/message_id`| `ZENDESK_ACCOUNT_ID`| | **# entities** : 11.8M per day across all pods  
**Avg message size** : ~200 bytes  
**Throughput** : 11.8M per day across all pods  
Standard Event| [Category Viewed](https://github.com/zendesk/help_center/blob/master/doc/events/activity/knowledge_base.md#category_viewed)| | [guide/activity/category_viewed.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/category_viewed.proto) | | `help_center.activity.category_viewed`| `account_id/message_id`| `ZENDESK_ACCOUNT_ID`| | **# entities** : 3.4M per day across all pods  
**Avg message size** : ~200 bytes**Throughput** : 3.4M per day across all pods  
Standard Event| [Related article clicked](https://github.com/zendesk/help_center/blob/master/doc/events/activity/knowledge_base.md#related_article_clicked)| | [guide/activity/related_article_clicked.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/related_article_clicked.proto) | | `help_center.activity.related_article_clicked`| `account_id/message_id`| `ZENDESK_ACCOUNT_ID`| | **# entities** : 1.4M per day across all pods  
**Avg message size** : ~210 bytes  
**Throughput** : 1.4M per day across all pods  
Standard Event| [Anonymous support request submitted](https://github.com/zendesk/help_center/blob/master/doc/events/activity/request_form.md#anonymous_support_request_submitted)| | [guide/activity/anonymous_support_request_submitted.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/anonymous_support_request_submitted.proto) | | `help_center.activity.anonymous_support_request_submitted`| `account_id/message_id`| `ZENDESK_ACCOUNT_ID`| | **# entities** : 580K per day across all pods  
**Avg message size** : ~230 bytes  
**Throughput** : 580K per day across all pods  
Standard Event| [Support request made](https://github.com/zendesk/help_center/blob/master/doc/events/activity/request_form.md#support_request_made)| | [guide/activity/support_request_made.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/support_request_made.proto) | | `help_center.activity.support_request_made`| `account_id/message_id`| `ZENDESK_ACCOUNT_ID`| | **# entities** : 184K per day across all pods  
**Avg message size** : ~250 bytes  
**Throughput** : 184K per day across all pods  
Standard Event| [Support request viewed](https://github.com/zendesk/help_center/blob/master/doc/events/activity/request_form.md#support_request_viewed)| | [guide/activity/support_request_viewed.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/support_request_viewed.proto) | | `help_center.activity.support_request_viewed`| `account_id/message_id`| `ZENDESK_ACCOUNT_ID`| | **# entities** : 950K per day across all pods  
**Avg message size** : ~200 bytes  
**Throughput** : 950K per day across all pods  
Standard Event| [Submit request form viewed](https://github.com/zendesk/help_center/blob/master/doc/events/activity/request_form.md#submit_request_form_viewed)| | [guide/activity/submit_request_form_viewed.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/submit_request_form_viewed.proto) | | `help_center.activity.submit_request_form_viewed`| `account_id/message_id`| `ZENDESK_ACCOUNT_ID`| | **# entities** : 3.4M per day across all pods  
**Avg message size** : ~220 bytes  
**Throughput** : 3.4M per day across all pods  
Standard Event| [Suggested article clicked](https://github.com/zendesk/help_center/blob/master/doc/events/activity/request_form.md#suggested_article_clicked)| | [guide/activity/suggested_article_clicked.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/activity/suggested_article_clicked.proto) | | `help_center.activity.suggested_article_clicked`| `account_id/message_id`| `ZENDESK_ACCOUNT_ID`| | **# entities** : 100K per day across all pods  
**Avg message size** : ~400 bytes  
**Throughput** : 100K per day across all pods  
Standard Event| Agent-graph graphql request| | [agent_graph/events.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/a52c1902c57e3ee61c3570cae29e5e60d8d4307a/schemas/zendesk/protobuf/agent_graph/events.proto)| | `agent_graph.events`| `account_id/message_id`| `ZENDESK_ACCOUNT_ID`| | **# entities** : 170K per day across all pods**Avg message size** : Not Sure**Throughput** : 100K per day across all pods  
Standard Event| Flow Builder V2 Flow Event| | [answer_bot/flow_builder/flows_v2.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/f61c740b49b6ac65230908ae0a0e88452d3d360d/schemas/zendesk/protobuf/answer_bot/flow_builder/flows_v2.proto) | [Checklist](https://docs.google.com/document/d/1bcwF3ie6wPCCfZ8bBZ2LNe7HsVGIAzmd26c20samgd8/edit)| `flow_builder.flows.v2`| `account_id/message_id`| | | **# entities:** 4k messages per pod per day **Avg message size** : 50kb**Throughput:** Up to 100/minute across all pods  
40MB/pod/day  
Standard event| | | [sunco/usage/conversation_events.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/sunco/usage/conversation_events.proto) | | PDA topic: `platform.standard.sunco.conversation_events`Non PDA topic:`sunco.conversation_events`| | accountIdschemaPathmessageIdObjectIdcreatedAt| |   
Standard event| | | [sunco/usage/message_action_events.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/sunco/usage/message_action_events.proto) | | PDA topic:`platform.standard.sunco.message_events`Non PDA topic:`sunco.message_events`| | accountIdschemaPathmessageIdObjectIdcreatedAt| |   
Standard event| | | [sunco/usage/message_created_events.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/sunco/usage/message_created_events.proto) | | PDA topic:`platform.standard.sunco.message_events`Non PDA topic:`sunco.message_events`| | accountId?schemaPathmessageIdObjectIdcreatedAt| |   
Standard event| | | [sunco/usage/message_delivery_events.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/sunco/usage/message_delivery_events.proto) | | PDA topic:`platform.standard.sunco.message_events`Non PDA topic:`sunco.message_events`| | accountId?schemaPathmessageIdObjectIdcreatedAt| |   
Standard event| | | [sunco/usage/notification_events.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/sunco/usage/notification_events.proto) | | PDA topic:  
`platform.standard.sunco.notification_events`  
Non PDA topic:  
`sunco.notification_events`| | accountId?schemaPathmessageIdObjectIdcreatedAt| |   
Standard event| | | [sunco/usage/usage_events.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/sunco/usage/usage_events.proto) | | PDA topic:  
`platform.standard.sunco.usage_events`  
Non PDA topic:  
`sunco.usage_events`| | accountId?schemaPathmessageIdObjectIdcreatedAt| |   
Standard even| | | [sunco/usage/user_events.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/sunco/usage/user_events.proto) | | PDA topic:  
`platform.standard.sunco.user_events`  
Non PDA topic:  
`sunco.user_events`| | accountId?schemaPathmessageIdObjectIdcreatedAt| |   
Standard event| Guide self-service session| | [platform/standard/user_sessions/self_service_user_session.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/standard/user_sessions/self_service_user_session.proto) | | `guide.user-sessions.self-service-sessions`| `account_id/message_id`| | | **# entities** : 1.4M per day across all pods**Avg message size** : ~300 bytes**Throughput** : 1.4M per day across all pods  
Standard event| Guide self-service page analytics| | [platform/standard/user_sessions/page_analytics_event.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/standard/user_sessions/page_analytics_event.proto) | | `guide.user-sessions.self-service-page-analytics`| `account_id/message_id`| | | **# entities** : 15M per day across all pods**Avg message size** : ~250 bytes**Throughput** : 15M per day across all pods  
Standard event| Deployment Result| | [platform/standard/customer_config_history/deployment_event.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/standard/customer_config_history/deployment_event.proto) | | `platform.standard.deploy-results`| | schemePathaccountIdoccurredAt| [Initial Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/1670)Follow-up PRs:

  * [Schema update](https://github.com/zendesk/zendesk_protobuf_schemas/pull/1699)
  * [Renaming schema definition file](https://github.com/zendesk/zendesk_protobuf_schemas/pull/1721)

|   
Standard event| Data Quality Sourcedata | | [data_quality/sourcedata.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/data_quality/sourcedata.proto) | | data-quality.sourcedata.rowcounts| | | [PR 1865](https://github.com/zendesk/zendesk_protobuf_schemas/pull/1865) |   
Standard Event| Flow Builder Free Text Prediction Event| | [answer_bot/guided_flows/flow_builder/free_text_prediction_event.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/answer_bot/guided_flows/flow_builder/free_text_prediction_event.proto) | | `flow_builder.flows.v2`| `account_id`| | | **# entities:** 3M messages per day across all pods (600k max per pod)**Avg message size** : ~200 bytes**Throughput:** **** 3M messages per day across all pods  
Standard Event| Generative Replies Prediction event| | [answer_bot/generative_replies/generative_replies_prediction_event.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/answer_bot/generative_replies/generative_replies_prediction_event.proto)| | `answer-bot-service.generative-replies.predictions`| `account_id/message_id`| | | **# entities:** 1M messages per day across all pods**Avg message size** : ~1500 bytes**Throughput:** 1M messages per day across all pods  
Standard Event| Generative Replies Article Viewed event| | [answer_bot/generative_replies/generative_replies_article_viewed.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/answer_bot/generative_replies/generative_replies_article_viewed.proto)| | `answer-bot-service.generative-replies.article-views`| `account_id/message_object_id`| | | **# entities: 2.4K** messages per day during EAP across all pods**Avg message size** : ~600 bytes**Throughput:** **2.4K** messages per day during EAP across all pods  
Standard Event| Agent Productivity Metrics| | [agent_metrics/agent_metrics.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/agent_metrics/agent_metrics.proto) | [Checklist](https://docs.google.com/document/d/1c6Y5GBWT10w3c-pesNIj8F-Yo-ElZ3awPjldneReBVg/edit#heading=h.epdecdaxpos6) | ars.agent-productivity-metrics.1hour-aggregation| `account_id/message_id`| | | **# entities: 30M** messages per day**Avg message size** : < 1 MB**Throughput:** **30M** across all pods  
Standard Event| `AI_INTELLIGENT_TRIAGE_PREDICTION_EVENTS`| | <https://github.com/zendesk/zendesk_protobuf_schemas/pull/2599> | <https://github.com/zendesk/collections-service/pull/566#issuecomment-2222304600> | `platform.standard.machine-learning.triage.prediction.events`| account_id/message_id| Common protobuf header| <https://github.com/zendesk/collections-service/pull/566> | **# entities: 600k** messages per day**Avg message size** : < 1 MB**Throughput:** **600k** across all pods  
Standard Object| `COLLECTION_AI_INTELLIGENT_TRIAGE_INTENT_LABELS`| | <https://github.com/zendesk/zendesk_protobuf_schemas/pull/2635> | <https://github.com/zendesk/collections-service/pull/573#issuecomment-2257780962> | `platform.standard.machine-learning.triage.intent-labels`| account_id/object_id| Common protobuf header| <https://github.com/zendesk/collections-service/pull/573> | **# entities:** 43**k** messages per day**Avg message size** : < 1 MB**Throughput:** **43k** across all pods  
Standard Object| Guide Article Editor Feedback| | <https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/guide/guide_domains/guide_article_editor_feedback.proto> | | `guide-domains.guide-article-editor-feedbacks`| `account_id/message_id`| Common protobuf header| | **# entities: <1k **messages per day**Avg message size** : < 1 KB**Throughput:** <**1k** across all pods  
Standard Event| `COLLECTION_OMNICHANNEL_QUEUE_WORK_ITEM_EVENTS`| | <https://github.com/zendesk/zendesk_protobuf_schemas/pull/2816/files> | <https://docs.google.com/document/d/1aiX7kK27fdejEoFbAHwVCoA6JDGAugidgu0ChzUZlag/edit?tab=t.0#heading=h.epdecdaxpos6> | `qrs.work-item-change.events`| account_id/message_id| Common protobuf header| <https://github.com/zendesk/kennel/pull/26351> | **# entities: ~23k** messages per day**Avg message size** : < 1 MB**Throughput:** **~23k** across all pods  
Standard Object| `COLLECTION_OMNICHANNEL_QUEUES`| | <https://github.com/zendesk/zendesk_protobuf_schemas/pull/3068/files> | <https://docs.google.com/document/d/1aiX7kK27fdejEoFbAHwVCoA6JDGAugidgu0ChzUZlag/edit?tab=t.0#heading=h.epdecdaxpos6> | `qrs.queue-entity`| account_id/object_id| Common protobuf header| <https://github.com/zendesk/kennel/pull/26351> | **# entities: 7k** messages per day**Avg message size** : < 1 MB**Throughput:** **7k** across all pods  
Standard Object| `COLLECTION_OMNICHANNEL_QUEUE_GROUPS`| | <https://github.com/zendesk/zendesk_protobuf_schemas/pull/3068/files> | <https://docs.google.com/document/d/1aiX7kK27fdejEoFbAHwVCoA6JDGAugidgu0ChzUZlag/edit?tab=t.0#heading=h.epdecdaxpos6> | `qrs.queue-group-entity`| account_id/object_id| Common protobuf header| <https://github.com/zendesk/kennel/pull/26351> | **# entities: 7k** messages per day**Avg message size** : < 1 MB**Throughput:** **7k** across all pods  
  
* * *

  1. Categories: 



  * Core Object

  * Core Event

  * Custom Object

  * Custom Event?

---

### Schema Onboarding

**Page ID:** 1113555809  
**Version:** 3  
**Last Updated:** 2020-05-22  
**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/1113555809](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/1113555809)  

#### Data Engineering Context

[[Posted to slack for discussion here](https://zendesk.slack.com/archives/C0127FUBD41/p1589551205031600)]

As we pursue a strategy of becoming the principal CRM platform for our customers -- a one-stop-shop for all of their customer centric processes, workflows, reporting, etc. -- it is becoming increasingly important to present a coherent story about how all of the data customers care about is integrated and accessed.

As part of the overall [Platform Data Architecture](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/970330740/Platform+Data+Architecture) efforts, we need to bring together the various schema that we have developed in our various products into a coherent whole. We need to make the view we offer our customers logical and ensure all the various fragments fit together.

This is not a quick process and will happen in multiple stages over time.

To help get this started, our [Platform Data Architecture - Onboarding Checklist v3](https://docs.google.com/document/d/1LfhZOqsX8qElWP3WKP4TS56pPwKdZBnMTY-pTGbRBeE/edit) calls for the schema of each core object data type to be documented and reviewed prior to broad adoption. We've been calling this "governance" for lack of a better term.

After discussion between product management and engineering, we've agreed to start with the following fairly lightweight process. It should look familiar, based as it is on the existing ADR process for global engineering review. It also builds on the existing protobuf schema repository we have that defines each of the core data types as they are shared.

If you intend to publish a Core Object to a Kafka entity stream for use in the platform data architecture then you need to provide a fully documented protobuf schema and submit a pull request (PR) to the [zendesk/zendesk_protobuf_schemas](https://github.com/zendesk/zendesk_protobuf_schemas) repository. Each PR will be tracked on this [kanban-style project board in github](https://github.com/orgs/zendesk/projects/11). Your PR must document the schema and include the following:

  * For each schema type, describe what the data represents and how that relates to our product. Make this readable by non-engineers. Describe how this schema relates to other schemas.

  * For each field, describe the semantics and any limitations and constraints on the value.

  * If a field contains a "key" pointing to another object type (typically an "id" field), make clear what that resource is, and link to its schema, if possible.

  * Where denormalization is used (i.e. data from other objects is included), describe why that is necessary and whether clients can expect the data to be correct and up-to-date. Please also link to the original schema being denormalized when possible. 

  * Your protobuf namespace must be `platform.core`




As an example the Guide team recently wrote up this PR with their [proposed protobuf schema for Articles](https://github.com/zendesk/zendesk_protobuf_schemas/pull/476) as a core data type.

The PRs will be open for discussion and will initially be guided through to merge by a small group of people including , ,  and  to ensure timely followup and closure. You can tag them as `@zendesk/pda-schema` on github. We expect this process to evolve as we iterate further.

Once complete, the schema should be listed in our Platform Data Registry.

For any and all questions, please use the [#platform-schema](https://zendesk.slack.com/archives/C0127FUBD41) slack channel.

---

### Platform Schema & Metadata Working Group

**Page ID:** 4621118077  
**Version:** 18  
**Last Updated:** 2024-06-05  
**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4621118077](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4621118077)  

#### Data Engineering Context

*This section covers platform-level data engineering concepts relevant to PDD and EDA initiatives.*

Documents relating to the 2021 Platform Schema & Metadata Working Group

## Charter 

<https://docs.google.com/document/d/1PdA8XCk2oU7tZdjtCIX5nKkFedif4NzS5GrWz7wS4iQ/edit?usp=sharing>

Above is the original charter for the group. For Q3 we changed the scope of the WG as per [this announcement on Slack](https://zendesk.slack.com/archives/C01N6Q0J8UT/p1623823320053700). The short version if the changes are that we found that doing a remote, async, global working group came with many challenges, so we changed to a regular sync format. The second change was to re-scope the WG to focus on the _foundational_ aspects to building a metadata platform, specifically for onboarding to the Platform Data Architecture.

## Working Group Outcomes

The working group concluded at the end of Q3 2021.

(see iceberg diagram below) The newly founded Foundation Analytics Data Catalog team will be taking on ongoing ownership of some of the _foundational (bottom of the iceburg)_ parts of this problem space, as it comes to Platform Data Architecture enablement, onboarding data sets to the Data Hub, integration with service.yml etc. This will occur in collaboration with our soon to start Data Architect.

A new lineup of people from engineering and product will be brought together in 2022 to dive into some of the (top of the iceburg) parts with relation to Custom Data & Logic, UI Platform etc.

## Meetings

Platform Schema & Meta WG: Meeting Notes

Fortnightly syncs were held with both APAC/AMER members and APAC/EMEA members.

## Who's in the group?

#### Executive Sponsor

#### Working Group Leaders

Leaders are **Accountable** in RACI terms for ensuring WG delivers the goals stated in the charter, and guiding the group to achieve them.

#### Core Group

The core members of the WG are **Responsible** in RACI terms for delivering the goals stated in the charter.

#### Extended Group

The larger extended group includes other interested parties that are **Consulted** by the group or **Informed** of the outcomes in RACI terms.

## Lessons learnt

  * Running an asynchronous working group with participants in all timezones that we have engineers is an excellent aspiration, but in practice difficult to maintain engagement

    * With some staff on leave or changing roles, different regions going in and out of lockdowns, production freezes and reliability focus, there was a lot going on for everyone

    * All of the above made it hard to maintain engagement for the duration of the group, and hard for folks to dedicate out-of-band time to areas outside of their normal work

    * We switched from async to a recurring, synchronous meeting which helped maintain the momentum of the conversation, although it didn't necessarily help keep the POCs and such moving. In the future, involving PGM from the beginning to help facilitate progress would help. 

  * We need to work before we can run

    * There is a long path ahead of us (see dependency map in diagrams below) to get our infrastructure and tooling into a spot where we can begin looking to morphing our products into dynamic, tenant-aware, metadata-driven experiences (ala. [Salesforce paper](https://zendesk.slack.com/files/U07ALLK7H/F0287UG1Y87/p889-weissman-1.pdf))

    * The work starting the Foundation Analytics Data Catalog team in the coming quarters, building out core capabilities for onboarding to the Platform Data Architecture, describing and cataloguing internal datasets with help build a solid bedrock to build on

    * Making it easy for internal engineering teams to adopt a common data platform, and onboard to it is critically important

  * There are still many open questions (see meeting notes) around how we manage per-customer schema and metadata, as well as per-use-case annotations (eg. UI-specific metadata, metadata to describe abilities wrt. Triggers/Workflow)

    * Some of these questions are coming to a head soon and will likely require a more pragmatic approach to alignment here, being mindful not to cause undue disruption to critical delivery streams, but avoiding too much fragmentation

      * eg. Triggers V2, Custom Objects V2, Zendesk Integration Services, Webhooks, Event Job Dispatcher, Explore integration, Sunshine Events, Import/Export

  * We need to lock down our terminology to avoid confusion

    * This area has a lot of fuzzy terminology that has subtly different meanings to many people




## Diagrams

**Note:** Hover over the embedded LucidChart below with your mouse to show the different tabs.

5trueleftrich1491ea76b-b588-46f5-ab68-0d4416d7d739Confluence:208381722670072a23137-a469-4fd4-8440-6f06cc192ada|103589275|4621118077|onUSRW36+Bg1KzjWpo0B7IpHYMtycSTdglUWzTLg+Xc=72a23137-a469-4fd4-8440-6f06cc192ada1614739427633500

## Related Documents

  * One Zendesk: Strategy

  * <https://docs.google.com/document/d/1pIsLN-7SDXkw4bI8rr_rZeb7YZBrjPkY-3_mFDnCJ7M/edit#>

  * <https://docs.google.com/document/d/1ub5O_kvWa2_MgyjFKF3Fsij2V0YSM9xX8cPfgHgAG2U/edit>


truecreation

---

### What exactly are ZObjects?

**Page ID:** 6248464471  
**Version:** 2  
**Last Updated:** 2024-06-05  
**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6248464471](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6248464471)  

#### Data Engineering Context

This was originally a Slack posted at <https://app.slack.com/docs/T024F4EL1/F01G3DXQHJ8> from , but has been archived to Confluence due to Slack's retention policies.

Authors: Brett Adams and Amy Derosier  
Date: 

Following on from the updated [ADR:Platform Data Architecture: Standard Objects](https://github.com/zendesk/techmenu/pull/395/files) it has become increasingly apparent that we need to clarify the introduction of our ZObjects terminology.

ZObjects come in two "flavors"\- Standard and Custom. (top, bottom, strange and charm will be defined at a future date)

Standard ZObjects are those in our base products - Tickets, Deals, Leads, Conversations, Users, Groups, Articles, etc. Basically, any of the data model types that we have defined and built into our own product offerings.

Custom ZObjects are extended data types our customers can create within our products - right now, Sunshine Events, Profiles and Custom Objects provide such capabilities.

A really, really important point to understand is that **these terms are all meant as** _**conceptual**_**terms** for the benefit of talking amongst ourselves, and most importantly, with our customers.

ZObjects are an _overarching conceptual model_ for talking about the behaviors and capabilities we expect _from all of the various implementations_ of data models within our varied products _over time_.

As we further develop our platform-oriented offerings, customers should expect that they can add fields to any ZObjects (Standard or Custom), regardless of which "product" they are used within. They should expect that the built-in functionality of our products will be able to use this data in support of their business processes. They should expect that these objects are all visible in Explore for analytics. They should expect that where custom logic can be defined in our products, it can also work against both flavors of ZObject.

Put another way, there's no "abstract Ruby base class for ZObject" that all of our various data model implementations need to descend from. The code doesn't all have to be implemented in one stack - we're going to need these capabilities in multiple stacks. There _may_ be common Ruby, Java or Go libraries in the future to make it easy for each of our various technology components to offer these common capabilities, but there's no explicit _requirement_ for that.

Please post further questions to the [#architecture](https://zendesk.slack.com/archives/C9FSBLE0Z) channel.

Amy & Brett

---

### Platform Schema & Meta WG: Meeting Notes

**Page ID:** 4619712960  
**Version:** 18  
**Last Updated:** 2021-09-29  
**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4619712960](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4619712960)  

#### Data Engineering Context

*This section covers platform-level data engineering concepts relevant to PDD and EDA initiatives.*

**Reminder: Record meetings**

## 2021-02-23 - APAC/AMER Kickoff

**Attendees**

  *     * Portfolio Architect, prev: Connect, Sunshine, APIs

  *     * Business Rules team, Symphony

    * Now working on transactional platform for triggers (Triggers V2)

    * Keen on POC

  *     * Interest in auto-generated UI

    * Keen on POC

  *     * Our Chief Product Architect … will be our chief cheerleader, enabling us where we need to be enabled

  *     * GTL on Platform

    * Experience with metadata, pluggable UIs in other companies

    * Keen on POC

    * Help w/ interviews

  *     * Portfolio Architect

    * Participating on specification / documentation

  *     * Fdn Analytics - want to be able to understand data we're ingesting

    * Worked in data governance at GE, GE Digital Assets Service

    * Help w/ spec

  *     * Dir Product, formerly Support core elements (business rules, tickets, sandbox)

    * Now Platform, custom data and business logic

  *     * Transitioning to be GTL for Custom Objects

    * Looking to ensure consistent theory between Custom Objects, custom fields, etc.

    * Keen on POC time allowing

  *     * Challenges not having common model for metadata and schema

    * Help with spec & POC




**Agenda**

  * Introductions

    * See notes above

  * Walk through WG purpose & deliverables

    * [ _WG Charter_](https://docs.google.com/document/d/1PdA8XCk2oU7tZdjtCIX5nKkFedif4NzS5GrWz7wS4iQ/edit?usp=sharing)

    * [ _Data Models_](https://docs.google.com/document/d/1Q5zWVfx0vqe1HyPEXPZjhZUUoIHA0Mj_nm3WoFmrdvY/edit?usp=sharing)

    * [ _Brett's video on Data Models_](https://drive.google.com/file/d/1-1bVGy6JLZJulihyeG_lXHx3OJDvvLnA/view?usp=sharing)

    * [ _What exactly are ZObjects_](https://zendesk.slack.com/files/T024F4EL1/F01G3DXQHJ8?origin_team=T024F4EL1)

    * [ _UI Platform Vision_](https://docs.google.com/document/d/14kYJLnq8b4TYyTlQmhirnpZQwtlkH5cFN1ysfDMo1mI/edit?usp=sharing)

    * [ _OneGraph_](https://github.com/zendesk/techmenu/pull/554)

    * Salesforce [_describeSObject_](https://developer.salesforce.com/docs/atlas.en-us.230.0.api.meta/api/sforce_api_calls_describesobjects_describesobjectresult.htm)

  * Discuss what is _not_ in scope

    * Relationship to [_Data Catalog_](https://docs.google.com/document/d/1nelYoCRTvW8f_JggBdp_KeXUwFt79ufSvZh5S3xvDNs/edit?usp=sharing)

    * Infrastructure concerns

    * Data Governance

  * Discussion on how best to operate WG given timezone

  * Record Open Questions

    * Metadata representation that can do custom per-account customization

    * Budget of time per person

  * Risks for the WG

    * POC #guild-schema-driven-ui auto-generation of admin pages overlap/dependencies

      * Different ideas of schema/meta, readonly r/w, very broad

      * How does it work?

    * May decide on a standard, but follow-on work is hard to make a reality, programmes, how do we actually get there

    * Existing ticket/org/user fields could be a strong anchor bias, or be prohibitive to migrate

    * Timezones

    * Divergence on terminology/understanding

  * Glossary as first step




## 2021-02-23 - APAC/EMEA Kickoff

**Recording** : [_https://zendesk.zoom.us/rec/share/4eWC7fHAGe6tcCyTSjujB1ADm3eBEyipMHOU8ROO5TuBFaqsGzU_bpx6R47ll8s1.EHFDmCYKvbS1oWsV_](https://zendesk.zoom.us/rec/share/4eWC7fHAGe6tcCyTSjujB1ADm3eBEyipMHOU8ROO5TuBFaqsGzU_bpx6R47ll8s1.EHFDmCYKvbS1oWsV)

Passcode: 2St+nYz#

**Attendees**

  *     * Portfolio Architect

  *     * CPH - Guide Piratos

    * Events & Entity Streams

    * Worked with  has introduced lots of ideas in this space

    * Domain Event log off escape

    * Collections Service w/ Ciaran to flow guide data to Explore

    * Guide Search, AB integration

  *     * EDA team

    * 2 years @ ZD

    * Data Catalog, analytics perspective, human usage

    * Data Portal

    * Data Lineage, data lineage

  *     * Portfolio Architecture

    * Worked everywhere

    * Platform Data Architecture, Collections

    * Vision for Data Architecture

    * Metadata overlaps with data architecture

  *     * New to ZD

    * Principal for Explore

    * Data arch vision

    * Explore is downstream of entity streams & other data

    * Data infra background, semantic web

  *     * GTL for machine learning group

    * ~ 4 years

    * Answer bot & Content Cues

    * Ticket Enrichment Service, applying ML on ticket data

    * Interested in prediction data can interact




**Agenda**

  * Introductions

    * See notes above

  * Walk through WG purpose & deliverables

    * [ _WG Charter_](https://docs.google.com/document/d/1PdA8XCk2oU7tZdjtCIX5nKkFedif4NzS5GrWz7wS4iQ/edit?usp=sharing)

    * [ _Data Models_](https://docs.google.com/document/d/1Q5zWVfx0vqe1HyPEXPZjhZUUoIHA0Mj_nm3WoFmrdvY/edit?usp=sharing)

    * [ _Brett's video on Data Models_](https://drive.google.com/file/d/1-1bVGy6JLZJulihyeG_lXHx3OJDvvLnA/view?usp=sharing)

    * [ _What exactly are ZObjects_](https://zendesk.slack.com/files/T024F4EL1/F01G3DXQHJ8?origin_team=T024F4EL1)

    * [ _UI Platform Vision_](https://docs.google.com/document/d/14kYJLnq8b4TYyTlQmhirnpZQwtlkH5cFN1ysfDMo1mI/edit?usp=sharing)

    * [ _OneGraph_](https://github.com/zendesk/techmenu/pull/554)

    * Salesforce [_describeSObject_](https://developer.salesforce.com/docs/atlas.en-us.230.0.api.meta/api/sforce_api_calls_describesobjects_describesobjectresult.htm)

  * Discuss what is _not_ in scope

    * Relationship to [_Data Catalog_](https://docs.google.com/document/d/1nelYoCRTvW8f_JggBdp_KeXUwFt79ufSvZh5S3xvDNs/edit?usp=sharing)

    * Infra

    * Data Governance

    * **Record-level metadata**

  * Discussion on how best to operate WG given timezone

  * Record Open Questions

    * Metadata representation that can do custom per-account customization

    * Budget of time per person

  * Risks or concerns for the WG

    * POC #guild-schema-driven-ui auto-generation of admin pages overlap/dependencies

      * Different ideas of schema/meta, readonly r/w, very broad

      * How does it work?

    * May decide on a standard, but follow-on work is hard to make a reality, programmes, how do we actually get there

    * Existing ticket/org/user fields could be a strong anchor bias, or be prohibitive to migrate to a new standard

    * Timezones

      * Mitigation: keep broadcast on Slack

    * Divergence on terminology/understandin  


  * : Technical metadata & business metadata - terminology from Google Data Catalog

    * Tech - schema, strict

    * Business, loosely defined

    * [ _https://schema.org/_](https://schema.org/) semantic types across industries

  * Next steps

    * Create shared glossary

      * Try diverge/converge exercise and compare notes

      * Catkins to send out a template




## 2021-03-03 Platform Meta & Data Catalog

**Attendees**

**Notes**

  * We don't believe that Platform Metadata & Data Catalog are incompatible

  * Platform Metadata will be upstream of Data Catalog. The interface between them is to be determined later when both efforts are further along.

  * Platform Metadata represents logical data and is not concerned with the physical location of the data

  * Data Catalog keeps track of a broader group of data sets and derived data sets

  * Data Catalog is asynchronously populated from multiple sources

  * Data Catalog will soon begin evaluating existing technologies in the Open Source and Commercial worlds

  * **Open Question:** How are per-account _custom_  data types or custom extensions to existing datatypes to be represented in the Data Catalog

  * **Open Question:** How de we manage the difference between the production topology (eg "the partitions") and the data topology




## 2021-06-16 Vocabulary exercise cont. & WG reset 

**Attendees** : 

**Meeting Notes**

  * Resetting the WG a bit to focus on answering a few more some more short-term questions

  * Moving from a primarily async model to a having regular meetings

    * Regular meetings to help maintain momentum

    *  _Try_ to slice the research areas / POCs to avoid the need of having syncs on all three sides of the APAC/AMER/EMEA triangle

  * POCs / Research areas

    *  _Validate some hypotheses_

    * Try DataHub

    * Try GraphQL IDL to express others

    * Jason's Service.yml to Cerebro

    *  _Q:**Should**_ a registry contain customer data?

      * Changes from a static GitHub based workflow to a Runtime one

      * Huge difference in scope

      * Can these be two solutions layered?

  * Value Prop Brainstorming

    * Allow services to more easily adopt PDA & see downstream benefits

    * Input to Documentation & Data Governance

    * Can I make this breaking change? Who do I need to talk to first?

      * Currently referencing [intake forms](https://docs.google.com/document/d/1QrH5txc9ptBL5xUkIrJb_C4kQBVEzlCrfgbG8-_nkzo/edit) / google sheets / confluence

    * Service.yml

      * Automation for kafka topics, collections, tables in Zendesk DataHub/Data Lake, Cerebro, ACLs

    * Connecting into the Platform Data Graph / OneGraph

      * Generating TypeScript types

    * Describing Custom Data in the same way as standard objects

    * Explore

    * Import/Export

    * UseCase: Triggers V2

      * Be able to pull relationships and fields for objects to use in trigger conditions, including account specifics of custom objects, relationships, fields etc

      * Power Admin form for configuring triggers, provide type information

  * Returned to vocab exercise for the remainder of the session




## 2021-06-24 APAC/EMEA

Attendees 

**Meeting Notes**

  * Did a re-cap of the WG pivot and meeting schedule change

  * Discussion of the POCs

    * has an interest in the GraphQL as a descriptor language

      * Catkins - that makes sense given the proximity to  & OneGraph team

    * has moved from DUB -> Miami, straddling SF & EU timezones

      * As  and other EDA folks are in DUB, probably makes sense to do as a AMER/EMEA POC re: DataHub evaluation

    * is in same TZ as Dovetail team, so keen to kelp  with his POC

    * Big question of whether we _should_ try to combine customer & zendesk data types

      *  _or should this be deferred after PDA essentials tackled?_

  * With the timezones and the POCs

  * Focus on self-service & PDA enablement as foundation for the WG: 3 key areas

    * Source of truth for datasets

    * Workflow for teams contributing data to PDA

      * eg. if you do X, you get Y & Z

    * Data description format chosen

  * to create and share dependency map, highlight fundamentals that need to be tackled and show what they unlock

    * Probably on Miro

  * to organize interview w/  in next two weeks before summer holidays

  * Definition of Done for the WG

    * Still an ADR with some recommendations from the POCs, create dependency map showing where we _could_ go in the future and what are the stepping stones to get there




## 2021-06-30 - APAC/AMER

**Recording:**

**Attendees:**

**Meeting Notes**

  * Catkins - recap of above

  * Standard & Custom Objects

    * Looking to unify extensibility of custom objects & custom fields

  * Shift has been to see whether we can use something off the shelf

    * Acryl DataHub has claimed that it could do it, but we need to validate it

  * Difference between standard and custom object is artificial

    * Should be the same, to avoid assymetrical platform

    * We want custom data to do everything

    * Model, definition, structure

  * Standard object standards aren't set up for custom data

    * eg. schema per-object, kafka headers

    * ProtoBuf may not be sufficiently expressive

    * Protobuf may be something that we can compile down to

    * Shouldn't be afraid to make some decisions that are hard

  * Zendesk DataHub and other FDN projects built on published standards

  * Either treating custom-data as a `Hash` or building schemas

    * Want to be able to use custom data/fields in triggers or business rules, in UI or other programming model

    * Under the hood can store objects as Hashes, but show rich schema to UI

  * Core Objects / Standard Objects

    * Explore want to use some core objects, but unable to find them (eg. User)

    * Core Objects => Standard Objects re-brand

    * Big gaps in coverage, user/agent group relationships

    * Should be available on-demand

  * Can't ignore per-customer customization

    * Layers customization ontop of standard

    * Application layer translation, DataHub 

  * Data Catalog

    * Cardinality of custom data

      * Does data lake need to have S3 prefix per customer defined type

        * No, not really useful for reporting

      * For Platform Data Graph, yes maybe have a "Car" type represented in the rgaph

      * There needs to be two levels here

      * Multiplexing custom data in same kafka topcis

      * Layered GraphQL IDL

  * Support graph models ticket/support fields

    * Consumer needs schema up-front

    * eg. would lotus need to reload if new field is added?

    * Autogenerated TS types from GQL

    * Typically "peek" at type-name 

    * One-schema per-customer isn't ideal for AW, having to deal with arbitrary types is a headache

  * Conditions

    * ifs/else/not etc, run data through a function and pop out whether to show something

    * Conditions to refresh lotus

    * Publishing asset that contains a condition tree, runtime fetches it and runs rules and may or may/no refresh Lotus

    * Many representations of conditional logic, ZIS, triggers, sell, triggers 2 - need standardization

      * Triggers 2 POC serialized a parse tree

  * Custom data

    * Examples of type-ahead

    * One-to-many or one-to-one object, how do we render the name? Composites?

    * CO - fixed system column called display_name or title or rejected proposal to delegate to field, a composite field

    * Computed fields - run through template or conditions

  * A little lost in some of the converations as things and hazy on things that are consuming the artifacts

    * Concrete examples

    * Consumers clear is useful




## 2021-07-14 - APAC/AMER

Recording: <https://zendesk.zoom.us/rec/share/KBZBS0hT5IwBnxEGY-uzw3uN7HEXnKkRn7uB5OamMogcZdu3Lfx5fvDRNxrJW2Tc.Ayyttx_n9o5-k-7m> Passcode: ?=&M5HoM

Attendees: 

  * Ananth: demoing branch of schema IDL format

    * YAML based, but not critical to the design

    * SchemaDef data structure uses a graph under the hood

      * graph lets tooling walk the graph to identify potential data quality bugs

    * Transpiles to semi-arbitrary targets, eg protobuf, aws glue catalog

  * Separation of logical schema and infra

    * Some linting and CI at the front

    * Some workflow for infra changes

  * Explore / Data Mesh - Defining data transforms in SQL

    * Spark SQL, Flink SQL preferred over Apache Beam - abstraction layer misses out on engine optimizations




## 2021-07-28 - APAC/AMER

Recording: <https://zendesk.zoom.us/rec/share/_TqZ4zEkK7TdWgqx2kSi-gZVvfwNJrJ9cNuHqayLGliBdvtutqOQzxP-Z3mitn3u.wD5OQIVhxCu_BLpX> Passcode: QM!MnV.7

Attendees: 

  * David - system user key rotation

    * Learning - test kits, spec etc v helpful

    * MicroProfiler have conformance tests

  * ZRN

    * Namespacing

      * Partner developers

      * Custom Objects

      * Reserved namespaces to avoid collisions

    * Display Name

      * System field for all object

    *   * Non Service data to ZD DataHub

    * Does this fit into the PDA?

  * PDA for a service data without account id, eg acquisitions

  * Manager hired for Data Catalog team

  * Hiring for new Data Architect




## 2021-08-11 - APAC/AMER

Recording:

Attendees:

Meeting Notes:

  * POCs

    * Cerebro thing works!

    * Platform Data Set showing up in Staging

  * Schema translation

    * SQL output working

    * GraphQL vs homegrown SDL?

      * J Hwang has the keys

      * What are the questions?

        * RFC?

      * DataHub

  * Data Catalog team starting now

  * Domain events

    * do we need to support repeated oneof fields?

      * One kafka topic vs many per event

  * Event ordering

  * End to end delivery guarantees

  * Triggers V2

    * Ideation phase, re-align on product vision

    * Expansion of vision?

    * Rename? Platform rules engine

    * Transactional bits

    * Rules engine

      * Not coupled to classic

      * Faster

      * Formulas

      * etc

  * Customer-defined datatypes

    * Lotus to be refactor, package up lotus components

    * Down the road metadata endpoint would be v helpful

    * Right now buried in tech debt

    * Longterm common interface for these things, shared across different entity types




## 2021-08-11 - APAC/AMER

Recording:

Attendees:

Meeting Notes:

## 2021-08-25 - APAC/AMER

Recording:

Attendees:

Meeting Notes:

  * ZRNs

  * Apache ORC columnar storage used at LinkedIn

  * POCs

    * Still some open issues

    * RFC - should we be rolling our own format?

    * Operators

  * <https://docs.google.com/document/d/1oT4OuyKlEcIO6Fug4ytNxu1XVe4tVBAhCCDfs_hc3cM/edit?usp=sharing>

  * <https://docs.google.com/document/d/1fBuFaHV-C2E252R0vLH36esqwdTXCG6uJR86-caGXdQ/edit?usp=sharing>

  * <https://github.com/zendesk/zendesk_rules>

    * Used by views and triggers

    * Customer lookup fields considering using it to define filtered relationship constraints 

  * <https://docs.google.com/document/d/1BGLFi0JJVEfW-5pKwAUsjCa2bTASacb5hOEiIYgIMew/edit>

  * How do we represent product-specific constraints

  * Interlang - common tongue




## 2021-09-08 - APAC/AMER

Recording: <https://zendesk.zoom.us/rec/share/CXAoLLDpQxerL3sScaix_jY5VBefx4VwHtIWQVxXy_E3GF3SyF_T3UW6x10avII6.kTfzVsuBptfZlCGk> Passcode: K+Y134dp

Attendees: 

Meeting Notes:

  * David L: RFC schema lang

    * Additional context to the RFC

    * Deadline for feedback?

    * Hoping to move along to ADR

  * Kristoffer Hansen move out of group

  * Other POCs passed over to David L / Sebastian's team

    * Work not to be blocked on ADR process

  * ZRNs coming

  * Wrap up?

    * Ongoing steering/governance committee?

      * Lobby Brett / VPs?

    * Bifurcation?

      * Production / SFDC Paper stuff

    * Served it's purpose in the current form

      * Sum up deliverables

        * Sub-groups? Some other group

          * SDL to capture broader req's, 

        * Data architect to take over stream

          * Data Cat - ongoing

          * SDL exploration

            * RFC for schema def, don't conflate with full meta

        * Glossary - final outcome

          * Draft PR?

        * PDA Entity streams

          * are they still useful? kafka powered anything? kafka mover? order guarantees?

  * Mobile App

    * Can we publish changes via meta rather than package bumps

  * 


## 2021-09-29 - APAC/AMER

  * What are the API gaps that we have in a metadata picture

    * List ZObjects

    * List custom types

    * Build for a consumer

    * Suspect when frontend comes, API contract

    * Existing field endpoints - can we remove hardcoding

    * E2E story of usage

    * Ticket fields endpoint

      * Inconsistent w/ user/org fields

    * Gabe: MySQL internals, looking for analogs

      * Effective use of InnoDB

  * PDA

    * 2019 - very kafka oriented, get all entity streams, build materialised views

    * Struggled to get data models to exist in that form

    * Missing foundational layers, eg. account moves

    * OneGraph shifted thinking somewhat

      * More interested

      * More acceptable than we used to

    * Entity streams for DataHub/Explore

    * Do people want to build materialised views

    * These things need use-cases, eg. Views had a useful use-case

    * Hard to get on roadmap unless consumer

    * What do we need metadata for?

      * Customer facing aspects, eg. SFDC paper

    * Because we weren't metadata-first, people hardcoded

    * eg. Custom Objects backing ZObjects

    * eg. Call object in classic

    * Analytics - PDA is a contract

  * Quarterly syncups?

    * Common meta between analytical/product

  * Vocab

    * TechMenu

  *

---

### Platform Schema & Meta WG: Requirements Gathering

**Page ID:** 4615194805  
**Version:** 7  
**Last Updated:** 2021-08-09  
**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4615194805](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4615194805)  

#### Data Engineering Context

*This section covers platform-level data engineering concepts relevant to PDD and EDA initiatives.*

To gather requirements for the common metadata specification, we will conduct a series of Zoom interviews with various people in Engineering, Product & Design, and record the notes from the discussions below.

### Admin Center

Contact:

### Garden

Contact: 

### Schema Driven UI

Contact 

  * Catchup March 5th w/ Austin DZ, Catkins

  * Still lots of unknowns, what is everything we can interact with

  * POC informs schema driven UI

  * Different ideas

    * eg. readonly views of data, low code UI solutions for internal, reproducable forms and settings, visualisation - user defined schemes for agent workspace layout

  * Read or RW

  * Technologic

    * [Formik](https://formik.org/) & [Form](https://formium.io/)ium

    * Schema driven forms, including validation, dirty states

    * Used in Zendesk, with read schemas for nice validation forms

  * Common API patterns across formik

  * Cross-platform UI

    * What level do we care about most? eg terminology labels

  * Concerned about combining third party and schema and customization stuff

    * Weird junk for internal stuff

  * Chonk use-cases vs dynamic

    * Separation of needs here

    * Internal customers - more static

    * Customer customers - more dynamic

  * Where are these stitched together

  * Where is the metadata line

    * Where is schema, where is the "other stuff"

  * "We can define the shape, but how we do we define the relationships between the shapes?"

    * How do we define the interactions between these

    * eg Master/Detail views

  * Queries for metadata

  * Designer for POC

    * Vedran??

    * Organise next week

  * Typeform

    * Baseline for agnostic data types




### Data Management UI

Contact: 

### Sunshine Events & Profiles / Custom Activity

Contact: 

### OneGraph

Contact: 

### Custom Objects

Contact: 

### Triggers, Automations, Workflow

Contact: 

Recording: <https://zendesk.zoom.us/rec/share/D6V3Lsb6dFiqdLwnvMIdYTaVaoAlsX5YURR2h8aRgHxHnj1iAY9VhIfSiOGfIfGF.JtDLH6yxudLY_Eem> Passcode: 1.X*2FJv

  * Triggers V2

    * Right now, fairly hard coded preset fields/relationships

    * List of relationships

      * eg user belongs to group, ticket belongs to user

      * strict hierarchy of items

    * Set number of parent items that be looked up

      * set number of child items that can have actions on them

    * Unsure where they're going to live

      * Timing means that it's a relationship structure that is looked up in classic

    * Prototype used a JSON structure to represented fields / relationships

      * Engine designed to be data agnostic

    * [Link to protype](https://github.com/zendesk/triggers-v2-prototype-java)

    * Prototype keeps data fetching out

    * Combining of built-in and customer-defined part

      * Custom fields can be stitched into the JSON

    * "Entry" object

      * Object who's lifecycle change that causes the trigger to be invoked

      * created/updated

      * Ticket org, user etc

      * Entry object schema is fetched

  * Q3? maybe to start working on

    * Architecture & design

    * Expected deliverable is an ADR

  * Transactional?

  * Metadata for rule definitions??




### Guide

Contact: 

Recording: <https://zendesk.zoom.us/rec/share/eaxjjvxFo0jWb7BUC20QWHY4MV3C3CL3tPEk6vF4Fi-_nspR87dslZ9pO1t2RgGi.XEwTGxiFkoxgUXRY> Passcode: C5mBz+g=

  * Kasper - helping for use-cases

  * Guide-REST, describing all APIs in OAS / JSON schema

    * Noticed that contract first was uncommon at Zendesk

    * Not recording all of the schema details first in a contract makes the devolpment process much harder

    * Contract first vs Code first

      * Seen it in Catkins protobuf / grpc

      * Kristoffer - explore data and collections

      * Using protobuf as a tool to talk about schemas with Explore team

    * Product shouldn't be looking at the code, but outward facing contract is interesting

      * Can't do that code first

    * Cheaper to change a contract

    * Used GraphQL under the hood power the queries

    * Nice templating to describe the types and how it maps to graphql, then generates the OpenAPI

    * [Endpoints are authored in Typescript using a library](https://github.com/zendesk/guide-rest/blob/33e841ab3ad97642c6fce830cae66ca0990b6cf9/apps/server/src/modules/community-badges/components/badge.ts)

  * Explore integration

    * Driven by dashboard mockups, by a designer and PM with no real deep knowledge of what data existed

      * Worked backwards from there to figure out which fields are needed

      * Process has evolved to use prototyping so that you could see

      * Previously was driven by lo-fi definition in a dataset

      * [Currently describe prototype dataset in yaml](https://github.com/zendesk/explore_datasets_manager/pull/16/files)

        * Once agreed upon, turns into a protobuf schema which becomes the contract in the collection service and the point of reference

        * Part of explore

        * Starts out low fidelity in yaml, higher fidelity in protobuf

        * Quick turnaround

        * Loads it into a test instance in Staging it

        * Lets people click around and understand it, hands on experience

      * Guide and Sell provided feedback on providing datasets

        * Also desire to become more self-service in Explore

        * Self service lets there be more async work at higher velocity

    * Events in Guide

      * Piratos - guide data platform team

      * Split into domain events and activity events

      * Domain events have an effect on the domain object, activity don't

      * Domain events only exist if change was applied

        * Using Escape now, originally using maxwell

      * Entity streams and standard objects

        * Entity streams not PDA compliant yet, but desire to

        * Article Standard object for Explore integration

        * Want to deprecate entity streams because we get stuff for free

      * Looking at standardizing activity events

        * Higher volume

        * Best effort semantics instead of transactional

        * Don't usually denormalize

        * That needs to happen for explore, eg. article title from standard into activity event

        * Denormalisation happens in ETL layer of explore

      * Conversation now around how explore can use data sets and join with others

      * Can we view articles as a common dataset for customers, what does that mean aside from technical integration, do we need to do customer specific documentaion

      * Not everything is the same for all accounts

        * eg. plan gating

        * sometimes usage

        * can't have gather without guide

        * schemas are consistent across acounts

        * no custom, structured data in guide or gather

      * Content blocks

        * Whole new format for article

        * New entity / entity stream

        * Schema is common across acounts

        * No customer defined content blocks

        * Some desire to embed other data types, but too early to talk much about

        * Domain Boundary

          * Content Block standard entity shows rendered content for standard objects

          * Earlier in the pipeline, but not trying to leak implementation details

          * Makes it easy for others to use output without having to deal with rendering the objects

          * Precomputed

          * Apps in articles probably not rendered, some things may render differently depending on channel (eg help center, vs widget vs AW)

      * Discoverability

        * It would be nice if we could ___, can you build us an event stream

          * Often times it already exists

        * Documentation

          * Spend a lot of time explaining how things are interconnected and how to use it

          * Ask can we use it, might be an internal representation, etc

          * If you don't know how to exercise a code path to emit an event

      * Customer Context timeline

        * Built on Activity Events

        * Do we map them to something more stable

      * Activity events from before event definitions were layed down activity vs domain

        * Want to deprecate

        * Had to find consumers datadog metrics to see what consumer groups were consuming what topics

        * Schema registry is useful not just to show schemas but who is using them

        * service.yml to generate ACLs

        * self-service reduces friction

      * We need to put requirements on consumers, when we have a dataset we may have deletion requirements

        * How to we broadcast deletion requirements

        * Easy enough for things that are tombstone-able

        * Normal retention topics teams need to know when to delete, AND make sure that happens and bring peace of mind  





### Sell

Contact: 

### Explore

**Recording:** <https://zendesk.zoom.us/rec/share/mVl3MrHLHik-Di38tdTAinOJtbTuIeqvey0NZrerSD219D6aGM5N9Q-8bSuOWnOz.vtY3-LV5BaIYod5k>

**Passcode:** 6&b.pWZi

Contact: 

  * TODO -  to transcribe handwritten notes




### Explore & Data Mesh

Contact: 

### Foundation Storage

Contact: 

### EDA / Enterprise Analytics 

Contact:

---

### Platform Schema & Metadata WG: Proof of Concept

**Page ID:** 4627992983  
**Version:** 2  
**Last Updated:** 2021-03-05  
**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4627992983](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4627992983)  

#### Data Engineering Context

*This section covers platform-level data engineering concepts relevant to PDD and EDA initiatives.*

One of the key deliverables for the Working Group is a working End-to-end POC that demonstrates the value of a Metadata Registry.

## Metadata aspects to demonstrate

  * Use of data types

  * Use of fields in data types

  * Dynamic population of forms / views based on metadata & schena

  * Use of semantic information from metadata

  * Use of relationship descriptions

  * Querying for data types by some criteria

    * eg. "datatypes that have a relationship to a Ticket", "datatypes that can be used in a trigger"




## Ideas

  * Omnipanel UI configuration

    * Allow admins to pick extra data to show in the Omnipanel

    * Select from datatypes that relate to a Ticket / User / Org

    * Select which fields show up

    * Readonly? Read/write? Dynamic form in Omnipanel for updating info or creating related records?

    * Very similar to data management stuff that  and co have been talking to

  * OneGraph

    * Demo from  had papered over some of the aggregation of metadata, but we could try and implement it properly for consumption by OneGraph

  * App Settings UI

    * notes here: <https://docs.google.com/document/d/1Wf5N7bDaLCBLn4eJjeF2yvBdnnmPd9itiqLCqtMbwUA/edit#heading=h.7gxdxlluxgv0>

  * Admin pages driven from object metadata

    * We're hoping to offer low code or auto layout solutions for simple admin layouts and flows. These would be driven by a "schema definition" for the structure of a form, table etc

    * Supply the schema of an admin data type, like a staff record, or a custom ticket field, via OneGraph

    * Derive a list control and CRUD forms from the metadata

---

### Platform Schema & Metadata WG: Research - Competitor analysis

**Page ID:** 4627993579  
**Version:** 2  
**Last Updated:** 2021-06-18  
**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4627993579](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4627993579)  

#### Data Engineering Context

*This section covers platform-level data engineering concepts relevant to PDD and EDA initiatives.*

There are examples across the enterprise SaaS space of implementations of metadata or reflection APIs.

## Salesforce

Salesforce have a set of "describe" calls to gather metadata at about various aspects of their products.

Docs: <https://developer.salesforce.com/docs/atlas.en-us.230.0.api.meta/api/sforce_api_calls_list_describe.htm>

Call| Description  
---|---  
[describeAllTabs()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describealltabs.htm#topic-title)| Returns information about all the tabs--including Lightning page tabs--available to the logged-in user, regardless of whether the user has chosen to hide tabs in his own user interface via the All Tabs (**+**) tab customization feature.  
[describeAppMenu()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describeappmenu.htm)| Retrieves metadata about items either in the Salesforce mobile app navigation menu or the Salesforce drop-down app menu.  
[describeApprovalLayout()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describeapprovallayout.htm)| Retrieves metadata about approval layouts for the specified object type.  
[describeAvailableQuickActions()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describeavailablequickactions.htm)| In API version 28.0, describes details about actions available for a specified parent. In API version 29.0 and greater, describes details about actions available for a specified context.  
[describeCompactLayouts()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describecompactlayouts.htm)| Retrieves metadata about compact layouts for the specified object type.  
[describeDataCategoryGroups()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describedatacategorygroups.htm#sforce_api_calls_describedatacategorygroups)| Retrieves available category groups for entities specified in the request.  
[describeDataCategoryGroupStructures()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describedatacategorygroupstructures.htm#sforce_api_calls_describedatacategorygroupstructures)| Retrieves available category groups along with their data category structure for entities specified in the request.  
[describeGlobal()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describeglobal.htm#topic-title)| Retrieves a list of available objects for your organization's data.  
[describeGlobalTheme()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describeglobaltheme.htm)| Returns information about both objects and themes available to the current logged-in user.  
[describeKnowledge()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describeknowledge.htm#sforce_api_calls_describeknowledge)| Retrieves the Knowledge language settings in the organization.  
[describeLayout()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describelayout.htm#topic-title)| Retrieves metadata about page layouts for the specified object type.  
[describePrimaryCompactLayouts()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describeprimarycompactlayouts.htm)| Retrieves metadata about the primary compact layout for each of the specified object types.  
[describeQuickActions()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describequickactions.htm)| Retrieves details about specified actions.  
[describeSearchScopeOrder()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describesearchscopeorder.htm)| Retrieves an ordered list of objects in the logged-in user's default global search scope, including any pinned objects in the user's search results page.  
[**describeSObject()**](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describesobject.htm#topic-title)| **Retrieves metadata (field list and object properties) for the specified object type. Superseded by  **[**describeSObjects()**](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describesobjects.htm#topic-title)**.**  
[**describeSObjects()**](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describesobjects.htm#topic-title)| **An array-based version of describeSObject.**  
[describeSoftphoneLayout()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describesoftphonelayout.htm#topic-title)| Describes the softPhone layout(s) created for an organization.  
describeSoqlListViews()| Retrieves the SOQL query and other information about a list view.  
[describeTabs()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describetabs.htm#topic-title)| Returns information about the standard and custom apps available to the logged-in user, as listed in the Lightning Platform app menu at the top of the page.  
[describeTheme()](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describetheme.htm)| Returns information about themes available to the current logged-in user.  
  
They are all definitely interesting, but in the case of this WG, `describeSObject` is the most relevant.

  * _Retrieves metadata (field list and object properties) for the specified object type.._




<https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_calls_describesobjects_describesobjectresult.htm>

There is some symmetry between the Salesforce `SObject` and our `ZObject`s, but note that the [Salesforce SObject is a much more concrete ](https://trailhead.salesforce.com/en/content/learn/v/modules/apex_database/apex_database_sobjects )concept.

### Parts of an SObject description

The SObject description has many different responsibilities that are somewhat interleaved in a relatively flat representation. Some of the properties specified don't seem to apply to _all_ SObject types.

  * Capabilities of the object

    * `activateable`,`compactLayoutable`,`createable`,

`dataTranslationEnabled`,`deepCloneable`,`deletable`,`feedEnabled`,`layoutable`,`mergeable`,`mruEnabled`,`queryable`,`replicateable`,`retrieveable`,`searchable`,`searchLayoutable`,`triggerable`,`undeletable`,`updateable`

  * Links to CRUD pages for the object

    * `urlDetail`,`urlEdit`,`urlNew`,

  * Storage information

    * `keyPrefix`,`networkScopeFieldName`,

  * Custom Objects info

    * `custom`,`customSetting`

  * Array of "Field"s

    * Represents the schema of an object

    * Many of the properties appear to be only relevant to specific types of fields - I'm unsure if they're always returned regardless, or this if a Field is a sort of union type that will be only one of those at a time

    * Each field has some metadata of it's own

      * General descriptive information

        * `name`,`soapType`,

      * UI concerns

        * `controllerName`,`dependentPicklist`,`displayLocationInDecimal`,`extraTypeInfo`,`htmlFormatted`,`inlineHelpText`,`label`,`nameField`,`namePointing`,

      * Data type information

        * `autonumber`, `type`

          * `type` refers to a FieldType which is one of:

            * `string`, `boolean`, `int`, `double`, `date`, `datetime`, `base64`, `ID`, `reference`, `currency`, `textarea`, `percent`, `phone`, `url`, `email`, `combobox`, `picklist`, `multipicklist`, `anyType`, `location`

      * Validation & data constraints are captured in various properties of a Field

        * `bytelength`,`digits`,`length`,`nillable`,`picklistValues`,`precision`,`restrictedPicklist`,`scale`,`unique`

      * Capabilities of the field - eg. what features work with it

        * `createable`, `dataTranslationEnabled`,`filterable`,`groupable`,`filteredLookupInfo`,`permissionable`,`searchPrefilterable`,`sortable`,

`updateable`,`writeRequiresMasterRead`,

      * Information about the storage of the field

        * `encrypted`,`highScaleNumber`,`idLookup`

      * Defaults

        * `defaultedOnCreate`,`defaultValueFormula`,

      * Specifics of formula fields

        * `formula`,

      * Information to describe foreign key semantics

        * `polymorphicForeignKey`,`relationshipName`,`relationshipOrder`,`referenceTargetField`,`referenceTo`,




## Kustomer API

metadata: [https://dev.kustomer.com/v1/metadata/](https://dev.kustomer.com/v1/metadata/wLj8d55Qd3EBK2Aut)

get klass: <https://dev.kustomer.com/v1/klasses/get-kobject>

---

### Platform Schema & Metadata WG: POC - Schema Description Language

**Page ID:** 4948068369  
**Version:** 1  
**Last Updated:** 2021-06-18  
**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4948068369](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4948068369)  

#### Data Engineering Context

*This section covers platform-level data engineering concepts relevant to PDD and EDA initiatives.*

_WORK IN PROGRESS_

Some discussion has happened recently around what is the best format for describing data. We would like to bias toward something open source, with some off-the-shelf tooling, but extensible and expressive enough to allow us to annotate data types with some more domain and business specific metadata such as team ownership, regulatory information, or even i18n hinting.

The current theory is that perhaps [GraphQL SDL](https://graphql.org/learn/schema/) is sufficiently expressive as an authoring language to allow it to generate Protobuf schemas, or AWS Athena tables when provided with enough annotation. Lets try it, and discover if it is expressive enough for this use-case, or whether another technology is required.

---

### Platform Schema & Metadata WG: POC - Using service.yml to register PDA data sets

**Page ID:** 4948068402  
**Version:** 1  
**Last Updated:** 2021-06-18  
**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4948068402](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4948068402)  

#### Data Engineering Context

*This section covers platform-level data engineering concepts relevant to PDD and EDA initiatives.*

_WORK IN PROGRESS_

_  recently shared an RFC & draft ADR describing the use of service.yml as a mechanism for recording some information about PDA datasets._

_We would like to help Jason in any way that we can to understand the tradeoffs, and opportunities of leveraging the foundation interface to provide various automations in support of the PDA. Some possibilities include automation of Cerebro entries to replace the handcrafted  __Platform Data Registry_ _  page on confluence with something that can link to other interesting service catalog and team information. Other examples are automation of kafka topic creation, or collections in the collection service._

---

### Platform Schema & Metadata WG: POC - Data Catalog as a store for schema & metadata

**Page ID:** 4949016940  
**Version:** 1  
**Last Updated:** 2021-06-18  
**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4949016940](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4949016940)  

#### Data Engineering Context

*This section covers platform-level data engineering concepts relevant to PDD and EDA initiatives.*

_WORK IN PROGRESS_

 _After  _ _,  _ _  & _ _  had met up with some folks from _[_Acryl_](https://www.acryl.io/) _, the company that now shephards the LinkedIn  _[_DataHub_](https://github.com/linkedin/datahub) _  project. In the discussion, it was suggested that DataHub may be feasibly used to solve some of our platform metadata use-cases alongside those of the  _[_#proj-data-mesh_](https://zendesk.slack.com/archives/C01HVBFN18D) _._

_We would like some people to kick the tyres on it, and evaluate whether it would be fit for purpose, and learn a bit more about some of the practical aspects of working with that technology. Some members of this group are already engaged on the Data Mesh project, and this is a key area of overlap, so we would definitely intend to share this one._

---

### Platform Schema & Metadata WG: Research - should ZD and customer-defined data types be described by the same system

**Page ID:** 4949016984  
**Version:** 1  
**Last Updated:** 2021-06-18  
**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4949016984](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4949016984)  

#### Data Engineering Context

*This section covers platform-level data engineering concepts relevant to PDD and EDA initiatives.*

_WORK IN PROGRESS_

Another big question is whether or not we should try to house both Zendesk-defined data types alongside the Customer-defined ones (eg. extensions to existing objects as custom fields, or completely custom object or event types), or whether they are complementary or even layered systems.

As  rightly raised in the APAC/AMER WG meeting, the scope of the two is very different, where Zendesk types are potentially able to be managed fairly statically in a GitHub based workflow, customer-defined types are necessarily a runtime concern, and additionally bring with with all the considerations of our partition strategy.

---

### Platform Data Architecture Refresh, April 2021

**Page ID:** 4713916387  
**Version:** 1  
**Last Updated:** 2021-04-08  
**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4713916387](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4713916387)  

#### Data Engineering Context

*This section covers platform-level data engineering concepts relevant to PDD and EDA initiatives.*

When a strategy has become clearer and the concepts that were once novel are now taken for granted, it can make sense to go back and clean up the names and descriptions.

Such is the case with _Platform Data Architecture_. For various reasons we made the first steps towards the goal of a unified domain model for all of Zendesk, coupled with standardized access patterns and turn-key capabilities, within the realm of _streaming data_ , specifically Kafka topics containing [_events and so-called entity streams_](https://techmenu.zende.sk/standards/events/). Driven largely by the need to feed data into Explore and the Enterprise Data Warehouse from across our applications in a uniform, scalable manner, as well as the desire to consolidate and streamline how we index data into Elasticsearch, Kafka ended up being a cornerstone of the Platform Data Architecture.

For _One Graph_ , the initial focus was on aligning the effort with the [_One Zendesk strategy_](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/786935424/One+Zendesk+Strategy) at a high level rather than emphasizing the centrality of GraphQL in the platform. GraphQL was seeing rapid adoption across Zendesk, but with each product group building their own tools and services, we worried about divergence and wanted to steer the technology towards standardization and shared services. With the continued success of GraphQL at Zendesk, and the level of acceptance it has gained as a central technology, we feel it is now time to fold it into the Platform Data Architecture and promote it as a principal architectural component.

Therefore we now wish to update what we mean by Platform Data Architecture: what is the scope, what are the principal components, what does the future look like.

# Platform Data Architecture (PDA)

The _PDA_ is an overarching concept that provides a clear framework for executing on the [_One Zendesk strategy_](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/786935424/One+Zendesk+Strategy), which is centered around the goals of _horizontal integration and vertical decoupling_. The PDA is being actively grown, but is still in its early stages - we will continue to invest in and evolve it in the future. The PDA consists of the following primary components:

  * At the core of the PDA are the **Zendesk Objects** , or **ZObjects** , which is a comprehensive, cohesive, and consistent data model that spans all of our customer facing applications. This is a crucial foundation for _horizontal integration_ , providing any Zendesk application a shared view of the world. We want to surface this data model through a **Zendesk Data Catalog** to aid discoverability and understanding, and we want to govern it to ensure it is consistent and coherent - this governance process will result in a set of curated [**_Standard Objects_**](https://techmenu.zende.sk/adrs/platform-data-architecture-zendesk-objects/). In this regard, we have shared objectives with our Enterprise Data team who have already built solutions to some of these problems for their own needs. Lowering the barrier to teams contributing Zendesk Objects is vital in ensuring that we can make it comprehensive, while processes around standardization and best practices are key to ensure consistency and coherence.

  * A data model that only exists in the abstract is of little use and would quickly become out of touch with reality, so it's crucial to integrate access to data that follow the model. The first such data access integration is **Platform Data Streams** , consisting of the event and entity streams found in Kafka topics. The Protobuf schemas used to encode the data in the topics currently represent the data model - but we are in the process of figuring out how to represent Zendesk Objects in a higher level format that gives us more leverage, while still being able to generate e.g. Protobuf schemas for encoding data.

  * To complement the _streaming modality_ of data access, we are now incorporating the **Platform Data Graph** into the architecture to provide a _query modality_. This component, which we've described as _One Graph_ until now, represents a graph oriented view of Zendesk Objects, and allows front-end and mobile applications to query and act on data across the entire data model using the GraphQL protocol. We expect to have a majority of our data model represented in the Platform Data Graph by the end of 2021 by merging the Guide Graph and Support Graph projects and then continue to expand by incorporating the Sell Graph and any other applications in 2022. Currently, the schemas of our GraphQL endpoints have no direct relationship with the Protobuf schemas representing the same concepts in the Platform Data Streams, but after we get the fundamental aspects of running a single GraphQL gateway service taken care of we will start working on a unified system of describing schemas at a higher level across Streams, Graph, and any other modality or format that is deemed appropriate.




On top of these exist higher level capabilities:

  * The **Platform Data Collections Service** offers a way to index and stream entities or events of a specific type for a single account. This is already used to deliver data to Explore, but we envision this capability also being leveraged to support _universal data export_ and _account moves of Platform Data Streams_.

  * The [**_Platform Data Indexing Architecture_**](https://techmenu.zende.sk/adrs/platform-data-indexing-architecture/) provides a blueprint for indexing Platform Data Streams into Elasticsearch in a scalable, maintainable, and reliable manner. There are ongoing investigations about standardizing not just the _indexing_ of data for search, but also the _search capability_ itself, providing a unified search endpoint.

  * **Platform Data Mesh** provides a catalog of analytical datasets built from Platform Data Streams and augmented with other sources of data to support self-service analytics and data science use-cases.




In time, we hope to be able to add even more capabilities to this list, such as a universal UI Platform for rendering all parts of the Model into user interfaces and providing rich interactivity, GraphQL subscriptions driven by Streams, etc.

One important question is how the elevation of GraphQL to a core platform capability impacts our _API First_ principle of always releasing public REST APIs as part of GA'ing new features. We want to reiterate that REST is still how we expose public APIs to our customers and third party developers, and the adoption of GraphQL does not mean that teams are free from the requirement that they build REST endpoints for their features. In the short term, we see no change to how this is accomplished, but longer term we are interested in investigating the ability to leverage the Platform Data Graph itself to provide a dramatically more productive, consistent, and coherent REST API platform that allows teams to define REST routes in terms of GraphQL queries and mutations, using a heavily standardized or indeed centralized system. We are already seeing steps in this direction with e.g. [_guide-rest_](https://github.com/zendesk/guide-rest), which is a TypeScript service used by Guide teams to expose their GraphQL data and actions as REST endpoints. We will be spending more time on this subject in the future, and want to emphasize that we have not settled on any specific approach.

The role of these architectural concepts is to drive alignment and clarify communication - and therefore we need to make sure they reflect the current business objectives and the state of our organization and infrastructure, finding the right balance between feasibility and aspiration. We do not want our architectural "north star" to be disconnected from the reality of how we work, but we also need to define a future far enough out that we can confidently make multi-year investments and not worry about the direction changing _too much_. We hope this refresh will provide clarity for some time to come.

---


# Related Platform Data Documentation

The following pages provide additional context for data engineering and platform data initiatives:

## Export item by timestamp.html

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/att6747784765](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/att6747784765)  
**Last Updated:** 2025-01-02  

---

## How to drive testing at scale for cross functional projects

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5491852423](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5491852423)  
**Last Updated:** 2025-03-13  

Testing for cross functional projects is always a challenge and requires meticulous planning and co-ordination. Core services is at the center of most things Zendesk does, hence we are usually in the thick of things for large scale cross org projects, sometimes at a global scale. Here are some guidelines which I follow when leading testing efforts for such projects: 

  1. **Know your partners:**

     1. Program Manager - Make them your best friend

     2. Engineering Lead

     3. Product Lead

     4. Cross functional test leads

     5. If you manager is not directly involved, always keep them in loop. 

  2. **Know your project:**(PDD eg Product Discovery Document | Sell Bundle - Core Services ) This document needs to have clearly defined requirements and will be the single source of truth. 

     1. What - MVP

     2. Why - MVP


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5491852423)*

---

## Platform Data Architecture Program

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/866746601](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/866746601)  
**Last Updated:** 2021-07-30  

## ** Current Program Status**  
  
---  
Done. Milestone achieved! On track according to plan: no major, unmitigated risks or blockers. Needs attention: risk(s) w/potential impact on scope or schedule exists. significant threat will block/is blocking progress and/or delivery. Goal not met.| Weekly Status: 2020 H1 Product Development Programs **Summary of state of program at closing:** 51% - 75%Yellow

  * Not all datasets originally in scope have adopted the PDA
  * However, "we primed the pump well enough for PDA" . Some teams have adopted PDA and standards are in place.
  * Search track has been deprioritized until further notice

  
**Page Last Updated**|   
**Company Goal**|  CRM & Platform Solutions  
---|---  
**Key Result Goal**| ~~# of objects following the Core Objects reference Architecture~~  
# of datasets following the Platform Data architecture  
**Key Result Actual as at**|  50 ( 3 datasets)  
**How to Find Us**  
---  
**Slack Channels**| 


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/866746601)*

---

## Platform Data Architecture Program - Meeting minute

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/866650420](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/866650420)  
**Last Updated:** 2021-02-18  

## Related documents

Portfolio - Continue to advance adoption of the Zendesk OS and Common Architecture

Logistics

  * [Google shared drive](https://drive.google.com/drive/folders/1NSzugiuRvBV_WzWBqn8KCw1Vrvlxgu9S)

  * [OKR Alignment diagram](https://docs.google.com/presentation/d/1Y2bLr_TwxwL6xCFZ1mAfYFCVSNbRrGd3pbAz3YJ5Qcs/edit)e

  * Request for help to Support team: Platform Data Architecture




Program related Pages

  * Portfolio: Portfolio - Continue to advance adoption of the Zendesk OS and Common Architecture

  * [Platform Data Object - OKR breadkdown - Sheet](https://docs.google.com/spreadsheets/d/1zltSMuKH646zCJnzcQbb1sGh4LMtYsnGKsPnRSgtX6Y/edit#gid=0)

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/866650420)*

---

## 2025-30-09 EDA, ZAP and B-Team discuss Lineage project

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7518814209](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7518814209)  
**Last Updated:** 2025-10-02  

# Present

# Minutes

  * Walked through the Project Page: Data Lineage

  * Intermediate metadata file

    * Cannot be just one file, will get manageable

    * Generation from DBT Manifest is really important

    * Can extend tools as we add more metadata natively in DBT

    * DBT is not the only user of this file



  * We are absolutely ok (even more excited actually) for the Metadata as Code implementation to continue!


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7518814209)*

---

## 2025-08-08 EDA and Wollemi discuss Workday Data Location

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7424540801](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7424540801)  
**Last Updated:** 2025-08-27  

# Present

# Minutes

  * Concerns

    * SaaS account is for our business, may not fit

    * Security

      * Service accounts can bypass

      * DEV_DBT_ROLE and others

      * How do we limit visilbiity of this data?

    * Fragmentation - how many accounts will we have?

  * Disadvantages of a new account


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7424540801)*

---

## Re: ZDP_META for CADD

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7384006758](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7384006758)  
**Last Updated:** 2025-08-04  

I have added the references of usage below. If we want to sure, then we will have to make a slack post tagging EDA and PA to get their confirmations.

---

## 2025-07-29 Foundation CADD Alignment

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7368311106](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7368311106)  
**Last Updated:** 2025-07-30  

# Present

# Minutes

  * Tables missing the meta and deleted columns

    * These columns provide details on whether the row is active

    * Past EDA queries have not had to deal with deletion, so this is new

    * Do we run it weekly?

      * If the live list of accounts that are churned is available, we no longer need the cadence to be that regular

    * Suggestion: run the 500 account scrub anyway and then do it again when methodology is locked.

      * Expensive

      * We are running late on commitments


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7368311106)*

---

## ZDM Snowflake Access Details Page Performance Analysis

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7351174163](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7351174163)  
**Last Updated:** 2025-07-24  

This page is created to demonstrate the work done for spike card SSD-3816cae89f0e-c846-3d65-88a5-bb277a2031b3System Jira . This page provides analysis of why is this page taking more time to load and time for tab switch. It also provides various approaches to improve performance of this page and tab switching.  
  
ZDM : Snowflake Access -> Access Name. This loads following page with 5 tabs for steward/owner/admin.   
Overview, Manage Access, Dataset Information, Pending Requests, Delete Dataset Collection  
For other users, this page loads 3 tabs.  
Overview, Manage Access, Dataset Information  
  
By using below code, got idea, which methods are taking how much time.  
`const fetchData = async () => { `

` console.time('fetchData');`

…….  
`console.timeEnd('fetchData');`

}  
  
Above logic is implemented for all fetch methods and got idea below time is taken by methods.  
For access Quality Assurance has 4922 users. Loading this access,


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7351174163)*

---

## Alation Feedback

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7346618415](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7346618415)  
**Last Updated:** 2025-10-08  

none

This page summarises pain points, challenges, and suggestions from Zendesk team members regarding Alation as our enterprise data catalog. The feedback below reflects real user experiences and highlights both technical and usability gaps, as well as recommendations for product improvements and workflow enhancements.

* * *

## Summary of Feedback

### Major Themes & Pain Points

#### 1\. **Lineage and Impact Analysis**

  * **Snowflake-centric Lineage:** Current dependency lineage is limited to Snowflake and does not automatically integrate with BI tools (e.g., Tableau, Looker, Coefficient). This limits end-to-end impact analysis, especially for downstream consumers.

  * **Incomplete/Unreliable Analysis:** Missing or inaccurate lineage hinders incident response and schema change management, forcing time-consuming manual workarounds.

  * **Export/Actionability Issues:** Impact analysis exports lack actionable details (object names, ownership info, integration with external tools).

  * **Unclear Updates:** Users are unsure when or how lineage information is refreshed, making them hesitant to trust Alation's impact analysis.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7346618415)*

---

## Foundational Models - workshop - Decisions

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7316078978](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7316078978)  
**Last Updated:** 2025-07-03  

Workshop Date| 2nd July, 2025  
---|---  
Attendees|   
  
# Decisions 

  * Definition: What are Foundational Models

    * Foundational models are data assets capturing business critical metric, and are operationally monitored for data quality and availability.

  * Rover will own only a part of the foundational layer, the part which directly relates to BCM(aka P0 metrics)

  * Rover will inform Product Analytics when starting the work on each table to prevent further changes to that table and its business logic. If a change is needed that needs to be communicated to Rover, so that we can make the same changes to the moved model.

  * Foundational Modelling principles are applied to every table we move to Foundational layer. High level foundational modelling is defined [here](https://lucid.app/lucidspark/13e05f8f-11f5-42ab-bd1d-78e1d17402f4/edit?beaconFlowId=10485F4136283CE7&invitationId=inv_8110cc15-de73-485b-95a4-c29b79e689a6&page=0_0#). 

  * Rover will work with Product Analytics(or EDA) when new BCM is being defined to check if that can be built on top of existing Foundational

    * This is being done to prevent more functional models being added while we move models to foundational.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7316078978)*

---

## 2025-07-02 EDA and B-Team Sync on DEV DBT ROLE

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7311360002](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7311360002)  
**Last Updated:** 2025-08-21  

# Present

# Minutes

  * Went over DEV DBT ROLE deprecation

    * <https://docs.google.com/document/d/1qsRnUkkZxab9SYAhOdIQ6HaD0gkyBMQNpNDRzj5UQh4/edit?tab=t.0>

    * Suggestion that we just co-ordinate and have a short period of disruption

  * Main point of discussion is the DEV Databases

  * Methods of resolving DEV databases

    * Mirror masking policies from production to DEV

      * Only SaaS, Global and Internal Tools

      * Expensive, but probably most complete option


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7311360002)*

---

## Legacy Data Lake Deprecation

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7215318016](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7215318016)  
**Last Updated:** 2025-11-07  

# Introduction

Now that ZDP is up and running we can begin to dissect and decommission elements of the Legacy Data Lake to optimise cost and deduplicate work based on Legacy Data Lake EOL Discovery . 

none

* * *

# Legacy Data Lake Components

This diagram shows all processing in the legacy datalake and the datasets involved. This forms the basis for the deprecation plan.

1falsesimpleleft11e28e961-4643-4ea1-8de9-327ea0e694b4Confluence:208381722670033cc7c9f-c6ed-400c-a600-9b33cb085135v2_7b3d1253414377584ce07c6a7698a9b78b32c99cc390bf12b2aae381b2ef1e0f-a=103589275&c=Confluence%3A2083817226&d=33cc7c9f-c6ed-400c-a600-9b33cb085135&p=72153180161762484654472500

Lucid Diagrams

  * [High level diagram](https://lucid.app/lucidchart/33cc7c9f-c6ed-400c-a600-9b33cb085135/edit?invitationId=inv_44c099ac-70f3-45a0-bd92-c9fa4ed840f1&page=0_0#) \- the one shown on this page

  * [Dependency Diagram](https://lucid.app/lucidchart/17e6d6e6-1639-4345-a18c-117e258e82c5/edit?page=0_0&invitationId=inv_e916ad8c-259a-4e4a-b5cc-3fb6f4ee7bdd#) \- All dataset dependencies for the entire legacy datalake


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7215318016)*

---

## 2025-05-20 EDA and Wollemi discuss Feature Databases and Shared Sandboxes

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7199850502](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7199850502)  
**Last Updated:** 2025-05-22  

# Present

# Minutes

  * Recapped DEV_DBT_ROLE

    * [Too widespread, several hundred users](https://docs.google.com/spreadsheets/d/1mixhc6BM31AMrQpU_FXWEnW_r7bPK3fsP4BTiMHfl-E/edit?gid=396349981#gid=396349981)

    * means you have access to all feature databases, 

    * Does not suit finance/sensitive data development as anyone who has DEV_DBT_ROLE can look at data in any featureDB

    * Some people are using this role to bypasses access system, which discourages sensitive data from being ingested to ZDP

    * Leadership has come to a decision to deprecate this role on July 10, 2025 and there will be no more extension for this role

  * What people use the role for

    * DBT Development, specifically creation and usage of feature databases


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7199850502)*

---

## Re: Sandbox Sharing Rules and Restrictions

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6912311385](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6912311385)  
**Last Updated:** 2025-02-13  

I was going to leave a similar comment. The analyst teams don't all sit in EDA so we should make this more generic to just analyst teams.

---

## Re: Sandbox Sharing Rules and Restrictions

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6908576419](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6908576419)  
**Last Updated:** 2025-02-12  

to be clear there are collectively more analysts in teams scattered around the company in a number of different in-function teams vs the pool of EDA analysts. So we would want to make sure we have the correct teams listed, and to have a way to add to the list of cleared teams. (In total it is maybe like ~15 different teams of "analysts" / "data / ML engineers" by job title, and then an unknown number of 'lite analysts' in an unknown (but probably roughly equal) number of ops and Prod Dev teams that make up a wider outer asteroid belt of users (who have the same user needs as our mainline 'analysts/data / ML engineers' but have them intermittently) in the Zendesk data universe, so to speak)

---

## DEV_DBT_ROLE analysis

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6840123495](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6840123495)  
**Last Updated:** 2025-07-01  

none

# Introduction

This page is used to describe and summarise the scope of DEV_DBT_ROLE and all privileges granted to it.

The role is managed through Terraform and it exists in all Snowflake accounts - Dev, Staging and Production. The definition of this role is stored in YAML files in [zdp-snowflake-infra github repository](https://github.com/search?q=repo%3Azendesk%2Fzdp-snowflake-infra%20DEV_DBT_ROLE&type=code).

# How is the role assigned to users?

The DEV_DBT_ROLE is assigned to anyone who is using DBT at Zendesk to perform various tasks. Those employee come from different parts of Organization, such as:

  * Various Engineering teams (Foundation, Explore, Machine Learning Eng, etc)

  * Enterprise Data and Analytics

  * Sales

  * Finance


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6840123495)*

---

## S3 Ingester

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6624084008](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6624084008)  
**Last Updated:** 2025-05-17  

# Important Information

## About this Project

**Epic Owner**|   
---|---  
**Epics**|  FDB-4263cae89f0e-c846-3d65-88a5-bb277a2031b3System Jira  
**Metrics**| 

  * How much does it cost to ingest API gateway logs into snowflake per month?
  * How many projects are using the API gateway logs

  
  
## Objectives

As part of the GCP end of life program, we want to ensure that EDA can calculate all the statistics they need to in regard to API usage. This means we need to import a source of data for which endpoints are being hit. That source the API Gateway Logs, which are available in S3.

## What does success look like?


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6624084008)*

---

## SOC2 Controls for User Roles

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6528369274](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6528369274)  
**Last Updated:** 2024-11-14  

none

There are two different categories of Users and Roles and how we provision access to Snowflake for each - for **humans** and for **services**.

# Human Access

## The general access

For general access to Snowflake, which includes granting employees the Public access to Snowflake accounts via Okta, the flow is:

  * an employee goes to Okta, navigates to the ProductivApp and submits access to Snowflake via ProductivApp

  * the Wollemi team (the snowflake approvers) reviews and approves the request

  * the request goes back to the IT team, who grants access and assigns the Public role to that employee




The employees that belong to either Engineering (300+) or Enterprise Data and Analytics (741) get access by default, while employees from other departments still need to submit ProductivApp requests.

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6528369274)*

---

## ZDP Enablement Videos

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6496518386](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6496518386)  
**Last Updated:** 2024-12-11  

## Important information  
  
**Key contacts**|   
---|---  
**Objective**|  Create enablement videos on key topics surrounding ZDP to better support our users   
**Tickets**|  FDB-4106cae89f0e-c846-3d65-88a5-bb277a2031b3System Jira  
**Due date**|  December 31 2024  
**Status**|  in progressYellow  
  
## What is going on?

As the Zendesk Data Platform (ZDP) continues to roll-out to all teams in prod-dev, we need to ensure we are providing the best support material to our stakeholders. In order to get teams a deeper understanding on key areas across ZDP, we have decided to release a small suite of videos introducing end-users to different realms of ZDP.

## Why are we doing this?

We can answer a lot of questions by explaining in videos via walkthroughs on specific topics within ZDP. The goal here is for whenever an interested Zendeskian navigates to our [ZDP homepage ](https://zendeskdev.zendesk.com/hc/en-us/p/zendesk-data-platform)they can choose to read our copious amounts of documentation, or select a topic they want to watch a quick bite-size video on.

## How will we do this?

Adi has identified 7 topics which we need to develop enablement videos for as per the below. We intend to release one video per week starting 1st November.

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6496518386)*

---

## Deleted Legacy Datastore Cost Savings

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6479708251](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6479708251)  
**Last Updated:** 2024-10-08  

As of 8th October 2024, participating CDP scrum teams have identified legacy datastores they either have deleted or expect to delete in the very near future, which saves costs on unnecessary datastores.

## Deleted Datastores

To date (8th October 2024) we have 100 datastores no longer required hard deleted. At the point in time of this assessment, we are only able to gain the actual cost-saving information for those deleted within the last 30 days, therefore this number may be greater, however for those we could identify information for are listed below. These figures were taken by using the Cost Explorer function in AWS console.

There were 21 of the 100 that we could gather information on as per the below:

**Datastore Name**| **Owner**| **Type**| **Cost per month**| **Cost per annum**  
---|---|---|---|---  
customer-config-history-redis-pod17| sandbox platform| redis| $9| $108  
customer-config-history-redis-pod29| sandbox platform| redis| $9| $108  
podzilla-lambda-staging-area-pod13| | S3| $1| $12  
Torch_Alpha_SearchRoutingAudits| Torch| DynamoDB| $1| $12  
Torch_Alpha_SearchRoutings| Torch| DynamoDB| $1| $12  
Torch_Alpha_WhaleAccountAudits| Torch| DynamoDB| $1| $12  
Torch_Alpha_WhaleAccounts| Torch| DynamoDB| $1| $12  
Torch_SearchRoutingAudits| Torch| DynamoDB| $1| $12  
Torch_SearchRoutings| Torch| DynamoDB| $1| $12  
Torch_WhaleAccountAudits| Torch| DynamoDB| $1| $12  

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6479708251)*

---

## ZDP: Cost Modelling

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6468337898](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6468337898)  
**Last Updated:** 2024-11-06  

# Important Information  
  
**Epic Owner**|   
---|---  
**Epics**|  FDB-3890cae89f0e-c846-3d65-88a5-bb277a2031b3System Jira  
  
# Objectives

We should be able to clearly see costs in snowflake and how they relate to various components of work.

# In Brief

Estimating the cost of ZDP with reasonable accuracy for financial reports

61false.*Brief.*nonelisttrue

# Details

## Typical ZDP Project Data Flow


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6468337898)*

---

## Integrating Pendo for to track MCT activation and adoption

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6376948933](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6376948933)  
**Last Updated:** 2024-08-12  

This article will help you to understand scope of work : Pendo for MCT adoption and activation

  1. MCT adoption on Pendo

  2. MCT activation on Pendo




##  Instructions

Step by step process 

  1. Created a Pendo account and upgraded the access to 'tagging and editor'!

  2. Already had an Zendesk_Product account where the MCT was already enabled.

  3. Tracking the data

     1. Created a page as per taxonomy - Support_ModifyClosedTicket

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6376948933)*

---

## 2022-07-28: Kick Off - ECR Migration

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6209929484](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6209929484)  
**Last Updated:** 2024-05-14  

Post by Sheilina Ryan

Hello EveryoneWe are excited to bring to you the ECR Migration - Kick Off which, considering the broad reach across all timezones, will be handled asynchronously!Fear not! You can join the regional office hours where we can go through some of the material and run through some hand on tutorials together.Below is all the information you need! You can also access all information on our program page, reach us at #ask-gcr-ecr-migration or pop into on of your timezone friendly office hours to get hands on help! Kick off & Migration Information

  * [Kickoff Deck](https://docs.google.com/presentation/d/12ttdo1isMCU5ljsZRlVC0B81M4gLqgH3LSkqZa2q9iE/edit#slide=id.g130cd0e253b_0_10)

  * [Video overview for engineers](https://drive.google.com/file/d/1hFp52T6SYbtTAdcgNvG0q0_jL6k35NUS/view)

  * [Migration overview](https://docs.google.com/presentation/d/1oY8MNI3OiX4F7XUuNYpyDl6e7u5hPks2W1mKHzcufkk/edit#slide=id.g13d176176f3_0_25)




Office Hours ScheduleWe have scheduled regional office hours and we plan on these sessions to be hands on. Please join us in one of the sessions to perform your migration, follow one of our tutorials and of course bring along any questions for us to answer! Office Hours: Link to event - " target="_blank">Add to your calendar Office Hours: Link to event - " target="_blank">Add to your calendarProgram ScheduleThe GCR-ECR Migration program is one of our top priorities in Q3, so, with your help, we aim at getting the bulk of the migration work done within the Q3 timeframe.The team has recently explored an opportunity to make the migration even easier for you - A "Sidecar" initiative has been implemented and this takes into account dependencies between services and will make it easier for teams to migrate to ECR with minimal manual intervention.Here is what our latest program schedule looks like:Automated PR Availability dates for teams:Aug 05 Foundation-Cloud teamsAug 22 Support & ExploreSep 02 Dev Platform, Foundation-Storage & EP teams, Guide, Chat, SRE, Foundation-Data, Messaging, Core Services, EDA, G&M, Machine Learning, Security, Support-Platform, Talk, Explore, SunCo, IT, Mobile, EOL, ZOS, Resilience, Globalization, Foundation Eng & Architecture teamsMigration Target completion dates for teams:Aug 26 Foundation-Cloud images converted to ECRSep 16 Support & Explore images converted to ECRSep 30 Sell images converted to ECROct 15 Dev Platform, Foundation-Storage, EP, Guide, Chat, SRE, Foundation-Data, Messaging, Core Services, EDA, G&M, Machine Learning, Security, Support-Platform, Talk, Explore, SunCo, IT, Mobile, EOL, ZOS, Resilience, Globalization, Foundation Eng & Architecture images converted to ECR HousekeepingTo ensure the smooth running of the program we ask you to please

  1. Link your team's epic to the milestones relevant for your team under the [GCR to ECR Migration Project](https://zendesk.atlassian.net/browse/PLAN-326).

  2. Plan for the migration to start as soon as the PRs are available for your team; please have resources ready



*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6209929484)*

---

## Re: 2023-04-26: Restoring JIG metrics to PDW

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6196007916](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6196007916)  
**Last Updated:** 2024-05-07  

//slack-preserver url=https://zendesk.slack.com/archives/CSDSKKFHS/p1677860244072059 page=0

Show thread

#database-operations \--- (rama.tallapaneni) @ Fri, 03 Mar 2023 16:17:24 UTC wrote: <@UA60E1HV1> Can you please help here ``` Failure running task 'jig_metrics' in task list: dial tcp: lookup <http://prod-use1-jigdb-dbcluster-1tls7ycvdov87.cluster-ro-cxek2uttrqvw.us-east-1.rds.amazonaws.com|prod-use1-jigdb-dbcluster-1tls7ycvdov87.cluster-ro-cxek2uttrqvw.us-east-1.rds.amazonaws.com> on 169.254.1.1:53: no such host"``` \--- (rama.tallapaneni) @ Fri, 03 Mar 2023 16:18:02 UTC wrote: ```message: "Failure running task 'slack_integrations' in task list: dial tcp: lookup <http://slack-integration-db-cluster.pod13.usw2.zdsys.com|slack-integration-db-cluster.pod13.usw2.zdsys.com> on 169.254.1.1:53: no such host" subprocess: "collector"``` \--- Amit Agarwal (aagarwal) @ Fri, 03 Mar 2023 17:55:04 UTC wrote: Hi <@U03ANK43KD0>, this Aurora clusters has been upgraded to 2x and Graviton (With new end points) and old has been deleted yesterday as a part of <https://zendesk.atlassian.net/browse/DBA-26524|DBA-26524>. Please let me know if you need new cluster endpoint and it's going to be RO or RW end point? \--- Amit Agarwal (aagarwal) @ Fri, 03 Mar 2023 18:30:37 UTC wrote: Hi <@U03ANK43KD0> 1\. Please use "<http://jig-jig-pod19.cluster-ro-cxek2uttrqvw.us-east-1.rds.amazonaws.com|jig-jig-pod19.cluster-ro-cxek2uttrqvw.us-east-1.rds.amazonaws.com>" instead of "<http://prod-use1-jigdb-dbcluster-1tls7ycvdov87.cluster-ro-cxek2uttrqvw.us-east-1.rds.amazonaws.com|prod-use1-jigdb-dbcluster-1tls7ycvdov87.cluster-ro-cxek2uttrqvw.us-east-1.rds.amazonaws.com>" 2\. <http://slack-integration-db-cluster.pod13.usw2.zdsys.com|slack-integration-db-cluster.pod13.usw2.zdsys.com> is cname which was pointing to old cluster <http://slack-integration-db-dbcluster-1e44hs0ot6c8t.cluster-c9impiyapurt.us-west-2.rds.amazonaws.com|slack-integration-db-dbcluster-1e44hs0ot6c8t.cluster-c9impiyapurt.us-west-2.rds.amazonaws.com> and same has been updated with new entry <http://slack-integration-slack-integration-pod13.cluster-c9impiyapurt.us-west-2.rds.amazonaws.com|slack-integration-slack-integration-pod13.cluster-c9impiyapurt.us-west-2.rds.amazonaws.com> so please keep using the same cname. Please check and let me know if still an issue. Thank You. \--- Eric Salituro (esalituro) @ Fri, 03 Mar 2023 23:00:46 UTC wrote: <@U03ANK43KD0>: I fixed it. \--- Eric Salituro (esalituro) @ Fri, 03 Mar 2023 23:00:49 UTC wrote: Deploying now. \--- (rama.tallapaneni) @ Fri, 03 Mar 2023 23:34:50 UTC wrote: <@U5RU4663Y> after deploying we got the error like Error opening DB connection pdw_ro_1:***@tcp(<http://jig-jig-pod19.cluster-ro-cxek2uttrqvw.us-east-1.rds.amazonaws.com:3306|jig-jig-pod19.cluster-ro-cxek2uttrqvw.us-east-1.rds.amazonaws.com:3306>)/jig?parseTime=true: dial tcp 10.219.40.215:3306: connect: connection timed out cc<@UJYDL41RA> \--- (rama.tallapaneni) @ Fri, 03 Mar 2023 23:35:26 UTC wrote: <@U5RU4663Y> Error opening DB connection edw_ro_1:***@tcp(<http://slack-integration-db-cluster.pod13.usw2.zdsys.com:3306|slack-integration-db-cluster.pod13.usw2.zdsys.com:3306>)/slack_integration?parseTime=true: dial tcp 10.210.156.156:3306: connect: connection timed out cc <@UJYDL41RA> \--- Eric Salituro (esalituro) @ Fri, 03 Mar 2023 23:58:20 UTC wrote: DNS cache? \--- Amit Agarwal (aagarwal) @ Fri, 03 Mar 2023 23:58:34 UTC wrote: Hi <@UME8WS1U0>, Can you please confirm that you took care of Security Group from old Aurora cluster to new Aurora cluster for JIGDB and SLACKDB, i am asking for above mentioned issue? \--- Amit Agarwal (aagarwal) @ Sat, 04 Mar 2023 00:16:20 UTC wrote: Hi <@U03ANK43KD0> Temporary i created the Security Group and assigned to these 2 clusters, Can you please try again? \--- (rama.tallapaneni) @ Sat, 04 Mar 2023 00:18:00 UTC wrote: Sure \--- (asee) @ Sat, 04 Mar 2023 00:20:39 UTC wrote: We should have created a new security group for jigDB when provisioning self service \--- (asee) @ Sat, 04 Mar 2023 00:20:48 UTC wrote: Cc <@U02H47A5YP8> \--- (asee) @ Sat, 04 Mar 2023 00:20:52 UTC wrote: Cc <@U03FGMS3C93> \--- Amit Agarwal (aagarwal) @ Sat, 04 Mar 2023 00:22:08 UTC wrote: It might work or not <@U03ANK43KD0>, please let me know so i can try attaching the different existing SG. Thank You. \--- Eric Salituro (esalituro) @ Sat, 04 Mar 2023 00:38:18 UTC wrote: Unfortunately, tomorrow's run has started, so we won't know until it gets to the tasks in question sometime around 3h from now \--- Amit Agarwal (aagarwal) @ Sat, 04 Mar 2023 00:39:36 UTC wrote: Let me assign all the security group which i know of then. Thank You \--- Amit Agarwal (aagarwal) @ Sat, 04 Mar 2023 00:48:29 UTC wrote: It seems temporary created SG were wiped of from the cluster because of SAO operator and i can not assign existing one's for some reason. I am sure your task related to *slack and jigdb* will fail but unfortunately i do not have any workaround for that. \--- Luke Josh (luke.josh) @ Sat, 04 Mar 2023 01:02:17 UTC wrote: The security group for the new cluster will be managed by the aurora operator, any manual changes to the groups might be overwritten \--- Amit Agarwal (aagarwal) @ Sat, 04 Mar 2023 01:03:23 UTC wrote: Yes, i got to know with successful experiment :slightly_smiling_face: , thanks for confirming <@U02H47A5YP8> \--- Eric Salituro (esalituro) @ Mon, 06 Mar 2023 16:37:26 UTC wrote: Hey guys, what's the plan here? <@U5RU4663Y>: you were correct, the jig is up, so to speak. (as in, it hasn't worked for several days) \--- Luke Josh (luke.josh) @ Mon, 06 Mar 2023 21:50:54 UTC wrote: Hi friends, sorry for not replying to this earlier, I wasn't near my laptop over the weekend and it slipped my mind. This cluster has been migrated to self service aurora, during the process of which, the `edw` user would have been wiped. I can see two solutions to this: 1\. A DBA uses RIC to connect to the new cluster and creates this user manually. If this route is chosen, the user will have to continue to be manually rotated. ◦ Depending on _where_ this is connecting from, the security groups may get in the way, as I believe they are set up to only allow access from the kubernetes cluster the application is deployed in. 2\. Whatever is using this user authenticates using self service/temp auth instead of the static credential ◦ The service would need to be running in a k8 pod in the same k8 cluster as the application (pod19), and meet the requirements for temp auth (mostly, that the project is deployed in it's own namespace, and that the `project` label matches the name of the namespace) ◦ This is the preferred option, as the credentials will be automatically rotated cc <@U0LT7AN4R> \--- Amit Agarwal (aagarwal) @ Mon, 06 Mar 2023 22:51:23 UTC wrote: Hi <@U02H47A5YP8> User should not have been dropped because user information is part of data in database and will be coming to target instance with data. I guess it is problem of some ingress rule. \--- Luke Josh (luke.josh) @ Mon, 06 Mar 2023 22:56:01 UTC wrote: Hey Amit, we did drop the user for sure. We do this when migrating an instance into self service to ensure that there aren't any static users that are forgotten about that could become a security issue in the future. This generally relies on the assumption that the only client to the database is the service that is provisioning it… we'll do more investigation into this in the future to avoid this scenario \--- Amit Agarwal (aagarwal) @ Mon, 06 Mar 2023 22:57:32 UTC wrote: Can you please provide the list of users which you dropped ? it is really critical and can be dangerous. \--- Amit Agarwal (aagarwal) @ Mon, 06 Mar 2023 23:00:54 UTC wrote: Can you please confirm that you have dropped 1\. pdw_ro_1 ON <http://jig-jig-pod19.cluster-ro-cxek2uttrqvw.us-east-1.rds.amazonaws.com|jig-jig-pod19.cluster-ro-cxek2uttrqvw.us-east-1.rds.amazonaws.com> AND 2\. edw_ro_1 ON <http://slack-integration-db-cluster.pod13.usw2.zdsys.com|slack-integration-db-cluster.pod13.usw2.zdsys.com> \--- (asee) @ Mon, 06 Mar 2023 23:02:39 UTC wrote: I remember dropping edw_ro_1 when migrating the slack integration \--- Peter Nguyen (peter.nguyen) @ Mon, 06 Mar 2023 23:02:59 UTC wrote: same as for jig with pdw_ro \--- Luke Josh (luke.josh) @ Mon, 06 Mar 2023 23:04:01 UTC wrote: yeah we removed all users that weren't mysql/rds system users, so they will be gone \--- Amit Agarwal (aagarwal) @ Mon, 06 Mar 2023 23:05:23 UTC wrote: Hi <@UJYDL41RA> <@U03ANK43KD0>, please start using temp auth for your application and check with <@U02H47A5YP8> for procedure. Thank You. \--- Luke Josh (luke.josh) @ Mon, 06 Mar 2023 23:13:28 UTC wrote: happy to help :slightly_smiling_face: the process in general will be: 1\. <@UME8WS1U0> / <@U03FGMS3C93> can "share" the cluster with the app that needs access in the service.yaml file for jig/slack (<https://zendeskdev.zendesk.com/hc/en-us/articles/5245378295066-service-yml-Aurora-external-reference|ref>) 2\. the application that needs to access the cluster will need to add an `auroraExternal` resource to the infrastructure section of their service.yaml (see same link above) 3\. the application will then need to enable temp auth & config delivery, and consume the secrets delivered to the application by temp auth (<https://zendeskdev.zendesk.com/hc/en-us/articles/360011545640-How-do-I-connect-my-app-to-my-self-service-datastores-|see here>) As I said above, this does rely on the application being kubernetes based, and deployed in the same region as the cluster (pod13 & 19 for these two clusters). If this isn't the case we'll have to go for a different solution, but I'm happy to help work one out. \--- Eric Salituro (esalituro) @ Tue, 07 Mar 2023 00:25:11 UTC wrote: What do we need to do on our side? \--- Luke Josh (luke.josh) @ Tue, 07 Mar 2023 00:37:41 UTC wrote: Hi Eric -- step 2 and 3 above are what would need to be done on the application's side. If you share details of your project (github, cerebro etc) I'd be happy to provide more guidance \--- Eric Salituro (esalituro) @ Tue, 07 Mar 2023 00:39:10 UTC wrote: I can't see the link, so I'll need the boilerplate for the service.yaml \--- Luke Josh (luke.josh) @ Tue, 07 Mar 2023 00:40:43 UTC wrote: you'll need to be connected to the vpn in my guess; it's on the engineering help centre instance \--- Eric Salituro (esalituro) @ Tue, 07 Mar 2023 00:42:26 UTC wrote: I'm on the VPN. I'm getting a 404 for the page in question \--- Eric Salituro (esalituro) @ Tue, 07 Mar 2023 00:45:33 UTC wrote: I'm a little unclear as to what we're supposed to be modifying. For JIG and Slack we're have username/password authentication. Are you saying we have to use something else? \--- Luke Josh (luke.josh) @ Tue, 07 Mar 2023 00:48:49 UTC wrote: Sort of, the suggestion here is that you migrate to use temporary authentication, which is a system that provides application pods with a username and password on startup that is regularly rotated, rather than the static username and password you're currently using -- this is the standard way to access self service aurora clusters. I'm trying to work out why you can't access those help centre pages, bare with me :slightly_smiling_face: \--- Luke Josh (luke.josh) @ Tue, 07 Mar 2023 01:01:07 UTC wrote: I can't see any permission settings for those articles :thinking_face: can you access the home page? <https://zendeskdev.zendesk.com/hc/en-us> \--- Eric Salituro (esalituro) @ Tue, 07 Mar 2023 01:01:25 UTC wrote: yes \--- Luke Josh (luke.josh) @ Tue, 07 Mar 2023 01:02:19 UTC wrote: maybe an issue with the hyperlinks: <https://zendeskdev.zendesk.com/hc/en-us/articles/5245378295066-service-yml-Aurora-external-reference> <https://zendeskdev.zendesk.com/hc/en-us/articles/360011545640-How-do-I-connect-my-app-to-my-self-service-datastores-> do they work? \--- Eric Salituro (esalituro) @ Tue, 07 Mar 2023 01:03:54 UTC wrote: 1st one, no. 2nd one, yes \--- Eric Salituro (esalituro) @ Tue, 07 Mar 2023 01:08:48 UTC wrote: Is there some kind of naming convention that will tell me what the variables are called? \--- Luke Josh (luke.josh) @ Tue, 07 Mar 2023 01:13:21 UTC wrote: How annoying… not sure what is going on there, sorry. The jist from that article is the `auroraExternal` format for your `service.yaml`: ```infrastructure: auroraExternal: \- name: [db-name] attributes: externalClusterName: [external-db-name] externalClusterProject: [external-project-name] schemas: \- [schema_name] readOnlySchemas: \- [schema_name] ``` in the case where you want to access jig & slack, it'd be something like: ```infrastructure: auroraExternal: \- name: jig attributes: externalClusterName: jig externalClusterProject: jig schemas: \- jig \- name: slack attributes: externalClusterName: slack-integration externalClusterProject: slack-integration schemas: \- slack_integration``` (<@UME8WS1U0> <@U03FGMS3C93> could y'all confirm I got the schema names right above?) once you've done that, you can follow the second article on how to get the credentials, in a nutshell, they'll be located in: ```/secrets/MYSQL_jig_PASSWORD /secrets/MYSQL_jig_USERNAME /secrets/MYSQL_slack_PASSWORD /secrets/MYSQL_slack_USERNAME``` also note that the pegasus team will need to grant your project access to their cluster through a corresponding change in their service.yaml before this will work \--- Eric Salituro (esalituro) @ Tue, 07 Mar 2023 01:15:06 UTC wrote: ok, that makes more sense. And if I reference those variables in my Samson env, things should work? \--- Luke Josh (luke.josh) @ Tue, 07 Mar 2023 01:17:00 UTC wrote: By variables, you mean the location of those credential files? it should do, if your app is already loading them from a file provided by secrets sidecar or similar \--- Eric Salituro (esalituro) @ Tue, 07 Mar 2023 01:17:26 UTC wrote: secrets as per the second article \--- Eric Salituro (esalituro) @ Tue, 07 Mar 2023 01:18:26 UTC wrote: I'm trying to confirm the changes are limited to deployment, and not a code change \--- Luke Josh (luke.josh) @ Tue, 07 Mar 2023 01:29:40 UTC wrote: it's hard to say without knowing your app's db connection logic - if you currently read separate credentials for jig & slack, both from secret files provided by the secrets sidecar or similar, then it shouldn't require code change \--- Luke Josh (luke.josh) @ Thu, 09 Mar 2023 00:34:54 UTC wrote: hi <@UJYDL41RA> & <@U027X9VFL12> :wave: Just a follow up on our discussion this morning, I think we have a few action items: • Myself and Jeff will do some thinking on alternative solutions for access from PDW -> jig • Y'all will attempt a deploy to pod19 • I'll work with the pegasus team to "share" their aurora cluster with your project in their service yamls I do think the cleanest solution here is a deploy of pdw in pod19, as that will enable it to use temp auth without any exceptions / edge cases, and get all the goodness of automatic rotated credentials, etc., but obviously we are happy to work with you to find a solution if that is not feasible. I just wanted to highlight a couple of bits and pieces to help with your migration to self service now that I know a bit more about the architecture: • You'll need to add a bit of extra config to your `service.yaml` to ensure that the credentials are only fetched in the pods where the clusters exist ◦ we can use the `delete` parameter of the `auroraExternal` objects in your service yaml for this… it's a bit of an awkward name, but having `delete: true` on the object will prevent it from being created in the first place also ◦ this field can be parameterized by partition; you can follow jig's <https://github.com/zendesk/jig/blob/master/service.yml#L6-L16|service.yml> as an example (just for the parameterization & delete flag usage - you'll need to use an `auroraExternal` still, not an `aurora`) ▪︎ you can find the help center documentation for the variable replacement used above <https://zendeskdev.zendesk.com/hc/en-us/articles/4404594167706-Variable-Replacement-in-service-yml|here> • Please note that self service aurora clusters operate on *port 3307* and not the standard 3306 • Another thing to note is configuration delivery: this delivers config items (as opposed to secret items) for self service datastores. These are delivered in a similar manner (i.e., as files), but to the `/config/foundation` directory ◦ you can find all details on config that will be delivered <https://zendeskdev.zendesk.com/hc/en-us/articles/360014585480-How-do-I-get-my-Aurora-details-|here>, but note that both the `HOSTNAME` and `READER_HOSTNAME` are delivered here, so you can continue to connect to the reader in that way :slightly_smiling_face: ◦ the port is also delivered here, if you'd like to receive it in that method Please don't hesitate to reach out to us if you need a hand! we'll let you know if we can come up with any alternative methods of connection. \--- Eric Salituro (esalituro) @ Thu, 09 Mar 2023 00:40:58 UTC wrote: I've been told that we may have to make arrangements for our deployment on pod19 to communicate with our tracking db (<@U5RU4663Y> knows about it) \--- Amit Agarwal (aagarwal) @ Thu, 09 Mar 2023 00:51:30 UTC wrote: Hi <@UJYDL41RA>, What help you need from my side to make it happen? \--- Luke Josh (luke.josh) @ Tue, 14 Mar 2023 05:41:13 UTC wrote: hi friends, just a few updates from my side: • I've left some comments on the pull request <@U027X9VFL12> sent me, please let me know if I can help further • I spoke with <@UME8WS1U0> today regarding the changes required on the pegasus side - it will be just the small change to the `service.yml` in both the jig and slack projects • <@U0LT7AN4R> and I have discussed alternative possibilities if the pod19 deploy becomes prohibitively difficult. ◦ the only avenue we (as the owners of the aurora operator) can make from our side is to allow the sharing of secrets between pods in exceptional circumstances like this. We would _really_ *really* like to avoid this if at all possible, as it will make our planned transition to zvault (the podded vault) practically impossible, and will require quite a bit of work on the aurora operator which isn't likely to be quick ◦ the other option will be for the DBAs to create a static user using RIC. In this case I think the security groups attached to the self service cluster _may_ get in the way, but we can likely find a way to apply some one of rules/security groups to specific clusters by exception to patch this if that's the case :slightly_smiling_face: \--- (asee) @ Tue, 14 Mar 2023 05:42:47 UTC wrote: in order for me to update the service.yml I would need the project names :bow: \--- Luke Josh (luke.josh) @ Tue, 14 Mar 2023 05:43:04 UTC wrote: I can dig that out for you :loading: \--- Luke Josh (luke.josh) @ Tue, 14 Mar 2023 05:59:50 UTC wrote: ah sorry to be the bearer of (minor) bad news, but I've just noticed the service uses a namespace `product-data-warehouse-golang-version`, but <https://github.com/zendesk/product_data_warehouse_go/blob/master/kubernetes/collector.yml#L8|has a project label> of `pdw`. Temp auth requires these to be consistent - theres some more details as to the why of that <https://zendeskdev.zendesk.com/hc/en-us/articles/4417511905434-Why-it-s-important-to-ensure-your-project-labels-match-when-using-Zendesk-OS-Interface|here>. Eric & Treavien… can this label be updated also? Alvin, provided that label can be updated, the name for the `shareclusterWithProjects` parameter will be `product-data-warehouse-golang-version` \--- (asee) @ Tue, 14 Mar 2023 23:19:53 UTC wrote: I'll get PRs up and ready :bow: \--- (asee) @ Tue, 14 Mar 2023 23:48:09 UTC wrote: <https://github.com/zendesk/jig/pull/917> <https://github.com/zendesk/slack_integration/pull/819> \--- Treavien Holley (treavien.holley) @ Thu, 16 Mar 2023 22:18:31 UTC wrote: Hi <@U02H47A5YP8>, just to confirm only the project name in the collectors need to be updated from `pdw` -> `product-data-warehouse-golang-version`? Also, I have corrected some of those changes in the PR after your review if you wanted to take another look at those. \--- Luke Josh (luke.josh) @ Thu, 16 Mar 2023 23:46:49 UTC wrote: Hey Treavien -- I'm not 100% sure what you mean by collectors in this context; but the project label will need to match the namespace name for all pods that need to connect to the databases \--- Eric Salituro (esalituro) @ Thu, 16 Mar 2023 23:47:07 UTC wrote: pdw collectors -- the services \--- Treavien Holley (treavien.holley) @ Thu, 16 Mar 2023 23:47:43 UTC wrote: I am referring to your last message \--- Luke Josh (luke.josh) @ Fri, 17 Mar 2023 00:05:25 UTC wrote: Temp auth will only care about the project name, yes, but looking the `collector.yml` manifest, it is defined in a few places. I'd suggest updating this file to look like the following: ```--- apiVersion: apps/v1 kind: Deployment metadata: name: pdw-collector namespace: product-data-warehouse-golang-version labels: project: product-data-warehouse-golang-version role: collector team: eda-platform spec: selector: matchLabels: project: product-data-warehouse-golang-version role: collector template: metadata: name: pdw-collector labels: project: product-data-warehouse-golang-version role: collector team: eda-platform annotations: secret/KAFKA_SSL_CERT_KEY_BASE64: KAFKA_SSL_CERT_KEY_BASE64 secret/KAFKA_SSL_CERT_PEM_BASE64: KAFKA_SSL_CERT_PEM_BASE64 spec: containers: \- name: collector image: <http://gcr.io/docker-images-180022/apps/pdw:latest|gcr.io/docker-images-180022/apps/pdw:latest> # replaced during deploy command: ["/bin/sh","-c"] args: ["./pdw collector 2>&1 | logger --size 10240 -s -n 127.0.0.1 -P 5000 2>&1"] securityContext: runAsNonRoot: true readOnlyRootFilesystem: true readinessProbe: # when can traffic be sent in? httpGet: path: /z/ping port: 7778 initialDelaySeconds: 20 timeoutSeconds: 1 failureThreshold: 10 periodSeconds: 5 livenessProbe: # when should it be restarted ? httpGet: path: /z/ping port: 7778 initialDelaySeconds: 600 failureThreshold: 1 periodSeconds: 20 ports: \- containerPort: 8081 env: \- name: "TASK_GROUPS_TO_RUN" value: "main" \- name: POD_ROLE value: "collector" \- name: rsyslog-server image: <http://gcr.io/docker-images-180022/apps/pdw_rsyslog_sidecar:build|gcr.io/docker-images-180022/apps/pdw_rsyslog_sidecar:build> samson/dockerfile: none securityContext: runAsNonRoot: true readOnlyRootFilesystem: true ports: \- containerPort: 5000 name: upd protocol: UDP volumeMounts: \- name: tmp mountPath: /tmp \- name: certs mountPath: /etc/kafka/ssl resources: requests: cpu: "0.5" memory: "512M" limits: cpu: "1" memory: "1024M" volumes: \- name: tmp emptyDir: {} \- name: certs emptyDir: {} \--- apiVersion: v1 kind: Service metadata: name: pdw-collector namespace: product-data-warehouse-golang-version labels: project: product-data-warehouse-golang-version role: collector team: eda-platform consul-tag/diagnostic-http: "true" spec: ports: \- name: http port: 7777 selector: project: product-data-warehouse-golang-version role: collector``` Note however that the `selector` fields on deployments are immutable. So to get that updated, you'll need to delete & recreate it, rather than update it in place. You can do this with an annotation on the deployment, `'<http://strategy.spinnaker.io/recreate|strategy.spinnaker.io/recreate>': 'true'` which will cause spinnaker to just delete it and recreate it, rather than update it. Note that this will cause a short window where zero pods are running for the deployment \--- Treavien Holley (treavien.holley) @ Fri, 17 Mar 2023 15:18:04 UTC wrote: <@U02H47A5YP8> Just a heads up we are deploying this project with `Samson` not spinnaker. \--- Treavien Holley (treavien.holley) @ Mon, 20 Mar 2023 15:34:33 UTC wrote: <@U02H47A5YP8> <@UME8WS1U0>, I have corrected my PR now to match your request and will follow the next steps after they can be deployed. When would the PRs from the `jig` and `slack` repos be merged and deploy on your end? \--- (asee) @ Mon, 20 Mar 2023 22:10:05 UTC wrote: I will get to it today, we have a live incident for JIG and will have to allow that to resolve first \--- (asee) @ Mon, 20 Mar 2023 23:42:36 UTC wrote: deployed to Production \--- Luke Josh (luke.josh) @ Mon, 20 Mar 2023 23:45:56 UTC wrote: amazing thanks Alvin!!! Trea, apologies for the delayed response. You can achieve the same thing through Samson (deleting the deployment and creating it again in a subsequent deploy) - looks like you are on that track already looking at the samson project :slightly_smiling_face: <#C1DEPRE8K|ask-compute> will be able to help you out with this if you need I'll take another look at the pull request today \--- Treavien Holley (treavien.holley) @ Tue, 28 Mar 2023 19:29:44 UTC wrote: Hi <@U02H47A5YP8>, We're getting this error now for jig: ```Error opening DB connection pdw_ro_1:***@tcp(<http://jig-jig-pod19.cluster-ro-cxek2uttrqvw.us-east-1.rds.amazonaws.com:3306|jig-jig-pod19.cluster-ro-cxek2uttrqvw.us-east-1.rds.amazonaws.com:3306>)/jig?parseTime=true: dial tcp 10.219.40.215:3306: connect: connection timed out``` Is there a firewall or. anything on your side blocking this? \--- Luke Josh (luke.josh) @ Tue, 28 Mar 2023 21:31:23 UTC wrote: hi <@U027X9VFL12> :wave: a couple of notes: • you're using port 3306 - self service auroras use port 3307 - you can read this from `/config/foundation/DATASTORE_AURORACLUSTER_jig_PORT` :slightly_smiling_face: • it looks the user you're attempting to connect with (`pdw_ro_1`) is not the user delivered by temp auth - this is delivered under `/secrets/MYSQL_jig_USERNAME` (and will start with `v-` e.g., `v-1680038529657-b-team-t5da2cf60`) • note the password is also delivered under `/secrets/MYSQL_jig_PASSWORD` • all the above config and credentials are also delivered for the `slack` cluster, just replace `jig` with `slack` (the name in the delivered file is determined by what you set as the "name" of the infrastructure items in your service yaml) \--- Treavien Holley (treavien.holley) @ Tue, 28 Mar 2023 21:51:20 UTC wrote: <@U02H47A5YP8> In my PR I have this set up for the user and password in the config or are you referring to samson? \--- Eric Salituro (esalituro) @ Tue, 28 Mar 2023 21:52:06 UTC wrote: It needs to be set in samson, and referenced in the code as env variables \--- Luke Josh (luke.josh) @ Tue, 28 Mar 2023 21:54:16 UTC wrote: I think what you're doing should work (i.e., using the `secret` provider of zendesk_config_go rather than the env provider <https://github.com/zendesk/product_data_warehouse_go/pull/384/files#diff-2becd6600d4792421e713ae8c9eb70e058011b0ef86e87066b78b1a38563adefR128-R129> ) My comment is just based on the connection error you sent, `pdw_ro_1` can't be coming from that file… so I'm guessing it's still loading from an env var / some other mechanism somewhere else in the codebase :thinking_face: \--- Eric Salituro (esalituro) @ Tue, 28 Mar 2023 21:59:33 UTC wrote: It looks like `3306` is hard-coded: <https://github.com/zendesk/product_data_warehouse_go/blob/212e6d21b98d96d1703e3866689a2e63b873377b/internal/app/pdw/config.go#L132> \--- Treavien Holley (treavien.holley) @ Tue, 28 Mar 2023 22:00:53 UTC wrote: How will changing the port from `3306` -> `3307` affect our other tasks? \--- Eric Salituro (esalituro) @ Tue, 28 Mar 2023 22:01:48 UTC wrote: note that in the code, that it uses a JigDBConfig message \--- Eric Salituro (esalituro) @ Tue, 28 Mar 2023 22:02:17 UTC wrote: it should be exposed as a config variable \--- Eric Salituro (esalituro) @ Tue, 28 Mar 2023 22:02:22 UTC wrote: bad form \--- Eric Salituro (esalituro) @ Tue, 28 Mar 2023 22:03:04 UTC wrote: <@U02H47A5YP8>: whats the tag we should be using here (instead of env): ```type JigDBConfig struct { Host string `env:"JIG_DB_HOST" default:""` // Jira Integration Database string `env:"JIG_DB_DATABASE" default:""` Username string `env:"JIG_DB_USERNAME" default:""` Password string `secret:"JIG_DB_PASSWORD" default:""` }``` \--- Luke Josh (luke.josh) @ Tue, 28 Mar 2023 22:05:41 UTC wrote: for secrets, you can use `secret`, which will load a file with the same name from the `/secrets` directory for config stored in `/config/foundation` you can use the file provider, e.g: `AuroraClusterHost string `env:"AURORA_CLUSTER_HOST" file:"/config/foundation/DATASTORE_AURORACLUSTER_your_table_name_HOST"`` (example sourced from the readme of the <https://github.com/zendesk/zendesk_config_go|repo>) \--- Eric Salituro (esalituro) @ Tue, 28 Mar 2023 22:06:59 UTC wrote: <@U027X9VFL12>: the code needs to be updated <https://github.com/zendesk/product_data_warehouse_go/blob/212e6d21b98d96d1703e3866689a2e63b873377b/internal/app/pdw/config.go#L125> and <https://github.com/zendesk/product_data_warehouse_go/blob/212e6d21b98d96d1703e3866689a2e63b873377b/internal/app/pdw/config.go#L155> \--- Treavien Holley (treavien.holley) @ Tue, 28 Mar 2023 22:07:59 UTC wrote: Yes, I just should have to edit the host a bit \--- Treavien Holley (treavien.holley) @ Mon, 03 Apr 2023 13:45:31 UTC wrote: `Error opening DB connection v-1680528972707-product-68b36a00:***@tcp(:3307)/slack_integration?parseTime=true&tls=true&allowCleartextPasswords=true: dial tcp :3307: connect: connection refused` <@U02H47A5YP8> this is the error we are receiving now, all of the env variables are present. Any ideas? \--- Treavien Holley (treavien.holley) @ Mon, 03 Apr 2023 17:38:33 UTC wrote: `Error opening DB connection v-1680542533285-product-68b36a00:***@tcp(<http://slack-integration-slack-integration-pod13.cluster-ro-c9impiyapurt.us-west-2.rds.amazonaws.com:3307|slack-integration-slack-integration-pod13.cluster-ro-c9impiyapurt.us-west-2.rds.amazonaws.com:3307>)/slack_integration?parseTime=true&tls=true&allowCleartextPasswords=true: x509: certificate signed by unknown authority` Now it has updated to this \--- Eric Salituro (esalituro) @ Mon, 03 Apr 2023 17:40:31 UTC wrote: Is that true for jig too? \--- Treavien Holley (treavien.holley) @ Mon, 03 Apr 2023 17:41:44 UTC wrote: About to check \--- Eric Salituro (esalituro) @ Mon, 03 Apr 2023 17:42:18 UTC wrote: <https://zendeskdev.zendesk.com/hc/en-us/articles/360016896879-How-do-I-connect-to-my-Aurora-MySQL-Database-with-TLS-> \--- Eric Salituro (esalituro) @ Mon, 03 Apr 2023 17:43:02 UTC wrote: Looks like you just need to add a CA_CERT to the config \--- Treavien Holley (treavien.holley) @ Mon, 03 Apr 2023 18:43:53 UTC wrote: The CA_CERT didn't seem to work \--- Eric Salituro (esalituro) @ Mon, 03 Apr 2023 18:45:16 UTC wrote: you need to use the filepaths for both CA_CERT and DATABASE_NAME (like for the HOSTNAME and PORT) \--- Treavien Holley (treavien.holley) @ Mon, 03 Apr 2023 18:47:57 UTC wrote: I have \--- Eric Salituro (esalituro) @ Mon, 03 Apr 2023 18:52:47 UTC wrote: I was looking at the code, sorry \--- Eric Salituro (esalituro) @ Mon, 03 Apr 2023 18:55:57 UTC wrote: can you flip those around so they're in the right order? My OCD is complaining \--- Eric Salituro (esalituro) @ Mon, 03 Apr 2023 18:57:18 UTC wrote: I'm guessing you also need to perform this step: ```/*Register RDS Root CA Certificate*/ tlsConfig := "aurora-tls" rootCertPool := x509.NewCertPool() pem := []byte(conf.AuroraCACert) if ok := rootCertPool.AppendCertsFromPEM(pem); !ok { fmt.Println("Unable to add root cert to pool") os.Exit(1) } err = mysql.RegisterTLSConfig(tlsConfig, &tls.Config{RootCAs: rootCertPool}) if err != nil { fmt.Println("Unable to register TLS config") os.Exit(1) }``` \--- Eric Salituro (esalituro) @ Mon, 03 Apr 2023 19:03:42 UTC wrote: <@U02H47A5YP8>: any way we can get around this TLS stuff? We don't have it in our code presently. \--- Treavien Holley (treavien.holley) @ Mon, 03 Apr 2023 20:06:58 UTC wrote: I did add to both the jig and slack connection strings to set tls to true. john wad wondering if that was one of the things missing and what we were trying <@UJYDL41RA> \--- Eric Salituro (esalituro) @ Mon, 03 Apr 2023 20:11:23 UTC wrote: That's cool <@U027X9VFL12>, but I believe you'll still need to write code to register the TLS as well, which we don't presently do. \--- Treavien Holley (treavien.holley) @ Mon, 03 Apr 2023 20:11:51 UTC wrote: I'm trying that now \--- Luke Josh (luke.josh) @ Mon, 03 Apr 2023 22:46:43 UTC wrote: hi friends :wave: TLS has to be enforced on all connections (as SOC2 compliance requires encryption in transit). So there isn't a way around it, sorry :disappointed: \--- Treavien Holley (treavien.holley) @ Mon, 03 Apr 2023 22:46:47 UTC wrote: Hey <@U02H47A5YP8>, would you have any suggestions on how to get the CA Cert working in our codebase? \--- Luke Josh (luke.josh) @ Mon, 03 Apr 2023 22:46:56 UTC wrote: let me take a look now \--- Treavien Holley (treavien.holley) @ Mon, 03 Apr 2023 22:47:34 UTC wrote: Thanks \--- Luke Josh (luke.josh) @ Mon, 03 Apr 2023 23:18:31 UTC wrote: I think it fits into your `ConnString` methods pretty well add a method like this: ```func makeTLSConfig(tlsCert string) (string, error) { tlsConfig := "aurora-tls" rootCertPool := x509.NewCertPool() pem := []byte(tlsCert) if ok := rootCertPool.AppendCertsFromPEM(pem); !ok { return "", errors.New("Unable to add root cert to pool") } err := mysql.RegisterTLSConfig(tlsConfig, &tls.Config{RootCAs: rootCertPool}) if err != nil { return "", errors.New("Unable to register TLS config") } return tlsConfig, nil }``` then use it like this: ```func (c *JigDBConfig) ConnString() string { tlsConfig, err := makeTLSConfig(c.AuroraCACert) if err != nil { // TODO - bubble error up, or compute the tlsConfig before hitting this function, and pass it in } return fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?parseTime=true&tls=%s&allowCleartextPasswords=true", c.Username, c.Password, c.AuroraClusterHost, c.AuroraClusterPort, c.AuroraDatabaseName, tlsConfig) }``` and similar for slack: ```func (c *SlackDBConfig) ConnString() string { tlsConfig, err := makeTLSConfig(c.AuroraCACert) if err != nil { // TODO - bubble error up, or compute the tlsConfig before hitting this function, and pass it in } return fmt.Sprintf("%s:%s@tcp(%s:%d)/%s?parseTime=true&tls=%s&allowCleartextPasswords=true", c.Username, c.Password, c.AuroraClusterHost, c.AuroraClusterPort, c.AuroraDatabaseName, tlsConfig) }``` You'll just need to handle the possible error produced by loading the tls config. The function that calls these `ConnString` methods already returns an error, so I think it would be trivial to just modify the signature of ConnString to be `func() (string, error)` and then handle it in `Getdbh` like this: ```func (c *Config) GetDbh(ctx context.Context, source string, useDRDB bool, statsdClient statsd.ClientInterface) (DBHelper, error) { ... case source == "slack_integration": connectionString, err := c.SlackDB.ConnString() if err != nil { return nil, error } return c.NewDBHelperFunc(c.SlackDB.LoggableConnString(), connectionString, statsdClient) ``` hope that helps :pray: \--- Treavien Holley (treavien.holley) @ Tue, 04 Apr 2023 21:15:00 UTC wrote: Thank you for all your help so far <@U02H47A5YP8>! Our slack works now but the jig doesn't seem to have any runs and doesn't seem to have any of the changes. Any idea? \--- Eric Salituro (esalituro) @ Tue, 04 Apr 2023 21:20:40 UTC wrote: this is the error: ```Error opening DB connection root:***@tcp(<http://pdw-database.cluster-c9impiyapurt.us-west-2.rds.amazonaws.com:3306|pdw-database.cluster-c9impiyapurt.us-west-2.rds.amazonaws.com:3306>)/dw_prod_analytics?parseTime=true: dial tcp 10.211.37.232:3306: connect: connection timed out``` can we confirm the temp auth config is correct? \--- Luke Josh (luke.josh) @ Tue, 04 Apr 2023 21:22:57 UTC wrote: Nice one! Looks like that isn't temp auth config that's being used - the username should be similar to the one for jig (starting with "v-"), and the host should include the name of zpod- is that the old host by any chance? (I can dig deeper in about an hour when I log on) \--- Eric Salituro (esalituro) @ Tue, 04 Apr 2023 21:23:16 UTC wrote: yikes \--- Luke Josh (luke.josh) @ Tue, 04 Apr 2023 22:30:51 UTC wrote: That host (`<http://pdw-database.cluster-c9impiyapurt.us-west-2.rds.amazonaws.com|pdw-database.cluster-c9impiyapurt.us-west-2.rds.amazonaws.com>`) is set in samson as the `DW_DB_HOST` env var for production. Is this error definitely coming from attempting to connect to the jig cluster? \--- Eric Salituro (esalituro) @ Tue, 04 Apr 2023 22:34:01 UTC wrote: ah. :lightbulb: that's our state database. do we need to enable something so that the collector can contact this db? \--- Eric Salituro (esalituro) @ Tue, 04 Apr 2023 22:35:15 UTC wrote: it's working for pod13, so it needs to work on pod19 as well \--- Luke Josh (luke.josh) @ Tue, 04 Apr 2023 22:35:19 UTC wrote: ahhh, was this error in pod19? there might need to be a security group or similar updated on the cluster to allow pod19 to access it \--- Eric Salituro (esalituro) @ Tue, 04 Apr 2023 22:35:44 UTC wrote: si \--- Luke Josh (luke.josh) @ Tue, 04 Apr 2023 22:38:57 UTC wrote: <@U5RU4663Y> is this something you'd be able to help with? a quick summary of the above thread to save you :reading:: • the pdw application has been deployed to pod19 in order to consume the self service aurora cluster for the `jig` application • it has not previously been deployed in this partition • the application is now unable to connect to it's state db (<https://us-west-2.console.aws.amazon.com/rds/home?region=us-west-2#database:id=pdw-database;is-cluster=true|this one> in `us-west-2`) with the error `connect: connection timed out`(note, this cluster isn't self service) I'm guessing there is a security group rule or similar to only allow connections from pod13 where it has only been deployed to before now.. could this be updated? \--- Amit Agarwal (aagarwal) @ Thu, 06 Apr 2023 17:58:35 UTC wrote: Let's meet today to troubleshoot this issue. \--- Amit Agarwal (aagarwal) @ Thu, 06 Apr 2023 23:13:59 UTC wrote: Added following 3 ingress rule for pod19 K8s in SG pdw-db-security-group-SecurityGroup-2VAN3218OK6S (sg-07805770fd38e6906) \--- Eric Salituro (esalituro) @ Thu, 06 Apr 2023 23:53:01 UTC wrote: Now we're seeing this error: ```Error opening DB connection zd_analytics_1:***@tcp(<http://pod17-account-db.zdsys.com:3306|pod17-account-db.zdsys.com:3306>)/zendesk_prod?parseTime=true: dial tcp 10.218.165.209:3306: connect: connection timed out"``` POD17? \--- Amit Agarwal (aagarwal) @ Thu, 06 Apr 2023 23:54:22 UTC wrote: Why it is going to 17, can you make it 19 and check? \--- Eric Salituro (esalituro) @ Thu, 06 Apr 2023 23:54:47 UTC wrote: That's my question...I don't know how to make it 19 \--- Eric Salituro (esalituro) @ Thu, 06 Apr 2023 23:54:56 UTC wrote: it's on 19...so... \--- Eric Salituro (esalituro) @ Thu, 06 Apr 2023 23:55:07 UTC wrote: is that coming from temp auth? \--- Amit Agarwal (aagarwal) @ Thu, 06 Apr 2023 23:55:32 UTC wrote: May be some of your configuration \--- Eric Salituro (esalituro) @ Thu, 06 Apr 2023 23:55:35 UTC wrote: this is probably the JIG db, so is the address in DNS or whatever correct? \--- Amit Agarwal (aagarwal) @ Thu, 06 Apr 2023 23:56:14 UTC wrote: That's production account db slaves \--- Eric Salituro (esalituro) @ Thu, 06 Apr 2023 23:56:50 UTC wrote: we're supposed to get the HOST_NAME from temp auth \--- Amit Agarwal (aagarwal) @ Thu, 06 Apr 2023 23:58:08 UTC wrote: I am sorry unfortunately I don't know how your application configuration are set up. \--- Eric Salituro (esalituro) @ Thu, 06 Apr 2023 23:58:28 UTC wrote: ```type JigDBConfig struct { AuroraClusterHost string `env:"AURORA_CLUSTER_jig_HOST" file:"/config/foundation/DATASTORE_AURORACLUSTER_jig_READER_HOSTNAME" default:""` // Jira Integration AuroraClusterPort int `env:"AURORA_CLUSTER_jig_PORT" file:"/config/foundation/DATASTORE_AURORACLUSTER_jig_PORT" default:"3307"` AuroraCACert string `env:"MYSQL_AURORA_jig_CA_CERT" file:"/config/foundation/DATASTORE_AURORACLUSTER_jig_CA_CERT" default:""` AuroraDatabaseName string `env:"MYSQL_jig_DATABASE_NAME" file:"/config/foundation/DATASTORE_AURORACLUSTER_jig_DATABASE_NAME" default:""` Database string `env:"JIG_DB_DATABASE" default:""` Username string `secret:"MYSQL_jig_USERNAME" env:"MYSQL_jig_USERNAME" default:""` Password string `secret:"MYSQL_jig_PASSWORD" env:"MYSQL_jig_PASSWORD" default:""` }``` \--- Eric Salituro (esalituro) @ Fri, 07 Apr 2023 00:02:29 UTC wrote: ```return fmt.Sprintf("%s:***@tcp(%s:%d)/%s?parseTime=true&tls=%s&allowCleartextPasswords=true", c.Username, c.AuroraClusterHost, c.AuroraClusterPort, c.AuroraDatabaseName, tls)``` \--- Eric Salituro (esalituro) @ Fri, 07 Apr 2023 00:03:02 UTC wrote: I feel like we need to <@U02H47A5YP8> to check on the `DATASTORE_AURORACLUSTER_jig_READER_HOSTNAME`? \--- Luke Josh (luke.josh) @ Fri, 07 Apr 2023 00:52:09 UTC wrote: Temp auth won't be providing you any account db config (you'd need to be using a shardAccess resource in your service.yml for that) I presume it's some config that isn't being set in this partition as a guess. It's a public holiday here and I'm not at home, but I can check in a couple of hours \--- Luke Josh (luke.josh) @ Fri, 07 Apr 2023 02:13:23 UTC wrote: <@UJYDL41RA> <@U027X9VFL12> that connection information is not coming from temp auth - it seems your connections to the self service databases are fine now. I think the issue is in your connection to the accountdb (which we are not providing any config for). `zd_analytics` appears to be coming from your `MYSQL_USER` environment variable, but I can't be sure since it is loaded as a secret value. My guess is that the problem is coming from here - where you are randomly selecting db connection info for the accountdb from consul <https://github.com/zendesk/product_data_warehouse_go/blob/98b47ffe9135ab8b2dea808f32aa419bb2ae0a7c/internal/app/pdw/consul_to_database_config_adapter.go#L46-L51|https://github.com/zendesk/product_data_warehouse_go/blob/98b47ffe9135ab8b2dea808f[…]bb2ae0a7c/internal/app/pdw/consul_to_database_config_adapter.go> here is where you're actually making the consul call: <https://github.com/zendesk/product_data_warehouse_go/blob/98b47ffe9135ab8b2dea808f32aa419bb2ae0a7c/internal/app/pdw/consul_to_database_config_adapter.go#L46-L51|https://github.com/zendesk/product_data_warehouse_go/blob/98b47ffe9135ab8b2dea808f[…]bb2ae0a7c/internal/app/pdw/consul_to_database_config_adapter.go> I'm not very familiar with consul… perhaps it is returning reader endpoints for other partitions in this pod but for for others; I think you need to find a way to ensure that you're getting the connection details for the regional reader endpoint for the pod you're connecting to \--- Eric Salituro (esalituro) @ Fri, 07 Apr 2023 16:27:19 UTC wrote: that's super helpful, thanks! Sorry you had to look at this over the holiday... \--- Eric Salituro (esalituro) @ Fri, 07 Apr 2023 16:27:35 UTC wrote: We were fine waiting until Monday. :wink: \--- Eric Salituro (esalituro) @ Fri, 07 Apr 2023 16:29:01 UTC wrote: ~I wonder if there isn't a way to skip account_db in non-sharded role and we just need to set it up for pod19~ Looks like it JOINs to accounts so that's out. \--- Eric Salituro (esalituro) @ Fri, 07 Apr 2023 17:00:40 UTC wrote: <@U5RU4663Y>: I think the easier approach would let pod19 connect to the other consul account_dbs \--- Amit Agarwal (aagarwal) @ Fri, 07 Apr 2023 17:02:30 UTC wrote: I can not decide that, it will be Security Risk to allow across the pods. Better will be to find the config/entry for account db17 and replace with account db 19. CC: <@U1E22SF4N> \--- Eric Salituro (esalituro) @ Fri, 07 Apr 2023 17:04:59 UTC wrote: but we're already doing that on pod13 \--- Eric Salituro (esalituro) @ Fri, 07 Apr 2023 17:08:22 UTC wrote: when it gets pod19-account-db, it still can't connect to it: ```Error opening DB connection zd_analytics_1:***@tcp(<http://pod19-account-db.zdsys.com:3306|pod19-account-db.zdsys.com:3306>)/zendesk_prod?parseTime=true: dial tcp 10.222.145.211:3306: connect: connection timed out"``` \--- Amit Agarwal (aagarwal) @ Fri, 07 Apr 2023 17:20:23 UTC wrote: where did you made the change from <http://pod17-account-db.zdsys.com|pod17-account-db.zdsys.com> to <http://pod19-account-db.zdsys.com|pod19-account-db.zdsys.com>? \--- Eric Salituro (esalituro) @ Fri, 07 Apr 2023 17:21:01 UTC wrote: I didn't, it just randomly pokes at account-dbs until it runs out \--- Eric Salituro (esalituro) @ Fri, 07 Apr 2023 17:22:18 UTC wrote: \--- Amit Agarwal (aagarwal) @ Fri, 07 Apr 2023 17:24:35 UTC wrote: hmmm, so it means as per Luke it is making random selection for accountdb \--- Eric Salituro (esalituro) @ Fri, 07 Apr 2023 17:25:04 UTC wrote: and i'm fine with that as long as it can eventually connect to pod19 \--- Amit Agarwal (aagarwal) @ Fri, 07 Apr 2023 17:30:39 UTC wrote: will check and get back to you. \--- Amit Agarwal (aagarwal) @ Fri, 07 Apr 2023 17:58:39 UTC wrote: I do not have access to modify the SG in Production for account db. \--- Eric Salituro (esalituro) @ Fri, 07 Apr 2023 17:58:59 UTC wrote: do we know who does? \--- Amit Agarwal (aagarwal) @ Fri, 07 Apr 2023 17:59:45 UTC wrote: Let's check with <#C1Q5JJXCZ|ask-security> \--- Amit Agarwal (aagarwal) @ Fri, 07 Apr 2023 18:04:10 UTC wrote: <https://zendesk.slack.com/archives/C1Q5JJXCZ/p1680890640117499> \--- Treavien Holley (treavien.holley) @ Wed, 12 Apr 2023 00:34:22 UTC wrote: Hi <@U02H47A5YP8> is there a way we can escalate this issue above with security? \--- Luke Josh (luke.josh) @ Wed, 12 Apr 2023 00:52:07 UTC wrote: I'm not sure sorry, this isn't really my area of expertise… I'd suggest bumping the thread - it might have gotten missed over the easter long weekend. Another route you could go down is asking the deploy team (<#C0206JAJFPU|ask-deploy> based on consul's <https://cerebro.zende.sk/projects/consul|cerebro entry>) for advice on getting the right endpoint from consul - that seems easier to me than allowing a connection to the pod19 accountdb from a pod13 kpod If all else fails… you could consider migrating your access to the accountdb from the statically provisioned user you're currently using, to a self service user following <https://zendeskdev.zendesk.com/hc/en-us/articles/4467019809946-How-do-I-migrate-my-application-to-use-Self-Service-Shard-Access-|these steps>. If you do this, accountdb config will be delivered to your application kpod in the same way the self service config is delivered… so you wouldn't need consul to find the host at all \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 15:40:21 UTC wrote: let's stop using Consul for long-lived RDS endpoints. it needlessly puts Consul on the critical path, and the DNS records don't change anyway \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 15:41:18 UTC wrote: so if the DBAs can provide the DNS record for account DB replicas in pod19, <@UJYDL41RA> you can use that DNS record directly in your config instead of the consul DNS address \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 15:47:53 UTC wrote: might be worth a separate chat/thread too, this thread has several unrelated issues confusing things. even after re-reading the thread, I don't understand why PDW can't connect to account DB in the same partition. you shouldn't just be scanning across account DB endpoints in every partition until one succeeds, that's a surefire way to have something break later \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 15:48:42 UTC wrote: if it's strictly a SG issue, I can work with DBAs and Network can work together to fix that. very simple stuff \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 15:55:11 UTC wrote: just saw the x-post to <#C1Q5JJXCZ|ask-security>. frankly security doesn't weigh in on infra concern very frequently, they mostly set policy/standards. Foundation (DBAs and Network) needs to drive this second, we shouldn't need to change any rules if we do this correctly - there are already services running on k8s that have access to the account DB (like the account service). so if PDW is running on the pod19 k8s cluster, you should already have network access to the account DB replicas in pod19 \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 15:56:20 UTC wrote: <@U027X9VFL12> maybe you can weigh in since you raised the Q in <#C0206JAJFPU|ask-deploy> \--- Eric Salituro (esalituro) @ Wed, 12 Apr 2023 16:03:57 UTC wrote: <@U3PNWNQPR>: I don't know why, but I posted the error message. The scanning is probably for load-balancing ```Error opening DB connection zd_analytics_1:***@tcp(<http://pod19-account-db.zdsys.com:3306|pod19-account-db.zdsys.com:3306>)/zendesk_prod?parseTime=true: dial tcp 10.222.145.211:3306: connect: connection timed out"``` \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 16:33:31 UTC wrote: where is your PDW container running? which k8s cluster, and does PDW run on any particular node? \--- Eric Salituro (esalituro) @ Wed, 12 Apr 2023 16:42:33 UTC wrote: pod19 \--- Eric Salituro (esalituro) @ Wed, 12 Apr 2023 16:43:29 UTC wrote: we were running it without incident on pod13 \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 18:14:12 UTC wrote: something else in the mix then. the account DB instances have the `Data` SG attached to them, which allows any connection (any port + protocol) from any the `App` security group, which is used by the k8s nodes and the ENIs mounted for kpods to use. is PDW running through some proxy? if you're running a console, is it getting routed through DataSunrise? \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 18:19:23 UTC wrote: hmm when trying to test connectivity from one of the k8s nodes, I can't connect to port 3306. contradicts my previous point (at least from the node perspective, not necessarily the kpod perspective) \--- Treavien Holley (treavien.holley) @ Wed, 12 Apr 2023 18:20:47 UTC wrote: Hi <@U3PNWNQPR>, recently I have set up temp auth for two of our pdw tasks `slack` and `jig` this causes them to use the port `3307`. The slack version is working in pod13 but jig is in pod19 and that is where we are having our issues if that helps. \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 18:21:45 UTC wrote: I thought we were debugging access to the account DB. \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 18:21:59 UTC wrote: \--- Treavien Holley (treavien.holley) @ Wed, 12 Apr 2023 18:22:34 UTC wrote: We are but I was giving more clarity to how we came to this point \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 18:23:22 UTC wrote: ok, thanks for the context. we should be able to ignore anything related to slack and jig, for the purpose of figuring out your account DB problems \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 18:23:31 UTC wrote: can you link to where your k8s manifests are defined? something is up \--- Treavien Holley (treavien.holley) @ Wed, 12 Apr 2023 18:31:08 UTC wrote: This is our k8s files for PDW <https://github.com/zendesk/product_data_warehouse_go/tree/master/kubernetes> \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 18:35:23 UTC wrote: <!subteam^S9H7RK928|@dba-us> looking for a sanity check before I propose SG changes. how are other applications reaching the account DB in pod19? <@U5RU4663Y>'s earlier change added the kpod subnet CIDRs to the SG, which seems to have worked, but that would mean nothing else in the pod19 k8s cluster can reach <http://pod19-account-db.zdsys.com|pod19-account-db.zdsys.com>. seems unlikely, no? \--- Eric Salituro (esalituro) @ Wed, 12 Apr 2023 18:38:22 UTC wrote: they're not. all our services were running exclusively on pod13 until the security regime change and now we have to deploy a single service on pod19 to access JIG db. \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 18:38:51 UTC wrote: I'm asking about services other than PDW. let's give the DBAs a chance to respond \--- Muralidhar Bopparaju (mbopparaju) @ Wed, 12 Apr 2023 18:40:07 UTC wrote: pod19 account db does get used by several other services in pod19 - from pod19 k8s (like support for e.g). This can be seen from the number of connections to the account db in pod19. \--- Muralidhar Bopparaju (mbopparaju) @ Wed, 12 Apr 2023 18:42:07 UTC wrote: we did discuss this in our standup a few days ago -- and it was not clear as to why that connectivity issue did arise. \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 18:43:01 UTC wrote: <@UJYDL41RA> stupid question, but just to eliminate red herrings - where are you getting that error message from? is it from an interactive console or from DD logs? if it's from DD logs, can you post a link? want to ensure we're not getting misled by error messages from other clusters \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 18:49:40 UTC wrote: nm, I exec'ed directly into your container and confirmed that it was able to reach the account-db endpoint. so either that log message is a red herring, or something is different about how you're testing the connection, but your kpod can definitely reach the `<http://pod19-account-db.zdsys.com|pod19-account-db.zdsys.com>` RDS cluster: ```$ k exec -it pdw-nonsharded-go-pod19-55b7d7c964-bkm8x -- /bin/sh Defaulted container "collector" out of: collector, rsyslog-server, zendesk-auth-sidecar-container, zendesk-auth-init-container (init), secret-puller (init) $ which curl /usr/bin/curl $ curl -vv <telnet://pod19-account-db.zdsys.com:3306> * Rebuilt URL to: <telnet://pod19-account-db.zdsys.com:3306/> * Trying 10.219.37.52... * TCP_NODELAY set * Connected to <http://pod19-account-db.zdsys.com|pod19-account-db.zdsys.com> (10.219.37.52) port 3306 (#0) Warning: Binary output can mess up your terminal. Use "\--output -" to tell Warning: curl to output it to your terminal anyway, or consider "\--output Warning: <FILE>" to save to a file. * Failed writing body (0 != 29) * Closing connection 0``` \--- Treavien Holley (treavien.holley) @ Wed, 12 Apr 2023 19:02:28 UTC wrote: <@U3PNWNQPR>: <@UJYDL41RA> was getting the the logs from gcp logging I can see what query he was running but here is a snippet of his results. \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 19:05:16 UTC wrote: doesn't make sense - logs from services on our k8s clusters are sent to Datadog, not GCP/Stackdriver. also I don't see `kafkacat` anywhere in the repo you linked earlier, is that part of a separate service? \--- Eric Salituro (esalituro) @ Wed, 12 Apr 2023 20:42:28 UTC wrote: we have a sidecar that routes logs to stackdriver \--- Eric Salituro (esalituro) @ Wed, 12 Apr 2023 20:49:41 UTC wrote: Ok, <@U3PNWNQPR>: you are correct, I'm now seeing the task is timing out, and no connection error. \--- Eric Salituro (esalituro) @ Wed, 12 Apr 2023 20:50:11 UTC wrote: <@U027X9VFL12>: try increasing the timeout for the task to 1h \--- Eric Salituro (esalituro) @ Wed, 12 Apr 2023 22:52:36 UTC wrote: <@U3PNWNQPR>: I got another failure: ```Error opening DB connection zd_analytics_1:***@tcp(<http://pod19-account-db.zdsys.com:3306|pod19-account-db.zdsys.com:3306>)/zendesk_prod?parseTime=true: dial tcp 10.218.229.206:3306: connect: connection timed out``` Note the address is `10.218.229.206` not `10.219.37.52` We're tracking this service via Stackdriver: <https://console.cloud.google.com/logs/query;query=resource.type%3D%22k8s_container%22%0Aresource.labels.cluster_name%3D%22blue-k8s%22%0Aresource.labels.namespace_name%3D%22default%22%0Aresource.labels.container_name%3D%22kafkacat-logs-product-data-warehouse-go-log%22%0Alabels.%22k8s-pod%2Fapp%22%3D%22kafkacat-logs-product-data-warehouse-go-log%22%0AjsonPayload.group%3D%22collector-nonsharded-go-pod19%22%0A--severity%3DERROR%0A-jsonPayload.message%3D%22%2Fz%2Fping%20completed%22%0A-jsonPayload.message%3D%22Not%20waiting%20for%20JRuby%20collector%22%0A-jsonPayload.message%3D%22No%20tasks%20are%20ready%20to%20run,%20checking%20backfill%20list..%22%0A-jsonPayload.message%3D%22Loaded%201%20tasks%22%0A-jsonPayload.message%3D%22No%20backfills%20pending,%20resuming%20normal%20run%22%0A-jsonPayload.message%3D%22Loading%20task%20list%22%0A-jsonPayload.message%3D%22Looping%20in%20TaskList.Run%22;timeRange=PT1H;summaryFields=:true:32:end;cursorTimestamp=2023-04-12T22:37:37.546740472Z?project=edw-prod-153420|https://console.cloud.google.com/logs/query;query=resource.type%3D%22k8s_container%22%0Ar[…]p=2023-04-12T22:37:37.546740472Z?project=edw-prod-153420> \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 23:01:09 UTC wrote: There are multiple nodes in that cluster. Same security groups. Different ip shouldn't matter \--- Eric Salituro (esalituro) @ Wed, 12 Apr 2023 23:01:42 UTC wrote: I get that, but did you try telnetting to that address? \--- Eric Salituro (esalituro) @ Wed, 12 Apr 2023 23:02:11 UTC wrote: I don't know why we can connect to one but not the other \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 23:04:48 UTC wrote: You have a console for your service right? You can run the curl command I shared earlier to test different IPs \--- Eric Salituro (esalituro) @ Wed, 12 Apr 2023 23:05:18 UTC wrote: I do not. I have no ability to access anything in AWS via console \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 23:05:32 UTC wrote: Not AWS, the k8s console \--- Eric Salituro (esalituro) @ Wed, 12 Apr 2023 23:05:51 UTC wrote: I don't have access to any pods after the changes from a couple of months ago \--- Eric Salituro (esalituro) @ Wed, 12 Apr 2023 23:06:07 UTC wrote: I used to ssh to dbaXX and now that doesn't work \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 23:09:20 UTC wrote: Your team needs to be able to manage your service. Good time for your team to figure out RIC and get SSH and whatever other access you need to maintain your app. I can't be your ops team and run arbitrary commands for you \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 23:09:55 UTC wrote: I can share some materials tomorrow if you need help getting started \--- Eric Salituro (esalituro) @ Wed, 12 Apr 2023 23:09:58 UTC wrote: that's fine. we can just it down. \--- Eric Salituro (esalituro) @ Wed, 12 Apr 2023 23:16:51 UTC wrote: Thanks for you help. Sorry to have inconvenienced y'all. \--- Alex Glover (aglover) @ Wed, 12 Apr 2023 23:24:06 UTC wrote: No worries, I think we're getting close! \--- Eric Salituro (esalituro) @ Wed, 26 Apr 2023 01:52:08 UTC wrote: Finally, <@U5RU4663Y> <@U9X72N0E8> <@U02H47A5YP8> <@U027X9VFL12> \--- Treavien Holley (treavien.holley) @ Wed, 26 Apr 2023 01:52:46 UTC wrote: Glad it's all done \--- Luke Josh (luke.josh) @ Wed, 26 Apr 2023 07:03:22 UTC wrote: amazing!! so glad to see it :slightly_smiling_face: To tie everything in a neat bow - I've documented some meeting minutes for this morning <https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5760484691/2023-04-26+Restoring+JIG+metrics+to+PDW|here>. I believe all action items are accounted for… please let me know if I'm mistaken or if there is anything else we can help you with :handshake: \---

---

## Re: Ibises

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6195875752](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6195875752)  
**Last Updated:** 2024-05-07  

//slack-preserver url=https://zendesk.slack.com/archives/C0462LNFM5G/p1673322159494599 page=0

Show thread

#transform-data-platform \--- Wai Chee Yau (wyau) @ Tue, 10 Jan 2023 03:42:39 UTC wrote: <@U2MHK6CET> <@UCL31N50W> and <!subteam^S04HB5MMU4F|@pda-onboarding-tiger-team> caught up today on the launch metrics <https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5640716585/Launch+Metrics+datasets|datasets analysis>. Here's a summary of our discussion. Let me know if I've missed anything. *List of Features dimension table* • We can derived ~130 features that are available to certain plans using `subscription_features` table in data lake. • For features available to all plans, we would require the relevant team(s) to publish the feature PDA data through future state proposed pipeline documented <https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5643207050/Launch+Metrics+Future+State+Design|here>. This will make the dataset available in our data warehouse. • <!subteam^S04HB5MMU4F|@pda-onboarding-tiger-team> will automate a number of the tasks for onboarding PDA datasets. • We only require feature name for this, GUI/API paths etc on this <https://zendesk.atlassian.net/wiki/spaces/Prod/pages/510263410/Product+Ownership|page> can be descoped for MVP. • *Action items* ◦ Sayaka to summarize a small sets of important features that is good to have as candidate for the MVP and initial releases besides custom ticket status (CTS) *Plan to Features dimension table* This mapping information is coded into 2 systems. It's not available in db tables nor data lake/EDW. We can try to get the 3 teams (Quoll, Narwhals and Rakali teams from Core services and Billing) maintaining these systems to publish PDA data through <https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5643207050/Launch+Metrics+Future+State+Design|our pipeline> by trying to get onto their roadmaps. Another stop gap suggestion by Sayaka, we can use the information we have on : • what features an account has • what plan does the account has • We can linked up the information without needing this dimension table. This make the dimension table a nice to have for MVP *Action Items* • Neil to reach out to the Billing/Core services teams and see whether the new <https://docs.google.com/document/d/1n1sCOt_ct9pE595iZJXuXOp0z-EL7H-vNnMvtIlky_g/edit|Project Kennedy> can take into considerations our requirements as well. Project Kennedy looks at reducing the time it takes to take SKUs to market *Product Metrics* 1\. activations : for features that allow customers to activate/deactivate, we will provide a common <https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5643207050/Launch+Metrics+Future+State+Design|pipeline> for the activation/deactivation PDA events to be sent in by the feature teams. 2\. engagements: There's no set patterns for calculating engagements as it depends on features. E.g. macros come out of box with 4 macros, so we cant just use number of macros as the metric. a. We will deal with this one at a time to start off with until we can come up with a standard guidance. 3\. volume a. Median is preferred over averages as average can be skewed by outliers (extreme low or extreme high). b. Depending on features, median can be computationally expensive. E.g. Tickets will be expensive to calculate whereas Groups or Organizations (much smaller datasets) will be fine. c. We may use ranges if its too computationally heavy for the datasets *Financial metrics* • ARR metrics is being covered by EDA not Foundation engineering. • For Cloud cost, further discussion is needed between Sayaka and David Boothroy's team and this metric can be descoped for MVP \--- Sayaka Hill (shill) @ Tue, 10 Jan 2023 18:16:47 UTC wrote: thanks for the summary <@U0MACLTSP> I added the top 20 features and tagged you in a comment in the <https://docs.google.com/document/d/1xjutjpKH3ej2phIKflZb5dnuzx_dZ-hiGXtGm_R2aAk/edit?usp=sharing|CTS Launch Metrics BRD> \--- Wai Chee Yau (wyau) @ Tue, 10 Jan 2023 20:41:09 UTC wrote: thanks Sayaka for providing the information so quickly! \--- Wai Chee Yau (wyau) @ Tue, 10 Jan 2023 22:13:52 UTC wrote: Looks like from the list of 20 only 4 are tied to plan subscriptions. Others are available to all plans ```select * from data_lake_classic.subscription_features where name in ('business_hours', 'groups', 'light_agents', 'organizations','ticket_forms') order by updated_at desc limit 500``` \--- Wai Chee Yau (wyau) @ Tue, 10 Jan 2023 22:14:15 UTC wrote: Talk, Chat and Explore are modelled as "product" rather than "feature" \--- Wai Chee Yau (wyau) @ Tue, 10 Jan 2023 22:14:47 UTC wrote: Most of these features are also enabled by default ya. I dont think customers can turned off organizations, groups, ticket forms etc \--- Edward Savage (esavage) @ Wed, 11 Jan 2023 00:47:27 UTC wrote: It'll be interesting to ask the question, once we have a better idea of how much features cost, if it makes sense to offer those features by default. For various segments of customers. Random thought but kinda cool to think about what we could ask with even this data set. \---

---

## 2022-02-26: Data Platform Knowledge Building - Zendesk Data Catalog

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6179586790](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6179586790)  
**Last Updated:** 2024-04-23  

Post by Neil Cunningham

**TLDR** ; Here is what the data catalog is and does and what we are planning on doing with it. We need to learn about how the data catalog might impact your group and want to know about your use cases.

February 24, 2021  |  Foundation AnalyticsTo help our customers to better understand Fdn-Analytics' mission of empowering Zendesk to lead with data, we will continue releasing a series of posts to do just that. Today we would like to bring everyone up to speed on the Data Catalog project. What is the Zendesk Data Catalog? A data catalog is a centralized inventory of all the metadata information related to all the data assets at Zendesk. It enables users (engineers, analysts, governance/data stewards, applications) to discover, search and extract metadata information in an automated manner. Why do we need a data catalog? Think about a scenario where an engineer wants to understand a Mysql data set, its attributes, the business glossary, policies and lineage of where the data is collected from (S3, MySql, Kafka etc) and used in downstream systems (Glue/Athena, Big Query, etc) to get a holistic view of the data flow. This is being done manually by team conversations and documentation.Another scenario would be an application/pipeline failing today because of the upstream schema changes done yesterday which was not communicated. It could impact SLOs as well.With a Data Catalog, the user will be able to get answers to the questions like:

  * What is the latest snapshot of the schema of any new/existing dataset?

  * How can I interpret a message in a Kafka topic?

  * What are the tags, terms, confidentiality level associated?

  * Can I understand the lineage - the interactions between the upstream and downstream systems (eg: the data on S3 was transformed to a Mysql table and a Big Query table was derived out of it)?

  * Can I create a new business glossary?

  * Can I access metadata information using APIs?

  * Can I update the tags in bulk?


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6179586790)*

---

## 2021-01-28: Platform Schema & Metadata Working Group

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6148424339](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6148424339)  
**Last Updated:** 2024-04-04  

Post by Christopher Atkins

Hi again folks, just putting out one last plug for the **Platform Schema & Metadata Working Group** which we'll be kicking off in the next week or two. If helping about how we the structure and capability of our ZObjects sounds like something you're interested in, please reach out!A long-time Zendesker recently told me that describing the stated goal as a building **Data Catalog** may be clearer? Do _you_ have ideas on the _terminology_ we could use around data? If so, reach out!NB: If you don't have quite enough time to join the working group, but have some thoughts on the topic, I'm happy to organise a one-off catchup to help your input make it into the discussion and design. Just fill in the form, and mention it in the free text box at the end, or just DM myself, [@ggrossman](https://zendesk.slack.com/team/U08F4SFCH) or [@dzuckerman](https://zendesk.slack.com/team/UGZU43J5B).

Hi #product-dev-all. The Portfolio Architecture Team is about to kick off a new working group and are calling for volunteers who are interested in helping define the future of **Platform Schema & Metadata**.

  * [Working group charter](https://docs.google.com/document/d/1PdA8XCk2oU7tZdjtCIX5nKkFedif4NzS5GrWz7wS4iQ/edit?usp=sharing)

  * [Application form](https://forms.gle/v4M4zguWcnrVz3X78)




Brace for the buzzwords: The Platform Schema & Metadata working group will be continuing the Platform Data Architecture & One Zendesk Vision and defining a common schema and metadata representation of the data defined in our products, extended by customers or defined by our customers and partners.This schema and metadata representation will become a foundational part of other product efforts such as One Graph, Triggers/Automations, Zendesk Integrations Systems, Webhooks, Custom Objects/Events/Profiles, UI Platform, AnswerBot Flow Builder, more data sets in Explore and general platform-ey good stuff. Additionally, this will be used to maintain a Global Data Catalog used for EDA & internal analytics and by our Machine Learning teams.Note: this schema/metadata is intended to describe ZObjects as distinct from infrastructure concerns like AWS metadata.The main deliverables for the group are:

  * TechMenu ADR containing draft schema/metadata specification, including definitions of any new terminology.

  * :laptop: End-to-end POC & recorded demo using the draft specification to power some dynamic functionality.



*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6148424339)*

---

## 2020-06-27: Instacart Taskforce learnings - Shift PDW tasks from Production Shard DB

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6145213639](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6145213639)  
**Last Updated:** 2024-04-02  

Post by Nan Guo

To continue our learning series from Instacart task force, this post focuses on work Instacart TaskForce did that effectively address production Shard DB load and performance issue by offloading most expensive and slowest PDW tasks to DRDB. To keep it brief in Slack, this post serves as a high level summary and introduction to a [more detailed technical document ](https://docs.google.com/document/d/1Klsj0aKbkxsEkBRfmjApR4Vn434zjNjfOFqzACQQOs4/edit?usp=sharing)that we encourage everyone to read and gain deeper learnings.

Production Aurora MySQL Shard DBs are external customer facing databases to serve all our customers for both write and read across all our products. It is critical shared resources we need to keep high performant, stable and reliable all the time. Load spike and/or unexpected long running queries are the typical culprits of incidents impacting many products and customers. Be able offloading non customer-facing slow queries to other data stores can significantly help our reliability and capacity. We have seen clear evidence of DB load spike from some heavy PDW tasks while task force working on improving Instacart reliability. Since then we have been working with EDA teams to offload slowest PDW queries to DRDB (DB for disaster recovery, no customer facing queries running there).

In [our technical document](https://docs.google.com/document/d/1Klsj0aKbkxsEkBRfmjApR4Vn434zjNjfOFqzACQQOs4/edit?usp=sharing), we discussed:

  * Aurora MySQL DB is designed for OLTP

  * Historical context on how we correlate DB spike to Select Latency elevation

  * Prior efforts for improvements

  * How Instacart task force approaches the problem

    * Use data driven approach by building good dashboard to identify issues and tracking progress of improvements

    * Upsize small subset of DRDB clusters of selective Pods


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6145213639)*

---

## 2020-01-15: Engineering promotions

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6138757378](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6138757378)  
**Last Updated:** 2025-07-29  

Posts by Soren Abildgaard, Steve Loyd, Abhi Deshmukh, Jesper Hvirring Henriksen, Jason Smale, Todd Roman, Colum Twomey, 

## Directors

Hello Engineering,  
I'm happy to announce a promotion to Director of Engineering in this final 2019 cycle. Promotion to Director includes demonstrating accomplished levels of leadership in managing large scale teams, delivering on key initiatives and influencing our global engineering organization. We're excited to celebrate a milestone for Zendesk engineering with this promotion.

I hope you will all join me in congratulating the outstanding performance and looking forward to the impact they will make in their new role.

Søren Abildgaard  
SVP Engineering

**Rasmus Barfoed - Director, Engineering**

Rasmus has been a manager at Zendesk since 2014 and currently leads three of the Guide feature development teams and Guide Test Engineering. He leads his team with empathy and he is a leader who is respected by both his team and peers and knows how to navigate the growing global Engineering organization. Rasmus has impactfully contributed to our architecture, systems design and performance analysis, all the while leading and delivering with a large team. Rasmus' teams have made numerous significant contributions to our Guide product over the years - more notable ones include: Knowledge Bank, Gather SKU, Team Publishing, Flexible Hierarchies, User Segments Service, Article Verification and Scheduled Publishing. In addition to Guide, his teams have contributed significantly to Garden, helping improve this key aspect of our product development process. His dedication, execution delivery and management skills have been essential to our success.

## sre-dart, IM and Strategic Integrations

Please join me in congratulating the following individuals for their promotions. Each of them has demonstrated leadership and valuable technical contributions within the sre-dart, Incident Management, and Strategic Technology teams.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6138757378)*

---

## 2019-07-03:PDW MySql User Survey and Deprecation

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6135317346](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6135317346)  
**Last Updated:** 2024-03-26  

Post by Raj Khare

Attention all PDW Mysql users,

As part of upcoming improvements to the Product Data Pipeline:

  1. The PDW Mysql Instance will be deprecated (also known as hostname: [_pdw-database.cluster-c9impiyapurt.us-west-2.rds.amazonaws.com_](http://pdw-database.cluster-c9impiyapurt.us-west-2.rds.amazonaws.com/)).

  2. Product data will continue to be populated in the EDW as it is today.

  3. Product data will continue to be collected as defined in the github repo [tasks](https://github.com/zendesk/dw_prod_analytics/tree/master/config/dw_config/tasks).




These changes will allow for an increase in task volume, efficiency, and reduce the lag of `run_at`.

EDA will continue to support the [dw_prod_analytics repo](https://github.com/zendesk/dw_prod_analytics) and the current [process](https://docs.google.com/document/d/1Q-GzrJX2SeAwmXbrZrCQkL9jdshAxvODWLmrYdePtOw/edit) to create new metrics and tasks will remain the same.  
As tasks and metrics are defined, the new data will become available in the EDW (already part of current process).  
Any dashboards or system accounts should be connected to the EDW as well.

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6135317346)*

---

## Snowflake Access System: User Types

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6121883345](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6121883345)  
**Last Updated:** 2024-03-18  

Implementation of the snowflake access system within ZDM necessitated the addition of some new user types. This document will outline the different levels of access, how they are granted, and what privleges they provide.

# Access Admins

Access admins are generally aligned to the data governance / EDA teams. This is a global permission - a user is either an access admin, or they are not. They are able to:

  * create new dataset collections in ZDM

  * promote a user to an owner of any dataset collection

  * demote any existing dataset collection owner




Access Admins are set using environment variables: `ZSM_ACCESS_ADMIN_USERS` is a comma separated list of user emails, and `ZSM_ACCESS_ADMIN_TEAMS` is a comma separated list of scrum teams.

It is worth noting that a scrum team must exist in ZIG to use the teams environment variable - this generally will not map well to the EDA team, as they are not an engineering team.

# Data Owners

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6121883345)*

---

## Onboarding Customers to Snowflake Access System

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6051431250](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6051431250)  
**Last Updated:** 2024-02-12  

16falselistfalse

This document is designed to detail the onboarding procedures for customers into the Snowflake Access System. It will outline the steps that need to be taken by the Zendesk team to ensure their datasets in Snowflake are accessible and governed properly. 

## Important considerations for an onboarding customer

  * Before onboarding existing datasets, make sure you know which users already have access to them. That's because **they will loose access** to fields that are not classified as non sensitive and they will need to have a request properly approved by a steward through [ZDM](https://datastores.zende.sk/ui/snowflake/access) to gain access again.

  * Once onboarded, masking policies will be applied to the fields of the datasets and **there 's no going back**.

  * Make sure you know who the data stewards are for each dataset collection so that you can reach out to them to inform them about request approvals that might be coming their way.

  * If you need dataset collections to be created, reach out to the Data governance team to let them know. They can create those collection and assign the data stewards to them.




## Pre-requisites

  * Verify that your datasets are present within the [Snowflake account](https://app.snowflake.com/zendesk/amer_hipaa/#/data/databases/EMPORIUM_TEST).

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6051431250)*

---

## Snowflake Access System Phase 2: Data Owners

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6036258970](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6036258970)  
**Last Updated:** 2024-04-04  

# Context

On the 23rd of January, we met with security. Highlights from this meeting:

  * They are concerned that data stewards can promote other data stewards - they stated this is the job of the "data owner"

  * There is another class of user that is able to assign data owners to dataset collections (and by extension, create dataset collections). This is likely the EDA and data governance teams.

  * They would like us to implement something to track/restrict the number of users our system provides access to in snowflake (i.e., the number of users with "approved" permissions - it doesn't matter how many permissions that user has, restricted or hazardous - the limit is the number of users).

  * They are still happy for us to deploy to production with the current "stewards promoting stewards" approach




# Requirements

How can we support data owners in the current system? Let's break down the requirements:

  * A steward should behave the same way as it currently does, with the single exception that they cannot promote other stewards

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6036258970)*

---

## Legacy Tableau Migration to Snowflake

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5975084074](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5975084074)  
**Last Updated:** 2023-12-05  

# Important Information

## About this Project

**Points of Contact**| 

  * 
  
---|---  
**Epic Ticket**|  SNFLK-485cae89f0e-c846-3d65-88a5-bb277a2031b3System JIRA  
**Objective**| 

  * Testing the level of effort of migrating the dashboards from GBQ to ZDP

  
  
# In Brief

By creating identical dummy tables in Snowflake Sandbox migrating the dashboard in Tableau to ZDP to test the LOE of the upcoming ZDP Dashboards Migration.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5975084074)*

---

## Snowflake Access System: Worked Examples

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5890900657](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5890900657)  
**Last Updated:** 2023-10-09  

The examples on this page should help understanding why we suggest both group and individual column level permissions

# Permission Types

## Dataset Collection Permissions

**Dataset collection permissions are intended to be less fine grain than individual column permissions and represent regular use cases.**

The intention of dataset collection permissions is to represent a repeated set of data access requirements. By grouping like data together, especially datasets that depend on each other, we aim to have a collection represent the smallest reasonable amount of permission required to perform a task. They do not expose ALL data in the datasets, Hazardous/Highly Restricted data is still masked.

## Individual Column Permissions

**Individual column permissions are intended to be for extremely sensitive columns, rare cases that should be carefully considered.**

They are very fine grain permissions for data that can never be granted access via regular dataset collection permissions.

# Examples

## Collection Permissions: The EDA team regularly using data to do their job


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5890900657)*

---

## Snowflake Access System

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5863735454](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5863735454)  
**Last Updated:** 2024-11-06  

# Important Information

## About this Project

**Epic Owner**|   
---|---  
**Epics**|   
**Metrics**| 

  * How long does it take for a new user to get access to snowflake?
  * Number of users using this system to access Snowflake?

  
  
## Objectives

Snowflake will provide ALL people at Zendesk with ALL their data needs. From Snowflake Access System: Discovery we believe that we need a comprehensive and reliable access system with the following properties:

  * Automation


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5863735454)*

---

## Finance Analysis Access Requirements

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5829460005](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5829460005)  
**Last Updated:** 2023-07-06  

_Friday 7th July_

# Present

# Minutes

  * Current work in EDW

    * reads from Zuora/Salesforce and aggregate

    * current dataset is full access with no row or column level filtering

    * Examples of: marketing campaign would need to see effects

  * Zuora - in the past not typically categorized as sensitive

    * We avoid this by not bringing this sensitive data in the EDW queries

    * To add new fields to zuora requires manual changes in EDW, and the services account needs access


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5829460005)*

---

## b081a6c8-c41e-4ba3-9bcd-2b74cd5df828.csv

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/att5781357708](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/att5781357708)  
**Last Updated:** 2023-05-19  

---

## Archived: New Engineer Onboarding Guide

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5755245066](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5755245066)  
**Last Updated:** 2025-08-29  

17:info:atlassian-info#FFBDAD

This page is outdated for a few years, needs complete rewrite

## Introduction

This page list down steps for new engineer joining the Ibises team to get started.

This help center article [page](https://zendeskdev.zendesk.com/hc/en-us/categories/1260801549669-Engineering-Onboarding-Program) a list of all the onboarding related documentation.

### Setup Zendesk GitHub Access

<https://zendeskdev.zendesk.com/hc/en-us/articles/1260804700350-How-do-I-access-GitHub-at-Zendesk->

### Zendesk setup tool - zetup

Follow this [page](https://zendeskdev.zendesk.com/hc/en-us/articles/7035500485530-How-do-I-setup-my-laptop) to use internal Zendesk tool - zetup to install the following:

## Other software and access


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5755245066)*

---

## Re: Glossary

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5752720082](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5752720082)  
**Last Updated:** 2023-04-16  

Hi , I think the challenge with this is that it means different things to different parts of the company. To my understanding, and as far as Prod Dev are concerned, a product is a billable entity, plus the internal business areas that support those billable entities. We can use the list of 'products' in Cerebro as a guide: Answer Bot, Chat, Connect, Core Services, Dev Ecosystem, Dev Platform, EDA, Engineering Productivity, Explore, Foundation, Globalization, Growth & Monetization, Guide, Integrations, IT Engineering, Machine Learning, Marketing, Mobile, Professional Services, Reliability, Security, Sell, Solutions Consulting, Sunshine, SunCo, Support, Talk. 

I will try again to get an official 'blessed' consensus on this for you

---

## Should we integrate the new PDA ingestion to the legacy Hudi pipeline

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5743248335](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5743248335)  
**Last Updated:** 2023-07-24  

**Status**|  CompletedGreen  
---|---  
**Impact**|  MediumYellow  
**Driver**|   
**Approvers**|   
**Contributors**|  @ contributors  
**Informed**|   
**Due date**|  Type // to add a date  
**Resources**|  Type /link to add links to relevant research, pages, and related decisions  
  
##  Relevant data

Add any data or feedback the team should consider when making this decision.

##  Background

Currently the PDA onboarding automation tiger team has been building out a new pipeline to ingest PDA data from Kafka into the data lake. The output of this pipeline would be the raw L0 dataset in S3.

[Lucid link](https://lucid.app/lucidchart/052fd84e-a570-49fe-80c8-a6478716583f/edit?beaconFlowId=EADAEAC8B70C986D&invitationId=inv_538c639c-6e21-4d26-ab2c-282faf57a01e&page=0_0#)


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5743248335)*

---

## Store Data Lake L0 Raw Data in Zendesk Partition Based Buckets

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5741412546](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5741412546)  
**Last Updated:** 2023-07-27  

**Status**|  completedGreen  
---|---  
**Impact**|  LowGreen  
**Driver**|   
**Approvers**|   
**Contributors**|   
**Informed**|   
**Due date**|   
**Resources**| [Request For Comment (RFC) Document ](https://docs.google.com/document/d/1_VuiQElQYrEobMg1W48J4T7mhe5jLe11yYIW0aWVu9Y/edit)  
  
##  Relevant data

Add any data or feedback the team should consider when making this decision.

##  Background

Foundation Engineering and Enterprise Data Analytics (EDA) teams are building a new Zendesk Data Platform (ZDP). The new ZDP will replace our existing data warehouse on BigQuery with [_Snowflake_](https://www.snowflake.com/en/). See the ZDP [_RFC_](https://docs.google.com/document/d/1VMfScYI2M3jfXjDPthjj41qEJYCRO4zWj5C33dI4Iyo/edit#heading=h.vy2pygvndlrc) for more details on the high level proposal of the ZDP. 

As part of this project, we are evaluating the appropriate infrastructure partition strategy for the new data lake and data warehouse (Snowflake). We want to ensure that the selected partition strategy is optimal for the existing and new [_use cases_](https://docs.google.com/spreadsheets/d/1rTpi-pbiPDbIDdQQz5WSrUrZnNua2h--ckq5tWzCn6E/edit#gid=0) of the ZDP. This document discusses the trade offs of different partition options for the raw data from Zendesk systems landing in the data lake.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5741412546)*

---

## PDA Customer Survey Results

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5646353005](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5646353005)  
**Last Updated:** 2023-02-16  

17

## Background

Platform data architecture (PDA) is a standard created by architecture team within Zendesk product development organization to make it easy to produce, consume and share data across the different products and systems. The details on how to be compliant with PDA is documented [here](https://techmenu.zende.sk/standards/pda-standards/). 

To better understand the current state of PDA, we have conducted a customer survey on engineering teams that has published PDA / non PDA datasets in Jan 2023. See this [spreadsheet](https://docs.google.com/spreadsheets/d/16wIRVfrToeTBKE-dwcgk2JsQX78JvsJ2cfMpTneNpi8/edit#gid=1109464361) for the raw data of the survey response.

This page summarizes the results from the survey responses.

## Response Rate

The response rate is 88.89%

8 out of the 9 groups that owns PDA dataset responded to the survey.

The responses were mostly filled out either by the Technical Lead or Group Tech Lead of the groups.

  * AnswerBot - **responded**


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5646353005)*

---

## Shein research

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5524063682](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5524063682)  
**Last Updated:** 2022-09-05  

# Infos

  * Shein is the only account on prod US rscluster12

  * Is has exceptionally 4 dc2.8xlarge nodes instead of 2




# Use PG graviton instances

  * A benchmarking to compare RS 2 nodes vs PG R6g.16xlarge has been done

  * [https://zendesk.datadoghq.com/dashboard/7ig-pfh-hhy/explore-benchmarking-shard-level-performances-comparison?tpl_var_base_shard.name=rscluster12-clone-base&tpl_var_variant_shard.name=shard-test-1-production-us-east-1&from_ts=1659581427129&to_ts=1660103113183&live=false](https://zendesk.datadoghq.com/dashboard/7ig-pfh-hhy/explore-benchmarking-shard-level-performances-comparison?tpl_var_base_shard.name=rscluster12-clone-base&tpl_var_variant_shard.name=shard-test-1-production-us-east-1&from_ts=1659581427129&to_ts=1660103113183&live=false)

  * We can see a lot more errors on PG side, it sounds like the DB was not able to handle so many concurrent connections has there was no connections pooling or limitations

  * It sounds like PG was faster, but the results may be biased due to the failures



*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5524063682)*

---

## Platform Schema & Meta WG: Meeting Notes

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4619712960](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4619712960)  
**Last Updated:** 2021-09-29  

**Reminder: Record meetings**

## 2021-02-23 - APAC/AMER Kickoff

**Attendees**

  *     * Portfolio Architect, prev: Connect, Sunshine, APIs

  *     * Business Rules team, Symphony

    * Now working on transactional platform for triggers (Triggers V2)

    * Keen on POC

  *     * Interest in auto-generated UI

    * Keen on POC

  *     * Our Chief Product Architect … will be our chief cheerleader, enabling us where we need to be enabled


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4619712960)*

---

## Platform Schema & Meta WG: Requirements Gathering

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4615194805](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4615194805)  
**Last Updated:** 2021-08-09  

To gather requirements for the common metadata specification, we will conduct a series of Zoom interviews with various people in Engineering, Product & Design, and record the notes from the discussions below.

### Admin Center

Contact:

### Garden

Contact: 

### Schema Driven UI

Contact 

  * Catchup March 5th w/ Austin DZ, Catkins

  * Still lots of unknowns, what is everything we can interact with

  * POC informs schema driven UI


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/4615194805)*

---

## 2018 Q2 Planning - Dev and Operations Estimates

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/424182411](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/424182411)  
**Last Updated:** 2018-03-29  

### **T-Shirt Size Estimate**

**Small**  
1 person x 1 sprint  
**Medium**  
1 person x 2 sprint  
**Large**  
1 person x 3 sprint  
**X-Large**  
1 person x 5 sprint  
**XX-Large**  
1 person x 7 sprint

### Priority

| 

### Project Title

| Project Type| QA Ready Date| GA Date| Product Manager| 

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/424182411)*

---

## Glossary

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/286006622](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/286006622)  
**Last Updated:** 2024-07-12  

This glossary page is deprecated. Zendesk Engineering glossary terms, and Zendesk-wide terms, can be found on [Data Catalog](https://zendesk.alationcloud.com/app/doc-hub/1). Documentation about how to add a new term or propose changes to an existing term can be found on [Zendesk Engineering Docs](https://zendeskdev.zendesk.com/hc/en-us/sections/5167509167642-Engineering-glossary). Please note that you must be [on the VPN](https://zendeskit.zendesk.com/hc/en-us/articles/206156318-How-To-Connect-to-Global-Protect-VPN) to access Data Catalog.

## Zendesk terms glossary

This page is intended to contain the definitions of the many acronyms and abbreviations in use across the organization, not just Engineering terms. It should contain any abbreviations, technologies, and code names in use by Engineering. It is very much a work in progress and will be only as good as we can make it, so feel free to make additions and/or corrections as you see fit. The more accurate information we have in here the better it will be for everyone.

As the Engineering glossary has migrated to [Data Catalog](https://zendesk.alationcloud.com/app/doc-hub/1), this page is locked for editing. Please follow the information on [Zendesk Engineering Docs](https://zendeskdev.zendesk.com/hc/en-us/sections/5167509167642-Engineering-glossary) about the new procedures for adding, editing and linking to glossary terms. Got questions? Contact  or [#zendesk-engineering-docs](https://zendesk.slack.com/archives/CTGN59A4S) on Slack.

See also:

  * [Data Catalog Glossary](https://zendesk.acryl.io/glossary) (see [2022-12-07 announcement](https://zendesk.enterprise.slack.com/files/T024F4EL1/F04E84SNQ1Y?origin_team=T024F4EL1&origin_channel=CDPSAQ963))
  *   * [Customer-Facing Zendesk Terms Glossary](https://support.zendesk.com/hc/en-us/articles/203661746-Zendesk-glossary)
  * [Internal Zendesk Glossary](https://docs.google.com/document/d/113XunO3N7nCt2IOzAs0lJB-lyJYsfzBr7oeLlLmggz8/edit?usp=sharing) (non-Engineering, business-centric)



  


Term| Description  

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/286006622)*

---

## FinOps-G&M Sync Up Meeting Minutes

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/200966753](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/200966753)  
**Last Updated:** 2020-08-31  

|    
---|---  
**Attendees**| 

  * Blaec, Om, Craig, Melody, Michael Y., Javier, Juris, Paige, Tung

  
**Agenda**| 

  * Zuora Incident - Global Tax Option
  * Talk Usage - Spike in unpaid usage for single customer
  * Multi-Product Bundle / Unified Shell Account
  * Services 559 De-commissioning
  * Zuora incidents - 3 since last Friday - _New_
  * Zuora Field Appendix - _New_

  
  
| **Owner**| **Status**| **Notes**  
Zuora incident - Global Tax Option| Katie Strader| Greenopen| 

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/200966753)*

---

## Intro to Scala training waitlist

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/1681001276](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/1681001276)  
**Last Updated:** 2024-02-29  

Interested in learning about Scala / Functional Programming. Come along to the Intro to Scala training.

The next training in APAC will be held in October 2023. If you would like to attend, please join the #mel-scala-intro-oct-2023 slack channel.

The training material covers Scala basics like syntax and introduces common data structures that you would work with like List, Option and Try.  The training takes 2 full days.  Transitioning to Scala isn't just a different syntax, it's also an intro to functional programming principles that can take a bit of a mind shift. Presenters will introduce new concepts and there are lots of exercises for you to complete.

No prior Scala experience is expected. If you already have an introductory FP / Scala background, there is also the <https://zendesk.atlassian.net/wiki/spaces/ENG/pages/757828783/Applied+Scala+training+waitlist+Melbourne> .

We have run this training 4 or 5 times in the past in Melbourne, and once in SF.

**Name**| **Team**| **Location / Region**  
---|---|---  
| Views Core| CA  
| Views Core| CA  
| Views Enablement| CA  
| Views Enablement| Madison  
| Views Enablement| New York  
| Views Enablement| Madison  
| Views Enablement| Seattle  
Nhat Long Nguyen| Sell Billing| Cracow  

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/1681001276)*

---

## 2014-08-18 Program Management Tech Talk.pdf

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/att98238478](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/att98238478)  
**Last Updated:** 2014-08-25  

---

## Engineering Tech Talks archive

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/92898165](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/92898165)  
**Last Updated:** 2024-07-23  

Tech Talks were in-person. The effort was paused during COVID-19 and never resumed. They were primarily replaced by Weekly Engineering Meeting.  
  
# Upcoming Speakers and Topics

Interested in speaking? Choose a signup link below based on your office. (You can present when visiting another office, too!)

  
| **Schedule / Signup Links**| **Local sponsor**| **Slack pre-talk notification channel**  
---|---|---|---  
**Dublin**| [Schedule & signup](https://docs.google.com/spreadsheets/d/12dKU-OLOLf9PxpNWAcCu0RwF_FHYSXSEydTeWdW9DOQ/edit?usp=sharing)| | [#engineering-dub](https://zendesk.slack.com/messages/C1Y5QF0JZ)  
**Melbourne**| [Schedule & signup](https://docs.google.com/spreadsheets/d/1rqF-k0zqqFpmLYWqkGiUwBH81W-XVUPicWwz6XgXwCI/edit?usp=sharing)| | [#melbourne-engineering](https://zendesk.slack.com/messages/C0R1ACC5S)  
**San Francisco**| [Schedule & signup](https://docs.google.com/spreadsheets/d/1DHS605tQqERaGDhnSH0yqwyuvefw8pmW_RQvb_oElvU/edit?usp=sharing)| | [#engineering-sf](https://zendesk.slack.com/messages/C1D89TNBV)  
**Singapore**| [Schedule](https://docs.google.com/spreadsheets/d/14GWbtvSlKEljtV_5kQuBLCV1bhZwpJilEI8N217rMNA/edit?usp=sharing) & [signup](https://docs.google.com/forms/d/e/1FAIpQLSepKI-yuaK2YSKpy2OLyJq61O9V1aGtmYk8mCspRLKMcQzIcw/viewform)| | [#chat-engineering](https://zendesk.slack.com/messages/C1D627C8K)  
**Copenhagen**| [Schedule & signup](https://docs.google.com/spreadsheets/d/1o0shBEnygnwESkeTePcRt4k60GzwXgHpHi3kkK_SzX8/edit?usp=sharing)| | [#engineering-cph](https://zendesk.slack.com/messages/CG0N9TM18/)  
**Montr eal**| [Schedule & signup](https://docs.google.com/spreadsheets/d/1hEJ4nLvhlnitkG5PyLvfm-b8hm2-keAfASuycIiZX14/edit#gid=1200566767)| | [#sunco-eng](https://zendesk.slack.com/archives/CJM6HKQUA)  
**Madison**| [Schedule & signup](https://docs.google.com/spreadsheets/d/1Ck8cxpxTNqLPbIJWT1k45U-KOfww8SI7Cp-4ZwVU_0k/edit#gid=0)| | [#engineering-msn](https://zendesk.slack.com/messages/CE096N1PH/)  
  
# Preparation & Follow-up

  * [**Have a read of the tech-talk playbook**](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/362087938)**! It 's really important** and includes steps that **you, the speaker,** must follow.

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/92898165)*

---

## Sample Technical Interview Questions

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/92897598](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/92897598)  
**Last Updated:** 2022-03-29  

**UPDATE 3/29/22: These questions haven't been updated or evaluated in some time! A better resource is Zendesk's[CoderPad](https://app.coderpad.io/dashboard/pads)****account.**

Here are some sample interview questions that can be used when interviewing Engineering candidates. These are just questions that others at Zendesk have used in the past; you don't have to use questions from this list! Feel free to contribute your own favorite questions to this document.

# Questions

## BART Architecture

Contributor: 

**Motivation**

The purpose of this interview question is 3-fold

  1. Assess the candidate's ability to solve a problem. This reveals aptitude around: scoping, communication, critical thinking.
  2. Assess the candidate's ability to incorporate feedback.
  3. When applicable, explore the extent of a candidate's knowledge.




*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/92897598)*

---

## Aurora Customer Summary

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/915017447](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/915017447)  
**Last Updated:** 2020-02-27  

Engineering teams are already using Aurora in staging and production, so these have been a great source of information as to the types of configuration options that are important to them.

## What is important for engineering teams to configure

Overwhelmingly engineering teams have little interest in fine grained control over various Aurora settings. The identified configuration options that teams were interested in are:

  * Selecting the appropriate instance size

  * Character encoding so the application could correctly store emojis  
 _However, given that many of our customers will need to support the many languages that Rosetta supports, this could be configuration that we provide by default_

  * Number of read replicas

  * Enabling Performance Schema




Other than this, all team requests were more along the lines of additional features that Foundation would be building on top of Aurora.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/915017447)*

---

## Global Event Bus (GEB) run book

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/903260150](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/903260150)  
**Last Updated:** 2025-09-22  

The Global Event Bus (GEB) is also known by it's github project name kafka-bus. 

See Cerebro for links to dashboard, logs, github: <https://cerebro.zende.sk/projects/global-message-bus>

## Commands

There is no command line interface for the GEB.

## Feature toggles

The GEB account move participant can be toggled using the feature toggle [exodus_kafka_bus_participant_job_enabled](https://monitor.zende.sk/features/6873-exodus_kafka_bus_participant_job_enabled) ([staging](https://monitor.zendesk-staging.com/features/7196-exodus_kafka_bus_participant_job_enabled/edit)).

# Zendesk Partition Kafka Outage

If there is an outage to a Zendesk Kafka Cluster, that could affect routing of a foreign cluster (eg Chat) into ALL Zendesk partitions. As such it may be necessary to switch the GEB instance performing routing for the foreign cluster. This should be escalated to the Goanna team if it is required.

Note that transferring routing responsibilities is a trade off with a loss of ordering guarantees.

Consider the following example:


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/903260150)*

---

## Aurora Technical Discovery

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/896150233](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/896150233)  
**Last Updated:** 2020-05-12  

## Purpose

The purpose of this document is to provide enlightenment on the features we could offer to customers of an Aurora self service solution and use this to determine the scope of work and potential time required to build a solution. This document is only a list of possibilities. There is no guarantee on any of the features or recommendations in this document being made available in the final product. 

## Intended Audience

The intended audience of this document includes anyone that may be directly involved in the development and delivery of the Aurora Self Service solution. The contents of this document assume a degree of technical knowledge in software engineering, devops, AWS, and databases. 

## Scope

Whilst the scope of work to follow will be focused on an initial EAP, this document will cover potential features that would be deemed out of scope for EAP, LA and even possible an initial GA solution.

## The Questions

  * What does the most feature rich Aurora database look like?

  * What are the dimensions of cost for Aurora?

  * Are there available tools for customer and operator monitoring? Do we need to build any more?


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/896150233)*

---

## Bunyip

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/89227310](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/89227310)  
**Last Updated:** 2017-11-29  

See:  located in the .

---

## Aurora Compliance Discovery

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/888551073](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/888551073)  
**Last Updated:** 2020-02-28  

3

# Concerns

The scope of the aurora operator is still in discovery which limits the potential depth of detail for compliance in this document.

I believe we should also be complying with controls: c24, c25, c26, c.28 which relate to deploys, since software for self service is deployed and this is on top of the previous list of "datastore soc2 controls". There may be other controls that need to be included too since we are assessing operator code not just datastores.

Also: C.22 (version control software used)

I've added those in.

Security/Compliance review go together. Here are some relevant docs:

Zendesk Security Principles

Zendesk Security Standard

Aurora Security Discovery


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/888551073)*

---

## Aurora Security Discovery

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/888541142](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/888541142)  
**Last Updated:** 2021-07-22  

The purpose of this work is to ensure that we have adequately considered security in Aurora Operator design, speculate about threat model and propose mitigation that should be implemented in a future Aurora Self Service. We expect that threat modelling is going to answer most of questions of this discovery; we propose to use [STRIDE](https://docs.microsoft.com/en-us/previous-versions/commerce-server/ee823878\(v=cs.20\)?redirectedfrom=MSDN) and [OWASP](https://owasp.org/www-community/Application_Threat_Modeling) methodologies to undertaking threat modelling exercise. Terminology that we are going to use on this page is aligned with [OWASP terms](https://owasp.org/www-project-cheat-sheets/cheatsheets/Threat_Modeling_Cheat_Sheet). Obviously working on the document of this kind can be crucial because SQL injection is at the [top of Top 10 Application Security Risks.](https://owasp.org/www-project-top-ten/) Besides generic work to address AWS Aurora product shortcomings based on OWASP threat modelling we are going to spend most time to address how Aurora Operator is going hand off authentication material to users, how Temp Auth work is going to be integrated with Aurora and what default settings the operator should enforce.

# Architecture View

OWASP recommends to utilize [4+1 architecture view](https://en.wikipedia.org/wiki/4%2B1_architectural_view_model) to outline overall architecture during threat modelling exercise. However using 4+1 technique seems to be excessive and I couldn't find any viable examples except of outdated academic papers . We will try to follow the spirit of 4+1 as it is a comprehensive method to capture architecture view, however we are going to simplify and combine several views in one diagram. 

We are going to cover in the architecture the following:

  * Aurora Operator and handling authentication to the end user

  * Aurora Operator creates resources to harden Aurora Cluster: dedicated VPC, subnets, security groups. 

  * Cooperation between the operator and TempAuth init container. 




## Current Aurora Topology (TBC)

Below we tried to capture current topology so we can be more concrete about the potential use cases of the operator. Zendesk have recently introduce ProxySQL solution that allows connection multiplex and makes it easier to abstract Aurora replica movements from the application. 

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/888541142)*

---

## Channels - Architecture Document

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/85459442](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/85459442)  
**Last Updated:** 2021-08-03  

This page is defunct, please see <https://github.com/zendesk/zendesk_channels/wiki/Architecture>

  


# ~~Motivation~~

~~This document serves as a guidebook for understanding and explaining the Channels architecture in it's current and future forms.~~

~~**Table of Contents**~~

~~~~

# ~~Context~~

~~Channels relates specifically to the Facebook and Twitter integrations in Zendesk. The goal of the architecture is to provide a seamless experience for support agents in Zendesk to interact with customers in Facebook/Twitter. To accomplish this, the architecture interfaces with Facebook and Twitter's APIs to capture and synchronize  interactions like posts, comments, tweets, direct messages, etc.~~

~~1 4cacf209-4af8-4d4d-b39d-6506a91f24ca1Confluence:20838172261000c6c727f7-0319-459b-a780-af53f017caa0c6c727f7-0319-459b-a780-af53f017caa0|103589275|85459442|Z0GJgvTVbpsYjd/1pjc5PECWs25LW0U6/YPr37oCoio=leftrich16279819423071000~~

  

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/85459442)*

---

## Foundation - Storage - Glider

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/830146039](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/830146039)  
**Last Updated:** 2025-07-02  

## Welcome to Glider

The Data Mover People

* * *

# Mission

Glider builds and maintains services that move data between live data stores without data loss, leaks, or corruption. 

# Team

Location| Melbourne (MEL)  
---|---  
Engineering Manager|   
Product Manager|   
Tech Leads|   
Team Members|   
Cerebro| [teams/glider](https://cerebro.zende.sk/teams/glider)  
GitHub Team| [@zendesk/glider](https://github.com/orgs/zendesk/teams/glider)  

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/830146039)*

---

## Standard Objects

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/829821236](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/829821236)  
**Last Updated:** 2025-07-28  

This documentation is pending an update and migration to the TechMenu as a Standard in 2025-H2. If you want to read other (stale) definitions, see:

  1. https://zendesk.atlassian.net/wiki/spaces/ENG/pages/6248464471/What+exactly+are+ZObjects

  2. <https://docs.google.com/presentation/d/1yU9ApsiLsWyM5XuunITchQSATwlRrsK9mu1qm2T1G58/edit?slide=id.g7d7fef748e_0_220#slide=id.g7d7fef748e_0_220>

  3. <https://techmenu.zende.sk/adrs/platform-data-architecture-zendesk-objects/>




# What is a Standard Object?

Standard Objects are a set of **native types** defined and owned by Zendesk, the **collection of data** conforming to those types along with a set of **standard access patterns** to use this data within the Zendesk platform.

In practice, Standard Objects are:

  * A set of native Zendesk types, each represented by a well-known schema, which are easily discoverable to Zendesk engineers.

  * An API associated with each type to allow write operations to create or mutate or read instances of the type. This API allows us to surface a Standard Object in the Zendesk platform.

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/829821236)*

---

## Data storage @ Zendesk

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/788044361](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/788044361)  
**Last Updated:** 2022-12-23  

Sept 5, 2022 - Casey Waters

This page is no longer valid or maintained.

See:  
[Aurora MySQL](https://zendeskdev.zendesk.com/hc/en-us/sections/360004187979-Aurora)  
[DynamoDB](https://zendeskdev.zendesk.com/hc/en-us/sections/360003677240-Dynamo)  
[Redis](https://zendeskdev.zendesk.com/hc/en-us/sections/1260801146349-Redis)  
[S3](https://zendeskdev.zendesk.com/hc/en-us/sections/360003723299-S3)

Aug 25, 2021

Hello!  Thanks for visiting this page.  There may be some content below that is not current.  As the Foundation Storage team works on giving this page a refresh, send us a Slack on #ask-storage so we can help!

([originally posted on slack](https://zendesk.slack.com/archives/CDPSAQ963/p1576265945004600) Dec 13 2019)

## Preface

The scope of this document is for datastores that store Customer Data or Service Data, defined in accordance with our [Information Management Standards](https://docs.google.com/document/d/1xNSyCK2WsjKMKFIJwEvhk6Uu_0uBVWHS98uZEukVDmU/edit). It does not apply to internal tools like Cerebro, or Foundation-managed infrastructure services like Kubernetes or Foundation (FDN) Self-Service. 


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/788044361)*

---

## ObjectStore Operator (S3)

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/770478181](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/770478181)  
**Last Updated:** 2021-11-04  

# Description

As part of the [Self Service initiative](https://zendesk.atlassian.net/wiki/spaces/ops/pages/648609836/Self+Service+Program) at Zendesk, Foundation Storage is providing a Self Service Object Store datastore for engineering teams to use in their applications.

This will leverage our Kubernetes runtime provided by Foundation Compute, and make use of the [Operator Pattern](https://coreos.com/blog/introducing-operators.html) popularised by CoreOS for managing non-native Kubernetes resources within Kubernetes itself.

# Motivation

We want our engineering teams to move fast. However, we also want them to move safely. To this end, we require our engineering teams to create compliant data stores.

**Project work - Epic**| **Epic owner**  
---|---  
<https://zendesk.atlassian.net/browse/ESS-195>|   
<https://zendesk.atlassian.net/browse/ESS-466>|   
Validation Webhook|   
<https://zendesk.atlassian.net/browse/ESS-16>|   
[DataDog Dashboard](https://zendesk.datadoghq.com/dashboard/j8f-rxz-5vy/s3-operator-dashboard?from_ts=1635389719874&to_ts=1635994519874&live=true)|   
<https://zendesk.atlassian.net/browse/ESS-1188> |   
  
# Resources

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/770478181)*

---

## Ticket Platform Onboarding Plan

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/770150237](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/770150237)  
**Last Updated:** 2025-07-09  

Note: Individual users should create a personal copy of this template to track their progress.  
  
# Week 1 

587 587 incomplete Attend 2-day general onboarding 636 636 incomplete Read what your team is up to:  670 670 incomplete [Ticket Platform Operational Review 2021b](https://docs.google.com/presentation/d/1YMI7EQo8IsmBqazA5MJEvs2BSvpYJG6DeCbPB00MKRs)  671 671 incomplete [Productboard Roadmap](https://zendesk.productboard.com/feature-board/2156018-support-hierarchy/features/5885131/detail) 672 672 incomplete Jira [roadmap](https://zendesk.atlassian.net/jira/software/c/projects/TP/boards/2222/roadmap). 674 674 incomplete Watch our last Operational Excellence Review  678 678 incomplete Watch our last [Ticketing+ All Hands](https://drive.google.com/drive/folders/1jRXRc5MsPWjDIelBw_8xM5HmU6q5_ef8?usp=sharing) 637 637 incomplete Learn about the roles within Zendesk Engineering: Titles and Roles in Engineering 589 589 incomplete Learn the lingo: [Data Catalog](https://zendesk.acryl.io/glossaryNode/urn:li:glossaryNode:Business%20Terms/Contents?is_lineage_mode=false) 591 591 incomplete Get your laptop set up here: [Getting Started: Development](https://zendeskdev.zendesk.com/hc/en-us/sections/1260801720129).  679 679 incomplete Follow Email Engineering - Initial Laptop Setup, with differences noted in Ticket Platform Laptop Setup. 676 676 incomplete Get your Misc tool access provisioned: 677 677 incomplete [Miro](https://zendeskit.zendesk.com/hc/en-us/articles/1260800121209-How-to-Request-Access-to-Miro) 635 635 incomplete Get added to the appropriate groups: 646 646 incomplete [Z1 - Ticket Platform](https://support.zendesk.com/agent/filters/360139029894),  669 669 incomplete [Geekbot](https://app.geekbot.com/dashboard/standup/65049/view/insights) for write-in standups 647 647 incomplete [Github - Ticket Platform](https://github.com/orgs/zendesk/teams/ticket-platform), 648 648 incomplete [Github - Support Ticket Archiving](https://github.com/orgs/zendesk/teams/support-ticket-archiving) 649 649 incomplete Slack group @ticket-platform-team (email IT for this), 650 650 incomplete [Google Group - Ticket+Platform](https://groups.google.com/a/zendesk.com/forum/#!managemembers/ticket-platform/members/active) 651 651 incomplete Workday 652 652 incomplete ZIG 634 634 incomplete Join the Slack channels you'll need: ticket-platform-team, _ticketing-plus, ask-ticket-platform, ticket-platform-td, jw-teams, incident-annc, engineering, eng-announcements 641 641 incomplete Watch the last Town Hall which are posted to [#town-hall-global](https://zendesk.slack.com/archives/C1EK0S7T3) and on [Zentranet](https://zentranet.com/intranet/) 657 657 incomplete Update your WFH set up if needed: [IT WFH Requests](https://zendeskit.zendesk.com/hc/en-us/articles/360051476674-How-to-Request-IT-Accessories-Peripherals-Mouse-Keyboard-Monitor-and-Other-Accessories-) 659 659 incomplete Read week 1 of <https://degreed.com/pathway/mplqxwjd9d> 593 593 incomplete _Stretch:_ Get your tools provisioned COG Readiness Checklist (You won't be on-call immediately, but this is the list of what you need)

# Week 2

660 660 incomplete Read week 2 of <https://degreed.com/pathway/mplqxwjd9d> 663 663 incomplete Do week 2 of [New Hire Onboarding Checklist (Engineering)](https://docs.google.com/document/d/1EIDNP_HaLZrD9d26FnhLZYrslp7em8M5a1pG_zvAeFA/edit) 654 654 incomplete Watch Gabe's "Ticket Lifecycle, Archiving, Incremental API" talk on COG Training Session 655 655 incomplete Watch Craig's "Classic Architecture and Kubernetes" talk on COG Training Sessions 595 595 incomplete Consume the "Onboarding Musts" in Ticket Platform Learning Materials 611 611 incomplete Learn our values: [Product Development Operating Principles](https://zentranet.com/a/zendesk/intranet/departments/product-development/product-development-operating-principles) 596 596 incomplete Create yourself a production Zendesk instance (or several): Creating Zendesk Test / Sponsored / Personal Accounts 597 597 incomplete Find some new-hire work in [Jira](https://zendesk.atlassian.net/jira/software/c/projects/TP/summary). 680 0ae1764d-84c7-48d0-9d4d-029d84d54c4a incomplete Check out [Unleash](https://zendeskdev.zendesk.com/hc/en-us/sections/7794825005978-Unleash-internal-unified-search) \- Zendesk's internal search tool 638 638 incomplete Shadow one [Classic deploy](https://zendesk.enterprise.slack.com/archives/CBX3FKN93). 630 630 incomplete Be a part of grooming and plan your sprint. 645 645 incomplete Check out our last [TickySum (2024)](https://drive.google.com/drive/folders/1dYreGJ-QFEDoc7dTJ) to see where our thinking is at. 599 599 incomplete Read through ProdDev's last quarterly review Quarterly Planning 2024 667 667 incomplete Set up 1-1s with every team member to get to know everyone (the 1-1 doesn't necessarily have to be during this week).

# Week 3-4

661 661 incomplete Read weeks 3 & 4 of <https://degreed.com/pathway/mplqxwjd9d> 664 664 incomplete Do week 3 & 4 of [New Hire Onboarding Checklist (Engineering)](https://docs.google.com/document/d/1EIDNP_HaLZrD9d26FnhLZYrslp7em8M5a1pG_zvAeFA/edit) 600 600 incomplete Watch Anatoly's "Datadog Observability Workshop for On-call engineers" talk on COG Training Sessions 601 601 incomplete Watch Jacob's "Forms, Field, Conditions & Multibrand" talk on COG Training Sessions 658 658 incomplete Get [AWS SSH access](https://zendeskdev.zendesk.com/hc/en-us/articles/360015289139-How-do-I-use-AWS-SSH-to-connect-to-my-EC2-Instances-) (if not already set up) 623 623 incomplete Ensure you have access to the AWS Athena Data Lake: [Accessing the Athena Data Lake](https://zendeskdata.zendesk.com/hc/en-us/articles/360017624914-Accessing-the-Athena-Data-Lake-The-New-Hive-) 639 639 incomplete Get 1 Pull Request merged 666 666 incomplete Read our [last ops review](https://docs.google.com/presentation/d/1YMI7EQo8IsmBqazA5MJEvs2BSvpYJG6DeCbPB00MKRs/edit#slide=id.gd13184162d_0_3). 643 643 incomplete _Stretch:_ Find a buddy and be the main on deploying your PR  665 665 incomplete Bonus: Read [A journey to (and into) a Zendesk partition](https://docs.google.com/document/d/1H6woWEtgbZHjnm0CKwbfBN-cx02v00GXpRebdyX4qYE/edit)

# Week 5-6

662 662 incomplete Read weeks 5 & 6 of <https://degreed.com/pathway/mplqxwjd9d> 613 613 incomplete Discuss your career path with your manager: 625 625 incomplete Learn the Zen levels more deeply in the Individual Contributors Job Architecture and Engineering Managers Job Architecture 608 608 incomplete _Optional:_ Become a champion of something for the team (see Titles and Roles in Engineering) 622 622 incomplete Sign up for [interview training](https://degreed.com/courses/interviewing-and-candidate-assessment-at-zendesk?d=9617676&orgsso=zendesk), required of all employees who conduct interviews 644 644 incomplete Be the main on a Classic deploy.

# Week 20


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/770150237)*

---

## Engineering Review

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/769328458](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/769328458)  
**Last Updated:** 2025-10-13  

# What is Engineering Review & why do we need it? 

At Zendesk, we take pride in the skill and ability of our Engineering organization. However, that does not mean we don't benefit from reviewing important decisions. Engineering Review is a process that is meant to empower teams to have the maximum impact, ensure consistency with the Zendesk architectural direction, and avoid being surprised by unknown limitations and requirements late in the game.

note

[Here](https://drive.google.com/file/d/12FQ8HwyVW33VS1AWm-oFoKam6quiGcod/view?usp=sharing) is a ~20 min video introducing Engineering Review delivered in October 2021.

[Here](https://drive.google.com/file/d/12FQ8HwyVW33VS1AWm-oFoKam6quiGcod/view?usp=sharing) is a ~20 min video introducing Engineering Review delivered in October 2021.

# Goals of Engineering Review

## Encourage collaboration on technical proposals

As Zendesk engineers, part of our everyday work is to make technical proposals, get to agreement on those proposals, and implement the resulting decisions. We make decisions about technology choices, how we think about work (see our [Engineering](https://techmenu.zende.sk/standards/first-principles/) and [Service](https://techmenu.zende.sk/standards/service-principles/) Principles) technical designs, and standards adoption.

## Avoid costly pitfalls 

We are a global Engineering organization, building products and services in each local office that need to fit together into a global product portfolio. Our organization's size and geographical separation makes communication a challenge.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/769328458)*

---

## I am a Reliability Champion

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/766513199](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/766513199)  
**Last Updated:** 2022-10-26  

As part of the overall Reliability effort in Engineering, the **Reliability Champion** advocates good practices for logging, monitoring and alerting in the team, follows through with observability gaps resolution and post-incident remediation tasks.

By partnering with Product Management to help define measurement as part of the feature design process, the Reliability Champion contributes to evangelizing a data-driven mindset in Product and Engineering.

_Importantly, this role is not a point on the dual ladder, but a set of responsibilities any  **engineer  ** may take on. This role is not permanent for a given team: it may be rotated around members of the team depending on circumstance. Anyone on the team can be a Reliability Champion, possibly the Technical Lead in small teams. The Team Manager decide who are the Reliability Champions for the team._

### **As a Reliability Champion:**

#### I partner with the Product Manager

  * I help define feature usage indicators during the feature exploration phase
  * I identify monitoring metrics for new services with PMs
  * I participate in SLI/SLO/Error Budget definitions with PMs and Customers



#### I partner with the Engineers

  * I identify reliability gaps (SPOF, operational constraints, service coupling) in systems
  * I educate peers on reliability practices and observability tooling

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/766513199)*

---

## Clickhouse Operator Plan

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7653425348](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7653425348)  
**Last Updated:** 2025-11-26  

# Introduction

The Wollemi team will design and build a Clickhouse operator and make it accessible through Self Service. 

# What is important for engineering teams to configure

Engineering teams should be able to quickly provision a Clickhouse cluster with just a few lines of code. They want to do the Self Service way and specify a few lines in their project's service.yaml. The result is a fully provisioned Clickhouse cluster that teams connect to.

In order to provision a cluster and make it accessible to a team, we need to:

  * Ensure a cluster is provisioned in the same namespace as each given project

  * Ensure that Clickhouse settings can be specified via service.yaml

    * It is possible to provision new clusters and update existing clusters

  * Ensure the config delivery (the same way we do for Snowflake Access Operator)

  * Ensure Clickhouse externals 


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7653425348)*

---

## Foundation Data - Analytics

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7648149781](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7648149781)  
**Last Updated:** 2025-11-25  

# **Welcome to Prism   **

**Our Mission: TBA**

**Team members**

\- Data Engineering Manager

\- Senior Data Engineer

\- Data Engineer

\- Data Engineer (C)

\- Data Engineer (C)

\- (Bluecloud Contractor)

\- (Bluecloud Contractor)


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7648149781)*

---

## Streamlit in ZDP: Write access

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7581762159](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7581762159)  
**Last Updated:** 2025-11-13  

This document will explore the options we have to allow streamlit apps to write data. This is in response to user feedback that applications would like to do this, specifically the "value calculator" use case.

It should be noted, the write access required is **not** to existing production datasets, but rather to specific tables that exist specifically for a given streamlit app to store inputs / results / outputs, etc in. Streamlit apps would NOT be given write access (for example) to datasets in FORMATTED, CLEANSED, etc.

### Context / facts / scene setting

  * To write into a table, the role that creates / owns the streamlit app must have the `INSERT` privilege (and any others required for relevant table management - e.g., `ALTER`, `CREATE`, `DROP`, etc), or the `OWNERSHIP` privilege of the schema & tables

  * Humans in ZDP do not have these permissions to date

  * Any masking policies applied to any table that is read by a streamlit app will be respected; the user who is **using** the app will have these permissions calculated against their roles.




### A note on schema structure

In the previous document, I suggested that all streamlit apps live inside a single database (`STREAMLIT_APPS` or similar), which are then split into schemas by domain as appropriate (e.g., `STREAMLIT_APPS.FINANCE`, `STREAMLIT_APPS.SALES`, or whatever makes sense). Given there is a requirement for apps to have supporting tables that will be written into, I now believe it makes more sense to maintain a **schema per streamlit app**(e.g., the schema `STREAMLIT_APPS.VALUE_CALCULATOR` would contain the streamlit app itself, as well as any table(s) that the app would write into).

### A note on the access system

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7581762159)*

---

## Frontend Usage Instrumentation POC Handover (22nd Oct 2025)

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7573472262](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7573472262)  
**Last Updated:** 2025-11-11  

## Session with Shajith, Baldvin and Bhavvya

**Next steps**

  * Rob to update the high level requirements document to include ad hoc analysis capabilities for product teams.

  * Rob to work with Sayaka to create a mock-up for the standard product adoption report/dashboard.

  * Rob to work with Megan to discuss PLG team ownership of the front-end layer.

  * Shajith and POC team to continue working with the three feature teams  to implement tracking code.

  * Shajith to add URL/page navigation tracking to Lotus and support front-end.

  * ZDP GTLs and EMs to complete solution design for the initiative and share feedback with POC team.

  * Shajith to continue following up with PLG team (engineering side)  regarding ownership transition.

  * Rob to check the working channel thread regarding PLG's proposal document.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7573472262)*

---

## Fullstack Onboarding

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7569801559](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7569801559)  
**Last Updated:** 2025-11-26  

# Glossary

  * [**Classic**](https://github.com/zendesk/scooter) \- RoR monolith (backend mostly)

  * [**Lotus**](https://github.com/zendesk/zendesk_console) \- Main frontend monolith, responsible mostly for the agent side UI (EmberJS + React)

  * [**Admin Center Framework (ACF)**](https://zendeskdev.zendesk.com/hc/en-us/articles/5793771892122-What-is-Admin-Center) \- a framework for the ongoing _Reactification_ of admin pages UI. Each page has it's own repo based on the framework. [Example acf owned by our team](https://github.com/zendesk/admin_center_framework_ticket_forms)

  * [**Scooter**](https://github.com/zendesk/scooter) \- tool for setting up development environment (runs a subset of Zendesk's repositories remotely only for you)

  * **ZDI** \- A precursor to Scooter, you will find mention of this tool in old docs. In all cases, you should _not_ follow ZDI setup instructions as it has reached __`end-of-support` as of Q4 2025.

  * [**Arturo**](https://zendeskdev.zendesk.com/hc/en-us/articles/6135611517466-Arturos) \- synonym for feature flag at Zendesk

  * [**Monitor**](https://zendeskdev.zendesk.com/hc/en-us/articles/1260804977710-What-is-Zendesk-Monitor-for-Engineering-An-Overview#h_01GXPYVHS4W2NE041R8WNMB84G) \- tool for managing Arturos, Accounts and other "super admin" stuff.




# Minimal setup

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7569801559)*

---

## 015 - Storing Platform Feature State Tables in Aurora

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7569015127](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7569015127)  
**Last Updated:** 2025-11-11  

**Status**|  IN PROGRESSYellow  
---|---  
**Impact**|  MediumYellow  
**Driver**|   
**Approvers**|   
**Contributors**|  @ contributors  
**Informed**|   
**Due date**|  Type // to add a date  
**Outcome**|  Ticket Platform will build Platform Field Feature State tables in Aurora instead of on Platform Objects.  
  
##  Background

After deciding on the creation of a state table, we considered options for where to store the data. We took a look at Aurora and DynamoDB, and during a discussion with Vinyl, a team member raised the idea of building the table on Platform Objects. 

Each template would be mapped to a Platform Object, with an instance for each account's version of that platform feature.

During discussion with Vinyl, we considered building a state table on Platform Objects. Building on platform objects would save us from waiting on DBAs for migration and would align with the engineering shift to use PLOBs for new models in Classic. 

However, there were several issues that came up in discussion that dissuaded us from building on PLOBs. 


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7569015127)*

---

## Spike - Adding a Rich Text Editor in Lotus for AI Agent Simple Setup

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7556235665](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7556235665)  
**Last Updated:** 2025-10-28  

As outlined in [this Jira ticket](https://zendesk.atlassian.net/browse/TPE-5749), and [this Slack thread](https://zendesk.slack.com/archives/C095YDDH475/p1760945685782979?thread_ts=1760719659.135729&cid=C095YDDH475), Ponderosa wanted to investigate the level of effort required to add a [Rich Text Editor](https://garden.zendesk.com/patterns/rich-text-editor) to the "Expand your AI agent's knowledge" page of AI agent simple setup. This is mainly to avoid unsightly raw markdown, namely bold headings and links to external page citations that come from the OpenAI web search result.

Current state with markdown

Future state with Rich Text Editor

### Background

The supported rich text editor package used at Zendesk and in Lotus is [CKEditor 5](https://ckeditor.com/ckeditor-5/), an open source JavaScript package. When working with text data in CKEditor, the recommended format is HTML. Fortunately, the Help Center articles API expects HTML as its expected format when creating and updating articles, so we would not need to perform any additional data transformation steps between rich text editing and saving the data in the Help Center (Help Center article persistence is required for AI agents to have access to the knowledge generated by OpenAI web search). We would only need to perform a one-time transformation of markdown to HTML when we first get the OpenAI web search results back - this could be done using the [showdown](https://www.npmjs.com/package/showdown) package, something we are already doing to support markdown-to-HTML transformation in Lotus as outlined [here](https://github.com/zendesk/zendesk_console/blob/11f1e34d158b8c8a1b535ef72df7bf364f1c9b3e/lotus_react/src/Editor/Shell/helpers/textConverters.ts#L20).

CKEditor 5 comes with a few theming options - the one that we use in Zendesk applications is the [Lark theme](https://ckeditor.com/docs/ckeditor5/latest/api/theme-lark.html). These themes are established using CSS rules which makes it more challenging to apply theme customizations, especially using Garden and styled-components. Garden achieves its theme customizations through [CSS overrides as outlined in its CKEditor package](https://github.com/zendeskgarden/ckeditor/tree/main/src/theme). Lotus currently **does not** use the Garden CKEditor theme and instead injects its own style with the [useCKEditorStyles](https://github.com/zendesk/zendesk_console/blob/main/lotus_react/src/Editor/Core/hooks/useCKEditorStyles.ts) hook. However, these styles **do not** currently align with those prescribed in Garden (though they are close). If we wanted to match the Garden CKEditor theme, we would almost certainly need to do it through CSS overrides in styled-components where we target specific CKEditor class names. For example:

typescriptwide760

We also got feedback from design ( and team) that having a persistent toolbar (with bold, italic, link options, etc.) was deemed too distracting and cumbersome for a simple AI agent knowledge flow. We want to keep the knowledge input as minimalist as we can during accelerated setup. This could possibly be circumvented by using the [Balloon editor](https://ckeditor.com/docs/ckeditor5/latest/examples/builds/balloon-editor.html), where the toolbar only appears inline when the user requests it by highlighting content. However, even that might be too complex and unneeded for this setup experience.

Another thing to consider is that the OpenAI web search add knowledge page has a read-only mode (where the user has to click the pencil icon in order to edit). This means we would also need to format the read-only text to align exactly with what styles the user can see and implement in CKEditor. This adds complexity and we would need to ensure these styles sync up with every new option we give users access to in the rich text editing toolbar.

One last thing to note is that all implementations of CKEditor in Lotus seem to use the [DecoupledEditor](https://ckeditor.com/docs/ckeditor5/latest/api/editor-decoupled.html) with all elements being totally custom, home-grown React components. This makes it more difficult to follow patterns for more basic implementations (like what we would require here), because there aren't any.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7556235665)*

---

## [WIP] Frontend Product Usage Data Instrumentation Discovery

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7555056803](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7555056803)  
**Last Updated:** 2025-11-13  

none

## Background

**Problem**

Frontend usage data is fragmented (Segment, Pendo, homegrown - frontend event ingestor), with inconsistent ingestion standard, and some of the methods not having complete data due to opt out, ad blockers--making adoption, funnel, and performance analytics unreliable.

A tiger team was formed - [#product-analytics-working-group](https://zendesk.enterprise.slack.com/archives/C0826MKHFNG) to worked on this problem to come up with a proof of concept in 2025. In 2026, Zendesk Data Platform (ZDP) team will own both the ingestion and transformation components of the new product usage instrumentation pipeline. 

Ownership of the shared JS SDK remains TBD. For current status, decisions, and POC details, see : <https://zendesk.atlassian.net/wiki/spaces/PRODDEV/pages/7525859909/Product+Instrumentation+-+Rebooted?atlOrigin=eyJpIjoiOGJjMzk0NDYzYjI3NDdjN2JiYThlNmI1MWFlNTI1NTAiLCJwIjoiY29uZmx1ZW5jZS1jaGF0cy1pbnQifQ>

## Objectives

Provide platform tooling to enable frontend teams to easily instrument product usage information and deliver insights via ZDP

## Scope

**In scope**


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7555056803)*

---

## Gmail Connector - Operability checklist

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7528186818](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7528186818)  
**Last Updated:** 2025-10-13  

# Operability requirements for Services/Features

  * version: v2.0.1

  * last reviewed date: 2025-10-09

  * owner: Email Integrations (Axolotl)




## Service/Feature Documentation

382 382 complete Service/Feature must complete its Cerebro Page. [**Before EAP**] _1_ 383 383 complete Service/Feature must be listed in their Team's Cerebro page, under Stakeholder. [**Before EAP**] _2_ 403 7fbfe7bf-b6bb-4a4c-9a1b-3d6aba962f9f complete Service must complete the service tiering criticality questions [**Before GA**] _3_ 384 384 complete A Service/Feature must have sufficient documentation. [[DOC]](https://github.com/zendesk/zendesk_mail_fetcher/blob/main/README.md) [**Before GA**] _3_

## Service/Feature Capacity

385 385 incomplete Capacity requirements for a service/feature are periodically reviewed by owned teams[[JIRA](https://zendesk.atlassian.net/browse/AXOL-1122)] [**Atleast quarterly**] _4_ 386 386 complete Capacity change process must be backed up by runbooks or be automated. [**Before GA**] _5_

## Testing baseline for Services/Features

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7528186818)*

---

## Attribute for Zendesk-1.pdf

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/att7518650566](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/att7518650566)  
**Last Updated:** 2025-10-02  

---

## [ADR] Gmail Sending - ESG

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7516062874](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7516062874)  
**Last Updated:** 2025-10-28  

**ADR Owner**|     
---|---  
**Status**|  ApprovedGreen  
**Scope**|  Group  
**Components**| [classic](https://github.com/zendesk/zendesk) [gmail-connector](https://github.com/zendesk/gmail-connector)  
**Reviewers**|  Please give your  (approved) or  (commented)  
  
# Reviewers

Please follow the guidelines in _Engineering Review_ for review process and approval. Once a decision is made on whether to move forward on the project, it should be updated in [_the Email Group Decision Record_](https://docs.google.com/document/d/127V2UP060axxcCba9E47jVxvYr7Q6OGovQd4evoVmXY/edit).   
**Reviewers:** Please review by Oct 17, 2025

**Stakeholders:**[Email Integrations (Axolotl)](https://zendesk.atlassian.net/people/team/2649553b-9d1a-47b6-a54f-35c9b9f20784) ( )

**Reviewer**| **Role**| **Responsibility**| **Status**| **Date**  
---|---|---|---|---  
  | Engineering Manager| Consulted (review required)| |    
  | Product Manager| Consulted (review required)|  Approved|     
  | GTL| Approval required| |    
  | Tech Lead| Approval required|  Approved|    

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7516062874)*

---

## Granular Permissions Team Charter

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7464878919](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7464878919)  
**Last Updated:** 2025-09-10  

## Our Mission

:rocket:1f680🚀#DEEBFF

To ensure consistency, security, and correctness of permission enforcement across the product.

We focus on the deep, technical implementation and enforcement of very detailed, fine-tuned permission logic within the system and on custom roles across all plans.

### Core Objectives

  * Centralizing access check across all services.

  * Managing low-level permission rules that define exactly what individual users or agents can do within various contexts.

  * Controlling access at a precise level such as individual actions, data fields, or specific system functions.

  * Building and maintaining the backend permission engines, policies, and frameworks that enable flexible, nuanced authorization.

  * Ensuring consistency, security, and correctness of permission enforcement across the product.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7464878919)*

---

## Bootstrap metadata and lineage tables

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7458816746](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7458816746)  
**Last Updated:** 2025-09-10  

## Overview  
  
To successfully onboard DBT customers onto the new lineage catalog, we must ensure that all existing datasets and columns are present in the new metadata and lineage tables. This is critical for validation: when a DBT repo submits new lineage information, its upstream datasets and columns must already exist in the catalog, or validation will fail.

[TL;DR -> decision](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7458816746/Bootstrap+metadata+and+lineage+tables#Post-Discussion-Decisions%3A-Catalog-Bootstrapping-%26-Metadata-Automation)

### What have we decide to do that may affect how do we bootstrap the database?

  * DBT repositories already generate manifest and catalog JSON files as part of their build process and upload these files to S3 (specifically, `s3://data-catalog-db2-alation-s3-bucket-production/dbt/`).

  * In order for the existing and new DBT repos to generate the draft `dataset-metadata.yml` before they can manually fill the gap and submit the final metadata. We will create toolings for DBT with two planned epics (FDB-5597cae89f0e-c846-3d65-88a5-bb277a2031b3System Jira and FDB-5598cae89f0e-c846-3d65-88a5-bb277a2031b3System Jira) that read these JSON files, parses them for dataset and column definitions, including upstream lineage information, then convert these information into `dataset-metadata.yml`




## Bootstrapping Approaches

We have three main strategies for ingesting the initial state of datasets, columns, and lineage:

### Option 1. Bootstrap from DBT-Generated JSONs

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7458816746)*

---

## Classic User API - Reliability

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/743903554](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/743903554)  
**Last Updated:** 2019-10-17  

# Overview (classic api/v2/users)  


<https://developer.zendesk.com/rest_api/docs/support/users>

Zendesk's public API /api/v2/user endpoints have caused capacity problems and production incidents in the past due to expensive SQL queries.   


Also we need to protect ourselves from abusive or accidental creation of an excessive number of users. We already have some customers with a 1M:1 ratio of end-users to agent. We need to come up with a strategy (a number of users allowed per plan type, and a way to manage customers who approach or violate this limit) including optionally allowing customers to exceed this limit if they have a legitimate use case.

## Two types of queries have been identified as problematic:

  * Queries for deep pagination, e.g. with high values for the LIMIT and OFFSET parameters
  * Count(*) for accounts with large number of users



## Anatoly from the Platform Capacity team has compiled a list of recent incidents here:

[https://zendesk.atlassian.net/wiki/spaces/CP/pages/706153754/2019-05-10+-+Users+API+capacity+assessment](https://zendesk.atlassian.net/wiki/spaces/CP/pages/706153754/2019-05-10+-+Users+API+capacity+assessment)

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/743903554)*

---

## Billing Growth

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/743018956](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/743018956)  
**Last Updated:** 2021-10-04  

# What would you say… you do here?

**Mission Statement**

Improve all aspects of Billing Shopping Cart experience through data, experimentation, and user testing

# What are we working on?  


**Recently Shipped**

  1. Shopping Cart Presets Experiment (Cheng from Walrus)



# What's coming up?

  1. Maintenance Mode improvements with Madison Upmarket Team
  2. Super cool experiments


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/743018956)*

---

## Looker Dashboards and ZDP access

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7429652481](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7429652481)  
**Last Updated:** 2025-08-22  

As mentioned in the project page, we have developed [dashboards in Looker](https://zendeskbi.cloud.looker.com/boards/207) to track Service Catalog adoption and usage. These dashboards take advantage of ZDP/Snowflake data and queries in order to present the data.

However, this is a fairly recent tool and access to it is not clear, so this document will serve as a guide on how to get access to both ZDP and Looker, as well as how to get the relevant permissions to view the necessary data and produce similar dashboards.

## Looker Access

As mentioned above, our dashboards, as well as many other from other teams, are available in Looker (not to be confused with Looker Studio, that is a different tool). Looker is a business intelligence platform specially tailored to organize and visualize data relevant to businesses, allowing people and teams to make informed decisions. This is what we are currently using at Zendesk.

However, access to Looker does not come by default to all developers. Access can be requested via Productiv, which will grant users a license to view the data. For elevated permissions, such as a Developer license (required to develop more dashboards) the BI & Reporting needs to be contacted. For more information check the following confluence page:

  * <https://zendeskdev.zendesk.com/hc/en-us/articles/8312771590042-Using-Looker-to-analyze-ZDP-data>




## Snowflake/ZDP access

The data used by Looker comes from ZDP/Snowflake, so access to the tool is also required. 

Access to Snowflake should be available by default to all Engineering members, which should include access to all relevant instances. It is also possible to request elevated access if the default one is not sufficient, which should be done by opening a JIRA ticket.

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7429652481)*

---

## Building a Test Strategy for a Program

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7427785033](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7427785033)  
**Last Updated:** 2025-08-25  

For any complex program, a refined testing strategy must emphasize rigorous planning, detailed documentation, automation maturity, risk mitigation and robust communication across multiple teams and layers. Below is a structured framework outlining the main phases of the testing lifecycle over 1 release:

For a multi-release program, rinse and repeat these steps for every release

61falsedecimalflattrue<https://zendesk.atlassian.net/wiki/spaces/ENG/whiteboard/7428210743?createdFromSlug=%2Fwiki%2Fspaces%2FENG%2Fpages%2Fedit-v2%2F7427785033>

* * *

### Planning

 _**Owner:** E2E Test Lead. _

_**Timeline:** Depending on the project schedule and time to launch, this phase should begin atleast ~2 sprints before Dev Code Complete_

**Aspect**| **Action**  
---|---  
**What to Test?** | Derive from Scope/Requirements | 

  * Product Lead/Business Lead to define scope/requirements documents
  * Build E2E Test Plan for these requirements

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7427785033)*

---

## Supercharge Setup Phase 2 - RFC

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7418020030](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7418020030)  
**Last Updated:** 2025-08-19  

61truenonelisttrue

## Context 

Supercharge Setup is a project designed to enhance the trial customer experience by simplifying account configuration. The Trial team uses the emails threads, which are fetched during the initial import process, to propose things like macros and auto replies.

## Motivation

Zendesk is a complex system and new customers (especially those who are not at the enterprise level) often have difficulty properly configuring their Zendesk accounts. By fetching entire email threads, we will be able to automatically propose parts of the account configuration and streamline the setup process. Simplifying this process increases the likelihood that trial customers will purchase a standard Zendesk subscription.

## Objectives

### In scope

  * **Import The Entire Email Thread**

    * Fetch mails from `Sent` folder.

    * Define how to send the emails from the `Sent` folder to the Trial team.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7418020030)*

---

## Global Event Bus Delivery

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/741382263](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/741382263)  
**Last Updated:** 2019-11-19  

Even if there is nothing to add into the table values, please do not remove the rows. They are an integral part of automatically displaying your page on the Project Page listing. 

Group|   
Goanna, Foundation Storage  
  
---|---  
Description| This page documents the Global Event Bus Project  
Roadmap Project| Multiple ROADs exist, System JIRAcae89f0e-c846-3d65-88a5-bb277a2031b3ROAD-4625, System JIRAcae89f0e-c846-3d65-88a5-bb277a2031b3ROAD-4626  
Primary Dev Team|   
Supporting Dev Teams| Chat Ops, Tea Pot, Foundation Config, Security, Network  
Product Manager|   
Program Manager|   
Engineering Leads|  +   
  
  


  



*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/741382263)*

---

## Alation Slowness & Capacity Escalation – Evidence Summary

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7413465546](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7413465546)  
**Last Updated:** 2025-08-17  

Zendesk has raised multiple high-severity tickets for persistent slowness, capacity, and reliability issues with our Alation instance. 

These problems directly undermine the value of the platform as an enterprise data catalog, especially for API-driven automation and governance.

## Critical Cases Demonstrating Slowness/Capacity Issues

**Reported Date**| **Case Number**| **Subject/Description**  
---|---|---  
Jun 18, 2025| 00101626| Alation instance extremely slow - 502 Bad Gateway errors when accessing catalog pages  
Jun 13, 2025| 00101375| Alation Instance Is Slow & Unusable  
Jun 5, 2025| 00096577| Restart Prod Instance  
May 28, 2025| 00096048| Alation Instance Is Slow  
May 28, 2025| 00096050| Restart Prod Instance  
May 1, 2025| 00094865| Gateway Timeouts & Bad Gateways When Querying Lineage  
Feb 12, 2025| 00091176| Lineage APIs Are Slow  
Jan 23, 2025| 00090164| 504 errors on dataflow API  
Dec 16, 2024| 00088928| 504 timeout when querying lineage  
Sep 5, 2024| 00083898| 504 timeouts  
  
## Nature of the Problems

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7413465546)*

---

## Communication Templates

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7410450651](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7410450651)  
**Last Updated:** 2025-08-26  

Effective and proactive communication across all teams ensures we hit deadlines and deliver projects on time. Here are some comms templates for various stages of E2E Testing Cycle

Sharing the Schedule (before or during the Pre-testing prep stage)

_Hello All, Here are some key dates/milestones (in US timezone) we will be tracking to help with timely prep and execution of the overall E2E testing for the <project name> **< Date>** launch._

_** This schedule is in the format <Date Deadlines> <Milestone> <Action Owner> **_

_ **Pre-testing prep**_

  *  _May 13: Test Kickoff (E2E Test Lead/Program)_

  * _May 17: Identify Test Champion (All teams)_

  * _May 24: Draft v1 of test plans / test cases (All teams)_

  * _Week of May 27-31: Prepare test data and test accounts (All teams)_

  * _May 29: Finalize test plans / test cases (All teams)_


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7410450651)*

---

## Staff service development tips and tricks (& calling production)

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/738820425](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/738820425)  
**Last Updated:** 2020-03-23  

This page is to gather all those tips and tricks you do develop core services.

This is similar to a classic related page and some of these entries are copies of their entries. 

2

## Failed PATCH Entitlement debugging

Tips using acme-app and kurl

## Raw MySQL console

Sample query

## Getting an account

ruby

 _All of these methods do the same thing. They take you to the shard the account is on.  _


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/738820425)*

---

## Weekly Engineering Meeting

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/736494552](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/736494552)  
**Last Updated:** 2025-09-08  

**Slack channel:** [#weekly-engineering](https://zendesk.slack.com/archives/CL59BGUCE)

**Goal:** This meeting aims to share key engineering thoughts and trends. With a growing team in different time zones, we must be purposeful about connecting on engineering-focused topics and learnings. We want to curate great content that's easily digestible, and has a regular cadence. 

**Why** : To help us all improve our craft as engineers, and consequently improve the quality of our product. 

**How:** Have a great success, problem, or failure you'd like to share? Talks can be submitted by filling out [this form](https://docs.google.com/forms/d/e/1FAIpQLSdeiXLhZuAknUN6A6fS24elK5r2eJSCeep9KtY_Jlinih5ing/viewform). Make sure your topic aligns with these guidelines:

  * The goal of Weekly Engineering is to share learnings - wins, fails, and roadblocks along the way. We want to hear the problem statement and the story behind the journey to find a solution.

  * Steer clear of announcements - we're keener to hear how and why the new tool or process was decided on, and how and why it came to be.




Submissions are reviewed weekly by the Content Team. A member of the Content Team will follow up with feedback and confirm your time slot after your submission is reviewed. Typically this will be done following the current week's conclusion of the Weekly Engineering meeting. 

If your talk was selected, congratulations! Follow these **Presenter Guidelines** to ensure a successful Weekly Engineering Meeting:

  * Add your slides in the provided deck at your earliest convenience to allow the Content Team time to review and provide feedback. *_Hard deadline_ for slides is the end of the week prior to the session you are scheduled for.

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/736494552)*

---

## AI agent simple setup documentation

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7357563239](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7357563239)  
**Last Updated:** 2025-08-15  

### General Info

  * Reach out to the [#genbots-conversational-experience-team](https://zendesk.enterprise.slack.com/archives/C07ANSKSFHV) Slack channel for general questions about our AI agent offering

  * [Jorge Nunes](https://zendesk.enterprise.slack.com/team/U073DQ1KT5Z) is the engineering manager, [Priscila Santos](https://zendesk.enterprise.slack.com/team/U07AGEBBHHQ) is an engineer we can reach out to as well.

  * AI agents can only be "trained" off of material available in the account's Knowledge Center - there is currently no way to upload one-off content. There is work in progress for [multiple content sources](https://docs.google.com/presentation/d/10G28fjLjXbMw2gav6sZiGPPJ-X1jp12W9iwKF8vDi28/edit?slide=id.g370431bec75_0_406#slide=id.g370431bec75_0_406) \- it's unclear if it will be ready for us in time.

  * Many of the admin center API endpoints required for AI agent provisioning are graphQL endpoints. If we are going to build this in the Onboarding Panel, it would probably make sense to adopt graphQL rather than mock it with REST.




## Knowledge Builder ()

The Knowledge Generation UX source lives in [Guide Client](https://github.com/zendesk/guide-client/tree/master/apps/knowledge-generation). The current flow uses the the [platform data graph](https://github.com/zendesk/platform-data-graph) `api/graphql` endpoint.

Primarily, there are two steps to this process.

The first operation is `GuideClient__HelpCenterTreeCompletion` which is used to generate the preview of the articles based on the three inputs, (Description, Type of business and FAQ data)

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7357563239)*

---

## Technical Design - Offers in OES

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7353434149](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7353434149)  
**Last Updated:** 2025-10-27  

## **Context**

Growth Engine generates personalized offers for the prospective buyers. This personalization is primarily based on an ML oriented approach using the ZDP and several other sources. 

While presenting these offers to our prospects and increasing the chance to avail them, we would also want to control how they are rendered. For the purpose of this document, this rendering aspect is concerned with the following

  * Order of presentation of these offers

  * Dismissal of an offer if the prospect is not interested

  * Capability to experiment with the Offer UX




## Required Approvers

**Name**| **Responsibility / Job Title**| **Date and comments**  
---|---|---  
Zach Dennis| Senior Staff Software Engineer|   

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7353434149)*

---

## Supercharge Setup Phase 1 - RFC

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7352812031](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7352812031)  
**Last Updated:** 2025-08-19  

61truenonelisttrue

## Context 

Supercharge Setup is a project designed to enhance the trial customer experience by simplifying account configuration. Email connectors fetch additional email metadata, which will be used to recommend Zendesk account settings such as triggers and views.

## Motivation

Zendesk is a complex system and new customers (especially those who are not at the enterprise level) often have difficulty properly configuring their Zendesk accounts. By fetching additional email metadata, we will be able to automatically propose parts of the account configuration and streamline the setup process. Simplifying this process increases the likelihood that trial customers will purchase a standard Zendesk subscription.

## Objectives

### In scope

  * **Expose Email Metadata (Labels)**

    * Fetch email labels from both Gmail and Exchange.

    * Use a common format for labels and store them in the ticket object (classic database).


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7352812031)*

---

## SPIKE: Cleansed Layer Completeness Checks using Formatted Layer

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7337607546](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7337607546)  
**Last Updated:** 2025-07-22  

## **Background**  
  
Completeness checks for the SCD1 cleansed layer currently rely on comparing row counts between DRDBs and cleansed layer tables. However, the DRDBs are costly to maintain and now only run once weekly due to DBA constraints. This weekly schedule prevents completeness checks from running daily or hourly in alignment with cleansed layer propagation schedules, leading to delayed detection of missing data. Delays impact the ability to backfill or rebuild cleansed tables timely for monthly critical reporting. Additionally, manual DRDB start/stop processes consume valuable engineering time.

## **Goal**

Investigate and evaluate alternative methods to perform cleansed layer completeness checks that do not require active DRDBs. The solution should enable more frequent completeness verification aligned with data propagation schedules, reduce operational overhead, and improve detection and remediation times for missing data.

## Out of Scope

  * SaaS -> Cleansed completeness checks

  * Global tables that have been propagated to cleansed

  * Views




## Questions

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7337607546)*

---

## How to respond to Snowflake incidents?

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7329875580](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7329875580)  
**Last Updated:** 2025-07-21  

The main Snowflake Status page is - <https://status.snowflake.com/>

It shows the current state of four components, as well as all current and past incidents.

# Should we call a zendesk incident? 

Yes. If either Database or Data Ingestion component experience an outage, that would affect:

  * OBP

  * Agent Months Reporting




The OBP has an SLA of 4 hours, so the impact would not be seen immediately. However, we should still call a **SEV-3** incident and make sure the owning team is paged and aware. If a Snowflake outage runs for more than 4 hours, we need to inform Zendesk OBP customers that there will be stale data.

In both cases, the owning team is [Koopa team](https://cerebro.zende.sk/teams/koopa). 

Also, inform #snowflake-admin-team channel that there is an active Snowflake incident. 

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7329875580)*

---

## 009 - Ticket Platform Field Migrations

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7325680235](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7325680235)  
**Last Updated:** 2025-09-09  

**Status**|  In progressYellow  
---|---  
**Impact**|  MediumYellow  
**Driver**|   
**Approver**|   
**Contributors**|   
**Informed**|  @ stakeholders  
**Due date**|   
  
## Documentation

  * [Platform Objects documentation](https://zendeskdev.zendesk.com/hc/en-us/articles/9128839248794-How-do-I-create-platform-objects) (sections on updating and uninstalling)

  * TODO: Link Zendesk Engineering Docs for allowed migration changes (To be created)

  * TODO: Link Zendesk Engineering Docs for how to migrate (To be created)

  * Related decision: 011 - Ticket Platform Field and Option Inactivation



*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7325680235)*

---

## Re: Platform Data Architecture Program

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/970457878](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/970457878)  
**Last Updated:** 2020-03-18  

When can we rename this program to Data Platform Architecture so as not to confuse?

---

## Platform Data Architecture

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/970330740](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/970330740)  
**Last Updated:** 2023-04-07  

# Updates

Platform Data Architecture Refresh, April 2021

# Background

Over the past few years, Zendesk has been transitioning from a collection of more or less integrated products into a cohesive suite with unified, extensible workflows, centralised administration, and shared notions of users and other core concepts. (See the [_One Zendesk strategy_](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/786935424/One+Zendesk+Strategy) doc written in late 2019.) We are more tightly and deeply integrating data sets originating in one application into other applications and features, existing as well as new.

Additionally, as we seek to evolve as a platform for Enterprise solutions, we will need to present not a fragmented landscape of domain models that make sense only within their respective products, but rather a cohesive set of core models, covering the breadth of our offerings, coupled with powerful practical capabilities that allow ourselves and third parties to efficiently integrate, extend, and build upon the Zendesk Platform.

#   
Data at the Centre

2falseleftrich10821f4b3-8b30-48fa-b644-beaf428795acConfluence:2083817226700dc441e2d-7f53-4541-a802-3aa1415fe1a3dc441e2d-7f53-4541-a802-3aa1415fe1a3|103589275|970330740|byzlXLxITB14pfx97hwbRCc0+3stHGVpXCMoouHedeQ=1584697098296500

In order to reach our Platform goals, we need to move to an architecture that puts our core data sets at the center and enables practical applications to be built using powerful, scalable primitives that take full advantage of those data sets.

Platform Data Architecture can be understood as the formal way we think about data in the Platform. To date we have identified three main pillars (and more may be described later). 

## Standard Objects 

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/970330740)*

---

## Platform Data Registry

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/952048005](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/952048005)  
**Last Updated:** 2025-01-23  

For now, this is where we will list the types available for use in our platform. These will include Standard Objects, Core Events, Custom Objects, and other types we introduce in the future. 

**Platform Data Category 1**| **Name**| **ZRN Type Prefix**| **Schema Location**| **Checklist Link**| **Kafka topic**| **Kafka key**  
| **Kafka headers**| **Approval Details**| **Estimated Metrics**  
---|---|---|---|---|---|---|---|---|---  
Standard Object| Ticket| zen:ticket| | | | | | |   
Standard Object| User| zen:user| | | | | | |   
Standard Object| User Authentication| | [platform/standard/users/user_authentication_events.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/standard/users/user_authentication_events.proto)| | `platform.standard.user_authentication_events`| | | [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/736)| (as of 13th Nov 2020)  
**# events/entities** 520,000 per pod per day**Avg message size**  
100 bytes**Throughput**  
360/min  
Standard Object| Article| zen:article| [platform/standard/article.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/standard/articles/article.proto) | [Checklist](https://docs.google.com/document/d/1MXPxvIaCSTuwDIUCZBOvws-neIfsB-LCccKzq8Wp8hc/edit?usp=sharing)| `platform.core.articles`| TBC: `"account_id/entity_id"` where `entity_id` is a concatenation of article id and locale for a unique identifier| | |   
Standard Object | Community Post| zen:community_post| [platform/standard/community_posts/community_post.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/standard/community_posts/community_post.proto) | [Checklist](https://docs.google.com/document/d/1MXPxvIaCSTuwDIUCZBOvws-neIfsB-LCccKzq8Wp8hc/edit?usp=sharing)| `platform.standard.community_posts`| TBC:`"account_id/community_post_id"`| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| |   
Standard Object| Deal| zen:deal| [platform/core/deal.proto](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/platform/core/deal.proto) | [Checklist](https://docs.google.com/document/d/1AMaeQqRFegiJ80A4dXxCjRy97K4ATYHACii3_e_Ief8/edit)| `mirror.platform.core.deals`| `account_id/entity_id`

  * `entity_id` \- Deal ID, autoincremented PK from database

| `ZENDESK_ACCOUNT_ID``ZENDESK_PB_HEADER`| [Approval PR](https://github.com/zendesk/zendesk_protobuf_schemas/pull/583)| (as of 19th Aug 2020)  
**# events/entities**  
`29,475,632`**Avg message size**  

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/952048005)*

---

## Dark Knight

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/923468214](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/923468214)  
**Last Updated:** 2025-10-28  

[Dark Knight Schedule](https://calendar.google.com/calendar/embed?src=zendesk.com_p8thqd98drp37da1lfshed51ug%40group.calendar.google.com&ctz=America%2FLos_Angeles)

**tl;dr:**  The dark knight keeps the team shielded from interrupts. Resolves remediation and healing work that does not directly align to the roadmap.

The DK is a shameless rip off of the [Rockstars, Janitors and Builders](https://www.youtube.com/watch?v=posb7CzWSFc) concept.

# The Dark Knight

"I'm whatever the team needs me to be" (Batman voice)

Protects the team so they can stay focused.  Monitors the health of our systems.  High-priority bug squasher.

[The 10,000 foot view of DK.](https://lucid.app/lucidspark/83e8bcb8-417a-4a66-9d24-6675449fa2f1/edit?viewport_loc=-2563%2C458%2C3982%2C2271%2C0_0&invitationId=inv_dc856319-9bc3-4080-97a3-6d62d3e86007)

### The Dark Knight's Priorities:

### 1) Daily health check-ins:

  1. Monitor our SLAs.  You should be checking these daily to see how the health of our systems are.  File tickets and alert the team as appropriate. If an error budget is blown, the Dark Knight should kick off the remediation process.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/923468214)*

---

## Architecture Directions 2020-2022

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/911308944](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/911308944)  
**Last Updated:** 2020-02-24  

The presentation embedded below captures a number of important topics related to the long range planning (LRP) cycle that ended in late 2019. Members of the architecture team engaged with Group Tech Leads in each local region to discuss the role this material should play in shaping technical roadmaps.

One initiative in particular emerged from the Nov 2019 Singapore leadership offsite: the need to address many of the challenges that our service oriented architecture and increasingly distributed data architecture presents. The resulting "[Core Objects](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/829821236/Core+Objects)" initiative is aimed to provide a decoupled mechanism for services that need to consume key data types across the Zendesk product portfolio such as Users, Tickets, Conversations and Content and also support the development of common capabilities such as Search, Views, Data Export and Explore integration over time. Core Objects will also play a role in the Zendesk Platform GraphQL API work that we are exploring in 2020.

1280truehttps://docs.google.com/presentation/d/1H2ADzUTdrgNl6lJ3LO9jirdzQGDYD5sx3aV9GqcMzF4/edit?ts=5e539f5a#slide=id.g59bee3a5ff_1_168720

---

## DevLeads Summit 2014

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/86116278](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/86116278)  
**Last Updated:** 2018-02-23  

## **Note: DevLead is our old pre-2018 name for  .**

## Why

To discuss and resolve key questions around the next generation of the Zendesk platform and architecture. 

## Where

1019 Market St.

## When

# September 15-19, 2014

  


## Planning to Attend:

  1. Tony

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/86116278)*

---

## One Zendesk: Strategy

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/786935424](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/786935424)  
**Last Updated:** 2019-12-17  

([Republished from Slack post ](https://zendesk.slack.com/archives/CDPSAQ963/p1576170766263500)to aid discoverability)

We are in the middle of a large-scale shift in strategy that will affect most everybody in the company. At the latest all-hands event in San Francisco, Søren and Shawna presented the vision for the company going forward.

Some quotes:

  * "In 2022, we will have two major $1B rev businesses (SMB/MM & Ent)"
    * "The easiest CRM software for SMBs & MMs to discover, try, buy & use for engaging their customers. This is anchored on conversation-centric Support & Sell Suites, built on Sunshine. "
    * "We are a strategic provider of modern CX solutions to enterprise that are built on and extendable with Sunshine, leveraging a mature partner ecosystem."
  * "Polaris as the start of a consolidated UI platform for all of our applications and platform"
  * "Deliver a single, well integrated Platform (Sunshine) "
  * "Build on a single, manageable, compliant, resilient stack (Foundation)"
  * "Move towards a common Architecture; API, Data & UI"



We want to emphasize how much of a shift this is. Consider our strategy over the last couple of years:

[](https://www.lucidchart.com/documents/edit/7a95a81c-84ff-4aa9-9160-a66a347cb754/3eI~x-ZlcdKm?callback=close&name=docs&callback_type=back&v=4769&s=612)


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/786935424)*

---

## ProgInScala3ed.pdf

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/att778476544](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/att778476544)  
**Last Updated:** 2019-11-12  

---

## Ticket Domain Events

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/773430135](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/773430135)  
**Last Updated:** 2025-10-10  

**Ticket Domain Events**  (abbreviated as "TDE") are messages published to our event bus to provide multiple consumers notification that a change has happened to a Ticket. This allows developers to react to or duplicate ticket changes in a low-latency, asynchronous, decoupled fashion. 

## Background Reading

  * [Cerebro: Ticket Domain Events reference](https://cerebro.zende.sk/projects/ticket-domain-events)

  * [ADR: Embracing Domain Events](https://techmenu.zende.sk/adrs/embracing-domain-events/)

  * [Standard: Events & Streaming Data](https://techmenu.zende.sk/standards/events/)

  * [ADR: Kafka is the Event Bus](https://techmenu.zende.sk/adrs/kafka-is-the-event-bus/)

  * [ADR: Ticket Domain Events: Positions and schema decisions](https://techmenu.zende.sk/adrs/ticket-domain-events/)




## What do events on the bus look like?

In practice, each event is represented as a single Protobuf-encoded message written to the `support.ticket_events` topic in Kafka, partitioned by the ticket id. See the [zendesk/service.yml](https://github.com/zendesk/zendesk/blob/dc409590f4bc81db8969abb44a011045371869ad/service.yml#L284-L289) for the current topic configuration. For example, a single API call resulting in the creation of a ticket will result in many events (e.g. `TicketCreated`, `CommentAdded`, `SubjectChanged`) placed in the same Kafka partition. For the most current authoritative reference to format of the events, read the [zendesk.protobuf.support.tickets.v2.TicketEvent message schema in the zendesk_protobuf_schemas](https://github.com/zendesk/zendesk_protobuf_schemas/blob/master/schemas/zendesk/protobuf/support/tickets/v2/ticket_events.proto) repository.

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/773430135)*

---

## Quick Assist

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/767951028](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/767951028)  
**Last Updated:** 2019-10-24  

System JIRAkey,summary,type,created,updated,due,assignee,reporter,priority,status,resolutioncae89f0e-c846-3d65-88a5-bb277a2031b3ROAD-4966

System JIRAkey,summary,type,created,updated,due,assignee,reporter,priority,status,resolutioncae89f0e-c846-3d65-88a5-bb277a2031b3SGT-501

[Deck for Support product demos](https://docs.google.com/presentation/d/1gMPmx2uGpAtCcZyIH1SQFK84oSdABFThd45Qz1wNNDY/edit?usp=sharing)

[5 Minute Overview + Demo](https://zendesk.zoom.us/recording/play/fjt5kK8JeFEAgti40OTbPy-bBz1b3sFvS7AHD1FJ4k_2O7ZHK2WnK4sdZFQxduQV)

  


Quick Assist is a new help + onboarding feature released and maintained by Ponderosa; it is an evergreen interface implemented within Lotus React, aimed to enable customers and trialers to access help and learn about important features.

Feature goals:

  * Reduce Advocacy contact / Z1 tickets filed by customers during their onboarding and initial product use
  * Provide condensed documentation for key account provisioning + onboarding points in a friendly, easy-to-use portal
  * Enable customers to get up and running with their new Zendesk



*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/767951028)*

---

## Repairing the Incomplete Backfill of Archived Tickets

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7575373748](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7575373748)  
**Last Updated:** 2025-11-27  

# The Problem

When attempting to migrate the SKU Expansion metrics to Zendesk Data Platform (ZDP), the AdminX team found proof that tickets are missing from ZDP that are present in Legacy Data Lake (LDL). These tickets are old, and not present anywhere in ZDP.

For our metrics to be consistent with those we already provide to our customers, we need to repair this missing data.

# How do we know this?

AdminX was able to track down individual tickets that are missing from ZDP but present in LDL, see:

<https://docs.google.com/document/d/1OOqJlt9GkvYznGh1tYenYtlz1i3J_F3s8HkxZUqun0g/edit?tab=t.bl2j9iehe0g>

In summary:

  * These tickets are all archived, and before 2017

  * ZDP started in 2023 

  * These tickets would have been archived long before ZDP began ingesting data via CDC


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7575373748)*

---

## Data Masking GA: Drive E2E Testing

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7559020826](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7559020826)  
**Last Updated:** 2025-10-29  

# Overview  
  
CSQ will be driving E2E testing for Data Masking team's GA release. To be able to release with confidence, we would like to ensure each team involved has done the following:

  * Created an E2E test plan

  * Written tests that run in at least 1 Jenkins job

  * Conducted load testing as needed

  * Completed testing by the Go/ No-go date

  * Given the sign-off that testing is completed by the Go/ No-go date




For the duration of the E2E testing window, there are 2x per week test sync meetings for all dependency teams (to accommodate all time zones) as well as a 1x per week meeting between Data Masking + CSQ, in order to communicate and sync on testing progress, questions, bugs, blockers, etc.

# Resources

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7559020826)*

---

## [Research] How Yuki Works ?

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7558299743](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7558299743)  
**Last Updated:** 2025-10-31  

> This doc describe how yuki tool works and how we could integrate into our existing infrastructure.

## How YUKI Works ?  


Yuki analyzes each query along with Snowflake warehouse metadata to decide which warehouses a query should run on. It does this by:

  * Reviewing query execution patterns and metadata such as Query IDs, timestamps, runtime, warehouse sizes, credit usage, and execution stats over the last 30 days

  * Detecting repeated query patterns and evaluating best fit warehouse size

  * Selecting the appropriate warehouse for the query dynamically




The goal is to reduce idle warehouse time, optimizing warehouse usage and lowering costs.

To route queries through Yuki, deploy the Yuki proxy in your environment using the Helm chart and Terraform. Your service's queries first pass through Yuki, which selects the right warehouse for execution based on its analysis.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7558299743)*

---

## Attribute Data Flow.pdf

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/att7533887945](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/att7533887945)  
**Last Updated:** 2025-10-12  

---

## Attribute Sensor Overview.pdf

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/att7533625889](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/att7533625889)  
**Last Updated:** 2025-10-12  

---

## [WIP] Attrib.io Proof of Concept

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7518453944](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7518453944)  
**Last Updated:** 2025-11-10  

none

## Introduction

Slack channels: [#zen-attribute-ext](https://zendesk.slack.com/archives/C09L4D0S41X/p1760056339020339), [#temp-attribute-vendor-staging-pic](https://zendesk.enterprise.slack.com/archives/C09LSK50K7C)

Attribute is a business observability platform that allocates cloud costs to customers, products, and teams without new tagging, using workload telemetry. They use proprietary eBPF algorithm to inspect network packet to do cost attribution. The sensor is deployed as a privileged DaemonSet on the Kubernetes clusters and claims a "security-first design," local data minimization, and high operational safety with low overhead.  However, the deployment model--kernel-privileged, cloud SaaS backend and unverifiable data redaction carries risk which needs to be thoroughly evaluated and considered.

### Purpose

Purpose of the POC is to determinte if [attrib.io](http://attrib.io) could does what it's website says:

  * Automate cost allocation without tagging by attributing costs to customer accounts (Coupang vs Ubiquiti etc) or customer segments. 

  * Ability to allocate costs by features (API endpoints) from requests -> database calls etc.




cost attribution by customer accounts

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7518453944)*

---

## Ticket Platform Field Deactivation

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7508492385](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7508492385)  
**Last Updated:** 2025-10-06  

## Deactivation

In the event that we want to disable a feature for a customer, Ticket Platform Fields can be deactivated from within Classic GenericFeatureInstaller#deactivate. 

As of Q3 of 2025, an "inactive" state means that `ticket_field.is_active` is set to `false`. This is our MVP to support deactivation for ITAM and Realtime QA.

**Note:** Features with multiple installers must implement a deactivate method for each installer. Currently, installers without a deactivate method will be silently skipped, which could possibly lead to a state where some fields are deactivated and some fields remain active. 

## Reactivation

The feature can be reinstalled by re-running GenericFeatureInstaller#install and/or by calling install method of the FeatureEnablement API. 

Please reach out to #ask-ticket-platform with any questions!

## Deactivated Field Behavior 

A form with active platform fields looks like this:

After running deactivation, the deactivated platform fields will no longer be visible on the form:


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7508492385)*

---

## 014 - Platform Features State Table Schema

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7508459597](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7508459597)  
**Last Updated:** 2025-11-11  

**Status**|  COMPLETEGreen  
---|---  
**Impact**|  MediumYellow  
**Driver**|   
**Approvers**|   
**Contributors**|  @ contributors  
**Informed**|   
**Due date**|  Type // to add a date  
**Outcome**|  Decide on the schema and indexes for the Platform Feature state Table  
  
16falsedecimallisttrue

# Background

In our early iterations of ticket platform fields and the feature installation path, we decided not to store feature state directly. We decided to rely on existing feature state mechanisms at Zendesk instead, namely Product Service and Account Settings. We did not want to build a new feature state management system when a few of them already existed at Zendesk. Our hope was that those existing systems could meet our needs, but we figured that we could always decide to build our own feature state system if needed later on.

## Why we decided to begin storing state

As of Q4 of 2025, we have decided to track state for platform features. While it was possible to avoid platform state management in the short term, the lack of state and version awareness is creating issues as migrations, rollbacks, and deactivations could create versioning discrepancies between accounts. A source of truth across platform features will improve development speed and incident remediation as we continue to platformatize additional Zendesk capabilities such as triggers, rules, and views.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7508459597)*

---

## ML EAP (Production) - Test run 7 (25773741)

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7507804339](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7507804339)  
**Last Updated:** 2025-10-06  

# Setup Details

DBT Repository: <https://github.com/zendesk/zdp_dbt_regional_account_move_testing>

Test plan: <https://docs.google.com/document/d/1ox-nLC6ZeWDRGuM7D9BZqA1el56DmPANjJ0JpZV826k/edit?tab=t.0>

## Test Account

**Account ID**| **Pod**| **Pandora**| **Domain**  
---|---|---|---  
25773741| 13| [394810](https://pandora-v2.zende.sk/resources/accounts/394810)| <https://z4nab-f598b8-c5a76c309032f612d3e7dcc52cf5a1220a1556.zendesk.com/>  
25778694| 26| [395281](https://pandora-v2.zende.sk/resources/accounts/395281)| <https://z4n-acc-mv-test-1.zendesk.com>  
25778693| 26| [395280](https://pandora-v2.zende.sk/resources/accounts/395280)| <https://z4n-acc-mv-test-2.zendesk.com>  
  
# Steps:

**UTC**|  ?| **Details**  
---|---|---  
**Preparation**  
 |  694 3ce56c20-9918-4c89-aabf-d6b788674baf complete | Create a new account for testing, details are [here](https://github.com/zendesk/zdp-account-moves-testing/blob/672dfdb4953c6e79dbc82c270e277acd8d3c8b13/README.md#L242).ID: 25778694  

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7507804339)*

---

## Ticket Platform Fields - On-call Runbook

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7501644272](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7501644272)  
**Last Updated:** 2025-11-20  

## Summary  
  
Ticket Platform Fields (TPF) are a feature that allows Zendesk Teams to store data on a ticket using ticket fields.

This document runs through investigation steps, common issues, and remediations for those issues.

## Common Issues

### Customer-side API issues

Features that create TPFs are creating new fields on a customer's account. We have had this cause issues for a customer because their custom code interacting with the Fields and Tickets APIs was not expecting the format of the new field. In these cases the customer will need to remediate on their end, however we can relieve the issue by removing the feature from the account.

## Remediations

Requires RIC write access. Perform these remediations with a buddy and only if necessary!

## Disabling Fields

In RIC, find the fields by `key` and change their `is_active` flag to false.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7501644272)*

---

## Hidden Ticket Platform Fields - On-Call Runbook

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7501644240](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7501644240)  
**Last Updated:** 2025-09-24  

## Summary

Hidden Ticket Platform Fields are a feature that allows Zendesk Teams to store data on a ticket using ticket fields, without exposing that data to customers. Hidden Ticket fields are not visible or editable by either Agents or Admins. They should not be visible to customers via any APIs or UIs.

## Troubleshooting Details

## 1\. Don't Panic

Hidden Ticket Platform Fields are Restricted Availability, and are currently only approved for one use case: Resolution Based Pricing (RBP).

RBP does not store any sensitive data or PII. While we do not want RBP data exposed to customers, it does not represent a security incident if data is somehow visible somewhere.

## 2\. Investigate

For issues with Hidden Ticket Platform Fields, we will likely have some tolerance of issues.

### Visible Hidden Fields

Investigate the root cause and understand how we might solve it. Hand off to Raichu or Ticket Platform during that team's business hours.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7501644240)*

---

## ML EAP - Test run 6 (20250918)

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7486341121](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7486341121)  
**Last Updated:** 2025-09-22  

# Setup Details

DBT Repository: <https://github.com/zendesk/zdp_dbt_regional_account_move_testing>

Test plan: <https://docs.google.com/document/d/1ox-nLC6ZeWDRGuM7D9BZqA1el56DmPANjJ0JpZV826k/edit?tab=t.0>

## Test Account

**Account ID**| **Pod**| **Pandora**| **Domain**  
---|---|---|---  
24294674| 999| [392035](https://pandora-v2.zende.sk/resources/accounts/392035)| <https://z3nacc-mv-test0918-999-1.zendesk-staging.com>  
24294678| 999| [392039](https://pandora-v2.zende.sk/resources/accounts/392039)| <https://z3nacc-mv-test0918-999-2.zendesk-staging.com>  
24294679| 999| [392040](https://pandora-v2.zende.sk/resources/accounts/392040)| <https://z3nacc-mv-test0918-999-3.zendesk-staging.com>  
24294680| 999| [392041](https://pandora-v2.zende.sk/resources/accounts/392041)| <https://z3nacc-mv-test0918-999-4.zendesk-staging.com>  
24294677| 998| [392036](https://pandora-v2.zende.sk/resources/accounts/392036)| <https://z3nacc-mv-test0918-998-1.zendesk-staging.com>  
24294673| 998| [392034](https://pandora-v2.zende.sk/resources/accounts/392034)| <https://z3nacc-mv-test0918-998-2.zendesk-staging.com>  
24294676| 998| [392038](https://pandora-v2.zende.sk/resources/accounts/392038)| <https://z3nacc-mv-test0918-998-3.zendesk-staging.com>  
24294675| 998| [392037](https://pandora-v2.zende.sk/resources/accounts/392037)| <https://z3nacc-mv-test0918-998-4.zendesk-staging.com>  
  
# Steps:

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7486341121)*

---

## ML EAP - Test run 5

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7484440577](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7484440577)  
**Last Updated:** 2025-09-17  

# Setup Details  
  
DBT Repository: <https://github.com/zendesk/zdp_dbt_regional_account_move_testing>

Test plan: <https://docs.google.com/document/d/1ox-nLC6ZeWDRGuM7D9BZqA1el56DmPANjJ0JpZV826k/edit?tab=t.0>

## Test Account

**Account ID**| **Pod**| **Pandora**| **Domain**  
---|---|---|---  
24271416| 999| [ _387974_](https://pandora-v2.zende.sk/resources/accounts/387974)| [ _https://z4n-acc-mv-test-999-3.zendesk-staging.com_](https://z4n-acc-mv-test-999-3.zendesk-staging.com/)  
  
# Steps:

**UTC**|  ?| **Details**  
---|---|---  
**Preparation**  
 |  445 3ce56c20-9918-4c89-aabf-d6b788674baf complete | Create a new account for testing, details are [here](https://github.com/zendesk/zdp-account-moves-testing/blob/672dfdb4953c6e79dbc82c270e277acd8d3c8b13/README.md#L242).ID: 24271416  
|  446 0bd565ba-67fc-4b76-ba6c-2caea213412f complete | Update monitoring notebook with account and table details  
 |  447 00265fd8-0762-492c-8c6f-9eb35c994c22 complete | Add data for the account in formatted.   

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7484440577)*

---

## ML EAP - Test run 4

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7481917442](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7481917442)  
**Last Updated:** 2025-09-16  

# Setup Details  
  
DBT Repository: <https://github.com/zendesk/zdp_dbt_regional_account_move_testing>

Test plan: <https://docs.google.com/document/d/1ox-nLC6ZeWDRGuM7D9BZqA1el56DmPANjJ0JpZV826k/edit?tab=t.0>

## Test Account

**Account ID**| **Pod**| **Pandora**| **Domain**  
---|---|---|---  
24271414| 999| [ _387972_](https://pandora-v2.zende.sk/resources/accounts/387972)| [ _https://z4n-acc-mv-test-999-1.zendesk-staging.com_](https://z4n-acc-mv-test-999-1.zendesk-staging.com/)  
  
# Steps:

**UTC**|  ?| **Details**  
---|---|---  
**Preparation**  
 |  185 3ce56c20-9918-4c89-aabf-d6b788674baf complete | Create a new account for testing, details are [here](https://github.com/zendesk/zdp-account-moves-testing/blob/672dfdb4953c6e79dbc82c270e277acd8d3c8b13/README.md#L242).ID: 24271414  
|  186 0bd565ba-67fc-4b76-ba6c-2caea213412f incomplete | Update monitoring notebook with account and table details  
 |  187 00265fd8-0762-492c-8c6f-9eb35c994c22 complete | Add data for the account in formatted. 10 records  

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7481917442)*

---

## ML EAP - Test run 3

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7480475649](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7480475649)  
**Last Updated:** 2025-09-15  

# Setup Details  
  
DBT Repository: [https://github.com/zendesk/zdp_dbt_regional_ml_agent_productivity](https://github.com/zendesk/zdp_dbt_regional_ml_agent_productivity/)

Test plan: <https://docs.google.com/document/d/1ox-nLC6ZeWDRGuM7D9BZqA1el56DmPANjJ0JpZV826k/edit?tab=t.0>

## Test Account

**Account ID**| **Pod**| **Pandora**| **Domain**  
---|---|---|---  
24271415| 998| [ _387971_](https://pandora-v2.zende.sk/resources/accounts/387971)| [ _https://z4n-acc-mv-test-998-3.zendesk-staging.com_](https://z4n-acc-mv-test-998-3.zendesk-staging.com/)  
  
# Steps:

**UTC**|  ?| **Details**  
---|---|---  
**Preparation**  
 |  185 3ce56c20-9918-4c89-aabf-d6b788674baf complete | Create a new account for testing, details are [here](https://github.com/zendesk/zdp-account-moves-testing/blob/672dfdb4953c6e79dbc82c270e277acd8d3c8b13/README.md#L242).ID: 24271415 [_https://z4n-acc-mv-test-998-3.zendesk-staging.com_](https://z4n-acc-mv-test-998-3.zendesk-staging.com/)  
|  186 0bd565ba-67fc-4b76-ba6c-2caea213412f complete | Update monitoring notebook with account and table details  
 |  187 00265fd8-0762-492c-8c6f-9eb35c994c22 complete | Add data for the account in formatted. 10 records  

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7480475649)*

---

## ML EAP - Test run 2

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7475625998](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7475625998)  
**Last Updated:** 2025-09-14  

# Setup Details  
  
DBT Repository: [https://github.com/zendesk/zdp_dbt_regional_ml_agent_productivity](https://github.com/zendesk/zdp_dbt_regional_ml_agent_productivity/)

Test plan: <https://docs.google.com/document/d/1ox-nLC6ZeWDRGuM7D9BZqA1el56DmPANjJ0JpZV826k/edit?tab=t.0>

## Test Account

**Account ID**| **Pod**| **Pandora**| **Domain**  
---|---|---|---  
24271413| 998| [387973](https://pandora-v2.zende.sk/resources/accounts/387973)| <https://z4n-acc-mv-test-998-2.zendesk-staging.com>  
  
# Steps:

**UTC**|  ?| **Details**  
---|---|---  
**Preparation**  
 |  85 3ce56c20-9918-4c89-aabf-d6b788674baf complete | Create a new account for testing, details are [here](https://github.com/zendesk/zdp-account-moves-testing/blob/672dfdb4953c6e79dbc82c270e277acd8d3c8b13/README.md#L242).ID: 24271413 <https://z4n-acc-mv-test-998-2.zendesk-staging.com>  
|  86 0bd565ba-67fc-4b76-ba6c-2caea213412f complete | Update monitoring notebook with account and table details  
 |  87 00265fd8-0762-492c-8c6f-9eb35c994c22 complete | Add data for the account in formatted. 10 records  

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7475625998)*

---

## 013 - Installer - install and update (migrate) behavior

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7470153868](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7470153868)  
**Last Updated:** 2025-09-15  

**Status**|  In progressYellow  
---|---  
**Impact**|  LowGreen  
**Driver**|   
**Approver**|  @ approver  
**Contributors**|  @ contributors  
**Informed**|  @ stakeholders  
**Due date**|  Type // to add a date  
**Resources**|  Type /link to add links to relevant research, pages, and related decisions  
  
##  Relevant data

  * 009 - Ticket Platform Field Migrations




##  Background

In 009 - Ticket Platform Field Migrations we decide on the specific fields that can be migrated and why, and we discuss the decision not to store versioning metadata and build a more robust (and complicated) migration system.

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7470153868)*

---

## Review process for dataset collection and security classification

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7447871650](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7447871650)  
**Last Updated:** 2025-09-10  

## Background

Currently, DGO and Stewards are responsible for assigning dataset collections and L5 security classifications at both the dataset and column levels in ZDP. This model ensures oversight and compliance, but it also creates a bottleneck in the overall ingestion and onboarding process, sometimes causing considerable delays in enabling access for data consumers.

## Problem Statement

The mandatory DGO/Steward review process for dataset collections and column-level security classification is slowing down dataset ingestion and reducing agility in making new datasets available to consumers.

## Objective

This document evaluates whether the responsibility for setting dataset collections and L5 security classifications can be shifted directly to data producers, streamlining the onboarding process and reducing delays:

  * Assess feasibility and risks of such delegation.

  * Determine if/when DGO review is still necessary.

  * Identify compliance/governance implications.

  * Provide a reasoned recommendation and proposed next steps.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7447871650)*

---

## 012 - Platform Fields will not support tag synchronization

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7441580555](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7441580555)  
**Last Updated:** 2025-08-28  

**Status**|  In progressYellow  
---|---  
**Impact**|  HighRed / MediumYellow / LowGreen  
**Driver**|  @ mention driver  
**Approver**|  @ approver  
**Contributors**|  @ contributors  
**Informed**|  @ stakeholders  
**Due date**|  Type // to add a date  
**Resources**|  Type /link to add links to relevant research, pages, and related decisions  
  
##  Background

Provide context on a decision the team needs to make and include information about constraints and challenges.

##  Relevant data

Add any data or feedback the team should consider when making this decision.

##  Options considered


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7441580555)*

---

## Documentation - How Tos

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7435190423](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7435190423)  
**Last Updated:** 2025-10-07  

note

ZDP account move is in staging testing phase, production rollout will be late October, 2025.

ZDP account move is in staging testing phase, production rollout will be late October, 2025.

# Account Moves Overview

Zendesk offers data locality features that allow customers to host their data in specific geographic regions. When a customer requests that their account is moved to a new region, all associated service data must be migrated to the newly selected region.

## Types of Account Moves

  * **Cross-region Moves** : When a customer's data must be physically relocated from one geographic region to another.

  * **Within Region Moves** : Zendesk periodically relocates accounts within regions (pods) for load balancing. These are:

    * ZDP only filters CDC/PDA changes generated by application for account move, considering these are not relevant for analytics.

    * Fully transparent to customers


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7435190423)*

---

## Theming Center Refactoring Plan

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7434338372](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7434338372)  
**Last Updated:** 2025-09-26  

Theming center (TC) was originally created with a Command Query Responsibility Segregation (CQRS) architecture and Event Sourcing. This decision was initially made to support a version history feature for themes, but then during development a feature that relies on Github was added instead. However, CQRS/Event Sourcing was already in place and ended up no being removed. 

Nowadays, this introduces a couple of issues that make using and updating Theming Center difficult, such as:

  * Complexity: we have a complex architecture resulting in a codebase where it is difficult to understand the business logic and make any changes

  * Performance: we have problems keeping the latest state of our projections which can lead to inconsistencies

  * Data auditing: with the current data modeling it is really hard to query and identify, for example, how many accounts have themes in a specific state, as well as other metrics.




All of these make our development slower, as well as introduces delays when we need to audit data to address customers' questions. With this in mind, we want to do a refactor of Theming Center that will use ActiveRecord instead of the CQRS pattern/Event Sourcing.

This document will present an overview of the steps we will need to take to achieve this, as well as an outline of the possible solution. 

## Data Model and Database

Due to a usage of CQRS and Event Sourcing we currently use Projections and Aggregates to check the state of a Theme/Marketplace License and perform updates. Instead of having these, we want to have ActiveRecord models that represent the elements we need to manipulate, allowing us to save them in a more traditional way. 

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7434338372)*

---

## 011 - Ticket Platform Field and Option Inactivation

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7429129025](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7429129025)  
**Last Updated:** 2025-09-26  

**Status**|  In progressYellow  
---|---  
**Impact**|  HighRed / MediumYellow / LowGreen  
**Driver**|   
**Approver**|   
**Contributors**|  @ contributors  
**Informed**|  @ stakeholders  
**Due date**|  Type // to add a date  
**Resources**|   
  
##   Background

We need to implement inactivation functionality for Ticket Platform Fields and field options. Platform fields differ from custom fields in that they are created and managed by Zendesk internal teams rather than customers. We need to determine the best mechanism for inactivating fields and field options while minimizing code changes, database modifications, and API impact.

##  Relevant data

Currently:

  * Ticket Platform Fields have an `is_active` boolean flag that controls visibility and usage


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7429129025)*

---

## How to Write a Funfiller Backfill

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7425852039](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7425852039)  
**Last Updated:** 2025-09-15  

Funfiller is a backfill infrastructure that is specific to the Classic ecosystem and the data in the pods in Aurora. It's based on more generalized state machine and durable job system that is in the [concurable gem](https://github.com/zendesk/concurable). It's a high throughput, concurrent, durable backfill system built to use to backfill large volumes of data quickly. More information on the general structure and how it was built is in the Funfiller page. There is also more documentation on the Funfiller infrastructure in Classic in the readme files in the Funfiller folder in Classic. The general [readme](https://github.com/zendesk/zendesk/blob/main/app/backfills/funfiller/README.md) and the [fanout readme](https://github.com/zendesk/zendesk/blob/main/app/backfills/funfiller/fan_out/README.md) will provide more in depth background on overall structure.

## Where to start:

If you're here then you need to write a backfill to repair, or create new data in aurora or DynamoDB or both for some or multiple Classic models. A few details will help clarify what your backfill will look like and what modules of Funfiller will be useful for you.

### To Fan Out or Not to Fan Out?

Funfiller has a FanOut extension that can be included in your backfill. This provides a hierarcical job structure, which starts at the Pod level and goes all the way down to an account_record level(aka Tickets). See a visual representation here. 

What model are you primarily concerned with fixing/creating? How many of these models exist per account will answer this question.

  * include the FanOut module if: you're backfilling a model like Tickets, TicketArchiveStubs(archived tickets), Users, Attachments, Events and friends

  * don't include the FanOut module if you're backfilling something like an account setting, an account subscription, or any other model where the amount of objects is less than 1 or 2 thousand. It's not worth fanning out for those as an AccountJob can do the work inline just fine.




### Model Scoping

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7425852039)*

---

## CDC Ingestion into ZDP via Snowpipe Streaming

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7423689043](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7423689043)  
**Last Updated:** 2025-11-11  

## About this Project

**Summary**|  This is second version of ZDP ingestion pipeline that streams change data capture (CDC) events from Shardded MySQL databases into Zendesk data platform (ZDP). The v1 of the CDC ingestion pipeline is replaced by this pipeline on 28th Aug 2025 AEST.  
---|---  
**Status**|  [Epic Jira](https://zendesk.atlassian.net/browse/PDATGR-630)  
  
## Background

This page describes one of the main data ingestion mechanism for Product Data into ZDP (ZDP overall architecture [diagram](https://lucid.app/lucidchart/6ffabd6c-43c9-4fec-b276-b6bdcb3aa6a2/edit?invitationId=inv_569ebbfa-e2e7-408c-9444-c9118aa9af76&page=cFb3e6BTyU-a#)) based on processing of CDC events generated by the sharded MySQL databases and ingesting those data from Kafka into Snowflake tables. We currently have ingested more than 300 CDC tables into ZDP.

See this [help center article](https://zendeskdev.zendesk.com/hc/en-us/articles/9298271450010-What-are-the-supported-methods-to-ingest-product-data-into-ZDP) for the other supported standard ingestion methods. 

### Why are we doing this?

The v1 CDC ingestion pipeline based off Kafka Connect, S3, EMR and Snowpipe file ingestion has a few drawbacks including

  * Kafka connect was dropping data due to S3 rate limit

  * multiple hops from Kafka to S3 before landing in Snowflake resulting in increased latency and complexity


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7423689043)*

---

## Acryl: Previous Data Catalog Solution

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7422739949](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7422739949)  
**Last Updated:** 2025-08-20  

Before our adoption of Alation, Acryl served as the primary data catalog. Acryl was selected after a thorough proof-of-concept (POC) process, as it initially best fit the organization's limited scope and requirements at the time. The deployment began officially in June 2022 and the data catalog went generally available (GA) by October 2022.

## **Key reasons for initial selection**

  * Acryl was chosen following vendor comparisons and POCs that included Atlan, with Acryl better satisfying criteria for that phase of ZDP's growth.

  * At the time, ZDP's metadata collection needs and data governance complexity were manageable within Acryl's core feature set.




## **Emerging shortcomings and challenges**

As Zendesk's metadata and data governance requirements rapidly expanded--with new metadata standards and more complex roles and responsibility models--Acryl was unable to keep pace:

  * **Insufficient feature coverage:** Out-of-the-box, Acryl could not accommodate the breadth and depth of metadata newly required by the Data Governance Office. Workarounds became necessary to store additional metadata.

  * **Performance and scalability issues:** Integration with more data sources and the data warehouse exposed scalability challenges. Searches in Acryl frequently took over 1-2 minutes, or failed to produce expected results, greatly reducing data discovery efficiency.

  * **Delayed feature delivery:** Critical features, such as support for customized ownership roles, were significantly delayed beyond vendor commitments, indicating development velocity and prioritization concerns.

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7422739949)*

---

## Data Quality integration request: Legacy epic status, unified solution approach, and effort recommendation

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7420805168](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7420805168)  
**Last Updated:** 2025-08-20  

## 1\. Background: Data Quality's requirement

Data Quality requires robust metadata integration between DBT projects and the Data Catalog to support compliance and data quality workflows. The currently available solution is incomplete; existing workstreams do not deliver the reliability or coverage needed for Data Quality operations.

* * *

## 2\. Status of prior epic and incomplete tickets

Under [DATACATALG-1061 Epic - DBT Metadata Manifest Workflow](https://zendesk.atlassian.net/browse/DATACATALG-1061), most work remains at "intake" status:

Ticket| Title| Status  
---|---|---  
DATACATALG-1084| Investigate Optimal Solution/Design| Intake  
DATACATALG-1085| Integrate GitHub Actions| Intake  
DATACATALG-1086| Implement Metadata Validation| Intake  
DATACATALG-1087| Implement Metadata Sync| Intake  
DATACATALG-1089| Add GitHub Action Endpoints| Intake  
DATACATALG-1090| Setup Metadata Sync Scheduler| Intake  
DATACATALG-1093| Generate Metadata Report| Intake  
DATACATALG-1105| SPIKE - Metadata as Code (DBT)| Resolved  

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7420805168)*

---

## 010 - Hidden Fields v1

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7416315992](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7416315992)  
**Last Updated:** 2025-09-15  

**Status**|  In progressYellow  
---|---  
**Impact**|  LowGreen  
**Driver**|   
**Approvers**|   
**Contributors**|  @ contributors  
**Informed**|   
**Due date**|  Type // to add a date  
**Outcome**|  Team Raichu will build v1 of Hidden Fields for the Resolution Based Pricing use case.  
  
##  Relevant data

  * Hidden Ticket Platform Fields Design Doc

  * [Investigation] Different event types for HTPF

  * [https://docs.google.com/document/d/1peYWAIhufSVffFQ465aWXj6B3BhLDwgcM3dl9mEx-80/edit?pli=1&tab=t.0#heading=h.5t0m5b2cqcsu](https://docs.google.com/document/d/1peYWAIhufSVffFQ465aWXj6B3BhLDwgcM3dl9mEx-80/edit?pli=1&tab=t.0#heading=h.5t0m5b2cqcsu)




*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7416315992)*

---

## How to integrate with ZDP account moves?

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7413531702](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7413531702)  
**Last Updated:** 2025-10-05  

# `FOUNDATIONAL.ACCOUNT_MOVES.INSTANCE_ACCOUNT_SHARD_LOCATION` Table

This table provides a comprehensive, real-time view of the current location of Zendesk customer accounts within the Zendesk Data Platform (ZDP). It tracks ongoing and completed account moves, showing which region, shard, and pod an account is currently hosted in. 

**Column Name**| **Data Type**| **Description**  
---|---|---  
INSTANCE_ACCOUNT_ID| Number| Unique identifier for the Zendesk customer account  
INSTANCE_ACCOUNT_NAME| Varchar| Name of the Zendesk customer account  
INSTANCE_ACCOUNT_SUBDOMAIN| Varchar| URL subdomain of the account in the source system  
INSTANCE_ACCOUNT_CREATED_TIMESTAMP| Timestamp_NTZ| Creation time of the Zendesk customer account  
INSTANCE_ACCOUNT_DELETED_TIMESTAMP| Timestamp_NTZ| Deletion time of the Zendesk customer account  
INSTANCE_ACCOUNT_SNOWFLAKE_REGION| Varchar| Name of the Snowflake region where the account currently resides in ZDP  
INSTANCE_ACCOUNT_SHARD_ID| Number| Unique identifier of the account's shard in the source region  
INSTANCE_ACCOUNT_POD_ID| Number| Identifier for the pod where the account is hosted  
LOCATION_LAST_CHANGED_TIMESTAMP| Timestamp_NTZ| Timestamp when Exodus successfully last moved this account.  
ZDP_ACCOUNT_MOVE_IN_PROGRESS| Boolean| Indicates if a ZDP account move is in progress (`TRUE` if moving)  
ZDP_ACCOUNT_MOVE_STATUS| Varchar| Current state of the account move (e.g., `SUCCESSFUL`, `QUEUED`, `RUNNING`), or blank  
ZDP_MOVE_START_TIMESTAMP| Timestamp_NTZ| Timestamp when the ZDP account move began  
ZDP_MOVE_END_TIMESTAMP| Timestamp_NTZ| Timestamp when the ZDP account move completed  
INSTANCE_ACCOUNT_FROM_SNOWFLAKE_REGION| Varchar| Source Snowflake region (from which the account is moving)  

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7413531702)*

---

## Escape v2 Runbook

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/932655657](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/932655657)  
**Last Updated:** 2025-07-16  

# Summary

Escape v2 is a new version of Escape that runs as its own application rather than as part of Maxwell Smarts. Escape allows applications to publish messages to Kafka as part of a database transaction. The message to be published is inserted into a table. Escape then follows the mysql binlog and publishes the messages to Kafka.

As well as the Shards DBs, standalone Aurora MySQL instances are also supported in this new version. 

An instance of the application is deployed for each DB cluster that has been set up. [Read our ADR](https://github.com/zendesk/lizards/tree/master/adrs/binlog-replication-apps-deployment-strategy) for more information on how this works.

See Cerebro for links to dashboard, logs, github: <https://cerebro.zende.sk/projects/escape>

Escape is a Tier 0 service used by many other Products. During an outage to Escape, the topics published by Escape may be delayed. It is hard to quantify the customer impact of these delays, as Escape is agnostic to the topics being published.

# Logs

Escape runs on many different namespaces and the service tag in datadog is tied to the namespace of the service. As such, searching for logs with `service:escape` only finds logs in the `escape` namespace, which are the logs for Escape running on the shard databases.

In order to view logs for all Escape services, search using the `container_name:escape` tag.

# Commands


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/932655657)*

---

## Logging in depth

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/786902338](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/786902338)  
**Last Updated:** 2020-01-15  

_Note: this page deals with logging in  **Sparrow** only._

We currently have many logging sources and locations and it is a bit hard to follow (and to manage!). This page explains most of the aspects of logging in Sparrow.

## S3 Logs

### What is logged?

Logs in S3 contain the logs for each application **before our custom configuration kicks in**. Remember that we perform a custom setup for the logs when we start an application, this is done outside the `log4j.properties` configuration.

  * EMR cluster ID (e.g. `j-10M3OHZCGLILF`)
  * YARN Application ID (e.g. `application_1574164391015_0201`)
  * Container ID (e.g. `container_1574164391015_0202_01_000002`)
  * One file for stderr and one file for stdout.



They do NOT contain most of the logs for the applications, since we store these logs in `/tmp/sparrow.log` rather than in stdout.

### Where are logs stored?

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/786902338)*

---

## Foundation Interface Assessment

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/783847124](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/783847124)  
**Last Updated:** 2021-05-24  

# Preface

We've been tasked to explore possibility to integrate Temporary Auth project Runtime and/or Setup with Foundation Interface and it's components.

In this document we are going:

  * Compare functionality of Temporary Auth Runtime and Existing Solution by Foundation Interface Team
  * Compare functionality of Access Provisioner Operator and Temporary Auth Operator
  * Analyse the ways to integrate with the Foundation Interface



# Temp Auth Runtime and Sidecar offered by Foundation

Components overview

temp auth| vault agent| Functionality| Comments  
---|---|---|---  
temporary auth init container| -| init container to render temporary in the given volume, e.g. /secrets. The idea behind it was to make the solution compatible with samson secret puller, zendesk_config_go packages and etc.Also init container must exit with code 0 before pod deployment can proceed. Having this ensures that secrets are in place when app container starts up.| Temporary auth init container serves two functions:


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/783847124)*

---

## mail-parsing-queue

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/776309159](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/776309159)  
**Last Updated:** 2025-07-16  

# Important Links

Github Repo| [zendesk/zendesk_mail_parsing_queue](https://github.com/zendesk/zendesk_mail_parsing_queue)  
---|---  
Dashboard| [Email ~ Healthchecks (ALL)](https://zendesk.datadoghq.com/dashboard/5qn-wyc-ksm/email-healthchecks-all)  
Logs| `Index: support-mail-processing``Service: mail_conveyor`[Mail Parsing Queue US Datadog Logs](https://zendesk.datadoghq.com/logs?cols=service%2C%40account.id&index=support-mail-processing&messageDisplay=inline&query=service%3Amail_conveyor&stream_sort=desc)[Mail Parsing Queue EU Datadog Logs](https://app.datadoghq.eu/logs?cols=%40resque.job&index=support-mail-processing&messageDisplay=inline&query=service%3Amail_conveyor&stream_sort=time%2Casc)  
Rollbar| [Mail Parsing Queue US Rollbar](https://rollbar-us.zendesk.com/Zendesk/Mail-Parsing-Queue/)[Mail Parsing Queue EU Rollbar](https://rollbar-eu.zendesk.com/Zendesk/Mail-Parsing-Queue/)  
APM| [mail-parsing-queue-active-record](https://zendesk.datadoghq.com/apm/service/mail-parsing-queue-active-record/mysql2.query?hostGroup=%2A&start=1623407097067&end=1623410697067&paused=false&env=production)[mail-parsing-queue-mysql](https://zendesk.datadoghq.com/apm/service/mail-parsing-queue-mysql/mysql2.query?hostGroup=%2A&start=1623407097067&end=1623410697067&paused=false&env=production)  
Cerebro| [Mail Parsing Queue](https://cerebro.zende.sk/projects/mail-parsing-queue)  
Runbook(s)| Postfix Runbooks  
  
# Description

Mail Parsing Queue (MPQ) is a Ruby application that uploads email attachments to S3 and converts (and uploads) emails into JSON documents ready for further processing by Mail Ticket Creator (MTC), to ultimately be used to create and update Support tickets.

Internally, MPQ uses the [Adrian gem](https://github.com/zendesk/adrian) to watch a directory for inbound email files (.eml) that need to be processed. Built into MPQ is the following:

  1. Blocking individual emails via banned message IDs, Arturos, invalid/missing Reply-To, etc.

  2. Striping of unwanted HTML such as Pre-header spans.

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/776309159)*

---

## Pod validation

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/774603106](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/774603106)  
**Last Updated:** 2021-10-15  

As Explore is separate from the POD infrastructure, a POD validation is a matter of verifying correct connectivity and setup. Explore need: 

  * various services being deployed and functional in the new pod.

  * credentials and connectivity to this various services to be correct. 

  * Explore being reachable from the new pod.




As Explore is evolving, the scope of Pod validation for Explore need to be assess for each new pod. 

As for organising Explore Pod validation, the <https://zendesk.atlassian.net/browse/EXPODY-574> is an example of this task. 

### Account creations

Accounts in Zendesk belong to a given Pod. To be able to verify Explore is working for a new Pod, accounts in the targeted Pod are needed. Some test accounts belonging to the targeted Pod will be made available, this information should be available in the related slack channel. 

If you need to create your own accounts, please read :Creating Account via form: Production, Staging & Acceptance

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/774603106)*

---

## S3v1 Final Battle

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7581015773](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7581015773)  
**Last Updated:** 2025-11-16  

Remaining services that have an Objectstore deployed

**Service**| **Status**| **Env**| **Empty**| **Action**  
---|---|---|---|---  
account-write-warden| Orphaned| Staging| N/A| Delete  
agent-graph| Orphaned| Staging + Prod (pod26)|  | Delete  
b-team-test-app| Test bucket| Staging + Prod| N/A| Delete  
beagle-example-ml-service| Orphaned| Staging| N/A| Delete  
classic-operations-data-pipeline| Orphaned| Staging| N/A| Delete  
data-deletion-data-pipeline| [Active](https://github.com/zendesk/data-deletion-data-pipeline/blob/main/service.yml#L5-L21)| Staging + Prod (pod13, 18, 25, 26)|  | Delete (permission [granted](https://zendesk.slack.com/archives/C08B8NSJ6H0/p1763042717857799?thread_ts=1762925522.376529&cid=C08B8NSJ6H0))  
data-mover-test-app| Test bucket| Staging| N/A| Delete  
explore-data-pipeline| Orphaned| Staging| N/A| Delete  
gecko-test-participants| Test bucket| Staging| N/A| Delete  
ml-training-pipelines| Orphaned| Staging| N/A| Delete  
monitor-micro-frontends| Buggged (`objectstore` exists but no `s3` CR or bucket)| Production (pod19)| N/A| Delete  
nps| Orphaned| Staging| N/A| Delete  
sell-calendars-integrator| [Active](https://github.com/zendesk/sell-calendars-integrator/blob/master/service.yml#L29-L36)| Staging + Prod (sell-dmz-production)|  | **Reach Out**  
sentiment-ml-service| Orphaned| Staging | N/A| Delete  
support-search-data-pipeline| Orphaned| Staging| N/A| Delete  
z2-sunco-widget| Orphaned| Staging + Prod (pod26)|  | Delete

---

## Spike: A catchup job to fetch the missed metadata

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7575372024](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7575372024)  
**Last Updated:** 2025-11-10  

## Overview  
  
The current system has three sequential jobs that perform a full data pull:

  * `pulltablefromalation` \- Fetches all tables and stores them in S3

  * `pullcolumnlineagefromalation` \- Fetches columns and lineage metadata from table data

  * `populatedatacatalogdb` \- Loads all fetched data into the database




This is currently populated on staging and prduction but next we are going to: 

  * Nuke the ZDM datacatalog database on Thursday 12th November 2025 and do a fresh Alation dump

  * Use the up-to-date datacatalog DB to raise the DBT PRs for each repo.

  * Lets assume DBT repos will take 2-3 weeks to review and merge the PRs and then we will cut-off Alation write access. After this step we wont be able to delete or truncate the datacatalog DB tables.

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7575372024)*

---

## Solution Options for Frontend Instrumentation

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7572095213](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7572095213)  
**Last Updated:** 2025-11-11  

none

# Options

## Options A - Single raw events table per role (agents/admins/end user)

This is the high level proposed option for this ([Lucid](https://lucid.app/lucidchart/522d4b70-f620-408b-a507-f6db76746ec3/edit?invitationId=inv_3807e9d9-d5b2-4905-ae05-f8e7ab67b497&page=0_0#))

1trueleftrich153580a5d-d28a-45f9-b502-966eb2a1e6b5Confluence:2083817226700v2_8ebfac4da9db11d4adfcdb09f68bdbd4cef472158ab027bcba59726e2521c5ee-a=103589275&c=Confluence%3A2083817226&d=522d4b70-f620-408b-a507-f6db76746ec3&p=7555056803522d4b70-f620-408b-a507-f6db76746ec31762155410272500

#### **High level how it works**

**Browser to Kafka Ingestion**

  * frontend clients to include a shared JS library in UIs (Lotus/Support, Admin Center, Guide, etc.)

  * The browser will send frontend events to new POST endpoints using the shared javascript library (batches of events supported)

    * admin/agent: `/frontendevents/staff/user_activity` should be **authenticated**


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7572095213)*

---

## Detect Derivable relationships

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7555056685](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7555056685)  
**Last Updated:** 2025-10-28  

## Introduction  
  
After importing metadata from Alation, we have an opportunity to **optimize our metadata management strategy** by distinguishing between **explicitly set** and **implicitly derived** security classifications and sensitivities.

Currently, all metadata imported from Alation is marked as explicit, even when it can be automatically derived from upstream lineage. This creates unnecessary maintenance burden and potential inconsistencies when upstream classifications change.

## The Problem

When data flows through transformation pipelines (e.g., `RAW -> FORMATTED`), security classifications and sensitivities are often **propagated unchanged** through lineage relationships. For example:

  * A column in `FORMATTED.SCHEMA.TABLE` with `EXACT_COPY` relationship to `RAW.SCHEMA.TABLE` should inherit the same security classification

  * If both tables currently show `L2` classification and `PII` sensitivity, only the source (RAW layer) should be marked as **explicit**

  * The downstream table (FORMATTED layer) should be marked as **implicit** since it derives from upstream




However, after Alation import, **both are marked as explicit** , making it harder to:

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7555056685)*

---

## 2025-10-15 Foundation Data meets Edge on LDL EOL

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7538180365](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7538180365)  
**Last Updated:** 2025-10-15  

Present

# Minutes

  * Walked through managed data pipeline

  * Current plan: <https://docs.google.com/document/d/1qz89wbn9ultMEyY9-drcINCLjPf4FNaHdA-Y4naxExs/edit?tab=t.0>

    * Seen as too much effort

    * Don't need an entire service

  * New plan

    * Do the transforms in DBT in Snowflake

    * Write the new data to a new S3 bucket (with reverse ETL)

    * Alter classic to connect via External to new data source and read data


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7538180365)*

---

## Cleansed Models Account Move Integration Guide

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7495188554](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7495188554)  
**Last Updated:** 2025-09-29  

This guide is for teams creating regional tables in `cleansed` layers. The SQL models remain unchanged; enablement is done via dbt_project.yml configuration.

## Background: The account move problem in ZDP

When an account moves regions (e.g., AMER to EMEA), data must migrate without duplications, gaps, or historical overrides. Projects need to integrate with the Account Move filtering v2 solution because the earlier approach only copied formatted tables, whereas the new approach also migrates historical data. During an account move, running transformations on that account can introduce inconsistencies. To prevent this, we defer transformations until the account's full history has been copied to the target destination; accounts in transit are temporarily excluded from model transformations. This behaviour is handled by macros in the zdp_dbt_utils repository, which projects can now enable in pre-production environments.

Cleansed handles this using project-level configuration and hooks, not relying heavily on model SQL changes. However there are fields that need to be additionally passed to the `build_ `macros to ensure they use/not use the new filters as appropriate.

## Solution overview for cleansed

  * Enable account-move handling via:

    * Config changes:

      * A runtime control flag to opt-in by environment.

      * Pre- and post-hooks that manage buffer offsets for safe, consistent processing during region moves.

    * SQL changes


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7495188554)*

---

## Optimization runbook - TICKET_FIELDS_STRING Filtered tables

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7487914141](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7487914141)  
**Last Updated:** 2025-10-23  

**Runbook Status**|  IN PROGRESS  
---|---  
**Owner**(benchmark conducted by)|   
**Related documents**| <https://docs.google.com/document/d/1Q6_B8bJ0KjD_XEzgScXEvVcDUzuisV5Io7-3-S87jZw/edit?tab=t.0#heading=h.t1raf4bmuc57> Improving performance by utilizing filtered tables  
  
Statuses: IN PROGRESS / FINALIZEDGreen / CANCELLEDRed

none

# What: The **Optimisations purpose**

There are two tables commonly causing performance issues namely: **ticket_field_strings** and **ticket_field_changes**. These tables are very large, and joins involving them take a significant amount of time.  
The problem can be solved by replacing joins to the entire tables with joins to a filtered table specifically defined on the most frequently used `field_names` or `custom_fields_ids`. These tables are much smaller and leverage corresponding indexes that PostgreSQL ignores when scanning the entire tables.

This approach is much more efficient than joining to the full tables. This optimisation focuses on **ticket_field_strings**. See also:Improving performance by utilizing filtered tables

# When**: When to use this Optimisation**

This optimisation can be utilised when joins to the`ticket_fields_string` contains explicit comparisons on `ticket_fields_string.custom_field_id`. 


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7487914141)*

---

## Optimization runbook - TICKET_FIELD_CHANGES Filtered tables

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7485095960](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7485095960)  
**Last Updated:** 2025-11-13  

**Runbook Status**|  IN PROGRESS  
---|---  
**Owner**(benchmark conducted by)|   
**Related documents**| <https://docs.google.com/document/d/1Q6_B8bJ0KjD_XEzgScXEvVcDUzuisV5Io7-3-S87jZw/edit?tab=t.0#heading=h.t1raf4bmuc57> Improving performance by utilizing filtered tables  
  
Statuses: IN PROGRESS / FINALIZEDGreen / CANCELLEDRed

none

# What: The **Optimisations purpose**

There are two tables commonly causing performance issues namely: **ticket_field_strings** and **ticket_field_changes**. These tables are very large, and joins involving them take a significant amount of time.  
The problem can be solved by replacing joins to the entire tables with joins to a filtered table specifically defined on the most frequently used `field_names` or `custom_fields_ids`. These tables are much smaller and leverage corresponding indexes that PostgreSQL ignores when scanning the entire tables.

This approach is much more efficient than joining to the full tables. This optimisation focuses on **ticket_field_changes**. See also:Improving performance by utilizing filtered tables

# When**: When to use this Optimisation**

This optimisation can be utilised when the calculated parts of the query involving `ticket_field_changes` contain explicit comparisons on `ticket_field_changes.field_name`. These comparisons can be either:


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7485095960)*

---

## Support S3V2 External in ZDM

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7448953654](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7448953654)  
**Last Updated:** 2025-09-03  

Important Information

## About this Project

**Epic Owner**|   
---|---  
**Epics**|  Epic SSD-4015cae89f0e-c846-3d65-88a5-bb277a2031b3System Jira  
**Metrics**| 

  * How many customers start using ZDM to track s3v2 external ?
  * How many shared/external buckets are getting managed by ZDM ?

  
**Abbreviations**|   
  
## In Brief

Provides a way to manage S3V2 External buckets provisioned through self service datastore procedure in ZDM

none

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7448953654)*

---

## Support SQS External in ZDM

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7448953644](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7448953644)  
**Last Updated:** 2025-09-03  

Important Information

## About this Project

**Epic Owner**|   
---|---  
**Epics**|  Epic SSD-4015cae89f0e-c846-3d65-88a5-bb277a2031b3System Jira  
**Metrics**| 

  * How many customers start using ZDM to track SQS External ?
  * How many shared/external queues are getting managed by ZDM ?

  
**Abbreviations**|   
  
## In Brief

Provides a way to manage SQS External queues provisioned through self service datastore procedure in ZDM

none

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7448953644)*

---

## [2025 August] CDC Snowpipe Streaming Post Release Cost Review

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7418019879](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7418019879)  
**Last Updated:** 2025-09-01  

## Context

We have migrated the CDC ingestion pipeline from the old [S3/EMR/Snowpipe file based pipeline](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/5880874518/ARCHIVED+CDC+Binlog+Processor?atl_f=PAGETREE) to [Snowpipe streaming](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7423689043/CDC+Ingestion+into+ZDP+via+Snowpipe+Streaming?atl_f=PAGETREE).

This page documents the changes in cost observed 4 days post cutover to the new pipeline. 

## Summary

Based on the cost data since switchover to the new CDC pipeline, we observed that

  * CDC ingestion cost for 364 tables is reduced by **60%** from a monthly cost of $75.5k down to $30.3k. 

  * this is equivalent to an estimated **$542k/year** savings

  * most of the cost savings stems from the expensive cost of snowpipe file used in the old pipeline as it was costing close to **$50k/month**. In comparison snowpipe streaming cost is much cheaper




## Costs Comparison

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7418019879)*

---

## Alation Analytics ETL

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7416545558](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7416545558)  
**Last Updated:** 2025-08-18  

Alation docs on ETL can be found [here](https://www.alation.com/docs/en/latest/installconfig/AlationAnalyticsV2/AlationAnalyticsV2ETL.html).  
  
**Our ETL job is setup to run every 3 hours UTC time.**

### 1\. **Purpose & Initialization**

  * ETL extracts data from Alation's internal database (Rosemeta) and loads it into the Alation Analytics V2 database. This is the foundation for usage analytics. [Alation](https://www.alation.com/docs/en/latest/installconfig/AlationAnalyticsV2/AlationAnalyticsV2ETL.html?utm_source=chatgpt.com)

  * Upon initial setup, the V2 database is empty and is populated via the first ETL job. Afterwards, ETL runs incrementally. [Alation](https://www.alation.com/docs/en/latest/installconfig/AlationAnalyticsV2/AlationAnalyticsV2ETL.html?utm_source=chatgpt.com)




### 2\. **Scheduling & Incremental Behavior**

  * By default, the ETL runs daily at **10:59 AM** , covering the previous **180 days** of data. [Alation](https://www.alation.com/docs/en/latest/installconfig/AlationAnalyticsV2/AlationAnalyticsV2ETL.html?utm_source=chatgpt.com)

  * The initial load begins from the earliest user creation date and may take longer. Subsequent ETL runs only process new data since the last run. [Alation](https://www.alation.com/docs/en/latest/installconfig/AlationAnalyticsV2/AlationAnalyticsV2ETL.html?utm_source=chatgpt.com)



*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7416545558)*

---

## Re: Supercharge Setup Phase 1 - RFC

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7408746583](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7408746583)  
**Last Updated:** 2025-08-14  

**Inbound Pipeline:**  
The email connector fetches emails from the Inbox folder, parses them, and creates or updates tickets based on the email data, such as headers. In summary:

  * It checks the From header and uses it to look for an existing end user on the client account, or creates a new end user for the customer account if necessary.

  * It checks the To header to find the recipient address (which should be a configured support address).

  * This pipeline is specifically designed to process emails from the Inbox folder.




**Why can 't we process emails from the Sent folder through the inbound pipeline?**

  * The From header contains the support email address configured by the customer. Our system will attempt to create an end user for this address, but it already exists as a support email address, leading to a conflict (support addresses cannot be used as end-user addresses).

  * The To header contains the end-user address, which isn't configured as a support address, so we will fail to match it in our recipient address table.

  * One might suggest detecting this situation and swapping the addresses. However, this creates another issue: while ticket comments would be created correctly, using the support address as the sender would trigger the outbound pipeline described above, causing the email to be sent again--something we definitely don't want.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7408746583)*

---

## CDC Snowpipe Streaming Cutover Procedure

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7387217921](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7387217921)  
**Last Updated:** 2025-08-20  

none

This document outlines a procedure for cutting over the ingestion of CDC data from the EMR pipeline to the new Snowpipe Streaming pipeline.

## 1\. Preflight checks

1| If cutting over in production, has the pipeline first been cutover and verified in staging? This should include checking the CDC Compatibility Validation metrics on the [DataDog dashboard](https://zendesk.datadoghq.com/dashboard/g6t-hjs-r43/draft-zdp-kafka-snowpipe-streaming-ingester?fromUser=false&refresh_mode=paused&tpl_var_env%5B0%5D=staging&tpl_var_kube_role%5B0%5D=formatted-*&from_ts=1754361030662&to_ts=1754364630662&live=false&tile_focus=3548470970383806) to ensure that there are no errors or mismatches. If there are any errors check out the logs to see what they are: [CDC Compatibility check logs](https://zendesk.datadoghq.com/logs?query=service%3Azdp-kafka-snowpipe-streaming%20container_name%3Acdc-compatibility-check-worker%20-status%3Ainfo&agg_m=count&agg_m_source=base&agg_t=count&cols=host%2Cservice%2Cpod&index=foundation&messageDisplay=inline&refresh_mode=sliding&storage=hot&stream_sort=desc&viz=stream&from_ts=1755540929773&to_ts=1755562529773&live=true)  
---|---  
2| Are **dependent teams aware **that we are making this change? Can they verify the CDC tables after we cutover? Are they aware this process **will pause ingestion for between 2-3 hours**? In particular, we should share with them some of the **expected changes to the** `FORMATTED` **layer** following the release:Changes to Formatted layer for CDC datasets with Snowpipe Streaming release  
3| Notify the [#snowpetrels-team](https://zendesk.enterprise.slack.com/archives/C07DRPV1D8T) that we're starting the migration of the dataset topic, as they may need to adjust their Snowpipe monitoring accordingly  
4| Ensure there is no data in the `ZDP.CDC_INGESTION_OPS.MAXWELL` table and there are no offsets in the channel for that table:sql  
  
## 2\. Cutover the dataset

### 2.1 Stop ingesting the data on the cdc-binlog-processor

The steps outlined in this section will stop the `kafka-connector` for ZDP from writing the dataset messages to the L0 S3 bucket in a specified environment. This effectively halts processing of the dataset via the existing EMR/Snowpipe pipeline.

1| Create a PR that disables ZDP output for the appropriate environment by setting the `ENABLE_ZDP_OUTPUT` environment variable to `FALSE`:  
<https://github.com/zendesk/kafka_connectors/blob/1d953da3d49a49f963201ad6c6fb4eaa20b3c4c7/cicd-toolkit/kubernetes/resources/kafka-connectors.jsonnet#L27>  

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7387217921)*

---

## Snowpipe Streaming Escalated Response

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7379189816](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7379189816)  
**Last Updated:** 2025-10-06  

none  
  
# Snowpipe Streaming

The following section outlines some more advanced topics related to diagnosing the Snowpipe Streaming ingestion pipeline.

## Check lag for CDC 

Query to check to see if Maxwell table is lagging (update the `zdp_meta_eff_ts` condition to see how far back you want to check the lag for)

wide760

Query to check to see if formatted tables are lagging. Change the max_lookback_minutes variable if you want to query older data. Update the table name `SNOWPIPE_STREAMING_TEST.SHARDDB.TICKETS` , `$source_schema` and `$source_table` to match the formatted table that you want to check on

wide760

## Check data completeness for CDC 

Query to check data completeness in Maxwell table. Note currently we are seeing some gaps as the app is filtering out the DDL events and only send the DML events to the Maxwell table. So this may not mean real drop of data.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7379189816)*

---

## Sparrow Job Overview

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7342293564](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7342293564)  
**Last Updated:** 2025-07-17  

Sparrow Job leverages Spark under the hood.  
Spark cluster is being run in kubernetes in `zendesk-spark-operator` namespace.  
there are 4 types of pods:

  * the `spark-history-server` which is responsible for hosting the spark-history-server of all pipelines

  * `spark-operator` its a k8s operator for spark responsible for orchestrating and managing the lifecycle of the spark jobs

  * The `{pipeline-id}-driver` pod

  * `sparkdag-{pipeline-id}-exec` executor pods




All ETL logic runs across both the driver and executor pods.  
The driver pod acts as the **brain** of the Spark application, coordinating the execution by scheduling and delegating computational tasks to the executor pods (such as aggregations, joins, etc.).  
The executors perform the heavy lifting of processing data in parallel. Results from executors are sent back to the driver, which can then write the data to a datastore, log results, or perform any further actions.

# Brief overview of the Sparrow lifecycle

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7342293564)*

---

## Migrating Monitor off Legacy Data Lake buckets

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7338590563](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7338590563)  
**Last Updated:** 2025-07-24  

Monitor lets people do admin stuff to zendesk accounts. 

# What does it do right now?

The current flow is:

  * These tables are ingested via CDC

    * These tables are then transformed to create the foundational tables needed

  * Push account mappings data to S3

    * <https://github.com/zendesk/zendesk_monitor/blob/master/app/jobs/legacy_data_lake.rb#L5-L7>

    * It doesn't seem this data is being used in ZDP, only legacy data lake.

    * This is using the compliance_baa_accounts table in the accountsDB, which is already present in [snowflake](https://app.snowflake.com/zendesk/amer/#/data/databases/FORMATTED/schemas/ACCOUNTSDB/table/COMPLIANCE_BAA_ACCOUNTS)

  * Join the data using a DBT job 


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7338590563)*

---

## ZDP Compliance - Account Moves

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7336427654](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7336427654)  
**Last Updated:** 2025-09-07  

# Problem Statement

Zendesk provides data locality features, enabling customers to host their data in specific regions such as AMER, EMEA, or APAC. When a customer purchases this feature and requests a move to another region, we are responsible for relocating all associated customer data to the requested region.

On the application side, account moves are orchestrated by Exodus and involve physical data migration through service-specific movers (e.g., S3 mover, MySQL mover). Beyond cross-region moves, Zendesk also performs shard rebalancing within pod for load distribution, which are opaque to customers and do not impact service availability.

Within the Zendesk Data Platform (ZDP), which hosts historical data and analytical data in Snowflake regional accounts, we must ensure that account moves are accurately reflected without data loss or duplication. While within region moves do not require data relocation for ZDP, cross-region moves introduce significant complexities related to historical data, aggregations, and denormalized wide tables that must be addressed to maintain data integrity and compliance.

# Challenges that are unique to ZDP

  * ZDP will retain historical data, data volume will increase as an account will age and will have more adoption. 

  * Data is organised in different layers to enable easy consumption, and to support analytics/reporting in the form of trend analysis, training machine learning models, and insights generation for both internal and external customer facing use cases.

    * Different data layers store data in aggregated, chronological, and denormalised forms to enable querying in a cost effective and performant way.

  * To organise data in different layers, processing jobs are executed on a required schedule daily (internal reporting), and hourly (customer facing). Running these jobs on schedule provides us a mechanism to balance cost with the value generated. 

    * Pausing these jobs beyond a certain time duration will either translate into bad customer experience or will increase overall cost to process data and catchup.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7336427654)*

---

## Ongoing Maintenance

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7335018647](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7335018647)  
**Last Updated:** 2025-08-07  

none

# Purpose

The purpose of this document is to identify and summarise all ongoing work required to maintain the current data catalog and lineage solution. This includes processes, communication channels, monitoring, backend tasks, and support routines to ensure operational effectiveness and reliability.

# Communication Channels

## Slack Channels

###  [ask-alation-data-catalog](https://zendesk.enterprise.slack.com/archives/C06KBKNRTST)

**Purpose** : This channel is for questions, announcements and links related to Zendesk's Data Catalog tooling (Alation).

**# of members** : 164

**Level of Activity:** Moderate to high -- multiple active threads and replies in just the last week; overall ongoing daily usage.

**Topics:** Common topics include help requests about table/data access issues, troubleshooting integration errors, field/dataset updates, permissions, usage tips, feature walkthroughs, and sharing solutions and best practices.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7335018647)*

---

## TM-Spinnaker Plugin Integration for CS teams

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7323189458](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7323189458)  
**Last Updated:** 2025-11-12  

Epic: CSQT-1679cae89f0e-c846-3d65-88a5-bb277a2031b3System Jira

TM-Spinnaker Plugin Doc: <https://tm.zende.sk/docs/v0.11/tutorial/spinnaker/spinnaker-cicd/>

Spinnaker UI: [https://spinnaker.zende.sk](https://spinnaker.zende.sk/#/search)

# Overview

We would like to setup all Core Services ~~\+ Online Business (billing)~~ teams on CICD Toolkit to leverage the TM-Spinnaker plugin to control which smoke + regression jobs run on deploys. This will involve:

  * Investigating which smoke + regression jobs run currently on deploys so we know which jobs to we need to ensure will run on deploys for each team

  * Carry out TM Spinnaker plugin integration for all codebases listed below for both smoke + regression jobs

  * Dismantling any instances of the custom `withRegressionJob()` jsonnet function ([example](https://github.com/zendesk/advanced-encryption-service/pull/894)).

  * Removing manually added smoke jobs, `postDeployJenkinsJobs`

  * Configuring Spinnaker to use TM


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7323189458)*

---

## System Overview

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7319717328](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7319717328)  
**Last Updated:** 2025-08-19  

none  
  
## Overview

Zendesk's data catalog is built on Alation and consists of three main automation repositories that work together to maintain metadata consistency across our data infrastructure:

  * [**data-catalog-ingestion**](https://github.com/zendesk/data-catalog-ingestion) \- Ingests metadata from source systems into Alation

  * [**catalog-metadata-collection**](https://github.com/zendesk/catalog-metadata-collection) \- Propagates and maintains metadata within Alation

  * [**catalog-schema-ingestion**](https://github.com/zendesk/catalog-schema-ingestion) \- API that is invoked by dbt repos for uploading the manifest files to s3 buckets.  





## Useful Links

  * [Help Center Docs](https://zendeskdev.zendesk.com/hc/en-us/sections/8118312429338-Data-Catalog)


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7319717328)*

---

## Support SQS on ZDM

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7285801845](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7285801845)  
**Last Updated:** 2025-06-26  

Important Information

## About this Project

**Epic Owner**|   
---|---  
**Epics**|  Epic SSD-3799cae89f0e-c846-3d65-88a5-bb277a2031b3System Jira  
**Metrics**| 

  * How many customers start using ZDM to track sqs ?
  * How many queues are getting managed by ZDM ?

  
**Abbreviations**|   
  
## In Brief

Provides a way to manage SQS queues provisioned through self service datastore procedure in ZDM

none

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7285801845)*

---

## 2025-05-20 Edge and Wollemi

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7210303489](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7210303489)  
**Last Updated:** 2025-05-25  

# Present

# Minutes

  * Two MPD workflows that are in use

    * API Gateway log processing

      * The stats produced from this process are no longer needed

      * We can deprecate this flow.

    * Account Stats Data Pipeline

      * Sends data back to S3v2 which is read by classic

      * A great candidate for reverse ETL

      * Several rows per account, so, likely around 600,000 lines of data updated daily.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7210303489)*

---

## Snowflake Row Metadata Feature to Replace Ingest Timestamp

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7196672143](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7196672143)  
**Last Updated:** 2025-05-28  

## Introduction

Currently with PDA [snowpipe streaming ](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-overview)pipeline, we don't have a way to get Snowflake to automatically set the insertion/update time when a row is added to the Formatted table. This is due to the lack of row metadata timestamp field which is available for [snowpipe file based method](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-intro). 

This means that we need to run additional Snowflake tasks to set the `zdp_meta_l1_ingest_ts` timestamp field after rows has been inserted. This resulted in additional Snowflake compute costs to support this which is estimated to cost more than 200k USD per year. 

To mitigate this use case, Snowflake has a [private preview feature to provide the row timestamp ](https://docs.snowflake.com/en/LIMITEDACCESS/row-timestamp)metadata information automatically. This page describes a timebox-ed short spike to evaluate the suitability of this feature for this.

Note at the time of writing (19th May 2025), Snowflake is unable to enable private preview feature for production account, this test is only conducted against Snowflake dev and staging. Hence proper testing and evaluation against production account is required once Snowflake make this available.

**Snowflake row timestamp**

This timestamp field is automatically added as `METADATA$ROW_LAST_COMMIT_TIME`as an additional column for all rows in the table. This column shows the time when a row is inserted or updated.

For rows that already exist in a table before this feature is enabled, this column will have value set to `null`. It is not possible to manually update the value of this column.

## Summary

  * Tested that the feature works as expected in terms of setting the last commit time on row in DEV and Staging set on a new column `METADATA$ROW_LAST_COMMIT_TIME` that represent the time a record is inserted or updated.


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7196672143)*

---

## Snowflake: Security Data Lake

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7156564013](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7156564013)  
**Last Updated:** 2025-05-13  

The TPE team is looking to ingest secure log data into Snowflake. This document aims to summarise their requirements and our decisions from an infrastructure / snowflake management perspective.

[Ref for self service snowflake access](https://zendeskdev.zendesk.com/hc/en-us/articles/7422547402138-How-do-I-provision-service-access-to-Snowflake)

# Security requirements

Their RFC is [here](https://docs.google.com/document/d/1cHaVY8HJAMXPzFPz457XXsMJmNoOxUrvM-KYxKsUbD4/edit?tab=t.0).

The takeaway section from the above RFC for the purpose of this document is:

> **Access Control and Isolation**
> 
> We have considered several ways to control access to our security data. We outlined a few security requirements that we have and that was an important factor of this decision.
> 
> The TPE team should have full access to the data, and Snowflake objects used to store or process it.
> 
> The Security Analytics tool must be able to access data in a dedicated database. It needs to be able to create new Snowflake objects (streams, tasks) and modify them.
> 
> Only the TPE team should have access to the data (access for Snowflake admins, maintainers, and engineers that must have access to the data is permitted)
> 

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7156564013)*

---

## Re: Managed Data Pipeline Tasks

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7143948789](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7143948789)  
**Last Updated:** 2025-04-29  

This pipeline is used for validating Rich Ticket in ZDP.

The pipeline will flatten the Rich Tickets generated from Legacy Data Lake, and we will copy this to ZDP so we can validate against Rich Ticket generated in ZDP.

---

## Managed Data Pipeline Tasks

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7126450521](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7126450521)  
**Last Updated:** 2025-10-23  

# Introduction

The Managed Data Pipeline is a deprecated project to allow easy running of spark queries, Athena queries, AWS Batch and other machine learning tasks: 

  * A project can have many pipelines and each pipeline runs tasks one after the other

  * It knows which pipeline configs to run by examining the `pipeline_deployments.json` file

  * This [github search](https://github.com/search?q=org%3Azendesk+pipeline-deployments.json&type=code&p=1) finds all MDP repos

  * <https://github.com/zendesk/data-pipeline-guide/blob/master/reference/pipeline-steps/latest/README.md> \- Details of the Architecture

  * <https://github.com/zendesk/data-pipeline-guide/blob/master/reference/pipeline-steps/latest/pipeline-steps.md> \- Possible operations that a pipeline can perform

  * [Cost Explorer Report](https://us-east-1.console.aws.amazon.com/costmanagement/home?region=ap-southeast-2#/cost-explorer?chartStyle=STACK&costAggregate=unBlendedCost&endDate=2025-03-31&excludeForecasting=false&filter=%5B%7B%22dimension%22:%7B%22id%22:%22Service%22,%22displayValue%22:%22Service%22%7D,%22operator%22:%22INCLUDES%22,%22values%22:%5B%7B%22value%22:%22EC2%20Usage%22,%22displayValue%22:%22EC2%20Usage%22%7D,%7B%22value%22:%22Amazon%20Elastic%20MapReduce%22,%22displayValue%22:%22Elastic%20MapReduce%22%7D%5D%7D,%7B%22dimension%22:%7B%22id%22:%22LinkedAccount%22,%22displayValue%22:%22Linked%20account%22%7D,%22operator%22:%22INCLUDES%22,%22values%22:%5B%7B%22value%22:%22114712639188%22,%22displayValue%22:%22zendesk-production%20\(114712639188\)%22%7D%5D%7D,%7B%22dimension%22:%7B%22id%22:%22TagKey%22,%22displayValue%22:%22Tag%22%7D,%22operator%22:%22INCLUDES%22,%22values%22:%5B%7B%22value%22:%22DataPipeline%22,%22displayValue%22:%22DataPipeline%22%7D%5D,%22growableValue%22:%7B%22value%22:%22ClusterTag%22,%22displayValue%22:%22ClusterTag%22%7D%7D%5D&futureRelativeRange=CUSTOM&granularity=Monthly&groupBy=%5B%22TagKeyValue:Hostgroup%22%5D&historicalRelativeRange=LAST_6_MONTHS&isDefault=true&reportName=Managed%20Data%20Pipeline%20Costs&showOnlyUncategorized=false&showOnlyUntagged=false&startDate=2024-10-01&usageAggregate=undefined&useNormalizedUnits=false) \- Breakdown of map reduce in these pipelines (This does not include athena query costs)




## Observations

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7126450521)*

---

## Writing a PDA Compliant ZDP Pipeline in Classic

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7126253613](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7126253613)  
**Last Updated:** 2025-05-07  

If you own an entity that needs to be accessible in ZDP, you will (likely) need to build a PDA complaint pipeline to ZDP. 

High Level Context on PDA Compliant ZDP Pipelines  
  
The ZAP and ZDP teams have put together a tremendous lot of really good documentation on how to build this type of pipeline. As a Classic engineer, I found there was still Classic relevant context that I needed. Ive now built 3 PDA Compliant ZDP Pipelines and want to share what Ive learned.  


###   
ZAP/ZDP Docs

  * [How to Create and Publish PDA compliant data to Kafka](https://zendeskdev.zendesk.com/hc/en-us/articles/6558614723610-How-do-I-create-and-publish-Platform-Data-Architecture-PDA-compliant-data-to-Kafka)

  * Onboarding data into Zendesk Data Platform (ZDP)




### Step 1 - Create your Data Schema

#### Basic Instructions  

*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7126253613)*

---

## 2025-05-23: Dev environment vulnerabilities in the OpEx dashboard

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7123959990](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7123959990)  
**Last Updated:** 2025-04-22  

Post by Koen Hendrix

We heard a lot of feedback from engineers that the inclusion of vulnerabilities from Dev environments (Scooter and ZDI) was causing a lot of extra work and stress by marking down teams for vulnerabilities that were often out of their control.

The Engineering Productivity team applied for an exception for vulnerabilities coming from these environments, and this has been approved. Right now, we are working on applying this exception in our data pipelines, so that these vulnerabilities will no longer show up in your teams' OpEx Dashboards.

**As of last week, we have excluded vulnerabilities from ZDI, and we are working on doing the same for those from Scooter.** This is a bit more complicated, but we hope to have a solution very soon.

Thanks for all the feedback about the SPR and vuln management processes. We hear you. You're always welcome to reach out to #vuln-mgt or DMing me if you have more feedback.

Some Q&A that might pop up:  
**Is it safe to apply such a broad exception for vulnerabilities?**  
In an ideal world, there are no security vulnerabilities, or at least security vulnerabilities are patched almost immediately. In the actual world, we all have limited people and time, and need to prioritise our work. The Security team is satisfied that the risk presented by Dev environment vulnerabilities is currently not on top of the priority list.

**Will this exception last forever?**  
Nothing lasts forever, the same is true here. This exception has to be reviewed biannually, and currently lasts until Q3 2023. At that stage, it will be reviewed, and either ended or renewed.

**What should I do about exceptions that are still visible?**  
Please do not feel obligated to work on vulnerabilities coming from your team's Scooter environments. We are working on excluding these from the dashboard now. This will take some more time though. 


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7123959990)*

---

## [2025 April]  PDA Snowpipe Streaming First Release Cost Review

**Source:** [https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7112491067](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7112491067)  
**Last Updated:** 2025-08-19  

## Context

We have migrated ingestion of PDA datasets into Snowflake (ZDP) from EMR based pipeline to Snowpipe streaming in March 2025. It has been nearly a month that the new pipeline is running in production. Hence it is a good time to review and compare the cloud cost between the old and new pipeline.

**Old pipeline**

1falseleftrich1ad1a855a-a9c0-4b56-9e2f-f1665e2eb1feConfluence:2083817226700v2_36423f1225b9a68268fd86c6cbdad7a862168534a31b1db4d8e2198bc9855a63-a=103589275&c=Confluence%3A2083817226&d=8081075a-4d00-4271-9cf2-be38659d2437&p=71124910678081075a-4d00-4271-9cf2-be38659d24371744861752049500

**New snowpipe streaming pipeline**

3falseleftrich19122ef78-67af-46fc-80ba-91c6f81a3440Confluence:2083817226700v2_b0144a51247b401b06251bbc238814ef8433ddd6ae2e16c584427cdaa775c913-a=103589275&c=Confluence%3A2083817226&d=f8964d24-fdfe-4e3b-b49d-bf7cd4d9eaa5&p=7112491067f8964d24-fdfe-4e3b-b49d-bf7cd4d9eaa51744861924217500

## Summary

**Reduction in ingestion cost**

The new ingestion pipeline using Snowpipe streaming has reduced costs by **25%** compared to the old pipeline.

  * Average Ingestion Costs:


*[See full page for complete details](https://zendesk.atlassian.net/wiki/spaces/ENG/pages/7112491067)*

---


# Appendix: Data Engineering Glossary

## Key Terms

- **PDD (Platform Data Domain)**: The organizational domain responsible for platform-level data infrastructure, pipelines, and services
- **EDA (Enterprise Data Architecture)**: The enterprise-wide data strategy, governance, and architectural standards
- **Data Engineering**: The practice of designing, building, and maintaining data pipelines and infrastructure
- **Product Analytics**: Analysis of product usage data to drive product decisions
- **ETL/ELT**: Extract, Transform, Load / Extract, Load, Transform data processes
- **Data Pipeline**: Automated workflow for moving and transforming data
- **Data Model**: Structured representation of data entities and relationships

