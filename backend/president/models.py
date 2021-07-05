from common.models import Reader, Printer, FileDTO
import pandas as pd
from icecream import ic


class Service(Reader):
    url = 'http://info.nec.go.kr/main/showDocument.xhtml?electionId=0000000000&topMenuId=VC&secondMenuId=VCCP09'

    def __init__(self):
        self.f = FileDTO()
        self.r = Reader()
        self.p = Printer()

    def mapspr(self):
        f = self.f
        r = self.r

        f.context = './saved_data/'
        f.fname = 'presidentdata.xlsx'
        pd.read_excel(f, header=1,usecols=3)


if __name__ == '__main__':
    s = Service()
    ic(s.mapspr())