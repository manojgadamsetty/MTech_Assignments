# IS ZC444 Artificial Intelligence - Exam Preparation Guide

This guide is synthesized from:
- `AI/ArtificialIntelligence_ContactSession_1.pptx` to `AI/ArtificialIntelligence_ContactSession_5.pptx`
- `AI/AI CS 6.pdf`
- `AI/AI CS 7.pdf`
- `AI/IS ZC444 COURSE HANDOUT.docx`
- `AI/2025-2026_SEM_1_IS_ZC444_SS_ZC444_ARTIFICIAL_INTELLIGENCE_EC2_REGULAR_NS_21-09-2025_EN.pdf`

Text extractions are available under `AI/_extracted_text/`.

## 1. Course at a glance

Core flow of this course:
1. AI fundamentals and rational agents
2. Problem formulation and search
3. Knowledge representation and logical inference
4. Reasoning under uncertainty (probability, Bayes nets, HMM)
5. Learning methods (supervised, unsupervised, reinforcement)
6. Modern AI blocks (NN, deep learning, game search)

## 2. Module-wise concept map

### Module A: AI foundations and agents
- What is AI: acting humanly, thinking humanly, thinking rationally, acting rationally
- Rational agent model is central
- Agent = sensors + actuators + program + performance measure
- PEAS framework:
  - Performance measure
  - Environment
  - Actuators
  - Sensors
- Environment dimensions:
  - fully/partially observable
  - deterministic/stochastic/strategic
  - episodic/sequential
  - static/dynamic/semi-dynamic
  - discrete/continuous
  - single/multi-agent
- Agent types:
  - simple reflex
  - model-based reflex
  - goal-based
  - utility-based
  - learning agent

### Module B: Problem solving by search
- Problem components:
  - initial state
  - actions
  - transition model
  - goal test
  - path cost
- State space and search tree concepts
- Node fields: state, parent, action, depth, path cost
- Evaluation criteria:
  - completeness
  - optimality
  - time complexity
  - space complexity

#### Uninformed search
- BFS: complete, optimal (unit costs), memory heavy
- DFS: low memory, not optimal, may be incomplete in infinite depth
- Depth-limited DFS
- Iterative deepening: BFS completeness + DFS space efficiency
- Uniform-cost search: optimal with positive costs
- Bidirectional search: useful when goal is explicit and reverse operators exist

#### Informed search
- Heuristic `h(n)` as estimate to goal
- Greedy best-first: `f(n)=h(n)`
- A*: `f(n)=g(n)+h(n)`
- Admissible heuristic: never overestimates true cost
- Consistent heuristic: triangle inequality style condition

#### CSP and consistency
- Variables, domains, constraints
- Node consistency and arc consistency
- AC-3 algorithm for enforcing arc consistency
- Typical problems:
  - N-Queens
  - cryptarithmetic
  - map coloring
  - 8-puzzle abstraction

### Module C: Knowledge representation and reasoning

#### Propositional logic
- Syntax, semantics, models, entailment
- Connectives: NOT, AND, OR, implication, biconditional
- Inference rules:
  - Modus Ponens
  - Resolution
  - Unit resolution
- Model checking vs theorem proving

#### First-order logic
- Objects, predicates, functions, variables, quantifiers
- Universal and existential quantification
- Unification and substitutions
- CNF conversion idea for resolution-based reasoning

#### Inference strategies
- Forward chaining:
  - data-driven
  - start from known facts
  - apply rules to derive new facts
- Backward chaining:
  - goal-driven
  - start with query and prove subgoals recursively
- Prolog style reasoning connection

#### Wumpus world (common reasoning case)
- Sensor signals: stench, breeze, glitter, bump, scream
- Logical encoding of safe/unsafe cells
- PEAS specification and inference-based action selection

### Module D: Probability and uncertain reasoning
- Probability basics:
  - joint, marginal, conditional probability
  - independence and conditional independence
- Bayes rule:
  - `P(A|B) = P(B|A)P(A)/P(B)`
- Bayesian networks:
  - DAG over random variables
  - CPT at each node
  - factorized joint: `P(X1..Xn)=Product P(Xi|Parents(Xi))`
- Markov models and HMM:
  - hidden state, observation, transition model, sensor model
  - filtering, prediction, smoothing, most-likely state sequence (Viterbi)

### Module E: Learning methods

#### Supervised learning
- Classification and regression
- Linear regression and logistic regression basics
- Decision trees:
  - entropy
  - information gain
  - split selection
  - overfitting and pruning

#### Unsupervised learning
- Clustering concept
- K-means procedure and convergence intuition

#### Reinforcement learning
- Agent, state, action, reward, policy, value
- Q-learning update intuition

#### Neural and deep learning basics
- Perceptron and activation functions (threshold/sigmoid/ReLU)
- Multi-layer perceptron and backpropagation concept
- CNN intuition for images
- RNN intuition for sequences

## 3. High-priority definitions to memorize

