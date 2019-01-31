# sqlite3 標準モジュールをインポート
import sqlite3
import hashlib
from datetime import datetime 

# データベースファイルのパス
dbpath = 'data.db'
conn = sqlite3.connect(dbname, check_same_thread=False);
c = conn.cursor();

# データベース接続とカーソル生成
connection = sqlite3.connect(dbpath)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
# connection.isolation_level = None
cursor = connection.cursor()

# エラー処理（例外処理）
try:

except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])


def add_user(username, password):
    try:
        # ENCRYPT(HASH) Password
        encrypted_password = hashlib.sha256( \
                password.encode('utf-8')).hexdigest()
        # Do
        c.execute('INSERT INTO users(name, password) VALUES(?, ?)',\
                (username, encrypted_password));
        conn.commit()
    except sqlite3.Error as e:
        # if Error occured, raise Error(Exception).
raise e

def get_user_by_name(name):
    try:
        c.execute('SELECT * FROM users WHERE name = ?', (name,))
        res = c.fetchone()
        return res
    except sqlite3.Error as e:
        # if Error occured, raise Error(Exception).
raise e

    
def add_tweet(user_id, text):
    try:
        # now is an INTEGER, it treat as UNIX Time.
        now = int(datetime.now().strftime('%s'), 10)
        # Do
        c.execute('INSERT INTO tweets(text, user_id, published_at) VALUES (?, ?, ?)', \
                  (text, user_id, now))
        conn.commit()
    except sqlite3.Error as e:
        # if Error occured, raise Error(Exception).
        raise e


def get_all_tweets():
    try:
        # Tweet's order should be in the newest order.
        c.execute('SELECT * FROM tweets ORDER BY published_at DESC')
        res = c.fetchall()
        return res
    except sqlite3.Error as e:
        # if Error occured, raise Error(Exception).
raise e


# 保存を実行（忘れると保存されないので注意）
connection.commit()

# 接続を閉じる
connection.close()
