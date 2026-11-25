import base64
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_b64(rel_path):
    full_path = os.path.join(BASE_DIR, rel_path)
    with open(full_path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

img_arch = get_b64("screenshots/architecture_diagram.png")
img_p2 = get_b64("screenshots/phase2_sorting_knapsack.png")
img_p3 = get_b64("screenshots/phase3_route.png")
img_med = get_b64("screenshots/medium_dataset.png")
img_tests = get_b64("screenshots/test_cases.png")
img_perf = get_b64("screenshots/performance_test.png")
img_chart = get_b64("results/runtime_chart.png")

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>DAA Capstone Report - Mini-Courier Planner</title>
<style>
  @page {{
    size: A4;
    margin: 16mm 14mm 16mm 14mm;
  }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.5;
    color: #1e293b;
    font-size: 10.5pt;
    margin: 0;
    padding: 0;
  }}
  .cover-page {{
    page-break-after: always;
    min-height: 88vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    text-align: center;
    padding: 30px 10px;
    box-sizing: border-box;
  }}
  .cover-header {{
    border-bottom: 2px solid #0f172a;
    padding-bottom: 18px;
  }}
  .univ-name {{
    font-size: 23pt;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
    text-transform: uppercase;
  }}
  .univ-loc {{
    font-size: 13pt;
    font-weight: 500;
    color: #475569;
  }}
  .report-tag {{
    display: inline-block;
    margin-top: 35px;
    padding: 6px 18px;
    background-color: #f1f5f9;
    border: 1px solid #cbd5e1;
    border-radius: 20px;
    font-size: 11pt;
    font-weight: 700;
    color: #334155;
    text-transform: uppercase;
    letter-spacing: 1px;
  }}
  .project-title {{
    font-size: 30pt;
    font-weight: 800;
    color: #1e3a8a;
    margin: 25px 0 10px 0;
    line-height: 1.2;
  }}
  .project-subtitle {{
    font-size: 13.5pt;
    color: #475569;
    margin-bottom: 30px;
  }}
  .course-box {{
    background: #f8fafc;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    padding: 16px 24px;
    max-width: 520px;
    margin: 0 auto;
    font-size: 11pt;
    text-align: left;
  }}
  .course-box p {{
    margin: 5px 0;
  }}
  .meta-grid {{
    display: flex;
    justify-content: space-between;
    margin-top: 45px;
    text-align: left;
    padding: 0 30px;
  }}
  .meta-col {{
    flex: 1;
  }}
  .meta-label {{
    font-size: 10pt;
    color: #64748b;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 4px;
  }}
  .meta-val {{
    font-size: 14pt;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 3px;
  }}
  .meta-sub {{
    font-size: 11pt;
    color: #475569;
  }}
  .cover-date {{
    font-size: 11pt;
    font-weight: 600;
    color: #64748b;
    margin-top: 35px;
  }}

  .page-break {{
    page-break-before: always;
  }}
  h1 {{
    font-size: 15pt;
    font-weight: 800;
    color: #0f172a;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 5px;
    margin-top: 20px;
    margin-bottom: 10px;
  }}
  h2 {{
    font-size: 12pt;
    font-weight: 700;
    color: #1e293b;
    margin-top: 14px;
    margin-bottom: 6px;
  }}
  h3 {{
    font-size: 10.5pt;
    font-weight: 700;
    color: #334155;
    margin-top: 10px;
    margin-bottom: 4px;
  }}
  p {{
    margin: 5px 0 8px 0;
    text-align: justify;
  }}
  ul, ol {{
    margin: 5px 0 8px 20px;
    padding: 0;
  }}
  li {{
    margin-bottom: 3px;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 9pt;
  }}
  th, td {{
    border: 1px solid #cbd5e1;
    padding: 5px 7px;
    text-align: left;
  }}
  th {{
    background-color: #0f172a;
    color: #ffffff;
    font-weight: 600;
  }}
  tr:nth-child(even) {{
    background-color: #f8fafc;
  }}
  code {{
    font-family: Consolas, 'Courier New', monospace;
    font-size: 9pt;
    background: #f1f5f9;
    padding: 2px 4px;
    border-radius: 4px;
    color: #0f172a;
  }}
  pre {{
    font-family: Consolas, 'Courier New', monospace;
    background-color: #0f172a;
    color: #f8fafc;
    padding: 10px;
    border-radius: 6px;
    font-size: 8.5pt;
    overflow-x: auto;
    line-height: 1.35;
    margin: 8px 0;
  }}
  .figure-box {{
    text-align: center;
    margin: 12px 0;
  }}
  .figure-img {{
    max-width: 95%;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.06);
  }}
  .figure-caption {{
    font-size: 8.5pt;
    font-weight: 600;
    color: #475569;
    margin-top: 4px;
  }}
  .callout {{
    background-color: #eff6ff;
    border-left: 4px solid #2563eb;
    padding: 8px 12px;
    margin: 8px 0;
    border-radius: 0 6px 6px 0;
    font-size: 10pt;
  }}
