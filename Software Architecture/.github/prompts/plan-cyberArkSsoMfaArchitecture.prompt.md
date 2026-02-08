## Plan: CyberArk SSO/MFA Architecture Assignment

**Objective**: Document a workplace system's architecture in PPT format (PDF submission) to understand software architecture basics.

**System**: CyberArk Identity - SSO/MFA Platform (or PAM with MFA integration)

### Assignment Structure (11 Slides Total)

#### Slide 1: Purpose of the System (Goal)
- What problem does the system solve?
- Primary business/technical objectives
- Target users and use cases

#### Slides 2-3: Key Requirements
- **Slide 2 - Functional Requirements**:
  - User authentication and authorization
  - Key Considerations

1. **System Scope**: Focus on core SSO/MFA authentication flows. Avoid over-complicating with privileged session management unless directly relevant.

2. **ASR Examples for SSO/MFA**:
   - Security: Prevent unauthorized access, protect credentials
   - Performance: Authentication response time < 2 seconds
   - Availability: 99.9% uptime for authentication service
   - Scalability: Support 100K concurrent users
   - Usability: Seamless authentication experience

3. **Common Tactics in SSO/MFA**:
   - Security: OAuth 2.0/OIDC, JWT tokens, encryption (TLS/AES), MFA verification
   - Availability: Load balancing, redundancy, health monitoring, failover
   - Performance: Caching (sessions, tokens), connection pooling, CDN
   - Scalability: Horizontal scaling, stateless design, database sharding
   - Modifiability: Layered architecture, microservices, API gateway

4. **Deliverable**: PowerPoint presentation, export to PDF for submission

5. **Confidentiality**: Anonymize proprietary implementation details for academic submission
  - Security (encryption, zero trust, compliance)
  - Performance (authentication latency, throughput)
  - Availability (uptime SLAs, fault tolerance)
  - Scalability (user load, concurrent sessions)
  - Usability (authentication experience)
  - Maintainability and modifiability

#### Slide 4: Utility Tree of ASRs
- Prioritize quality attributes (H/M/L)
- Map scenarios with business impact
- Top 5 ASRs identified for deeper analysis

#### Slide 5: Tactics for Top 5 ASRs
- For each top ASR, document:
  - The specific tactic employed
  - How it addresses the requirement
  - Example: Security → Encryption, OAuth 2.0/OIDC, token validation

#### Slides 6-9: Software Architecture Diagrams
- **Slide 6 - Context Diagram**: System boundaries, external actors, integrations
- **Slide 7 - Module Decomposition**: Logical component breakdown, layers
- **Slide 8 - Component & Connector**: Runtime view, data flows, communication
- **Slide 9 - Deployment Diagram**: Infrastructure, servers, network topology

#### Slide 10: How the System Works
- End-to-end authentication flow
- Key interactions between components
- Example scenario walkthrough

#### Slide 11: Key Learnings
- Insights gained from architecture study
- Trade-offs observed
- Architectural patterns applied

### Execution Steps

1. **Select specific system focus**: CyberArk Identity (cloud SSO/MFA) vs PAM with MFA
2. **Gather content**: Document purpose, requirements, ASRs from work knowledge
3. **Create utility tree**: Prioritize ASRs with (H/M/L, H/M/L) quality-scenario pairs
4. **Identify tactics**: Map architectural tactics to top 5 ASRs
5. **Design 4 diagrams**: Context, Module, C&C, Deployment views
6. **Document workflow**: Write system operation description
7. **Capture learnings**: Reflect on architecture insights
8. **Build presentation**: Assemble in PowerPoint, export to PDF

### Further Considerations

1. **System scope**: Focus on core SSO/MFA flows only, or include privileged session management? Recommend starting narrow (SSO/MFA authentication flow) for clarity.

2. **Diagram tools**: Will you use draw.io, Lucidchart, PowerPoint shapes, or another tool for architecture diagrams?

3. **Sensitive information**: Ensure you anonymize or generalize any proprietary CyberArk implementation details that shouldn't be shared in academic submissions.
