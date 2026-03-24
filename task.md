# Backlog Report Generator Update

- [x] Analyze the provided pattern for generating student roll numbers.
- [x] Add input fields to the UI: Year, Code, Branch, Reg End, LE End.
- [x] Implement logic to generate `[YEAR][CODE]1A[BRANCH_CODE][01 to REG_END]` and `[YEAR+1][CODE]5A[BRANCH_CODE][01 to LE_END]` dynamically instead of hardcoded arrays.
- [x] Display and fetch data using this new pattern.
- [x] Add fail-fast timeout logic for APIs taking >15s to display an explicit error to the user.