</style>
</head>
<body>

<!-- COVER PAGE -->
<div class="cover-page">
  <div class="cover-header">
    <div class="univ-name">K.R. Mangalam University</div>
    <div class="univ-loc">Gurugram, Haryana</div>
  </div>

  <div>
    <div class="report-tag">Academic Capstone Assignment</div>
    <div class="project-title">Mini-Courier Planner</div>
    <div class="project-subtitle">Algorithmic Logistics Optimization using Dynamic Programming & Graph Search</div>

    <div class="course-box">
      <p><strong>Course:</strong> Design & Analysis of Algorithms (ETCCDA302)</p>
      <p><strong>Programme:</strong> BCA Hons. (AI & DS), Semester III</p>
      <p><strong>Assessment Type:</strong> Coding-Based Capstone Project</p>
    </div>
  </div>

  <div class="meta-grid">
    <div class="meta-col">
      <div class="meta-label">Submitted By</div>
      <div class="meta-val">Piyush Sharma</div>
      <div class="meta-sub">Roll No: 2501201009</div>
      <div class="meta-sub">BCA Hons. (AI & DS)</div>
    </div>
    <div class="meta-col" style="text-align: right;">
      <div class="meta-label">Submitted To</div>
      <div class="meta-val">Ruchika Bhakhar</div>
      <div class="meta-sub">Course Instructor / Faculty</div>
      <div class="meta-sub">Dept. of Computer Science & Applications</div>
    </div>
  </div>

  <div class="cover-date">November 2026</div>
</div>

<!-- SECTION 1 -->
<div>
  <h1>1. Introduction</h1>
  <p>In this capstone assignment, I have designed and implemented an end-to-end algorithmic courier dispatch and route planning engine called <strong>Mini-Courier Planner</strong>. In standard logistics networks, a distribution depot receives batches of incoming parcel orders having varying delivery deadlines, weights, and urgency priorities. However, the delivery van possesses a constrained payload capacity (in kilograms), preventing the delivery of all pending orders simultaneously in a single trip.</p>
  
  <p>To resolve this practical optimization challenge, the software pipeline addresses two fundamental decisions:</p>
  <ul>
    <li><strong>Optimal Packing Selection (Trip Plan):</strong> Determining which subset of parcels maximizes total fulfilled delivery priority without exceeding van carrying capacity.</li>
    <li><strong>Optimized Delivery Route:</strong> Computing the most efficient sequence of stops starting from the central depot, visiting all necessary destinations, and returning back to base with minimal travel distance (km).</li>
  </ul>

  <p>The system uniquely combines four classic computer science algorithms studied in the curriculum:</p>
  <ol>
    <li><strong>Merge Sort (Divide-and-Conquer):</strong> Prioritizes parcels strictly by urgent delivery deadlines with stability preservation.</li>
    <li><strong>0/1 Knapsack (Dynamic Programming):</strong> Solves the constrained loading problem to global optimality via bottom-up tabulation.</li>
    <li><strong>Dijkstra's Algorithm (Greedy Single-Source Shortest Paths):</strong> Determines optimal road paths across the weighted city graph.</li>
    <li><strong>Nearest Neighbour Heuristic (TSP Approximation):</strong> Constructs an approximate traveling salesperson tour in polynomial time.</li>
  </ol>
  
  <p>All algorithms were coded natively in pure Python without reliance on third-party algorithmic packages, using <code>matplotlib</code> solely for empirical scalability benchmarking.</p>
</div>

