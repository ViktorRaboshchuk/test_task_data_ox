from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    django command to be run using shell that downloads all data to DB
    """
    def handle(self, **options):
        import yfinance as yf
        from yahoo_data.models import HistoricalData

        tickets = "PD ZUO PINS ZM PVTL DOCU CLDR RUN"

        for ticker in list(tickets.split(" ")):
            data = yf.download(
                tickers="{}".format(ticker),
                period="max",
                interval="1d",
                group_by="ticker",
                auto_adjust=False,
                prepost=True,
                threads=True,
                proxy=None,
            )

            for row in data.itertuples():

                ticker_hist_row = HistoricalData.objects.create(
                    ticker=ticker,
                    date=row.__getattribute__("Index"),
                    open=row.__getattribute__("Open"),
                    high=row.__getattribute__("High"),
                    low=row.__getattribute__("Low"),
                    close=row.__getattribute__("Close"),
                    adj_close=row.__getattribute__("_5"),
                    volume=row.__getattribute__("Volume"),
                )
