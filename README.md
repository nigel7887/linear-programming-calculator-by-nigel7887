# linear-programming-calculator-by-nigel7887
Linear Programming Calculator by way of Simplex Method
/ 심플렉스 메서드에 의한 선형 계획 문제 계산기


## Source Code and simple exe program
Simplex Method.py
Simplex Method.exe

## Intro
Simple and crude linear programming calculator by using the simplex method.

The following are needed to "fill in" the necessary info needed to complete the formula.

- The terms in each constraint polynomials are to be transposed as so:
1. all variable terms are on the left side,
2. and the constants are placed on the right.

- Type in each inputs corresponding to each question provided by the program.
1. Number of variables
2. Coefficients of each variables
3. Constants

Only integer or decimal number inputs are allowed.

<br/>

KOR - 한국어
심플렉스 메서드를 사용한 선형 계획 문제 계산기

각 제약조건식의 항은 다음과 같이 이항된 상태여야합니다:
1. 변수항은 왼쪽,
2. 상수는 오른쪽.

Exe. 프로그램이 던지는 질문에 따라 다음 인풋 정보가 필요합니다.
1. 변수의 갯수
2. 각 변수항의 계수들
3. 각 식의 상수

오로지 정수 또는 소숫점 숫자 인풋만 허용됩니다.

## Example

A simple integer example => type in each input<br/>
INPUT         &nbsp;&nbsp;&nbsp; KEY<br/>
2 3		        &nbsp;&nbsp;&nbsp; No. of non-basic var's, 	No. of basic var's(<=> no. of constraints) <br/>
3 5 0 0 0  0	&nbsp;&nbsp;&nbsp; Objective Function's coefficients. Last input is constant number (if none, input 0)<br/>
1 0 1 0 0		  &nbsp;&nbsp;&nbsp; First constraint's coefficients<br/>
0 2 0 1 0		  &nbsp;&nbsp;&nbsp; Second constraint's coefficients<br/>
3 2 0 0 1		  &nbsp;&nbsp;&nbsp; Third constraint's coefficients<br/>
...<br/>
4 12 18		    constraints' constants on the right<br/>
<br/>
<br/>
Another Example _ (여유, 잉여, 인공 포함한 인공 문제 확장형)<br/>
3 3<br/>
109.6  89.5  0  0  -100  0   -1200	( = 1.1M-0.4  0.9M-0.5  0  0  -M  0  -12M)<br/>
0.3  0.1  1  0  0  0<br/>
0.5  0.5  0  1  0  0<br/>
0.6  0.4  0  0  -1  1<br/>
...<br/>
2.7  6  6<br/>


한국어
간단 선형계획 예제<br/>
2 3		        &nbsp;&nbsp;&nbsp; 비기저변수갯수	기저변수갯수(즉 제약식 수)<br/>
3 5 0 0 0  0	&nbsp;&nbsp;&nbsp; 목적함수 계수.	마지막 수는 상수(없으면 0)	<br/>
1 0 1 0 0		  &nbsp;&nbsp;&nbsp; 첫 번째 제약식 계수<br/>
0 2 0 1 0		  &nbsp;&nbsp;&nbsp; 두 번째 제약식 계수<br/>
3 2 0 0 1		  &nbsp;&nbsp;&nbsp; 세 번째 제약식 계수<br/>
4 12 18		    &nbsp;&nbsp;&nbsp; 각 제약식 우변<br/>
<br/>
<br/>
방사선 예제 _ (여유, 잉여, 인공 포함한 인공 문제 확장형)<br/>
3 3<br/>
109.6  89.5  0  0  -100  0   -1200	( = 1.1M-0.4  0.9M-0.5  0  0  -M  0  -12M)<br/>
0.3  0.1  1  0  0  0<br/>
0.5  0.5  0  1  0  0<br/>
0.6  0.4  0  0  -1  1<br/>
2.7  6  6<br/>

