from scrapy.spiders import CSVFeedSpider

filename = "CSVSpiderList.txt"
class CSVDataset(CSVFeedSpider):
    name = "CSVSpider"

    start_urls = ["https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv"]
    delimiter = ';'
    quoutechar = '"'

    headers = ['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol','quality']

    def parse_row(self,response,row):

        print("Density = ",row["density"],"\tAlcohol = ",row["alcohol"])

        with open(filename,'a+') as f:
            f.write(row["density"]+"\n")