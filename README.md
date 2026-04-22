


# Python Data Cleaning Cookbook

<a href="https://www.packtpub.com/product/python-data-cleaning-cookbook/9781800565661?utm_source=github&utm_medium=repository&utm_campaign=9781800208919"><img src="https://static.packt-cdn.com/products/9781800565661/cover/smaller" alt="Learn Amazon SageMaker" height="256px" align="right"></a>

This is the code repository for [Python Data Cleaning Cookbook](https://www.packtpub.com/product/python-data-cleaning-cookbook/9781800565661?utm_source=github&utm_medium=repository&utm_campaign=9781800565661), published by Packt.

**Modern techniques and Python tools to detect and remove dirty data and extract key insights**

## What is this book about?
Getting clean data to reveal insights is essential, as directly jumping into data analysis without proper data cleaning may lead to incorrect results. This book shows you tools and techniques that you can apply to clean and handle data with Python. You'll begin by getting familiar with the shape of data by using practices that can be deployed routinely with most data sources. Then, the book teaches you how to manipulate data to get it into a useful form. You'll also learn how to filter and summarize data to gain insights and better understand what makes sense and what does not, along with discovering how to operate on data to address the issues you've identified. 

Moving on, you'll perform key tasks, such as handling missing values, validating errors, removing duplicate data, monitoring high volumes of data, and handling outliers and invalid dates. Next, you'll cover recipes on using supervised learning and Naive Bayes analysis to identify unexpected values and classification errors, and generate visualizations for exploratory data analysis (EDA) to visualize unexpected values. Finally, you'll build functions and classes that you can reuse without modification when you have new data.

By the end of this Python book, you'll be equipped with all the key skills that you need to clean data and diagnose problems within it.

This book covers the following exciting features: 
* Find out how to read and analyze data from a variety of sources
* Produce summaries of the attributes of data frames, columns, and rows
* Filter data and select columns of interest that satisfy given criteria
* Address messy data issues, including working with dates and missing values
* Improve your productivity in Python pandas by using method chaining
* Use visualizations to gain additional insights and identify potential data issues
* Enhance your ability to learn what is going on in your data
* Build user-defined functions and classes to automate data cleaning

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1800565666) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders.

The code will look like the following:
```
landtemps = pd.read_csv('data/landtempssample.csv',
    names=['stationid','year','month','avgtemp','latitude',
           'longitude','elevation','station','countryid','country'],
    skiprows=1,
    parse_dates=[['month','year']],
    low_memory=False)

```

**Following is what you need for this book:**
This book is for anyone looking for ways to handle messy, duplicate, and poor data using different Python tools and techniques. The book takes a recipe-based approach to help you to learn how to clean and manage data. Working knowledge of Python programming is all you need to get the most out of the book.

With the following software and hardware list you can run all code files present in the book (Chapter 1-10).

### Software and Hardware List

| Chapter  | Software required                                                                    | OS required                        |
| -------- | -------------------------------------------------------------------------------------| -----------------------------------|
| 1 - 10   |   Python 3.6+ (Jupyter Notebook) / Google Colab                               				| Windows, Mac OS X, and Linux (Any) |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781800565661_ColorImages.pdf).

## Errata
 
* Page 79, Step 5: **unqiue** _should be_ **unique**

### Related products <Other books you may enjoy>
* Practical Data Analysis Using Jupyter Notebook [[Packt]](https://www.packtpub.com/product/practical-data-analysis-using-jupyter-notebook/9781838826031) [[Amazon]](https://www.amazon.com/dp/B08BNDJJH6)

* Hands-On Exploratory Data Analysis with Python [[Packt]](https://www.packtpub.com/product/hands-on-exploratory-data-analysis-with-python/9781789537253) [[Amazon]](https://www.amazon.com/dp/1789537258)

## Get to Know the Author
**Michael Walker**  has worked as a data analyst for over 30 years at a variety of educational institutions. He has also taught data science, research methods, statistics, and computer programming to undergraduates since 2006. He generates public sector and foundation reports and conducts analyses for publication in academic journals.


### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781800565661">https://packt.link/free-ebook/9781800565661 </a> </p>