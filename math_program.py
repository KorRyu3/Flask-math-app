import numpy as np

# エラー処理プログラム ----------------------------------------------

def error(err = ""):
  if err == "" or str(err).isspace():
    return None
  else:
    try:
      err = int(err)
    except TypeError:
      return "TypeError"
    except ValueError:
      return "ValueError"
    except IndexError:
      return "IndexError"
    else:
      n = int(err)
      return n

# ----------------------------------------------------------------

# フィボナッチ数列 --------------------------------------------------

# フィボナッチ数列をn項目まで出力する関数
def fibo(n = ""):

  # error処理
  n = error(n)
  if (n == None or 
      n == "TypeError" or 
      n == "ValueError" or 
      n < 1):
    return "自然数を入力して下さい"
  result = [0, 1]
  for i in range(1, n):
    result.append(result[i - 1] +  result[i])
  del result[0]    # 0番目の要素「0」を削除
  return result

# ----------------------------------------------------------------


# 素数 -----------------------------------------------------------

# 与えられた自然数nに対して、それが素数かどうか判定する関数
def is_prime(n):

  # error処理
  n = error(n)
  if (n == None or 
      n == "TypeError" or 
      n == "ValueError" or
      n < 2):
    return "2以上の値を入力して下さい"

  if ((n == 2) or 
      (n == 3) or 
      (n == 5) or 
      (n == 7) or 
      (n == 11)): 
    return "これは素数です。"
  
  # ↓ 素数を列挙していけばいくだけ処理を高速にすることが可能
  elif ((n == 1) or 
        (n % 2 == 0) or 
        (n % 3 == 0) or 
        (n % 5 == 0) or 
        (n % 7 == 0) or 
        (n % 11 == 0)): 
    return "これは素数ではありません。"
  prime = np.array(range(12, int(n ** 0.5) + 1))  
  prime_idx = (   #下記倍数が"False"のブールインデックスを格納
      ~(
          (prime % 2 == 0)
        | (prime % 3 == 0)
        | (prime % 5 == 0) 
        | (prime % 7 == 0) 
        | (prime % 11 == 0)
      )
  )
  for i in list(prime[prime_idx]):  # 上記倍数を除いたリストを作ることにより処理の高速化が可能
    if n % i == 0:
      return "これは素数ではありません。"  # nがiで割り切れたらFalseを返す
  return "これは素数です。"


# n以下の全ての素数を出力する関数 
def primes(n):   
    # error処理
    n = error(n)
    if (n == None or 
        n == "TypeError" or 
        n == "ValueError" or
        n < 2):
      return "2以上の値を入力して下さい"
    
    n_list = []
    for i in range(2, n + 1):
        if is_prime(i) == "これは素数です。":   # 上記の関数を使用し、n以下の素数を判定
            n_list.append(i)
    return n_list

# ----------------------------------------------------------------


# コラッツ予想 ----------------------------------------------------

# コラッツ予想の手順数と成り立つかどうかの判定プログラム
# 奇数偶数の判定をwhileでまわす。１になったら終わり
def collatz(n = ""):
  
  # error処理
  n = error(n)
  if (n == None or 
      n == "TypeError" or 
      n == "ValueError" or
      n < 1):
    return "自然数を入力して下さい"

  i = 0
  Int = n
  while n > 1:
    if n % 2 == 0:
      n /= 2
    else:
      n = 3 * n + 1
    i += 1
    # print(f"現在の数：{n}")
    # print(f"操作数：{i}回目")
  return f"自然数 '{Int}' はコラッツ予想が成り立ち、{i}回操作をすれば1になります"
  
# ----------------------------------------------------------------


# 英単語登録 -----------------------------------------------------

# 初期英単語
english_words = {"apple": "りんご", "orange": "みかん", "peach": "もも"}

def register():
    
    key = input("英単語を入力してください\n")

    if key in english_words:
        # キーが english_words に登録されている
        return english_words[key]
    else:
        # キーが english_words に登録されていない
        print("この英単語は登録されていません")
        registration = input("登録しますか？ y/n\n")
        if registration == "y" or registration == "yes":
          english_words[key] = input("\"{}\"の日本語訳を入力してください。\n".format(key))
          return "登録が完了しました。"
        else:
          return "登録を中止しました。"
      
# ----------------------------------------------------------------


#　ツェラーの公式 -------------------------------------------------

# 指定した西暦と日付の曜日を表示するプログラム
def day_of_week(year_month_day):
    day_of_week = ["土", "日", "月", "火", "水", "木", "金"]
    
    # error処理
    error_sentence = "西暦と月日を YY/MM/DD の形式で入力して下さい"
    try:
        year_month_day_ls = year_month_day.split("/")
    except ValueError:
        return error_sentence
    else:
        # year_month_day_lsがint型に変換できるかどうかを判定
        for i in year_month_day_ls:
            n = error(i)
            if (n == None or 
                n == "TypeError" or 
                n == "ValueError"):
                return error_sentence
        # year_month_day_lsの要素数が3つかどうかを判定
        if len(year_month_day_ls) != 3:
            return "西暦と月日を YY/MM/DD の形式で入力して下さい"
        year = error(year_month_day_ls[0])
        month = error(year_month_day_ls[1])
        day = error(year_month_day_ls[2])
        # yearが0以下かどうかを判定
        if year < 0:
            return "西暦は正の整数で入力して下さい"
        # monthが1~12の範囲内かどうか、dayが1~31の範囲内かどうかを判定
        if (month > 12 or month < 1 or 
            day > 31 or day < 1):
            return "存在しない日付です."
        
    # 1月と2月は前年の13月と14月として計算する
    if month == 1 or month == 2:
        month += 12
        year -= 1
    # ツェラーの公式
    day_num = (day + (26 * (month + 1) // 10) + year + (year // 4) - (year // 100) + (year // 400)) % 7

    # 1月と2月の変換を元に戻す
    if month == 13 or month == 14:
        month -= 12
        year += 1

    return "{}年{}月{}日は{}曜日です".format(year, month, day, day_of_week[day_num])

# ----------------------------------------------------------------

