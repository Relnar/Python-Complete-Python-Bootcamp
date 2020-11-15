import zipfile
import shutil
import os

def main():
	f = open('fileone.txt', 'w+')
	f.write('ONE FILE')
	f.close()
	f = open('filetwo.txt', 'w+')
	f.write('TWO FILE')
	f.close()

	# Zip files
	comp_file = zipfile.ZipFile('comp_file.zip', 'w')
	comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
	comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
	comp_file.close()

	# Extract all files in a zip
	zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
	zip_obj.extractall('extracted_content')
	zip_obj.close()

	# Zip whole folder
	dir_to_zip = os.path.abspath('extracted_content')
	output_filename = 'example'
	shutil.make_archive(output_filename, 'zip', dir_to_zip)

	# Unzip whole folder
	shutil.unpack_archive('example.zip', 'final_unzip', 'zip')


if __name__ == "__main__":
	main()