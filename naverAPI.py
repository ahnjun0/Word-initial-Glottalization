import pandas as pd
import urllib.request
import json
from clientInfo import *

# 참고사항 : https://seo.tbwakorea.com/blog/naver-seo-api-searching-data/

info = clientInfo()

client_id = info.CLIENT_ID
client_secret = info.CLIENT_SECRET

url = "https://openapi.naver.com/v1/datalab/search"

weekdata = ['2015-12-28', '2016-01-04', '2016-01-11', '2016-01-18', '2016-01-25', '2016-02-01', '2016-02-08', '2016-02-15', '2016-02-22', '2016-02-29', '2016-03-07', '2016-03-14', '2016-03-21', '2016-03-28', '2016-04-04', '2016-04-11', '2016-04-18', '2016-04-25', '2016-05-02', '2016-05-09', '2016-05-16', '2016-05-23', '2016-05-30', '2016-06-06', '2016-06-13', '2016-06-20', '2016-06-27', '2016-07-04', '2016-07-11', '2016-07-18', '2016-07-25', '2016-08-01', '2016-08-08', '2016-08-15', '2016-08-22', '2016-08-29', '2016-09-05', '2016-09-12', '2016-09-19', '2016-09-26', '2016-10-03', '2016-10-10', '2016-10-17', '2016-10-24', '2016-10-31', '2016-11-07', '2016-11-14', '2016-11-21', '2016-11-28', '2016-12-05', '2016-12-12', '2016-12-19', '2016-12-26', '2017-01-02', '2017-01-09', '2017-01-16', '2017-01-23', '2017-01-30', '2017-02-06', '2017-02-13', '2017-02-20', '2017-02-27', '2017-03-06', '2017-03-13', '2017-03-20', '2017-03-27', '2017-04-03', '2017-04-10', '2017-04-17', '2017-04-24', '2017-05-01', '2017-05-08', '2017-05-15', '2017-05-22', '2017-05-29', '2017-06-05', '2017-06-12', '2017-06-19', '2017-06-26', '2017-07-03', '2017-07-10', '2017-07-17', '2017-07-24', '2017-07-31', '2017-08-07', '2017-08-14', '2017-08-21', '2017-08-28', '2017-09-04', '2017-09-11', '2017-09-18', '2017-09-25', '2017-10-02', '2017-10-09', '2017-10-16', '2017-10-23', '2017-10-30', '2017-11-06', '2017-11-13', '2017-11-20', '2017-11-27', '2017-12-04', '2017-12-11', '2017-12-18', '2017-12-25', '2018-01-01', '2018-01-08', '2018-01-15', '2018-01-22', '2018-01-29', '2018-02-05', '2018-02-12', '2018-02-19', '2018-02-26', '2018-03-05', '2018-03-12', '2018-03-19', '2018-03-26', '2018-04-02', '2018-04-09', '2018-04-16', '2018-04-23', '2018-04-30', '2018-05-07', '2018-05-14', '2018-05-21', '2018-05-28', '2018-06-04', '2018-06-11', '2018-06-18', '2018-06-25', '2018-07-02', '2018-07-09', '2018-07-16', '2018-07-23', '2018-07-30', '2018-08-06', '2018-08-13', '2018-08-20', '2018-08-27', '2018-09-03', '2018-09-10', '2018-09-17', '2018-09-24', '2018-10-01', '2018-10-08', '2018-10-15', '2018-10-22', '2018-10-29', '2018-11-05', '2018-11-12', '2018-11-19', '2018-11-26', '2018-12-03', '2018-12-10', '2018-12-17', '2018-12-24', '2018-12-31', '2019-01-07', '2019-01-14', '2019-01-21', '2019-01-28', '2019-02-04', '2019-02-11', '2019-02-18', '2019-02-25', '2019-03-04', '2019-03-11', '2019-03-18', '2019-03-25', '2019-04-01', '2019-04-08', '2019-04-15', '2019-04-22', '2019-04-29', '2019-05-06', '2019-05-13', '2019-05-20', '2019-05-27', '2019-06-03', '2019-06-10', '2019-06-17', '2019-06-24', '2019-07-01', '2019-07-08', '2019-07-15', '2019-07-22', '2019-07-29', '2019-08-05', '2019-08-12', '2019-08-19', '2019-08-26', '2019-09-02', '2019-09-09', '2019-09-16', '2019-09-23', '2019-09-30', '2019-10-07', '2019-10-14', '2019-10-21', '2019-10-28', '2019-11-04', '2019-11-11', '2019-11-18', '2019-11-25', '2019-12-02', '2019-12-09', '2019-12-16', '2019-12-23', '2019-12-30', '2020-01-06', '2020-01-13', '2020-01-20', '2020-01-27', '2020-02-03', '2020-02-10', '2020-02-17', '2020-02-24', '2020-03-02', '2020-03-09', '2020-03-16', '2020-03-23', '2020-03-30', '2020-04-06', '2020-04-13', '2020-04-20', '2020-04-27', '2020-05-04', '2020-05-11', '2020-05-18', '2020-05-25', '2020-06-01', '2020-06-08', '2020-06-15', '2020-06-22', '2020-06-29', '2020-07-06', '2020-07-13', '2020-07-20', '2020-07-27', '2020-08-03', '2020-08-10', '2020-08-17', '2020-08-24', '2020-08-31', '2020-09-07', '2020-09-14', '2020-09-21', '2020-09-28', '2020-10-05', '2020-10-12', '2020-10-19', '2020-10-26', '2020-11-02', '2020-11-09', '2020-11-16', '2020-11-23', '2020-11-30', '2020-12-07', '2020-12-14', '2020-12-21', '2020-12-28', '2021-01-04', '2021-01-11', '2021-01-18', '2021-01-25', '2021-02-01', '2021-02-08', '2021-02-15', '2021-02-22', '2021-03-01', '2021-03-08', '2021-03-15', '2021-03-22', '2021-03-29', '2021-04-05', '2021-04-12', '2021-04-19', '2021-04-26', '2021-05-03', '2021-05-10', '2021-05-17', '2021-05-24', '2021-05-31', '2021-06-07', '2021-06-14', '2021-06-21', '2021-06-28', '2021-07-05', '2021-07-12', '2021-07-19', '2021-07-26', '2021-08-02', '2021-08-09', '2021-08-16', '2021-08-23', '2021-08-30', '2021-09-06', '2021-09-13', '2021-09-20', '2021-09-27', '2021-10-04', '2021-10-11', '2021-10-18', '2021-10-25', '2021-11-01', '2021-11-08', '2021-11-15', '2021-11-22', '2021-11-29', '2021-12-06', '2021-12-13', '2021-12-20', '2021-12-27', '2022-01-03', '2022-01-10', '2022-01-17', '2022-01-24', '2022-01-31', '2022-02-07', '2022-02-14', '2022-02-21', '2022-02-28', '2022-03-07', '2022-03-14', '2022-03-21', '2022-03-28', '2022-04-04', '2022-04-11', '2022-04-18', '2022-04-25', '2022-05-02', '2022-05-09', '2022-05-16', '2022-05-23', '2022-05-30', '2022-06-06', '2022-06-13', '2022-06-20', '2022-06-27', '2022-07-04', '2022-07-11', '2022-07-18', '2022-07-25', '2022-08-01', '2022-08-08', '2022-08-15', '2022-08-22', '2022-08-29', '2022-09-05', '2022-09-12', '2022-09-19', '2022-09-26', '2022-10-03', '2022-10-10', '2022-10-17', '2022-10-24', '2022-10-31', '2022-11-07', '2022-11-14', '2022-11-21', '2022-11-28', '2022-12-05', '2022-12-12', '2022-12-19', '2022-12-26', '2023-01-02', '2023-01-09', '2023-01-16', '2023-01-23', '2023-01-30', '2023-02-06', '2023-02-13', '2023-02-20', '2023-02-27', '2023-03-06', '2023-03-13', '2023-03-20', '2023-03-27', '2023-04-03', '2023-04-10', '2023-04-17', '2023-04-24', '2023-05-01']

