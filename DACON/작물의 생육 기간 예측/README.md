# 딥러닝 프로젝트 - 스터디 1조 

## 주제

:seedling: **이미지 비교를 통한 작물의 생육 기간 예측**

![tree](https://user-images.githubusercontent.com/92377162/146768921-25b550ff-584c-4e86-b994-2e1950a4acf2.png)

* 4차산업혁명의 시대를 맞아 농업의 분야에서도 AI  기술이 널리 사용되고 있습니다. 

* 스마트팜, IT  기술을 동원하여 더욱 효율적인 작물 재배가 가능해지고 있습니다.

* 작물의 효율적인 생육을 위한 가장 최적의 환경을 도출한다면 식물 재배에 큰 도움이 될 것입니다.


## 목적

:bulb: **식물 생육을 위한 최적의 환경 도출**


## 데이터

:memo: :memo: :memo:

**1. train_dataset [Folder]**
   * 예시) DAT00 ~ DAT01 (1일 차이) / DAT00 ~ DAT02 (2일 차이)


**2. test_dataset [Folder]**

   * idx : 테스트 데이터 인덱스값

   * before_file_path : 이전 사진 이미지 파일명

   * after_file_path : 이후 사진 이미지 파일명


**3. sample_submission.csv**

   * idx : test_data.csv의 index와 매칭

   * time_delta : test_data.csv에서의 before_file_path에 해당하는 이미지부터 after_file_path에 해당하는 이미지까지 식물의 생육기간을 예측


## 개발 환경

<div align=left> 
   <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
   <img src="https://img.shields.io/badge/jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white">
   <img src="https://img.shields.io/badge/google colab-F9AB00?style=for-the-badge&logo=google colab&logoColor=white"> 
   <img src="https://img.shields.io/badge/pytorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"> 
   <br>
</div>


## 노션

:link: <https://seonwook97.notion.site/1-ada66cda850540eabade5a11b0bfa7dc>


## 참조

:link: <https://dacon.io/competitions/official/235851/overview/description>





