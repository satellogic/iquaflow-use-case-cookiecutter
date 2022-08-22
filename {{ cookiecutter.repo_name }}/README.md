# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}
____________________________________________________________________________________________________

## Requirements

* Docker
* nvidia-docker (for gpu usage)

## How to execute

1. `git clone git@github.com:satellogic/{{ cookiecutter.repo_name }}`
2. `cd {{ cookiecutter.repo_name }}`
3. The experiment process is executed with `python ./iqf-usecase.py`. A docker container is recomended as follows:
4. Build the docker image (\*\*\*). This will also download the dataset and weights

```bash
make build
```

5. Raise a running container

```bash
make container
```

6. As soon as the docker is running in background you can launch the following services whithin it:

    * Launch a jupyter lab server. (\**)

        ```bash
        make nb
        ```
        - To access the notebook from your browser in your local machine, access `localhost:[your_port]/?token=iqf` in your browser.
        - If the executions are launched in a server, make a tunnel from your local machine. `ssh -N -f -L localhost:[your_port]:localhost:[your_port] [remote_user]@[remote_ip]`  Otherwise skip this step.

    * Stops the jupyter server.

        ```bash
        make nbstop
        ```

    * Launch an mlflow server (\*)

        ```bash
        make mlf
        ```
        Then access it from your browser by using this address `localhost:5055`.
        Similar to the notebook server, you might need to make a tunnel.

    * To raise an interactive shell from our running container. (\*)

        ```bash
        make execsh
        ```
        
    * To run tests

        ```bash
        make test
        ```

    * Stop the docker container and everything that is running within it

        ```bash
        make stop
        ```

____________________________________________________________________________________________________

## Notes

   - The results of the IQF experiment can be seen in the MLflow user interface.
   - For more information please check the IQF_expriment.ipynb or IQF_experiment.py.
   - The default ports are `8888` for the notebookshell, `5000` for the mlflow and `9197`
   - (*)
        Additional optional arguments can be added. The dataset location is:
        >`DS_VOLUME=[path_to_your_dataset]`
   - To change the default port for the mlflow service:
     >`MLF_PORT=[your_port]`
   - (**)
        To change the default port for the notebook: 
        >`NB_PORT=[your_port]`
   - A terminal can also be launched by `make dockershell` with optional arguments such as (*)
   - (***)
        Depending on the version of your cuda drivers and your hardware you might need to change the version of pytorch which is in the Dockerfile where it says:
        >`pip3 install torch==1.7.0+cu110 torchvision==0.8.1+cu110 -f https://download.pytorch.org/whl/torch_stable.html`.
   - (***)
        The dataset is downloaded with all the results of executing the dataset modifiers already generated. This allows the user to freely skip the `.execute` as well as the `apply_metric_per_run` which __take long time__.
