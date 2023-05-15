import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import naverAPI

def searchRatio_all(word1, word2):
    df = naverAPI.apiCall(word1, word2)
    
    # Set graph size
    plt.figure(figsize=(10,5))


    # Set x-axis and y-axis data
    x = df.index
    xShow = df['date']
    y1 = df['ratio1']
    y2 = df['ratio2']


    # Draw the graph
    plt.scatter(xShow, y1, label=word1)
    plt.scatter(xShow, y2, label=word2)
    
    x_reshape = x.values.reshape(-1, 1)

    # Fit a linear regression model to the data for each search term
    reg1 = LinearRegression().fit(x_reshape, y1)
    reg2 = LinearRegression().fit(x_reshape, y2)
    

    # Calculate R-squared values for each model
    r2_first = r2_score(y1, reg1.predict(x_reshape))
    reg2_coefficient = reg2.coef_[0]
    reg2_intercept = reg2.intercept_
    

    # Draw the linear regression lines on the graph
    plt.plot(xShow, reg1.predict(x_reshape), label='{}, $R^2={:.2f}$'.format(word1, r2_first), color="red", linewidth="4")
    plt.plot(xShow, reg2.predict(x_reshape), label='{} : {:.2f}% → {:.2f}%'.format(word2, reg2_intercept*100, (reg2_coefficient*384 + reg2_intercept)*100), color="blue", linewidth="4")

    plt.xticks(np.arange(0,384,60))

    # Set labels, title, and legend
    plt.xlabel('점 1개는 1주일을 뜻함 (2016 1월 - 2023 5월)')
    plt.ylabel('비율')
    plt.title('시간에 따른 NAVER 검색 시의 어두경음화 발현 양상 변화')
    plt.legend()

    # Set y-axis limits and format the ticks as percentages
    plt.ylim([0, 1])
    plt.gca().yaxis.set_major_formatter('{:.0%}'.format)

    # Show the plot
    plt.show()
    
    

    
def searchRatio_generation(word1, word2):
    df = naverAPI.apiCall_generation(word1, word2)
    
    # Set graph size
    plt.figure(figsize=(10,5))

    # print(df)
    # Set x-axis and y-axis data
    x = df.index
    xShow = df['date']
    y1 = df['ratio10']
    y2 = df['ratio20']
    y3 = df['ratio30']
    y4 = df['ratio40']
    y5 = df['ratio50']
    y6 = df['ratio60']
    
    x_reshape = x.values.reshape(-1, 1)

    # Fit a linear regression model to the data for each search term
    reg1 = LinearRegression().fit(x_reshape, y1)
    reg2 = LinearRegression().fit(x_reshape, y2)
    reg3 = LinearRegression().fit(x_reshape, y3)
    reg4 = LinearRegression().fit(x_reshape, y4)
    reg5 = LinearRegression().fit(x_reshape, y5)
    reg6 = LinearRegression().fit(x_reshape, y6)
    
    reg1_coefficient = reg1.coef_[0]
    reg1_intercept = reg1.intercept_
    
    reg2_coefficient = reg2.coef_[0]
    reg2_intercept = reg2.intercept_

    reg3_coefficient = reg3.coef_[0]
    reg3_intercept = reg3.intercept_

    reg3_coefficient = reg3.coef_[0]
    reg3_intercept = reg3.intercept_

    reg4_coefficient = reg4.coef_[0]
    reg4_intercept = reg4.intercept_

    reg5_coefficient = reg5.coef_[0]
    reg5_intercept = reg5.intercept_

    reg6_coefficient = reg6.coef_[0]
    reg6_intercept = reg6.intercept_

    # Calculate R-squared values for each model
    r2_first = r2_score(y1, reg1.predict(x_reshape))
    r2_second = r2_score(y2, reg2.predict(x_reshape))
    r2_third = r2_score(y3, reg3.predict(x_reshape))
    r2_fourth = r2_score(y4, reg4.predict(x_reshape))
    r2_fifth = r2_score(y5, reg5.predict(x_reshape))
    r2_sixth = r2_score(y6, reg6.predict(x_reshape))
    

    # Draw the linear regression lines on the graph
    plt.plot(xShow, reg1.predict(x_reshape), label='10대 이하 : {:.2f}% → {:.2f}%'.format(reg1_intercept*100, (reg1_coefficient*89 + reg1_intercept)*100), color="red", linewidth="5")
    plt.plot(xShow, reg2.predict(x_reshape), label='20대 : {:.2f}% → {:.2f}%'.format(reg2_intercept*100, (reg2_coefficient*89 + reg2_intercept)*100), color="orange", linewidth="5")
    plt.plot(xShow, reg3.predict(x_reshape), label='30대 : {:.2f}% → {:.2f}%'.format(reg3_intercept*100, (reg3_coefficient*89 + reg3_intercept)*100), color="yellow", linewidth="5")
    plt.plot(xShow, reg4.predict(x_reshape), label='40대 : {:.2f}% → {:.2f}%'.format(reg4_intercept*100, (reg4_coefficient*89 + reg4_intercept)*100), color="green", linewidth="5")
    plt.plot(xShow, reg5.predict(x_reshape), label='50대 : {:.2f}% → {:.2f}%'.format(reg5_intercept*100, (reg5_coefficient*89 + reg5_intercept)*100), color="blue", linewidth="5")
    plt.plot(xShow, reg6.predict(x_reshape), label='60대 이상 : {:.2f}% → {:.2f}%'.format(reg6_intercept*100, (reg6_coefficient*89 + reg6_intercept)*100), color="purple", linewidth="5")

    plt.xticks(np.arange(0,89,17))

    # Set labels, title, and legend
    plt.xlabel('검색어 : {}  _ 월간 변화량 (2016 1월 - 2023 5월)'.format(word2))
    plt.ylabel('비율')
    plt.title('세대 차이별 시간에 따른 NAVER 검색 시의 어두경음화 발현 양상 변화')
    plt.legend()

    # Set y-axis limits and format the ticks as percentages

    plt.ylim([0,1])
    plt.gca().yaxis.set_major_formatter('{:.0%}'.format)

    # Show the plot
    plt.show()