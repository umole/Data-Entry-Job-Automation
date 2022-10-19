from get_data import GetData
from enter_data import EnterData

get_data = GetData()
enter_data = EnterData()

address = get_data.get_addresses()
price = get_data.get_prices()
link = get_data.get_links()

for _ in range(len(address)):
    enter_data.input_data(address[_], price[_], link[_])




