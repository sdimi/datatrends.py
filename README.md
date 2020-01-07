
## About 

Uni project for the Big Data course.

Datatrends is a reporting tool for detecting trends in big datasets. Your *input* is one or multiple datasets (csv, txt etc.)  The columns should have the same length and may contain various datatypes; the tool picks only the numerical ones. The *output* is a pdf report with scatterplot graphs of the correlated columns accompanied by descriptive statistics. The type of the regression line can be linear, quatradic or cubic and is automatically estimated by the R-squared measure. 

### Run 
```python
python analyzer.py dataset.csv
#python3 recommended
```
### Example
[This dataset](https://github.com/sdimi/datatrends.py/blob/master/test%20datasets/advertising.csv) produces [this pdf](https://github.com/sdimi/datatrends.py/blob/master/sample%20report.pdf?raw=true)

#### Dependencies
* numpy
* scipy
* matplotlib

#### The output report (pdf)
![PICTURE](http://i.imgur.com/wvBHKgK.jpg)
***

#### Authors
* [Basilis Charalampakis](https://github.com/charbgr)
* [Dimitris Spathis](https://github.com/sdimi)


