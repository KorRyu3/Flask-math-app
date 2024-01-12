

# 環境準備
## ライブラリのインストール
```bash
$ pip install flask   
$ conda install flask
```

## 環境
- Python 3.10.8
- Flask 2.2.2
- Anaconda 23.7.3
- VS Code 1.81.1

## 実行方法
1. VS CodeのAnaconda環境で、local_web.pyを実行する。
2. ブラウザで、http://127.0.0.1:5000 を開く。


# 取扱説明
## ファイル構成
```
.
├── README.md
├── local_web.py
├── math_program.py
└── templates
    ├── index.html
```

## 使い方
1. ローカルで、local_web.pyを実行する。
2. ブラウザで、http://127.0.0.1:5000 を開く。
3. 実行したい数学プログラムを、プルダウンメニューから選ぶ。
4. "ユーザー入力"に数値のみを入力する。
5. 実行ボタンを押す。
6. 実行結果に表示されたことを確認する。


## プログラムの内容
### math_program.py
- error()： エラー処理を実行する関数
- fibo()：フィボナッチ数列を指定の項数まで出力する関数
- is_prime()：素数かどうかを判定する関数
- primes()：素数を指定の個数まで出力する関数
- collatz()：コラッツ予想の手順数を出力する関数
- --register(): 英単語を登録する関数-- 未実装
- day_of_week(): 指定した日付の曜日を出力する関数


## 備考
- Webサイトを作成するために、Flaskを使用しました。
- プログラムの実行結果を、Webサイトに表示するために、HTMLを使用しました。
- local_web.pyとindex.htmlのプログラムを書く際に、ChatGPT, GitHubCopilot, Code Llammaを一部使用しました。




