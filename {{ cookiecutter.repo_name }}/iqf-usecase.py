import os

from iq_tool_box.experiments import ExperimentInfo, ExperimentSetup
from iq_tool_box.experiments.task_execution import PythonScriptTaskExecution

# from iq_tool_box.datasets import DSModifier, DSWrapper,DSModifier_jpg
# from iq_tool_box.metrics import ???
# from custom_iqf import CustomModifier, CustomMetric

#Define name of IQF experiment
experiment_name = "{{ cookiecutter.repo_name }}"

#Define path of the original(reference) dataset
data_path = "/iqf/???"

#DS wrapper is the class that encapsulate a dataset
ds_wrapper = DSWrapper(data_path=data_path)

#Define path of the training script
python_ml_script_path = 'custom_train.py'

#List of modifications that will be applied to the original dataset:

ds_modifiers_list = [
    # ???
]

# Task execution executes the training loop
# In this case the training loop is an empty script,
# this is because we evaluate the performance directly on the result of the modifiers.
task = PythonScriptTaskExecution( model_script_path = python_ml_script_path )

#Experiment definition, pass as arguments all the components defined beforehand
experiment = ExperimentSetup(
    experiment_name=experiment_name,
    task_instance=task,
    ref_dsw_train=ds_wrapper,
    ds_modifiers_list=ds_modifiers_list,
    repetitions=1
)

#Execute the experiment
experiment.execute()

# ExperimentInfo is used to retrieve all the information of the whole experiment. 
# It contains built in operations but also it can be used to retrieve raw data for futher analysis

experiment_info = ExperimentInfo(experiment_name)

_ = experiment_info.apply_metric_per_run(
    # ??? CustomMetric
    ds_wrapper.json_annotations,
)
