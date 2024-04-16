import os
import hashlib
from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)


# 不安全的SQL查询，可能导致SQL注入
@app.route('/insecure_sql', methods=['GET'])
def insecure_sql():
    user_id = request.args.get('user_id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id={user_id}"  # SQL注入风险
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return str(result)


# 潜在的跨站脚本攻击（XSS）
@app.route('/xss', methods=['GET'])
def xss():
    user_input = request.args.get('comment', '')
    return render_template_string(f"<html><body>{user_input}</body></html>")  # XSS风险


# 跨站请求伪造（CSRF）的示例，没有CSRF令牌
@app.route('/transfer', methods=['POST'])
def transfer():
    # 假设这是一个转账操作，但没有CSRF保护
    account_from = request.form['from']
    account_to = request.form['to']
    amount = request.form['amount']
    # 执行转账逻辑...
    return "Transfer completed"


# 使用不安全的eval函数
def insecure_eval(expression):
    return eval(expression)  # 不安全的eval使用


# 使用弱加密算法MD5
def weak_encryption(password):
    return hashlib.md5(password.encode()).hexdigest()  # 弱加密算法使用


# 不安全的文件操作，可能导致路径遍历攻击
def insecure_file_operation(file_path):
    with open(file_path, 'r') as file:
        return file.read()  # 路径遍历风险


# 主执行函数，用于演示
if __name__ == '__main__':
    app.run(debug=True)

    # 调用不安全函数示例
    insecure_eval("os.system('ls')")  # 非常危险！执行了系统命令
    weak_hash = weak_encryption('password123')  # 使用弱加密算法加密密码
    print(f"Weak hash: {weak_hash}")
    try:
        content = insecure_file_operation('../../some_secret_file.txt')  # 尝试读取上级目录的文件
        print(f"File content: {content}")
    except FileNotFoundError:
        print("File not found.")