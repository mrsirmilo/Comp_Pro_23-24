from turtle import *

pensize(2)
speed(10)
bgcolor("blue")
color('white')

def snowflake_arm():
    for i in range(12):
        for j in range(2):
            forward(50)
            right(60)
            forward(50)
            right(120)
        right(30)

for _ in range(12):
    snowflake_arm()
    right(30)
