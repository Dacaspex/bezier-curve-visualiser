# bezier-curve-visualiser

This (mini) project is about the visualisations of n-dimensional bezier curves. It aims at rendering bezier curves and their 
properties such as slope and its construction. This project was programmed in python as a fun side project while I was bored
during public transport. 

![image of the program with 7 control points](https://github.com/Dacaspex/bezier-curve-visualiser/blob/master/docs/images/7_control_points.png)

## Installation instructions
1. Clone this repository
```bash
user:pc/projects$ git clone https://github.com/Dacaspex/bezier-curve-visualiser.git
```
2. Create and activate virtual environment
```
user:pc/projects$ python -m venv bezier-curve-visualiser
user:pc/projects$ cd bezier-curve-visualiser
user:pc/projects/bezier-curve-visualiser$ Scripts\activate
user:pc/projects/bezier-curve-visualiser$ pip install -r requirements.txt
```
3. Start program
```
user:pc/projects/bezier-curve-visualiser$ python main.py <nr of control points> <steps>
```

## Extra information
Bezier curves can be constructed by recursively create linear interpolations between n-1 dimensions and drawing the points. 
This can be visualised by clicking on the curve. This shows these constructions lines.

You can also take a drag the control points around. 

## Images
![image of the program with a construction curve](https://github.com/Dacaspex/bezier-curve-visualiser/blob/master/docs/images/7_control_points_construction.png)
![image of the program with more control points](https://github.com/Dacaspex/bezier-curve-visualiser/blob/master/docs/images/more_control_points.png)
