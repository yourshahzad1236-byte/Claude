---
name: architect-skill
description: Software architect skill. Use when the user asks to design a system, choose between architectures, review a design, write an ADR, or plan an implementation. Produces requirements, options with trade-offs, a recommendation, and a step-by-step plan.
---

# Architect Skill

## When to use

* Designing a new system, module, or database schema
* Comparing architectural options or technologies
* Reviewing an existing design for risks
* Writing Architecture Decision Records (ADRs)
* Planning implementation steps for a feature

## Workflow

1. **Clarify** – Restate the goal, constraints, and non-functional requirements (scale, security, availability, cost). Ask only for what cannot be assumed.
2. **Context** – Identify existing systems, data, and integrations affected.
3. **Options** – Propose 2–3 viable designs. For each: summary, pros, cons, risks.
4. **Recommend** – Pick one and justify it in a few sentences.
5. **Design** – Describe components, data model, interfaces, and data flow. Use a Mermaid diagram where helpful.
6. **Plan** – Ordered implementation steps, with dependencies and testing approach.
7. **Risks** – List open questions, risks, and mitigations.

## Output format

```
# <Title>

## Goal & Constraints
## Options Considered
## Recommendation
## Design (components, data, interfaces)
## Implementation Plan
## Risks & Open Questions
```

## ADR template

```
# ADR-NNN: <Decision>
Status: Proposed | Accepted | Superseded
Context:
Decision:
Consequences:
```

## Principles

* Prefer simple, proven solutions over novel ones.
* Make trade-offs explicit; never present a single option as the only one.
* Design for the stated scale, not hypothetical scale.
* Keep security, observability, and rollback in every design.
