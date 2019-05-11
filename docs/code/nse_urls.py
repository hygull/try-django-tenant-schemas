import requests
from bs4 import BeautifulSoup
import json

url = "https://www.nsenmf.com/NMFIITrxnService/NMFTrxnService/help"
res = requests.get(url)
print(res.status_code)

soup = BeautifulSoup(res.text, "html.parser")
trs = soup.find_all("tr")

data = []
titles =  ["uri", "method", "descirption"]

print(trs)
for tr in trs:

	tds = list(tr.children)
	# ['\n', <td>TRXNREVERSEFEED</td>, '\n', <td title="https://www.nsenmf.com/NMFIITrxnService/NMFTrxnService/TRXNREVERSEFEED">
	# <a href="help/operations/GetTrxnReverseFeed" rel="operation">POST</a>
	# </td>, '\n', <td>Service at https://www.nsenmf.com/NMFIITrxnService/NMFTrxnService/TRXNREVERSEFEED</td>, '\n']

	tds = [td for td in tds if td != '\n']
	# [<td>TRXN_DETAILED_REPORT</td>, <td title="https://www.nsenmf.com/NMFIITrxnService/NMFTrxnService/TRXN_DETAILED_REPORT">
	# <a href="help/operations/TRXN_DETAILED_REPORT" rel="operation">POST</a>
	# </td>, <td>Service at https://www.nsenmf.com/NMFIITrxnService/NMFTrxnService/TRXN_DETAILED_REPORT</td>]

	d = {}

	index = 0
	print("TDS => ", len(tds))
	print(tds)
	for td in tds:
		# print(td.string)
		# print(td is None and td.string == '')
		# print("-" * 60)
		if index == 0:
			# <td>TRXNREVERSEFEED</td>
			d[titles[index]] = td.string # td.text => AttributeError: 'NavigableString' object has no attribute 'text'
		elif index == 1:
			# <td title="https://www.nsenmf.com/NMFIITrxnService/NMFTrxnService/TRXNREVERSEFEED">
			# <a href="help/operations/GetTrxnReverseFeed" rel="operation">POST</a>
			# </td>

			# [td for td in td.contents if td != '\n'] # 'method': [<a href="help/operations/GetTrxnReverseFeed" rel="operation">POST</a>]
			d[titles[index]] = [td for td in td.contents if td != '\n'][0].string # 'method': [<a href="help/operations/GetTrxnReverseFeed" rel="operation">POST</a>]
			print(td, td.title, type(td))
			d["absolute_url"] = td.get("title")
		elif index == 2:
			# <td> Service at https://www.nsenmf.com/NMFIITrxnService/NMFTrxnService/TRXNREVERSEFEED</td>
			d[titles[index]] = td.string
		else:
			print("XTRA")

		index += 1
	data.append(d)

print(json.dumps(data, indent=4))

"""
<td>SYSTRXNREG</td>


<td title="https://www.nsenmf.com/NMFIITrxnService/NMFTrxnService/SYSTRXNREG">
<a href="help/operations/SystematicTransaction" rel="operation">POST</a>
</td>


<td>Service at https://www.nsenmf.com/NMFIITrxnService/NMFTrxnService/SYSTRXNREG</td>




<td>TRXN_DETAILED_REPORT</td>


<td title="https://www.nsenmf.com/NMFIITrxnService/NMFTrxnService/TRXN_DETAILED_REPORT">
<a href="help/operations/TRXN_DETAILED_REPORT" rel="operation">POST</a>
</td>


<td>Service at https://www.nsenmf.com/NMFIITrxnService/NMFTrxnService/TRXN_DETAILED_REPORT</td>




<td>TRXNDETAILSREPORT</td>


<td title="https://www.nsenmf.com/NMFIITrxnService/NMFTrxnService/TRXNDETAILSREPORT">
<a href="help/operations/TRXNDETAILSREPORT" rel="operation">POST</a>
</td>


<td>Service at https://www.nsenmf.com/NMFIITrxnService/NMFTrxnService/TRXNDETAILSREPORT</td>




<td>TRXNREVERSEFEED</td>


<td title="https://www.nsenmf.com/NMFIITrxnService/NMFTrxnService/TRXNREVERSEFEED">
<a href="help/operations/GetTrxnReverseFeed" rel="operation">POST</a>
</td>


<td>Service at https://www.nsenmf.com/NMFIITrxnService/NMFTrxnService/TRXNREVERSEFEED</td>


"""