<!-- PHASE 1 -->
<div class="page-break">
  <h1>2. Phase 1 - Courier Problem Design and Planning</h1>
  
  <h2>2.1 Problem Formulation</h2>
  <p>The depot operates under physical physical constraints: parcel demand exceeds instantaneous capacity. Therefore, the planning engine executes a four-stage sequential pipeline:</p>
  <ol>
    <li>Identify and rank urgent packages based on deadlines and customer priorities (Sorting).</li>
    <li>Compute the highest-value parcel subset that packs within the van's weight limit W (Knapsack DP).</li>
    <li>Derive the all-pairs shortest distances connecting the depot and selected delivery nodes (Dijkstra).</li>
    <li>Formulate a low-distance circular tour originating and terminating at the Depot (Nearest Neighbour TSP).</li>
  </ol>

  <h2>2.2 Parcel Attributes</h2>
  <p>Parcels are ingested via standard CSV formatting containing discrete quantitative attributes:</p>
  <table>
    <thead>
      <tr>
        <th>Attribute</th>
        <th>Data Type</th>
        <th>Description</th>
        <th>Sample Value</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><code>parcel_id</code></td><td>String</td><td>Unique parcel tracking identifier</td><td>P1</td></tr>
      <tr><td><code>destination</code></td><td>String</td><td>Target delivery node / address code</td><td>C</td></tr>
      <tr><td><code>weight</code></td><td>Integer</td><td>Physical package weight in kilograms (kg)</td><td>6</td></tr>
      <tr><td><code>priority</code></td><td>Integer</td><td>Urgency rating on a scale from 1 (low) to 10 (critical)</td><td>8</td></tr>
      <tr><td><code>deadline</code></td><td>Integer</td><td>Maximum allowable delivery window (hours)</td><td>2</td></tr>
    </tbody>
  </table>

  <h2>2.3 Delivery Points and Road Graph Representation</h2>
  <p>The central hub is consistently designated as <code>Depot</code>. Delivery destinations are modeled as vertices in an undirected, weighted graph G = (V, E) where edge weights denote road distances in kilometers. Two-way traffic is assumed.</p>
  
  <p>An <strong>Adjacency List</strong> (implemented as a Python dictionary of neighbour-distance tuples) was chosen over an Adjacency Matrix because road networks in urban logistics are inherently sparse (E &lt;&lt; V^2). The adjacency list requires only O(V + E) space compared to O(V^2) for matrices, and enables Dijkstra's algorithm to inspect direct outgoing edges without scanning non-existent connections.</p>

  <div class="figure-box">
    <img src="{img_arch}" class="figure-img" alt="Figure 1: Architectural Pipeline">
    <div class="figure-caption">Figure 1: Architectural Pipeline of Mini-Courier Planner</div>
  </div>

  <h2>2.4 Algorithmic Complexity Profile</h2>
  <table>
    <thead>
      <tr>
        <th>Pipeline Stage</th>
        <th>Algorithm</th>
        <th>Paradigm</th>
        <th>Time Complexity</th>
        <th>Space Complexity</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Package Prioritization</td><td>Merge Sort</td><td>Divide-and-Conquer</td><td>O(n log n)</td><td>O(n)</td></tr>
      <tr><td>Box Filling / Selection</td><td>0/1 Knapsack</td><td>Dynamic Programming</td><td>O(n &times; W)</td><td>O(n &times; W)</td></tr>
      <tr><td>Road Distance Analysis</td><td>Dijkstra (Multi-Source)</td><td>Greedy Search</td><td>O(k &times; V^2)</td><td>O(V)</td></tr>
      <tr><td>Delivery Tour Planning</td><td>Nearest Neighbour</td><td>Heuristic Approximation</td><td>O(k^2)</td><td>O(k)</td></tr>
    </tbody>
  </table>
  <p><em>(Where n = parcel count, W = van capacity, V = network vertices, k = unique delivery stops).</em></p>
</div>

