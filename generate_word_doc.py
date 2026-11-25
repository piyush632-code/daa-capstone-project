import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
import os

doc = docx.Document()

# Page Margins
sections = doc.sections
for section in sections:
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)

# Title / Cover Page
p_univ = doc.add_paragraph()
p_univ.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_univ = p_univ.add_run("K.R. MANGALAM UNIVERSITY\n")
run_univ.font.size = Pt(20)
run_univ.font.bold = True
run_univ.font.color.rgb = RGBColor(15, 23, 42)

run_loc = p_univ.add_run("Gurugram, Haryana\n")
run_loc.font.size = Pt(12)
run_loc.font.color.rgb = RGBColor(71, 85, 105)

p_tag = doc.add_paragraph()
p_tag.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_tag = p_tag.add_run("\nACADEMIC CAPSTONE ASSIGNMENT REPORT\n")
run_tag.font.size = Pt(11)
run_tag.font.bold = True
run_tag.font.color.rgb = RGBColor(51, 65, 85)

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_title = p_title.add_run("Mini-Courier Planner\n")
run_title.font.size = Pt(26)
run_title.font.bold = True
run_title.font.color.rgb = RGBColor(30, 58, 138)

run_sub = p_title.add_run("Algorithmic Logistics Optimization using Dynamic Programming & Graph Search\n\n")
run_sub.font.size = Pt(12)
run_sub.font.color.rgb = RGBColor(71, 85, 105)

p_course = doc.add_paragraph()
p_course.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_c = p_course.add_run("Course: Design & Analysis of Algorithms (ETCCDA302)\nProgramme: BCA Hons. (AI & DS), Semester III\nAssessment Type: Coding-Based Capstone Project\n\n")
r_c.font.size = Pt(11)
r_c.font.bold = True

table_meta = doc.add_table(rows=1, cols=2)
table_meta.alignment = WD_TABLE_ALIGNMENT.CENTER
row_cells = table_meta.rows[0].cells
row_cells[0].text = "SUBMITTED BY:\nPiyush Sharma\nRoll No: 2501201009\nBCA Hons. (AI & DS)"
row_cells[1].text = "SUBMITTED TO:\nRuchika Bhakhar\nCourse Instructor / Faculty\nDept. of Computer Science & Applications"

p_date = doc.add_paragraph()
p_date.alignment = WD_ALIGN_PARAGRAPH.CENTER
r_date = p_date.add_run("\n\n\nNovember 2026")
r_date.font.size = Pt(11)
r_date.font.color.rgb = RGBColor(100, 116, 139)

doc.add_page_break()

# Section 1: Introduction
h1 = doc.add_heading("1. Introduction", level=1)
doc.add_paragraph(
    "In this capstone assignment, I have designed and implemented an end-to-end algorithmic courier dispatch and route planning engine called Mini-Courier Planner. In standard logistics networks, a distribution depot receives batches of incoming parcel orders having varying delivery deadlines, weights, and urgency priorities. However, the delivery van possesses a constrained payload capacity (in kilograms), preventing the delivery of all pending orders simultaneously in a single trip."
)
doc.add_paragraph("The software pipeline addresses two fundamental optimization decisions:")
p_pts = doc.add_paragraph()
p_pts.add_run("1. Optimal Packing Selection (Trip Plan): ").bold = True
p_pts.add_run("Determining which subset of parcels maximizes total fulfilled delivery priority without exceeding van carrying capacity.\n")
p_pts.add_run("2. Optimized Delivery Route: ").bold = True
p_pts.add_run("Computing the most efficient sequence of stops starting from the central depot, visiting all necessary destinations, and returning back to base with minimal travel distance (km).")

doc.add_paragraph("Four classic computer science algorithms were combined:")
doc.add_paragraph("• Merge Sort: Prioritizes parcels strictly by urgent delivery deadlines with stability preservation.", style='List Bullet')
doc.add_paragraph("• 0/1 Knapsack (DP): Solves the constrained loading problem to global optimality via bottom-up tabulation.", style='List Bullet')
doc.add_paragraph("• Dijkstra’s Algorithm: Determines optimal road paths across the weighted city graph.", style='List Bullet')
doc.add_paragraph("• Nearest Neighbour Heuristic: Constructs an approximate traveling salesperson tour in polynomial time.", style='List Bullet')

# Section 2: Phase 1
doc.add_page_break()
doc.add_heading("2. Phase 1 - Courier Problem Design and Planning", level=1)
doc.add_heading("2.1 Problem Formulation", level=2)
doc.add_paragraph(
    "The depot operates under physical physical constraints where parcel demand exceeds instantaneous capacity. Therefore, the planning engine executes a four-stage sequential pipeline: (1) Sorting urgent parcels, (2) 0/1 Knapsack optimization, (3) Dijkstra all-pairs shortest paths, and (4) Nearest Neighbour delivery tour."
)

