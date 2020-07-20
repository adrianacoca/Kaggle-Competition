# Kaggle-Competition

**The aim of this project, was to predict the price of diamonds based on its other features through Supervised Machine Learning.**   

The featrues were: 
1. id  
2. carat  
3. cut   
4. color  
5. clarity  
6. depth  
7. table  
8. x  
9. y  
10. z   
  
### Training Model 
**Cleaning the data:**   
Since cut color clarity are of type object, LabelEncode all three columns.   
   
Then create various lists of combinations of features:   
*all features except id* 🌟   
features_0 = ['carat','table','x','y','z','price','color_numeric','cut_numeric', 'clarity_numeric', 'depth']    
  
*getting rid of id, depth* 🌟  
features_1 = ['carat','table','x','y','z','price','color_numeric','cut_numeric', 'clarity_numeric']  
  
*getting rid of id, depth, cut_numeric, clarity_numeric*  
features_2 = ['carat','table','x','y','z','price','color_numeric']  
  
*getting rid of id, x, y, z*  
features_3 = ['carat','table','depth','price','color_numeric','cut_numeric', 'clarity_numeric']  
  
*getting rid of id, depth, cut_numeric, clarity_numeric, table, color_numeric*  
features_4 = ['carat','x','y','z','price']  
  
**Testing Models:** 
I found out the RMSE for various models, trying out the different feature arrangements.   
Regressor Models worked much better than Classifier models. 
1. Decision Tree Classifier   
    RMSE: 1217.41
2. KNeighbors Classifier  
    RMSE: 11693.566
3. Decision Tree Regressor  
    RMSE: 748.275
4. Random Forest Regressor 🌟    
    RMSE: 576.832










