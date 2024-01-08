##### 入力・初期化 ###############################################################################################
### 数値を1文字ずつ数値リストにする
a = 123
list(map(int, list(str(a)))) #### [1, 2, 3]

### 数値配列にする
a = 1 2 3
list(map(int, input().split())) #### [1, 2, 3]

### 各変数にする
a = 1 2
a, b  = map(int, input().split()) ### a = 1, b = 2

### 複数初期化
a, b, c = 0, 1, 2

##### 出力 ###############################################################################################
### 変数(複数)
a = 1
b = 2
print(a, b) ### 1 2

### リスト
l = [1, 2, 3]
print(*l) ### 1 2 3 ※returnでは使えない、関数に渡す場合のみ

### format
print("{}と{}".format(1, 2)) ### 1と2

### カンマ区切り(改行せず) ループ処理で使用
print(a, end=",")


##### リスト ###############################################################################################
l = []

### 合計
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

### 指定したインデックスに値を追加(index, value)
l.insert(0, "a")

### 指定したインデックス要素の削除
del l[i]

### 昇順ソート
l.sort() ### lをソートする
l.sort(reverse=False) ### lをソートする
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
# O=nのため、dict()でハッシュ化(O=1)できないか検討した方がいい
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

### リスト内の文字を連結(リストは文字列である必要がある)
''.join(["a", "b", "c"]) ### abc

### 重複要素のみ抽出
l1 = [1, 2]
l2 = [2, 3]

a = list(set(l1) & set (l2)) ### [1] ※listにしないとsetオブジェクトになる

### スライス
a = [0, 1, 2, 3, 4]

# [1, 2] 終了インデックスは含まれない
print(a[1:3])

# [0, 1] 前から指定したインデックス1つ前まで
print(a[:2])

# [2, 3, 4] 指定したインデックスから最後まで
print(a[2:])

### ハッシュセット
s = set()

### 追加
s.add()

### ハッシュマップ
d = dict()

### 追加
d[key] = value

### 指定した値のインデックス取得※
arry = [1, 2, 2, 3]
arry.index(2) ### 1


##### 繰り返し###############################################################################################
## 0スタート
range(3) # 0,1,2

### 1スタート
range(1, 3) # 1,2

### 1スタートで最後+1
range(1, 3+1) # 1,2,3

### 0スタートで増分が2
range(0, 4, 2) # 0, 2

### イテラブルオブジェクトのループ
l = [0, 1, 2]
for v in l:
    print(v) ### 0 1 2

### イテラブルオブジェクトの同時ループ
l = [0, 1, 2]
m = ["a", "b", "c"]
for v1, v2  in zip(l, m):
    print(v1, v2) ### 0 a  1 b  2 c


##### 文字列 ###############################################################################################
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

###　文字列の末尾(負数)を抜き出す
"is2"[-1:] ### 2

### 文字列の末尾(負数)から削除して残す
"is2"[:-1] ### is

### 置換
'1.1.1.1'.replace('.', '[.]') ### 1[.]1[.]1[.]1

### 指定した文字で分割
'あ@あ'.split('@') ### ['あ', 'あ']

### 文字から文字コード取得
ord('a') ### 97

### 文字コードから文字取得
chr(97) ### a

### 指定文字を含むか
"a" in "abc" ### True

### 指定文字の位置
"abc".find("a") ### 0

### テンプレートリテラル
a = 'あ'
b = 'あ'
f"{a}@{b}" ### あ@あ

### 英数字のみか判定
'ABC123'.isalnum() ### True
'ABC-123'.isalnum() ### False

### 小文字
"T".lower() ### t

##### 数値 ###############################################################################################
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

### ユークリッドの互除法(2つの自然数の最大公約数)
import math
a = 1050
b = 300
print(math.gcd(a,b)) ### 150

### 文字コード(ord関数でUnicode取得しaからの相対位置を返す)
ord('c')-ord('a') ### 2

### 小数点桁指定
format(0.00001, '.8f') ### 0.00001000

### 桁指定
f"{0:02d}" ### '00' ※0=桁が満たない場合に先頭を0埋め、2d=2桁の10進数にする

### 絶対値
abs(0-2) ### 2

##### 時間 ###############################################################################################
### 12時間制(12:01:00AM)から24時間制にする(00:01:00)
# https://docs.python.org/ja/3/library/datetime.html
from datetime import datetime
dt = datetime.strptime(s, '%I:%M:%S%p')
    # 24時間制の文字列に変換して返す
    return dt.strftime('%H:%M:%S')