def apiCall(search, search2):
    
    # Create an empty DataFrame with columns "date", "ratio1", and "ratio2"
    # to_DataFrame = pd.DataFrame(columns=["date", "ratio1", "ratio2"])
    to_DataFrame = pd.DataFrame(columns=["date", "ratio1", "ratio2"])

    
    body = '{\
        \"startDate\":\"2016-01-01\",\
        \"endDate\":\"2023-05-07\",\
        \"timeUnit\":\"week\",\
        \"keywordGroups\":[{\"groupName\":\"'+search+'\",\"keywords\":[\"'+search+'\"]},\
                            {\"groupName\":\"'+search2+'\",\"keywords\":[\"'+search2+'\"]}]\
        }'
        
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    request.add_header("Content-Type", "application/json")

    response = urllib.request.urlopen(request, data=body.encode("utf-8"))

    rescode = response.getcode()
    # print(rescode)

    if rescode == 200:
        response_body = response.read()
        response_data = response_body.decode("utf-8")
        
        result = json.loads(response_data) # type : <class 'dict'>
    

        date1 = [a["period"] for a in result["results"][0]["data"]]
        ratio_data1 = []


        if len(result["results"][0]["data"]) == 384:
            ratio_data1 = [a["ratio"] for a in result["results"][0]["data"]]
            
        elif len(result["results"][0]["data"]) == 0:
            ratio_data1 = [0] * 384
        
        else:
            tmp_versus = [x for x in weekdata if x not in date1]
            tmp_index = []
            for i in tmp_versus:
                tmp_index.append(tmp_versus.index(i))
            
            ratio_data1 = [a["ratio"] for a in result["results"][0]["data"]]
                
            for i in tmp_index:
                ratio_data1.insert(i, 0)


        
        date2 = [a["period"] for a in result["results"][1]["data"]]
        # print(date2)
        ratio_data2 = []
        
        if len(result["results"][1]["data"]) == 384:
            ratio_data2 = [a["ratio"] for a in result["results"][1]["data"]]
            
        elif len(result["results"][1]["data"]) == 0:
            ratio_data2 = [0] * 384
        
        else:
            tmp_versus = [x for x in weekdata if x not in date2]
            # print("DATE2")
            # print(date2)
            
            # print("tmp_Versus")
            # print(tmp_versus)
            
            tmp_index = []
            for i in tmp_versus:
                tmp_index.append(tmp_versus.index(i))
            
            ratio_data2 = [a["ratio"] for a in result["results"][1]["data"]]
            
            # print(tmp_index)
            for i in tmp_index:
                ratio_data2.insert(i, 0)


        # print(ratio_data2)
        # print("date1 = {}, date2 = {}, weekdata = {}, ratio_data2 = {}".format(len(date1), len(date2), len(weekdata), len(ratio_data2)))

        to_DataFrame = pd.DataFrame({"date": weekdata, "search1": ratio_data1, "search2": ratio_data2})

        # Calculate the ratio of search1 and search2 for each date
        to_DataFrame['ratio1'] = to_DataFrame['search1'] / (to_DataFrame['search1'] + to_DataFrame['search2'])
        to_DataFrame['ratio2'] = to_DataFrame['search2'] / (to_DataFrame['search1'] + to_DataFrame['search2'])

        to_DataFrame = to_DataFrame.drop('search1', axis=1)
        to_DataFrame = to_DataFrame.drop('search2', axis=1)

        return to_DataFrame

    elif __name__ == "__main__":
        print("Error Code:" + rescode)


