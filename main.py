from deterministic_state import DeterministicState
from policy_evaluation import PolicyEvaluation

state = DeterministicState(5,"first")
state.create_default_reward_matrix()
state.print_state_machine_diagram()
PolicyEvaluation(state).execute()