<!-- PHASE 2 -->
<div class="page-break">
  <h1>3. Phase 2 - Package Prioritization and Box Filling</h1>
  
  <h2>3.1 Step 1: Merge Sort Prioritization</h2>
  <p>Parcels are initially ordered using Merge Sort. The comparator prioritizes the earliest delivery deadline. If two parcels possess identical deadlines, the tie is broken in favor of higher priority. Because Merge Sort is a <strong>stable sorting algorithm</strong>, parcels sharing equal deadlines and priorities preserve their original relative arrival sequence.</p>

  <h2>3.2 Step 2: 0/1 Knapsack Formulation (Dynamic Programming)</h2>
  <p>In parcel loading, fractional items cannot be packed; each item is either included (x_i = 1) or omitted (x_i = 0). Greedy heuristics (e.g., sorting by priority/weight ratio) often lead to suboptimal van utilization. Dynamic Programming guarantees finding the mathematically optimal packing configuration.</p>

  <p>Let dp[i][w] denote the maximum achievable priority considering the first i sorted parcels under an instantaneous capacity limit w:</p>
  <div class="callout">
    <strong>Bellman Recurrence Relation:</strong><br>
    dp[i][w] = dp[i-1][w] &nbsp;&nbsp;&nbsp;<em>(if weight_i &gt; w)</em><br>
    dp[i][w] = max( dp[i-1][w], &nbsp; dp[i-1][w - weight_i] + priority_i ) &nbsp;&nbsp;&nbsp;<em>(if weight_i &le; w)</em>
  </div>

  <div class="figure-box">
    <img src="{img_p2}" class="figure-img" alt="Figure 2: Sorting, DP Table and Packing Plan">
    <div class="figure-caption">Figure 2: Execution Output - Merge Sort, Knapsack DP Table, and Optimal Packing Plan</div>
  </div>

  <h2>3.3 Packing Plan & Failure of Greedy Approach</h2>
  <p>For the benchmark dataset (10 parcels, 20 kg capacity):</p>
  <ul>
    <li><strong>DP Optimal Selection:</strong> P5 (5kg, p=7), P1 (6kg, p=8), P7 (4kg, p=6), P2 (3kg, p=5), P4 (2kg, p=3). Total Weight = 20 / 20 kg (100% capacity), Total Priority = <strong>29</strong>.</li>
    <li><strong>Greedy Failure Demonstration:</strong> A greedy heuristic sorting by priority picks P3 (9kg, p=9), P1 (6kg, p=8), and P5 (5kg, p=7) with total weight 20 kg, achieving a total priority of only <strong>24</strong>. Greedy sacrifices multiple smaller high-value packages, falling short of DP by 5 points.</li>
  </ul>
</div>

<!-- PHASE 3 -->
<div class="page-break">
  <h1>4. Phase 3 - Route Maker and Graph Processing</h1>

  <h2>4.1 Step 3: Shortest Path Finding via Dijkstra's Algorithm</h2>
  <p>Once the parcels are selected, their unique destination addresses define the set of delivery stops S = {{F, C, A, B}}. Because roads vary in distance, direct roads are not necessarily the shortest. Dijkstra's algorithm explores shortest paths from the <code>Depot</code> and from each selected delivery stop.</p>
  
  <p>For example, the direct road from <code>Depot</code> to <code>A</code> is 4 km. However, Dijkstra discovers the indirect route <code>Depot -&gt; B -&gt; A</code> which has a total length of only <strong>3 km</strong> (2 km + 1 km), demonstrating significant route savings.</p>

  <div class="figure-box">
    <img src="{img_p3}" class="figure-img" alt="Figure 3: Dijkstra Shortest Paths and TSP Tour">
    <div class="figure-caption">Figure 3: Execution Output - Road Graph, Dijkstra Shortest Paths, and Final Delivery Tour</div>
  </div>

  <h2>4.2 Step 4: Nearest Neighbour TSP Heuristic</h2>
  <p>Finding the exact minimum Hamiltonian cycle across k delivery locations is NP-Hard (O(k!)). To maintain real-time responsiveness, the Nearest Neighbour heuristic makes locally optimal greedy selections:</p>
  <table>
    <thead>
      <tr>
        <th>Current Location</th>
        <th>Unvisited Stops & Dijkstra Distances</th>
        <th>Selected Next Hop</th>
        <th>Segment Distance</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Depot</td><td>B: 2km, A: 3km, C: 8km, F: 13km</td><td><strong>B</strong></td><td>2 km</td></tr>
      <tr><td>B</td><td>A: 1km, C: 6km, F: 11km</td><td><strong>A</strong></td><td>1 km</td></tr>
      <tr><td>A</td><td>C: 5km, F: 10km</td><td><strong>C</strong></td><td>5 km</td></tr>
      <tr><td>C</td><td>F: 5km</td><td><strong>F</strong></td><td>5 km</td></tr>
      <tr><td>F</td><td>All stops completed &rarr; Return to Depot</td><td><strong>Depot</strong></td><td>13 km</td></tr>
    </tbody>
  </table>
  <p><strong>Total Constructed Tour:</strong> <code>Depot &rarr; B &rarr; A &rarr; C &rarr; F &rarr; Depot</code> (Total Distance: <strong>26 km</strong>). Exhaustive permutation checks confirm that 26 km is the absolute global optimum for this dataset.</p>
