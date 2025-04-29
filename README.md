# The universal classification of sports

This is a crude attempt to come up with a simple method of sports classsification.

The goal is to evaluate whether the below set of three metrics that can adequately distribute the list of sporting endeavors across a 3d scatter plot. This enables discussions among people about their thoughts on different sports.

<!-- tag:BEGIN_IMAGE -->
![a screenshot of a 3d scatterplot graph showing many different sports arranged by axes of physical exertion, mental exertion, and scoring objectivitiy](./graph.png)
<!-- tag:END_IMAGE -->

We all know that chess, esports, and track *feel like* different "types" of sports, while others, such as hotdog eating competitions or the [Microsoft Excel World Championships](https://fmworldcup.com/excel-esports/) feel like they shouldn't count but its not easy to articulate  why.

This project creates a 3d plot to attempt to cluster the sports together by some intuitive metrics. It's closer to messing around than anything super serious. Maybe one day this project will grow up to be similar to [the cube rule](https://cuberule.com/).
<!-- tag:END_INTRO -->

## Scoring Definitions
For these we use a 12 point scale because its vary sub-divisible into integers that are easy to turn into fractions.

### Objectivity
How objective, and/or verifiable is the scoring, particularly to people in the audience with only a basic "elevator explaination" level of knowledge of how the sport is scored. 

**Examples:**

- **0** - depends completely on how the judges feel 
- **3** - mostly subjective or difficult for an audience member to come to the same score as the judges (figure skating, gymnastics, dance)
- **8** - Semi objective, who won is clearly measurable but based on something arbitrary, such as points or baskets, mostly verifiable by the audience or containing multiple ways to score points, which can make things harder to follow (american football)
- **9** - Semi objective, who won is clearly measurable but based on something arbitrary, such as points or baskets, but still easily verifiable by an audience member (soccer)
- **12** - totally objective and based on something measurable sich as distance, time, or another commonly used unit of science (crew, track, swim)


### Physical Exertion
How physically demanding is it (mental tougness included, otherwise this would effectively double-count). Think of things like:

- How much of the body is moving
- Is it bursts of intense energy, or sustained endurance
- How close to the body's physical limits are atheletes pushing it 
- possibly consider injury rates due to exertion
- 

**Examples:**

- **0** - not at all
- **1** - minimally, moving a finger (tetris)
- **2** - more movement, such as whole arm (chess)
- **3** - multiple limbs but still fairly sedentary (F1/driving)
- **5** - inconsistently active (golf) 
- **6** - fairly consistently active within a smallish area (ping pong)
- **6** - fairly consistently active within a larger area (tennis, badminton)
- **8** - fairly consistently active within an even larger area (american football, soccer)
- **10** - intense physical activity, possibly with some chance to rest (boxing, track)
- **12** - intense physical activity where you are really pushing the limits most of the time (tour de france, marathon, triathalon, swim)


### Mental Exertion
How mentally demanding is it. This includes skills such as:

- strategy
- planning
- considering moves of your opponent
- psyching out your opponent with false moves
- factoring in weather conditions
- how recoverable a mistake is
- how damaging a mistake could be

**Examples:**

- **0** - No strategy at all
- **3** - Some planning and strategy but not a ton (hot dog eating, sprinting, swim)
- **6** - A decent amount of strategy - such as where to best position yourself on the playfield, or how to psych out your opponent. Mistakes are costly but fairly recoverable. (basketball, soccer, football, ping pong)
- **9** - Fairly significant strategy. Mistakes could eaily cost you the win and are quite hard to recover from, possibly also including accounting for the  or conditions (pool, archery, etc)
- **12** - Strategy is everything and a wrong move at the start can easily cost you everything and be nearly impossible to recover from (chess, microsoft excel)


## Contributing to the site
The source code for this site is maintained [here](https://codeberg.org/MoralCode/sports-comparison). Issues and contributions are welcome.

<!-- tag:END_SCORING -->
## How to mess with this

1. open the `.csv` in libreoffice if you want
2. run `poetry install` to install python dependencies (requires poetry)
3. run `poetry run python3 sports.py` to see the data as a 3d graph
4. 3. run `poetry run python3 sports.py --html` to output an HTML see the data as a 3d graph