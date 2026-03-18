# 🏗️ Macro-Micro System Architecture

This API does not exist in a vacuum. It is the execution layer of a broader two-part ecosystem designed for modern supply chain logistics.

## 1. The Macro Layer: Digital Capacity Twin
* **Repo:** [Digital Capacity Optimizer](https://github.com/sandesh-s-hegde/digital_capacity_optimizer)
* **Role:** Predictive Analytics. It runs 18,000+ rows of historical data through Monte Carlo simulations to predict volume surges and capacity shortfalls across global shipping lanes.
* **Output:** Identifies *where* and *when* physical assets are needed.

## 2. The Micro Layer: B2B Fleet Aggregator (This API)
* **Role:** Tactical Execution. When the Macro layer predicts a shortfall (e.g., needing 50 vans in Dublin), this API pings multiple real-world suppliers, aggregates the inventory, applies surge pricing, and locks in the physical capacity.
* **Output:** Converts predictive data into actionable, stateful database bookings.

## 🔄 The Closed Loop
By separating the heavy data-science forecasting (Macro) from the high-speed transactional booking engine (Micro), the system achieves massive horizontal scalability without latency bottlenecks.