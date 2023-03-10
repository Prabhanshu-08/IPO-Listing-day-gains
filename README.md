# IPO-Listing-day-gains


![IPO](https://user-images.githubusercontent.com/88246010/223772397-dbdcbea8-467e-45fe-a43f-75c23ebece74.gif)


**What is an IPO and why companies launch IPOs?**

Whenever a company becomes a Public company from a private company it has to get listed on Indian Stock Exchanges(NSE or BSE) before getting listed companies come up with IPOs to raise money from general public(Retail Investors), Qualified Institutional Investors(QII), and Non Institutional Investors(NII). An IPO allows a company to raise equity capital from public investors. The transition from a private to a public company can be an important time for private investors to fully realize gains from their investment as it typically includes a share premium for current private investors.

**Performance Of Indian IPOs**
![image](https://user-images.githubusercontent.com/88246010/222199594-76508b2a-fae0-4ac6-a886-a32512e8aab9.png)


**Motivation of Project**

The project is build to earn some profit from these IPOs. The gains that an IPO will have on listing day(the day when company gets listed on stock exchange usually after 7-8 days later after launch of IPO) can be predicted with the help of regression machine learning models. The actual value of the gains depends on various micro economic factors and can never be predicted accurately. But a close and actionable value can be predicted by analyzing the particiaption of people in various categories that is RI, QII and NII. If an IPO is subscribed(number of people applying for IPO) in good numbers by all three categories then probabillity of a good listing day gains increases. Based on this logic this project is made.


**Data Source**

* [MoneyControl](https://www.moneycontrol.com/)

* [Chittorgarh](https://www.chittorgarh.com/)


**Build With**
1. Pandas
2. Numpy
3. Matplotlib
4. Seaborn
5. Sklearn
6. CatBoost
7. XgBoost
8. AdaBoost

**Selecting The Best Model**
![image](https://user-images.githubusercontent.com/88246010/222204973-c70c4be7-21c6-41d0-82e1-aeb11455862b.png)

![image](https://user-images.githubusercontent.com/88246010/222205655-15481457-81ef-48af-97fa-9be5dc7094ec.png)

![image](https://user-images.githubusercontent.com/88246010/222205334-2d8727ed-e53f-484b-93ad-341bb8d27c01.png)


* Xgboost and Catboost are best models among all

**Usage**

* Before the following steps make sure you have [git](https://git-scm.com/download), [Anaconda](https://www.anaconda.com/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system

* Clone the complete project with git clone https://github.com/Prabhanshu-08/IPO-Listing-day-gains.git or you can just download the code and unzip it

* Once the project is cloned, open anaconda prompt in the directory where the project was cloned and paste the following block

```
conda create -n ipo_listing_day_gains python=3.8.8
pip install -r requirements.txt
conda activate ipo_listing_day_gains 
```

* And finally run the project with
```python app.py```

**DEMO**

![image](https://user-images.githubusercontent.com/88246010/223772544-7928953d-55cd-4f71-ae6a-9927f7485f3b.png)

Fill all the details mentioned on the page. All these details can be found on either of the links mentioned above. Lets's take an example of 'Burger King' IPO. It has these details:

RI : 68.15

QII : 86.64

NII : 354.11

Issue Price : 60

![image](https://user-images.githubusercontent.com/88246010/223772773-036405ef-2906-4faf-bb34-0016b72b8951.png)



The model predicts listing day gains 126.86% and actual listing day gain was around 130%(pretty close). Offcourse the actual value can never be predicted.

**Further Improvements**

1. The model currently takes only 3 values as input. More relevant coulmns like GMP(Grey Market Premium) can be added to further reduce RMSE.
2. The UI can be made more attractive.
3. A different model can be used for better results.
4. More data needs to be added while training to further reduce RMSE and make predictions more dependable.

**Contact**

If you have any doubt or want to contribute feel free to reach out to be at [LinkedIn](https://www.linkedin.com/in/prabhanshu-gupta-71248118a/)
