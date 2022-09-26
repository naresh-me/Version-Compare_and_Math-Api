from importlib.resources import Resource
import this
from flask import Flask
import statistics
import numpy as np
import sys
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class MathApi(Resource):
    @app.route("/min/<numbers>/<int:quantifier>")
    def min(numbers, quantifier):
        # numsArray = self.strngToIntArray(numbers)
        numbers = str(numbers).strip('[')
        numbers = numbers.strip(']')
        numsArray = [int(x) for x in numbers.split(',')]
        minQuantifierRes = SubsetsRec().getAllMin(
            numsArray, len(numsArray), [], quantifier)
        return str(minQuantifierRes)
        # return self.mathFunction(numbers=numbers, quantifier=quantifier, funcType="minQuantifier")

    @app.route("/max/<strngNumber>/<int:quantifier>")
    def max(strngNumber, quantifier):
        # numsArray = self.strngToIntArray(numbers)
        strngNumber = str(strngNumber).strip('[')
        strngNumber = strngNumber.strip(']')
        numsArray = [int(x) for x in strngNumber.split(',')]
        maxQuantifierRes = SubsetsRec().getAllMax(
            numsArray, len(numsArray), [], quantifier)
        return str(maxQuantifierRes)
        # return self.mathFunction(numbers=numbers, quantifier=quantifier, funcType="maxQuantifier")

    @app.route("/avg/<strngNumber>")
    def avg(strngNumber):
        # numsArray = self.strngToIntArray(numbers)
        strngNumber = str(strngNumber).strip('[')
        strngNumber = strngNumber.strip(']')
        numsArray = [int(x) for x in strngNumber.split(',')]
        avgRes = round(sum(numsArray) / len(numsArray), 2)
        return str(avgRes)
        # return self.mathFunction(numbers=numbers,  funcType="avg")

    @app.route("/median/<strngNumber>")
    def median(strngNumber):
        strngNumber = str(strngNumber).strip('[')
        strngNumber = strngNumber.strip(']')
        numsArray = [int(x) for x in strngNumber.split(',')]
        # numsArray = self.strngToIntArray(numbers)
        mediamResult = statistics.median(numsArray)
        return str(mediamResult)
        # return self.mathFunction(numbers=numbers, funcType="median")

    @app.route("/percentile/<strngNumber>/<int:quantifier>")
    def percentile(strngNumber, quantifier):
        strngNumber = str(strngNumber).strip('[')
        strngNumber = strngNumber.strip(']')
        numsArray = [int(x) for x in strngNumber.split(',')]
        # numsArray = self.strngToIntArray(numbers)
        percentileRes = np.percentile(numsArray, quantifier)
        return str(percentileRes)
        # return self.mathFunction(numbers=numbers, quantifier=quantifier, funcType="percentile")

    def mathFunction(self, numbers, quantifier, funcType):
        numsArray = self.strngToIntArray(numbers)
        if funcType == "percentile":
            percentileRes = np.percentile(numsArray, quantifier)
            return str(percentileRes)
        elif funcType == "median":
            mediamResult = statistics.median(numsArray)
            return str(mediamResult)
        elif funcType == "avg":
            avgRes = round(sum(numsArray) / len(numsArray), 2)
            return str(avgRes)
        elif funcType == "maxQuantifier":
            maxQuantifierRes = round(sum(numsArray) / len(numsArray), 2)
            return str(maxQuantifierRes)
        elif funcType == "minQuantifier":
            # print(numsArray)
            minQuantifierRes = self.getAllSubsetsRec(
                numsArray, len(numsArray), [], quantifier)
            return str(minQuantifierRes)

    def strngToIntArray(strngNumber):
        # print(type(strngNumber))
        strngNumber = str(strngNumber).strip('[')
        strngNumber = strngNumber.strip(']')
        intArray = [int(x) for x in strngNumber.split(',')]
        return intArray


class SubsetsRec:
    def getAllMin(self, intArry, arryLen, tempArry, sum):

        if (sum == 0):
            return len(tempArry)
        if (sum < 0):
            return sys.maxsize
        if (arryLen == 0):
            return sys.maxsize

        x = self.getAllMin(intArry, arryLen - 1, tempArry, sum)

        tempArry.append(intArry[arryLen - 1])
        y = self.getAllMin(intArry, arryLen, tempArry,
                           sum - intArry[arryLen - 1])
        tempArry.pop(len(tempArry) - 1)

        return min(x, y)

    def getAllMax(self, intArry, arryLen, tempArry, sum):

        if (sum == 0):
            return len(tempArry)
        if (sum < 0):
            return 0
        if (arryLen == 0):
            return 0

        x = self.getAllMax(intArry, arryLen - 1, tempArry, sum)

        tempArry.append(intArry[arryLen - 1])
        y = self.getAllMax(intArry, arryLen, tempArry,
                           sum - intArry[arryLen - 1])
        tempArry.pop(len(tempArry) - 1)

        return max(x, y)


api.add_resource(MathApi, '/')

if __name__ == '__main__':
    app.run(debug=True)
