# sqlite3 標準モジュールをインポート
import sqlite3

# データベースファイルのパス
dbpath = 'data.db'

# データベース接続とカーソル生成
connection = sqlite3.connect(dbpath)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
# connection.isolation_level = None
cursor = connection.cursor()

# エラー処理（例外処理）
try:

except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])

# 保存を実行（忘れると保存されないので注意）
connection.commit()

# 接続を閉じる
connection.close()