</div>

<!-- PHASE 4 -->
<div class="page-break">
  <h1>5. Phase 4 - Performance Testing and Optimization</h1>

  <h2>5.1 Test Suite & Verification (11/11 Passed)</h2>
  <p>An automated test suite (<code>test_cases.py</code>) validates algorithmic correctness against edge cases, Python built-in references, and brute-force benchmarks:</p>
  
  <div class="figure-box">
    <img src="{img_tests}" class="figure-img" alt="Figure 4: Test Suite Results">
    <div class="figure-caption">Figure 4: Automated Verification Suite - All 11 Unit Tests Passing</div>
  </div>

  <h2>5.2 Empirical Benchmark Analysis</h2>
  <p>Synthetic scalability tests were executed across increasing orders of magnitude from 10 to 1,000 parcels. Each configuration was executed over 3 trials, recording average step durations in milliseconds (ms):</p>

  <div class="figure-box">
    <img src="{img_perf}" class="figure-img" alt="Figure 5: Performance Test Console Output">
    <div class="figure-caption">Figure 5: Empirical Benchmark Output Across Increasing Problem Scales</div>
  </div>

  <table>
    <thead>
      <tr>
        <th>Parcels (n)</th>
        <th>Stops (V)</th>
        <th>Capacity (W)</th>
        <th>Merge Sort (ms)</th>
        <th>Knapsack DP (ms)</th>
        <th>Dijkstra (ms)</th>
        <th>NN-TSP (ms)</th>
        <th>Total Time (ms)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>10</td><td>6</td><td>20 kg</td><td>0.043</td><td>0.119</td><td>0.140</td><td>0.012</td><td>0.315</td></tr>
      <tr><td>50</td><td>10</td><td>50 kg</td><td>0.195</td><td>0.833</td><td>0.312</td><td>0.015</td><td>1.355</td></tr>
      <tr><td>100</td><td>20</td><td>100 kg</td><td>0.337</td><td>3.114</td><td>1.534</td><td>0.046</td><td>5.031</td></tr>
      <tr><td>500</td><td>50</td><td>500 kg</td><td>2.310</td><td>95.993</td><td>20.023</td><td>0.317</td><td>118.643</td></tr>
      <tr><td>1000</td><td>100</td><td>1000 kg</td><td>5.358</td><td>408.253</td><td>143.424</td><td>1.200</td><td>558.234</td></tr>
    </tbody>
  </table>

  <div class="figure-box">
    <img src="{img_chart}" class="figure-img" alt="Figure 6: Runtime Benchmark Chart">
    <div class="figure-caption">Figure 6: Runtime Scaling Chart across Major Pipeline Components</div>
  </div>

  <h2>5.3 Architectural Observations & Growth Rates</h2>
  <ul>
    <li><strong>Knapsack Bottleneck:</strong> Knapsack DP accounts for &gt;70% of total runtime on large inputs due to its pseudo-polynomial O(n &times; W) complexity. As both n and W scale 10x (100 to 1000), tabular operations scale ~100x.</li>
    <li><strong>Dijkstra Scaling:</strong> Running Dijkstra from each stop scales as O(k &times; V^2). At 100 delivery points, distance resolution takes 143 ms.</li>
    <li><strong>Merge Sort Efficiency:</strong> Demonstrates remarkable O(n log n) efficiency, completing 1,000 parcels in merely 5.3 ms.</li>
    <li><strong>Nearest Neighbour Speed:</strong> Remains virtually instantaneous (&lt;1.2 ms) even at scale, illustrating the practical power of polynomial heuristics over exponential brute-force TSP.</li>
  </ul>

  <h2>5.4 Future Optimization Roadmap</h2>
  <ul>
    <li><strong>Min-Heap Dijkstra:</strong> Introducing Python's <code>heapq</code> reduces time complexity from O(V^2) to O((V + E) log V).</li>
    <li><strong>1D Memory-Optimized DP:</strong> Knapsack memory can be compressed to O(W) by iterating capacity backwards in a 1D array.</li>
    <li><strong>2-Opt Tour Refinement:</strong> Post-processing Nearest Neighbour tours with 2-Opt edge swaps eliminates intersecting route paths.</li>
  </ul>
