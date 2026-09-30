# System documentation update structure

```markdown
# 1. Release summary
| Item | Value |
|---|---|
| Change request | CR-… |
| Module(s) | … |
| Release / deployment date | … |
| QA sign-off | Signed by <name> on <date> / Pending |
| Sources | SRS v…, Design v…, Implementation notes v…, Test report cycle … |

# 2. Functional description (as implemented)
## 2.x <Function name>
<!-- Business-language description of how it works now. Cite FR IDs in brackets. -->

# 3. Business rules
| Rule | Description | Enforced in (object) | Source (RULE/FR) |

# 4. Screens and reports
| App / page / report | Purpose | Roles | Key items / parameters | Change in this release |

# 5. Data dictionary
## 5.1 New tables
### HRD.<TABLE>
Purpose: …
| Column | Type | Null | Description | Valid values / FK |
## 5.2 Changed tables
| Table | Column | Change | New definition | Meaning |
## 5.3 Retired objects

# 6. Program units, views, triggers and jobs
| Object | Type | Purpose | Parameters / schedule | Called from / by | CR / DS |

# 7. Interfaces
| Interface | Direction | Data | Frequency | Error handling |

# 8. Security and roles
| Role | Access granted / changed | Authorization scheme |

# 9. Operations and support
## 9.1 Monitoring and scheduled tasks
## 9.2 Common errors and resolution
| Error / message | Cause | Resolution |
## 9.3 Rollback reference

# 10. Known limitations and not delivered
| Item | Description | Reference (DEF / FR / deviation) | Planned fix |

# 11. Change log
| Date | CR | Section(s) changed | Summary | Author |
```
