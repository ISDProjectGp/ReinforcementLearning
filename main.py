from deterministic_state import DeterministicState
from policy_evaluation import PolicyEvaluation
from geo_matrix_generate import GeoMatrixGenerator

gen = GeoMatrixGenerator()
print(gen.create_reward_matrix())
print(gen.create_connectivity_matrix())