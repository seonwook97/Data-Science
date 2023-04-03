# 머신러닝 프로젝트 (졸업 프로젝트)

## 주제

:car:🚥:car::traffic_light:: **고령보행자 사고다발지 도출 및 신 노인보호구역 제안**

![노인](https://user-images.githubusercontent.com/92377162/147870659-2b955df1-124a-454f-b666-8a77c0c26331.png)

* 서울시 노인 교통사고, 고령자 수 매년 꾸준히 증가 -> **노인보호구역** 지정 필요성 증가

* 서울특별시에 위치하는 노인 보호구역은 어린이 보호 구역 대비 **6.3%** 밖에 되지 않음

* **명확하지 않은** 보호구역 지정기준 + **매우 적은 숫자**로 제대로 운영되지 않는 노인보호구역


## 목적

:bulb: **노인 교통사고와 관련된 데이터를 통한 머신러닝 모델링을 통해 新 노인보호구역 도출**


## 데이터

:memo: :memo: :memo:

**1. 14-19년도 사건사고(사망 및 사고 포함)**
   * 용도 : 노인 교통사고에 유의미한 영향을 미치는 요인을 여러 변수들을 통해 분석
   * 구성: 발생지 시군구, 기상상태, 부상정도, 가해자차종, 사고유형, 피해자 연령, 사고유형 대분류 

**2. TASS 교통사고 사망(2012~2018)**
   * 용도 : 14-19년도 사건사고 데이터 분석 특성을 바탕으로 사망 사고 위치 및 기타 변수들에 대해 분석 
   * 구성 : 위도, 경도, 가해자차종, 사고유형 대분류 

**3. 12-19년도 고령자 사고다발지**
   * 용도 : 사망 사고 위치 데이터를 통한 반경 내 노인 교통사고 지역 확인 및 사고 횟수 측정 
   * 구성 : 위도, 경도, 지점명, 부상정도

**4. 서울시 사회복지시설**
   * 용도 : 교통사고 사망 위치 데이터 및 사고다발지 데이터 간 노인 교통사고 연관성 분석 
   * 구성 : 주소


## 과정 및 개요

![전종설](https://user-images.githubusercontent.com/92377162/147871227-6e0d6fa4-e85e-45df-9dfc-d54ec4c8240c.png)

   
## 개발 환경

<div align=left> 
   <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
   <img src="https://img.shields.io/badge/jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white">
   <img src="https://img.shields.io/badge/google colab-F9AB00?style=for-the-badge&logo=google colab&logoColor=white"> 
   <img src="https://img.shields.io/badge/scikit learn-F7931E?style=for-the-badge&logo=scikit learn&logoColor=white"> 
   <br>
</div> 


## 참고문헌 및 자료출처

- 14-19년도 사건사 데이터 / TASS 교통사고분석시스템 / http://taas.koroad.or.kr/
- 12-18년도 사망사고데이터 / TASS 교통사고분석시스템 / http://taas.koroad.or.kr/
- 12-19년도 고령자 사고다발지 / TASS 교통사고분석시스템 / http://taas.koroad.or.kr/
- 서울시 사회복지시설 정보 / 공공데이터 포털 / https://www.data.go.kr/index.do
- 손원표, 이효진. (2021). 초등학교 주변 어린이 보호구역 시범사업의 성과분석 및 개선방안. 교통기술과정 책, 18(1), 87-96.


## 프로젝트 코드 오픈소스 배포

- 정예원 팀원의 깃허브를 이용한 오픈소스 배포
- https://github.com/uomah/Graduation_Project



