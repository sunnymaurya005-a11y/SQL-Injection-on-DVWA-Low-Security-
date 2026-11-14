# Manual SQL Injection Lab Inputs

**Target:** Local DVWA → SQL Injection  
**Scope:** The tester's own local Docker lab only.

## Low security — logical-condition test

Input used in the supplied screenshot:

```text
' OR '1'='1
```

**Purpose:** Observe whether the input changes the query's logical condition and returns records beyond the normal lookup.

**Evidence:** `screenshots/sql-injection-low-result.jpg`

## Baseline — normal identifier

```text
1
```

**Purpose:** Establish the normal lookup response for user ID 1.

**Important:** `1` is an ordinary identifier, not an injection payload.

**Evidence:** `screenshots/sql-injection-baseline.jpg`

## Medium security — observation notes

The Medium interface uses a dropdown-style input rather than the free-text field shown at Low. In the common DVWA implementation, the form submits the selected identifier in a POST request. This changes how the request is delivered; it does not, by itself, prove that server-side SQL is safe.

Record the exact request and response from your own local run. Do not claim that a test succeeded unless the observed output supports that conclusion.

## Test log

| Level | Input / action | Classification | Result |
|---|---|---|---|
| Low | `' OR '1'='1` | Logical-condition test string | Refer to supplied screenshot and report |
| Low | `1` | Normal ID baseline | Refer to supplied screenshot and report |
| Medium | Select a valid ID and inspect the POST request | Baseline / request inspection | Record your actual observation in the report |
