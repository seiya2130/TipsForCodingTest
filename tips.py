## 入力
### 数値を1文字ずつ数値リストにする
a = 123
list(map(int, list(str(a)))) #### [1, 2, 3]

### 数値配列にする
a = 1 2 3
list(map(int, input().split())) #### [1, 2, 3]

### 各変数にする
a = 1 2
a, b  = map(int, input().split()) ### a = 1, b = 2


## 出力
### 変数(複数)
a = 1
b = 2
print(a, b) ### 1 2

### リスト
l = [1, 2, 3]
print(*l) ### 1 2 3 


## リスト
l = []

### 合計
from numpy import *
sum(l)

### 長さ
len(l)

### 最大値
max(l)

### 要素の追加
l.append(1)

### 指定した値のインデックス
i = 1
l.index(i)

### 指定したインデックス要素の削除
del l[i]

### 昇順ソート
l.sort() ### lをソートする
sorted(l) ## lをソートした新しいリストを返す

### 降順ソート
l.sort(reverse=True) ### lを逆ソートする
sorted(l, reverse=True) ### lを逆ソートした新しいリストを返す

### 重複削除(その後リストにする)
list(set(l))

### 反転
l.reverse() ### lを反転させる
list(reversed(l)) ### lを反転して新しいリストを返す

### 特定文字のカウント
l.count("a")

### リストの末尾の値
l[-1]

### 二次元配列の長さ(リスト化する)
[len(v) for v in l]

## リストの半分
nums = [1, 2, 3, 4, 5, 6]
nums[:len(nums) // 2] ### [1, 2, 3]
nums[len(nums) // 2:] ### [4, 5, 6]

### 配列のマージ
l3 = l1 + l2

### 配列の初期化(複数値)
l = [0] * 3 ### [0, 0, 0]


## 繰り返し
## 0スタート
range(3) # 0,1,2

### 1スタート
range(1, 3) # 1,2

### 1スタートで最後+1
range(1, 3+1) # 1,2,3

### 0スタートで増分が2
range(0, 4, 2) # 0, 2


## 文字列
### 前方一致
"abc".startswith("ab") # True

### 前方から一致文字を削除(連続する限り)
"aabc".lstrip("a") # bc

### 後方一致
"abc".endswith("bc") # True

### 後方から一致文字を削除(連続する限り)
"abc".rstrip("c") # ab

### 指定文字数文先頭から削除
"abccc"[2:] ### ccc(2文字削除)

### 指定文字数文後方から削除して残す
"abccc"[:2] ### ab(3文字削除)

### 置換
'1.1.1.1'.replace('.', '[.]') ### 1[.]1[.]1[.]1


## 数値
### 割り算(余り切り捨て)
5 // 2 ### 2

### 累乗
4 ** 3 ### 64

### 最大値
max(1, 2, 3) ### 3

### 最小値
min(1, 2) ### 1

### 配列の積(numpyは数値計算用の拡張モジュール)
import numpy as np
np.prod(l)
