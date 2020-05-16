import pandas as pd
import matplotlib.pyplot as plt
def replace_yes(cell):
    if cell=="yes":
        return 1
    return 0
df = pd.read_csv('C:/Users/PRUSTY/Desktop/DS_ML_Task1/DS_ML_Task1/student-math.csv', converters = {
    'schoolsup':replace_yes,
    'famsup': replace_yes,
    'paid':replace_yes,
    'activities':replace_yes,
    'nursery':replace_yes,
    'higher':replace_yes,
    'internet':replace_yes,
    'romantic':replace_yes,
})
col = df.loc[: , "G1":"G3"]
df['final_grade'] = col.mean(axis=1)
df = df.drop(['G1','G2','G3'], axis=1)
df.to_csv('C:/Users/PRUSTY/Desktop/DS_ML_Task1/DS_ML_Task1/Output_final_grade.csv')
plt.subplot(1,2,1)
plt.title('Scatter plot')
colors = [1.0,2.0,3.0,4.0]
plt.scatter(df.studytime, df.final_grade, c=df.studytime)
plt.xlabel('studytime--->')
plt.ylabel('final_grade--->')
plt.subplot(1,2,2)
plt.title('Box_Plot')
box_plot = df.boxplot(column=['final_grade', 'studytime'])
plt.show()
