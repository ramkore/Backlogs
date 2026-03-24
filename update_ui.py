import re

file_path = "d:/1.Projects/Results/BacklogReport 1/Backlog_Report.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Replace CSS
css_old = r"""        \.controls \{
            max-width: 1800px;.*?
        \.btn:disabled \{
            opacity: 0\.5;
            cursor: not-allowed;
            transform: none !important;
        \}"""
css_new = r"""        .top-bar-container {
            max-width: 1800px;
            margin: 24px auto;
            padding: 0 16px;
        }

        .top-bar {
            background: var(--card-bg);
            border-radius: var(--radius);
            box-shadow: var(--shadow);
            padding: 16px 20px;
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            align-items: flex-end;
            justify-content: space-between;
        }

        .input-group {
            display: flex;
            gap: 12px;
            align-items: flex-end;
            flex-wrap: wrap;
        }

        .input-wrapper {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .input-label {
            font-size: 11px;
            font-weight: 700;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .filter-input {
            padding: 9px 12px;
            border: 1px solid var(--border);
            border-radius: 6px;
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            outline: none;
            width: 140px;
            background: #fafafa;
            transition: all 0.2s;
        }

        .filter-input:focus {
            background: #fff;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(26, 35, 126, 0.1);
        }

        .action-group {
            display: flex;
            gap: 10px;
            align-items: center;
            flex-wrap: wrap;
        }

        .btn {
            padding: 9px 16px;
            border: none;
            border-radius: 6px;
            font-family: 'Inter', sans-serif;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            height: 38px;
        }

        .btn:hover:not(:disabled) {
            transform: translateY(-1px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }

        .btn-primary {
            background: var(--primary);
            color: white;
        }

        .btn-primary:hover:not(:disabled) {
            background: var(--primary-light);
        }

        .btn-success {
            background: var(--success);
            color: white;
        }

        .btn-accent {
            background: var(--accent);
            color: white;
        }

        .btn-outline {
            background: transparent;
            color: var(--text);
            border: 1px solid var(--border);
        }

        .btn-outline:hover:not(:disabled) {
            background: var(--bg);
            border-color: #bbb;
        }

        .divider {
            width: 1px;
            height: 30px;
            background: var(--border);
            margin: 0 4px;
        }

        .btn:disabled {
            opacity: 0.6;
            cursor: not-allowed;
            filter: grayscale(100%);
        }"""
content = re.sub(css_old, css_new, content, flags=re.DOTALL)

# 2. Update print media query
content = content.replace(".controls,", ".top-bar-container,")

# 3. Replace HTML
html_old = r"""    <div class="controls">
        <button class="btn btn-primary" id="fetchBtn" onclick="fetchAndUpdate\(\)">🚀 Fetch & Update from API</button>
        <button class="btn btn-success" id="exportBtn" onclick="exportCSV\(\)" disabled>📥 Export CSV</button>
        <button class="btn btn-accent" onclick="window\.print\(\)">🖨️ Print</button>
        <button class="btn btn-outline" onclick="toggleOnlyBacklogs\(\)">🔍 Toggle: Show Only Backlogs</button>
        <span id="statusBadge" style="font-size:12px;font-weight:600;color:var\(--text-muted\);margin-left:auto;"></span>
    </div>"""
