# Three_Doors_Problem_Ipynb_GUI
Run three door problem interactively on Ipynb/jupyter notebook GUI

Here we choose ipywidgets package

# User guide

## Introduction
### Interactive GUI playing Three door problem on Colab



## Replicate on empty Colab

* 1 - Clone repository

    $\quad$ Open Colab and clone our repository

    ```bash
    !git clone https://github.com/BlackJack255/Three_Doors_Problem_Ipynb_GUI.git
    ```

    $\quad$ Then go to our repository folder
    ```bash
    %cd Three_Doors_Problem_Ipynb_GUI/
    %ls
    ```
    $\quad$ There should be our files
    <br>
    <br>

* 2 - Installation

    Required packages should already be installed in Colab

    If not installed, run following command

    ```bash
    !pip install ipywidgets
    ```



* 3 - Run and enjoy the GUI

    ```python
    from Three_Doors_GUI import Three_Doors

    three_door = Three_Doors(init_num=3, max_num=10)
    three_door.run_gui()
    ```

