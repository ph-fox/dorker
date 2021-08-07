import os, argparse, time
parser = argparse.ArgumentParser()
parser.add_argument('-d','--dork',help="Enter your dork")
parser.add_argument('-a','--amount',help="Enter amount of site to printout")
arg = parser.parse_args()

class Dorker:
	def __init__(self, dork, amount):
	 self.dork = dork
	 self.amount = amount

	def check_requirements(self):
		try:
		 from googlesearch import search
		 if(self.dork is None and self.amount is None):
		  print(f'Usage: python3 {os.path.basename(__file__)} -d <dork> -a <amount>')
		  exit()
		 else:
		  dork.searcher(search)
		except ModuleNotFoundError:
		 print("Installing Required Module!..")
		 os.system("pip3 install googlesearch-python")
		except Exception as err:
		 print("Error: {}".format(err))
	def searcher(self,search):
		count=0
		print("="*14+"-Dorking-"+"="*14)
		print()
		for site in search(self.dork, num_results=int(self.amount)):
		 count+=1
		 print(f'({count}):  {site}')
		 time.sleep(.1)
		print()
		print("="*14+"Done"+"="*14)

if __name__=="__main__":
 print("""
888~-_                   888   _                    
888   \\   e88~-_  888-~\\ 888 e~ ~   e88~~8e  888-~\\ 
888    | d888   i 888    888d8b    d888  88b 888    
888    | 8888   | 888    888Y88b   8888__888 888    
888   /  Y888   ' 888    888 Y88b  Y888    , 888    
888_-~    "88_-~  888    888  Y88b  "88___/  888    

DORKER BY: Anikin Luke
 """)
 dork = Dorker(arg.dork, arg.amount)
 dork.check_requirements()
