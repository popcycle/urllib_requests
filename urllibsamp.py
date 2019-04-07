from urllib.request import urlretrieve

url = "https://www.data.brisbane.qld.gov.au/data/dataset/b2dbc243-0705-4757-9acf-30f48d6957a0/resource/91b087a1-8d3c-463a-94c0-d3577be6a0dc/download/bcccarpark-2016-03-10th-30th.csv"

urlretrieve(url, 'bcccarpark-2016-03-10th-30th.csv')