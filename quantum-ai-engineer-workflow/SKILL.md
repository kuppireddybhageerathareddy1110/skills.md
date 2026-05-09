---
name: quantum-ai-engineer-workflow
description: >
  Comprehensive guide for Quantum AI & ML engineering roles: algorithm development (QNN, QAOA, VQE,
  quantum kernels), NISQ optimization, hybrid quantum-classical systems, quantum MLOps, enterprise
  quantum AI architecture, quantum NLP, agentic quantum systems, and quantum fuzzy logic.
  Use this skill whenever the user asks about quantum machine learning, quantum neural networks,
  variational quantum algorithms, quantum computing for AI, NISQ devices, quantum advantage,
  hybrid quantum-classical pipelines, quantum AI architecture, quantum NLP, quantum RL,
  or any role combining quantum computing with ML/AI. Also triggers for: "implement QNN",
  "design quantum ML system", "quantum kernel SVM", "QAOA for optimization", "VQE tutorial",
  "quantum AI strategy", "quantum error mitigation", "quantum NLP", "quantum fuzzy logic",
  "quantum agentic AI", "quantum MLOps", or any request to build or explain quantum AI systems.
---

# Quantum AI & ML Engineering Workflow

Complete guide for six quantum AI roles from algorithm implementation to enterprise architecture.
Follow the role most relevant to the user's need.

---

## Current Status (2025) — Read First

```
TODAY (Simulators ✅ / Early Hardware ⚠️):
  ✅ QML on simulators (Qiskit, PennyLane, Cirq)
  ✅ VQE for small molecules (5–10 qubits)
  ✅ QAOA for combinatorial optimization
  ✅ Quantum kernel SVM
  ✅ Hybrid quantum-classical training

  ⚠️ Real hardware: 5–20 qubits, noisy, NISQ era
  ❌ Quantum advantage over classical (except narrow cases)
  ❌ Scalable QNN, quantum NLP, fault-tolerant QC

TIMELINE:
  2025–2027: NISQ era, 50–100 qubits, hybrid systems
  2027–2030: 1,000+ logical qubits (with error correction)
  2030+:     General-purpose quantum AI
```

Always benchmark against classical baseline. Always have classical fallback in production.

---

## Role 1: Quantum AI Engineer

### Core Responsibilities
- Design quantum circuits for ML tasks
- Implement variational quantum algorithms (VQA, VQE, QAOA)
- Optimize quantum gate depth
- Build quantum-classical hybrid systems
- Test on simulators + real hardware

### 1.1 Quantum Neural Network (QNN)

```python
from qiskit import QuantumCircuit
import numpy as np

class QuantumNeuralNetwork:
    def __init__(self, n_qubits=4, n_layers=2):
        self.n_qubits = n_qubits
        self.n_layers = n_layers
        self.n_params = n_qubits * n_layers

    def create_ansatz(self, params):
        """Parameterized circuit: H → RY/RZ layers → CX entanglement → measure"""
        qc = QuantumCircuit(self.n_qubits, self.n_qubits)
        for i in range(self.n_qubits):
            qc.h(i)                              # Superposition
        for layer in range(self.n_layers):
            for i in range(self.n_qubits):
                idx = layer * self.n_qubits + i
                qc.ry(params[idx], i)
                qc.rz(params[idx] * 0.5, i)
            for i in range(self.n_qubits - 1):  # CX ladder
                qc.cx(i, i + 1)
            qc.cx(self.n_qubits - 1, 0)         # Wrap-around
        qc.measure(range(self.n_qubits), range(self.n_qubits))
        return qc

    def parameter_shift_gradient(self, params, loss_fn):
        """Quantum gradient: ∂f/∂θ = [f(θ+π/4) - f(θ-π/4)] / (2·sin(π/4))"""
        grads = np.zeros(len(params))
        for i in range(len(params)):
            p_plus = params.copy(); p_plus[i] += np.pi / 4
            p_minus = params.copy(); p_minus[i] -= np.pi / 4
            grads[i] = (loss_fn(p_plus) - loss_fn(p_minus)) / (2 * np.sin(np.pi / 4))
        return grads
```