gene = [["ratio10", ["1","2"]], ["ratio20",["3","4"]], ["ratio30",["5","6"]], ["ratio40",["7","8"]], ["ratio50",["9","10"]], ["ratio60",["11","11"]]]
monthdata = ['2016-01-01', '2016-02-01', '2016-03-01', '2016-04-01', '2016-05-01', '2016-06-01', '2016-07-01', '2016-08-01', '2016-09-01', '2016-10-01', '2016-11-01', '2016-12-01', '2017-01-01', '2017-02-01', '2017-03-01', '2017-04-01', '2017-05-01', '2017-06-01', '2017-07-01', '2017-08-01', '2017-09-01', '2017-10-01', '2017-11-01', '2017-12-01', '2018-01-01', '2018-02-01', '2018-03-01', '2018-04-01', '2018-05-01', '2018-06-01', '2018-07-01', '2018-08-01', '2018-09-01', '2018-10-01', '2018-11-01', '2018-12-01', '2019-01-01', '2019-02-01', '2019-03-01', '2019-04-01', '2019-05-01', '2019-06-01', '2019-07-01', '2019-08-01', '2019-09-01', '2019-10-01', '2019-11-01', '2019-12-01', '2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01', '2020-10-01', '2020-11-01', '2020-12-01', '2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01', '2021-07-01', '2021-08-01', '2021-09-01', '2021-10-01', '2021-11-01', '2021-12-01', '2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01', '2022-06-01', '2022-07-01', '2022-08-01', '2022-09-01', '2022-10-01', '2022-11-01', '2022-12-01', '2023-01-01', '2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01']

