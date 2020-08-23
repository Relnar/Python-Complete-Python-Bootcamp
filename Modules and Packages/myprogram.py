from mymodule import my_func
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

def main():
	my_func()
	some_main_script.report_main()
	mysubscript.sub_report()

if __name__ == "__main__":
	main()
