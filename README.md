# Recommending system for FIFA18

Project done for a course Recommender Systems at University of Tampere.  
In collaboration with: [Karsten Paulussen](https://github.com/karsten0702)

One of the most popular feature in FIFA18 is the career mode, where user's goal is to improve his team and win as much competitions as possible. It is hard for the user to decide which players to buy to maximally improve their team by taking into account all different attributes. This reports presents an application that helps the user by both determining the worst player in the specific team and by recommending a list of players that are seen as possible replacement to improve the team. The application offers a basic graphic user interface to improve users' experience. The recommender was evaluated subjectively by both authors. We believe that both the way the worst player and the top five recommendations can be considered as good recommendations.

## Getting Started
Requirements:
- pandas
- scipy
- numpy
- sklearn
- flask

## Running the server

Open anaconda console and run the following commands. You need to run the second command (set... ) just the first time.

```
cd <path to the project>/reccomender_systems_project
set FLASK_APP=recommender_model.py
run flask
```

App is now available on (http://127.0.0.1:5000/).
