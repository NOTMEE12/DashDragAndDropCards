# Drag and Drop cards example for Dash Plotly

https://github.com/user-attachments/assets/b1c50a16-1633-4718-8f57-1ced5e561a09

## Tools/Projects used:

We use [dragula](https://bevacqua.github.io/dragula/) for the dragging process, and
we use [dash mantine components](https://dash-mantine-components.com) for the looks.  
Many thanks to https://community.plotly.com/t/drag-and-drop-cards/42480/2

## Features:
- order change
- change cards column
- Change tables
- mirroring the database (the dimmed table below the normal one in the video)

## How to run?

First install all the packages required:
```commandline
pip install -r requirements.txt
```
then run:
```commandline
python main.py --theme="dark"
```
---

> [!NOTE]  
> To change the amount of columns, open `data.py` and change `column_amount` value.  
> To change the amount of cards per column, open `data.py` and change `card_amount_inside_columns`.  
> To change amount of tables, change `table_dimensions` in `data.py`.
