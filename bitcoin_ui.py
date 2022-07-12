import requests

import tkinter as tk

from datetime import datetime


url = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={},JPY,EUR"


def get_price (currency):

	try:

		response = requests.get(url.format("BTC", currency)).json()				#Crypto currency is here
		return response
	except:

		return False

def output (y) :
	while True:

		date_time = datetime.now()
		date_time = date_time.strftime("%d/%m/%y %H:%M:%S")
	
		currentprice = get_price(y)

		if currentprice:
			return (date_time , currentprice)

print("[INR]"  "[USD]"  "[EUR]"  "[CNY]"  "[CAD]"  "[AUD]")	
def main (canvas):
	default_currency_list = ["INR" , "USD" , "EUR" , "CNY" , "CAD" , "AUD"]
	print(default_currency_list)
	currency_input= textField.get()
	print(f"Input Is {currency_input}")

	for x in default_currency_list :
		if currency_input == "INR" :

				date_time , currentprice = output(currency_input)
				final_data = (str(currentprice[currency_input]))
				label1.config(text = str("Rs - " + final_data))
				label2.config(text = str ("As on - " + date_time))
				break



		elif currency_input == "USD" :
			date_time , currentprice = output(currency_input)
			final_data = (str(currentprice[currency_input]))
			label1.config(text = str("US $ " + final_data))
			label2.config(text = str ("As on - " + date_time))
			break
				

		elif currency_input == "EUR" :
			date_time , currentprice = output(currency_input)
			final_data = (str(currentprice[currency_input]))
			label1.config(text = str("EUROS " + final_data))
			label2.config(text = str ("As on - " + date_time))
			break

		elif currency_input == "CNY" :
			date_time , currentprice = output(currency_input)
			final_data = (str(currentprice[currency_input]))
			label1.config(text = str("Chinese Yuan " + final_data))
			label2.config(text = str ("As on - " + date_time))
			break
		elif currency_input == "CAD" :
			date_time , currentprice = output(currency_input)
			final_data = (str(currentprice[currency_input]))
			label1.config(text = str("Canadian $ " + final_data))
			label2.config(text = str ("As on - " + date_time))
			break
		elif currency_input == "AUD" :
			date_time , currentprice = output(currency_input)
			final_data = (str(currentprice[currency_input]))
			label1.config(text = str("Australian $ " + final_data))
			label2.config(text = str ("As on - " + date_time))
			break
					
			
	else :
		print("Wrong Input")


canvas = tk.Tk()
canvas.geometry("600x300")
canvas.title("Bitcoin App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

# default_currency_list = ["INR" , "USD" , "EUR" , "CNY" , "CAD" , "AUD"]
# label3.config(text = str(default_currency_list))
# label3 = tk.Label(canvas, font=t)
# label3.pack()


textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()

textField.bind('<Return>', main).upper()
# currency_input = textField.get()
label1 = tk.Label(canvas, font=t)
label1.pack()



label2 = tk.Label(canvas, font=f)
label2.pack()


canvas.mainloop()



		

