# Covid-19 (Coronovirus) analysis

## Overview
On March 11, 2020, the World Health Organization (WHO) declared the Covid-19 (a.k.a. new coronavirus) a pandemic. Since January 22, 2020, the Johns Hopkins CSSE maintains a [data repository](https://github.com/CSSEGISandData/COVID-19) to track the Covid-19 incidence worldwide. In order to understand a little bit how this disease will affect my country (Brazil), I performed some data analysis in this data.

For Portuguese speakers, I wrote a post in my blog about this analysis: [O que os dados dizem sobre o Coronavírus?](http://computacaointeligente.com.br/coolstuffs/analisando-coronavirus/)

## Some plots and tables got during the analysis (updated on May 1, 2020)
### Covid-19 worldwide (without China):
![covid-19-wo-chinha](figures/en/conf_cases_worldwide_no_china.png)

### Deaths worldwide (without China):
![deaths-wo-chinha](figures/en/deaths_worldwide_no_china.png)


### Top 10 infected countries
| Country/Region   |   Confirmed |   Deaths |   % Deaths  |% Population|
|:-----------------|------------:|---------:|------------:|-----------:|
| US               |      188172 |     3873 |     2.05822 | 0.0575155  |
| Italy            |      105792 |    12428 |    11.7476  | 0.175062   |
| Spain            |       95923 |     8464 |     8.82374 | 0.205298   |
| China            |       82279 |     3309 |     4.02168 | 0.00590775 |
| Germany          |       71808 |      775 |     1.07927 | 0.0865909  |
| France           |       52827 |     3532 |     6.68597 | 0.0788613  |
| Iran             |       44605 |     2898 |     6.49703 | 0.0545292  |
| United Kingdom   |       25481 |     1793 |     7.03662 | 0.0383236  |
| Switzerland      |       16605 |      433 |     2.60765 | 0.194973   |
| Turkey           |       13531 |      214 |     1.58155 | 0.0164371  |

### Comparing confirmed cases around the world

![comparing-countries](figures/en/conf_cases_countries.png)

### Early cases in Brazil
![early-br](figures/en/early_cases_conf_brazil.png)

### Comparing early cases around the world
![early-compare](figures/en/conf_early_cases_countries.png)


## Running the code
The analysis was coded in Python using Jupyter Notebook. To install the requirement:

`pip install requirements.txt `

First, run the `get_data.ipynb` script to get the most updated data from the [Johns Hopkins repository](https://github.com/CSSEGISandData/COVID-19).

Next, run the `analysis.ipynb` code and have fun

## Other analysis
Some people are also working on this data and providing some insightful analysis on Kaggle. You may want to check them as well:
- [COVID-19 - Analysis, Viz, Prediction & Comparisons](https://www.kaggle.com/imdevskp/covid-19-analysis-viz-prediction-comparisons)
- [Coronavirus (COVID-19) Visualization & Prediction](https://www.kaggle.com/therealcyberlord/coronavirus-covid-19-visualization-prediction)
- [Novel Corona Virus 2019 Dataset](https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset)



**If you find some bug or have any further question please let me know**

