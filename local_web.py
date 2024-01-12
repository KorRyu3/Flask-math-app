

# ローカルで動くWebサイトを作り、そこに自前のPythonプログラムを実装する

# 1. ローカルで動くWebサイトを作る
from flask import Flask, render_template, request
from math_program import *

app = Flask(__name__)

# プログラムの選択肢を定義
program_choices = {
    'fibo': 'フィボナッチ数列',
    'is_prime': '素数判定',
    'primes': 'n以下の素数を列挙',
    'collatz': 'コラッツ予想',
    # 'register': '英単語登録',
    'day_of_week': '西暦と日付の曜日を表示',
}

# ルートURLにアクセスしたときの処理
@app.route('/', methods=['GET', 'POST'])
def home():
    selected_program = None
    result = None
    user_input = None

    if request.method == 'POST':
        selected_program = request.form.get('program_select')
        print(selected_program)
        # placeholder = program_select_placeholder(selected_program)
        if selected_program:
            # ユーザーからの入力を取得
            user_input = request.form.get('user_input')

            # プルダウンメニューから選択されたプログラムに応じて実行
            result = run_selected_program(selected_program, user_input)

    # ウェブページのテンプレートにプルダウンメニュー、ユーザー入力フォーム、および実行結果を渡す
    return render_template('index.html', program_choices=program_choices, selected_program=selected_program, user_input=user_input, result=result)



# 選択されたプログラムを実行する関数
def run_selected_program(program_name, user_input):

    if program_name == 'fibo':
        # プログラム1の実行
        result = fibo(user_input)

    elif program_name == 'is_prime':
        # プログラム2の実行
        result = is_prime(user_input)

    elif program_name == 'primes':
        # プログラム3の実行
        result = primes(user_input)

    elif program_name == 'collatz':
        # プログラム4の実行
        result = collatz(user_input)
    # elif program_name == 'register':
    #     # プログラム5の実行
    #     result = register()

    elif program_name == 'day_of_week':
        # プログラム6の実行
        result = day_of_week(user_input)

    else:
        result = "未知のプログラム"

    return result





if __name__ == '__main__':
    app.run(debug=True)


