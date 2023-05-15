import matplotlib
import matplotlib.font_manager as fm
import dataProcess as dP
import sys

input = lambda:sys.stdin.readline()

fm._get_fontconfig_fonts()
font_location = "./NanumGothic.ttf"
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

def main():
    print("정보를 알고 싶은 단어를 공백으로 구분하여, 자음-쌍자음 순으로 입력하세요.")
    print("예시 : 공짜 꽁짜")
    
    # word1, word2 = input().split(" ")
    word1, word2 = "", ""
    
    
    dP.searchRatio_all(word1, word2)
    dP.searchRatio_generation(word1, word2)

if __name__ == '__main__':
    main()