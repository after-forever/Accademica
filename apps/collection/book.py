
from logging import exception
import requests


class NonexistentError(Exception):
    ""

class RequestError(Exception):
    ""

class Book():
    __isbn: str
    __title: str
    __author: str
    __publisher: str
    __pubdate: str
    __price: int
    __text_content: str
    __cover: str

    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return self.nqme

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def title(self) -> str:
        return self.__title

    @property
    def author(self) -> str:
        return self.__author

    @property
    def publisher(self) -> str:
        return self.__publisher

    @property
    def pubdate(self) -> str:
        return self.__pubdate

    @property
    def price(self) -> int:
        return self.__price

    @property
    def text_content(self) -> str:
        return self.__text_content

    @property
    def cover(self) -> str:
        return self.__cover

    def create_by_ISBN(self, isbn) -> None:

        url = "https://api.openbd.jp/v1/get"
        payload = {"isbn": isbn}
        try:
            res = requests.get(url, params=payload)
            res.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise RequestError("not found URL: {}".format(url)) from e

        if res.json()[0] == None:
            raise NonexistentError("not found ISBN: {}".format(isbn))

        onix = res.json()[0]["onix"]
        collateral_detail = onix["CollateralDetail"]
        product_supply =  onix["ProductSupply"]
        supply_detail = product_supply["SupplyDetail"]

        self.__text_content = ""
        for text_content in collateral_detail["TextContent"]:
            self.__text_content += text_content["Text"]
            self.__text_content += "\n\n"

        summary = res.json()[0]["summary"]
        self.__title = summary["title"] if "title" in summary else ""
        self.__author = summary["author"] if "author" in summary else ""
        self.__publisher = summary["publisher"] if "publisher" in summary else ""
        self.__pubdate = summary["pubdate"] if "pubdate" in summary else ""
        self.__price = supply_detail["Price"][0]["PriceAmount"] if "Price" in supply_detail else 0
        self.__cover = summary["cover"] if "cover" in summary else ""
