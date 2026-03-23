# 🌍 The Logistics Ecosystem Architecture

The **B2B Fleet Aggregator API** is designed to function as the automated execution layer (The "Micro") within a broader suite of supply chain analytics tools. 

*Note: The applications currently operate as decoupled, standalone microservices. The integration flow detailed below represents the **Phase 7 Technical Roadmap: Ecosystem Integration**.*

## Target Integration Roadmap (Phase 7: EGA Loop)

Once fully integrated, the ecosystem will form a closed **Empirically Grounded Analytics (EGA)** loop.

### 1. The Sensor: Project Sentinel
* **Role:** Captures unstructured visual data from distribution nodes.
* **Output:** Calculates real-time "Flow Entropy" and kinematic disorder.

### 2. The Brain: Digital Capacity Optimizer
* **Role:** Ingests the entropy data and runs stochastic simulations (Newsvendor Problem).
* **Output:** Determines if safety stock thresholds are breached and generates a capacity procurement payload.

### 3. The Executor: B2B Fleet Aggregator (This Repository)
* **Role:** Acts as the automated execution layer and webhook receiver for the Optimizer.
* **Action:** When triggered by stochastic capacity shortfalls, it automatically adjusts surge pricing, searches the database for low-emission partner vehicles, and executes the B2B booking to absorb the supply chain volatility.

## Current State
Presently, this API functions as an independent, production-ready backend. It allows B2B partners to manually provision fleet assets, simulate dynamic surge pricing logic, and calculate macro-level utilization metrics.