
!pip install pgmpy
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define the Bayesian Network Structure (DAG)
model = BayesianNetwork([('Burglary', 'Alarm'), ('Earthquake', 'Alarm'), ('Alarm', 'JohnCalls'), ('Alarm', 'MaryCalls')])

# Step 2: Define Conditional Probability Distributions (CPDs)
cpd_burglary = TabularCPD(variable='Burglary', variable_card=2, values=[[0.999], [0.001]])
cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2, values=[[0.998], [0.002]])

# CPD for Alarm with parents Burglary and Earthquake
cpd_alarm = TabularCPD(variable='Alarm', variable_card=2,
                       values=[[0.95, 0.94, 0.29, 0.001],
                               [0.05, 0.06, 0.71, 0.999]],
                       evidence=['Burglary', 'Earthquake'], evidence_card=[2, 2])

cpd_johncalls = TabularCPD(variable='JohnCalls', variable_card=2,
                           values=[[0.90, 0.05], [0.10, 0.95]],
                           evidence=['Alarm'], evidence_card=[2])

cpd_marycalls = TabularCPD(variable='MaryCalls', variable_card=2,
                           values=[[0.70, 0.01], [0.30, 0.99]],
                           evidence=['Alarm'], evidence_card=[2])

# Step 3: Add CPDs to the model
model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_johncalls, cpd_marycalls)

# Step 4: Verify the model
assert model.check_model()

# Step 5: Perform Inference
inference = VariableElimination(model)

# Calculate P(Alarm=1 | Burglary=1, Earthquake=0)
result = inference.query(variables=['Alarm'], evidence={'Burglary': 1, 'Earthquake': 0})
print(result)
