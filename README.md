# Three_Door_Problem_Ipynb_GUI
Run three door problem interactively on Ipynb/jupyter notebook GUI

Here we choose ipywidgets package

## User guide
### Interactive GUI playing Three door problem on Colab

* Open Colab

* Clone our repository

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



* Run and enjoy the GUI
```python
from Three_Doors_GUI import Three_Doors

three_door = Three_Doors(init_num=3, max_num=10)
three_door.run_gui()
```

