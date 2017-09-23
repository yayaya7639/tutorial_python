# Chapter 3

20. 余接関数を求める関数cot(theta)を実装せよ．
    - thetaはラジアンで入力されるとする．
21. 平方根を求める関数square_root(x)を実装せよ．
22. サイコロシミュレータ関数を実装せよ．
    - 出目は1-6でそれぞれの出目の確率は同様に確からしいとする．
    - (一度の実行で1-6の整数が1つ返る関数を作成する．）
23. 整数0から100までの一様乱数をn個のリストを返す関数random_nを実装せよ．
    - 整数nは標準入力で受け取る．
24. 標準入力から数値列を受け取り，その平均と標準偏差を標準出力せよ．
    - 例題
      - 入力: `81.65 97.52 95.25 92.98 86.18 88.45`
      - 出力: `平均: 90.34, 標準偏差: 5.46`
25. 2次元ベクトルを入力して，それを行列Aで変換した値を出力する関数transA(x)を実装せよ．
    - 行列Aは固定で，`A=[[1, 3], [7, 6]]`
    - Axを返す関数を設計する．
    - 例題
      - 入力: `2 3`
      - 出力: `11 32`
26. 25を書き換えて，行列Aも入力として受け取るような形にせよ．
    - ベクトルの次元数d，変換後の次元数mとする．
    - 入力フォーマットは次のようにする．
      ```
      d m
      e1 e2 ... ed
      A11 A12 ... A1d
      A21 A22 ... A2d
      :
      Am1 Am2 ... Amd
      ```
    - 例題
      - 入力: 
        ```
        2 3
        1 7
        2 4 
        1 7
        10 4
        ```
      - 出力:
        ```
        30 50 38
        ```
27. 標準入力で，点数を表す数値nと各点の座標(x, y)を受け取り，それらの間の距離を全て求め，行列表記で返せ．
    - 行列の(i,j)要素はi番目とj番目の点のユークリッド距離とする．
      - ユークリッド距離は小数点以下4桁まで出力
    - 入力される座標の各要素は実数である．
    - 例題
      - 入力:
        ```	
    	3
	1 2
    	1 3
    	2 3
    	```	  
      - 出力:
	```
    	0.0000 1.0000 1.4142
    	1.0000 0.0000 1.0000
    	1.4142 1.0000 0.0000
    	```
28. 27で作った関数の実行速度を計測し，それよりも高速な手法を検討せよ．
    - 実行速度を求めるために，データサイズを工夫した入力例を作るとよい．
    - また，1回の実行速度ではなく10回以上の実行の平均速度を使う．
29. πを求める関数calculat_piを実装せよ．
    - math.piなど円周率をすでに計算された値を使ってはいけない．