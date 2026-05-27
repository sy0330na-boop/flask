from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    print("홈 주소 진입")
    return render_template("index.html")

# 1. 더하기 처리
@app.route("/calcu/plus", methods=['POST'])
def plus():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result = num1 + num2
    return render_template("result.html", operator="더하기 (+)", num1=num1, num2=num2, result=result)

# 2. 빼기 처리
@app.route("/calcu/minus", methods=['POST'])
def minus():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result = num1 - num2
    return render_template("result.html", operator="빼기 (-)", num1=num1, num2=num2, result=result)

# 3. 곱하기 처리
@app.route("/calcu/multiply", methods=['POST'])
def multiply():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result = num1 * num2
    return render_template("result.html", operator="곱하기 (×)", num1=num1, num2=num2, result=result)

# 4. 나누기 처리 (0으로 나누기 방지 포함)
@app.route("/calcu/divide", methods=['POST'])
def divide():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    
    if num2 == 0:
        result = "공간이 파괴되었습니다. (0으로 나눌 수 없음)"
    else:
        # 소수점 둘째 자리까지 깔끔하게 표기
        result = round(num1 / num2, 2)
        
    return render_template("result.html", operator="나누기 (÷)", num1=num1, num2=num2, result=result)

@app.route("/aa")
def aa():
    print("aa")
    return "aa 페이지입니다."

@app.route("/bb")
def bb():
    print("bb")
    return "bb 페이지입니다."

if __name__ == "__main__":
    app.run(debug=True)