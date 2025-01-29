# OpenDeception
OpenDeception: Benchmarking and Investigating AI Deceptive Behaviors via Open-ended Interaction Simulation

# introduction
We introduce OpenDeception, a novel evaluation framework. It features 50 real - world inspired scenarios, which encompass five types of deception, ranging from telecommunications fraud, product promotion, personal safety, emotional deception, to privacy stealing.

# code
We construct 50 different deception scenarios in `example.py` and then use `simulate.py` to generate dialogue data. In `simulate.py`, we set the system prompt for the agent, which includes the skills that the agent can use and the restrictions that must be followed. We evaluate 11 mainstream large language model (LLM) models by calling different LLM application programming interfaces (APIs). In the end, we present all the generated data in the `data` directory and classify it manually.

# data
In the data we present, the results are divided into three categories: English models, Chinese models, and multiple AIs deceiving the same user. The results of each type of data are also subdivided. "Fail" indicates a failed dialogue generation, "cheat_none" indicates a successful dialogue generation without any intention of deception, "cheat_fail" indicates a failed deception, "cheat_success" indicates a successful deception, and "rejection" indicates the occurrence of model rejection.
