import ipywidgets as widgets
from IPython.display import display

import random

class Three_Door():
    def __init__(self, init_num=3, max_num=10):

        # icons for information
        # introduction
        self.intro = widgets.HTML(
            value="Set number of doors, then click \"Game Start\" <br>"
        )

        self.game_proc = widgets.HTML(
            value=""
        )
        self.game_proc_str = "There's a car behind one door, goats behind other doors.<br>Guess which door that car behinded? (Click one door)"

        # message before switch or keep
        self.final_choice = widgets.HTML(
            value=""
        )
        self.final_str = "Keep same choice, or switch to door "

        # final choices buttons
        self.keep_butt = widgets.Button(
            description='Keep same choice!',
        )
        self.switch_butt = widgets.Button(
            description='Switch!',
        )
        self.keep_butt.layout.visibility = 'hidden'
        self.switch_butt.layout.visibility = 'hidden'

        final_items = [self.keep_butt, self.switch_butt]
        self.final_box = widgets.Box(final_items)

        # result of game
        self.result_msg = widgets.HTML(
            value=""
        )


        # numeric variables
        self.init_num = init_num
        min_num = init_num
        self.min_num = init_num
        self.max_num = max_num

        self.door_num_int = widgets.BoundedIntText(
            value=init_num,
            min=min_num,
            max=max_num,
            description='doors:',
            disabled=False
        )
        self.start_butt = widgets.Button(
            description='Game Start',
        )

        # door and car variables
        items = [widgets.Button(description="") for i in range(init_num)]
        self.door_box = widgets.Box(items)
        self.car_arr = [0] * max_num

        # set on_click in constructor
        self.start_butt.on_click(self.start_click)

        num_final_butt = len(self.final_box.children)
        for i in range( num_final_butt ):
            self.final_box.children[i].on_click(self.reveal_answer)

    def run_gui(self):
        display(self.intro, self.door_num_int, self.start_butt, self.game_proc, self.door_box, self.final_choice, self.final_box, self.result_msg)


    # -----------------------------------------------------

    def manage_goat(self, door_num, chosen_i):
        # global variable
        #     door_box
        self.door_box.children[chosen_i].layout = widgets.Layout(border='2px solid orange')

        # need random choose door opened
        # local variable
        goat_arr = [0] * (door_num-1)
        if_chose_car = False
        #print("in manage_goat")

        hide_idx = -1

        store_idx = 0
        for i in range(door_num):
            if self.car_arr[i] == 0:
                if i != chosen_i:
                    goat_arr[store_idx] = i
                    store_idx += 1
            elif self.car_arr[i] == 1:
                if i == chosen_i:
                    if_chose_car = True
                else:
                    hide_idx = i
        #print("goat open arr: ", goat_arr)
        open_num = store_idx

        # random choose goat to open if chose car
        if if_chose_car == True:
            goat_hide = random.randint(0, store_idx-1)
            hide_idx = goat_arr[goat_hide]
            #print("goat be hide: ", hide_idx)
            # swap hide goat to last
            temp = goat_arr[goat_hide]
            goat_arr[goat_hide] = goat_arr[store_idx-1]
            goat_arr[store_idx-1] = temp

            #print("after random choose, goat open arr: ", goat_arr)
            open_num -= 1

        for i in range(open_num):
            # reveal this door, it's goat behind
            open_idx = goat_arr[i]
            self.door_box.children[open_idx].description = "GOAT"
            self.door_box.children[open_idx].button_style='info'

        # ask final choice
        # store win lose information in keep and switch button

        # keep same door
        self.final_box.children[0].value = chosen_i
        self.final_box.children[0].layout.visibility = None

        # switch door
        self.final_box.children[1].value = hide_idx
        self.final_box.children[1].layout.visibility = None

        self.final_choice.value = self.final_str + " " +str(hide_idx+1) + "?"

        #print("keep same door: ", final_box.children[0].value)
        #print("switch to door: ", final_box.children[1].value)

        # end of manage_goat

    def door_open(self, b):
        # global variables
        #     door_num_int
        if self.start_butt.value == 0:
            idx= b.value
            #print("in door_open: ")
            door_num = self.door_num_int.value
            #print("door_num: ", door_num)
            #print("car_arr: ", car_arr)

            if_car = self.car_arr[idx]

            #if if_car == 1:
            #    print("there's car")
            #else:
            #    print("only goat")

            self.manage_goat(door_num, idx)
            # now some door opened, status changed
            self.start_butt.value = 1
        #else:
            #print("extra information already revealed")

    def generate_door(self, door_num):
        # initial all status
        #
        # global variables:
        #     door_box
        #     start_butt

        # re-generate car array
        for i in range(self.max_num):
            self.car_arr[i] = 0
        car_idx = random.randint(0, door_num-1)
        self.car_arr[car_idx] = 1

        #print("car arr: ", car_arr)

        # also re-generate door buttons
        items = [widgets.Button(description="Door "+str(i+1)) for i in range(door_num)]
        for i in range(door_num):
            #print("i: ", i)
            item_i = items[i]
            #print("item: ", item_i)
            item_i.value = i
            #print("item value: ", item_i.value)
            item_i.button_style = "primary"
            item_i.on_click(self.door_open)
        self.door_box.children = items

        # status all door closed
        self.start_butt.value = 0

        # disable final choice
        self.final_choice.value = ""
        num_final_butt = len(self.final_box.children)
        for i in range( num_final_butt ):
            self.final_box.children[1].value = -1
            self.final_box.children[i].layout.visibility = 'hidden'

        # clear result_msg
        self.result_msg.value = ""

    def start_click(self, b):
        # global variables
        #     door_num_int
        #     game_proc
        door_num = self.door_num_int.value
        self.generate_door(door_num)
        self.game_proc.value = self.game_proc_str

    #self.start_butt.on_click(start_click)

    # ---------------------------------------------------


    # final choice, win or not

    def reveal_door(self, door_i):
        # global variable:
        # car_arr

        idx = door_i.value

        behind_thing = "N/A"
        if self.car_arr[idx] == 0:
            behind_thing = "GOAT"
        else:
            behind_thing = "CAR"

        door_i.description = behind_thing


    def reveal_answer(self, b):
        # on_click for final button
        # global variables
        # door_box
        # car_arr
        # result_msg

        # check if win or not
        final_idx = b.value
        result_str = "N/A"
        if_win = False
        final_butt_style = "danger"

        if self.car_arr[final_idx] == 1:
            if_win = True
            final_butt_style = "success"
            result_str = "You win a car!"
        else:
            result_str = "Uh oh, it's a goat"


        # reveal rest 2 doors
        # win(success) or lose(danger) button style
        # other button switch to info style
        # for loop
        num_final_butt = len(self.final_box.children)
        for i in range( num_final_butt ):
            # get door button
            door_idx = self.final_box.children[i].value
            door_butt = self.door_box.children[door_idx]
            self.reveal_door(door_butt)

            if door_idx == final_idx:
                # final chose door
                door_butt.button_style = final_butt_style
                door_butt.layout = widgets.Layout(border='2px solid yellow')
            else:
                # door not final choice
                if if_win:
                    door_butt.button_style = "info"
                else:
                    door_butt.button_style = "warning"


        # update result_msg HTML value
        self.result_msg.value = result_str
