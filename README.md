# Title
By {your_name}

## Readme Outline
- [Project Description](#project_desc)  
    - [Scenario](#scenario)
    - [Goals](#goals)
        - [Deliverables](#deliverables)
    - [Project Dependencies](#dependencies)

- [About the data](#data)
    - Scope
    - Acquiring
    - Preparing
    - Data Dictionary
    - Key Findings

- [Project Planning](#plan)  
    - Hypothesis
    - Steps
    - Conclusion



# About the project <a name="project_desc"></a>

## Scenario

{Describe the use case or business context that is the driver behind the project}

> __Agile Story__  
    As a `wine producer`  
    I want `predictions of wine quality`  
    So that `I can make better wine`  

## Goals

- MVP Goal : Predict quality score using simple regession model using existing features. RMSE ~1

### Deliverables

- CodeUP Quality README file
- Report notebook
- Slide-driven presentation

## Reproducing this project

{Are there any special considerations one must take to run this project on another machine?  Usually yes.  The most common considerations have been filled out already below.}

### Dependencies

This project makes use of several technologies that will need to be installed
* [![python-shield](https://img.shields.io/badge/Python-3-blue?&logo=python&logoColor=white)
    ](https://www.python.org/)
* [![jupyter-shield](https://img.shields.io/badge/Jupyter-notebook-orange?logo=jupyter&logoColor=white)
    ](https://jupyter.org/)
* [![numpy-shield](https://img.shields.io/badge/Numpy-grey?&logo=numpy)
    ](https://numpy.org/)
* [![pandas-shield](https://img.shields.io/badge/Pandas-grey?&logo=pandas)
    ](https://pandas.pydata.org/)
* [![matplotlib-shield](https://img.shields.io/badge/Matplotlib-grey.svg?)
    ](https://matplotlib.org)
* [![seaborn-shield](https://img.shields.io/badge/Seaborn-grey?&logoColor=white)
    ](https://seaborn.pydata.org/)
* [![scipy-shield](https://img.shields.io/badge/SciPy-grey?&logo=scipy&logoColor=white)
    ](https://scipy.org/)
* [![sklearn-shield](https://img.shields.io/badge/_-grey?logo=scikitlearn&logoColor=white&label=scikit-learn)
    ](https://scikit-learn.org/stable/)

Dependencies can be installed quickly with just a few lines of code.
```
%pip install notebook
%pip install numpy
%pip install pandas
%pip install matplotlib
%pip install seaborn
%pip install scipy
%pip install sklearn
```


# About the data

{What is the source of the data?
What does the data represent? }

## Scope

{ How many records/columns? How many nulls? Does this project focus on a particular subset of the overall data? }

## Acquiring

{Describe how the data is acquired. Provide sources and links.  Were any additonal technologies or scripts used? List them here.}

## Preparing

{How was the data prepared for exploration?  Was any data fabricated through imputing or resampling?}

## Data Dictionary
---
| **Variable Name** | **Explanation** | **Unit** | **Values** |
| :---: | :---: | :---: | :---: |
| Fixed Acidity |  Acids that do not evaporate readily (Tartaric Acid) | g/L | Float |
| Volatile Acidity | Acids evaporate readily (Acetic acid) | g/L | Float |
| Citric Acid | level of Citric acid | g/L | Float |
| Residual Sugar | Sugar that remains after fermenation | g/L | Float |
| Chlorides | Sodium Chloride content | g/L | Float |
| Free Sulfur Dioxide | Levels of free, gaseous sulfur dioxide | mg/L | Float |
| Total Sulfur Dioxide | Total Level of Sulfur Dioxide | mg/L | Float |
| Density | Density in relation to water | g/cm^3 | Float |
| pH| Acidity of the wine | 1-14 | Float |
| Sulphates | Level of potassium sulfate | g/L | Float |
| Alcohol | Alcohol by Volume per wine | ABV% | Float |
| Quality |  The median value of at least 3 independent evualations by wine experts| 1-10 | Integer |



# Project Planning <a name="plan"></a>

Our project makes use of [Trello](https://trello.com/invite/b/QJuhQCLq/e6f31d6c42f14e6e43ac38b3d6775e58/winequality) to manage the individual steps and backlong of the project.


## Initial Hypotheses

- Sugar and alcohol content directly to correlates to wine density
- For white wines, the higher acid content the higher quality
- For red wines, residual sugar content lowers quality score
- Sulfates will have negative impact on quality for both
- High volitile acid content lowers quality for both
- White and red wines may need predicted separately
