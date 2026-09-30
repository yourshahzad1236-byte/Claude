# Implementation notes structure

```markdown
# 1. Summary
| Item | Value |
|---|---|
| Design implemented | <file> v<x> (<status>) |
| Objects created / modified | n / n |
| Deviations from design | n |
| Unit tests | n (all expected to PASS in DEV) |

# 2. Files produced
| # | File | Object | Change type | DS | FR |

# 3. Deviations from design
| # | Design said | Implemented | Reason | Needs SA sign-off (Y/N) |
<!-- "None" if none. Every missing, renamed or re-signed object goes here. -->

# 4. Manual steps
<!-- APEX Builder changes (page-by-page), config, scheduler enablement, anything not scripted. -->

# 5. Installation
## 5.1 Prerequisites
## 5.2 Run order
## 5.3 Verification
## 5.4 Rollback

# 6. Unit tests
| Test | Program unit | Scenario | Covers (FR/AC) | Expected |

# 7. Known limitations and follow-ups
```