def apiCall_generation(search, search2):
    
    # Create an empty DataFrame with columns "date", "ratio1", and "ratio2"
    to_DataFrame = pd.DataFrame(columns=["date", gene[0][0], gene[1][0], gene[2][0], gene[3][0], gene[4][0], gene[5][0]])
    for gen in gene:
        
        if gen[0] != "ratio60":
            body = '{\
                \"startDate\":\"2016-01-01\",\
                \"endDate\":\"2023-05-07\",\
                \"timeUnit\":\"month\",\
                \"keywordGroups\":[{\"groupName\":\"'+search+'\",\"keywords\":[\"'+search+'\"]},\
                                    {\"groupName\":\"'+search2+'\",\"keywords\":[\"'+search2+'\"]}],\
                \"ages\":[\"'+gen[1][0]+'\", \"'+gen[1][1]+'\"]\
                }'
        else:
                        body = '{\
                \"startDate\":\"2016-01-01\",\
                \"endDate\":\"2023-05-07\",\
                \"timeUnit\":\"month\",\
                \"keywordGroups\":[{\"groupName\":\"'+search+'\",\"keywords\":[\"'+search+'\"]},\
                                    {\"groupName\":\"'+search2+'\",\"keywords\":[\"'+search2+'\"]}],\
                \"ages\":[\"'+gen[1][0]+'\"]\
                }'

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        request.add_header("Content-Type", "application/json")

        response = urllib.request.urlopen(request, data=body.encode("utf-8"))

        rescode = response.getcode()
        # print(rescode)

        if rescode == 200:
            response_body = response.read()
            response_data = response_body.decode("utf-8")

            result = json.loads(response_data) # type : <class 'dict'>


            date1 = [a["period"] for a in result["results"][0]["data"]]
            
            ratio_data1 = []
            

            if len(result["results"][0]["data"]) == 89:
                ratio_data1 = [a["ratio"] for a in result["results"][0]["data"]]
                    
            elif len(result["results"][0]["data"]) == 0:
                ratio_data1 = [0] * 89
                
            else:
                tmp_versus = [x for x in monthdata if x not in date1]
                tmp_index = []
                for i in tmp_versus:
                    tmp_index.append(tmp_versus.index(i))
                
                ratio_data1 = [a["ratio"] for a in result["results"][0]["data"]]
                
                for i in tmp_index:
                    ratio_data1.insert(i, 0)

            # print(ratio_data1)
        
            date2 = [a["period"] for a in result["results"][1]["data"]]
            ratio_data2 = []
        
            if len(result["results"][1]["data"]) == 89:
                ratio_data2 = [a["ratio"] for a in result["results"][1]["data"]]
                
            elif len(result["results"][1]["data"]) == 0:
                ratio_data2 = [0] * 89
                
            else:
                tmp_versus = [x for x in monthdata if x not in date2]
                tmp_index = []
                for i in tmp_versus:
                    tmp_index.append(tmp_versus.index(i))
                
                ratio_data2 = [a["ratio"] for a in result["results"][1]["data"]]
                
                for i in tmp_index:
                    ratio_data2.insert(i, 0)

                        
            # print(gen[0])
            # print(ratio_data1)
            # print(ratio_data2)
            
            # print(date)
            # print(to_DataFrame)
            
            to_DataFrame["date"] = monthdata
            to_DataFrame["search1"] = ratio_data1
            to_DataFrame["search2"] = ratio_data2
            # to_DataFrame = pd.DataFrame({"date": date, "search1": ratio_data1, "search2": ratio_data2})

            # Calculate the ratio of search1 and search2 for each date
            to_DataFrame[gen[0]] = to_DataFrame['search2'] / (to_DataFrame['search1'] + to_DataFrame['search2'])

            # print(to_DataFrame)
            
            to_DataFrame = to_DataFrame.drop('search1', axis=1)
            to_DataFrame = to_DataFrame.drop('search2', axis=1)
            
            # print(gen[0])
            # print(to_DataFrame)
            
        elif __name__ == "__main__":
            print("Error Code:" + rescode)
            
            
    return to_DataFrame