**Key design choices:**
- `n_qubits`: matches feature dimension after encoding
- `n_layers`: depth–accuracy tradeoff (more layers = expressive but noisy)
- Entanglement pattern: ladder (cheap) vs all-to-all (expensive)

### 1.2 Quantum Kernel Method

```python
class QuantumKernelMethod:
    """K(x1, x2) = |<ψ(x1)|ψ(x2)>|² — inner product in Hilbert space"""

    def encode_data(self, x, qc):
        """Angle encoding: θ_i = arcsin(x_i_normalized)"""
        x_norm = (x - x.min()) / (x.max() - x.min()) * 2 * np.pi
        for i in range(min(self.n_qubits, len(x))):
            qc.ry(x_norm[i], i)

    def compute_kernel(self, x1, x2, shots=1024):
        """Probability of |0...0⟩ = kernel value"""
        qc = QuantumCircuit(self.n_qubits, self.n_qubits)
        self.encode_data(x1, qc)
        # Apply inverse x1 encoding, then x2 encoding
        # K(x1,x2) = overlap probability
        qc.measure(range(self.n_qubits), range(self.n_qubits))
        # Execute and return counts.get('0'*n, 0) / shots
```

**Use case:** Drop-in kernel for classical SVM when classical kernels underperform.
Compute Gram matrix K[i,j] = kernel(X[i], X[j]) then pass to `sklearn.svm.SVC(kernel='precomputed')`.

### 1.3 QAOA (Combinatorial Optimization)

```python
class QAOA:
    """Quantum Approximate Optimization Algorithm
    Use for: Max-Cut, TSP, portfolio allocation, scheduling"""

    def create_qaoa_circuit(self, params, p=2):
        """
        Structure: H^n → [cost layer (RZZ) → mixer layer (RX)] × p
        params = [γ_0, β_0, γ_1, β_1, ...] length = 2p
        """
        qc = QuantumCircuit(self.n_qubits, self.n_qubits)
        for i in range(self.n_qubits):
            qc.h(i)
        for layer in range(p):
            gamma, beta = params[2*layer], params[2*layer+1]
            for i in range(self.n_qubits - 1):
                qc.rzz(2 * gamma, i, i+1)       # Cost Hamiltonian
            for i in range(self.n_qubits):
                qc.rx(2 * beta, i)              # Mixer Hamiltonian
        qc.measure(range(self.n_qubits), range(self.n_qubits))
        return qc

    def optimize(self, cost_func, maxiter=100):
        from scipy.optimize import minimize
        params = np.random.randn(self.n_params) * 0.1
        result = minimize(lambda p: self.evaluate(p, cost_func),
                         params, method='COBYLA', options={'maxiter': maxiter})
        return result.x, result.fun
```

### 1.4 VQE (Quantum Chemistry / Ground State)

```python
class VQE:
    """Variational Quantum Eigensolver
    Find ground state energy: E = <ψ|H|ψ>
    Hamiltonian format: [(coeff, 'ZZII'), (coeff, 'XZXI'), ...]"""

    def compute_energy(self, params, hamiltonian):
        total = 0
        for coeff, pauli_string in hamiltonian:
            total += coeff * self.measure_expectation(params, pauli_string)
        return total

    def measure_expectation(self, params, pauli_string):
        """Apply basis rotations per Pauli (X→RY(-π/2), Y→RX(π/2), Z→nothing)
        then measure parity: (-1)^(sum of bits)"""
```

**Encoding methods comparison:**

| Method | Qubits needed | Best for |
|--------|--------------|---------|
| Angle encoding | n | Low-dim features (n ≤ 20) |
| Amplitude encoding | log(n) | High-dim vectors (exponential compression) |
| Basis encoding | log(n) | Integer/discrete inputs |

---

## Role 2: Quantum ML Engineer (Production Systems)