</div>

<!-- PHASE 5 -->
<div class="page-break">
  <h1>6. Phase 5 - Result, Demonstration & Conclusion</h1>

  <h2>6.1 Scalability Demonstration on Medium Dataset (40 Parcels)</h2>
  <p>To verify production readiness, the system was executed on an expanded logistics scenario with 40 parcels, 12 city nodes, and 60 kg van capacity:</p>
  
  <div class="figure-box">
    <img src="{img_med}" class="figure-img" alt="Figure 7: Medium Dataset Demonstration">
    <div class="figure-caption">Figure 7: Demonstration Output on Medium Dataset (40 Parcels, 60kg Van Capacity)</div>
  </div>

  <h2>6.2 Execution Guide</h2>
  <pre><code># 1. Run standard courier planner on small dataset (20 kg capacity)
python main.py

# 2. Run with custom data files and specified capacity (e.g. 60 kg)
python main.py data/parcels_medium.csv data/roads_medium.csv 60

# 3. Execute unit verification tests
python test_cases.py

# 4. Run empirical performance benchmarks (regenerates results/runtime_chart.png)
python performance_test.py</code></pre>

  <h2>6.3 Project Codebase Structure</h2>
  <table>
    <thead>
      <tr>
        <th>File / Directory</th>
        <th>Role & Algorithmic Implementation</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><code>main.py</code></td><td>Application entry point orchestrating all 4 algorithmic phases</td></tr>
      <tr><td><code>sorting.py</code></td><td>Stable Merge Sort implementation for deadline-driven sorting</td></tr>
      <tr><td><code>knapsack.py</code></td><td>0/1 Knapsack DP table construction and backtrack selection</td></tr>
      <tr><td><code>route.py</code></td><td>Adjacency list graph, Dijkstra shortest paths & Nearest Neighbour tour</td></tr>
      <tr><td><code>performance_test.py</code></td><td>Multi-trial runtime benchmarking and Matplotlib visualization engine</td></tr>
      <tr><td><code>test_cases.py</code></td><td>Automated unit test suite validating correctness and optimality</td></tr>
      <tr><td><code>generate_data.py</code></td><td>Connected synthetic road network and parcel demand generator</td></tr>
      <tr><td><code>data/</code></td><td>Input CSV datasets (<code>parcels_*.csv</code> and <code>roads_*.csv</code>)</td></tr>
      <tr><td><code>results/</code></td><td>High-resolution empirical runtime charts (<code>runtime_chart.png</code>)</td></tr>
      <tr><td><code>screenshots/</code></td><td>Terminal execution output captures and architecture diagram</td></tr>
    </tbody>
  </table>

  <h2>7. Conclusion</h2>
  <p>The <strong>Mini-Courier Planner</strong> successfully integrates four foundational algorithmic paradigms into a coherent, high-performance software system. Through rigorous testing, the implementation proved that exact mathematical methods (Merge Sort, 0/1 Knapsack DP, Dijkstra) provide provable optimality for prioritization and dispatching, while heuristic approximation (Nearest Neighbour) overcomes combinatorial explosion for vehicle routing.</p>
  
  <p>The project provides deep practical insights into algorithmic trade-offs, theoretical vs empirical complexity, and real-world logistics engineering.</p>
</div>

</body>
</html>
'''

html_path = os.path.join(BASE_DIR, "DAA_Capstone_Report.html")
pdf_path = os.path.join(BASE_DIR, "DAA_Capstone_Report.pdf")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated HTML report at:", html_path)

# Run Edge headless to convert to PDF
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
if not os.path.exists(edge_path):
    edge_path = r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"

cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    html_path,
]

print("Compiling PDF using Edge headless...")
result = subprocess.run(cmd, capture_output=True, text=True)
print("PDF output code:", result.returncode)
if os.path.exists(pdf_path):
    print("DAA_Capstone_Report.pdf successfully created! Size:", os.path.getsize(pdf_path), "bytes")
else:
    print("Error generating PDF:", result.stderr)
