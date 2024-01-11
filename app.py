from flask import Flask
from authManager import auth_manager_blueprint
from authVerifier import auth_verifier_blueprint

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(auth_manager_blueprint, url_prefix='/manage')
app.register_blueprint(auth_verifier_blueprint, url_prefix='/verify')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