### 2.1 Noise Mitigation (Critical for NISQ)

**Zero Noise Extrapolation (ZNE):**
```python
def zero_noise_extrapolation(circuit, cost_func, scale_factors=[1, 3, 5]):
    """Run at 3 noise levels → fit curve → extrapolate to zero noise"""
    results = []
    for scale in scale_factors:
        # Insert identity gates (Ry(0)) to scale noise
        scaled_circ = circuit.copy()
        for _ in range(scale - 1):
            for q in range(scaled_circ.num_qubits):
                scaled_circ.ry(0, q)
        results.append((scale, cost_func(scaled_circ)))
    # Fit log-linear: extrapolate scale→0
    scales = np.array([r[0] for r in results])
    costs = np.array([r[1] for r in results])
    coeffs = np.polyfit(scales, np.log(np.abs(costs) + 1e-6), 1)
    return np.exp(coeffs[1])  # Zero-noise estimate
```

**Other mitigation techniques:**
- **Dynamical decoupling**: H → delay → X → delay → X → delay → H (decouple from environment)
- **Symmetry verification**: average over symmetric circuit variants
- **Probabilistic error cancellation**: expensive but exact

### 2.2 Circuit Optimization

```python
# Always transpile before sending to real hardware
from qiskit.transpiler import transpile

optimized = transpile(
    circuit,
    backend=backend,
    optimization_level=3,       # 0–3, higher = more aggressive
    layout_method='sabre',      # Smart qubit placement
    routing_method='stochastic'
)

# Estimate error probability before running
def estimate_error(circuit):
    """P_error = 1 - (1-ε_1q)^n1 × (1-ε_2q)^n2"""
    n2q = sum(1 for inst in circuit.data if len(inst.qargs) == 2)
    n1q = circuit.size() - n2q
    return 1 - (1 - 1e-3)**n1q * (1 - 1e-2)**n2q
```

**Circuit depth targets:** NISQ era: depth < 50 (before decoherence). Minimize 2-qubit gates (10× more error than 1-qubit).

### 2.3 Hybrid Quantum-Classical Pipeline

```
Classical Input
  → StandardScaler + PCA (reduce to ≤ n_qubits features)
  → Quantum Feature Encoding (angle/amplitude)
  → Variational Quantum Circuit
  → Measurement (expectation values)
  → Classical Post-processing (SVM, MLP, logistic regression)
  → Prediction
```

**Production pattern:**
```python
class HybridPipeline:
    def __init__(self, quantum_circuit, classical_model):
        self.qc = quantum_circuit
        self.clf = classical_model

    def fit(self, X, y):
        X_quantum = self.qc.get_expectation_values(X)  # Quantum features
        self.clf.fit(X_quantum, y)

    def predict(self, X):
        X_quantum = self.qc.get_expectation_values(X)
        return self.clf.predict(X_quantum)
```

### 2.4 Quantum MLOps

**Version what to track in MLflow:**
- Quantum: circuit code (Git hash), gate count, circuit depth, estimated error prob, shots
- Classical: all standard ML metrics (AUC, precision, recall)
- Hardware: provider, device name, calibration date

**Deployment strategy:**
```
Quantum Simulator (full validation, 100% traffic)
  → Real Hardware Canary (5% traffic, smoke tests)
  → Real Hardware 100%
  → Fallback to classical ML if quantum job fails or latency >SLA
```

**Monitoring alerts:**
- Quantum job failure rate >1% → switch to classical fallback
- Circuit execution latency >SLA → scale or fallback
- Accuracy degradation >5% vs classical baseline → retrain
- Hardware calibration mismatch → re-transpile

---

## Role 3: Quantum AI Architect

### 3.1 Use Case Prioritization

```
Near-term (1–2 years, NISQ feasible):
  • Portfolio optimization (QAOA, 20–100 qubits)
  • Quantum kernel SVM (10–50 qubits)
  • Quantum-accelerated sampling

Medium-term (3–5 years):
  • Drug discovery / quantum chemistry (VQE, 50–1000 qubits)
  • Hybrid quantum-classical NLP features
  • Supply chain optimization

Long-term (5–10+ years, needs FTQC):
  • Scalable QNN replacing classical deep learning
  • Quantum NLP at scale
  • Grover-accelerated search at scale
```

