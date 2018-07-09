#Web Scapping using BeautifulSoup and Request Lib.
# Script to scrap Flipkart


        from bs4 import BeautifulSoup
		import requests

		#change the link here accordingly
		
		source = requests.get('https://www.flipkart.com/search?q=Mobiles&otracker=start&as-show=off&as=off').text
		
		#Here we used lxml parsing
		soup = BeautifulSoup(source, 'lxml')
		
		#Data output is store in CSV file
		filename = "result.csv"
		
		f = open(filename, "w")
			
		
			header = "Product, Rating, Price, Features \n"
			
			f.write(header)
		       
			 #Got the class name from Inspect elment of the website
			for containers in soup.find_all('div', class_="_1UoZlX"):
			
					name = containers.find('div',class_="_3wU53n")
					#print (name.text)

					rating = soup.find('div',class_="hGSR34 _2beYZw")
					#print (rating.text)

					spec = "" 
					for feature in containers.find_all('li', class_="tVe95H"):
							spec = spec + feature.text + "  "
					#print (spec)


					price = containers.find('div', class_="_1vC4OE _2rQ-NK")
					#print (price.text)

					f.write( name.text.replace(",","|") + "," + rating.text + "," + price.text.replace(","," ")+ "," + spec + "\n")
		f.close()