<h1 align="center">Welcome to IBW Dataset 👋</h1>
<p>
  <a href="ibw-dataset.herokuapp.com" target="_blank">
    <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
  </a>
</p>

# Introduction
<p align="center">
  <a href="ibw-dataset.herokuapp.com" target="_blank">
    <img alt="Documentation" src="https://content.indiainfoline.com/_media/iifl/img/article/2016-11/25/full/1480065591-6229.jpg" />
  </a>
</p>
Internet has grown a lot in the last few years. According to The Telecom Regulatory Authority
of India (TRAI), the number of Internet subscribers in India increased from 1,160.52 million at the end of Jun-20 to 1,168.66 million at the end of Sep-20, and is
now worlds third largest internet user. Even social networking sites like Facebook have over 290 million active
users in India (Times of India).<br>
<br>Thus, detection of inappropriate use of language on internet which might harm
the user is of utmost importance. With the advent of technology many devices and operating systems are now
supporting Indian Languages, and hence there is a need for an insult detection system in Indian Languages. Insults act as a repelling
force for new users and also prevent regular users to participate in discussions in future. It is also frustrating to
find foul language when looking for something. It is also not possible to have a human moderator to monitor this
enormous amount of data.
<br><br>

We focus on words that may be insulting or harmful for other person. Insults can be of many types
like racial slurs, reference to handicap, foul language and provocative words. The indirect insults like sarcasm,
disguise and crude words are not identified by the method. so our team collected data from diffrent users in diffrent languages from this [ form ](https://ibw-dataset.herokuapp.com)


# Related Works

Various Datasets have been created for the English language. For Hindi, there was no such database we manually created
one. We tackled this problem in different ways.

* Collected Abusive words by web-scrapping  from diffrent websites (1000 entries)

* Created a list of bad words in Hindi, procured from various Hindi websites

* Collected words from various Hindi pdfs and forums(600 entries).

* Used Google Translate to convert the available Kaggle’s English dataset into Hindi(1000 entries) and
then manually modified it to retain the context.

*  Around 70% of the input is negative strings(non-insults).

* Did a Deep down study on how Google Translate works for English to Hindi

# Google Translate: a Study

We used Google Translate to convert English dataset into Hindi. As opposed to what one might expect with
Google, it is not so awesome. It has its limitations but can at least help the user to understand the general
meaning of a foreign text. Some languages produce better results than others, and works especially well when the
target language is English and source language is one of the languages of European Union. The following were
our conclusions from the study we did on English to Hindi translation according to the general results.<br> 

# About Dataset

The IBW dataset is an acronym that stands for the Indian Bad Words dataset. It is a dataset of thousands of abusive words which will be available in 14 different Indian languages.

### [CSV](ibw-dataset.herokuapp.com) [ 23.6MB ]

### [HDF5](https://osg-ny2.paperspace.io/tekeun9hs/tekeun9hs/datasets/dsrgt5fydni1tep/versions/1o9e4wj/data/ibw.h5?AWSAccessKeyId=7FZOXOZIC1MWW1TW4LUG&Expires=1622033164&Signature=PXnFin%2FW6Ct0VXMz9pz%2F9DWYQNs%3D) [ 25.1MB  ]

### [Text](https://osg-ny2.paperspace.io/tekeun9hs/tekeun9hs/datasets/dsr3kni6g9kpshm/versions/jnuu5iy/data/IBW.txt?AWSAccessKeyId=7FZOXOZIC1MWW1TW4LUG&Expires=1622033324&Signature=3g0pNqA8%2BLjJoi5VX1IbDCtO5nE%3D)   [ 57.1kB ]




## About Data collection methodology

Data was collected from diffrent sources and website through web scrapping and also hundredes of users contributed to build this dataset.


### Description of the data

_data contains ( ibw.csv, ibw.h5, ibw.txt)

```
Root
├── _data
│   ├── ibw.csv
│   ├── ibw.h5
│   ├── IBW.txt
│   ├── index.html
│   └── Languages
│       ├── language_0.csv
│       ├── language_1.csv
│       ├── language_2.csv
│       └── language_N.csv // N = Number of Languages
├── docs
│   ├── _config.yml
│   └── index.md
├── notebooks
│   └── preprocessing.ipynb
├── README.md
└── synthetic data generation
    └── DataGen.py
```

### And file formats

data includes(.csv, .txt, .h5).
```
-39 Files, format csv.
-1 Text, format txt.
-1 File, format h5.
```

# Overview of Data

* Most of Data is from Hindi langauges Because Hindi 
is majorly spoken in India 

  - ![](./wc.png)

* some words are so much common and easy to find

- ![](./graph1.jpg)
## Online Repository link

* [DataRepository](https://www.kaggle.com/datasets) - Link to the data repository.

## 👤 Author

* **authorname** - *Initial work* - [Vivek Patel](https://github.com/vivolscute)

* **Data Collector** - *Web Development* - [Hunaid nakhuda](https://github.com/hunaid-nakhuda)

See also the list of [contributors](https://github.com/vivolscute/INDIAN_Bad_Words_Dataset/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [https://www.youswear.com](https://www.youswear.com)
* [https://pypi.org/project/better-profanity/](https://pypi.org/project/better-profanity/)
* [https://www.scribd.com/doc/136875132/Punjabi-Insults](https://www.scribd.com/doc/136875132/Punjabi-Insults)


## Show your support

Give a ⭐️ if [this project](https://github.com/vivolscute/INDIAN_Bad_Words_Dataset) helped you!