### 3.2 Hardware Selection Matrix

| Provider | Qubits | 2Q Gate Error | Coherence | Best For | Access |
|----------|--------|--------------|-----------|---------|--------|
| IBM Q | 5–433 | 1–2% | 50–100 µs | Dev/research, free tier | Cloud |
| IonQ | 11–20 | 0.1% | >1 sec | High fidelity, small scale | Azure/AWS |
| Google Sycamore | 53 | 0.3–0.5% | 20–30 µs | Research, QAOA | Partners |
| Rigetti | 30 | 1% | 50 µs | Hybrid classical-quantum | Cloud |

**Selection rules:**
- High fidelity (few qubits) → IonQ
- Large scale research → Google / IBM Eagle/Heron
- Cost-effective dev → IBM Q free tier
- Production → multi-cloud active-active with failover

### 3.3 Enterprise Architecture Layers

```
Layer 1: Quantum Hardware (IBM/Google/IonQ, multi-cloud)
Layer 2: Quantum SDK (Qiskit / Cirq / PennyLane)
Layer 3: QML Libraries (Qiskit-ML / TF Quantum / PennyLane QML)
Layer 4: Classical ML Integration (PyTorch / TF / sklearn)
Layer 5: Orchestration (Airflow / Ray / Kubernetes)
Layer 6: Monitoring (Prometheus + Grafana + custom quantum metrics)
```

### 3.4 Cost Model

| Category | Annual Cost |
|----------|------------|
| Quantum hardware (IBM + IonQ) | $50K–500K |
| Classical GPU infrastructure | $200K–1M |
| Personnel (5 quantum + 10 ML engineers) | $3.5M–5M |
| **Total** | **$3.8M–6.5M** |

**ROI timeline:** Year 1 negative (build), Year 2 break-even, Year 3+ 300–500% ROI on successful use cases.

### 3.5 Risk Mitigation

| Risk | Probability | Mitigation |
|------|------------|-----------|
| Quantum advantage not proven | High | Always benchmark vs classical; classical fallback |
| Hardware noise/errors | High | ZNE + dynamical decoupling + error correction |
| Limited qubit availability | Medium | Multi-cloud strategy + approximate algorithms |
| Talent shortage | High | University partnerships + internal training ($5K/person/year) |

---

## Role 4: Quantum NLP Architect

### 4.1 Quantum Word Embeddings

**Classical:** Word2Vec, 300-dim vectors, O(d²) similarity
**Quantum:** Amplitude encode into log(d) qubits, O(log d) SWAP-test similarity

```python
# SWAP test: measure overlap |<ψ(x1)|ψ(x2)>|²
def swap_test(state1, state2, n_qubits):
    qc = QuantumCircuit(2*n_qubits + 1)
    qc.h(0)                                  # Ancilla superposition
    qc.initialize(state1, range(1, n_qubits+1))
    qc.initialize(state2, range(n_qubits+1, 2*n_qubits+1))
    for i in range(n_qubits):
        qc.cswap(0, i+1, n_qubits+i+1)      # Controlled SWAP
    qc.h(0)
    # P(ancilla=0) = (1 + |<ψ1|ψ2>|²) / 2 → solve for overlap
```

### 4.2 Application Timeline

| Application | Qubits Needed | Timeline | Status |
|------------|--------------|----------|--------|
| Word similarity (SWAP test) | 10–20 | 1–2 years | Research |
| Quantum kernel NLP | 10–50 | 1–2 years | Early research |
| Hybrid quantum-classical NLP | 50–100 | 3–5 years | Theoretical |
| Quantum attention mechanism | 100+ | 5–10 years | Theoretical |
| Full quantum language model | 1M+ | 10–15 years | Far future |

