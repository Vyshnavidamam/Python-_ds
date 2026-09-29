p_disease = 0.01
p_positive_given_disease = 0.90
p_positive_given_no_disease = 0.05
p_positive = (
 p_positive_given_disease * p_disease
 + p_positive_given_no_disease * (1 - p_disease)
)
p_disease_given_positive = (
 p_positive_given_disease * p_disease / p_positive
)
print("Probability:", p_disease_given_positive)