html_new = r"""    <div class="top-bar-container">
        <div class="top-bar">
            <div class="input-group" style="align-items: flex-end;">
                <div class="input-wrapper">
                    <span class="input-label">Year</span>
                    <input type="text" id="batchYear" value="24" class="filter-input" style="width: 50px; text-align: center;" />
                </div>
                <div class="input-wrapper">
                    <span class="input-label">Code</span>
                    <input type="text" id="collegeCode" value="6F" class="filter-input" style="width: 50px; text-align: center;" />
                </div>
                <div class="input-wrapper">
                    <span class="input-label">Branch</span>
                    <select id="branchSelect" class="filter-input" style="width: 160px; padding: 8px 10px;">
                        <option value="01">CIVIL (01)</option>
                        <option value="02">EEE (02)</option>
                        <option value="04">ECE (04)</option>
                        <option value="05" selected>CSE (05)</option>
                        <option value="62">CSE (CS) (62)</option>
                        <option value="67">CSE (AI & ML) (67)</option>
                        <option value="74">CSE (DS) (74)</option>
                    </select>
                </div>
                <div class="input-wrapper">
                    <span class="input-label">Reg End</span>
                    <input type="text" id="regEnd" value="C8" class="filter-input" title="Suffix for Last Regular Student (e.g. C8)" style="width: 60px; text-align: center;" />
                </div>
                <div class="input-wrapper">
                    <span class="input-label">LE End</span>
                    <input type="text" id="leEnd" value="12" class="filter-input" title="Suffix for Last LE Student (e.g. 12)" style="width: 60px; text-align: center;" />
                </div>
                <button class="btn btn-primary" id="fetchBtn" onclick="startFetchProcess()" style="margin-left: 4px;">🚀 Fetch Data</button>
            </div>

            <div class="action-group">
                <button class="btn btn-outline" onclick="resetFilter()">🔄 Reset UI</button>
                <div class="divider"></div>
                <button class="btn btn-outline" onclick="toggleOnlyBacklogs()">🔍 Show Backlogs Only</button>
                <div class="divider"></div>
                <button class="btn btn-success" id="exportBtn" onclick="exportCSV()" disabled>📥 Export CSV</button>
                <button class="btn btn-accent" onclick="window.print()">🖨️ Print</button>
            </div>
        </div>
        <div style="text-align: right; margin-top: 8px; padding-right: 4px;">
            <span id="statusBadge" style="font-size:12px;font-weight:600;color:var(--text-muted);"></span>
        </div>
    </div>"""
content = re.sub(html_old, html_new, content, flags=re.DOTALL)

# 4. Replace JS data array and add generation wrapper
js_old = r"""        // Pre-loaded student data from the backlog report
        const students = \[
.*?\];

        let showOnlyBacklogs = false;"""
js_new = r"""        // Generic empty student data array
        let students = [];

        let showOnlyBacklogs = false;

        function generateSequence(start, end) {
            const startStr = start.toUpperCase();
            const endStr = end.toUpperCase();

            if (startStr.length !== endStr.length || startStr.length < 2) return [startStr, endStr];

            const prefix = startStr.substring(0, startStr.length - 2);
            const prefixEnd = endStr.substring(0, endStr.length - 2);

            if (prefix !== prefixEnd) return [startStr, endStr];

            let s1 = startStr.charAt(startStr.length - 2), s2 = startStr.charAt(startStr.length - 1);
            let e1 = endStr.charAt(endStr.length - 2), e2 = endStr.charAt(endStr.length - 1);

            let all = [];
            for (let i = 0; i <= 9; i++) {
                for (let j = 0; j <= 9; j++) {
                    all.push(i.toString() + j.toString());
                }
            }
            const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            for (let c of letters) {
                for (let j = 0; j <= 9; j++) {
                    all.push(c + j.toString());
                }
            }

            const startIndex = all.indexOf(s1 + s2);
            const endIndex = all.indexOf(e1 + e2);

            let result = [];
            if (startIndex !== -1 && endIndex !== -1 && startIndex <= endIndex) {
                for (let i = startIndex; i <= endIndex; i++) {
                    result.push(prefix + all[i]);
                }
            } else {
                result = [startStr, endStr];
            }

            return result;
        }

        async function startFetchProcess() {
            const year = document.getElementById('batchYear').value.trim();
            const cCode = document.getElementById('collegeCode').value.trim().toUpperCase();
            const branch = document.getElementById('branchSelect').value;
            const regEnd = document.getElementById('regEnd').value.trim().toUpperCase();
            const leEnd = document.getElementById('leEnd').value.trim().toUpperCase();

            if (!year || !cCode || !branch || !regEnd || !leEnd) {
                alert("Please fill in all details (Year, Code, Branch, Reg End, LE End)");
                return;
            }

            localStorage.setItem('pecBacklogYear', year);
            localStorage.setItem('pecBacklogCode', cCode);
            localStorage.setItem('pecBacklogBranch', branch);
            localStorage.setItem('pecBacklogRegEnd', regEnd);
            localStorage.setItem('pecBacklogLEEnd', leEnd);

            const fetchBtn = document.getElementById('fetchBtn');
            fetchBtn.innerHTML = '<span class="spinner"></span> Generating...';
            fetchBtn.disabled = true;

            const regPrefix = `${year}${cCode}1A${branch}`;
            const startRoll = `${regPrefix}01`;
            const endRoll = `${regPrefix}${regEnd}`;
            
            const leYear = (parseInt(year) + 1).toString().padStart(2, '0');
            const lePrefix = `${leYear}${cCode}5A${branch}`;
            const leStartRoll = `${lePrefix}01`;
            const leEndRoll = `${lePrefix}${leEnd}`;

            const regRolls = generateSequence(startRoll, endRoll);
            const leRolls = generateSequence(leStartRoll, leEndRoll);
            
            const rolls = [...regRolls, ...leRolls];

            students = rolls.map((r, i) => ({
                sno: i + 1,
                roll: r,
                name: "Fetching...",
                phone: "",
                mother: "",
                father: "",
                nptel: "",
                lateral: !!r.includes("5A"),
                sem: {}
            }));

            renderTable();
            await fetchAndUpdate();
        }

        function resetFilter() {
            document.getElementById('batchYear').value = '24';
            document.getElementById('collegeCode').value = '6F';
            document.getElementById('branchSelect').value = '05';
            document.getElementById('regEnd').value = 'C8';
            document.getElementById('leEnd').value = '12';
            localStorage.removeItem('pecBacklogYear');
            localStorage.removeItem('pecBacklogCode');
            localStorage.removeItem('pecBacklogBranch');
            localStorage.removeItem('pecBacklogRegEnd');
            localStorage.removeItem('pecBacklogLEEnd');
            students = [];
            renderTable();
        }

        window.addEventListener('DOMContentLoaded', () => {
            const y = localStorage.getItem('pecBacklogYear');
            const c = localStorage.getItem('pecBacklogCode');
            const b = localStorage.getItem('pecBacklogBranch');
            const r = localStorage.getItem('pecBacklogRegEnd');
            const l = localStorage.getItem('pecBacklogLEEnd');
            if (y) document.getElementById('batchYear').value = y;
            if (c) document.getElementById('collegeCode').value = c;
            if (b) document.getElementById('branchSelect').value = b;
            if (r) document.getElementById('regEnd').value = r;
            if (l) document.getElementById('leEnd').value = l;
        });"""
