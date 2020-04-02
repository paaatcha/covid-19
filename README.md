# Covid-19 (Coronovirus) analysis

## Overview
On March 11, 2020, the World Health Organization (WHO) declared the Covid-19 (a.k.a. new coronavirus) a pandemic. Since January 22, 2020, the Johns Hopkins CSSE maintains a [data repository](https://github.com/CSSEGISandData/COVID-19) to track the Covid-19 incidence worldwide. In order to understand a little bit how this disease will affect my country (Brazil), I performed some data analysis in this data.

For Portuguese speakers, I wrote a post in my blog about this analysis: [O que os dados dizem sobre o Coronavírus?](http://computacaointeligente.com.br/coolstuffs/analisando-coronavirus/)

## Some plots and tables got during the analysis (updated on April 2, 2020)
### Covid-19 worldwide (without China):
![covid-19-wo-chinha](figures/en/conf_cases_worldwide_no_china.png)

### Deaths worldwide (without China):
![deaths-wo-chinha](figures/en/deaths_worldwide_no_china.png)


### Top 10 infected countries
| Country/Region   |   Confirmed |   Deaths |   % Deaths  |% Population|
|:-----------------|------------:|---------:|------------:|-----------:|
| US               |      213372 |     4757 |     2.22944 | 0.065218   |
| Italy            |      110574 |    13155 |    11.897   | 0.182975   |
| Spain            |      104118 |     9387 |     9.01573 | 0.222837   |
| China            |       82361 |     3316 |     4.02618 | 0.00591364 |
| Germany          |       77872 |      920 |     1.18143 | 0.0939032  |
| France           |       57749 |     4043 |     7.00099 | 0.086209   |
| Iran             |       47593 |     3036 |     6.37909 | 0.058182   |
| United Kingdom   |       29865 |     2357 |     7.89218 | 0.0449172  |
| Switzerland      |       17768 |      488 |     2.74651 | 0.208629   |
| Turkey           |       15679 |      277 |     1.76669 | 0.0190465  |

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

