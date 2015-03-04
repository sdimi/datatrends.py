
## About 
Datatrends is a reporting tool for detecting trends in big datasets. Your *input* is one or multiple datasets (csv, txt etc.)  The columns should have the same lenght and may contain various datatypes, the tool picks only the numerical ones. The *output* is a pdf report with graphs of the correlated columns accompanied by descriptive statistics. The type of the regression line can be linear, quatradic or cubic and is automatically estimated by the R2 measure. 

### Run 
```python
python analyzer.py dataset.csv
#python3 recommended
```

#### Dependencies
* numpy
* scipy
* matplotlib

#### The output report (pdf)
![PICTURE](http://i.imgur.com/qXcTthf.png)
***

#### Authors
* [Basilis Charalampakis](https://github.com/charbgr)
* [Dimitris Spathis](https://github.com/sdimi)


