import pickle
from MachineLearning import nb_model,qda_model,mlp_model

# Save the trained models
with open('naive_bayes_model.pkl', 'wb') as f:
    pickle.dump(nb_model, f)

with open('qda_model.pkl', 'wb') as f:
    pickle.dump(qda_model, f)

with open('mlp_model.pkl', 'wb') as f:
    pickle.dump(mlp_model, f)
