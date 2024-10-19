# Drag and Drop cards example for Dash Plotly

[Video of the concept]()


## Tools/Projects used:

We use [dragula](https://bevacqua.github.io/dragula/) for the dragging process, and
we use [dash mantine components](https://dash-mantine-components.com) for the looks.  
Many thanks to https://community.plotly.com/t/drag-and-drop-cards/42480/2

## Known bugs:

- dynamic layout (changing the `dmc.Stack`'s children will raise an error if cards were drag-n-dropped.)

## How to run?

First install all the packages required:
```commandline
pip install -r requirements.txt
```
then run:
```commandline
python main.py --theme="dark"
```

> [!NOTE]  
> To change the amount of columns, open `data.py` and change `column_amount` value.  
> To change the amount of cards per column, open `data.py` and change `card_amount_inside_columns`.
