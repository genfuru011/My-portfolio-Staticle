from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """トップページを表示します。"""
    return render_template('index.html')


@app.route('/blog')
def blog():
    """Blogページを表示します。"""
    return render_template('blog.html')

@app.errorhandler(404)
def page_not_found():
    """404エラーページを表示します。"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    # 開発サーバーをデバッグモードで起動
    # ポート番号は必要に応じて変更してください (例: port=5001)
    app.run(debug=True, port=5000)