content = re.sub(js_old, js_new, content, flags=re.DOTALL)

# 5. Fix title inside `<title>` to generic title
content = re.sub(r"<title>PEC CSE-A Backlog Report</title>", r"<title>PEC Backlog Report Generator</title>", content)

# 6. Fix report title inside UI
content = re.sub(r"📋 CSE-A — Semester-Wise Backlog Report \(I-I to IV-II\)", r"📋 PEC — Semester-Wise Backlog Report Generator", content)

# 7. Add updating of fetching name dynamically inside fetchAndUpdate
fetch_update_old = r"""                        if \(\!resp\.ok\) return;
                        const data = await resp\.json\(\);
                        if \(\!data || \!data\.student\) return;"""
fetch_update_new = r"""                        if (!resp.ok) {
                            if (st.name === "Fetching...") st.name = "Not Found";
                            return;
                        }
                        const data = await resp.json();
                        if (!data || !data.student) {
                            if (st.name === "Fetching...") st.name = "Not Found";
                            return;
                        }
                        
                        if (data.student.fullName && st.name === "Fetching...") {
                            st.name = data.student.fullName;
                        }"""
content = re.sub(fetch_update_old, fetch_update_new, content, flags=re.DOTALL)

# 8. Add catch block to catch exceptions and update student fetching text
fetch_update_catch_old = r"""                    \} catch \(e\) \{ \}
                \}\);"""
fetch_update_catch_new = r"""                    } catch (e) {
                         if (st.name === "Fetching...") st.name = "Not Found";
                    }
                });"""
content = re.sub(fetch_update_catch_old, fetch_update_catch_new, content, flags=re.DOTALL)

# 9. Clear invalid students after fetch cycle completes
fetch_update_finish_old = r"""            fetchBtn\.innerHTML = '✅ Updated from API';
            document\.getElementById\('progressText'\)\.textContent = `Completed! \$\{total\} students updated\.`;
            document\.getElementById\('exportBtn'\)\.disabled = false;"""
fetch_update_finish_new = r"""            // Filter out invalid generated roll numbers
            students = students.filter(st => st.name !== "Not Found" && st.name !== "Fetching...");
            students.forEach((st, idx) => st.sno = idx + 1);
            
            fetchBtn.innerHTML = '🚀 Fetch Data';
            fetchBtn.disabled = false;
            document.getElementById('progressText').textContent = `Completed! ${students.length} valid students updated.`;
            document.getElementById('exportBtn').disabled = false;"""
content = re.sub(fetch_update_finish_old, fetch_update_finish_new, content, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated successfully")
