# Covid-19 (Coronovirus) analysis

## Overview
On March 11, 2020, the World Health Organization (WHO) declared the Covid-19 (a.k.a. new coronavirus) a pandemic. Since January 22, 2020, the Johns Hopkins CSSE maintains a [data repository](https://github.com/CSSEGISandData/COVID-19) to track the Covid-19 incidence worldwide. In order to understand a little bit how this disease will affect my country (Brazil), I performed some data analysis in this data.

For Portuguese speakers, I wrote a post in my blog about this analysis: [O que os dados dizem sobre o Coronavírus?](http://computacaointeligente.com.br/coolstuffs/analisando-coronavirus/)

## Some plots and tables got during the analysis (updated on March 20, 2020)
### Covid-19 worldwide (without China):
![covid-19-wo-chinha](figures/en/conf_cases_worldwide_no_china.png)

### Deaths worldwide (without China):
![deaths-wo-chinha](figures/en/deaths_worldwide_no_china.png)


### Top 10 infected countries
| Country/Region   |   Confirmed |   Deaths |   Recovered |   % Deaths  |    % Population |
|:-----------------|------------:|---------:|------------:|------------:|-----------:|
| China            |       81156 |     3249 |       70535 |    4.0034   | 0.00582712 |
| Italy            |       41035 |     3405 |        4440 |    8.29779  | 0.0679036  |
| Iran             |       18407 |     1284 |        5710 |    6.97561  | 0.0225024  |
| Spain            |       17963 |      830 |        1107 |    4.62061  | 0.0384451  |
| Germany          |       15320 |       44 |         113 |    0.287206 | 0.0184739  |
| US               |       13677 |      200 |           0 |    1.46231  | 0.00418043 |
| France           |       10947 |      243 |          12 |    2.21979  | 0.0163419  |
| Korea, South     |        8565 |       91 |        1540 |    1.06246  | 0.0165875  |
| Switzerland      |        4075 |       41 |          15 |    1.00613  | 0.0478481  |
| United Kingdom   |        2716 |      138 |          67 |    5.081    | 0.00408489 |

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

