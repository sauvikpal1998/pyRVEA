import plotly
import plotly.graph_objs as go
from pyrvea.Problem.evonn_test_functions import EvoNNTestProblem
from pyrvea.Problem.evonn_problem import EvoNNModel
from pyrvea.Problem.evodn2_problem import EvoDN2Model
from pyrvea.Problem.testProblem import testProblem
from sklearn.neural_network import MLPRegressor
import numpy as np

# test_prob = EvoNNTestProblem("Three-hump camel")
# training_data_input, training_data_output = test_prob.create_training_data(
#     samples=150, method="random"
# )

# test_prob = testProblem('ZDT2', 30, 2, 0, 1, 0)
# training_data_input = np.random.rand(150,30)
# training_data_output = np.asarray([test_prob.objectives(x) for x in training_data_input])

test_prob = EvoNNTestProblem("Matyas")
training_data_input, training_data_output = test_prob.create_training_data(
    samples=250, method="random", seed=50
)
#
# model_evodn2 = EvoDN2Model(name="EvoDN2_" + test_prob.name)
# model_evodn2.set_params(
#         pop_size=500,
#         subnets=(6, 10),
#         num_nodes=10,
#         activation_func="sigmoid",
#         opt_func="llsq",
#         loss_func="rmse",
#         criterion="min_error",
#         logging=True,
#         plotting=True)
#
# model_evonn = EvoNNModel(name="EvoNN_" + test_prob.name)
# model_evonn.set_params(
#         num_nodes=20,
#         pop_size=500,
#         activation_func="sigmoid",
#         opt_func="llsq",
#         loss_func="rmse",
#         criterion="akaike_corrected",
#         logging=True,
#         plotting=True)

# model_evodn2.fit(training_data_input, training_data_output)
# model_evonn.fit(training_data_input, training_data_output)

mlp_reg = MLPRegressor(max_iter=10000, n_iter_no_change=100)
mlp_reg.fit(training_data_input, training_data_output)
mlp_reg_y_pred = mlp_reg.predict(training_data_input)

trace0 = go.Scatter(x=mlp_reg_y_pred, y=training_data_output, mode="markers")
trace1 = go.Scatter(x=training_data_output, y=training_data_output)
data = [trace0, trace1]
plotly.offline.plot(
        data,
        filename="MLP Regressor " + test_prob.name
                 + ".html",
        auto_open=True,
)


# test_prob = EvoNNTestProblem("Matyas")
# training_data_input, training_data_output = test_prob.create_training_data(
#     samples=250, method="random"
# )
#
# model_evodn2.fit(training_data_input, training_data_output)
# model_evonn.fit(training_data_input, training_data_output)
#
# test_prob = EvoNNTestProblem("Himmelblau")
# training_data_input, training_data_output = test_prob.create_training_data(
#     samples=250, method="random"
# )
#
# model_evodn2.fit(training_data_input, training_data_output)
# model_evonn.fit(training_data_input, training_data_output)
#
# test_prob = EvoNNTestProblem("Rastigrin", num_of_variables=2)
# training_data_input, training_data_output = test_prob.create_training_data(
#     samples=250, method="random"
# )
#
# model_evodn2.fit(training_data_input, training_data_output)
# model_evonn.fit(training_data_input, training_data_output)
#
# test_prob = EvoNNTestProblem("Three-hump camel")
# training_data_input, training_data_output = test_prob.create_training_data(
#     samples=250, method="random"
# )
#
# model_evodn2.fit(training_data_input, training_data_output)
# model_evonn.fit(training_data_input, training_data_output)
#
# test_prob = EvoNNTestProblem("Goldstein-Price")
# training_data_input, training_data_output = test_prob.create_training_data(
#     samples=250, method="random"
# )
#
# model_evodn2.fit(training_data_input, training_data_output)
# model_evonn.fit(training_data_input, training_data_output)
#
# test_prob = EvoNNTestProblem("LeviN13")
# training_data_input, training_data_output = test_prob.create_training_data(
#     samples=250, method="random"
# )
#
# model_evodn2.fit(training_data_input, training_data_output)
# model_evonn.fit(training_data_input, training_data_output)
#
# test_prob = EvoNNTestProblem("SchafferN2")
# training_data_input, training_data_output = test_prob.create_training_data(
#     samples=250, method="random"
# )
#
# model_evodn2.fit(training_data_input, training_data_output)
# model_evonn.fit(training_data_input, training_data_output)
#
# # ZDT 1 & 2
# test_prob = testProblem('ZDT2', 30, 2, 0, 1, 0)
# np.random.seed(30)
# training_data_input = np.random.rand(250, 30)
# training_data_output = np.asarray([test_prob.objectives(x) for x in training_data_input])
#
# f1_training_data_output = training_data_output[:, 0]
# f2_training_data_output = training_data_output[:, 1]
#
# mlp_reg = MLPRegressor(max_iter=10000, n_iter_no_change=100)
# mlp_reg.fit(training_data_input, f1_training_data_output)
# mlp_reg_y_pred = mlp_reg.predict(training_data_input)
#
# trace0 = go.Scatter(x=mlp_reg_y_pred, y=f1_training_data_output, mode="markers")
# trace1 = go.Scatter(x=f1_training_data_output, y=f1_training_data_output)
# data = [trace0, trace1]
# plotly.offline.plot(
#         data,
#         filename="MLP Regressor " + test_prob.name + "_f1"
#                  + ".html",
#         auto_open=True,
# )
#
# mlp_reg.fit(training_data_input, f2_training_data_output)
# mlp_reg_y_pred = mlp_reg.predict(training_data_input)
#
# trace0 = go.Scatter(x=mlp_reg_y_pred, y=f2_training_data_output, mode="markers")
# trace1 = go.Scatter(x=f2_training_data_output, y=f2_training_data_output)
# data = [trace0, trace1]
# plotly.offline.plot(
#         data,
#         filename="MLP Regressor " + test_prob.name + "_f2"
#                  + ".html",
#         auto_open=True,
# )
#

#
# model_evodn_f1 = EvoDN2Model(name="EvoDN2_" + test_prob.name + "_f1")
# model_evodn_f1.set_params(
#         pop_size=500,
#         subnets=(6, 10),
#         num_nodes=10,
#         activation_func="sigmoid",
#         opt_func="llsq",
#         loss_func="rmse",
#         criterion="min_error",
#         logging=True,
#         plotting=True)
#
# model_evodn_f2 = EvoDN2Model(name="EvoDN2_" + test_prob.name + "_f2")
# model_evodn_f2.set_params(
#         pop_size=500,
#         subnets=(6, 10),
#         num_nodes=10,
#         activation_func="sigmoid",
#         opt_func="llsq",
#         loss_func="rmse",
#         criterion="min_error",
#         logging=True,
#         plotting=True)
# model_evodn_f1.fit(training_data_input, f1_training_data_output)
# model_evodn_f2.fit(training_data_input, f2_training_data_output)
# #
# test_prob = testProblem('ZDT2', 30, 2, 0, 1, 0)
# training_data_input = np.random.rand(250, 30)
# training_data_output = np.asarray([test_prob.objectives(x) for x in training_data_input])
#
# f1_training_data_output = training_data_output[:, 0]
# f2_training_data_output = training_data_output[:, 1]
#
# model_evodn_f1.fit(training_data_input, f1_training_data_output)
# model_evodn_f2.fit(training_data_input, f2_training_data_output)