doc.add_heading("2.2 Parcel Attributes", level=2)
table_p = doc.add_table(rows=6, cols=4)
headers = ["Attribute", "Data Type", "Description", "Sample Value"]
for j, h in enumerate(headers):
    table_p.cell(0, j).text = h
    table_p.cell(0, j).paragraphs[0].runs[0].font.bold = True

rows_data = [
    ["parcel_id", "String", "Unique parcel tracking identifier", "P1"],
    ["destination", "String", "Target delivery node / address code", "C"],
    ["weight", "Integer", "Physical package weight in kilograms (kg)", "6"],
    ["priority", "Integer", "Urgency rating from 1 (low) to 10 (critical)", "8"],
    ["deadline", "Integer", "Maximum allowable delivery window (hours)", "2"],
]
for i, row in enumerate(rows_data):
    for j, val in enumerate(row):
        table_p.cell(i+1, j).text = val

doc.add_heading("2.3 Delivery Points and Graph Representation", level=2)
doc.add_paragraph(
    "The central hub is designated as 'Depot'. Delivery destinations are vertices in an undirected weighted graph G = (V, E). Roads are represented using an Adjacency List (dictionary of lists) which requires O(V + E) space, offering superior memory efficiency over an Adjacency Matrix (O(V^2)) for sparse road networks."
)

if os.path.exists("screenshots/architecture_diagram.png"):
    doc.add_paragraph()
    doc.add_picture("screenshots/architecture_diagram.png", width=Inches(6.0))
    p_cap = doc.add_paragraph("Figure 1: Architectural Pipeline of Mini-Courier Planner")
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Section 3: Phase 2
doc.add_page_break()
doc.add_heading("3. Phase 2 - Package Prioritization and Box Filling", level=1)
doc.add_heading("3.1 Step 1: Merge Sort Prioritization", level=2)
doc.add_paragraph(
    "Parcels are initially ordered using Merge Sort. The comparator prioritizes the earliest delivery deadline. If two parcels possess identical deadlines, the tie is broken in favor of higher priority. Because Merge Sort is a stable sorting algorithm, parcels sharing equal deadlines and priorities preserve their original arrival sequence."
)

doc.add_heading("3.2 Step 2: 0/1 Knapsack Formulation (Dynamic Programming)", level=2)
doc.add_paragraph(
    "In parcel loading, fractional items cannot be packed; each item is either included or omitted. Greedy heuristics often lead to suboptimal van utilization. Dynamic Programming guarantees finding the mathematically optimal packing configuration using the Bellman recurrence relation:\n"
    "dp[i][w] = dp[i-1][w]  (if weight_i > w)\n"
    "dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight_i] + priority_i)  (if weight_i <= w)"
)

if os.path.exists("screenshots/phase2_sorting_knapsack.png"):
    doc.add_paragraph()
    doc.add_picture("screenshots/phase2_sorting_knapsack.png", width=Inches(6.0))
    p_cap = doc.add_paragraph("Figure 2: Merge Sort, Knapsack DP Table, and Optimal Packing Plan")
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_heading("3.3 Packing Plan & Failure of Greedy Approach", level=2)
doc.add_paragraph(
    "For the benchmark dataset (10 parcels, 20 kg capacity), the DP approach selects parcels P5, P1, P7, P2, and P4, utilizing exactly 20/20 kg with a total priority of 29. In contrast, a greedy approach prioritizing items purely by urgency or weight selects P3, P1, and P5, achieving a total priority of only 24 (a deficit of 5 points). This proves the necessity of Dynamic Programming."
)

# Section 4: Phase 3
doc.add_page_break()
doc.add_heading("4. Phase 3 - Route Maker and Graph Processing", level=1)
doc.add_heading("4.1 Step 3: Shortest Path Finding via Dijkstra's Algorithm", level=2)
doc.add_paragraph(
    "Once parcels are selected, their unique destination addresses define the set of delivery stops (F, C, A, B). Dijkstra's algorithm computes the shortest paths from the Depot and between every pair of stops. For instance, the direct road from Depot to A is 4 km, but Dijkstra discovers the indirect route Depot -> B -> A which is only 3 km, generating an immediate 25% distance reduction."
)

if os.path.exists("screenshots/phase3_route.png"):
    doc.add_paragraph()
    doc.add_picture("screenshots/phase3_route.png", width=Inches(6.0))
    p_cap = doc.add_paragraph("Figure 3: Road Graph, Dijkstra Shortest Paths, and Delivery Tour")
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_heading("4.2 Step 4: Nearest Neighbour TSP Heuristic", level=2)
doc.add_paragraph(
    "Finding the exact minimum tour across k delivery locations is NP-Hard (O(k!)). The Nearest Neighbour heuristic makes greedy local choices in polynomial time (O(k^2)):\n"
    "• At Depot: Next stop is B (2 km)\n"
    "• At B: Next stop is A (1 km)\n"
    "• At A: Next stop is C (5 km)\n"
    "• At C: Next stop is F (5 km)\n"
    "• At F: Return to Depot (13 km)\n"
    "Total Tour: Depot -> B -> A -> C -> F -> Depot (Total Distance: 26 km)."
)