- Rational agent
- Agent function vs agent program
- State space, node expansion, frontier
- Completeness, optimality, admissibility, consistency
- Entailment, model, soundness, completeness
- Unification, substitution, CNF
- Prior, posterior, likelihood
- Conditional independence
- Policy, value function, reward

## 4. Algorithm cheat sheet

### BFS
- Queue (FIFO), level-order expansion
- Good for shortest path in unweighted graphs

### DFS
- Stack/recursion (LIFO)
- Low memory, may get stuck deep

### UCS
- Priority by `g(n)`
- Dijkstra-like behavior

### A*
- Priority by `f(n)=g(n)+h(n)`
- Optimal with admissible heuristic

### AC-3
- Maintain queue of arcs
- Remove unsupported domain values
- Re-enqueue neighboring arcs after revision

### Forward chaining
- Repeatedly fire applicable rules from known facts

### Backward chaining
- Decompose target goal into required premises

### Minimax and alpha-beta
- Minimax for 2-player zero-sum perfect-information games
- Alpha-beta prunes branches that cannot change decision

## 5. Important formulas

- `f(n)=g(n)+h(n)`
- `P(A|B)=P(B|A)P(A)/P(B)`
- `P(X1..Xn)=Product P(Xi|Parents(Xi))`
- Entropy: `H(S)=-Sum p_i log2(p_i)`
- Information gain: `Gain(A)=H(parent)-Sum (|S_v|/|S|)H(S_v)`
- (Common ML metrics often expected):
  - accuracy, precision, recall, F1

## 6. Frequently asked exam patterns

1. PEAS for a new application and classify task environment properties.
2. Run BFS/DFS/UCS/A* on a graph and compare expansion order and final cost.
3. Check if a heuristic is admissible/consistent.
4. Build/trace AC-3 with domain pruning steps.
5. Convert natural language statements into propositional/FOL forms.
6. Perform entailment using truth table, resolution, or chaining.
7. Compute conditional probabilities using Bayes rule or Bayes net decomposition.
8. Construct a decision tree using entropy/information gain.
9. Solve game trees with minimax and show alpha-beta cutoffs.
10. HMM filtering-style belief updates from observations.

## 7. Contrast tables for fast revision

### BFS vs DFS vs UCS vs A*
- BFS: level-wise, optimal only for unit cost, high memory
- DFS: deep-first, low memory, not optimal
- UCS: cost-first, optimal for positive costs
- A*: cost + heuristic, usually best practical choice with a good heuristic

### Forward chaining vs backward chaining
- Forward: fact-driven, good when many queries
- Backward: goal-driven, good for specific query proofs

### Supervised vs unsupervised vs reinforcement
- Supervised: labeled data, predict labels/values
- Unsupervised: unlabeled data, discover structure
- Reinforcement: sequential decisions using rewards

## 8. Two-week revision plan

### Week 1
1. Days 1-2: Agents, PEAS, environment properties
2. Days 3-4: Uninformed search and complexity
3. Days 5-6: Informed search, A*, heuristics
4. Day 7: CSP and AC-3

### Week 2
1. Days 8-9: Propositional + FOL representation
2. Days 10-11: Forward/backward chaining + unification
3. Days 12-13: Probability, Bayes nets, HMM
4. Day 14: Full revision + mock problems + formula drill

## 9. One-day-before exam plan

1. 2-hour high-yield block: PEAS + A* + logic entailment.
2. 90-minute formula block: Bayes, entropy, information gain, A* terms.
3. 60-minute algorithm recall: AC-3, chaining, minimax/alpha-beta.
4. Light review and rest.

## 10. Known extraction limitations

- `AI/AI CS 7.pdf` has OCR/noise in some pages, so a few deep-learning lines may be garbled.
- Game-playing details appear in course scope but slide-level extraction may not fully include all worked examples.
- If you want, I can make a second pass topic-by-topic from the original files and generate a cleaner question bank.

## 11. Source-to-topic provenance

- Agents, PEAS, environment properties: `AI/ArtificialIntelligence_ContactSession_1.pptx`, `AI/ArtificialIntelligence_ContactSession_2.pptx`
- Search (uninformed/informed), CSP: `AI/ArtificialIntelligence_ContactSession_2.pptx`, `AI/ArtificialIntelligence_ContactSession_3.pptx`, `AI/ArtificialIntelligence_ContactSession_4.pptx`
- Propositional/FOL/chaining: `AI/ArtificialIntelligence_ContactSession_4.pptx`, `AI/ArtificialIntelligence_ContactSession_5.pptx`
- Probability/Bayes/HMM: `AI/AI CS 6.pdf`
- Learning/NN/deep learning: `AI/AI CS 7.pdf`
- Evaluation and exam policy: `AI/IS ZC444 COURSE HANDOUT.docx`, `AI/2025-2026_SEM_1_IS_ZC444_SS_ZC444_ARTIFICIAL_INTELLIGENCE_EC2_REGULAR_NS_21-09-2025_EN.pdf`
