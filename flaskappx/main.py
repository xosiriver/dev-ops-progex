from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

num_to_roman = {
        1: "I",
    5: "V",
    4: "IV",
    10: "X",
    9: "IX",
    50: "L",
    40: "XL",
    100: "C",
    90: "XC",
    500: "D",
    400: "CD",
    1000: "M",
    900: "CM",
}

roman_to_num = {
   "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
}

def to_roman_numeral(num):
    r = ""
    keys = sorted(num_to_roman.keys(), reverse=True)
    if num == 0:
        return "nulla"   #special case1
    for key in keys:
        while num >= key:
            r += num_to_roman[key]
            num -= key
    
    if any(r[i:i+4] == r[i]*4 for i in range(len(r) - 4 + 1)):
        return "!!!This number cannot be represented by traditional roman numerals!!!"
    
    return r

def to_arabic_number(numeral):
    anum = 0
    for e, i in enumerate(numeral):
        if e < len(numeral) - 1:
            if roman_to_num[i] >= roman_to_num[numeral[e + 1]]:
                anum += roman_to_num[i]
            else:
                anum -= roman_to_num[i]
        else:
            anum += roman_to_num[i]

    return anum

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/convert', methods=['POST'])
def convert():
    input_number = int(request.form.get('inputNumber'))
    input_roman = request.form.get('inputRoman')

    converted_number = to_arabic_number(input_roman) if input_roman else input_number
    converted_roman = to_roman_numeral(input_number) if input_number else input_roman

    response_data = {
        'convertedNumber': converted_number,
        'convertedRoman': converted_roman
    }

    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)