# Section 5: Phase 4
doc.add_page_break()
doc.add_heading("5. Phase 4 - Performance Testing and Optimization", level=1)
doc.add_heading("5.1 Test Suite & Verification (11/11 Passed)", level=2)
doc.add_paragraph(
    "An automated test suite validates algorithmic correctness against edge cases (capacity 0, disconnected graphs, large capacity) and verifies correctness against brute-force baselines. All 11 unit tests passed."
)

if os.path.exists("screenshots/test_cases.png"):
    doc.add_paragraph()
    doc.add_picture("screenshots/test_cases.png", width=Inches(6.0))
    p_cap = doc.add_paragraph("Figure 4: Automated Verification Test Suite Output")
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_heading("5.2 Empirical Benchmark Analysis", level=2)
doc.add_paragraph(
    "Scalability tests were executed across increasing dataset sizes from 10 to 1,000 parcels. Each configuration was averaged across 3 trials:"
)

table_b = doc.add_table(rows=6, cols=8)
b_headers = ["Parcels", "Stops", "Capacity", "Merge Sort", "Knapsack DP", "Dijkstra", "NN-TSP", "Total (ms)"]
for j, h in enumerate(b_headers):
    table_b.cell(0, j).text = h
    table_b.cell(0, j).paragraphs[0].runs[0].font.bold = True

b_data = [
    ["10", "6", "20 kg", "0.043 ms", "0.119 ms", "0.140 ms", "0.012 ms", "0.315 ms"],
    ["50", "10", "50 kg", "0.195 ms", "0.833 ms", "0.312 ms", "0.015 ms", "1.355 ms"],
    ["100", "20", "100 kg", "0.337 ms", "3.114 ms", "1.534 ms", "0.046 ms", "5.031 ms"],
    ["500", "50", "500 kg", "2.310 ms", "95.993 ms", "20.023 ms", "0.317 ms", "118.643 ms"],
    ["1000", "100", "1000 kg", "5.358 ms", "408.253 ms", "143.424 ms", "1.200 ms", "558.234 ms"],
]
for i, row in enumerate(b_data):
    for j, val in enumerate(row):
        table_b.cell(i+1, j).text = val

if os.path.exists("results/runtime_chart.png"):
    doc.add_paragraph()
    doc.add_picture("results/runtime_chart.png", width=Inches(6.0))
    p_cap = doc.add_paragraph("Figure 5: Empirical Runtime Scaling Across Pipeline Components")
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Section 6 & 7: Phase 5 & Conclusion
doc.add_page_break()
doc.add_heading("6. Phase 5 - Result, Demonstration & Conclusion", level=1)
doc.add_heading("6.1 Medium Dataset Demonstration (40 Parcels)", level=2)
doc.add_paragraph(
    "The system was evaluated on a larger 40-parcel, 12-location dataset with 60 kg van capacity. The pipeline selected 14 parcels with a cumulative priority of 97 and synthesized a 105 km tour, confirming robustness on larger operational datasets."
)

if os.path.exists("screenshots/medium_dataset.png"):
    doc.add_paragraph()
    doc.add_picture("screenshots/medium_dataset.png", width=Inches(6.0))
    p_cap = doc.add_paragraph("Figure 6: Medium Dataset Execution Demonstration")
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_heading("7. Conclusion", level=1)
doc.add_paragraph(
    "The Mini-Courier Planner integrates four foundational algorithmic paradigms into an efficient, robust software system. Through empirical testing and theoretical analysis, the project demonstrates how exact mathematical programming (Merge Sort, 0/1 Knapsack DP, Dijkstra) provides optimal resource allocation, while heuristic approximation (Nearest Neighbour) circumvents computational bottlenecks in route planning."
)

out_docx_1 = r"c:\Users\piyus_on4gw3c\Downloads\DAA Capstone Project\DAA_Capstone_Report_Piyush_Sharma.docx"
out_docx_2 = r"c:\Users\piyus_on4gw3c\Downloads\DAA_Capstone_Report_Piyush_Sharma.docx"
out_docx_3 = r"C:\Users\piyus_on4gw3c\.gemini\antigravity\brain\e7581ed0-2689-45ae-a974-572e7dcaf513\DAA_Capstone_Report_Piyush_Sharma.docx"

doc.save(out_docx_1)
doc.save(out_docx_2)
doc.save(out_docx_3)

print("Saved DOCX files successfully!")
