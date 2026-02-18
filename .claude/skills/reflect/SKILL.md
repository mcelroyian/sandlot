---
name: reflect
description: Extract learnings from coding sessions and propose additions to agent instruction files (CLAUDE.md). Use when reviewing sessions to capture high-value patterns and preferences.
---

# Reflect Skill

Extract learnings from the current coding session and propose additions to agent instruction files (CLAUDE.md).

## Goal

Analyze the session to identify high-value, generalizable patterns and preferences that should be preserved as context for future coding agents.

## Process

### Phase 1: Analysis & Proposal
1. Review the entire current session
2. Extract learnings across these categories:
   - **Repository structure/architecture** patterns
   - **Tooling and build systems** (configs, commands, gotchas)
   - **Testing strategies** (patterns, frameworks, coverage)
   - **User workflow preferences** (how user wants to work)
   - **Organizational context** (team conventions, approval processes)
   - **Code patterns and best practices** (idioms, anti-patterns to avoid)
   - **Error handling patterns** (how errors are managed)
   - **Debugging approaches** (tools, techniques used)
   - **Performance considerations** (optimization patterns)
   - **Git/version control workflows** (branching, commits, PRs)
   - **Documentation standards** (what to document, formats)
   - **Dependency management** (how deps are added/updated)
   - **Security practices** (auth, validation, sensitive data)

3. For each potential addition, present:
   - **Category**: What type of learning
   - **Boundary**: Scope/applicability
   - **Why Important**: Value proposition
   - **Confidence**: High/Medium/Low value estimate
   - **Target File**: Where it should go (user/project CLAUDE.md)

4. **Quality Filter**:
   - Prioritize HIGH-VALUE additions only
   - Must be generalizable and reusable
   - If session had no novel learnings, say so (don't force it)
   - Focus on what's **modular and maintainable**

### Phase 2: User Approval
Present proposals as concise overview. User reviews and approves/rejects.

### Phase 3: Implementation
For approved items:
1. Make changes directly (proposals in Phase 2 should be clear enough)
2. Keep additions **compressed and generic** - avoid over-specification

## Style Guidelines

✅ **DO:**
- Be concise and actionable
- Focus on generalizable patterns
- Use bullet points over paragraphs
- Keep instructions modular
- Think "what would help future agents?"

❌ **DON'T:**
- Add overly specific examples
- Document one-off situations
- Create redundant content
- Over-engineer the additions
- Force learnings if none exist

## Example Invocation

User: `/reflect` or activates the skill

Assistant analyzes session and responds:

```
## Session Learning Extraction

Found 3 high-value additions:

**1. Testing Strategy - Integration Test Pattern**
- Boundary: How to run and structure integration tests
- Why: Tests require specific setup not documented
- Confidence: High
- Target: Project CLAUDE.md

**2. Workflow Preference - Commit Strategy**
- Boundary: User's preferred commit message style
- Why: Ensures consistent commit history
- Confidence: High
- Target: User CLAUDE.md

**3. Tooling - Long-running Commands**
- Boundary: Commands that need timeout awareness
- Why: Prevents CI failures and confusion
- Confidence: Medium
- Target: Project CLAUDE.md

Proceed with all, or specify which to implement?
```

## Notes

- This skill should feel lightweight and not disrupt flow
- User can always edit after implementation
- Goal is incremental context building over time