**Near-term realistic:** Use quantum kernels as drop-in feature maps for classical NLP classifiers (sentiment, topic classification).

---

## Role 5: Quantum Agentic AI Architect

### 5.1 Quantum Planning

**Classical A*:** O(b^d) — exponential blowup
**Grover's search:** O(√(b^d)) — quadratic speedup for action selection

```python
# Grover oracle marks optimal action in superposition
# Useful when action space is large and unstructured
```

### 5.2 Quantum Reinforcement Learning

```python
class QuantumRL:
    """Policy as parameterized quantum circuit"""
    def select_action(self, state, params):
        """Encode state → run VQC → measure → action probabilities"""
        qc = self.policy_circuit(state, params)
        probs = self.run(qc)
        return np.argmax(probs)  # Or sample for exploration

    def update_policy(self, gradient):
        """Parameter shift rule gradient → classical optimizer"""
```

**Quantum exploration advantage:** Superposition encodes multiple actions simultaneously — evaluate all branches before measurement collapse.

### 5.3 Multi-Agent Quantum Game Theory

**Classical Nash equilibrium** → suboptimal outcomes (Prisoner's Dilemma)
**Quantum strategy**: Entangled agents can achieve superclassical outcomes — shared Bell state allows coordination impossible classically.

---

## Role 6: Quantum Fuzzy Systems

**Core concept:** Encode fuzzy membership μ ∈ [0,1] as quantum amplitude via `θ = 2·arcsin(√μ)`, then `RY(θ)|0⟩` gives P(|1⟩) = μ.

| Classical Operation | Quantum Gate |
|--------------------|-------------|
| AND: min(μ_A, μ_B) | Controlled rotation, measure both qubits |
| OR: max(μ_A, μ_B) | Phase kickback + amplitude amplification |
| NOT: 1 - μ | X gate (bit flip) |

**Application:** Quantum fuzzy PID controller — quantum circuits adaptively tune K_p, K_i, K_d from real-time sensor fuzzy rules. Useful in robotics and process control under uncertainty.

---

## Learning Path

```
Phase 1 — Foundations (3–6 months):
  • Quantum mechanics basics (superposition, entanglement, measurement)
  • Qiskit fundamentals (IBM Quantum free tier)
  • Key algorithms: Grover's, Shor's, VQE

Phase 2 — QML Implementation (6–12 months):
  • Variational quantum algorithms (VQE, QAOA, VQC)
  • Quantum kernels and hybrid pipelines
  • Implement on Qiskit / PennyLane simulators
  • Resources: IBM Quantum Textbook (free), PennyLane demos

Phase 3 — Hardware & Production (6–12 months):
  • Error mitigation (ZNE, dynamical decoupling)
  • Circuit transpilation and optimization
  • Run on real hardware (IBM Q free tier)
  • Benchmark quantum vs classical

Phase 4 — Specialization (12+ months):
  • Choose: NLP / Agentic / Fuzzy / Chemistry / Finance
  • Contribute to Qiskit, PennyLane, or TF Quantum
  • Follow arXiv quant-ph/cs.LG
```

## Salary Reference (2025)

| Role | Range | Premium vs Classical |
|------|-------|---------------------|
| Junior Quantum Engineer | $150K–$200K | +20% |
| Senior Quantum Engineer | $250K–$350K | +30% |
| Quantum Architect | $350K–$500K+ | +40% |
| Quantum AI Researcher | $200K–$300K | +30–50% |

---

## Quick Implementation Checklist

Before any quantum ML project:
```
□ Define classical baseline (AUC, accuracy, latency)
□ Choose encoding method (angle / amplitude / basis)
□ Estimate qubit count needed (check vs hardware limits)
□ Estimate circuit error probability (depth × gate errors)
□ Plan classical fallback for production
□ Set up MLflow with quantum-specific metrics
□ Use simulator first — only move to hardware after validation
□ Run ZNE or dynamical decoupling on real hardware
□ Compare quantum output vs classical baseline before deploying
```
